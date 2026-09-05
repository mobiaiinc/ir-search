<samp>[🇰🇷 한국어](README.md) · 🇺🇸 English</samp>

# ir-search

> ⚠️ **This skill covers South Korean government / public-agency support programs only.** It does not cover programs from any other country, and the announcements it processes are written in Korean.

A Claude Code skill for **exhaustive surveys of Korean government support programs** (startup grants, commercialization funding, incubation space, R&D calls, vouchers, competitions).

It crawls every currently-open announcement from K-Startup, Bizinfo, NIPA, KOCCA, and SMTECH, matches them against the profile of the project in your working folder — founding stage, region, needs (funding / space / R&D) — verifies eligibility against the original announcement text, and produces a report with a three-tier classification:

- **Group A — Apply right now**: eligible as-is (sorted by deadline, imminent ones flagged)
- **Group B — Unlocked by a requirement (roadmap)**: triggers like incorporation or securing investment, with chained paths spelled out (e.g., competition prize → non-metro incorporation → Pre-TIPS → TIPS)
- **Group C — Eligible with reframing**: concrete angles for re-describing your item in another domain's language (content production, social services, art×tech, ...)

Why exhaustive review instead of keyword search: the programs an "AI startup" can actually win — content-production grants, art×tech residencies, social-service startup funds — never match the keyword "AI".

## Built for repeated use (v3)

Survey state lives in the project's **`.ir-search/`** folder, not in the conversation. A survey that outlives one session, or that someone else picks up on another machine, resumes from the same point.

```
<project>/.ir-search/
├── profile.md        applicant/item profile — later surveys just ask "anything changed?"
├── worklog.md        run log — when, which sources, how many items, how many A/B/C
├── queue.jsonl       work items — verify / manual / apply / follow-up / re-survey, with D-day
├── decisions.md      verdict and configuration decisions with reasons
└── runs/YYYYMMDD/    one survey: raw jsonl + announcement texts + report.md + stage marker
```

- **Resume**: if the session dies while verifying 30 candidates, the next session runs `status`, sees "stage verify, 12 items left in the queue", and continues
- **Re-survey**: diffed against the previous run automatically — only **new / deadline-changed / closed** announcements are reported, instead of re-reading 250+ items
- **Queue**: after the survey, "apply to Youth Startup Academy by 9/8 16:00" and "re-survey on 9/26" stay in the queue with D-days, appended to every chat reply

## Sample output (excerpt)

```markdown
# Support-program survey — ○○ (AI voice SaaS, pre-founder, Chungnam)
Surveyed 2026-09-05 · reviewed all 262 K-Startup + 300 Bizinfo items → verified 31 candidates

## Group A — Apply right now (by deadline)

1. **2026 Youth Startup Academy, extra round** — KOSME
   - Support: up to ₩100M commercialization fund + space + mentoring
   - Eligibility: pre-founders ✓ · under 39 ✓ · nationwide ✓
   - Deadline: 2026-09-08 16:00 (D-3) ⚠️ imminent
   - https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=1784xx

## Group B — Unlocked by a requirement (roadmap)

- **Pre-TIPS**: trigger = incorporating outside the capital region.
  Chain: competition prize/seed → Chungnam incorporation → Pre-TIPS → TIPS

## Group C — Eligible with reframing

- **Content production grant (KOCCA)**: reframe "AI voice tech" as an
  "audio-content production pipeline". Risk: deliverable must be content

## Absence check
- Pre-Startup Package: not currently open (usually announced in Feb — queued for re-survey)

## Priority actions
- by 9/8: apply to A-1 (note the 16:00 cutoff)
- by 9/15: draft C-1 content framing, then call the agency to confirm
```

Every mentioned announcement carries its original URL; anything not stated in the announcement text is marked "unknown" rather than guessed. A reviewer subagent checks the report against the original texts before delivery (missing URLs, numbers not in the source, missing imminent flags).

## Covered sources

| Source | What it is | Crawler |
|---|---|---|
| [K-Startup](https://www.k-startup.go.kr) | Unified startup-support portal (default) | `kstartup_crawl.py` |
| [Bizinfo](https://www.bizinfo.go.kr) | All-ministry/region SME support (widest coverage) | `sources_crawl.py` |
| [NIPA](https://www.nipa.kr) | AI / ICT programs | `sources_crawl.py` |
| [KOCCA](https://www.kocca.kr) | Content-industry programs | `sources_crawl.py` |
| [SMTECH](https://www.smtech.go.kr) | SME R&D calls | `sources_crawl.py` |

More sources (NIA, IITP, IRIS, regional agencies) are catalogued in `references/sources.md`. When a site blocks the crawler it climbs a TLS-fingerprint ladder (safari → safari_ios → chrome → chrome_android → mobile host) automatically; if that fails the source is reported as "check manually" — no login or CAPTCHA circumvention.

## Install

Three ways; the result is the same.

```bash
# A. clone + symlink (git pull updates it). Links the skill and its two subagents into ~/.claude
git clone https://github.com/mobiaiinc/ir-search.git && cd ir-search && ./install.sh

# B. for one project only
./install.sh --project ~/work/my-startup

# C. plugin marketplace (inside Claude Code)
/plugin marketplace add mobiaiinc/ir-search
/plugin install ir-search@ir-search
```

```bash
# recommended (avoids TLS-fingerprint blocking); falls back to urllib without it
python3 -m pip install --user 'curl_cffi>=0.15'
```

## Use

With your project folder open in Claude Code:

```
우리 아이템에 맞는 지원사업 전수조사 해줘
(Survey the support programs that fit this project)
```

or `/ir-search` (`/ir-search:ir-search` when installed as a plugin). Claude checks `.ir-search/`, reads project context from the folder if there is no profile yet, asks for the missing fields (founding stage, region, needs) once, and starts.

Later:

```
새로 나온 지원사업 있나?   → diff against the previous run: new / deadline changes / closed only
지원사업 큐 보여줘         → open work items with D-days
```

The crawlers and the state tool also work standalone:

```bash
# all open K-Startup announcements / detail-page text / Bizinfo / all four extra sources
python3 scripts/kstartup_crawl.py list -o all.jsonl --drop-expired
python3 scripts/kstartup_crawl.py detail 178481 -o details/
python3 scripts/sources_crawl.py list bizinfo -o biz.jsonl --max-pages 20
python3 scripts/sources_crawl.py list all -o sources.jsonl
python3 scripts/diff_surveys.py <previous run dir> <current run dir> --out new.jsonl
# profile · runs · queue
python3 scripts/survey_state.py status
# work items + D-day
python3 scripts/survey_state.py queue list
```

## Layout

```
ir-search/
├── SKILL.md                    # workflow (status → profile → collect all → review all → verify → 3-tier → review → update state)
├── scripts/
│   ├── fetchlib.py             # shared HTTP: fingerprint ladder, block detection, retry, delay, date utils
│   ├── kstartup_crawl.py       # K-Startup crawler
│   ├── sources_crawl.py        # Bizinfo / NIPA / KOCCA / SMTECH crawler
│   ├── diff_surveys.py         # incremental re-survey diff (new / changed / closed / stale sources)
│   └── survey_state.py         # .ir-search/ workspace (init / status / run / queue / decide)
├── agents/
│   ├── ir-detail-verifier.md   # structured eligibility extraction with evidence quotes (15+ candidates)
│   └── ir-report-reviewer.md   # report QA against source texts and the queue
├── references/
│   ├── sources.md              # source registry (verified access recipes + secondary sources)
│   ├── workspace-format.md     # .ir-search/ file spec
│   └── report-format.md        # report template, verification fields, verdict rules, review checklist
├── tests/                      # network-free unittest (synthetic HTML, temp workspaces)
├── docs/                       # for contributors: architecture, rules, standards, notes, operations, contracts, tracking/
├── CLAUDE.md / AGENTS.md       # entry point for agents editing this repository
├── install.sh                  # local install (symlink/copy, user- or project-level)
└── .claude-plugin/             # plugin manifests
```

Note: `SKILL.md`, the references, the agents, and the workspace files are written in Korean — the whole domain (announcements, eligibility criteria, report vocabulary) is Korean, and the model works with it natively.

## Development

```bash
python3 -m unittest discover -s tests -v
```

After changing a parser, run a live smoke test (`list --max-pages 2`) from a machine with network access and update the verification date in `references/sources.md`. Rules and traps are in `docs/`.

## Caveats

- Announcement details (deadlines, eligibility, amounts) change frequently. **Always confirm with the accepting agency before applying.** The report reflects the announcement text at survey time.
- Only public announcement pages are accessed, with a delay between requests. Please respect the target sites' terms of service.
- `.ir-search/` holds no personal data beyond the profile axes (founding stage, region, age band, ...). Whether to commit it is the project's call (`runs/*/details/` is large and usually excluded).

## License

MIT · upstream: [djfksjd/ir-search](https://github.com/djfksjd/ir-search)
