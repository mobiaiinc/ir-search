# 인터페이스 계약

이 프로젝트의 소비자는 둘이다: **SKILL.md(모델)**가 CLI를 호출하고, **사용자·후속 도구**가 `.ir-search/`의 파일을 읽는다. 아래가 그들이 의지할 수 있는 약속이다.

## 공통 관례

- 데이터 출력은 파일(`-o`, `--out`) 또는 `--json`일 때 stdout. 진행 로그는 stderr에 `[ir-search] ` 접두어
- 인코딩 UTF-8, JSONL은 한 줄에 JSON 객체 하나, `ensure_ascii=False`
- 날짜는 `YYYY-MM-DD`. 시각이 있으면 `YYYY-MM-DD HH:MM`. 모르면 빈 문자열(코드) / `불명`(문서)
- 종료 코드: `0` 성공 / `1` 입력 오류·워크스페이스 없음 / `2` 일부 소스 차단(저장은 됨)

## 크롤러 CLI

```
kstartup_crawl.py list [-o FILE] [--max-pages N=40] [--drop-expired]
kstartup_crawl.py detail <pbancSn>... [-o DIR=details]
sources_crawl.py list <bizinfo|nipa|kocca|smtech|all> [-o FILE] [--max-pages N=30] [--drop-expired]
sources_crawl.py detail <URL>... [-o DIR=details]
```

- `list`는 항상 파일을 쓴다 (0건이어도 빈 파일). 차단된 소스가 있으면 저장 후 종료 코드 2와 `BLOCKED sources: …` 로그
- `detail`은 URL당 파일 하나. 이름은 K-Startup `<pbancSn>.txt`, 그 외 `<URL에서 스킴 제거 후 비단어문자→_ 치환, 80자>.txt`. **첫 줄은 원문 URL, 빈 줄, 그 다음 본문 텍스트**. 허용 호스트 밖 URL은 건너뛴다
- 오류: 잘못된 ID·HTTP 비200·네트워크 실패는 그 항목만 건너뛰고 계속한다 (종료 코드 0)

### K-Startup 레코드 (`kstartup_crawl.py list`)

```json
{"pbancSn": "178481", "category": "사업화", "dday": "D-3", "title": "…", "program": "…", "org": "…",
 "start": "2026-08-20", "deadline": "2026-09-08", "agency_type": "공공",
 "url": "https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178481"}
```

`source` 필드가 없다. 소비자는 `pbancSn` 존재로 K-Startup임을 안다.

### 통합 레코드 (`sources_crawl.py list`)

```json
{"source": "bizinfo", "id": "PBLN_000000000112233", "title": "…", "field": "창업", "org": "중소벤처기업부 / 창업진흥원",
 "apply_start": "2026-08-01", "apply_end": "2026-09-10", "reg_date": "2026-08-01", "url": "https://…"}
```

`source`는 `bizinfo|nipa|kocca|smtech`. `id`는 소스 안에서만 유일하다 — 전역 키는 `(source, id)`.

## diff CLI

```
diff_surveys.py <prev_dir> <curr_dir> [--out FILE]
```

- 두 폴더의 `*.jsonl` 중 **원시 크롤 파일만** 읽는다. `new_items.jsonl`, `verified.jsonl`은 이름으로 건너뛰고, 그 밖의 파일도 크롤러 필드(`pbancSn` 또는 `source`+`id`+`apply_end`)가 없는 레코드는 무시한다
- stdout: `# Survey diff` 헤더, `## NEW (n)`, `## DEADLINE CHANGED (n)`, `## CLOSED (n)`, `## UNCHANGED: n`, 있으면 `## NEW SOURCES this run (…)`, `## WARNING — sources in previous run but not re-crawled: …`
- `--out`: NEW + 새 소스 항목을 원래 레코드 형식 그대로 JSONL로. 이 파일을 `detail` 명령에 바로 먹일 수 있다
- 종료 코드: 폴더 없음·jsonl 없음이면 1

## 상태 CLI (`survey_state.py`)

전역 옵션 `--root DIR`, `--today YYYY-MM-DD`(테스트·재현용). 워크스페이스 탐색: `--root` → `$IR_SEARCH_ROOT` → cwd에서 위로 `.ir-search/` → `cwd/.ir-search`.

| 명령 | stdout | 부수효과 |
|---|---|---|
| `init [--project-dir DIR]` | 생성/이관 로그 | `.ir-search/{profile.md,worklog.md,queue.jsonl,decisions.md,runs/}` 생성. `ir-search-profile.md`가 있으면 `profile.md`로 복사 후 `.migrated`로 개명. 있는 파일은 건드리지 않음 |
| `status` | 마크다운 요약 (프로필 `- ` 줄, 실행, 큐 표) | 없음 |
| `run new [--mode auto\|full\|diff] [--sources a,b] [--force] [--json]` | 실행 폴더 절대경로 한 줄 (`--json`이면 `{dir, mode, baseline}`) | `runs/YYYYMMDD[-N]/run.json`, `details/`. 진행 중 실행이 있으면 종료 코드 1 (`--force` 제외). `auto`는 완료 실행이 있으면 diff |
| `run stage <dir> <collect\|review\|verify\|report\|done>` | 확인 한 줄 | `run.json.stage` + `stage_log` 추가 |
| `run finish <dir> --report PATH [--counts k=v,…] [--candidates N] [--verified N] [--a N --b N --c N] [--note T]` | 확인 한 줄 | `run.json` 완료 필드, `worklog.md` 항목 추가, `profile.md` 마지막 조사 줄, 그 실행의 `verify` 큐 종료 |
| `run last [--json]` | 최근 완료 실행 경로 | 없음. 없으면 종료 코드 1 |
| `run current [--json]` | 진행 중 실행 경로와 stage | 없음. 없으면 종료 코드 1 |
| `queue add --type T --title S [--url U] [--source S] [--ref R] [--deadline D] [--note N]` | 큐 ID (`qNNN`) 한 줄 | 추가. 같은 type+ref/url이 열려 있으면 기존 ID를 내고 추가하지 않음 |
| `queue done <qid> [--note N]` | 확인 한 줄 | `status: done`, `closed` |
| `queue list [--type T] [--all] [--json]` | 마크다운 표 (id/종류/항목/마감/D-day/비고) 또는 JSON 배열 | 없음 |
| `decide --title S --decision S [--reason S] [--ref R]` | 확인 한 줄 | `decisions.md` 항목 추가 |

### run.json

```json
{"started": "ISO8601", "mode": "full|diff", "sources": ["kstartup"], "stage": "collect|review|verify|report|done",
 "baseline": "<직전 완료 실행 절대경로>|null", "stage_log": [{"stage": "…", "at": "ISO8601"}],
 "finished": "ISO8601", "report": "<프로젝트 상대경로>", "counts": {"kstartup": 262}, "candidates": 31, "verified": 31,
 "verdicts": {"A": 5, "B": 4, "C": 6}, "note": ""}
```

`started`, `mode`, `stage`는 생성 시부터 있다. 나머지는 단계에 따라 추가된다. 소비자는 없는 키를 허용해야 한다.

### queue.jsonl

```json
{"id": "q001", "type": "verify|manual|apply|followup|resurvey", "title": "…", "url": "", "source": "", "ref": "",
 "deadline": "YYYY-MM-DD|", "note": "", "run": "20260905|", "status": "open|done", "added": "YYYY-MM-DD", "closed": "YYYY-MM-DD"}
```

### worklog.md / decisions.md / profile.md

사람이 읽는 마크다운. 스크립트가 파싱하는 부분은 `profile.md`의 `- ` 줄과 `- 마지막 조사:` 줄뿐이다. 정확한 형식은 `references/workspace-format.md`가 사용자에게 약속한 것과 같다.

## 서브에이전트 입출력

- `ir-detail-verifier`: 입력 = `details/` 경로, `profile.md` 경로, 출력 경로. 출력 = JSONL, 필드 `source,id,url,title,pre_founder,age_gender_affil,region_residence,region_apply,support,exclusions,track_record,deadline,contact,body_in_attachment,evidence{},flags[]`. 실패 항목은 `{"source","id","error"}`
- `ir-report-reviewer`: 입력 = `report.md`, 실행 폴더, `.ir-search/`, 출력 경로. 출력 = `review-report.md` (결론 체크박스, 실패 표, 경고, 통과, 큐 제안)
