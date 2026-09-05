# Changelog

## v3.0.0 (2026-09-05) — local application: workspace, queue, worklog, harness

- **`.ir-search/` workspace** (`scripts/survey_state.py`): profile, append-only worklog, work-item queue with D-day, decision log, per-run folders with a stage marker. A survey that outlives one session resumes from the queue and the stage marker instead of re-asking the user. Legacy `ir-search-profile.md` is migrated automatically by `init`.
- **Shared scraping layer** (`scripts/fetchlib.py`): the TLS-fingerprint escalation ladder (safari → safari_ios → chrome → chrome_android → mobile host), body-marker block detection, retry with backoff, and the politeness delay now live in one module used by both crawlers. Blocked sources exit with code 2 and are reported as "수동 확인" rather than silently missing.
- `--drop-expired` on both crawlers; unparseable deadlines ("상시") are kept.
- **Subagents**: `ir-detail-verifier` (structured eligibility extraction with evidence quotes, for 15+ candidates) and `ir-report-reviewer` (report QA against the original texts and the queue).
- **Plugin packaging**: `.claude-plugin/plugin.json` + `marketplace.json` (single-skill plugin with root `SKILL.md`), `install.sh` for user- or project-level symlink installs.
- **Project harness** for contributors: `CLAUDE.md`/`AGENTS.md`, `docs/` (architecture, business rules, standards, engineering notes, operations, contracts, security) and `docs/tracking/` (status, findings, decision records).
- Reports move from `~/Documents/지원사업조사_*` to `<project>/.ir-search/runs/<date>/report.md` (a copy elsewhere is fine; the run folder is the diff baseline).
- `run last` / `run current` order runs by the `started` timestamp, not the folder name (`runs/20260905-10` no longer sorts before `-2`).

## v2 (2026-07) — multi-source

- Bizinfo / NIPA / KOCCA / SMTECH crawlers (`sources_crawl.py`), English README, blocked-site escalation ladder, JS-site fallback notes, profile persistence, incremental re-survey diff (`diff_surveys.py`).

## v1 (2026-07) — initial

- K-Startup crawler and the profile → collect-all → review-all → verify → 3-tier report workflow.
