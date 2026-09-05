# ir-search

한국 정부·공공기관 지원사업을 전수조사해 프로젝트 적합성을 3단계(A 즉시 가능 / B 로드맵 / C 변형)로 판정하는 Claude Code 스킬. 사용자는 지원사업을 찾는 예비창업자·초기 스타트업이고, 스킬은 그들의 프로젝트 폴더 안에서 실행된다. 코드는 의존성 없는 Python 스크립트 4개(크롤러 2, diff 1, 상태 관리 1)와 마크다운(스킬 본문, 참조 문서, 서브에이전트 2개)이 전부다. 이 파일은 **이 저장소를 고치는 사람·에이전트**를 위한 것이고, 스킬 사용자를 위한 문서는 README다.

## 프로젝트 구조

```
ir-search/
├── CLAUDE.md / AGENTS.md          ← 이 문서 (내용 동일)
├── SKILL.md                       ← 스킬 본문: 워크플로 0~4단계 + 마무리. 루트에 있어야 단일 스킬 플러그인으로 인식됨
├── references/
│   ├── sources.md                 ← 소스 레지스트리: 검증된 URL·페이지네이션 방식·차단 사다리
│   ├── workspace-format.md        ← 사용자 프로젝트의 .ir-search/ 규격 (profile/worklog/queue/decisions/runs)
│   └── report-format.md           ← 보고서 템플릿, 검증 항목, A/B/C 판정 기준, 검수 체크리스트
├── scripts/
│   ├── AGENTS.md                  ← 스크립트 모듈의 경계·불변조건
│   ├── fetchlib.py                ← 공용 HTTP: TLS 지문 에스컬레이션, 차단 판정, 재시도, 지연, 날짜 유틸
│   ├── kstartup_crawl.py          ← K-Startup 목록/상세
│   ├── sources_crawl.py           ← 기업마당·NIPA·KOCCA·SMTECH 목록/상세
│   ├── diff_surveys.py            ← 두 실행 폴더 비교 (신규/마감변경/종료/미갱신 소스)
│   └── survey_state.py            ← .ir-search/ 상태: init/status/run/queue/decide
├── agents/
│   ├── ir-detail-verifier.md      ← 상세공고 구조화 추출 서브에이전트 (근거 인용 필수)
│   └── ir-report-reviewer.md      ← 보고서 검수 서브에이전트 (원문 대조)
├── tests/                         ← 합성 HTML·임시 워크스페이스로 도는 unittest (네트워크 없음)
├── docs/
│   ├── architecture.md            ← 스킬 실행 흐름과 파일 간 데이터 흐름
│   ├── business-rules.md          ← 판정 규칙, 불명 처리, diff 분류, 큐 종류의 의미
│   ├── security.md                ← 접근 범위, 개인정보, 공고 텍스트=데이터
│   ├── standards.md               ← 위반하면 깨지는 규칙
│   ├── engineering-notes.md       ← 사이트별 함정, 파서가 깨지는 방식
│   ├── operations.md              ← 설치·검증·배포(플러그인) 절차
│   ├── contracts.md               ← jsonl 스키마, CLI 인터페이스, 종료 코드
│   └── tracking/
│       ├── status.md              ← 구현/검증 현황과 남은 범위
│       ├── findings.md            ← 지금 못 푸는 문제
│       └── decisions/             ← 트레이드오프가 있었던 결정 (index.md + NNNN-*.md)
├── .claude-plugin/                ← plugin.json + marketplace.json
├── install.sh                     ← ~/.claude 또는 <project>/.claude에 심링크/복사
└── README.md / README.en.md       ← 사용자 문서
```

## 절대 규칙 (전체 목록은 docs/standards.md)

1. **SKILL.md는 루트에 남는다.** `skills/` 하위로 옮기면 `git clone → ~/.claude/skills/ir-search` 설치가 깨지고, 루트 SKILL.md + `skills/` 디렉터리가 공존하면 플러그인 로더가 루트를 무시한다.
2. **원문에 없는 값은 만들지 않는다.** 파서는 필드를 못 찾으면 빈 문자열, 스킬·에이전트는 '불명'. 기본값으로 그럴듯한 값을 채우는 코드는 거부한다.
3. **차단은 우회하지 않고 보고한다.** 로그인·CAPTCHA·robots 우회 코드 금지. `Blocked`는 예외로 올라가 "수동 확인"이 된다.
4. **스크립트는 표준 라이브러리만으로 돈다.** `curl_cffi`는 선택 의존성이며 없으면 urllib로 폴백해야 한다.
5. **`.ir-search/`의 파일 형식을 바꾸면 이전 워크스페이스를 읽을 수 있어야 한다.** `run.json`·`queue.jsonl`에 필드를 추가할 수는 있어도 이름을 바꾸거나 필수로 만들 수 없다.

## 작업 전 읽을 것

- 항상: `docs/standards.md`, `docs/engineering-notes.md`
- 파서를 고칠 때: `docs/engineering-notes.md`의 해당 소스 항목 + `references/sources.md`의 같은 소스 절 (둘 다 고쳐야 한다 — 하나는 사람용, 하나는 코드용)
- `survey_state.py`를 고칠 때: `references/workspace-format.md` (사용자에게 약속한 형식) + `docs/contracts.md`의 run.json/queue.jsonl 스키마
- SKILL.md를 고칠 때: `docs/business-rules.md`의 판정 규칙 — SKILL.md와 `references/report-format.md`, `agents/*.md`가 같은 규칙을 다른 높이에서 말하므로 한 곳만 고치면 어긋난다
- 새 소스를 추가할 때: `references/sources.md`의 "접근 시 공통 원칙" → `scripts/sources_crawl.py`의 `page_*` 패턴 → `tests/test_parsers.py`에 합성 HTML 픽스처

## 문제 보고

- **즉시 사용자에게**: 파서가 실제 사이트에서 0건을 내면서 종료 코드 0으로 끝나는 경우(조용한 커버리지 손실), 개인정보가 워크스페이스·보고서에 기록될 수 있는 경로, 차단 우회에 해당하는 변경 요청
- **그 외**: `docs/tracking/findings.md`에 "조건 → 증상 → 왜 지금 못 푸는지"로 기록
