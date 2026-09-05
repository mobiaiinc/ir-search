import datetime as dt
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import fetchlib  # noqa: E402


class FakeBackend:
    """Stand-in for _CurlBackend: blocked fingerprints answer 403, others 200."""

    name = "curl_cffi"

    def __init__(self, impersonate, blocked=(), body="<html>ok</html>", fail_first=0):
        self.impersonate = impersonate
        self.blocked = set(blocked)
        self.body = body
        self.calls = []
        self.fail_first = fail_first

    def request(self, url, data, timeout):
        if self.fail_first:
            self.fail_first -= 1
            raise ConnectionError("reset")
        self.calls.append((self.impersonate, url, data))
        if self.impersonate in self.blocked:
            return 403, "<html>Access Denied</html>"
        return 200, self.body

    def rotate(self, impersonate):
        self.impersonate = impersonate


def make(backend):
    f = fetchlib.Fetcher(delay=0, log=lambda m: None)
    f.backend = backend
    return f


class EscalationTests(unittest.TestCase):
    def setUp(self):
        self._sleep = fetchlib.time.sleep
        fetchlib.time.sleep = lambda s: None

    def tearDown(self):
        fetchlib.time.sleep = self._sleep

    def test_ladder_order_and_stickiness(self):
        b = FakeBackend("safari", blocked={"safari", "safari_ios"})
        f = make(b)
        status, _ = f.get("https://www.k-startup.go.kr/list")
        self.assertEqual(status, 200)
        self.assertEqual([c[0] for c in b.calls], ["safari", "safari_ios", "chrome"])
        f.get("https://www.k-startup.go.kr/list?page=2")
        self.assertEqual(b.calls[-1][0], "chrome")  # starts from the working fingerprint
        self.assertEqual(len(b.calls), 4)

    def test_challenge_body_is_a_block_and_mobile_is_last(self):
        b = FakeBackend("safari", body="<title>Attention Required! | Cloudflare</title>")
        f = make(b)
        with self.assertRaises(fetchlib.Blocked) as cm:
            f.get("https://www.bizinfo.go.kr/x")
        self.assertEqual(len(cm.exception.tried), 5)
        self.assertIn("m.bizinfo.go.kr", b.calls[-1][1])

    def test_no_mobile_variant_for_non_www_host(self):
        b = FakeBackend("safari", blocked=set(fetchlib.IMPERSONATE_LADDER))
        f = make(b)
        with self.assertRaises(fetchlib.Blocked) as cm:
            f.get("https://nipa.kr/home/2-2")
        self.assertEqual(len(cm.exception.tried), 4)

    def test_post_data_passes_through(self):
        b = FakeBackend("safari")
        f = make(b)
        f.post("https://www.kocca.kr/list.do", data={"pageIndex": "2"})
        self.assertEqual(b.calls[-1][2], {"pageIndex": "2"})

    def test_network_error_is_retried(self):
        b = FakeBackend("safari", fail_first=1)
        f = make(b)
        self.assertEqual(f.get("https://www.x.go.kr/")[0], 200)

    def test_network_error_gives_up_after_retries(self):
        b = FakeBackend("safari", fail_first=10)
        f = make(b)
        with self.assertRaises(ConnectionError):
            f.get("https://www.x.go.kr/")

    def test_urllib_backend_has_single_step(self):
        class U(FakeBackend):
            name = "urllib"
            impersonate = None

        b = U(None)
        f = make(b)
        steps = list(f._steps("https://www.x.go.kr/"))
        self.assertEqual(steps[0], ("https://www.x.go.kr/", None))
        self.assertEqual(len(steps), 2)  # www + mobile


class BlockDetectionTests(unittest.TestCase):
    def test_statuses(self):
        for s in (403, 412, 429, 503):
            self.assertTrue(fetchlib.looks_blocked(s, ""))
        self.assertFalse(fetchlib.looks_blocked(200, "<html>공고</html>"))
        self.assertFalse(fetchlib.looks_blocked(404, ""))

    def test_markers_only_in_head(self):
        self.assertTrue(fetchlib.looks_blocked(200, "<html>접근이 차단되었습니다</html>"))
        far = "x" * 5000 + "Access Denied"
        self.assertFalse(fetchlib.looks_blocked(200, far))


class DateTests(unittest.TestCase):
    T = dt.date(2026, 9, 5)

    def test_norm_date_forms(self):
        for raw in ("2026.07.10", "2026-07-10", "2026/07/10", "2026년 7월 10일", "2026.07.10(금) 18:00", "26.07.10"):
            self.assertEqual(fetchlib.norm_date(raw), "2026-07-10", raw)
        self.assertEqual(fetchlib.norm_date("상시"), "상시")
        self.assertEqual(fetchlib.norm_date(""), "")

    def test_is_past(self):
        self.assertTrue(fetchlib.is_past("2026-09-04", self.T))
        self.assertFalse(fetchlib.is_past("2026-09-05", self.T))
        self.assertFalse(fetchlib.is_past("2026-09-06", self.T))
        for keep in ("", "상시", "예산 소진 시까지", "2026-13-40"):
            self.assertFalse(fetchlib.is_past(keep, self.T), keep)

    def test_strip_html(self):
        out = fetchlib.strip_html("<script>x()</script><p>신청대상:&nbsp;예비창업자</p><style>a{}</style>")
        self.assertIn("신청대상", out)
        self.assertNotIn("x()", out)


if __name__ == "__main__":
    unittest.main()
