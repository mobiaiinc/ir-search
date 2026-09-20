# 화이트스페이스 조사 A — 부동산·커뮤니티·포인트 (한일 크로스보더 신사업 후보 12건)

- 조사일: 2026-09-20
- 전제: `docs/japan-monthly-c2c-strategy-2026-09.md` 0·12·13절(도쿄 외국인 먼슬리 + AI 보증 내재화, 택건업 면허·家賃債務保証業 등록 예정, 대표 경영·관리 비자, 개발자 1명, 택건사 채용) 및 `docs/foreigner-monthly-strategy-2026-09.md` 0절(한국 외국인관광 도시민박 → 랜딩 윈도우 먼슬리)을 출발점으로, **한일 크로스보더에서 (a) 거의 아무도 하지 않고 (b) 성장 근거가 문서화되어 있으며 (c) 당사 자산(외국인 주거·납부 데이터, 한국 게스트 채널, 일본 면허, AI/개발)으로 선점 가능한** 신사업 후보를 부동산·커뮤니티·포인트 3개 도메인에서 발굴.
- 방법: WebSearch 150회(본체 43회 + 서브에이전트 2개 55회·52회, 한·일·영 쿼리). 원문 페이지 다수가 프록시 차단이라 **검색 스니펫 기준**이며, 모든 수치 뒤에 [출처 URL]을 병기하고 검증 불가 항목은 **미확인**으로 표기. 존재 검증에서 직접 플레이어 3개 이상이면 "이미 존재"로 표기.
- 서브에이전트 원본: 부동산 5개 시드(A~E)·커뮤니티/포인트 4개 시드(F~I) 조사 노트는 세션 스크래치에만 존재하며 본 문서에 통합.

---

## 0. 결론 요약

1. **진짜 공백은 "데이터 레이어"에 있다.** 한일 양국에서 외국인 주거·정착 서비스(중개·슈퍼앱·보증)는 각국 단일 시장에 이미 3개 이상 존재한다(일본 GTN·YOLO JAPAN·Guidable, 한국 한패스·하이어다이버시티·엔코). 그러나 **한 사람의 한국 체류 이력과 일본 체류 이력을 잇는 사업자는 검색상 하나도 없다.** 당사만 양국 면허·재고·납부 데이터를 동시에 갖게 되므로, 1순위는 **크로스보더 임차 이력 스코어(Rent-Passport) API**다.
2. **부동산 도메인에서 가장 비어 있는 것은 "호스트 금융"과 "管理組合 외국인 거버넌스"다.** 민박·먼슬리 호스트에게 예약·임대료 채권을 선지급하는 사업자는 일본·한국 모두 미확인(글로벌은 Guesty Capital·Host Financial 정도)이고, 외국인 구분소유자 급증에 대응하는 管理組合용 다국어 총회·규약·체납 SaaS도 컬럼만 있고 사업자가 없다.
3. **空き家·토큰·포인트는 "성장은 크지만 공백이 아니거나 규제가 벽"이다.** 空き家 외국인 구매 중개는 영어권에 7개 이상, 일본 부동산 ST는 누적 3,000억엔대로 이미 성숙, 한일 결제 브리지는 PayPay·카카오페이·GLN이 선점했고 포인트 상호전환은 자금결제법·전금법 이중 라이선스가 필요하다. 이 셋은 "당사가 공급자/파트너로 참여"하는 형태로만 의미가 있다.
4. **한일 인적 교류는 2026년에도 두 자릿수 성장 중이다.** 2025년 방일 한국인 946만·방한 일본인 365만(합산 약 1,311만, 사상 최다), 2026년 1~8월 방일 한국인 +21.2%, 1~7월 방한 일본인 +18.8%. 재류외국인 412만(+9.5%), 한국 체류외국인 287만(+5.2%). 성장 근거는 모든 후보에 공통으로 충분하다.
5. **상위 5개(스코어링 결과)**: ① 크로스보더 Rent-Passport 스코어 API ② 管理組合 외국인 거버넌스 SaaS ③ 민박·먼슬리 호스트 매출 선지급 ④ 해외 팬 대상 관계인구 멤버십 ⑤ 한국인 비거주 오너의 도쿄 물건 → 외국인 먼슬리 운영·보증 위탁. 모두 본체 먼슬리 플랫폼의 데이터·면허를 재사용하며, ①·③은 家賃債務保証業 등록과 동시에 착수 가능하다.

---

## 1. 매크로 수치 (2025–2026)

### 1.1 한일 인적 교류

| 항목 | 수치 | 시점 | 출처 |
|---|---|---|---|
| 방일 한국인 연간 | 945만9,600명(+7.3%), 소비 9,864억엔, 국적별 1위 | 2025 | [訪日ラボ](https://honichi.com/news/2026/02/10/inbound-korea-2025/) |
| 방일 외국인 총계 | 4,268만3,600명(+15.8%), 첫 4,000만 돌파 | 2025 | [やまとごころ](https://yamatogokoro.jp/inbound_data/59128/) |
| 방일 한국인 월간 | 2026-08 85만500명(+28.7%, 8월 사상 최다) / 1~8월 누계 742만300명(+21.2%) | 2026 | [JNTO](https://www.jnto.go.jp/news/press/20260916_montly.html), [トラベルボイス](https://www.travelvoice.jp/20260916-160529) |
| 방일 총계 2026 | 8월 309만8,900명(−9.6%, 중국 부진) / 상반기 2,108만(−2.0%) | 2026 | [やまとごころ](https://yamatogokoro.jp/inbound_data/61261), [やまとごころ](https://yamatogokoro.jp/inbound_data/60728/) |
| 방한 일본인 연간 | 365만명(중국 548만·대만 189만·미국 148만; 총 1,894만) | 2025 | [아주경제](https://www.ajunews.com/view/20260130103801235) |
| 방한 일본인 2026 | 1~7월 228만(+18.8%), 일본인 해외여행지 1위 한국 | 2026 | [뉴스핌](https://www.newspim.com/news/view/20260831000073) |
| 한일 왕래 합계 | 2024년 1,200만 초과 / 2025년 1,300만 초과, 사상 최다 | 2025 | [時事](https://www.jiji.com/jc/article?k=2026013001081&g=int), [トラベルボイス](https://www.travelvoice.jp/20250421-157525) |
| 대일 여행수지 | 적자 8.7조원, 사상 최대 | 2025 | [네이트뉴스](https://m.news.nate.com/view/20260623n33533) |
| 한일 항공 좌석 | 주 34만9,000석(2025말 대비 +2.4%) | 2026-07 | [뉴스핌](https://www.newspim.com/news/view/20260831000073) |

### 1.2 체류·재류 외국인

| 항목 | 수치 | 시점 | 출처 |
|---|---|---|---|
| 일본 재류외국인 | 412만5,395명(+9.5%, +35만6,418), 첫 400만 돌파 | 2025말 | [時事](https://www.jiji.com/jc/article?k=2026032700900&g=pol) |
| 국적별 | 중국 93만4,208 · 베트남 68만1,100 · **한국 40만7,341** | 2025말 | [nippon.com](https://www.nippon.com/ja/japan-data/h02750/) |
| 자격별 | 영주 94만7,125 · 기술·인문·국제 47만5,790 · 유학 46만4,784 · 특정기능 39만296 | 2025말 | [時事](https://www.jiji.com/jc/article?k=2026032700900&g=pol), [tokuteiginou-saiyo](https://tokuteiginou-saiyo.com/visa/tokutei-ginou-390k-foreign-residents-2025) |
| 일본 내 외국인 유학생 | 40만8,069명(+21.2%) | 2025-05 | [서울신문](https://www.seoul.co.kr/news/economy/2026/08/21/20260821500049) |
| 한국 체류외국인 | 287만4,278명(+5.2%), 등록 163만6,922(57.0%), 연내 300만 전망 | 2026-06 | [법무부](https://www.moj.go.kr/bbs/immigration/227/608714/artclView.do) |
| 재한 일본인 | 43,064명(2024-10-01) / 44,471명(2025-10-01, 外務省 海外在留邦人数調査 스니펫, 원문 미확인) | 2024–2025 | [data-seisaku](https://data-seisaku.com/00300-mofa-00300100-0000-full-list/), [JETRO 검색 스니펫](https://www.jetro.go.jp/world/reports/2025/01/231fa237934b5b0c.html) |
| 한국 내 일본 국적 유학생 | 3,872명(학사 1,682·어학원 1,208·교환 576) | 2025-12 | [K-Study Times](https://kstudytimes.kr/students-by-country/jp) |
| 한일 워킹홀리데이 | 양국 각 연 상한 1만명, 2025-10-01부터 생애 2회 | 2025 | [주한일본대사관](https://www.kr.emb-japan.go.jp/itpr_ko/working_holiday_2025..html), [3d-universal](https://3d-universal.com/blogs/2025/08/korea-working-holiday-visa.html) |
| 일본 디지털노마드 비자 | 646건(전년 257건의 2.51배); 상위 공관 시드니 57·시카고 41, 한국 공관 상위 미포함 | 2025 | [PR TIMES/JDNA](https://prtimes.jp/main/html/rd/p/000000024.000126832.html), [観光経済新聞](https://www.kankokeizai.com/2608181800kks/) |
| 한국 기업 일본 신설법인 | 2024년 314社(사상 최다) / 2025년 1~6월 218社 | 2025 | [JETRO](https://www.jetro.go.jp/biz/areareports/special/2025/0101/7645e965c3fc0e32.html), [日経](https://www.nikkei.com/article/DGXZQOGM263SD0W5A221C2000000/) |

### 1.3 일본 부동산·외국인 투자

| 항목 | 수치 | 시점 | 출처 |
|---|---|---|---|
| 도쿄 신축맨션 해외거주자 취득 비율 | 도내 3.0% · 23구 3.5%(전년 1.6%) · 도심 6구 7.5%; 23구 308호 중 대만 192·중국 30·싱가포르 21 | 2025 상반기 | [nippon.com](https://www.nippon.com/ja/japan-data/h02624/) |
| 해외투자자 일본 부동산 매입액 | 1조1,400억엔, 사상 최대 | 2026 상반기 | [한국경제](https://www.hankyung.com/article/2026082776251) |
| 도쿄 23구 신축 평균가 | 2026-05 1억6,286만엔(+15.9%); 2022년 8,236만엔 → 4년 약 2배; 한국 자산가 매입 문의 2배 | 2026 | [한국경제](https://www.hankyung.com/article/2026082776251) |
| 도쿄 23구 평균 맨션가 | 1억3,613만엔(+21%) | 2025 | [헤럴드경제](https://biz.heraldcorp.com/article/10800511) |
| 정기차가 비중 | 도쿄 23구 2025년도 9.2%(5년 연속 상승), 미나토구 37.5%; LIFULL 도쿄 9.3%(3년 +3.6pt) | 2025 | [健美家](https://www.kenbiya.com/ar/ns/jiji/purchase_know_how/10182.html), [LIFULL](https://lifull.com/news/45896/) |
| 외국인 입거 거절 | 日管協 조사 외국인 입주자 22% 거절 경험 · LIFULL 40.5% 차별 경험 · 외국인 트러블률 1.5% | 2025 | [SUUMO](https://suumo.jp/journal/2025/12/25/214133/), [LIFULL HOME'S](https://www.homes.co.jp/cont/press/rent/rent_01190/) |
| 家賃債務保証 시장 | 2024년도 2,548억5,700만엔(+6.7%) → 2025년도 2,723억9,000만엔(+6.9%) → 2029년도 3,500억엔 초과 예측 | 2025 | [矢野経済](https://www.yanoict.com/summary/show/id/776) |
| 民泊 届出住宅 | 42,070건(가동), 누적 届出 65,837 · 폐지 23,767(약 36%) | 2026-07-15 | [観光庁](https://www.mlit.go.jp/kankocho/minpaku/business/host/construction_situation.html) |
| 空き家 | 900만호 · 13.8%(2018년 849만 대비 +51만); 방치성 385만호 | 2023-10 | [BUILT](https://built.itmedia.co.jp/bt/articles/2405/08/news058.html), [LIFULL Business](https://biz.homes.jp/column/topics-00124) |
| 不動産ST | 누적 발행 약 2,600억엔(2025-12); 大和総研 2025말 3,003억엔 → 2026말 5,225억엔 예측; 野村 공모ST 2025년도 누적 3,333억엔(전년 2배) | 2026 | [zenn/komlock](https://zenn.dev/komlock_lab/articles/japan-real-estate-security-token-market), [大和総研](https://www.dir.co.jp/report/research/capital-mkt/it/20260126_025555.pdf), [野村HD](https://www.nomuraholdings.com/jp/news/nr/bstr20260402.html) |

### 1.4 2026년 정책 변화 (양국)

| 정책 | 내용 | 시점 | 출처 |
|---|---|---|---|
| 일본 외국인 정책 사령탑 | 「外国人との秩序ある共生社会推進室」 2025-07-15 발족, 담당대신 2025-11-04, 「総合的対応策」 2026-01-23 각료회의 | 2025–26 | [stepjob](https://stepjob.jp/gaikokujinseisaku/), [首相官邸](https://www.kantei.go.jp/jp/singi/gaikokujinzai/kakuryokaigi/dai2/shiryo1-4.pdf) |
| 외국인 토지취득 규제 | 2026-04부터 외국법인 대규모 토지(상업·주거 2,000㎡/농지 5,000㎡/산림 10,000㎡) 취득 시 대표자 국적 신고; 2026-03-04 「外国人による土地取得等のルールの在り方検討会」 초회; 2026년 여름까지 새 룰 골격, 통상국회 법안 방침 | 2026 | [日経](https://www.nikkei.com/article/DGXZQOUA160O90W5A211C2000000/), [内閣官房](https://www.cas.go.jp/jp/seisaku/symbiotic_society/gaikokujin_tochishutoku/kaisai-jokyo/dai1/shiryo3.pdf), [TMI](https://www.tmi.gr.jp/eyes/blog/2026/18051.html), [衆議院調査局](https://www.shugiin.go.jp/internet/itdb_rchome.nsf/html/rchome/shiryo/202602_real_estate_acquisition_by_foreign_nationals.pdf/$File/202602_real_estate_acquisition_by_foreign_nationals.pdf) |
| 특정재류카드 | 재류카드+마이넘버 일체화 2026-06-14 운용 개시; JESTA 2028년도 | 2026 | [外国人プレス](https://www.gaikokujin-press.com/archives/2961) |
| 空き家 세제 | 2023-12 空家法 개정 「管理不全空家」 권고 시 住宅用地特例 제외(고정자산세 최대 6배); 3,000만엔 양도소득 특별공제 2027-12-31 만료 | 2023–27 | [全日](https://magazine.zennichi.or.jp/legal-reform/15357), [国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/joto/3306.htm) |
| 관계인구·二地域居住 | 二地域居住促進法 2024-11-01 시행, 官民PF 709 자치체·197 기업; 関係人口 2,263만(18세 이상 22%), 2032년도 코로나 전 1.5배 목표; 総務省 「ふるさと住民登録制度」 가이드라인 Ver.1.0 2026-03-27, 2026년도 개시 | 2024–26 | [nikyo-labo](https://www.nikyo-labo.jp/media/dual-life/12201/), [inquire](https://inquire.jp/2024/12/13/sharesummit2024-dual-residence/), [国交省](https://www.mlit.go.jp/report/press/kokudoseisaku09_hh_000166.html), [トラベルボイス](https://www.travelvoice.jp/20260327-159498), [総務省](https://www.soumu.go.jp/furusatojuumin/) |
| 資金決済法 개정 | 2025-06-13 공포, 2026-06-12 전면 시행; 크로스보더 수납대행 = 為替取引 → 資金移動業 등록(6개월 경과조치); 제3자형 前払式 등록·공탁 | 2026-06 | [BUSINESS LAWYERS](https://www.businesslawyers.jp/articles/1476), [Westlaw Japan](https://www.thomsonreuters.co.jp/ja/westlaw-japan/law_guide/2026/0630/), [牛島総合](https://www.ushijima-law.gr.jp/client-alert_seminar/client-alert/20250630paymentservicesact/) |
| 한국 토큰증권 | 전자증권법·자본시장법 개정안 2026-01-15 국회 통과, **2027-02-04 시행**(1단계: 공모 조각투자증권 등), 하위법규 2026-09말 입법예고 | 2026 | [법률신문](https://www.lawtimes.co.kr/news/articleView.html?idxno=226492), [아시아경제](https://view.asiae.co.kr/article/2026090408553766523), [김앤장](https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=34390) |
| 한국 조각투자 | 카사 2026-08-10 서비스 종료 · 펀블 2026-05 운영중단·7-03 파산선고 · 2026년 발행 14건 | 2026 | [다음/뉴스](https://v.daum.net/v/20260811114137486), [이데일리](https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=04004886642036080), [파이낸셜뉴스](https://www.fnnews.com/news/202609021808148949) |
| 한국 전자금융거래법 | 2024-09-15 시행, 선불업 등록 확대(면제: 발행잔액 30억·연 500억), 충전금 50% 별도관리 | 2024 | [플래텀](https://platum.kr/archives/217353), [금융위](https://www.fsc.go.kr/no010101/82339) |
| 한국 외국인 주택 규제 | 외국인 토지거래허가구역(서울 전역+경기 23시군) 2026-08-26~2027-08-25 연장, 수도권 외국인 주택거래 27% 감소; 2026-02-10부터 체류자격·거주여부 신고 의무 | 2026 | [뉴스핌](https://www.newspim.com/news/view/20260820001214), [유스연합](https://www.youthassembly.kr/news/917295) |
| 한국 관광주민증·고향사랑 | 디지털 관광주민증 누적 411만건(2024-12)·52개 지역(2026-06); 외국인 발급 제안 2026-06 국민제안 최우수상; 고향사랑기부 2025년 1,514억5,600만원(+72.3%) | 2026 | [K-공감](https://gonggam.korea.kr/newsContentView.es?mid=a12502000000&section_id=&news_id=b40765ee-bd4a-4af6-99c2-916312547b2b), [아시아경제](https://view.asiae.co.kr/article/2026062607201468222), [정책브리핑](https://www.korea.kr/multi/visualNewsView.do?newsId=148966445) |

---

## 2. 후보 아이디어 12건

각 후보는 (1) 한 줄 (2) 타겟 (3) 근거 수치 (4) 존재 검증 (5) 성장성·미래가치 (6) 당사 자산 연결 (7) 규제 리스크 순.

### 후보 1. 크로스보더 Rent-Passport 스코어 API (외국인 thin-file 크레딧) — 시드 F

1. **한 줄**: 한국 게스트하우스·도쿄 먼슬리에서 축적되는 외국인의 임대료 납부·체류·eKYC 이력을 한일 양방향으로 이식 가능한 "임차 이력 스코어"로 만들어, 일본 家賃保証사·관리회사·MVNO·카드사와 한국 임대인·은행에 API로 판매.
2. **타겟**: 일본 재류외국인 412만5,395명(+9.5%) [https://www.jiji.com/jc/article?k=2026032700900&g=pol] 중 한국 국적 40만7,341명 [https://www.nippon.com/ja/japan-data/h02750/]; 한국 체류외국인 287만4,278명(+5.2%) [https://www.moj.go.kr/bbs/immigration/227/608714/artclView.do]; B2B 고객은 家賃保証 시장 2,723억9,000만엔(2025년도) [https://www.yanoict.com/summary/show/id/776]과 GTN 제휴 부동산사 약 43,000社 규모의 채널 [https://www.gtn.co.jp/business/realestate/rent-guarantor]. 1차 웨지는 한국→일본 이동자(한국 도시민박 게스트 → 도쿄 먼슬리) 및 일본→한국 이동 일본인.
3. **근거 수치**: 家賃債務保証 시장 2024년도 2,548억5,700만엔(+6.7%) → 2025년도 2,723억9,000만엔(+6.9%) → 2029년도 3,500억엔 초과, 보증사들이 "고령자·재류외국인"으로 확장 중 [https://www.yanoict.com/summary/show/id/776] [https://www.tokyo-takken.or.jp/re-port/78927]; 신용정보는 국경을 넘지 않고 일반 임대료 납부는 신용파일에 기록되지 않음 [https://e-housing.jp/post/japan-credit-card-guide-2025-loans-bank-regulation-and-credit-score]; CIC 「クレジット・ガイダンス」 2025-04-01 제공 개시 [https://www.americanexpress.com/ja-jp/benefits/good-news/life/credit-guidance/]; 외국인 카드 탈락 사유 = 재류 1년 미만·일본어·소득 [https://www.saisoncard.co.jp/credictionary/knowledge/article106.html]; 재류외국인 카드 보유율 **미확인**; 한국 은행권 외국인 대출 "사실상 없음"(2024-10) [https://news.mt.co.kr/mtview.php?no=2024102116374999164] → 2025-08 일부 은행 3,000만원 한도 개시 [https://www.mt.co.kr/finance/2025/08/20/2025081915325669124], JB금융 17.9%·5,000만원 [https://www.topdaily.kr/articles/103334]; 일본 AI 입거심사 확산: RM트러스트 누적 40만건 데이터 AI심사 2024-08-20 [https://www.value-press.com/pressrelease/340405], 日本セーフティー 2025-04 [https://www.nihon-safety.co.jp/backnumber/20250523.html], イタンジ 2026-03 [https://corp.itandi.co.jp/news_posts/260331_01]; 외국인 보증 심사 통과율 **미확인**; 특정재류카드 2026-06-14 운용으로 본인확인 인프라 정비 [https://www.gaikokujin-press.com/archives/2961]; LICC 가맹 보증사 간 연체정보 공유 체계 존재 [https://www.houserent-surety.com/comparison_table/member_organization.html].
4. **존재 검증**: 직접(KR↔JP 임대 이력 스코어) **0건 → 미존재**. 인접: GTN(외국인 家賃保証+에포스카드+모바일, 누적 70만 이용자, 2026-07-21 약 30억엔 조달, "데이터×AI 고도화" 명시) https://www.gtn.co.jp/business/realestate/rent-guarantor [https://prtimes.jp/main/html/rd/p/000000145.000054071.html] [https://www.gtn.co.jp/news/20260721]; MILIZE×React Plus 「Atobar.ai」(2025-11-21, thin-file BNPL AI 스코어) https://milize.co.jp/news/20251121_7029; LINE Score·d스코어 https://data.wingarc.com/credit-score-26008; 크레파스솔루션(한국 대안 CB, 2026-01 사람인 제휴) https://thevc.kr/crepasssolutions; Nova Credit 「Credit Passport」(20개국·28억 기록, 한국 포함·일본 미포함; Entrata 임대심사 통합 2025-04, 2만 커뮤니티) https://www.novacredit.com/credit-passport [https://www.entrata.com/press/entrata-integrates-nova-credits-credit-passport-to-expand-housing-access-for-international-renters]; Paperpike(2026-02 런칭 "portable housing passport") https://paperpike.com/; RentPassport(EU) https://rentpassport.eu/; TRUSTDOCK 재류카드 유효성 확인 API(2023-05 15억엔 조달) https://biz.trustdock.io/news/zairyu.option.
5. **성장성·미래가치**: 양국 외국인 모두 역대 최다 갱신 중이고, Entrata×Nova Credit(2025-04)이 "임대심사용 크로스보더 신용" 카테고리를 증명했으나 아시아·한일은 공백. GTN이 30억엔을 "데이터×AI"에 투입한다는 것은 이 레이어의 가치를 시장이 인정한 신호이자, 12~24개월 내 GTN이 자체 데이터로 유사 기능을 낼 수 있다는 경고. 미래가치는 스코어 자체보다 **양국 이력을 연결한 "귀국·재입국 리스크" 변수**(외국인 임대인의 최대 공포인 '먹튀'를 수치화)에 있다.
6. **당사 자산 연결**: 동일인의 한국 투숙·결제 이력 + 도쿄 먼슬리 납부 이력을 보유할 수 있는 유일한 사업자; 家賃債務保証業 등록으로 보증심사 데이터가 학습·검증 데이터로 직결(13절의 "첫 1,000건 라벨 파이프라인"이 그대로 상품); AI/개발 → API화; 택건업 → 부동산회사 채널.
7. **규제 리스크(중)**: 일본 개인정보보護法 제3자 제공·역외이전(제28조) 동의, 지정신용정보기관 외 신용정보 유통 제약; 한국 신용정보법상 CB 허가 없이 "신용점수" 제공 불가 → "임대 납부이력 증명/리스크 지표"로 포지셔닝하거나 크레파스류 대안 CB와 제휴; 국적 변수 배제 설계. (조문 단위 검토는 전문가 확인 필요.)

### 후보 2. 管理組合·管理会社용 외국인 거버넌스 AI SaaS — 시드 D

1. **한 줄**: 외국인 입주자·구분소유자 급증에 대응해 管理会社·管理組合에 규약 다국어화 + AI 24시간 다국어 응대 + 총회 의안서 번역·의결권 행사 지원 + 관리비 체납 다국어 통지를 월정액 SaaS로 제공(임차인 대응이 아니라 **소유자·총회·체납** 레이어).
2. **타겟**: 도쿄 23구 신축맨션 해외거주자 취득 3.5%·도심 6구 7.5% [https://www.nippon.com/ja/japan-data/h02624/]인 管理組合; いい生活Home 도입 1,500社 규모의 管理会社 시장 [https://www.es-service.net/service/es-home/]; 首都圏 외국인 145만명(2024-06) [https://veritas-investment.jp/lounge/contents/professional/6463/]; 한국 역수출 시 아파트아이 약 3만 단지·1,200만 세대 [https://play.google.com/store/apps/details?id=aptip.app].
3. **근거 수치**: 외국인 입주자 트러블 경험 약 30%, 유형은 소음 71.4%·쓰레기 33.0%(AlbaLink 500명) [https://prtimes.jp/main/html/rd/p/000000286.000055654.html]; 외국인 입주자 41.9%가 전기·가스·수도 절차에 불안(GTN 2026-03-10) [https://www.nikkei.com/article/DGXZRSP704165_Q6A310C2000000/]; 타워맨션 외국인 구분소유자 185만9,000엔 4년 체납 사례 [https://gentosha-go.com/articles/-/77001]; 총회 의안서 일본어 한정으로 의결권 미행사 문제 [https://visa-asocia.com/column/2523/]; 改正区分所有法 2026-04-01 시행(재건축·일괄매각 결의요건 개정) [https://mij-c.com/column/small-apartment/949]; 大東建託リーシング 2026-04 외국어 서포트 9언어로 확대(재류외국인 약 9할 커버) [https://www.kentaku.co.jp/news/release/2025/release_9LanguageUpdate_20260212.html]; 日管協 외국인 입거 실태조사 [https://www.jpm.jp/foreign//download.php?key=factsurvey01].
4. **존재 검증**: 임차인 다국어 대응은 **이미 존재(3+)** — GTN 25언어·연 20만건 https://www.gtn.co.jp/business/acceptance/living-support; いい生活Home(입주자 앱 자동번역 영·중·한, 1,500社) https://www.es-service.net/service/es-home/; WOVN.io https://wovn.io/; 다국어 콜센터 대행 19社 [https://www.biz.ne.jp/matome/2003282/]. **管理組合(구분소유자) 대상 다국어 총회·규약·체납 SaaS: 미확인(컬럼·사례만)** [https://mij-c.com/column/small-apartment/949] [https://kashiwabaralife.com/mansion/foreign-owner]. 한국: 아파트아이·아파트너(다국어 도입 예정) https://www.aptner.com/ — 외국인 특화 미확인.
5. **성장성·미래가치**: 임차인 → 소유자로 외국인이 이동하면서 管理組合 의사결정(2026-04 区分所有法 개정 후 결의 성패)·관리비 회수·해외거주 소유자 연락이 구조적 리스크가 됨. AI 번역 원가 급락으로 소규모 조합도 월정액 수용 가능. 후보 1의 스코어를 붙이면 "외국인 소유자 관리비 체납 보증"이라는 신상품으로 확장.
6. **당사 자산 연결**: 자사 먼슬리 물건이 속한 管理組合가 첫 고객; 외국인 임차인 데이터(국적·언어·트러블 유형)로 규약 위반 예측·템플릿 생성; 家賃債務保証業으로 관리비 체납 보증 결합; 한국 아파트앱 시장에 "외국인 입주민 모듈"로 역수출.
7. **규제 리스크(낮~중)**: 국적·재류자격은 要配慮 수준의 민감정보 취급 주의; 관리비 독촉을 대행하면 弁護士法 72조(비변호사 채권회수) 저촉 → 통지·번역까지로 한정; 번역문의 법적 효력(일본어 원문 우선) 명시.

### 후보 3. 민박·먼슬리 호스트 매출 선지급(팩토링/RBF) + 보증 패키지 — 시드 C

1. **한 줄**: 民泊·먼슬리 호스트의 향후 예약·임대료 채권을 당사 운영 데이터로 AI 심사해 수개월분을 선지급하고, 家賃債務保証과 묶어 "보증(신용보강)+선지급(유동성)" 한 계약으로 제공.
2. **타겟**: 일본 民泊 届出住宅 42,070건(가동), 누적 65,837건 중 폐지 23,767건(약 36%) [https://www.mlit.go.jp/kankocho/minpaku/business/host/construction_situation.html] — 특히 다이토구 2026-10-01 신규 민박 평일 제한·신주쿠 등 평일 금지 구역 호스트(본체 문서 12.3절); 도쿄 먼슬리 오너·운영대행; 한국 외국인관광 도시민박 호스트(한국 Airbnb 슈퍼호스트 +22%) [https://news.airbnb.com/ko/globalqualityreport/].
3. **근거 수치**: Airbnb 자체가 "예약 3일 후 수취금 50% 선지급" 테스트 [https://airstair.jp/airbnb-test-payout/]; 일본 RBF: Flex Capital 누적 103억엔·270社·디폴트율 0.26%(2025-05) [https://fivot.co.jp/news/flex-capital_10by/], Yoii 시리즈A 8억엔 [https://tomoruba.eiicon.net/articles/4424], 三菱UFJ信託 출자 일본 최초 RBF 펀드 설립 [https://prtimes.jp/main/html/rd/p/000000016.000078333.html]; 글로벌 RBF 2023년 33.8억달러 → 2027년 259.4억달러 [https://paytoday.jp/contents/japan-rbf/]; 改正住宅セーフティネット法 2025-10 시행으로 국가 인정 家賃債務保証業者 제도 [https://www.gov-online.go.jp/article/202511/entry-9961.html]; リブマックス 법인 100~200호 일괄 계약 10% 증가 [https://www.zenchin.com/news/post-4469.php]; 한국 HUG 「전월세 안심신탁」(임대인 월세 보장) 추진 [https://supple.kr/news/cmt184xdv00po10rp7kpgxkn0].
4. **존재 검증**: 글로벌 2~3개 — Guesty Capital(Parafin MCA, 1~2영업일 입금) https://www.guesty.com/features/guesty-capital/; Host Financial(STR 수익 기반 론) https://www.hostfinancial.com/short-term-rental-loans-mortgages; Clearco·Uplisting 프로그램 미확인. 일본: 일반 RBF(Yoii https://yoii.jp/ , Flex Capital https://flex-capital.jp/service/rbf/ , PAYTODAY https://paytoday.jp/)는 숙박 특화 아님; 家賃保証 대납(全保連 https://www.zenhoren.jp/service/rent/index.html , 日本セーフティー, エルズサポート)은 "연체 후 대납"이지 선지급 아님; 민박 운용대행(airhost https://airhost.jp/products/property-management-service , @Host https://athost.jp/)은 금융 미제공. 한국: 자리톡(월세 카드결제) https://tenant.zaritalk.com/ , 핀다 — 호스트 선지급 없음. **판정: 일본·한국 민박/먼슬리 호스트 대상 매출 선지급 전문 사업자 미확인 → 공백.**
5. **성장성·미래가치**: 폐지율 36%가 말해주듯 현금흐름 취약 호스트가 다수이고, 평일 금지 구역 확대(2026-10)로 수익 변동성이 커진다. RBF 자금(펀드·신탁은행)은 이미 있으나 "숙박·먼슬리 채권을 심사할 데이터"가 없어 진입 못 하므로, 데이터 보유자가 오리지네이터가 된다. 본체 BM의 호스트 락인(13.4절) 수단이자 보증료+수수료 이중 수익.
6. **당사 자산 연결**: 자사 민박·먼슬리 점유율·계절성·게스트 국적·연체 데이터 → 채권 스코어링; 家賃債務保証業 → 임차인 연체는 보증, 호스트 유동성은 선지급으로 분리; 한국 도시민박 호스트에 동일 모델 수출.
7. **규제 리스크(중)**: 채권양도(팩토링)는 貸金業 등록 없이 가능하나 "실질 대부" 판정 시 貸金業法 위반 → 진정 양도 구조 필수; 한국은 여신 성격이면 대부업·여신전문금융업 문제; Airbnb 등 플랫폼 정산채권의 양도 가능 여부(약관) 확인 [https://www.airbnb.com/help/article/2909]. 초기에는 자사 플랫폼 정산 채권(당사가 지급자)만 대상으로 하면 리스크 최소.

### 후보 4. 해외(한국) 팬 대상 관계인구 멤버십 / 디지털 시민권 — 시드 I

1. **한 줄**: 일본 지자체의 ふるさと住民 등록·디지털주민표(NFT) 제도를 한국인 등 해외 일본 팬에게 판매·운영하는 멤버십(등록 → 특전 → 자사 먼슬리·게스트하우스 체류 → 노마드·장기체류 전환), 역방향으로 한국 디지털 관광주민증을 일본인에게.
2. **타겟**: 일본 関係人口 약 2,263만명(18세 이상 22%; 방문계 1,884만) [https://www.travelvoice.jp/20250630-157959] [https://www.mlit.go.jp/report/press/kokudoseisaku09_hh_000166.html] — 해외 관계인구 **미확인**; 방일 한국인 946만 중 재방문 팬층(비율 미확인); 방한 일본인 365만 [https://www.ajunews.com/view/20260130103801235]; 노마드 비자 646건(2.51배) [https://prtimes.jp/main/html/rd/p/000000024.000126832.html].
3. **근거 수치**: 総務省 ふるさと住民登録制度 가이드라인 Ver.1.0 2026-03-27, 2026년도 개시, 전용 앱·베이직/프리미엄 2구분 [https://www.travelvoice.jp/20260327-159498] [https://www.soumu.go.jp/furusatojuumin/]; 해외재주 방인·외국인 확대 가능성 언급 [https://shop.gyosei.jp/online/archives/cat01/0000115542] — 외국인 등록 가부 공식 확정 **미확인**; 山古志 Nishikigoi NFT 디지털촌민 1,032명(2022-11) → 1,600명+(2024-05), 1만명 계획 [https://www.cas.go.jp/jp/seisaku/digitaldenen/menubook/2022_winter/00023.html] [https://sotokoto-online.jp/life/25277] [https://note.com/cryptovillage/n/n6d5fa341b57d]; 西川町 디지털주민표 NFT 1,000매 1분 완판·응모 13,440(13.4배)·실방문 1,360명·경제효과 230만엔 [https://forbesjapan.com/articles/detail/62877]; HafH 회원 20만 초과·누적 100만박(2025-08), 130개국 1.5만 시설, 서울·부산 포함 [https://www.hafh.com/en/topics/19258] [https://dc.watch.impress.co.jp/docs/news/1492122.html]; ADDress 270개소+·회원 증가 157% [https://ecrowd.co.jp/projects/23]; 호텔 서브스크 2028년 180억엔 [https://hotelbank.jp/industry-trends/hotel-subscription-market-2026-tipping-point/]; 한국 디지털 관광주민증 411만건·52개 지역, 외국인 발급 제안 2026-06 최우수상 [https://gonggam.korea.kr/newsContentView.es?mid=a12502000000&section_id=&news_id=b40765ee-bd4a-4af6-99c2-916312547b2b] [https://view.asiae.co.kr/article/2026062607201468222]; 고향사랑기부 2025년 1,514억5,600만원(+72.3%) [https://www.korea.kr/multi/visualNewsView.do?newsId=148966445]; 인바운드 2030년 목표 6,000만명·15조엔 [https://honichi.com/news/2025/06/23/kotsuseisaku-singikai-50/].
4. **존재 검증**: 국내 대상 디지털주민표·관계인구 서비스 **이미 존재(3+)** — 総務省 제도 앱 https://www.soumu.go.jp/furusatojuumin/ (인프라); Nishikigoi NFT/Crypto Village https://note.com/cryptovillage/n/n6d5fa341b57d; 西川町·美祢市 NFT https://hexanft.com/mndigital/; 美しい村NFT [https://prtimes.jp/main/html/rd/p/000000008.000101482.html]; HafH·ADDress(체류 레이어). **해외 팬 대상 관계인구 멤버십 운영자: 미발견 → 미존재.** 한국 외국인 관광주민증은 "제안 수상" 단계 https://korean.visitkorea.or.kr/dgtourcard/.
5. **성장성·미래가치**: 양국 모두 2026년이 "비거주 관계인구" 제도화 원년. NFT 13.4배 응모·고향사랑 +72%가 팬 수요를 실증. 수익 규모는 작지만 지자체 협업 실적이 택건업·보증업 신뢰로, 회원 체류·납부이력이 후보 1 스코어로 이어지는 선점 가치.
6. **당사 자산 연결**: 멤버십 특전의 핵심은 "체류" → 자사 도쿄 먼슬리·한국 게스트하우스가 특전 재고; 한국 게스트 채널로 일본 팬 모집; 도쿄 거점이 지방 지자체 허브.
7. **규제 리스크(낮~중)**: NFT의 자금결제법상 암호자산 해당성(특전 한정 NFT는 원칙 비해당, 사례별) [https://www.businesslawyers.jp/articles/1476]; 지자체 계약 절차·경품표시법; 한국 관광주민증 정부 시스템 API 연계 [https://openservice.go.kr/travelDigtCard]; 특전 체류 30일 초과 시 비자 범위 점검. 제도가 외국인을 미포함할 경우 지자체 단위 NFT/멤버십으로 우회.

### 후보 5. 한국인 비거주 오너의 도쿄 물건 → 외국인 먼슬리 운영·보증·납세관리 원스톱 (본체 추가)

1. **한 줄**: 도쿄 맨션을 매입한(또는 매입하려는) 한국 거주 오너에게 "외국인 먼슬리로 운영 + 당사 보증으로 공실·연체 흡수 + 비거주자 源泉徴収·納税管理人 처리 + 한국어 리포팅"을 AI 원격 운영으로 제공하고, 그 물건을 본체 플랫폼의 공급 재고로 편입.
2. **타겟**: 도쿄 도심 1억~3억엔대 맨션을 찾는 한국 자산가(부동산사 문의 2배) [https://www.hankyung.com/article/2026082776251]; 하나은행 상담 기준 도쿄 10~30억원대 주택 수요 [https://www.hankyung.com/article/202504242847O]; 해외거주자 도쿄 23구 취득 308호/반기(대만 192·중국 30) [https://www.nippon.com/ja/japan-data/h02624/] 중 한국인 비중 **미확인**; 한국 개인의 일본 부동산 취득 신고액 **미확인**(한국은행 통계 미노출) [https://www.bok.or.kr/portal/main/contents.do?menuNo=200405].
3. **근거 수치**: 해외투자자 일본 부동산 매입 2026 상반기 1조1,400억엔 사상 최대, 23구 신축 4년 2배 [https://www.hankyung.com/article/2026082776251]; 23구 기존 콘도 70㎡ 1억1,034만엔(+37%, 2025-09) [https://v.daum.net/v/20251030063250099]; 비거주자 오너 임대료 源泉徴収 20.42%·納税管理人 선임 의무 [https://ablaze-p.co.jp/inheritance_tax/18581] [https://www.creavision.co.jp/column/withholding-tax/]; 2026-04 외환법 시행규칙 개정으로 해외거주자 부동산 취득 보고의무 확대 [https://www.tmi.gr.jp/eyes/blog/2026/18051.html]; 정기차가 비중 미나토구 37.5% [https://www.kenbiya.com/ar/ns/jiji/purchase_know_how/10182.html]; 한국 외국인 토지거래허가구역 연장으로 서울 투자 억제(수도권 외국인 거래 27% 감소) [https://www.newspim.com/news/view/20260820001214] → 한국 자산가의 해외 대체 수요.
4. **존재 검증**: 한국어 매입 중개 **이미 존재(3+)** — 재팬홈즈 https://japan-homes.com/ , GL Smart Planning https://www.glsmart.jp/kor/ , 트러스트파트너스(세입자 모집·수금·유지보수 대행) https://www.trustpartners.net/ , 맨션맨 https://mansionman.info/ , JRE https://www.japan-real.com/ , 카네모토 https://kanemoto1.biz/ , 스타츠코리아 https://startskorea.co.kr/user/jp-invest-list , OM-ESTATE https://om-estate.kr/investment , HS/잼스하우스(한일 양국 면허) https://jamshouse.com/. 비거주 오너 관리: 日本財託 Global(한·중·영, 오너 앱) https://www.nihonzaitaku.co.jp/kanri/global/en/ , Housing Japan hands-free https://housingjapan.com/resources/hands-free-property-management-service/ , FPマネジメント https://fp-manage.com/foreign_management/. **"한국인 오너 물건을 외국인 먼슬리로 운영 + 자체 보증 + AI 원격"을 결합한 사업자: 미확인.** 중개는 포화, 운영·보증 레이어는 공백.
5. **성장성·미래가치**: 한국 내 규제(토허제·실거주 의무)와 도쿄 가격 상승·엔저가 한국 자산가의 도쿄 매입을 밀고 있으나, 매입 후 "비거주자 세무 + 공실 + 외국인 임차 리스크"를 한국어로 해결해 주는 곳이 없다. 당사에겐 **마스터리스 없이(OYO LIFE 교훈) 공급을 늘리는 경로**이자, 오너 물건의 운영 데이터가 후보 7(토큰)의 기초자산이 된다.
6. **당사 자산 연결**: 택건업(매입 중개·임대 관리), 家賃債務保証(오너에게 연체·공실 보증), AI 언더라이팅(임차인 심사), 한국 채널(오너 모집), 한국어 리포팅. 물건 1호당 중개보수 + 관리료 + 먼슬리 수수료 + 보증료의 4중 수익.
7. **규제 리스크(중)**: 2026년 외국인 토지취득 규제 입법(대상·지역 미정)이 한국인 오너의 매입 자체를 위축시킬 수 있음 [https://www.tmi.gr.jp/eyes/blog/2026/18051.html]; 納税管理人 인수 시 세무 책임; 賃貸住宅管理業 등록(200호 이상) 필요 가능성; 한국 외국환거래법 해외부동산 취득 신고 [https://www.bok.or.kr/portal/main/contents.do?menuNo=200405].

### 후보 6. 재한 일본인 먼슬리 + AI 심사·보증 + 정착 원스톱 (도쿄 모델의 역방향) — 시드 E

1. **한 줄**: 서울(신촌·홍대·강남)의 일본인 유학생·워홀·주재원·K-컬처 장기체류자에게 "보증금 0 먼슬리 + AI 심사 + 일본어 정착(전입·통신·은행)"을 제공.
2. **타겟**: 재한 일본인 43,064명(2024-10) [https://data-seisaku.com/00300-mofa-00300100-0000-full-list/]; 일본 국적 유학생 3,872명(어학원 1,208·교환 576) [https://kstudytimes.kr/students-by-country/jp]; 워홀 연 상한 1만·2025-10부터 2회 [https://3d-universal.com/blogs/2025/08/korea-working-holiday-visa.html]; JETRO 2025년도 조사 응답 在韓 일계기업 79社(전체 진출 수 **미확인**) [https://www.jetro.go.jp/news/releases/2025/13aebb32e58e01ad.html]; 고려대 어학당 정규과정 일본인 약 20%, 일부 어학원 약 80% [https://kankokuryugakuguide.com/koreablog/koreauniversit/] [https://ryugaku.kuraveil.jp/articles/358].
3. **근거 수치**: 방한 일본인 365만(2025) → 2026 1~7월 228만(+18.8%) [https://www.newspim.com/news/view/20260831000073]; 유학·연수 목적 방한 외국인 첫 50만 돌파 [https://www.koreapost.co.kr/news/articleView.html?idxno=88801]; 국내 외국인 유학생 275,580명(2025-05) [https://chartngraph.com/%EC%99%B8%EA%B5%AD%EC%9D%B8-%EC%9C%A0%ED%95%99%EC%83%9D-%ED%98%84%ED%99%A9/]; 서울 호텔 요금 "2배" 체감 [https://note.com/kpopyuriko/n/nca7e262dc58a]; 전세 보증금 관행이 일본인 최대 장벽 [https://www.owchikorea.com/].
4. **존재 검증**: 일본어 부동산 중개 **이미 존재(3+)** — スターツソウル https://kaigai.starts.co.jp/korea , エイブル ソウル https://www.able-nw.com/seoul/ , おうちコリア https://www.owchikorea.com/ , KOREA Benri https://koreabenri.com/ , 韓国掲示板 https://kaigai-bbs.com/kor/thread/rent/. **결정적으로 GTN Korea가 2025년 「韓国ライフサポート」(エイブル 제휴·공인중개사 고용·법인 전대·유학생 1개월~ 물건·가구 렌탈)를 개시하고 [https://prtimes.jp/main/html/rd/p/000000137.000054071.html], 2026-05-28 연세대 인근에 생활지원형 「GTN STAY」를 열었다 [https://www.gtn.co.jp/news/20260528].** 엔코스테이(서울 350개 공간, 누적 14,540명, 일본인 페이지 운영) https://stay.enko.kr/ [https://thevc.kr/enkorwithus]. → **보증·전대까지 포함해 "이미 존재"로 판정.** 남는 공백은 "도쿄 이력 승계(후보 1)"뿐.
5. **성장성·미래가치**: 수요 성장 수치는 12개 후보 중 가장 뚜렷하나, GTN이 보증·전대·유학생 물건을 이미 갖고 진입한 이상 단독 사업이 아니라 **본체 한국 먼슬리(랜딩 윈도우)의 일본인 세그먼트**로 흡수하는 것이 맞다.
6. **당사 자산 연결**: 한국 도시민박 재고의 30일+ 전환, 도쿄에서 만든 AI 심사·보증 모델의 역적용, 일본 측 유입 채널(유학원·워홀 에이전트·KSC).
7. **규제 리스크(중)**: 도시민박은 관광객 단기숙박 → 1개월 이상은 주택임대차보호법·임대사업자 영역(본체 한국 문서 5절); 한국 보증업은 보증보험·여신 라이선스 검토.

### 후보 7. 한일 크로스보더 부동산 토큰(먼슬리 주택 수익 토큰) — 시드 B

1. **한 줄**: 당사 운영 도쿄 외국인 먼슬리 포트폴리오(후보 5의 오너 물건 포함)를 不動産ST 또는 不特法 CF로 소액화해 일본 개인(1차) → 한국 개인(2027-02 이후 2차)에게 판매.
2. **타겟**: ALTERNA 이용자 100만명 [https://alterna-z.com/] 등 일본 ST/CF 리테일; 한국은 조각투자 투자자층(카사·펀블 이탈 수요) 및 도쿄 자산 선호 자산가.
3. **근거 수치**: 不動産ST 누적 약 2,600억엔(2025-12) → 2026말 5,225억엔 예측 [https://zenn.dev/komlock_lab/articles/japan-real-estate-security-token-market] [https://www.dir.co.jp/report/research/capital-mkt/it/20260126_025555.pdf]; 공모ST 2025년도 단년 1,650억엔·누적 3,333억엔(전년 2배) [https://www.nomuraholdings.com/jp/news/nr/bstr20260402.html]; ALTERNA 운용 2,477억엔·49물건·조성건수 점유 37.2% [https://alterna-z.com/] [https://www.bluebox.co.jp/article/alterna-hyoban/]; KDX 조성금액 점유 50.4% [https://speakerdeck.com/progmat/progmat-st-market-outlook-2026]; 不動産CF 2025년 1,711억엔 횡보 [https://www.crowdfundingchannel.jp/fudosan_cf_chaos_map_2026/], CREAL GMV 932억엔 [https://corp.creal.jp/news/4651/], COZUCHI 누적 1,183억엔 [https://sakk.jp/column/cozuchi-hyoban/]; 한국 토큰증권 2027-02-04 시행·1단계 공모 조각투자증권 [https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=34390]; 카사 종료·펀블 파산·2026년 발행 14건 [https://www.fnnews.com/news/202609021808148949].
4. **존재 검증**: 일본 공급측 **이미 존재·성숙(3+)** — ALTERNA https://alterna-z.com/ , ケネディクス/KDX ST [https://search.sbisec.co.jp/v2/popwin/info/home/seminar/home_seminar_briefing_260108_kenedix-st.pdf], Progmat https://progmat.co.jp/ , 野村 https://www.nomura.co.jp/sto/archive/index.html , 大和 https://www.daiwa.jp/products/securitytoken/ , SMBC日興 https://www.smbcnikko.co.jp/products/sto/ , CREAL https://corp.creal.jp/ , COZUCHI, Jointoα https://join-to.jp/. 한국: 카사 https://www.kasa.co.kr/ (종료), 밸류맵 STO https://www.valueupmap.com/sto. **한국 리테일에 일본 부동산 토큰을 파는 크로스보더 플레이어: 미확인.**
5. **성장성·미래가치**: 일본 ST는 2년 연속 2배, 2026년 1조엔 → 자산군 다양화 국면에서 "외국인 먼슬리 주거(자체 보증 배당)"는 신규 자산군. 한국은 국내 상품 신뢰 붕괴 후 "엔화·도쿄 자산" 대체 수요가 2027-02 제도 시행과 맞물림. 다만 당사 단독 발행은 불가하고 AM·증권사에 **"운영 데이터가 붙은 자산 공급자"**로 참여하는 것이 현실적.
6. **당사 자산 연결**: 운영 물건 + 家賃債務保証 → 배당 안정성; AI 언더라이팅 결과(입주율·연체율)가 토큰 밸류에이션 근거; 한국 채널 → 2027년 이후 국내 발행인 제휴.
7. **규제 리스크(높음)**: 不特法 허가·金商法(二種) 라이선스 필요 → AM·증권사 제휴 전제; 비거주자(한국 거주 개인)의 일본 증권계좌 원칙 불가 [https://faq.sbisec.co.jp/answer/5ec2341f8504de0011d61467/]; 한국 자본시장법 공모 구조·하위규정(2026-09말) 확인; 한국 외국환거래법 해외부동산 취득 신고 [https://www.bok.or.kr/portal/main/contents.do?menuNo=200405].

### 후보 8. 空き家 → 한국 채널 + 구매 후 외국인 먼슬리 운영·보증 — 시드 A

1. **한 줄**: 도쿄 통근권 근교·관광형 지방의 空き家를 한국인·외국인 구매자에게 중개하고, 구매 후 리노베 → 30일+ 먼슬리(워케이션·二地域居住·장기체류) 운영·보증·매각까지 원스톱.
2. **타겟**: 空き家 소유자(900만호 중 방치성 385만호) [https://biz.homes.jp/column/topics-00124]; 二地域居住 관심층 27.9%(MLIT 2022) [https://www.nikyo-labo.jp/media/dual-life/12201/]; 空き家 구매 희망 외국인(AkiyaMart 2025년 약 150건, 2026년 2배 전망) [https://www.businesstraveller.com/insights/features/japan-akiya-boom-buying-abandoned-homes/]; 한국인 수요는 언론 관심(뉴시스 기획 등) [https://www.newsis.com/view/NISX20250917_0003332295] 수준이며 매입 건수 **미확인**.
3. **근거 수치**: 空き家 900만호·13.8%(2023) [https://built.itmedia.co.jp/bt/articles/2405/08/news058.html]; 2030년 용도 없는 空き家 470만호 전망 [https://magazine.zennichi.or.jp/legal-reform/15357]; 全国版空き家バンク 1,106 자치체·누적 성약 약 21,700건(2025-05) [https://dl.ndl.go.jp/view/prepareDownload?itemId=info%3Andljp%2Fpid%2F14461454]; 성약률 편차(무로란 약 70% vs 시마네 감소) [https://www.hokkaido-np.co.jp/article/1244331/] [https://www.sanin-chuo.co.jp/articles/-/1071182]; 管理不全空家 고정자산세 최대 6배 [https://magazine.zennichi.or.jp/legal-reform/15357]; 3,000만엔 공제 2027-12-31 만료 [https://www.nta.go.jp/taxes/shiraberu/taxanswer/joto/3306.htm]; 二地域居住 官民PF 709 자치체 [https://inquire.jp/2024/12/13/sharesummit2024-dual-residence/]; 関係人口 2,263만 [https://www.mlit.go.jp/report/press/kokudoseisaku09_hh_000166.html]; 한국 빈집 2024년 약 13만호(0.7%) [https://www.nongmin.com/article/20250502500721](농식품부 기준; 통계청 기준 159만채 [https://supple.kr/news/cmu8xs2nd00ksibf13xyai000] — 정의 상이).
4. **존재 검증**: 일본 空き家 활용·매입 **이미 존재(3+)** — アキサポ https://www.akisapo.jp/ , 空き家活用株式会社(자치체 55곳) https://aki-katsu.co.jp/ , カチタス(누적 10만동) [https://prtimes.jp/main/html/rd/p/000000055.000079457.html], 家いちば https://www.ieichiba.com/ , 空き家ゲートウェイ https://akiya-gateway.com/. 영어권 외국인 구매 중개 **이미 존재(3+)** — AkiyaMart(US$5,000 정액) https://akiya-mart.com/ , Akiya & Inaka, Cheap Houses Japan [https://mailmate.jp/blog/cheap-houses-in-japan], Akiya Japan https://www.akiyajapan.com/ , All Akiyas https://www.allakiyas.com/ , AkiyaHub https://akiyahub.com/ , Home in Nihon https://homeinnihon.com/. 한국: 빈집애 https://www.binzibe.kr/main/ , 다자요(제주) — 국내용. **한국인 채널 + 구매 후 외국인 먼슬리 운영·보증: 미확인.**
5. **성장성·미래가치**: 세제 페널티(6배)와 2027년 공제 만료로 소유자의 처분 결심이 2026~27년에 몰리고, 二地域居住·関係人口 정책이 30일+ 먼슬리에 순풍. 그러나 구매 중개는 영어권 포화, 지방 물건은 본체(도쿄 도심 먼슬리)와 운영 시너지가 약하고, **2026년 외국인 토지취득 규제 입법이 정확히 이 영역을 겨냥**한다.
6. **당사 자산 연결**: 택건업(매입·매각 중개), 家賃債務保証, AI(空き家 수익화 스코어링), 한국 워케이션 수요 채널.
7. **규제 리스크(높음)**: 2026-01-23 총합대응책 "여름까지 새 룰", 통상국회 법안, 2026-04 외환법 보고의무 확대 [https://www.tmi.gr.jp/eyes/blog/2026/18051.html] [https://toushi.homes.co.jp/column/lifeplan/social-issues/current-topics90/]; 30일 미만은 民泊 180일 상한; 管理不全空家 매입 시 안전 책임 이전.

### 후보 9. 한일 양방향 재류자 슈퍼앱(주거 앵커 + 이력 승계) — 시드 H

1. **한 줄**: 재일 한국인·재한 일본인(+양국을 오가는 제3국인)을 한 계정으로 서비스하고 국가 이동 시 주거·보증·통신·계좌·비자·일자리 이력이 승계되는 정주 앱.
2. **타겟**: 재일 한국 국적 40만7,341명 [https://www.nippon.com/ja/japan-data/h02750/]; 재한 일본인 약 42,547명(2024) [https://www.mofa.go.jp/mofaj/files/100781392.pdf]; 한국 체류외국인 287만 [https://www.moj.go.kr/bbs/immigration/227/608714/artclView.do]; 워홀 양방향 연 최대 2만명(양국 상한 각 1만) [https://www.kr.emb-japan.go.jp/itpr_ja/visa_working_h.html].
3. **근거 수치**: Guidable Jobs 40만 사용자(2025-06, 229개국) [https://prtimes.jp/main/html/rd/p/000000066.000017621.html]; YOLO JAPAN 40만+(2026-06) [https://www.yolo-japan.co.jp/]; GTN 누적 70만·연 20만건 상담·25언어·2026-07 30억엔 조달(Globis·Minerva) [https://thebridge.jp/2026/07/gtn-raises-3-billion-yen-for-foreign-resident-support-platform]; 한패스 2026-02 AI 슈퍼앱 전환, 연 3조·누적 10조원 송금 [https://www.newspim.com/news/view/20260202000075]; 하이어다이버시티 50억 시리즈A(2025-04) [https://wowtale.net/2025/04/01/239212/]; 커넥트 투자(2026-05) [https://wowtale.net/2026/05/28/259324/]; 엔코 pre-A 20억·누적 23억 [https://www.venturesquare.net/957586]; 글로벌 Welcome Tech $70M·400만 사용자 [https://techcrunch.com/2022/04/14/welcome-tech-which-wants-to-build-a-super-app-for-immigrants-raises-30m/], Majority 누적 $90M+ [https://techcrunch.com/2024/05/22/majority-immigrant-banking-20m/].
4. **존재 검증**: 단일국 슈퍼앱 **이미 존재(양국 각 3+)** — 일본 GTN https://www.gtn.co.jp/ , YOLO JAPAN https://www.yolo-japan.co.jp/ , Guidable https://guidable.co.jp/news/800/ ; 한국 한패스, 하이어다이버시티, 커넥트, 엔코 https://about.enkor.kr/ , modu K. 커뮤니티: Man&Me(재일코리안) https://www.facebook.com/mannamii.jp/ , 마우무(한일 언어교환). **재일 한국인+재한 일본인을 동시에, 이력 승계로 서비스하는 앱: 미발견.**
5. **성장성·미래가치**: 카테고리 자본 유입(GTN 30억엔, 하이어다이버시티 50억)으로 검증됐지만 범용은 선점됨. 당사의 승산은 "양방향 + 주거 앵커 + 후보 1 스코어" 니치뿐이며, 이는 사실상 본체 플랫폼의 계정 설계(양국 공통 ID)로 흡수하는 것이 맞다.
6. **당사 자산 연결**: 주거 = 가입 시점(입국 시점) 앵커; 한국 도시민박 → 도쿄 먼슬리 파이프라인 = 획득 채널; GTN·YOLO가 갖지 못한 한국 측 재고.
7. **규제 리스크(중)**: MVNO 재판매·은행대리·비자 대행(行政書士·행정사 독점) 번들마다 라이선스; 개인정보 국외이전; 개발자 1명 체제에서 번들 확장은 실행 리스크 최대.

### 후보 10. 한일 왕복 거주자 Stay Pass(양국 재고 공통 멤버십 + 계약 이력 승계) (본체 추가)

1. **한 줄**: 한국 게스트하우스(1~29박) + 도쿄 먼슬리(30일+)를 한 멤버십·한 eKYC·한 결제수단으로 이용하고, 양국 체류·납부 이력이 승계되어 재이용 시 심사 생략·보증료 인하가 적용되는 "한일 왕복 거주 패스"(13절 Stay Pass의 양국 통합판).
2. **타겟**: 한일 왕래 1,300만 [https://www.jiji.com/jc/article?k=2026013001081&g=int] 중 반복 체류자 — 리피터율 대만·홍콩 95%·한국 80%(본체 13.1절), 어학연수 연 4회, 워홀 2회 허용 [https://3d-universal.com/blogs/2025/08/korea-working-holiday-visa.html], K-컬처 팬 방한 일본인 +18.8% [https://www.newspim.com/news/view/20260831000073].
3. **근거 수치**: HafH 회원 20만·누적 100만박·서울·부산 포함(2025-08) [https://www.hafh.com/en/topics/19258]; 호텔 서브스크 2028년 180억엔 [https://hotelbank.jp/industry-trends/hotel-subscription-market-2026-tipping-point/]; Weave Living 도쿄 240유닛(2025 H2)·서울 KKR JV 3건(동대문 98·여의도 157·강남 121)·서울 1,200호 목표·2026-07 TPG 550유닛 개발, 지역 3,000유닛 [https://www.mingtiandi.com/real-estate/finance/kkr-weave-living-buying-tokyo-properties-in-japan-expansion/] [https://www.mingtiandi.com/real-estate/finance/weave-kkr-joint-venture-buys-third-seoul-apartment-complex-for-32m/] [https://www.mingtiandi.com/real-estate/finance/weave-tpg-team-up-on-550-unit-seoul-rental-project/]; 삼삼엠투 일본 진출 **미확인**(영문판만) [https://www.shinailbo.co.kr/news/articleView.html?idxno=2165816].
4. **존재 검증**: 숙박 서브스크 **이미 존재(3+)** — HafH https://www.hafh.com/ , ADDress, LivingAnywhere Commons; 양국 운영 기관형 오퍼레이터 — Weave Living(서울·도쿄, 프리미엄·재고 보유형) https://www.weave-living.com/seoul , GTN(일본)+GTN Korea(한국) [https://prtimes.jp/main/html/rd/p/000000137.000054071.html]. **"1~29박 합법 민박 + 30일+ 임대차를 양국에서 한 이력으로 잇는 C2C형 패스": 미확인.** 단 HafH가 이미 서울을 커버하므로 "숙박 서브스크"로는 차별화 불가 → 차별점은 임대차(계약·주소·보증)와 이력 승계.
5. **성장성·미래가치**: 본체 BM의 LTV 단위(법인·호스트·Stay Pass)를 양국으로 확장하는 것이며 독립 사업이라기보다 **후보 1(스코어)·후보 9(계정)의 소비자 접점**. 후보 11(포인트)의 폐쇄형 대체물이기도 하다.
6. **당사 자산 연결**: 양국 재고·면허·eKYC·결제를 이미 보유 → 추가 자산 불요, 상품 설계만으로 가능.
7. **규제 리스크(낮음)**: 선불형 패스는 일본 前払式支払手段(자가형이면 신고 수준, 제3자형이면 등록) [https://www.freee.co.jp/kb/kb-trend/revision-of-the-fund-settlement-act/], 한국 선불업 면제 기준(잔액 30억·연 500억) [https://platum.kr/archives/217353] 내에서 설계; 개인정보 국외이전 동의.

### 후보 11. 한일 크로스보더 포인트 브리지(환율 없는 여행 포인트) — 시드 G

1. **한 줄**: 네이버·카카오·토스 포인트 ↔ PayPay·d·V·Ponta·楽天 포인트를 양국 여행자용으로 상호 전환·결제.
2. **타겟**: 방일 한국인 946만·소비 9,864억엔 [https://honichi.com/news/2026/02/10/inbound-korea-2025/], 2026 상반기 567만5,100명(+18.6%) [https://kstyle.com/article.ksn?articleNo=2281453]; 방한 일본인 365만, 2026 상반기 194만9,774명(+20.4%) [https://www.newspim.com/news/view/20260728000047].
3. **근거 수치**: 일본 포인트 발행액 2024년도 약 2조8,125억엔, V포인트 통합 2024-04 [https://www.yano.co.jp/press-release/show/press_id/3996]; 한국 포인트 발행액 총액 **미확인**; 간편결제 점유 네이버 51.5%·카카오 25.1%·토스 13.2% [https://blog.opensurvey.co.kr/article/ds-payment-2025-2/]; 페이 일평균 1.2조원(2026-09) [https://biz.newdaily.co.kr/site/data/html/2026/09/18/2026091800179.html]; PayPay 해외지불모드 2025-09-30 한국 개시(약 200만 점포, 해외결제에도 포인트 부여) [https://about.paypay.ne.jp/en/pr/20250916/01/] [https://www.travelvoice.jp/20250916-158378]; 카카오페이↔PayPay 연동, 일본 320만 가맹점, 해외결제 1.8배 [https://www.korit.jp/news/trend/platum-paypay-kakaopay-alipay-250926/] [https://v.daum.net/v/20250520073012458]; Alipay+ 한국 거래 +18% [https://www.businesswire.com/news/home/20251208351936/en]; LINE Pay 일본 2025-04-30 종료 [https://www.etoday.co.kr/news/view/2369721].
4. **존재 검증**: 결제 브리지 **이미 존재(3+)** — PayPay 해외 https://paypay.ne.jp/guide/overseas/ , 카카오페이 https://story.kakaopay.com/338-kakaopay-global/ , 네이버페이 https://www.navercorp.com/media/pressReleasesDetail?seq=29976 , GLN(하나은행, 14개국 58社 포인트/마일 교환 허브, NIPPON Platform 제휴) [https://kyodonewsprwire.jp/release/202308258514] [https://prtimes.jp/main/html/rd/p/000000063.000040904.html]; 일본 국내 포인트 교환 楽天 https://point.rakuten.co.jp/exchange/ , G-Plan https://www.g-plan.net/service/exchange. **KR↔JP 포인트 상호전환 소비자 서비스: 미발견**이나 GLN이 구조상 근접하고 대형 발행사 제휴로 즉시 복제 가능.
5. **성장성·미래가치**: 양방향 트래픽 +18~20%로 성장은 확실하나, 결제 인프라는 Alipay+·PayPay가 장악. 스타트업 여지는 "숙박 특화 리워드"뿐이며 이는 후보 10으로 흡수.
6. **당사 자산 연결**: 양국 숙박 재고 → 자가형 "숙박 크레딧" 폐쇄형 브리지 정도.
7. **규제 리스크(최고)**: 일본 2026-06 시행 개정 자금결제법(크로스보더 수납대행 = 為替取引, 제3자형 前払式 등록·공탁) [https://www.businesslawyers.jp/articles/1476]; 한국 전금법 선불업 등록·충전금 50% 별도관리 [https://www.fsc.go.kr/no010101/82339]; 환율 개입 시 소액해외송금업. 라이선스 부담 대비 차별화 폭이 가장 작음 → **보류**.

### 후보 12. 한일 진출기업 주재원·출장자 양국 주거 B2B 계정 (본체 추가)

1. **한 줄**: 일본에 신설법인을 내는 한국 기업(연 314社)과 한국 진출 일본 기업에 "도쿄 먼슬리 + 서울 먼슬리를 한 법인 계정·한 인보이스(적격청구서·세금계산서)"로 제공하는 양국 법인 주거 구독.
2. **타겟**: 한국 기업 일본 신설법인 2024년 314社 사상 최다·2025 상반기 218社 [https://www.jetro.go.jp/biz/areareports/special/2025/0101/7645e965c3fc0e32.html], K-스타트업센터 도쿄 2024-05 개소 [https://www.jetro.go.jp/biznews/2024/05/f51d2e361db67f54.html]; 도쿄 핵심 상권 공실률 0%대·K브랜드 임차난(2026-09) [https://www.newspim.com/news/view/20260915000803]; 在韓 일계기업(JETRO 응답 79社, 전체 **미확인**) [https://www.jetro.go.jp/news/releases/2025/13aebb32e58e01ad.html]; 일본인 출장 숙박비 상한 8,878엔 vs 도쿄 ADR 17,147엔(본체 0절), 서울 호텔 요금 상승 [https://note.com/kpopyuriko/n/nca7e262dc58a].
3. **근거 수치**: リブマックス 법인 일괄 계약 10% 증가 [https://www.zenchin.com/news/post-4469.php]; Unito 882실·시리즈D 10억엔·법인 플랜(본체 0절); GTN Korea 법인 전대·일본어 퇴거 정산 [https://prtimes.jp/main/html/rd/p/000000137.000054071.html]; 삼성글로벌리서치 도쿄 사무소 신설 등 대기업 도쿄 거점 확대(2026-03) [https://m.news.nate.com/view/20260330n29946].
4. **존재 검증**: 단방향 법인 주거는 **이미 존재(3+)** — 일본 Unito·リブマックス·Weave·GTN 법인; 한국 スターツソウル https://kaigai.starts.co.jp/korea , エイブル ソウル https://www.able-nw.com/seoul/ , GTN Korea. **양국 한 계정·한 인보이스 구독: 미확인.** 단, GTN이 양국 법인을 이미 갖고 있어 복제 위험 큼.
5. **성장성·미래가치**: 한국 기업의 일본 진출이 사상 최다이고 초기 인력은 1~6개월 체류가 전형 → 본체 "법인 출장자" 세그먼트의 한국 기업판. 독립 사업보다 본체 법인 계정 기능.
6. **당사 자산 연결**: 양국 재고·적격청구서 자동 발행(본체 5절)·한국어 영업.
7. **규제 리스크(낮음)**: 법인 계약은 정기차가·전대 구조로 해결; 세금계산서·적격청구서 양국 병행 발행 체계.

### 검토 후 제외(참고)

- **외국인 임차인 퇴거 정산·원상회복 AI**: REMODELA 「AI退去立会」 2024-12 개시·이용사 100社+ [https://www.zenchin.com/news/content-4390.php] [https://prtimes.jp/main/html/rd/p/000000016.000075721.html] → 이미 존재, 본체가 도입할 도구.
- **재류기한 연동 정기차가·비자 갱신 자동관리**: 사업자 미발견이나 기능 수준이며 본체 계약 엔진에 내장(정기차가는 재류카드 기간 맞춤 계약이 가능하다는 장점만 확인) [https://ielove-cloud.jp/blog/entry-01743/].
- **重要事項説明 다국어 AI**: 국가 14언어 무료 도구·大東建託 9언어 등 존재 [https://classlab.co.jp/services/ai-solution/ai-column/fudosan-gaikokujin-ai-taiou] → 내장 기능.

---

## 3. 스코어링과 상위 5개

기준(각 1~5, 높을수록 유리): 공백(직접 플레이어 부재), 성장(문서화된 수요·정책 순풍), 적합(당사 자산 재사용), 실행(개발자 1명·자본 경량으로 12개월 내 착수 가능성), 규제(리스크가 낮을수록 높은 점수).

| 순위 | 후보 | 공백 | 성장 | 적합 | 실행 | 규제 | 합계/25 | 판정 |
|---|---|---|---|---|---|---|---|---|
| **1** | 1. 크로스보더 Rent-Passport 스코어 API | 5 | 4 | 5 | 3 | 3 | **20** | 최우선. 보증 등록과 동시에 데이터 파이프라인 착수 |
| **2** | 2. 管理組合 외국인 거버넌스 SaaS | 4 | 4 | 3 | 4 | 4 | **19** | 2026-04 区分所有法 트리거, 자사 물건 조합부터 |
| **3** | 3. 호스트 매출 선지급+보증 | 5 | 3 | 4 | 3 | 3 | **18** | 자사 정산채권 한정으로 시작, 貸金業法 구조 검토 |
| **4** | 4. 해외 팬 관계인구 멤버십 | 4 | 3 | 3 | 4 | 4 | **18** | 2026년도 제도 원년, 지자체 1곳 파일럿 |
| **5** | 5. 한국인 오너 도쿄 물건 먼슬리 운영·보증 | 3 | 4 | 4 | 3 | 3 | **17** | 마스터리스 없는 공급 확장 경로 |
| 6 | 12. 한일 진출기업 양국 법인 계정 | 2 | 4 | 4 | 3 | 4 | 17 | 본체 법인 기능으로 흡수 |
| 7 | 6. 재한 일본인 먼슬리+보증 | 2 | 4 | 4 | 3 | 3 | 16 | GTN Korea 진입으로 "이미 존재", 세그먼트로 흡수 |
| 8 | 10. 한일 왕복 Stay Pass | 2 | 3 | 4 | 3 | 4 | 16 | 후보 1·9의 소비자 접점으로 설계 |
| 9 | 9. 양방향 슈퍼앱 | 2 | 4 | 4 | 2 | 3 | 15 | 범용은 선점, 계정 설계로만 |
| 10 | 8. 空き家 한국 채널+운영 | 3 | 4 | 3 | 2 | 2 | 14 | 토지규제 입법 확정 후 재검토 |
| 11 | 7. 크로스보더 부동산 토큰 | 2 | 5 | 2 | 1 | 1 | 11 | 2027-02 이후 AM 제휴 자산 공급자로 |
| 12 | 11. 포인트 브리지 | 2 | 4 | 2 | 2 | 1 | 11 | 보류 |

**상위 5개의 공통점**: 모두 본체 먼슬리 플랫폼의 세 자산(家賃債務保証 데이터, 택건업 면허, 양국 재고)을 재사용하며, 새 라이선스 없이(후보 3의 팩토링 구조 제외) 착수 가능하다. 1·3은 보증 등록 직후, 2·4는 2026년 내 제도 트리거(区分所有法 4월 시행·ふるさと住民 개시)에 맞춰, 5는 택건업 면허 취득 후 순차 착수가 자연스럽다. 12개월 내 가장 큰 경쟁 위협은 GTN(30억엔 조달, 양국 법인, 데이터×AI 선언)으로, 후보 1·6·9·12는 GTN이 먼저 움직일 수 있는 영역이므로 후보 1의 "양국 이력 연결" 데이터 확보 속도가 관건이다.

---

## 4. 미확인 항목 (추가 조사 권장)

- 재류외국인 신용카드 보유율, 외국인 家賃保証 심사 통과율, 한국 포인트 발행액 총액
- 한국 개인의 일본 부동산 취득 신고 건수·금액(한국은행), 도쿄 해외거주자 취득 308호 중 한국인 비중
- 재한 일본인 2025년 법무부 국적별 수치(外務省 44,471명은 스니펫만 확인), 在韓 일계기업 총수
- 管理不全空家 전국 지정 건수, 空き家バンク 전국 평균 성약률, JAPAN PROPERTY CENTRAL URL
- ふるさと住民登録 외국인 등록 가부 공식 확정, 関係人口 중 해외 비율
- 2025년 한일 왕래 공식 합계치(946만+365만 합산 약 1,311만), 2026-06말 일본 재류외국인 수
- 삼삼엠투·엔코의 일본 진출 여부, Clearco·Uplisting Airbnb 호스트 금융 프로그램, 日本財託 외국인 전용 서비스 상세

---

## 5. 주요 출처 (본문 인라인 URL 외 핵심)

- 인적 교류: [JNTO 2026-08](https://www.jnto.go.jp/news/press/20260916_montly.html) · [訪日ラボ 한국 2025](https://honichi.com/news/2026/02/10/inbound-korea-2025/) · [아주경제 2025 방한](https://www.ajunews.com/view/20260130103801235) · [뉴스핌 2026 방한 일본인](https://www.newspim.com/news/view/20260831000073) · [時事 한일 왕래](https://www.jiji.com/jc/article?k=2026013001081&g=int)
- 외국인 통계·정책: [時事 재류외국인 2025말](https://www.jiji.com/jc/article?k=2026032700900&g=pol) · [법무부 2026-06](https://www.moj.go.kr/bbs/immigration/227/608714/artclView.do) · [stepjob 외국인정책 연표](https://stepjob.jp/gaikokujinseisaku/) · [外国人プレス 특정재류카드](https://www.gaikokujin-press.com/archives/2961) · [TMI 토지취득 규제](https://www.tmi.gr.jp/eyes/blog/2026/18051.html)
- 부동산: [nippon.com 해외거주자 취득](https://www.nippon.com/ja/japan-data/h02624/) · [한국경제 도쿄 매입](https://www.hankyung.com/article/2026082776251) · [矢野 家賃保証](https://www.yanoict.com/summary/show/id/776) · [観光庁 民泊](https://www.mlit.go.jp/kankocho/minpaku/business/host/construction_situation.html) · [大和総研 ST](https://www.dir.co.jp/report/research/capital-mkt/it/20260126_025555.pdf) · [BUILT 空き家](https://built.itmedia.co.jp/bt/articles/2405/08/news058.html)
- 경쟁·플레이어: [GTN 30억엔](https://prtimes.jp/main/html/rd/p/000000145.000054071.html) · [GTN Korea](https://prtimes.jp/main/html/rd/p/000000137.000054071.html) · [GTN STAY](https://www.gtn.co.jp/news/20260528) · [Nova Credit×Entrata](https://www.entrata.com/press/entrata-integrates-nova-credits-credit-passport-to-expand-housing-access-for-international-renters) · [Guesty Capital](https://www.guesty.com/features/guesty-capital/) · [Weave×TPG 서울](https://www.mingtiandi.com/real-estate/finance/weave-tpg-team-up-on-550-unit-seoul-rental-project/) · [HafH 20만](https://www.hafh.com/en/topics/19258) · [西川町 NFT](https://forbesjapan.com/articles/detail/62877)
- 규제: [BUSINESS LAWYERS 資金決済法](https://www.businesslawyers.jp/articles/1476) · [법률신문 토큰증권](https://www.lawtimes.co.kr/news/articleView.html?idxno=226492) · [금융위 전금법](https://www.fsc.go.kr/no010101/82339) · [뉴스핌 토허제 연장](https://www.newspim.com/news/view/20260820001214) · [総務省 ふるさと住民](https://www.soumu.go.jp/furusatojuumin/)
