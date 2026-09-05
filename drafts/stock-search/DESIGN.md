# stock-search — 한·미·일 상장기업 공시 전수조사 설계 초안

> 초안. 소스 URL·API 형식은 기억에 의존한 것이며 **실측 검증 전**이다. 숫자·한도는 전부 "확인 필요".

## 무엇을 하는 스킬인가

관심 종목·테마 프로필에 대해 한국(DART)·미국(EDGAR)·일본(EDINET·TDnet)의 **1차 공시 자료를 전수 수집**하고, 프로필 기준으로 검토·원문 검증한 뒤 "지금 봐야 할 것 / 조건 충족 시 봐야 할 것 / 관점을 바꾸면 관련 있는 것"으로 분류해 보고서와 기한 큐를 남긴다. ir-search가 "놓친 지원사업"을 없애듯, 이 스킬은 "놓친 공시"를 없앤다.

**하지 않는 것**: 매수·매도 판단, 목표가, 추천. 시세·차트. 뉴스·커뮤니티 요약(2차 자료). 보고서의 모든 수치는 공시 원문 인용이며, 공시에 없는 것은 '불명'이다. 이 경계는 SKILL.md·에이전트·보고서 한계 고지에 같은 문장으로 들어간다.

## 왜 ir-search와 같은 구조가 맞는가

| 실패 원인 (ir-search) | 공시에서의 대응물 |
|---|---|
| 키워드 검색의 사각지대 | 종목명 검색만 하면 자회사·합병 상대·대량보유자 명의로 올라온 공시를 놓친다 → 기간 내 전체 공시 목록을 받아 제목을 전부 읽는다 |
| 자격요건 오판 | 제목("유상증자 결정")만 보고 판단하면 조건(제3자배정 대상, 납입일, 할인율)을 놓친다 → 본문에서 확인 |
| 추정 보고 | "실적이 좋을 것" → 공시 수치와 기한만 적고 해석은 근거 문장과 함께 |

## 프로필 축 (`.stock-search/profile.md`)

- **관심 대상**: 종목 코드 목록(시장 접두: `KR:005930`, `US:AAPL`, `JP:7203`) 또는 테마(예: "음성 AI, TTS") — 둘 다 가능
- **시장 범위**: KR / US / JP 중 선택 (소스 구성의 근거)
- **관심 사건 종류**: 실적·가이던스 / 자본 변동(유상증자·전환사채·자사주) / 지배구조(대량보유·최대주주 변경·M&A) / 규제·소송 / 신규 사업·계약 — 복수 선택
- **관점**: 사업 이해(고객·경쟁사 추적) / 투자 검토 / 채용·영업 대상 조사 등 **왜 보는지** 한 줄. 판정의 기준이 된다
- **기록 금지**: 보유 수량·평단·계좌·증권사. 프로필과 보고서 어디에도 넣지 않는다

## 소스 (references/sources.md에 상세)

| 시장 | 소스 | 접근 | 핵심 | 검증 상태 |
|---|---|---|---|---|
| KR | DART OpenAPI | 무료 키 (opendart.fss.or.kr) | 공시검색 `list.json` (기간·회사·유형), 문서 원문 zip | 미검증 |
| KR | KIND (krx) | HTML | 상장공시·시장조치 (DART에 없는 거래소 공시) | 미검증 |
| US | SEC EDGAR | 무료, User-Agent에 연락처 필수, 10 req/s | `data.sec.gov/submissions/CIK…json`, full-text search `efts.sec.gov`, 8-K/10-Q/10-K/13D/13G/S-1 | 미검증 |
| JP | EDINET API v2 | 무료 키 (Subscription-Key) | 일자별 제출 목록 `documents.json?date=…&type=2`, 有価証券報告書·大量保有報告書 | 미검증 |
| JP | TDnet 適時開示 | HTML (공식 API 없음) | 決算短信·業績修正·自己株式 — 当日·過去 목록 페이지 | 미검증, 차단 가능성 |
| JP | JPX 決算発表予定日 | CSV/HTML | 기한 큐의 재료 | 미검증 |

원칙은 ir-search와 같다: 공개 자료만, 키가 필요한 API는 사용자 키를 환경변수로(`DART_API_KEY`, `EDINET_API_KEY`, `SEC_USER_AGENT`), 없으면 그 소스는 "수동 확인"으로 보고. 우회 없음.

## 레코드 스키마 (jsonl, `(source, id)` 키)

```json
{"source": "dart", "id": "20260905000123", "market": "KR", "ticker": "005930", "company": "삼성전자",
 "title": "주요사항보고서(유상증자결정)", "type": "주요사항보고서", "filed": "2026-09-05", "deadline": "2026-09-19",
 "url": "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260905000123"}
```

`deadline`은 공시가 만드는 **기한**(청약일·납입일·주총일·배당기준일·공개매수 종료일)이며, 없으면 빈 값. diff의 "마감 변경"이 여기 걸린다. `filed`는 제출일. 전 소스 공통 필드로 두고, 소스 고유 필드(EDGAR `form`, EDINET `docTypeCode`)는 추가 필드.

## 워크플로 (SKILL.md 초안 참조)

```
0 status → profile 확인 (없으면 한 번에 질문)
1 수집: run new → 시장별 크롤러가 [직전 완료 실행 이후 ~ 오늘] 기간의 전체 공시 목록을 jsonl로
        (첫 실행은 --since 90d 기본. 테마 프로필이면 전 종목 목록에서 제목 검토, 종목 프로필이면 그 종목 + 연관 명의)
2 검토: 모델이 목록 전체를 읽고 프로필 사건 종류에 맞는 후보를 큐(verify)에
3 검증: 원문(DART 문서 zip → 텍스트, EDGAR 본문 HTML, EDINET PDF/XBRL, TDnet PDF)에서 수치·기한·조건을 근거 인용
        15건 이상 → stock-filing-verifier 서브에이전트 (추출만)
4 판정: A 즉시 검토(기한 있음 또는 프로필 사건 발생) / B 트리거 대기 / C 관점 전환 → report.md
마무리: stock-report-reviewer 검수 → queue(event 기한·followup·resurvey) → run finish → status
```

diff 모드는 ir-search와 같되, 공시는 사라지지 않으므로 CLOSED 분류는 "기한 경과"로 의미가 바뀐다. 즉 `deadline < today`인 직전 A항목 → "기한 지남" 알림 후 큐 닫기.

## A / B / C 정의 (확정 필요)

| 등급 | 조건 | 반드시 적을 것 |
|---|---|---|
| A 즉시 검토 | 프로필의 관심 사건 종류에 해당하고, 기한이 있거나(청약·주총·공개매수) 사실이 이미 발생(실적 확정·최대주주 변경) | 공시 수치(원문 인용), 기한과 시각, URL |
| B 트리거 대기 | 조건부 사건: "승인 시", "주총 결의 시", "가이던스 달성 시" — 트리거가 공시에 명시 | 트리거 문장, 예상 시점(공시에 있으면) |
| C 관점 전환 | 프로필 종목·테마 밖이지만 재해석하면 관련(경쟁사 대형 수주, 고객사 투자 축소, 규제 변경) | 왜 관련인지 한 문장 + 리스크 |
| 제외 | 정기·형식 공시(임원 소량 거래, 정정 없는 반복) | 건수만 한계 고지에 |

**미결**: 이 정의가 "공시 모니터링" 용도에 맞다. 만약 용도가 "종목 발굴(스크리닝)"이면 1단계가 재무 데이터(DART 재무 API, EDGAR XBRL frames)가 되고 판정 축이 달라진다. 사용자 확인 후 확정.

## 워크스페이스 `.stock-search/`

ir-search의 `.ir-search/`와 같은 파일 다섯 개. 다른 점:

- `queue.jsonl`의 `type`: `verify` / `event`(기한 있는 사건: 청약·주총·배당기준일) / `followup`(추가 공시 대기) / `manual`(차단·키 없음) / `resurvey`. `apply`는 없다
- `profile.md`에 `관심 대상` 줄이 여러 종목 코드를 담으므로 스크립트가 파싱하는 유일한 줄은 `마지막 조사`뿐 (ir-search와 동일 규칙)
- `runs/<날짜>/`에 `dart.jsonl`·`edgar.jsonl`·`edinet.jsonl`·`tdnet.jsonl` + `details/` (공시 원문 텍스트, PDF는 텍스트 추출본)

## 스크립트 (전부 미작성)

| 파일 | 역할 | 출처 |
|---|---|---|
| `fetchlib.py` | 그대로 복사. EDGAR는 User-Agent 필수라 `Fetcher(user_agent=…)` 인자 추가 필요 | ir-search |
| `dart_crawl.py` | `list` (기간·종목·유형) / `detail` (rcpNo → 원문 zip → 텍스트) | 신규 |
| `edgar_crawl.py` | `list` (CIK 또는 full-text 쿼리, 기간) / `detail` (accession → 본문) | 신규 |
| `edinet_crawl.py` | `list` (일자 반복) / `detail` (docID → PDF/XBRL → 텍스트) | 신규 |
| `tdnet_crawl.py` | `list` (일자별 適時開示 페이지) / `detail` (PDF → 텍스트) | 신규, 차단 시 EDINET·JPX로 대체 |
| `diff_surveys.py` | 그대로. `apply_end` 대신 `deadline`을 보게 필드명 매핑 한 줄 | ir-search |
| `survey_state.py` | 그대로 + 워크스페이스명 인자 + 큐 종류 표 | ir-search |

PDF → 텍스트는 표준 라이브러리로 안 된다. 선택 의존성(`pdfminer.six` 또는 `pypdf`)으로 두고, 없으면 "본문은 PDF 참조 + URL"로 기록 (ir-search의 "본문은 첨부 참조" 규칙과 같다).

## 함정 (예상, 실측 필요)

- DART 일일 호출 한도(10,000회로 기억)·문서 zip 인코딩(EUC-KR 섞임)
- EDGAR: User-Agent 없으면 403, 초당 10회 초과 시 차단. full-text search는 2001년 이후만
- EDINET: 일자별 호출이라 90일이면 90회. 大量保有報告書는 발행사 코드가 아닌 제출자 기준
- TDnet: 정적 페이지지만 당일 목록만 가볍고 과거는 일자 파라미터. 차단되면 EDINET에는 決算短信이 없으므로 결손 명시
- 한 사건이 3국에 동시 공시(ADR 상장사)되면 `(source,id)`가 셋 — 병합은 모델이 보고서에서 (ir-search findings 2번과 같은 미해결)
- 배당기준일·주총일은 공시 본문에만 있고 목록에는 없다 → `deadline`은 3단계 검증 후 채워지는 필드. 1단계에서는 빈 값이 정상

## 하네스

ir-search와 같은 슬롯. `docs/security.md`에 "보유 정보 기록 금지"와 "투자 판단 안 함"을 첫 줄로. `docs/business-rules.md`에 A/B/C 정의와 '불명' 규칙.
