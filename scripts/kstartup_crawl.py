#!/usr/bin/env python3
"""K-Startup announcement crawler — bundled with the ir-search skill.

Accesses only public announcement pages (currently-recruiting list).
No login, no private areas. A polite delay is applied between requests.

Usage:
  # Collect ALL currently-recruiting announcements (JSONL)
  python3 kstartup_crawl.py list -o kstartup_all.jsonl

  # Same, dropping items whose deadline is already past
  python3 kstartup_crawl.py list -o kstartup_all.jsonl --drop-expired

  # Save detail-page text (for eligibility verification)
  python3 kstartup_crawl.py detail 178481 178215 -o details/

HTTP handling (TLS-fingerprint escalation, block detection, retry, delay) lives in
fetchlib.py next to this file. Dependency: curl_cffi>=0.15 recommended; falls back
to urllib with an install hint when blocked.
"""
import argparse
import html as htmllib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetchlib import Blocked, Fetcher, is_past, strip_html  # noqa: E402

BASE = "https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do"
DETAIL_URL = BASE + "?schM=view&pbancSn={sn}"
DELAY = 0.3  # seconds between requests (politeness)


def log(msg):
    print(f"[ir-search] {msg}", file=sys.stderr)


def parse_list(html):
    """Extract announcement records from a list page.

    Only the main list (id=bizPbancList) is parsed — the carousel at the top
    repeats featured announcements, so it is discarded. The real list holds
    15 items per page.
    """
    items = []
    parts = html.split('id="bizPbancList"', 1)
    if len(parts) < 2:
        return items
    body = parts[1]
    for blk in re.split(r'<li class="notice">|<li >|<li>', body)[1:]:
        m = re.search(r"go_view\((\d+)\)", blk)
        if not m:
            continue

        def g(pat):
            mm = re.search(pat, blk)
            return re.sub(r"\s+", " ", mm.group(1)).strip() if mm else ""

        lists = [
            re.sub(r"\s+", " ", x).strip()
            for x in re.findall(r'<span class="list"><i[^>]*></i>([^<]+)</span>', blk)
        ]

        def pick(prefix):
            for x in lists:
                if x.startswith(prefix):
                    return x.replace(prefix, "").strip()
            return ""

        items.append(
            {
                "pbancSn": m.group(1),
                "category": htmllib.unescape(
                    g(r'<span class="flag type\d+">\s*([^<]+)</span>')
                ),
                "dday": g(r'<span class="flag day">\s*([^<]+)</span>'),
                "title": htmllib.unescape(g(r'<p class="tit">\s*([^<]+)')),
                "program": htmllib.unescape(lists[0]) if lists else "",
                "org": htmllib.unescape(lists[1]) if len(lists) > 1 else "",
                "start": pick("시작일자"),
                "deadline": pick("마감일자"),
                "agency_type": g(r'<span class="flag_agency">\s*([^<]+)</span>'),
                "url": DETAIL_URL.format(sn=m.group(1)),
            }
        )
    return items


def cmd_list(args):
    fetcher = Fetcher(delay=DELAY)
    log(f"fetch backend: {fetcher.backend_name}")
    seen = {}
    page = 1
    while page <= args.max_pages:
        try:
            status, html = fetcher.get(f"{BASE}?page={page}&schStr=&pbancEndYn=N")
        except Blocked as e:
            log(f"page {page}: {e} — stopping; report K-Startup as '수동 확인' if nothing was collected")
            break
        if status != 200:
            log(f"page {page}: HTTP {status} — stopping")
            break
        items = parse_list(html)
        if not items and page == 1:
            log("page 1: HTTP 200 but 0 items parsed — site layout changed or soft-blocked; check the HTML")
        new = [i for i in items if i["pbancSn"] not in seen]
        for i in items:
            seen[i["pbancSn"]] = i
        log(f"page {page}: {len(items)} parsed, {len(new)} new, total {len(seen)}")
        if not items or not new:
            break  # past the last page only carousel items remain → 0 new
        page += 1

    records = list(seen.values())
    if args.drop_expired:
        kept = [r for r in records if not is_past(r.get("deadline"))]
        log(f"drop-expired: {len(records) - len(kept)} past-deadline items removed")
        records = kept
    with open(args.output, "w", encoding="utf-8") as f:
        for i in records:
            f.write(json.dumps(i, ensure_ascii=False) + "\n")
    log(f"saved: {args.output} ({len(records)} items)")


def cmd_detail(args):
    fetcher = Fetcher(delay=DELAY)
    os.makedirs(args.output, exist_ok=True)
    for sn in args.pbancSn:
        if not sn.isdigit():
            log(f"ignoring invalid announcement id: {sn}")
            continue
        try:
            status, html = fetcher.get(DETAIL_URL.format(sn=sn))
            if status != 200:
                log(f"{sn}: HTTP {status}")
                continue
            path = os.path.join(args.output, f"{sn}.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(DETAIL_URL.format(sn=sn) + "\n\n" + strip_html(html))
            log(f"{sn}: saved → {path}")
        except Blocked as e:
            log(f"{sn}: {e} — record as '수동 확인'")
        except Exception as e:  # noqa: BLE001 — skip failures, keep going
            log(f"{sn}: error {e}")


def main():
    ap = argparse.ArgumentParser(description="K-Startup announcement crawler (ir-search)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="collect all currently-recruiting announcements")
    p_list.add_argument("-o", "--output", default="kstartup_all.jsonl")
    p_list.add_argument("--max-pages", type=int, default=40)
    p_list.add_argument(
        "--drop-expired", action="store_true", help="drop items whose deadline is already past"
    )
    p_list.set_defaults(func=cmd_list)

    p_det = sub.add_parser("detail", help="save detail-page text")
    p_det.add_argument("pbancSn", nargs="+", help="announcement id(s)")
    p_det.add_argument("-o", "--output", default="details")
    p_det.set_defaults(func=cmd_detail)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
