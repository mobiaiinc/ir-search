# stock-search 소스 레지스트리 (초안 · 전부 미검증)

접근 전 첫 페이지/첫 호출로 형식을 확인하고, 확인 날짜를 각 항목에 적는다. 키가 필요한 API는 환경변수로 받고, 없으면 그 소스는 "수동 확인".

## 한국

- **DART OpenAPI** — https://opendart.fss.or.kr — 무료 인증키(`DART_API_KEY`)
  - 공시검색: `https://opendart.fss.or.kr/api/list.json?crtfc_key=…&bgn_de=YYYYMMDD&end_de=YYYYMMDD&page_count=100&page_no=N` (`corp_code`·`pblntf_ty`로 좁힘). 페이지네이션 `page_no`
  - 원문: `https://opendart.fss.or.kr/api/document.xml?crtfc_key=…&rcept_no=…` → zip(XML/HTML)
  - 사람용 URL: `https://dart.fss.or.kr/dsaf001/main.do?rcpNo=<rcept_no>`
  - 한도: 일 10,000회로 기억. 회사 코드는 `corpCode.xml` 일괄 다운로드
- **KIND** — https://kind.krx.co.kr — 거래소 공시·시장조치(관리종목, 거래정지). HTML 폼 POST 페이지네이션 추정

## 미국

- **SEC EDGAR**
  - 회사별 제출 목록: `https://data.sec.gov/submissions/CIK##########.json` (10자리 0패딩)
  - 전문 검색: `https://efts.sec.gov/LATEST/search-index?q="…"&dateRange=custom&startdt=…&enddt=…&forms=8-K`
  - 원문: `https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-no-dashes>/<primary-doc>`
  - 규칙: `User-Agent: <회사명> <이메일>` 필수(`SEC_USER_AGENT`), 초당 10회 이하. 티커→CIK는 `company_tickers.json`
  - XBRL 재무: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` (스크리닝 용도로 확장 시)

## 일본

- **EDINET API v2** — https://api.edinet-fsa.go.jp — 무료 키(`EDINET_API_KEY`, 헤더 `Subscription-Key` 또는 쿼리)
  - 일자별 목록: `/api/v2/documents.json?date=YYYY-MM-DD&type=2`
  - 원문: `/api/v2/documents/<docID>?type=1`(zip: XBRL) / `type=2`(PDF)
  - 사람용 URL: `https://disclosure2.edinet-fsa.go.jp/…` (docID 기반, 형식 확인 필요)
  - 커버: 有価証券報告書·四半期報告書·臨時報告書·大量保有報告書. **決算短信은 없다** (TDnet)
- **TDnet 適時開示** — https://www.release.tdnet.info/inbs/I_main_00.html — 공식 API 없음
  - 당일 목록 정적 HTML, 과거는 `I_list_001_YYYYMMDD.html` 꼴로 기억. PDF 링크
  - 차단·구조 변경 가능성 높음. 실패 시 "決算短信 미수집" 명시
- **JPX** — 決算発表予定日 목록(CSV/HTML), 상장 종목 일람(Excel) — 기한 큐·종목 마스터

## 공통 원칙

- 공개 자료만. 로그인·유료 단말 우회 없음
- 2차 자료(뉴스·블로그·커뮤니티)는 소스가 아니다. 보고서에 인용하지 않는다
- 시세는 다루지 않는다. 필요하면 사용자가 별도 확인
