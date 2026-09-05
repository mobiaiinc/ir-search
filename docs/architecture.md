# 구성과 데이터 흐름

ir-search는 서버도 데이터베이스도 없다. 구성 요소는 세 층이다: **지시 층**(SKILL.md, references/, agents/ — 모델이 읽는다), **도구 층**(scripts/ — 모델이 Bash로 실행한다), **상태 층**(사용자 프로젝트의 `.ir-search/` — 도구가 쓰고 모델·사람이 읽는다). 지시 층은 도구 층을 호출하고, 도구 층만 상태 층을 쓴다. 모델이 `.ir-search/` 파일을 직접 편집하는 경우는 `profile.md`뿐이다.

## 한 번의 조사 흐름

```
사용자 요청 ("지원사업 찾아줘")
  │
  ▼
SKILL.md 0단계 ── survey_state.py status ──▶ .ir-search/ 읽기 (profile, runs/*/run.json, queue.jsonl)
  │                                            └─ 진행 중 run 있음 → 그 stage로 점프 (재개)
  ▼
survey_state.py run new ──▶ runs/<날짜>/run.json {stage: collect, mode: full|diff}
  │
  ▼ 1단계 수집
kstartup_crawl.py list ──┐
sources_crawl.py list ───┴─▶ fetchlib.Fetcher ──HTTP──▶ 공고 사이트 ──▶ runs/<날짜>/*.jsonl
  │                              (지문 사다리·차단 판정·지연)         (Blocked → 종료코드 2)
  ▼ (diff 모드) diff_surveys.py <직전 run> <이번 run> ──▶ new_items.jsonl
  ▼ 2단계 검토 (모델이 jsonl 전체를 읽음)
survey_state.py queue add --type verify ×N ──▶ queue.jsonl        ← 체크포인트
  ▼ 3단계 검증
kstartup_crawl.py detail / sources_crawl.py detail ──▶ runs/<날짜>/details/*.txt
  ├─ 후보 ≥15 → agents/ir-detail-verifier ──▶ verified.jsonl (근거 인용 포함)
  └─ 후보 <15 → 모델이 details/ 직접 읽음
  ▼ 4단계 판정 (모델) ──▶ runs/<날짜>/report.md ; survey_state.py decide ──▶ decisions.md
  ▼ 마무리
agents/ir-report-reviewer (report.md ↔ details/ ↔ queue.jsonl 대조) ──▶ review-report.md
survey_state.py queue add --type apply|followup|manual|resurvey
survey_state.py run finish ──▶ run.json {stage: done} + worklog.md 추가 + profile.md "마지막 조사" 갱신 + verify 큐 일괄 종료
```

## 구성 요소와 의존 방향

| 구성 요소 | 역할 | 의존 |
|---|---|---|
| `SKILL.md` | 단계별 절차. 어느 스크립트를 언제 어떤 인자로 부르는지 | references/, scripts/ CLI, agents/ |
| `references/sources.md` | 소스별 URL·페이지네이션·함정. 새 소스를 추가할 때의 출발점 | 없음 |
| `references/workspace-format.md` | `.ir-search/` 파일 규격 (사용자와의 약속) | 없음 |
| `references/report-format.md` | 보고서 템플릿, 검증 항목, 판정 기준 | 없음 |
| `scripts/fetchlib.py` | HTTP 한 곳: 백엔드 선택, 에스컬레이션, 차단 판정, 재시도, 지연, 날짜 정규화, HTML 제거 | 표준 라이브러리 (+ 선택: curl_cffi) |
| `scripts/kstartup_crawl.py` | K-Startup 목록(`bizPbancList` 블록 파싱)·상세 | fetchlib |
| `scripts/sources_crawl.py` | 4개 소스의 `page_*` 파서 + 공통 `crawl` 루프 + 상세 | fetchlib |
| `scripts/diff_surveys.py` | 두 실행 폴더의 jsonl을 `(source, id)`로 키잉해 비교 | 없음 (jsonl 형식만) |
| `scripts/survey_state.py` | `.ir-search/` 생성·조회·갱신. 스크립트 중 유일하게 상태를 쓴다 | 없음 |
| `agents/ir-detail-verifier.md` | details/ → verified.jsonl 구조화 추출 | details/ 형식 (첫 줄 URL) |
| `agents/ir-report-reviewer.md` | report.md를 details/·queue.jsonl과 대조 | 실행 폴더 구조 |

크롤러 → fetchlib 방향만 있고 역방향 import는 없다. `diff_surveys.py`와 `survey_state.py`는 서로 모른다: diff는 폴더 두 개를 받을 뿐이고, 어느 폴더가 "직전"인지는 SKILL.md가 `run last`로 얻어 넘긴다.

## 실행 폴더가 경계다

한 조사의 모든 산출물(원시 jsonl, details/, verified.jsonl, report.md, review-report.md, run.json)은 `runs/<날짜>/` 하나에 들어간다. diff 모드는 폴더 두 개를 비교하고, 재개는 폴더 하나의 `run.json`을 읽는다. 폴더 밖으로 나가는 것은 `worklog.md`(요약 한 항목), `queue.jsonl`(할 일), `decisions.md`(이유), `profile.md`의 마지막 조사 줄뿐이다.

## 설치 형태

같은 저장소가 세 방식으로 설치된다. 루트 `SKILL.md`가 세 방식 모두의 진입점이다.

- **직접 클론**: `~/.claude/skills/ir-search/` = 저장소 루트. Claude Code가 `SKILL.md`를 스킬로 읽고, `agents/`는 읽지 않는다 (사용자 에이전트는 `~/.claude/agents/`에서만 찾는다) → `install.sh`가 `agents/ir-*.md`를 그쪽으로 링크한다
- **플러그인**: `.claude-plugin/plugin.json`이 루트 `SKILL.md`를 단일 스킬로, `agents/`를 플러그인 에이전트로 등록한다. 스킬 호출명은 `ir-search:ir-search`
- **프로젝트 로컬**: `install.sh --project DIR` → `DIR/.claude/skills/ir-search`, `DIR/.claude/agents/`

스크립트 경로는 설치 방식마다 다르므로 SKILL.md는 "이 SKILL.md가 있는 폴더 기준 `scripts/`"로만 말한다.
