#!/usr/bin/env python3
"""Shared HTTP layer for the ir-search crawlers.

One place for everything the individual crawlers used to duplicate:

  * backend selection   — curl_cffi (browser TLS fingerprint) with a urllib fallback
  * escalation ladder   — on a block signal, rotate the TLS fingerprint
                          safari → safari_ios → chrome → chrome_android, then try the
                          mobile host variant (www. → m.) once; give up loudly after that
  * block detection     — HTTP status *and* body markers ("Access Denied", challenge
                          pages). A 200 with a challenge body is not a success.
  * retry / backoff     — transient network errors are retried (2s, 4s, …)
  * politeness delay    — enforced between requests by the fetcher itself, so callers
                          never forget it

Only public pages are fetched. This module never bypasses logins or CAPTCHAs: when the
ladder is exhausted it raises `Blocked` so the crawler can report "manual check" instead.

Usage (inside a crawler):

    from fetchlib import Fetcher, Blocked
    f = Fetcher(delay=0.3)
    status, html = f.get(url)
    status, html = f.post(url, data={"pageIndex": "2"})
"""
import re
import sys
import time
import urllib.parse

IMPERSONATE_LADDER = ("safari", "safari_ios", "chrome", "chrome_android")

# Status codes that mean "the WAF did not like this client", not "page missing".
BLOCK_STATUSES = frozenset({403, 405, 406, 412, 429, 503})

# Body markers seen on WAF / challenge pages. Checked case-insensitively on the
# first 4 KB of the body only (a real announcement page never opens with these).
BLOCK_MARKERS = (
    "access denied",
    "request rejected",
    "the requested url was rejected",
    "cf-challenge",
    "challenge-platform",
    "attention required",
    "captcha",
    "접근이 차단",
    "비정상적인 접근",
    "허용되지 않은 접근",
    "자동화된 요청",
)

DEFAULT_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15"
)


class Blocked(Exception):
    """Raised when every escalation step was tried and the site still refuses."""

    def __init__(self, url, tried):
        self.url = url
        self.tried = list(tried)
        super().__init__(f"blocked after trying {', '.join(self.tried)}: {url}")


def looks_blocked(status, text):
    """True when the response is a WAF/challenge answer rather than the page."""
    if status in BLOCK_STATUSES:
        return True
    head = (text or "")[:4096].lower()
    return any(m in head for m in BLOCK_MARKERS)


def mobile_variant(url):
    """`https://www.example.go.kr/x` → `https://m.example.go.kr/x`; None if not applicable."""
    p = urllib.parse.urlsplit(url)
    if not p.netloc.startswith("www."):
        return None
    return urllib.parse.urlunsplit((p.scheme, "m." + p.netloc[4:], p.path, p.query, p.fragment))


class _CurlBackend:
    name = "curl_cffi"

    def __init__(self, impersonate):
        from curl_cffi import requests as cr  # imported lazily: optional dependency

        self._cr = cr
        self.impersonate = impersonate
        self.session = cr.Session(impersonate=impersonate)

    def request(self, url, data, timeout):
        if data is None:
            r = self.session.get(url, timeout=timeout)
        else:
            r = self.session.post(url, data=data, timeout=timeout)
        return r.status_code, r.text

    def rotate(self, impersonate):
        self.impersonate = impersonate
        self.session = self._cr.Session(impersonate=impersonate)


class _UrllibBackend:
    name = "urllib"
    impersonate = None

    def request(self, url, data, timeout):
        import urllib.error
        import urllib.request

        body = urllib.parse.urlencode(data).encode() if data is not None else None
        req = urllib.request.Request(url, data=body, headers={"User-Agent": DEFAULT_UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:  # keep the status; a 403 is a signal, not a crash
            return e.code, e.read().decode("utf-8", "replace") if e.fp else ""

    def rotate(self, impersonate):  # urllib has nothing to rotate
        pass


class Fetcher:
    """HTTP client with the escalation ladder, retry, and politeness delay built in."""

    def __init__(
        self,
        delay=0.3,
        timeout=30,
        retries=2,
        ladder=IMPERSONATE_LADDER,
        mobile_fallback=True,
        log=None,
    ):
        self.delay = delay
        self.timeout = timeout
        self.retries = retries
        self.ladder = tuple(ladder)
        self.mobile_fallback = mobile_fallback
        self._log = log or (lambda msg: print(f"[ir-search] {msg}", file=sys.stderr))
        self._last_request = 0.0
        self.backend = self._make_backend()

    # -- backend --------------------------------------------------------------

    def _make_backend(self):
        try:
            return _CurlBackend(self.ladder[0])
        except ImportError:
            self._log("fetch backend: urllib (pip install 'curl_cffi>=0.15' if requests get blocked)")
            return _UrllibBackend()

    @property
    def backend_name(self):
        return self.backend.name

    # -- public API -----------------------------------------------------------

    def get(self, url):
        return self.fetch(url)

    def post(self, url, data):
        return self.fetch(url, data=data)

    def fetch(self, url, data=None):
        """Return (status, text). Raises `Blocked` when the ladder is exhausted."""
        tried = []
        for step_url, impersonate in self._steps(url):
            if impersonate is not None and impersonate != self.backend.impersonate:
                self._log(f"escalating TLS fingerprint → {impersonate}")
                self.backend.rotate(impersonate)
            label = f"{impersonate or self.backend.name}@{'m.' if step_url != url else 'www'}"
            tried.append(label)
            status, text = self._request_with_retry(step_url, data)
            if not looks_blocked(status, text):
                return status, text
            self._log(f"block signal (HTTP {status}) with {label}: {step_url[:80]}")
        raise Blocked(url, tried)

    # -- internals ------------------------------------------------------------

    def _steps(self, url):
        """Yield (url, impersonate) pairs in escalation order."""
        if self.backend.name == "curl_cffi":
            # start from the fingerprint currently in use, then the rest of the ladder
            current = self.backend.impersonate
            order = [current] + [x for x in self.ladder if x != current]
        else:
            order = [None]
        for imp in order:
            yield url, imp
        if self.mobile_fallback:
            m = mobile_variant(url)
            if m:
                yield m, order[0]

    def _request_with_retry(self, url, data):
        attempt = 0
        while True:
            self._politeness()
            try:
                return self.backend.request(url, data, self.timeout)
            except Exception as e:  # noqa: BLE001 — network-level errors only reach here
                attempt += 1
                if attempt > self.retries:
                    raise
                wait = 2 ** attempt
                self._log(f"network error ({type(e).__name__}: {e}); retry in {wait}s")
                time.sleep(wait)

    def _politeness(self):
        gap = time.monotonic() - self._last_request
        if gap < self.delay:
            time.sleep(self.delay - gap)
        self._last_request = time.monotonic()


def norm_date(s):
    """Normalize date-ish strings to YYYY-MM-DD; return the cleaned input if not parseable.

    Handles '2026.07.10', '2026-07-10', '2026/07/10', '2026년 7월 10일' and the
    two-digit-year form '26.07.10' that KOCCA uses.
    """
    import html as htmllib

    s = re.sub(r"\s+", " ", htmllib.unescape(s or "")).strip()
    m = re.search(r"(\d{4})[.\-/년\s]+(\d{1,2})[.\-/월\s]+(\d{1,2})", s)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    m = re.search(r"(?<!\d)(\d{2})[.\-/](\d{1,2})[.\-/](\d{1,2})", s)  # 26.07.10
    if m:
        return f"20{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return s


def is_past(date_str, today=None):
    """True only when *date_str* parses to a date strictly before today.

    Unparseable / empty strings return False: an unknown deadline must never be
    silently dropped — it stays in the list marked as unknown.
    """
    import datetime as _dt

    d = norm_date(date_str)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
        return False
    try:
        parsed = _dt.date.fromisoformat(d)
    except ValueError:
        return False
    return parsed < (today or _dt.date.today())


def strip_html(text):
    """Detail-page HTML → plain text (scripts/styles dropped, tags → newlines)."""
    import html as htmllib

    text = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", "", text)
    text = re.sub(r"<[^>]+>", "\n", text)
    text = htmllib.unescape(text)
    return re.sub(r"\n\s*\n+", "\n", text)
