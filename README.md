<samp>🇰🇷 한국어 · [🇺🇸 English](README.en.md)</samp>

# ir-search

> ⚠️ **한국(대한민국) 정부·공공기관 지원사업 전용**입니다. 다른 국가의 지원 프로그램은 다루지 않습니다.

한국 정부·공공기관 **지원사업 전수조사** Claude Code 스킬.

K-Startup·기업마당(bizinfo)·NIPA·KOCCA·SMTECH의 모집중 공고를 크롤링해서, 현재 작업 중인 프로젝트(아이템)의 프로필 — 창업 단계·지역·필요(자금/공간/R&D) — 에 맞는 사업을 골라내고, 상세공고 원문으로 자격요건을 검증한 뒤 3단계로 분류한 보고서를 만들어 줍니다:

- **A그룹 — 지금 즉시 지원 가능**: 현재 신분 그대로 자격 충족 (마감순, 임박 강조)
- **B그룹 — 요건 충족 시 (로드맵)**: 법인 설립·투자유치 등 트리거와 연쇄 경로 명시
- **C그룹 — 변형하면 가능**: 아이템을 다른 분야 언어로 재서술하는 프레이밍 각도 제안

키워드 검색이 아니라 전수 검토를 하는 이유: "AI 스타트업"이 지원할 수 있는 콘텐츠 제작지원·예술×기술 입주·사회서비스 창업지원 같은 사업은 키워드로 잡히지 않기 때문입니다.

## 반복 사용을 전제로 한 설계 (v3)

조사 상태는 프로젝트 폴더의 **`.ir-search/`** 에 남습니다. 대화 기억이 아니라 파일이 기준이라, 세션이 끊기거나 다른 기기·다른 사람이 이어받아도 같은 지점에서 계속됩니다.

```
<project>/.ir-search/
├── profile.md        신청자(아이템) 프로필 — 다음 조사부터 "바뀐 것 있나요?" 한 번만 확인
├── worklog.md        실행 기록 — 언제 어떤 소스를 몇 건 조사해 A/B/C 몇 건이 나왔나
├── queue.jsonl       할 일 — 검증 대기 / 수동 확인 / 신청 진행 / 후속 확인 / 재조사 예정 (D-day 포함)
├── decisions.md      판정·구성 결정과 이유 — 왜 B로 내렸나, 왜 그 소스를 뺐나
└── runs/YYYYMMDD/    한 번의 조사: 원시 jsonl + 상세 원문 + report.md + 단계 마커
```

- **재개**: 후보 30건을 검증하다 세션이 끊기면, 다음 세션은 `status` 한 번으로 "verify 단계, 큐에 12건 남음"을 보고 이어갑니다
- **재조사**: 직전 실행과 자동 비교(diff)해 **신규 / 마감 변경 / 종료된 기회**만 증분 보고합니다. 250건+를 매번 다시 읽지 않습니다
- **큐**: 조사가 끝난 뒤에도 "9/8 16:00까지 청창사 신청", "9/26 재조사"가 D-day와 함께 남습니다. 채팅 응답 끝에 항상 붙습니다

## 산출물 예시 (발췌)

```markdown
# 지원사업 전수조사 — ○○ (AI 음성 SaaS, 예비창업자, 충남)
조사일 2026-09-05 · K-Startup 262건 + 기업마당 300건 전수 검토 → 후보 31건 상세 검증

## A그룹 — 지금 즉시 지원 가능 (마감순)

1. **2026 청년창업사관학교 추가모집** — 중소벤처기업진흥공단
   - 지원: 사업화 자금 최대 1억 원 + 입주공간 + 멘토링
   - 자격: 예비창업자 포함 ✓ · 만 39세 이하 ✓ · 전국 접수 ✓
   - 마감: 2026-09-08 16:00 (D-3) ⚠️ 임박
   - https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=1784xx

## B그룹 — 요건 충족 시 열림 (로드맵)

- **프리팁스(Pre-TIPS)**: 트리거 = 비수도권 법인 설립.
  연쇄 경로: 경진대회 상금·시드 → 충남 법인 설립 → 프리팁스 → TIPS
  - https://www.k-startup.go.kr/...&pbancSn=1779xx

## C그룹 — 변형(프레이밍)하면 가능

- **콘텐츠 제작지원 (KOCCA)**: "AI 음성 기술"이 아니라 "오디오 콘텐츠
  제작 파이프라인"으로 재서술하면 대상. 리스크: 결과물이 콘텐츠여야 함
  - https://www.kocca.kr/...

## 부재 확인
- 예비창업패키지: 현재 모집중 아님 (통상 2월 공고 — 재조사 큐 등록)

## 우선순위 액션
- ~9/8: A-1 청창사 신청 (16:00 마감 주의)
- ~9/15: C-1 콘텐츠 프레이밍 초안 작성 후 문의처 유선확인
```

모든 공고에 원문 URL이 붙고, 공고에 없는 정보는 추정하지 않고 '불명'으로 표기합니다. 보고서는 전달 전에 검수 에이전트가 원문과 대조합니다 (URL 누락·원문에 없는 수치·임박 표기 누락).

## 커버 소스

| 소스 | 내용 | 크롤러 |
|---|---|---|
| [K-Startup](https://www.k-startup.go.kr) | 창업지원 통합 (기본) | `kstartup_crawl.py` |
| [기업마당](https://www.bizinfo.go.kr) | 전 부처·지자체 중소기업 지원 (최대 커버리지) | `sources_crawl.py` |
| [NIPA](https://www.nipa.kr) | AI/ICT 사업 | `sources_crawl.py` |
| [KOCCA](https://www.kocca.kr) | 콘텐츠 지원 | `sources_crawl.py` |
| [SMTECH](https://www.smtech.go.kr) | 중기부 R&D | `sources_crawl.py` |

그 외 소스(NIA·IITP·IRIS·지역기관 등)는 `references/sources.md`의 레지스트리 참조. 차단되면 TLS 지문 사다리(safari → safari_ios → chrome → chrome_android → 모바일 호스트)를 자동으로 타고, 그래도 안 되면 그 소스는 "수동 확인"으로 보고합니다 — 로그인·CAPTCHA 우회는 하지 않습니다.

## 설치

세 방식 중 하나. 결과는 같습니다.

```bash
# A. 클론 + 심링크 (git pull이 곧 업데이트). 스킬 + 서브에이전트 2개를 ~/.claude에 링크
git clone https://github.com/mobiaiinc/ir-search.git && cd ir-search && ./install.sh

# B. 특정 프로젝트에만
./install.sh --project ~/work/my-startup

# C. 플러그인 마켓플레이스 (Claude Code 안에서)
/plugin marketplace add mobiaiinc/ir-search
/plugin install ir-search@ir-search
```

```bash
pip install 'curl_cffi>=0.15'   # 권장 (TLS 지문 차단 회피). 없으면 urllib로 폴백
```

## 사용

Claude Code에서 프로젝트 폴더를 연 상태로:

```
우리 아이템에 맞는 지원사업 전수조사 해줘
```

또는 `/ir-search` (플러그인 설치 시 `/ir-search:ir-search`). Claude가 `.ir-search/`의 상태를 확인하고, 프로필이 없으면 폴더에서 프로젝트 정보를 읽은 뒤 비는 항목(창업 단계·지역·필요한 것)만 한 번에 물어보고 조사를 시작합니다.

이후에는:

```
새로 나온 지원사업 있나?        → 직전 실행과 diff, 신규·마감변경·종료만 보고
지원사업 큐 보여줘              → 열린 할 일과 D-day
```

크롤러와 상태 도구는 단독으로도 쓸 수 있습니다:

```bash
python3 scripts/kstartup_crawl.py list -o all.jsonl --drop-expired         # K-Startup 모집중 전수
python3 scripts/kstartup_crawl.py detail 178481 -o details/                # 상세공고 원문
python3 scripts/sources_crawl.py list bizinfo -o biz.jsonl --max-pages 20  # 기업마당
python3 scripts/sources_crawl.py list all -o sources.jsonl                 # 4개 소스 일괄
python3 scripts/diff_surveys.py <직전 실행 폴더> <이번 실행 폴더> --out new.jsonl
python3 scripts/survey_state.py status                                     # 프로필·실행·큐 요약
python3 scripts/survey_state.py queue list                                 # 할 일 + D-day
```

## 구성

```
ir-search/
├── SKILL.md                    # 워크플로 (상태 확인 → 프로필 → 전수수집 → 전수검토 → 상세검증 → 3분류 → 검수 → 상태 갱신)
├── scripts/
│   ├── fetchlib.py             # 공용 HTTP: 지문 사다리·차단 판정·재시도·지연·날짜 유틸
│   ├── kstartup_crawl.py       # K-Startup 크롤러
│   ├── sources_crawl.py        # 기업마당·NIPA·KOCCA·SMTECH 크롤러
│   ├── diff_surveys.py         # 재조사 증분 비교 (신규/마감변경/종료/미갱신 소스)
│   └── survey_state.py         # .ir-search/ 워크스페이스 (init / status / run / queue / decide)
├── agents/
│   ├── ir-detail-verifier.md   # 상세공고 구조화 추출 (근거 인용 필수) — 후보 15건 이상일 때
│   └── ir-report-reviewer.md   # 보고서 검수 (원문·큐 대조)
├── references/
│   ├── sources.md              # 소스 레지스트리 (검증된 접근법 + 보조 소스)
│   ├── workspace-format.md     # .ir-search/ 파일 규격
│   └── report-format.md        # 보고서 템플릿·검증 항목·판정 기준·검수 체크리스트
├── tests/                      # 네트워크 없는 unittest (합성 HTML, 임시 워크스페이스)
├── docs/                       # 기여자용: 구성·도메인 규칙·표준·엔지니어링 노트·운영·계약 + tracking/
├── CLAUDE.md / AGENTS.md       # 이 저장소를 고치는 에이전트를 위한 진입점
├── install.sh                  # 로컬 설치 (심링크/복사, 사용자/프로젝트 단위)
└── .claude-plugin/             # 플러그인 매니페스트
```

## 개발

```bash
python3 -m unittest discover -s tests -v   # 네트워크 없이 돕니다
```

파서를 고쳤으면 네트워크 있는 환경에서 실사이트 스모크(`list --max-pages 2`)를 돌리고 `references/sources.md`의 실측 날짜를 갱신하세요. 규칙과 함정은 `docs/`에 있습니다.

## 주의

- 공고 내용(마감일·자격요건·금액)은 수시로 바뀝니다. **신청 전 반드시 접수기관에 확인**하세요. 이 스킬의 산출물은 조사 시점의 공고 텍스트 기준입니다.
- 공개 공고 페이지만 접근하며 요청 간 지연을 둡니다. 대상 사이트의 이용약관을 존중해 주세요.
- `.ir-search/`에는 프로필 축(창업 단계·지역·연령대 등) 외의 개인정보를 넣지 않습니다. git에 올릴지는 프로젝트가 정합니다 (`runs/*/details/`는 크므로 보통 제외).

## License

MIT · 원저작: [djfksjd/ir-search](https://github.com/djfksjd/ir-search)
