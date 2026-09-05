#!/usr/bin/env python3
"""Workspace state for the ir-search skill — the `.ir-search/` folder in a project.

The skill is used repeatedly on the same project (every 2–4 weeks), and a single
survey can outlive one session (250+ items to review, 30+ detail pages to verify).
This tool keeps the durable, machine-checkable part of that state so the next
session — or the next agent — can pick up where the last one stopped instead of
re-asking the user or re-reading everything.

    <project>/.ir-search/
    ├── profile.md        applicant/item profile (founding stage, region, needs, …)
    ├── worklog.md        append-only log: one entry per finished survey run
    ├── queue.jsonl       open work items: verify / manual / apply / followup / resurvey
    ├── decisions.md      verdict + configuration decisions with their reasons
    └── runs/
        └── YYYYMMDD[-N]/ run.json (stage marker) + raw jsonl + details/ + report.md

Commands (all print human-readable output; `--json` where noted):

  init [--project-dir DIR]            create the workspace; migrate a legacy
                                      ir-search-profile.md from the project root
  status                              one-screen summary: profile, last run, open queue
  run new [--mode full|diff] [--sources s1,s2]
                                      create runs/<today>/ with run.json (stage=collect)
  run stage <run_dir> <stage>         advance the stage marker (collect/review/verify/report/done)
  run finish <run_dir> --report PATH [--counts k=v,...] [--candidates N] [--verified N]
                                      [--a N --b N --c N] [--note TEXT]
                                      mark done, append the worklog entry, update the
                                      profile's "마지막 조사" line
  run last [--json]                   print the most recent *finished* run dir (diff baseline)
  run current [--json]                print the in-progress run (resume point), if any
  queue add --type T --title TITLE [--url U] [--deadline YYYY-MM-DD] [--source S]
            [--ref ID] [--note TEXT]  add a work item (prints its id)
  queue done <qid> [--note TEXT]      close a work item
  queue list [--type T] [--all] [--json]
                                      open items as a markdown table sorted by deadline,
                                      with D-day computed from today
  decide --title TITLE --decision TEXT [--reason TEXT] [--ref ID]
                                      append a decision record to decisions.md

Workspace discovery: --root, else $IR_SEARCH_ROOT, else the nearest `.ir-search/`
walking up from the cwd, else `<cwd>/.ir-search`.
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

WORKSPACE_DIRNAME = ".ir-search"
LEGACY_PROFILE = "ir-search-profile.md"
STAGES = ("collect", "review", "verify", "report", "done")
QUEUE_TYPES = ("verify", "manual", "apply", "followup", "resurvey")
QUEUE_TYPE_LABEL = {
    "verify": "상세검증 대기",
    "manual": "수동 확인",
    "apply": "신청 진행",
    "followup": "후속 확인",
    "resurvey": "재조사 예정",
}

PROFILE_TEMPLATE = """# ir-search 프로필
- 대상: <프로젝트명 (아이템 한 줄)>
- 창업 단계: <예비창업자 / 개인사업자 / 법인 N년차>
- 지역 연고: <소재지 (이전 가능: ...)>
- 대표자: <연령대 / 성별 / 소속>
- 필요한 것: <자금, 공간, R&D, ...>
- 소스 구성: <kstartup, bizinfo, ...>
- 마지막 조사: (없음)
"""

WORKLOG_HEADER = """# ir-search 워크로그

조사 실행 기록. 완료된 실행마다 한 항목이 아래에 추가된다 (최신이 아래).
"""

DECISIONS_HEADER = """# ir-search 결정 기록

판정·구성에 대한 결정과 그 이유. 다음 조사에서 같은 고민을 반복하지 않기 위한 기록이다.
기록 기준: 다른 선택도 가능했던 결정만 (예: 판정 A→B 변경, 소스 제외, 프레이밍 각도 채택/기각).
"""


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def today(args=None):
    if args is not None and getattr(args, "today", None):
        return dt.date.fromisoformat(args.today)
    return dt.date.today()


def find_root(explicit=None):
    if explicit:
        return Path(explicit).expanduser().resolve()
    env = os.environ.get("IR_SEARCH_ROOT")
    if env:
        return Path(env).expanduser().resolve()
    cur = Path.cwd().resolve()
    for d in (cur, *cur.parents):
        cand = d / WORKSPACE_DIRNAME
        if cand.is_dir():
            return cand
    return cur / WORKSPACE_DIRNAME


def require_root(root):
    if not root.is_dir():
        sys.exit(f"ERROR: workspace not found: {root} (run `survey_state.py init` first)")
    return root


def read_jsonl(path):
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def write_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def dday(deadline, ref):
    """'D-3' / 'D-Day' / 'D+2' for a YYYY-MM-DD string; '' when unknown."""
    if not deadline or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", deadline):
        return ""
    delta = (dt.date.fromisoformat(deadline) - ref).days
    if delta == 0:
        return "D-Day"
    return f"D-{delta}" if delta > 0 else f"D+{-delta}"


def rel(path, root):
    """Path relative to the project dir (root's parent) when possible."""
    try:
        return str(Path(path).resolve().relative_to(root.parent.resolve()))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------------------
# init / status
# ---------------------------------------------------------------------------

def cmd_init(args):
    project_dir = Path(args.project_dir).expanduser().resolve() if args.project_dir else Path.cwd()
    root = Path(args.root).expanduser().resolve() if args.root else project_dir / WORKSPACE_DIRNAME
    root.mkdir(parents=True, exist_ok=True)
    (root / "runs").mkdir(exist_ok=True)

    profile = root / "profile.md"
    legacy = project_dir / LEGACY_PROFILE
    if not profile.exists():
        if legacy.exists():
            text = legacy.read_text(encoding="utf-8")
            profile.write_text(text, encoding="utf-8")
            legacy.rename(legacy.with_suffix(".md.migrated"))
            print(f"migrated legacy profile: {legacy.name} → {rel(profile, root)} "
                  f"(original kept as {legacy.name}.migrated)")
        else:
            profile.write_text(PROFILE_TEMPLATE, encoding="utf-8")
            print(f"created {rel(profile, root)} (fill in the <...> fields)")
    for name, header in (("worklog.md", WORKLOG_HEADER), ("decisions.md", DECISIONS_HEADER)):
        p = root / name
        if not p.exists():
            p.write_text(header, encoding="utf-8")
            print(f"created {rel(p, root)}")
    q = root / "queue.jsonl"
    if not q.exists():
        q.touch()
        print(f"created {rel(q, root)}")
    print(f"workspace ready: {root}")


def cmd_status(args):
    root = require_root(find_root(args.root))
    ref = today(args)
    print(f"# ir-search 상태 ({ref.isoformat()}) — {root}\n")

    profile = root / "profile.md"
    if profile.exists():
        print("## 프로필")
        for line in profile.read_text(encoding="utf-8").splitlines():
            if line.startswith("- "):
                print(line)
        print()

    cur = current_run(root)
    last = last_run(root)
    print("## 실행")
    if cur:
        print(f"- 진행 중: {rel(cur['dir'], root)} · 단계 {cur['stage']} · 모드 {cur.get('mode', '?')}"
              f" · 소스 {', '.join(cur.get('sources', [])) or '?'}  ← 여기서 재개")
    else:
        print("- 진행 중인 실행 없음")
    if last:
        print(f"- 마지막 완료: {rel(last['dir'], root)} ({last.get('finished', '?')[:10]})"
              f" · 보고서 {last.get('report', '?')}")
    else:
        print("- 완료된 실행 없음 (첫 조사는 전수 모드)")
    print()

    items = [q for q in read_jsonl(root / "queue.jsonl") if q.get("status") == "open"]
    print(f"## 큐 (열린 항목 {len(items)})")
    if items:
        print(render_queue(items, ref))
    else:
        print("(없음)")


# ---------------------------------------------------------------------------
# runs
# ---------------------------------------------------------------------------

def load_runs(root):
    runs = []
    for d in sorted((root / "runs").glob("*")):
        meta = d / "run.json"
        if d.is_dir() and meta.exists():
            r = json.loads(meta.read_text(encoding="utf-8"))
            r["dir"] = d
            runs.append(r)
    return runs


def last_run(root):
    done = [r for r in load_runs(root) if r.get("stage") == "done"]
    return done[-1] if done else None


def current_run(root):
    open_runs = [r for r in load_runs(root) if r.get("stage") != "done"]
    return open_runs[-1] if open_runs else None


def save_run(run):
    d = run["dir"]
    meta = {k: v for k, v in run.items() if k != "dir"}
    (d / "run.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cmd_run_new(args):
    root = require_root(find_root(args.root))
    cur = current_run(root)
    if cur and not args.force:
        sys.exit(f"ERROR: a run is still in progress: {rel(cur['dir'], root)} (stage {cur['stage']}).\n"
                 f"Resume it, finish it, or pass --force to start another.")
    base = today(args).strftime("%Y%m%d")
    d = root / "runs" / base
    n = 1
    while d.exists():
        n += 1
        d = root / "runs" / f"{base}-{n}"
    d.mkdir(parents=True)
    (d / "details").mkdir()
    mode = args.mode
    if mode == "auto":
        mode = "diff" if last_run(root) else "full"
    run = {
        "dir": d,
        "started": dt.datetime.now().isoformat(timespec="seconds"),
        "mode": mode,
        "sources": [s for s in (args.sources or "").split(",") if s],
        "stage": "collect",
    }
    if mode == "diff":
        prev = last_run(root)
        run["baseline"] = str(prev["dir"]) if prev else None
    save_run(run)
    if args.json:
        print(json.dumps({"dir": str(d), "mode": mode, "baseline": run.get("baseline")}, ensure_ascii=False))
    else:
        print(str(d))
        print(f"mode={mode}" + (f" baseline={run['baseline']}" if run.get("baseline") else ""), file=sys.stderr)


def cmd_run_stage(args):
    root = require_root(find_root(args.root))
    run = _run_by_dir(root, args.run_dir)
    if args.stage not in STAGES:
        sys.exit(f"ERROR: stage must be one of {STAGES}")
    run["stage"] = args.stage
    run.setdefault("stage_log", []).append(
        {"stage": args.stage, "at": dt.datetime.now().isoformat(timespec="seconds")}
    )
    save_run(run)
    print(f"{rel(run['dir'], root)}: stage → {args.stage}")


def _run_by_dir(root, run_dir):
    d = Path(run_dir).expanduser().resolve()
    meta = d / "run.json"
    if not meta.exists():
        sys.exit(f"ERROR: not a run directory (no run.json): {d}")
    run = json.loads(meta.read_text(encoding="utf-8"))
    run["dir"] = d
    return run


def parse_counts(s):
    out = {}
    for part in (s or "").split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = int(v)
    return out


def cmd_run_finish(args):
    root = require_root(find_root(args.root))
    run = _run_by_dir(root, args.run_dir)
    ref = today(args)
    counts = parse_counts(args.counts)
    run.update(
        {
            "stage": "done",
            "finished": dt.datetime.now().isoformat(timespec="seconds"),
            "report": rel(args.report, root),
            "counts": counts,
            "candidates": args.candidates,
            "verified": args.verified,
            "verdicts": {"A": args.a, "B": args.b, "C": args.c},
            "note": args.note or "",
        }
    )
    save_run(run)

    # worklog entry
    src = " / ".join(f"{k} {v}" for k, v in counts.items()) or "(건수 미기록)"
    verdicts = " / ".join(f"{g} {n}" for g, n in run["verdicts"].items() if n is not None) or "-"
    entry = [
        f"\n## {ref.isoformat()} — {'증분 재조사 (diff)' if run.get('mode') == 'diff' else '전수조사 (full)'} · {rel(run['dir'], root)}",
        f"- 소스: {src}",
        f"- 후보 {args.candidates if args.candidates is not None else '-'} → 상세검증 "
        f"{args.verified if args.verified is not None else '-'} → {verdicts}",
        f"- 보고서: {run['report']}",
    ]
    if run.get("baseline"):
        entry.append(f"- 기준(diff 베이스라인): {rel(run['baseline'], root)}")
    if args.note:
        entry.append(f"- 메모: {args.note}")
    with open(root / "worklog.md", "a", encoding="utf-8") as f:
        f.write("\n".join(entry) + "\n")

    # profile "마지막 조사" line
    profile = root / "profile.md"
    if profile.exists():
        text = profile.read_text(encoding="utf-8")
        line = f"- 마지막 조사: {rel(run['dir'], root)} ({ref.isoformat()})"
        if re.search(r"^- 마지막 조사:.*$", text, flags=re.M):
            text = re.sub(r"^- 마지막 조사:.*$", line, text, flags=re.M)
        else:
            text = text.rstrip("\n") + "\n" + line + "\n"
        profile.write_text(text, encoding="utf-8")

    # close verify items that belonged to this run
    queue = read_jsonl(root / "queue.jsonl")
    closed = 0
    for q in queue:
        if q.get("status") == "open" and q.get("type") == "verify" and q.get("run") == run["dir"].name:
            q["status"] = "done"
            q["closed"] = ref.isoformat()
            q["note"] = (q.get("note", "") + " [run finished]").strip()
            closed += 1
    if closed:
        write_jsonl(root / "queue.jsonl", queue)
    print(f"finished {rel(run['dir'], root)} · worklog updated · profile updated"
          + (f" · {closed} verify items auto-closed" if closed else ""))


def cmd_run_last(args):
    root = require_root(find_root(args.root))
    r = last_run(root)
    if not r:
        sys.exit(1)
    print(json.dumps({"dir": str(r["dir"]), "finished": r.get("finished"), "report": r.get("report")},
                     ensure_ascii=False) if args.json else str(r["dir"]))


def cmd_run_current(args):
    root = require_root(find_root(args.root))
    r = current_run(root)
    if not r:
        sys.exit(1)
    print(json.dumps({"dir": str(r["dir"]), "stage": r.get("stage"), "mode": r.get("mode"),
                      "sources": r.get("sources", [])}, ensure_ascii=False) if args.json else
          f"{r['dir']} stage={r.get('stage')} mode={r.get('mode')}")


# ---------------------------------------------------------------------------
# queue
# ---------------------------------------------------------------------------

def next_qid(queue):
    n = 0
    for q in queue:
        m = re.fullmatch(r"q(\d+)", q.get("id", ""))
        if m:
            n = max(n, int(m.group(1)))
    return f"q{n + 1:03d}"


def cmd_queue_add(args):
    root = require_root(find_root(args.root))
    if args.type not in QUEUE_TYPES:
        sys.exit(f"ERROR: --type must be one of {QUEUE_TYPES}")
    path = root / "queue.jsonl"
    queue = read_jsonl(path)
    # de-dup: same type + same ref/url still open → reuse
    for q in queue:
        if q.get("status") == "open" and q.get("type") == args.type and (
            (args.ref and q.get("ref") == args.ref) or (args.url and q.get("url") == args.url)
        ):
            print(q["id"])
            print(f"(already queued: {q['title']})", file=sys.stderr)
            return
    cur = current_run(root)
    item = {
        "id": next_qid(queue),
        "type": args.type,
        "title": args.title,
        "url": args.url or "",
        "source": args.source or "",
        "ref": args.ref or "",
        "deadline": args.deadline or "",
        "note": args.note or "",
        "run": cur["dir"].name if cur else "",
        "status": "open",
        "added": today(args).isoformat(),
    }
    queue.append(item)
    write_jsonl(path, queue)
    print(item["id"])


def cmd_queue_done(args):
    root = require_root(find_root(args.root))
    path = root / "queue.jsonl"
    queue = read_jsonl(path)
    for q in queue:
        if q.get("id") == args.qid:
            q["status"] = "done"
            q["closed"] = today(args).isoformat()
            if args.note:
                q["note"] = (q.get("note", "") + " " + args.note).strip()
            write_jsonl(path, queue)
            print(f"{args.qid} done: {q['title']}")
            return
    sys.exit(f"ERROR: no queue item {args.qid}")


def render_queue(items, ref):
    def sort_key(q):
        d = q.get("deadline") or "9999-99-99"
        return (QUEUE_TYPES.index(q["type"]) if q["type"] in QUEUE_TYPES else 99, d)

    rows = ["| id | 종류 | 항목 | 마감 | D-day | 비고 |", "|---|---|---|---|---|---|"]
    for q in sorted(items, key=sort_key):
        dd = dday(q.get("deadline"), ref)
        flag = ""
        if dd.startswith("D-") and dd != "D-Day":
            try:
                if int(dd[2:]) <= 3:
                    flag = " ⚠️"
            except ValueError:
                pass
        elif dd == "D-Day":
            flag = " ⚠️"
        elif dd.startswith("D+"):
            flag = " (지남)"
        title = q["title"] + (f" <{q['url']}>" if q.get("url") else "")
        rows.append(
            f"| {q['id']} | {QUEUE_TYPE_LABEL.get(q['type'], q['type'])} | {title} | "
            f"{q.get('deadline') or '불명'} | {dd}{flag} | {q.get('note', '')} |"
        )
    return "\n".join(rows)


def cmd_queue_list(args):
    root = require_root(find_root(args.root))
    queue = read_jsonl(root / "queue.jsonl")
    items = [q for q in queue if args.all or q.get("status") == "open"]
    if args.type:
        items = [q for q in items if q.get("type") == args.type]
    if args.json:
        print(json.dumps(items, ensure_ascii=False, indent=2))
        return
    if not items:
        print("(큐 비어 있음)")
        return
    print(render_queue(items, today(args)))


# ---------------------------------------------------------------------------
# decisions
# ---------------------------------------------------------------------------

def cmd_decide(args):
    root = require_root(find_root(args.root))
    ref = today(args)
    cur = current_run(root)
    lines = [f"\n## {ref.isoformat()} — {args.title}", f"- 결정: {args.decision}"]
    if args.reason:
        lines.append(f"- 이유: {args.reason}")
    if args.ref:
        lines.append(f"- 대상: {args.ref}")
    if cur:
        lines.append(f"- 실행: {rel(cur['dir'], root)}")
    with open(root / "decisions.md", "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"decision recorded: {args.title}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="ir-search workspace state (.ir-search/)")
    ap.add_argument("--root", help="workspace dir (default: nearest .ir-search/)")
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD) — for tests/reproducibility")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="create the workspace (migrates ir-search-profile.md)")
    p.add_argument("--project-dir", help="project root (default: cwd)")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("status", help="profile + last/current run + open queue")
    p.set_defaults(func=cmd_status)

    pr = sub.add_parser("run", help="survey run lifecycle")
    rs = pr.add_subparsers(dest="run_cmd", required=True)
    p = rs.add_parser("new")
    p.add_argument("--mode", choices=("auto", "full", "diff"), default="auto")
    p.add_argument("--sources", help="comma-separated source names crawled in this run")
    p.add_argument("--force", action="store_true", help="start even if another run is in progress")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_run_new)
    p = rs.add_parser("stage")
    p.add_argument("run_dir")
    p.add_argument("stage", choices=STAGES)
    p.set_defaults(func=cmd_run_stage)
    p = rs.add_parser("finish")
    p.add_argument("run_dir")
    p.add_argument("--report", required=True, help="report path (md)")
    p.add_argument("--counts", help="per-source item counts, e.g. kstartup=262,bizinfo=300")
    p.add_argument("--candidates", type=int)
    p.add_argument("--verified", type=int)
    p.add_argument("--a", type=int)
    p.add_argument("--b", type=int)
    p.add_argument("--c", type=int)
    p.add_argument("--note")
    p.set_defaults(func=cmd_run_finish)
    p = rs.add_parser("last")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_run_last)
    p = rs.add_parser("current")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_run_current)

    pq = sub.add_parser("queue", help="work-item queue")
    qs = pq.add_subparsers(dest="queue_cmd", required=True)
    p = qs.add_parser("add")
    p.add_argument("--type", required=True, choices=QUEUE_TYPES)
    p.add_argument("--title", required=True)
    p.add_argument("--url")
    p.add_argument("--source")
    p.add_argument("--ref", help="announcement id (pbancSn / pblancId / …)")
    p.add_argument("--deadline", help="YYYY-MM-DD")
    p.add_argument("--note")
    p.set_defaults(func=cmd_queue_add)
    p = qs.add_parser("done")
    p.add_argument("qid")
    p.add_argument("--note")
    p.set_defaults(func=cmd_queue_done)
    p = qs.add_parser("list")
    p.add_argument("--type", choices=QUEUE_TYPES)
    p.add_argument("--all", action="store_true", help="include closed items")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_queue_list)

    p = sub.add_parser("decide", help="append a decision record")
    p.add_argument("--title", required=True)
    p.add_argument("--decision", required=True)
    p.add_argument("--reason")
    p.add_argument("--ref")
    p.set_defaults(func=cmd_decide)

    args = ap.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
