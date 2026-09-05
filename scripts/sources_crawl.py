#!/usr/bin/env python3
"""Multi-source crawler for Korean government support-program announcements.

Part of the ir-search skill. Covers sources beyond K-Startup
(see kstartup_crawl.py for the K-Startup crawler):

  bizinfo  Bizinfo (기업마당) — largest aggregated portal, all ministries/regions
  nipa     NIPA (정보통신산업진흥원) — AI/ICT programs
  kocca    KOCCA (한국콘텐츠진흥원) — content-industry programs
  smtech   SMTECH (중소기업 기술개발사업) — SME R&D calls

Only public announcement pages are accessed; no login, no private areas.
A polite delay is applied between requests.

Usage:
  python3 sources_crawl.py list bizinfo -o bizinfo.jsonl --max-pages 20 --drop-expired
  python3 sources_crawl.py list all -o all_sources.jsonl
  python3 sources_crawl.py detail <URL> <URL> -o details/

Unified JSONL schema:
  {"source", "id", "title", "field", "org", "apply_start", "apply_end",
   "reg_date", "url"}

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
from fetchlib import Blocked, Fetcher, is_past, norm_date, strip_html  # noqa: E402

DELAY = 0.4  # seconds between requests (politeness)


def log(msg):
    print(f"[ir-search] {msg}", file=sys.stderr)


def clean(s):
    return re.sub(r"\s+", " ", htmllib.unescape(s or "")).strip()


def split_period(s):
    """Split '2026-07-07 ~ 2026-07-17'-style ranges into (start, end)."""
    parts = re.split(r"~|∼", s)
    if len(parts) == 2:
        return norm_date(parts[0]), norm_date(parts[1])
    return "", norm_date(s)


# --------------------------------------------------------------------------
# Per-source parsers. Each returns (items, has_more) for one page.
# Structures verified live on 2026-07-11; if a site redesign breaks a parser,
# it fails loudly (0 items) rather than returning wrong data.
# --------------------------------------------------------------------------

def page_bizinfo(fetch, page):
    # List rows: no / field / title+link(pblancId) / period / ministry / agency / reg / views
    url = (
        "https://www.bizinfo.go.kr/sii/siia/selectSIIA200View.do"
        f"?rows=15&cpage={page}&schEndAt=N"
    )
    status, h = fetch(url)
    if status != 200:
        return [], False
    items = []
    for row in re.findall(r"<tr>[\s\S]*?</tr>", h):
        m = re.search(r'href\s*=\s*"([^"]*pblancId=(PBLN_\d+)[^"]*)"[^>]*>\s*([\s\S]*?)</a>', row)
        if not m:
            continue
        tds = [clean(re.sub(r"<[^>]+>", " ", td)) for td in re.findall(r"<td[^>]*>([\s\S]*?)</td>", row)]
        # tds: [no, field, title-cell, period, ministry, agency, reg_date, views]
        start, end = split_period(tds[3]) if len(tds) > 3 else ("", "")
        items.append(
            {
                "source": "bizinfo",
                "id": m.group(2),
                "title": clean(m.group(3)),
                "field": tds[1] if len(tds) > 1 else "",
                "org": " / ".join(x for x in tds[4:6] if x) if len(tds) > 5 else "",
                "apply_start": start,
                "apply_end": end,
                "reg_date": tds[6] if len(tds) > 6 else "",
                "url": f"https://www.bizinfo.go.kr/sii/siia/selectSIIA200Detail.do?pblancId={m.group(2)}",
            }
        )
    return items, bool(items)


def page_nipa(fetch, page):
    # Table rows: no / D-day / title+link(/home/2-2/{id}) + program tag + period / author / reg
    status, h = fetch(f"https://www.nipa.kr/home/2-2?curPage={page}")
    if status != 200:
        return [], False
    items = []
    for row in re.findall(r"<tr>[\s\S]*?</tr>", h):
        m = re.search(r'href="(/home/2-2/(\d+))"[^>]*>([\s\S]*?)</a>', row)
        if not m:
            continue
        period = re.search(r"신청기간\s*:\s*([^<]+)", row)
        start, end = split_period(period.group(1)) if period else ("", "")
        prog = re.search(r'<span class="box[^"]*">([^<]+)</span>', row)
        reg = re.findall(r'<span class="bco">\s*(\d{4}-\d{2}-\d{2})\s*</span>', row)
        items.append(
            {
                "source": "nipa",
                "id": m.group(2),
                "title": clean(re.sub(r"<!--[\s\S]*?-->", "", m.group(3))),
                "field": clean(prog.group(1)) if prog else "",
                "org": "NIPA",
                "apply_start": start,
                "apply_end": end,
                "reg_date": reg[-1] if reg else "",
                "url": f"https://www.nipa.kr{m.group(1)}",
            }
        )
    return items, bool(items)


def page_kocca(fetch, page):
    # Rows: category / title+link(view.do?intcNo=...) / notice date / apply period / views
    # Pagination is a POST form submit (fn_egov_select_linkPage), not a GET param.
    status, h = fetch(
        "https://www.kocca.kr/kocca/pims/list.do",
        data={"menuNo": "204104", "pageIndex": str(page)},
    )
    if status != 200:
        return [], False
    items = []
    for row in re.findall(r"<tr>[\s\S]*?</tr>", h):
        m = re.search(r'href="(/kocca/pims/view\.do\?intcNo=([^&"]+)[^"]*)"[^>]*>([\s\S]*?)</a>', row)
        if not m:
            continue
        cat = re.search(r'<span class="category_color\d+">([^<]+)</span>', row)
        period = re.search(r'data-label="접수기간">\s*([^<]+)', row)
        notice = re.search(r'data-label="공고일">\s*([^<]+)', row)
        start, end = split_period(period.group(1)) if period else ("", "")
        items.append(
            {
                "source": "kocca",
                "id": m.group(2),
                "title": clean(m.group(3)),
                "field": clean(cat.group(1)) if cat else "",
                "org": "KOCCA",
                "apply_start": start,
                "apply_end": end,
                "reg_date": norm_date(notice.group(1)) if notice else "",
                "url": "https://www.kocca.kr" + htmllib.unescape(m.group(1)),
            }
        )
    return items, bool(items)


def page_smtech(fetch, page):
    # Rows: program / title+link(notice02_detail.do?...ancmId=...) / period / reg / status icons
    status, h = fetch(
        f"https://www.smtech.go.kr/front/ifg/no/notice02_list.do?pageIndex={page}"
    )
    if status != 200:
        return [], False
    items = []
    for row in re.findall(r"<tr>[\s\S]*?</tr>", h):
        m = re.search(r'href="(/front/ifg/no/notice02_detail\.do[^"]*ancmId=([^&"]+)[^"]*)"[^>]*>([\s\S]*?)</a>', row)
        if not m:
            continue
        tds = [clean(re.sub(r"<[^>]+>", " ", td)) for td in re.findall(r"<td[^>]*>([\s\S]*?)</td>", row)]
        period = next((t for t in tds if "~" in t), "")
        start, end = split_period(period) if period else ("", "")
        reg = next((t for t in tds if re.fullmatch(r"\d{4}-\d{2}-\d{2}", t)), "")
        # Drop the session id from the path; keep only the stable query params.
        path = re.sub(r";jsessionid=[^?]*", "", htmllib.unescape(m.group(1)))
        items.append(
            {
                "source": "smtech",
                "id": m.group(2),
                "title": clean(m.group(3)),
                "field": tds[1] if len(tds) > 1 else "",
                "org": "SMTECH(중소기업기술정보진흥원)",
                "apply_start": start,
                "apply_end": end,
                "reg_date": reg,
                "url": f"https://www.smtech.go.kr{path}",
            }
        )
    return items, bool(items)


SOURCES = {
    "bizinfo": page_bizinfo,
    "nipa": page_nipa,
    "kocca": page_kocca,
    "smtech": page_smtech,
}

ALLOWED_DETAIL_HOSTS = ("bizinfo.go.kr", "nipa.kr", "kocca.kr", "smtech.go.kr", "k-startup.go.kr")


def crawl(source, fetch, max_pages):
    """Crawl one source. Returns (items, blocked) — blocked=True means the ladder was exhausted."""
    pager = SOURCES[source]
    seen = {}
    for page in range(1, max_pages + 1):
        try:
            items, has_more = pager(fetch, page)
        except Blocked as e:
            log(f"{source} p{page}: {e} — stopping this source")
            return list(seen.values()), True
        if not items and page == 1:
            log(f"{source} p1: 0 items parsed — site layout changed or soft-blocked; check the HTML")
        new = [i for i in items if i["id"] not in seen]
        for i in items:
            seen[i["id"]] = i
        log(f"{source} p{page}: {len(items)} parsed, {len(new)} new, total {len(seen)}")
        if not has_more or not new:
            break
    return list(seen.values()), False


def cmd_detail(fetch, urls, outdir):
    """Save the text of announcement detail pages (any source) for eligibility checks."""
    os.makedirs(outdir, exist_ok=True)
    for url in urls:
        host = re.sub(r"^https?://([^/]+).*", r"\1", url)
        if not host.endswith(ALLOWED_DETAIL_HOSTS):
            log(f"skip non-source url: {url[:60]}")
            continue
        try:
            status, h = fetch(url)
            if status != 200:
                log(f"{url[:60]}: HTTP {status}")
                continue
            name = re.sub(r"\W+", "_", url.split("://", 1)[1])[:80]
            path = f"{outdir}/{name}.txt"
            with open(path, "w", encoding="utf-8") as f:
                f.write(url + "\n\n" + strip_html(h))
            log(f"saved: {path}")
        except Blocked as e:
            log(f"{url[:60]}: {e} — record as '수동 확인'")
        except Exception as e:  # noqa: BLE001 — skip failures, keep going
            log(f"{url[:60]}: error {e}")


def main():
    ap = argparse.ArgumentParser(
        description="Crawl Korean support-program announcement boards (ir-search)"
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="crawl announcement lists")
    p_list.add_argument("source", choices=[*SOURCES, "all"], help="source to crawl")
    p_list.add_argument("-o", "--output", default="sources.jsonl")
    p_list.add_argument(
        "--max-pages",
        type=int,
        default=30,
        help="page cap per source (bizinfo lists many announcements — "
        "recent pages usually suffice)",
    )
    p_list.add_argument(
        "--drop-expired", action="store_true", help="drop items whose apply_end is already past"
    )

    p_det = sub.add_parser("detail", help="save detail-page text for given URLs")
    p_det.add_argument("urls", nargs="+", help="announcement detail URLs")
    p_det.add_argument("-o", "--output", default="details")

    args = ap.parse_args()

    fetcher = Fetcher(delay=DELAY)
    log(f"fetch backend: {fetcher.backend_name}")

    if args.cmd == "detail":
        cmd_detail(fetcher.fetch, args.urls, args.output)
        return

    names = list(SOURCES) if args.source == "all" else [args.source]
    out = []
    blocked = []
    for name in names:
        items, was_blocked = crawl(name, fetcher.fetch, args.max_pages)
        out.extend(items)
        if was_blocked:
            blocked.append(name)
    if args.drop_expired:
        kept = [r for r in out if not is_past(r.get("apply_end"))]
        log(f"drop-expired: {len(out) - len(kept)} past-deadline items removed")
        out = kept
    with open(args.output, "w", encoding="utf-8") as f:
        for i in out:
            f.write(json.dumps(i, ensure_ascii=False) + "\n")
    log(f"saved: {args.output} ({len(out)} items)")
    if blocked:
        log(f"BLOCKED sources (report as '수동 확인'): {', '.join(blocked)}")
        sys.exit(2)


if __name__ == "__main__":
    main()
