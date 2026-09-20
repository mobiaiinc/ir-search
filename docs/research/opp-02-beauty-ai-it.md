# 화이트스페이스 조사 B — 뷰티·AI·IT (한일 크로스보더 신규사업 후보 12건)

- 조사일: 2026-09-20
- 목적: 외국인관광 도시민박(서울) 운영 + 도쿄 외국인 먼슬리 플랫폼(AI 언더라이팅·임대보증, 経営・管理 비자 대표, 개발자 1명, 宅建士 채용 예정)을 보유한 당사가 **뷰티(K-beauty·미용의료·뷰티테크)·AI·IT** 영역에서 (a) 거의 아무도 하지 않고 (b) 성장 근거가 있으며 (c) 당사 자산으로 선점 가능한 신규사업을 찾는다.
- 전제 문서: 과제에서 지정한 `docs/japan-monthly-c2c-strategy-2026-09.md`는 저장소에 존재하지 않아, 같은 취지의 `docs/foreigner-monthly-strategy-2026-09.md`(§0 결론, §4 타겟, §5 서비스, §6 해자)와 과제 지문의 회사 설명을 전제로 삼았다.
- 방법: WebSearch 약 175회(본 세션 약 55회 + 리서치 보조 2개 약 120회; 한·일·영). WebFetch 대부분 차단 → 수치는 검색 스니펫·보도 인용 기준. **모든 수치 뒤에 [출처 URL]**, 확인 못한 값은 **미확인**, 블로그·업계지 2차 인용은 "(2차)". 의사결정 전 원문 재확인 권장.
- 판정 기준: 직접 경쟁 플레이어 3개 이상 확인 → "이미 존재", 일부 요소만 존재 → "부분 존재", 확인 안 됨 → "공백".

---

## 0. 결론 요약

1. **"뷰티·AI·IT 자체"에는 빈 자리가 거의 없다.** 한국 미용의료 중개(강남언니·トリビュー), AI 피부분석(Perfect Corp·花王·룰루랩), 민박 AI 컨시어지(tripla·AirHost·Kotozna), 重説 AI(Ai-Smart重説·ITANDI), 외국인 정착 앱(Linc·GTN)은 모두 3개 이상 플레이어가 있다. 12개 후보 중 단독 카테고리로 "공백"인 것은 없고, 화이트스페이스는 전부 **"당사만 가진 재고·면허·데이터와 결합할 때만 생기는 교차 니치"**였다.
2. **가장 큰 기회는 뷰티가 아니라 "회복기 체류"다.** 2025년 한국 외국인환자 201만 명 중 일본인 60만 명(29.8%), 성형외과 외국인환자의 42.0%가 일본인이다 [https://www.mohw.go.kr/board.es?mid=a10503010100&bid=0027&act=view&list_no=1490280]. 예약 중개는 레드오션이지만 "민박/먼슬리 + 일본어 사후관리 + 귀국 후 도쿄 팔로업"을 표준 상품화한 사업자는 없고, 서울시가 2026-09에 처음으로 '의료친화 숙박시설' 공모를 냈다 [https://www.rapportian.com/news/articleView.html?idxno=240266]. → **후보 A, 1순위.**
3. **AI/IT의 진짜 자산은 "외국인 심사 데이터"다.** 일본 외국인의 39.3~40%가 입주 거절을 경험하고 [https://www.moj.go.jp/isa/content/001342229.pdf], 家賃保証 시장은 연 7% 성장해 FY2025 2,724억 엔이다 [https://www.tokyo-takken.or.jp/re-port/78927]. 당사 본업(AI 언더라이팅+보증)의 손실률 데이터를 宅建업자용 "외국인 특화 AI SaaS"(후보 E)와 한일 "임차인 신용 패스포트 API"(후보 H)로 외부화하는 것이 2·3순위다. 두 후보는 하나의 제품 로드맵(E가 채널, H가 데이터)으로 묶는다.
4. **규제가 만드는 창(窓)이 하나 있다.** 観光庁는 2026-07-15 자치체에 민박 "ICT 관리 의무" 조례화를 허용했다 [https://www.mlit.go.jp/kankocho/news06_00067.html]. 조례 제정 사이클(2026 하반기~2027)에 맞춘 컴플라이언스형 운영 AI(후보 F)는 통지 직후라 아직 통합 사업자가 없다. 4순위.
5. **한국 개발자 랜딩 패키지(후보 D)는 적합도는 최고이나 TAM이 작다**(K-Move 일본 취업 연 1,531명 [https://v.daum.net/v/20251104111647123]). 먼슬리 B2B 판매 채널로만 붙인다. 5순위.
6. **제외·보류**: 한국인 대상 일본 미용의료(B, 수요 근거 없음), 인바운드 데이터 판매(I, 대형 데이터 보유자 선점·2차 이용 금지), AI 통역 체크인(J, 5개 이상 존재), 외국인 정착 AI 앱(Linc 3억 엔 조달 등, 이미 존재). 분쟁 AI(K)·고령 오너 AI(G)·클리닉 MSO(L)·K-beauty 패널(C)은 독립 사업이 아니라 상위 후보의 기능으로 흡수한다.

---

## 1. 매크로 수치 (2025–2026)

| 항목 | 수치 | 시점 | 출처 |
|---|---|---|---|
| 방일 외국인·소비 | 4,268만 명 · 9조 4,559억 엔(+16.4%) · 1인당 22.9만 엔 · 쇼핑 2조 5,490억 엔 | 2025 | [観光庁](https://www.mlit.go.jp/kankocho/news02_00071.html), [やまとごころ](https://yamatogokoro.jp/inbound_data/59160/) |
| 한일 왕래 | 방일 한국인 9,459,600명(1위) · 방한 일본인 365만 명(최다) · 합계 1,300만 명 초과 | 2025 | [訪日ラボ](https://honichi.com/news/2026/02/10/inbound-korea-2025/), [時事](https://www.jiji.com/jc/article?k=2026013001081&g=int) |
| 방한 외래객 | 1,894만 명(최다) | 2025 | [やまとごころ](https://yamatogokoro.jp/inbound_data/59369/) |
| 재류외국인(일본) | 4,125,395명(+9.5%) · 한국 407,341 · 技人国 475,790 · 유학 464,784 | 2025-12 | [nippon.com](https://www.nippon.com/ja/news/kd1410172998839256010/) |
| 체류외국인(한국) | 2,874,278명 · 등록 1,636,922 | 2026-06 | [법무부](https://www.moj.go.kr/bbs/immigration/227/608714/artclView.do) |
| 한국 외국인환자 | 2,011,822명(+71.9%) · 일본인 600,009(29.8%) · 의료관광 지출 12.5조 원 | 2025 | [복지부](https://www.mohw.go.kr/board.es?mid=a10503010100&bid=0027&act=view&list_no=1490280) |
| 일본 화장품 시장 | FY2024 2조 5,800억 엔(+4.1%) · FY2025 2조 6,500억 엔 예측 | 2025 | [矢野経済](https://www.yano.co.jp/press-release/show/press_id/3922) |
| 일본 미용의료 시장 | 6,310억 엔(+6.2%) | 2024 | [矢野経済](https://www.yano.co.jp/press-release/show/press_id/3844) |
| K-beauty 수출 | 114억 달러(최대) · 미국 22억·중국 20억·일본 11억(10.87억, +4.9%) | 2025 | [뷰티누리](https://www.beautynury.com/m/news/view/110396/cat/20) |
| 일본 화장품 수입 중 한국 | 1,417.7억 엔(+5.6%) · 점유 30.8% 1위(2022~) | 2025 | [商業界](https://www.syogyo.jp/news/2026/03/post_043406) |
| 일본 내 한국코스메 시장 | 1,798억 엔(+23.1%) | 2025 | [DreamNews](https://www.dreamnews.jp/press/0000348216) |
| 일본 生成AI 시장 | 2024년 1,016억 엔 → 5년 내 8,000억 엔(IDC) · AI시스템 2025년 2조 3,725억 엔 → 2029년 6조 8,897억 엔(CAGR 36.0%) | 2025 | [IDC](https://my.idc.com/getdoc.jsp?containerId=prJPJ52722724), [IDC](https://www.idc.com/resource-center/blog/%E5%9B%BD%E5%86%85ai%E5%B8%82%E5%A0%B4%E3%81%AF%E4%BB%8A%E5%BE%8C4%E5%B9%B4%E3%81%A7%E7%B4%843%E5%80%8D%E3%81%AB%E6%88%90%E9%95%B7%EF%BC%9A-2029%E5%B9%B4%E3%81%AE%E5%9B%BD%E5%86%85ai%E5%B8%82%E5%A0%B4/) |
| 일본 AI 정책 | AI推進法 2025-05-28 성립·09-01 전면 시행(벌칙 없음, 7조 활용사업자 노력의무) · 人工知能基本計画 2025-12-23 각의결정 · 2025년 AI 직접지원 예산 1,969억 엔(+67.4%) | 2025 | [내각부](https://www8.cao.go.jp/cstp/ai/ai_act/ai_act.html), [기본계획](https://www8.cao.go.jp/cstp/ai/ai_plan/aiplan_20251223.pdf), [이데일리](https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=03660486645320016) |
| 일본 스타트업 투자 | 7,613억 엔(부채 제외, 횡보) · AI 한정 총액 **미확인** · Sakana AI 시리즈B 약 320억 엔 | 2025 | [스피다](https://initial.inc/articles/japan-startup-finance-2025), [STARTUP DB](https://lp.startup-db.com/media/articles/20251117-1121) |
| 한국 스타트업 투자 | 6조 5,724억 원(1,155건) · AI 비중 23.6%(2022년 9.4%→) · 모태펀드 AI 출자 3,180억 원 | 2025 | [wowtale](https://wowtale.net/2026/01/02/252647/), [네이트](https://news.nate.com/view/20260120n30518) |
| 한일 스타트업 교류 | 한일 공동펀드 1억 달러(모태펀드·JIC) · K-스타트업센터 도쿄 · SusHi Tech Tokyo 2026 60개국 770사 | 2025–26 | [정책브리핑](https://www.korea.kr/briefing/pressReleaseView.do?newsId=156635549), [platum](https://platum.kr/archives/285937) |
| 일본 IT 인력 부족 | 2030년 최대 79만 명(중위 45만) | 経産省 | [日経](https://www.nikkei.com/article/DGXZQOUC2425Y0U5A221C2000000/) |
| 일본 家賃債務保証 시장 | FY2024 2,548.6억 엔(+6.7%) · FY2025 2,723.9억 엔 · FY2029 3,500억 엔 초과 | 2025 | [東京都宅建協会](https://www.tokyo-takken.or.jp/re-port/78927) |
| 일본 宅建業者 | 132,291사(11년 연속 증가) | 2025-03 | [国交省](https://www.mlit.go.jp/report/press/tochi_fudousan_kensetsugyo16_hh_000001_00105.html) |
| 일본 民泊 届出住宅 | 42,070건(누계 65,837, 폐지 23,767) | 2026-07 | [観光庁](https://www.mlit.go.jp/kankocho/minpaku/business/host/construction_situation.html) |
| 한국 도시민박 | 영업중 6,134명 · 서울 3,869(63.1%) · 마포 1,293 | 2025-06 | [위홈](https://www.wehome.me/trust/ko/report-urbanstay-202506/) |
| 経営・管理 비자 | 2025-10-16부터 자본금 3,000만 엔+상근 1명, 경과조치 2028-10-16까지 | 2025 | [中小企業経営支援事務所](https://www.sme-support.co.jp/column/p1303/) |
| 원/엔 환율 | 100엔=868원(2026-08-21, 3년 최저)~887원(09-17) | 2026-09 | [kgosu](https://www.kgosu.com/2026/09/2026-9-9.html) |

---

## 2. 후보별 상세 (12건)

### 후보 A. 일본인 대상 한국 미용의료 관광 + 회복기 민박/먼슬리 패키지

1. **아이디어 한 줄**: 일본인 피부과·성형 환자에게 "시술 예약 + 일본어 케어·통역 + 회복기 숙박(민박/먼슬리) + 귀국 후 LINE 사후관리"를 한 묶음으로 파는 회복 특화 스테이 패키지.
2. **타겟**: 2025년 방한 일본인 365만 명(2019년 대비 108.2%) [https://www.ajunews.com/view/20260130103801235]; 2025년 한국 외국인환자 2,011,822명(+71.9%) 중 일본인 600,009명(29.8%, 2위) [https://www.mohw.go.kr/board.es?mid=a10503010100&bid=0027&act=view&list_no=1490280]; 피부과 외국인환자 131.3만 명(62.9%) 중 일본인 399,964명(30.5%), 성형외과 23.3만 명 중 일본인 97,847명(42.0%, 1위) [동상]; 2024년 피부과 방문 일본인 30.8만 명, 94% 여성, 20대 20% [https://v.daum.net/v/20251007143338257]; 일본인 피부과 환자 85% 이상이 4박 미만 [https://afterdoc.ai/blog/%EC%99%B8%EA%B5%AD%EC%9D%B8%ED%99%98%EC%9E%90%EC%9C%A0%EC%B9%98-%EC%9D%BC%EB%B3%B8-%ED%99%98%EC%9E%90%EC%9D%98-%ED%8A%B9%EC%A7%95%EA%B3%BC-%EC%A0%84%EB%9E%B5-%ED%8F%AC%EC%9D%B8%ED%8A%B8-67219] → 회복기(1주+) 숙박 수요는 성형외과(9.8만 명)에 집중; 서울 외국인환자 176만 명(+75.6%), 강남구 65만 명 [https://www.edaily.co.kr/News/Read?newsId=02017206645579792], [https://landvalueup.hankyung.com/valueupguide-20260915-0700].
3. **근거 수치**: 방한객 1천 명당 외국인환자 2019년 28.4명 → 2025년 106.2명 [https://magazine.hankyung.com/business/article/202608301297b]; 2025년 외국인환자·동반자 의료관광 지출 12.5조 원, 의료지출 3.3조 원 [https://www.mohw.go.kr/board.es?mid=a10503010100&bid=0027&act=view&list_no=1490280]; 2026-07 서울 외국인 의료소비액 2,131억 원(+66.5%) [https://www.medicaldaily.co.kr/post/120565]; 일본 미용의료 시장 2024년 6,310억 엔(+6.2%) [https://www.yano.co.jp/press-release/show/press_id/3844]; 日経MJ 2026-02 조사: 최근 1년 미용의료 이용 여성 502명 중 "한국에서 시술" 약 23% [https://www.nikkei.com/article/DGXZQOUC140YS0U6A210C2000000/]; SBC 2025-06 조사: 한국 미용피부과 경험 여성 1,002명, 도한 이유 "비용 저렴" 43.9%, "SNS 인플루언서" 37.1% [https://prtimes.jp/main/html/rd/p/000000230.000097803.html]; minfor 조사 20~50대 여성 57%가 한국 미용시술에 관심 [https://prtimes.jp/main/html/rd/p/000000013.000158040.html]; 강남언니 일본 유저 160만 명·제휴병원 1,500곳(2025-10) [https://www.mt.co.kr/future/2025/10/15/2025101511535184320], 강남언니 경유 일본인 예약 2023년 8만 → 2024년 12만 명 [https://magazine.hankyung.com/business/article/202608301297b]; 회복 호텔 시세 15만~40만 원/박 [https://koreaexperience.com/blog/korean-medical-tourism-recovery-hotels-and-aftercare-guide-2026]; 외국인 미용성형 부가세 환급 특례 2025-12-31 종료 [https://www.newsis.com/view/NISX20250731_0003273026], [https://news.nate.com/view/20251204n27886] → 2026년부터 가격 메리트 축소; "渡韓ガールズ" 인구 추계 **미확인**.
4. **존재 검증**:
   - 예약·중개(한국계): 강남언니(일본 유저 160만) [https://www.mt.co.kr/future/2025/10/15/2025101511535184320]; 바비톡 2025-08 일본 웹서비스 [https://zdnet.co.kr/view/?no=20250825181344]; 여신티켓(일본 가입자 200%↑) [https://supple.kr/news/cmrudmyed004w7pokrw3yj65h]
   - 예약·중개(일본계): トリビュー(한국 클리닉 429건) [https://tribeau.jp/countries/2/clinics]; minfor [https://minfor.jp/beauty/9191/]; HIS·JTB 시술 패키지 [https://otonari-korea.com/?p=330]; VELTRA 美容クリニック 카테고리 [https://www.veltra.com/jp/asia/korea/seoul/ctg/202278:beautyclinic/]; 江南ビューティーラウンジ [https://gan-beautylounge.com/]; ロコタビ 동행통역 [https://locotabi.jp/seoul/services/41565]; リエンジャン 제휴호텔 무료숙박 [https://jplienjang.com/beauty-fullservice/]; JK성형외과(외국인 연 4,000명) [https://jkplastic.com/jp/]
   - 회복기 숙박: 강남 리커버리 호텔 다수 [https://cyl.co.kr/id/blog/g-007-seoul-recovery-hotels/], [https://www.koreanplasticsurgery.info/post/recovery-hotel-vs-airbnb-vs-hospital-stay-in-korea-complete-guide-korean-plastic-surgery]; 위홈 '케어스테이' [https://wehome.me/trust/ko/carestay/]; 쿠시먼앤드웨이크필드 강남 '웰니스 스테이' [https://landvalueup.hankyung.com/valueupguide-20260915-0700]; 서울시·서울관광재단 '서울의료친화 숙박시설' 첫 공모(2026-09-14~30) [https://www.rapportian.com/news/articleView.html?idxno=240266]; 강남구 메디컬투어센터 [https://medicaltour.gangnam.go.kr/content/9/view.do?lang=ko&mid=2-9&cid=9]; "Meeting Beauty" 실체 **미확인**
   - **판정: 중개·예약은 "이미 존재"(3+). 회복기 숙박은 "부분 존재"** — 호텔형·클리닉 제휴호텔은 있으나 "민박/먼슬리 + 일본어 사후관리 + 귀국 후 LINE 팔로업"을 표준 상품화한 사업자는 검색상 없음. 서울시가 2026-09 첫 공모를 낸 것 자체가 공급 미정형의 신호.
5. **성장성·미래가치**: 외국인환자 2019→2025 4배 이상, 방한객 대비 환자 비율 3.7배 상승 [https://magazine.hankyung.com/business/article/202608301297b]; 일본 미용의료 시장 성장·"肌管理" 용어 정착 → 리피터 구조 [https://www.nikkei.com/article/DGXZQOUC140YS0U6A210C2000000/]. 리스크: 부가세환급 종료, 엔저로 일본 국내 시술과 총액 격차 축소 보도 [https://private-skin.clinic/blog/article-other/korea-beauty-guide-2026/] → 가격 우위보다 "회복 경험·사후관리" 차별화 필요.
6. **당사 자산 연결**: 등록 도시민박(서울) = 회복기 숙박 인프라 즉시 가동, 서울시 '의료친화 숙박시설' 공모 대상 [https://www.rapportian.com/news/articleView.html?idxno=240266]; 도쿄 법인·일본어 CS = 일본 측 집객·귀국 후 LINE 사후관리 창구(도쿄 제휴 클리닉 연계); AI 언더라이팅 노하우 → 시술 유형별 필요 체류일·객실 조건 자동 패키징; 게스트 데이터 → 성형외과(일본인 42%) 대상 B2B 리퍼럴.
7. **규제 리스크**: 「의료 해외진출 및 외국인환자 유치 지원에 관한 법률」 유치업자 등록(자본금 1억 원 이상, 종합여행업 등록 시 5천만 원, 보증보험, 유효 3년) [https://news.seoul.go.kr/welfare/archives/531323], [https://medicaltour.gangnam.go.kr/content/402/view.do?lang=ko&cid=402&mid=395-400]; 「외국인환자 적정 유치 수수료율 고시」 의원 30%·병원 20%·상급종합 15% 상한 [https://www.monews.co.kr/news/articleView.html?idxno=97781]; 관광진흥법 여행업 등록(항공·숙박 결합 판매 시) [https://www.law.go.kr/flDownload.do?flSeq=97940219]; 일본 医療広告ガイドライン(医療法 제6조의5) — 誘引性+特定性 충족 시 소개사이트도 규제, 비포애프터·체험담 제한 [https://cl-mirai-lab.doctorsfile.jp/article/4099], [https://zelojapan.com/en/lawsquare/38129], 해외 의료기관 광고 적용 여부 **미확인**; 일본 旅行業法(第3種 受注型企画旅行) [https://www.meti.go.jp/policy/mono_info_service/healthcare/iryou/downloadfiles/pdf/28fy_gyoumumanual.pdf]; 도시민박 내 의료행위 불가 → 방문간호·클리닉 연계로 분리(**미확인**).

### 후보 B. 한국인 대상 일본 미용의료·치과·인간독 + 엔저 + 먼슬리/민박 번들

1. **아이디어 한 줄**: 엔저를 활용해 한국인에게 일본 인간독(PET·MRI)·치과·재생의료를 한국어 코디 + 도쿄 먼슬리/민박과 묶어 판매.
2. **타겟**: 2025년 방일 한국인 9,459,600명(+7.3%, 국적별 1위) [https://www.news1.kr/industry/hotel-tourism/6046959]; 2024년 방일 한국인 1인당 지출 10.6만 엔 [https://honichi.com/news/2025/02/26/inbound-korea-2024/]; 일본 줄기세포 의료관광 한국인 연 3만 명 추산, 일본 원정치료 연 1조 원 규모 보도(2026-05) [https://www.dailymedi.com/news/news_view.php?ca_id=2212&wr_id=902872], [https://m.news.nate.com/view/20260511n27451]; 한국인의 일본 미용의료·치과·인간독 수요 정량 **미확인**.
3. **근거 수치**: 엔화 2026-08-21 100엔=868원(약 3년 최저), 2026-09-17 887원 [https://www.kgosu.com/2026/09/2026-9-9.html], [https://ttegl.com/jpy-krw-exchange-rate-forecast-2026/]; 일본 의료 인바운드 渡航者 약 2~3만 명(태국 360만, 한국 49만 대비) [https://mediphone.jp/medico-plus/mt_current_situation/]; 医療滞在ビザ 2023년 2,295건, 2024년 중국 846건으로 급감 [https://jpnmedical.com/japan/334/], [https://note.com/yayota/n/n10e377b1b7c0]; 일본 의료관광 시장 2025년 59.8억 달러 → 2030년 161.6억 달러(CAGR 22%, Mordor) [https://www.marketresearch.co.jp/insights/medical-tourism-market-mordor/]; 경산성 医療インバウンド 検討会 中間とりまとめ(2025-06) [https://www.meti.go.jp/shingikai/mono_info_service/medical_inbound/pdf/20250612_1.pdf], [https://www.travelvoice.jp/20250903-158088]; 재생의료 인바운드 외국인 약 8할 중국인 [https://biyouhifuko.com/news/japan/6909/].
4. **존재 검증**: JTB 医療ツーリズム [https://www.jtbbwt.com/business/service/solution/inbound/japan-travel-note/medical-healthtourism/]; HIS 医療ツーリズム [https://www.his-j.com/japan-tourist/service/medical-tourism/ja/]; JMHC [https://j-medical-healthcare.com/hti/medicaltourism/]; 恋する美容メディカルツーリズム [http://medical-tourism.co.jp/]; BIANCA CLINIC 訪日 재생의료 [https://prtimes.jp/main/html/rd/p/000000005.000098584.html]; Korea-M Clinic(긴자, 한국계) [https://korea-m.clinic/]; TIMC TOKYO 인간독+의료통역 투어 [https://www.tripadvisor.com/AttractionProductReview-g1066444-d24074048-Tokyo_2_Day_Medical_Checkup_Tour_with_Medical_Interpreter-Chuo_Tokyo_Tokyo_Prefec.html]; HopGo 일본 건강검진 리트리트 [https://hopgo.jp/japan-health-checkup-retreat/]; 차바이오텍 도쿄셀클리닉·네이처셀 후쿠오카 [https://www.hankyung.com/article/2023071348921]; 한국 여행사의 일본 인간독 상품 **미확인**. → **판정: "부분 존재"** — 일본 측 코디는 다수(중국인 중심), 한국인 특화 코디+숙박 번들은 소수. 단, 미용의료 한국인 수요는 근거 없음(한국이 미용 공급 우위).
5. **성장성·미래가치**: 강점 영역은 미용이 아닌 재생의료(줄기세포·엑소좀, 일본 2014 再生医療法) ·인간독·치과 — 한국 규제 공백을 일본이 메우는 구조 [https://www.hankyung.com/article/2023071348921]; 방일 한국인 946만의 일상화 + 엔저. 약점: 인바운드 의료 전체 2~3만 명, 医療滞在ビザ 감소 → 시장이 작고 정책 초기.
6. **당사 자산 연결**: 도쿄 법인+먼슬리 = 치과(4~6개월 간격)·재생의료 반복 투여 시 체류 수용; 한국 채널로 모객; AI로 검진 결과 요약·리마인드.
7. **규제 리스크**: 일본 医療広告ガイドライン [https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000206553_00012.html]; 医療滞在ビザ 身元保証機関 등록(과거 1년 외국인 환자 10명 이상 수용 실적 등) [https://www.mlit.go.jp/kankocho/seisaku_seido/iryotaizai_visa/index.html], [https://www.meti.go.jp/policy/mono_info_service/healthcare/kokusaitenkai/iryotokoshienkigyomuke.html]; 일본 旅行業法 등록 [https://www.meti.go.jp/policy/mono_info_service/healthcare/iryou/downloadfiles/pdf/28fy_gyoumumanual.pdf]; 한국 관광진흥법 여행업 등록 [https://www.law.go.kr/flDownload.do?flSeq=97940219]; 한국 의료법 제27조 제3항(영리 목적 환자 유인·알선 금지)의 해외 의료기관 알선 적용 여부 **미확인**; 미승인 치료 알선 시 표시광고법 리스크.

### 후보 C. K-beauty × 일본 D2C/체험형 커머스 (AI 피부분석 + 게스트 샘플링·패널 데이터)

1. **아이디어 한 줄**: (i) 서울 민박·도쿄 먼슬리 게스트에게 K-beauty 샘플·체험 키트를 제공하고 실사용 반응을 1st-party 패널 데이터로 브랜드에 판매, (ii) AI 피부분석 → 한국 화장품/시술 추천 → 구매·예약 연결.
2. **타겟**: 일본 내 한국코스메 시장 2025년 1,798억 엔(+23.1%, 일본 화장품 총시장의 6.1%) [https://www.dreamnews.jp/press/0000348216]; 방한 외국인 쇼핑 품목 1위 향수·화장품 71.8%(2024 외래관광객조사) [https://www.kcti.re.kr/web/board/boardContentsView.do?contents_id=969e40a59b534173bb2911c714ae929d&board_id=14]; 외국인 카드 소비 2026-05 2조 1,222억 원(첫 2조 돌파) [https://news.nate.com/view/20260617n28657]; 재류외국인 412.5만 명, 도쿄 80.1만 명, 한국 국적 40.7만 명 [https://news.yahoo.co.jp/articles/9376942d6fb001f7e7a1953d05a4979ab5862821]; 방일객 쇼핑 지출 2025년 2조 5,490억 엔 [https://www.mlit.go.jp/kankocho/content/002003329.pdf].
3. **근거 수치**: 일본 화장품 수입 2025년 4,460.7억 엔(+3.1%), 한국산 1,417.7억 엔(+5.6%) 점유 30.8% 1위(2022년부터 1위) [https://www.syogyo.jp/news/2026/03/post_043406]; 한국 화장품 대일 수출 2024년 10.36억 달러(+29.2%) [https://www.cosinkorea.com/news/article.html?no=53910], 2025년 10.87억 달러(+4.9%, 3위) [https://www.beautynury.com/m/news/view/110396/cat/20]; 일본 화장품 시장 FY2024 2조 5,800억 엔(+4.1%), FY2025 2조 6,500억 엔 예측 [https://netshop.impress.co.jp/n/2025/12/10/15272], [https://www.yano.co.jp/press-release/show/press_id/3922]; Qoo10 2025년 1회차 메가와리 유통액 490억 엔(+25%) [https://netshop.impress.co.jp/node/13650], [https://netkeizai.com/articles/detail/13837]; 돈키호테 코스메 9만 점, 한국 브랜드 점유율 **미확인** [https://digitalpr.jp/r/118328]; @cosme 베스코스 한국 브랜드 수상 수 **미확인**, Anua 6관 [https://girlspremium.jp/articles/view/3426]; 아모레성수 방문객 80% 이상 외국인(AI 피부진단) [https://biz.heraldcorp.com/article/10733695]; 마키아(集英社) 호텔 인바운드 샘플링 11개 호텔·연 외국인 숙박 60만 명 [https://adnavi.shueisha.co.jp/news/5533/]; Payke 누적 550만 DL, 인바운드 구매 데이터 패키지 판매 [https://payke.co.jp/news/20250116]; 에이피알 2025-1Q 일본 매출 293억 원(전년 동기 3배), 메가와리 2주 10.6억 엔 판매 1위 [https://v.daum.net/v/20250917060222095], [https://www.startuptoday.co.kr/news/articleView.html?idxno=568839].
4. **존재 검증**:
   - AI 피부분석: Perfect Corp → 花王 BeauScope next(2025) [https://prtimes.jp/main/html/rd/p/000000242.000066482.html]; 花王 肌id [https://md-next.jp/13978]; 資生堂 Optune 2020-06 종료(서브스크 실패) [https://xtrend.nikkei.com/atcl/contents/18/00888/00005/]; @cosme 肌遺伝子モード判定(2025-05) [https://www.istyle.co.jp/news/press/2025/05/0521.html]; Haut.AI [https://haut.ai/product/ai-skin-analysis]; 룰루랩 LUMINI(룰루랩재팬 JV, 2025 매출 30.9억 원) [https://www.thekbs.co.kr/news/articleView.html?idxno=1109]; 화해 [https://www.hwahae.com/en]; 아트랩 스킨로그 [https://www.thekbs.co.kr/news/articleView.html?idxno=13137]
   - 샘플링·서브스크: 마키아×코아글로벌 호텔 샘플링 [https://adnavi.shueisha.co.jp/news/5533/]; DHC 아메니티 [https://www.dhc-amenity.com/about/]; 호텔 샘플링 대행사 다수 [https://bizpa.net/mag/sampling-hotel/]; 한국코스메 정기편(marichanbox, ハハホホBOX 등) [https://my-best.com/4973], [https://pickys-life.jp/cosmetic-subscription/]; 민박·먼슬리 게스트 대상 K-beauty 샘플링 사업자 **검색상 없음**
   - 인바운드 구매 데이터: Payke [https://payke.co.jp/analytics]; 신한카드 DataBada [https://databada.shinhancard.com/]; KT TrIP [https://enterprise.kt.com/pd/P_PD_AI_BD_001.do]; 오렌지스퀘어 [https://www.sedaily.com/article/20038763]; 한국관광 데이터랩 [https://datalab.visitkorea.or.kr/]
   - **판정: (ii) AI 피부분석→추천은 "이미 존재"(기술 커머디티화). (i) 숙박 게스트 샘플링+체험+패널 데이터는 "부분 존재"** — 호텔 채널·카드 데이터는 있으나 "장기체류 외국인의 실사용 반응(리뷰·재구매) 패널"을 민박/먼슬리에서 수집·판매하는 사업자는 없음.
5. **성장성·미래가치**: 한국산 수입 1위(30.8%)·일본 내 한국코스메 +23.1% → 신규 브랜드의 "일본 진입 전 테스트 마케팅·샘플 피드백" 수요(Qoo10 메가데뷔 등) [https://www.fashionsnap.com/article/qoo10-mega-debut-2025-result/]; 외국인 소비가 실용·웰니스로 이동, 화장품 +35% [https://www.wikitree.co.kr/articles/1102676]. 리스크: 샘플링 단가 낮음, Optune처럼 서브스크 이탈 높음, 패널 규모(수천 명/월) 확보가 관건.
6. **당사 자산 연결**: 서울 민박 + 도쿄 먼슬리 = 양국 1st-party 패널; 게스트 국적·체류기간·연령 데이터 → 타깃 샘플링·설문(Payke 대비 "실사용 기간" 데이터가 차별점); Perfect Corp/Haut.AI API 활용해 자체 AI 개발 없이 진단→추천→클리닉 예약 연결 가능.
7. **규제 리스크**: 일본 薬機法 제66조 효능 표현 제한·景品表示法 스텔스마케팅 규제(2023-10~); 한국 화장품법 제13조 표시광고; 피부 이미지 = 민감정보 가능성(한·일 개인정보법); 시술 추천 시 한국 의료법 제56조·일본 医療広告ガイドライン; 일본 화장품 반입 시 化粧品製造販売業 허가(무상 샘플 포함, 세부 **미확인**).
### 후보 D. 한국 개발자·AI 인력 일본 공급 + 먼슬리 주거 번들 "랜딩 패키지"

1. **아이디어 한 줄**: 한국 개발자/AI 인력을 일본 기업에 취업·원격·준위임(SES형)으로 공급하고, 당사 도쿄 먼슬리 + AI 심사·임대보증 + 정착 지원을 하나의 "랜딩 패키지"로 묶어 기업(B2B)에 판매.
2. **타겟**: 수요측 — 일본 중소·중견 IT/SES 기업(KOTRA 2025 가을 일본 온라인 잡페어 참가 88개사 중 IT 31개사, 500명 채용 목표) [https://www.sedaily.com/NewsView/2H0EF1N0QE], [https://www.kita.net/board/totalTradeNews/totalTradeNewsDetail.do?no=69736&siteId=1]. 공급측 — K-Move 일본 취업자 2024년 1,531명(전체 해외취업 5,720명의 26.8%, 일본이 4년 만에 1위) [https://v.daum.net/v/20251104111647123]; 일본 내 한국인 취업자 75,003명(2024-10), 전문·기술직 비자 34,688명, IT 종사자 비중 13.4% [https://news.nate.com/view/20260317n32006]. 지역: 도쿄.
3. **근거 수치**: 일본 IT인재 부족 2030년 최대 약 79만 명, 중위 약 45만 명(経済産業省) [https://www.nikkei.com/article/DGXZQOUC2425Y0U5A221C2000000/], [https://www.meti.go.jp/shingikai/economy/daiyoji_sangyo_skill/pdf/001_06_00.pdf]; 帝国データバンク(2024-06~07, 4,705사) 生成AI 활용 기업 17.3%, 애로 1위 "AI 인재·노하우 부족" 54.1% [https://aismiley.co.jp/ai_news/teikokudatabank-generative-ai-utilize-survey/]; 総務省 令和7년판 情報通信白書 生成AI 활용 방침 보유 기업 68.9%(2024년도 49.7%→) [https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r07/html/nd112220.html]; 2025년 中小企業 한정 生成AI 도입률 단일 공식치 **미확인**(조사별 17.3%~64.4% 편차 [https://ai-japan-index.com/genai-adoption-dashboard/]); 技術・人文知識・国際業務 재류자 418,706명(2024년 말) [https://www.moj.go.jp/isa/publications/press/13_00052.html] → 475,790명(2025년 말) [https://www.nippon.com/ja/news/kd1410172998839256010/]; 한국 국적 技人国 인원 **미확인**; SES/엔지니어 파견 시장 2024년도 약 1조 엔, 2030년 약 1.7조 엔(2차) [https://www.itcross.jp/media/1593/]; 2025년판 오프쇼어개발백서 발주처 1위 베트남 43% [https://shiftasia.com/ja/column/2025%E5%B9%B4%E7%89%88%E3%82%AA%E3%83%95%E3%82%B7%E3%83%A7%E3%82%A2%E9%96%8B%E7%99%BA%E7%99%BD%E6%9B%B8%E3%81%8B%E3%82%89%E8%AA%AD%E3%81%BF%E8%A7%A3%E3%81%8F%E6%9C%80%E6%96%B0%E5%8B%95%E5%90%91/]; 일본 오프쇼어 시장 공식 총액 **미확인**.
4. **존재 검증**:
   - 취업 알선(한→일): K-Move 스쿨 [https://www.worldjob.or.kr/ovsea/sdytrn.do]; KOTRA 일본 온라인 잡페어(2025 봄 92개사·가을 88개사) [https://jffds.kotra.biz/fairDash.do?hl=KOR]; 마이나비코리아 [https://www.mynavikorea.co.kr/]; 파소나코리아 JOBHAKU [https://www.pasona.co.kr/]; 원티드 Work in Japan [https://event.wanted.co.kr/work_in_japan]; 사람인 일본 채용 [https://www.saramin.co.kr/zf_user/jobs/list/overseas?loc_cd=211200]; 코리아IT아카데미 [https://www.koreaisacademy.com/], 솔데스크 [https://soldesk.com/SBT_/?idx=92], 하이미디어 [https://www.himedia.co.kr/job/jit]; 일본 측 한국인 대응 인재소개사 [https://gaikokusaiyo.com/agency_nationality/kr/], kedomo [https://career.kedomo.com/engineer/]
   - 원격 아웃소싱: 코드벤터 [https://www.codeventer.com/japan-it-outsourcing-market-entry/]; ハイブリッドテクノロジーズ(4260, 베트남 BrSE) [https://hybrid-technologies.co.jp/]; 벤티지·케이엔에프 **미확인**
   - 외국인 인재 주거 번들: GTN(누적 70만 건 상담, 25언어 AI+유인 챗) [https://www.gtn.co.jp/business/support], 수용기업용 포털 BEST-ESTATE.JP for Partner(2026-06) [https://www.gtn.co.jp/news/20260625]; マイナビBiz 외국인 사원 가구부 주거 [https://biz.mynavi.jp/lp_theme/global]; YOLO JAPAN(등록 40만 명, YOLO HOME) [https://www.yolo-japan.co.jp/]; 리로 외국인 가구부 임대 [https://www.relo.jp/soumujinji365/foreigner-residence/]; クロスハウス [https://x-unit.jp/corporate/column/166/]
   - **판정: 취업 알선·주거 번들 각각은 "이미 존재"(3+). "한국 개발자 특화 × 채용 + AI 심사 기반 즉시 입주 먼슬리 + 정착/원격 전환" 단일 상품은 검색상 없음 → 조합 관점 "부분 존재".**
5. **성장성·미래가치**: 구조적 인력 부족(2030년 79만 명)이 확정 추세, K-Move에서 일본이 취업국 1위 [https://v.daum.net/v/20251104111647123]; 외국인 채용 시 최대 병목이 주거 수배임을 인사 실무 자료가 반복 지적 [https://biz.mynavi.jp/contents/134], [https://atinn.jp/information/housing-arrangement-guide-for-foreign-employees/]. 리스크: 한국인 일본 취업 절대 규모가 연 1,500명대로 TAM이 작음 → 수익은 알선 수수료가 아니라 주거·보증·SES 마진의 반복 매출로 설계.
6. **당사 자산 연결**: 도쿄 먼슬리 재고+AI 언더라이팅+보증 → 재류카드 발급 전 법인계약(먼슬리의 강점) [https://biz.mynavi.jp/contents/134]; 서울 민박 게스트·한국 채널 → 후보자 파이프라인; 일본 법인·宅建 → 사택 대행 계약 주체; 개발 역량 → 스킬 평가·매칭·주거 심사 데이터 통합.
7. **규제 리스크**: 労働者派遣法 파견 허가(기준자산 2,000만 엔×사업소, 현금 1,500만 엔×사업소) [https://ayusawa-partners.jp/column/haken-jigyou-kyoka]; SES 준위임의 위장청부 리스크 [https://lassic.co.jp/media/column/media-2008044/]; 職業安定法 有料職業紹介 허가(현금 150만 엔+) [https://jsite.mhlw.go.jp/mie-roudoukyoku/content/contents/002201639.pdf], 국외 소개 시 상대국 법령 준수 [https://jinjibu.jp/qa/detl/75624/1/]; 出入国管理法 技人国 요건 [https://www.moj.go.jp/isa/applications/resources/nyukan_nyukan69.html]; 한국 직업안정법 국외 유료직업소개 등록(자본금 5천만 원, 소개요금 3개월 임금의 33% 이내) [https://www.gov.kr/mw/AA020InfoCappView.do?CappBizCD=14900000005].

### 후보 E. 宅建업자 대상 "외국인 특화" AI 에이전트 SaaS (다언어 重説 보조·계약 검토·외국인 AI 심사·대응 챗)

1. **아이디어 한 줄**: 외국인 임차인 거래에 특화한 "다언어 重説·계약 보조 + 외국인 대응 AI 챗 + 외국인 심사 스코어"를 宅建업자·관리회사에 SaaS로 제공(宅建士의 설명 의무는 유지, AI는 초안·번역·이력 관리).
2. **타겟**: 宅建業者 132,291사(2025-03 말, 11년 연속 증가, +1,708사; 大臣면허 3,158·知事면허 129,133) [https://www.mlit.go.jp/report/press/tochi_fudousan_kensetsugyo16_hh_000001_00105.html]; 그중 도쿄 등 대도시 임대 중개·관리회사. 최종 수요: 재류외국인 4,125,395명(2025년 말) [https://www.nippon.com/ja/news/kd1410172998839256010/].
3. **근거 수치**: 전자계약 — 임대관리회사 도입 13.7%(이용자 76.3%가 희망, いえらぶ 2023) [https://www.itmedia.co.jp/business/articles/2305/18/news175.html]; 2024-05 賃貸管理業 63.5%·売買仲介 29.2% 이용 [https://prtimes.jp/main/html/rd/p/000000598.000008550.html]; 2025-05 엔드유저 이용 경험 26.8%, 부동산회사 약 4割 [https://presscarry.com/archives/119499]; 기업 도입 18.74% 언급 [https://www.ielove-group.jp/news/detail-835](원문 재확인 요); ITANDI 賃貸管理 전자계약 2025년도 43만 건 [https://corp.itandi.co.jp/news_posts/260416]. IT重説 이용 19.5%(2024-07)→24.0%(2025-01), 소비자 51.5% "써보고 싶다" [https://housecom-fc.jp/20251007-3/]("30~40%" 수치 **미확인**). 외국인 입주 거절 — 法務省 조사 39.3%가 외국인 이유로 거절, 41.2% 보증인 부재 거절, 26.8% "외국인 불가" 표시로 포기 [https://www.nikkei.com/article/DGXLASDG31H0D_V00C17A4CR0000/], [https://www.moj.go.jp/isa/content/001342229.pdf]; YOLO JAPAN 조사 2명 중 1명 거절 경험 [https://prtimes.jp/main/html/rd/p/000000080.000015950.html]. 부동산테크 시장(矢野) 2022년도 9,402억 엔(+21.1%), 2030년도 2조 3,780억 엔 [https://www.yano.co.jp/press-release/show/press_id/3551]. 카오스맵 제11판(2025-08) 528 서비스, 生成AI 분야 전년비 116% 증가 [https://prtimes.jp/main/html/rd/p/000000065.000038545.html]. 부동산회사 生成AI 업무 이용 41.4%, AI 에이전트 이용 12.7%, 향후 의향 71.6%(いえらぶ 2025-06) [https://www.ielove-group.jp/news/detail-1128]; "AI 관심 없음" 약 4割(アルサーガ 2025-10) [https://www.arsaga.jp/news/pressrelease-generative-ai-survey-real-estate-20251023/]. 重説 작성 공수 임대 240분·매매 300분 → AI 10분·30분(2차) [https://www.aidma-hd.jp/ai/ai-important-theory/].
4. **존재 검증**:
   - 重説 AI 생성: Ai-Smart重説(Paradis) [https://ai-zyusetu.com/]; smooos(MeSHLIFE, 공수 91% 절감) [https://prtimes.jp/main/html/rd/p/000000004.000114932.html]; AI重説 툴 8선 [https://www.aidma-hd.jp/ai/ai-important-theory/]; ITANDI 賃貸仲介 AI帳票生成(2025-08-20) [https://service.itandi.co.jp/news/250820]
   - 접객·에이전트 AI: いえらぶ AIエージェント [https://www.ielove-group.jp/news/detail-1287], いえらぶBB AI챗봇 [https://www.ielove-group.jp/news/detail-1198]; LIFULL AI 통합 에이전트 [https://lifull.com/news/45744/], 住宅AIコンシェルジュ(2025-10-06) [https://www.homes.co.jp/cont/press/release/atpress/atpress_01722/]; RENOSY [https://www.renosy.com/]; スマサテ AI 임대료 사정 [https://prtimes.jp/main/html/rd/p/000000023.000017292.html]
   - 계약서 AI 리뷰: LegalOn(유료 도입 9,000사 초과, 2026-07) [https://legalontech.jp/10931/]; GVA TECH [https://boxil.jp/mag/a7191/]
   - 외국인 대응·다언어: GTN 25언어 AI+유인 챗, ChatGPT 연계 β [https://www.gtn.co.jp/news/20230410], BEST-ESTATE.JP 앱 리뉴얼(2025-10) [https://www.gtn.co.jp/news/20251029]; ランゲージワン 12개국어 전화통역 [https://www.languageone.qac.jp/real-estate/]; 国交省 외국인 입주 가이드라인·重説·표준계약서 14언어 견본 [https://www.zennichi.or.jp/2019/11/25/191125/]; 개인 宅建士 영어 重説 대행 [https://www.lancers.jp/menu/detail/1241581]; YOLO HOME [https://www.yolo-japan.co.jp/]; ベストランド **미확인**
   - **판정: 重説 AI 생성·계약 리뷰·접객 AI는 "이미 존재". "외국인 특화 다언어 AI 重説 보조 + 외국인 임차인 AI 심사 + 다언어 계약 후 대응"을 묶은 宅建업자용 SaaS는 검색상 없음(통역 전화·유인 챗·PDF 견본 수준) → 니치 "부분 존재(공백)".**
5. **성장성·미래가치**: 전자계약·IT重説 침투 20~40%대로 전환 여지 큼; 生成AI 카테고리가 카오스맵 최고 성장(116%); 외국인 거절률 4~5割은 "심사 근거 부재"가 원인의 일부 → AI 심사+보증을 붙이면 관리회사·오너 수용률 개선 논리 성립. 대형(いえらぶ·ITANDI·LIFULL)이 범용 AI를 내장 → 범용 경쟁은 불리, 외국인 세그먼트 데이터 우위로만 방어.
6. **당사 자산 연결**: 외국인 입주 심사 데이터+보증 실적 → "외국인 심사 스코어" API(후보 H와 결합); 서울 민박 게스트 데이터로 한국인 임차인 세그먼트 우위; 宅建업 면허·宅建士로 자사 거래에 먼저 적용해 레퍼런스 확보.
7. **규제 리스크**: 宅建業法 35条(重説은 宅建士 독점, AI 완전 대행 불가), 37条 서면, IT重説 운용 규칙, 2022-05 전자교부 해금 [https://housecom-fc.jp/20251007-3/]; 번역본 사용 시 国交省 다언어 표준계약서와의 정합성·오역 책임 [https://classlab.co.jp/services/ai-solution/ai-column/fudosan-gaikokujin-ai-taiou]; 個人情報保護法(재류카드·여권), AI推進法 7조 활용사업자 책무 [https://www.businesslawyers.jp/articles/1475]; 심사 AI의 국적 기반 차별 금지(法務省 가이드라인 취지) [https://www.moj.go.jp/isa/content/001342229.pdf].

### 후보 F. 민박·호텔 무인 운영 AI — 2026 観光庁 "ICT 관리 의무" 컴플라이언스 패키지

1. **아이디어 한 줄**: 2026-07 観光庁 통지로 조례화될 "ICT 관리 의무"(소음계·출입구 카메라·모니터링·데이터 보존)와 旅館業法 ICT 본인확인을 한 번에 충족하는 컴플라이언스형 AI 운영 패키지(다국어 AI 컨시어지+본인확인+소음/클레임 자동 대응+자치체 보고).
2. **타겟**: 일본 民泊 届出住宅 42,070건(2026-07-15, 누계 届出 65,837·폐지 23,767) [https://www.mlit.go.jp/kankocho/minpaku/business/host/construction_situation.html]; 2026-01-15 시점 38,112건 [https://www.mlit.go.jp/kankocho/minpaku/business/host/content/001992627.pdf]; 住宅宿泊管理業者·운영대행사·소규모 호텔. 한국: 도시민박업 누적 등록 8,534명, 영업중 6,134명(2025-06-20), 2024 신규 2,323명(전년 2.6배), 서울 3,869명(63.1%), 마포구 1,293명 [https://www.wehome.me/trust/ko/report-urbanstay-202506/].
3. **근거 수치**: 観光庁·国交省·厚労省 연명 2026-07-15 「住宅宿泊事業法に規定する届出住宅に係るゼロ日規制等について（技術的助言）」— 조례로 신규 민박 금지·영업일수 제한(제로일 규제) 가능 명확화, ICT 관리(소음계·출입구 카메라, 모니터링, 데이터 보존) 조례 의무화 가능 [https://www.mlit.go.jp/kankocho/news06_00067.html], [https://www.travelvoice.jp/20260715-160180]; 観光庁 "ICTによる管理に関する説明会" 설명 기업 모집(2026) [https://www.mlit.go.jp/kankocho/topics06_00065.html]; 업계 반응 [https://sharing-economy.jp/ja/20260717/]; 旅館業 2025-04-01 「衛生等管理要領」 개정 — ICT 본인확인(얼굴·여권 영상 대조·녹화), 프론트 불설치 4조건 [https://luxent.jp/permit/3339/], [https://minpakugakko.com/ryokangyo-front-ict-r7-2026/]; 인력부족(帝国データバンク) 旅館・ホテル 정사원 60.2%·비정사원 59.6%(2025-01) [https://prtimes.jp/main/html/rd/p/000000712.000043465.html], 2025-10 비정사원 부족 59.0%로 전 업종 최고 [https://www.tdb.co.jp/report/economic/20251117-laborshortage202510/]; 한국 에어비앤비 2025-10-16 영업신고 의무화, 미제출 숙소 2026-01-01 이후 예약 차단 [https://zdnet.co.kr/view/?no=20250819084652], [https://www.thepublic.kr/news/articleView.html?idxno=273506]; 국내 7만+ 중 약 3만(40%+) 미신고 추정(2차) [https://host.enko.kr/blog/airbnb-illegal-accommodation-crackdown].
4. **존재 검증**:
   - tripla Bot(8언어, 2026-09-17 生成AI 탑재, 마이스테이즈 150시설) [https://tripla.io/2026/09/17/tripla-bot_update/], [https://tripla.io/2025/04/10/mystays-2/]
   - AirHost AI 게스트 어시스턴트(tripla Book 연계 2025-01) [https://airhost.jp/ai-assistant], [https://www.travelvoice.jp/20250114-157008]
   - matsuri technologies 약 4,000실 운영(2025-12) [https://speakerdeck.com/matsuritechnologies/matsuri-technologieszhu-shi-hui-she-hui-she-shao-jie-zi-liao-2024]
   - Bebot(Bespoke) [https://service.honichi.com/services/bespoke-bebot]
   - minpakuIN(영상 본인확인·스마트락 연동) [https://renoful.jp/minpakuin/]; Keycafe×minpakuIN [https://prtimes.jp/main/html/rd/p/000000011.000030273.html]; Keycafe는 Airbnb·AirHost·HotelSmart·Suitebook 연동 [https://bitdays.jp/real_estate/31638/]
   - HOTEL SMART(셀프체크인 4,500시설) [https://www.hotelsmart.jp/id-checkin/737/]
   - AssistBnB メッセージAI(2026-06-29, 월 8,000엔/물건~) [https://prtimes.jp/main/html/rd/p/000000004.000166439.html], MOSVA 民泊おもてなしAI 15언어 [https://ai.mosva.jp/]; Kotozna In-room 450시설 [https://value-works.jp/column/kotozna/]
   - 한국: 온다 ONDA(2025-10 시리즈B 브릿지 75억 원) [https://wowtale.net/2025/10/28/249337/], [https://zdnet.co.kr/view/?no=20251118161811]; 야놀자 Y FLUX [https://www.yanoljalab.com/yflux.php]; 온다 일본 진출 여부 **미확인**; Beds24·Squarehotel **미확인**
   - **판정: AI 컨시어지·셀프체크인·메시지 AI는 "이미 존재"(5+). 2026-07 통지 기반 "조례별 ICT 관리 의무(소음·카메라·데이터 보존·자치체 보고) + 본인확인 + AI 응대"를 규제 준수 패키지로 통합한 사업자는 통지 직후라 검색상 없음 → "부분 존재(초기 공백)".**
5. **성장성·미래가치**: 규제가 수요를 만드는 구조 — 자치체 조례 제정 사이클(2026 하반기~2027)에 맞춰 "설치+모니터링+보고" 의무 발생; 폐지율 36%(23,767/65,837)의 시장에서 살아남는 사업자는 컴플라이언스 투자가 가능한 관리업자·법인; 한국도 2026-01 미신고 퇴출로 합법 민박 고도화 수요. 리스크: 조례가 자치체별로 달라 표준화 어려움; 기존 PMS(AirHost·matsuri)가 기능 추가로 흡수 가능.
6. **당사 자산 연결**: 서울 도시민박 운영 경험·게스트 데이터로 한·영·일 응대 코퍼스; 도쿄 먼슬리에 동일 스택 적용(중장기 체류 본인확인·클레임); 관광진흥법 도시민박업과 住宅宿泊事業法 양쪽 규제에 동시 대응 가능한 소수 사업자.
7. **규제 리스크**: 住宅宿泊事業法(届出·180일 상한·관리업 위탁), 2026-07-15 技術的助言에 따른 자치체 조례 [https://www.mlit.go.jp/kankocho/news06_00067.html]; 旅館業法·衛生等管理要領(ICT 본인확인, 외국인 여권 사본 보존) [https://luxent.jp/permit/3339/]; 個人情報保護法(카메라 영상·여권 데이터), 소음계 데이터 프라이버시; 한국 관광진흥법 시행령(오피스텔 불가) [https://kbizon.com/%EC%99%B8%EA%B5%AD%EC%9D%B8%EA%B4%80%EA%B4%91-%EB%8F%84%EC%8B%9C%EB%AF%BC%EB%B0%95%EC%97%85/].

### 후보 G. 일본 고령 個人大家 대상 AI 임대관리 자동화 (공실·수리·외국인 입주 판단·상속)

1. **아이디어 한 줄**: 고령 개인 오너(또는 그 관리회사)에게 공실 AI 예측·외국인 임차인 AI 심사+보증·다언어 입주자 응대·수리 발주·상속 대비 자산 정리를 자동화하는 AI 관리 에이전트.
2. **타겟**: 민간 임대주택의 8割 이상이 개인 경영, 그중 6割이 60세 이상(国交省 平成22년) [https://www.mlit.go.jp/common/001017688.pdf]; 家主 앙케이트(2019) 60세 이상 34.3%로 최다 [https://www.mlit.go.jp/common/001320849.pdf]; 2026년판 오너 연령 60대 29.68%·70대 11.47%·80대 4.71%(2차) [https://uchicomi.com/uchicomi-times/category/investment/main/15342/]; 個人大家 수 — 不動産所得 신고자 약 224만 명(연도 **미확인**, 2차) [https://www.home4u.jp/lease/contents/manage/lease-65-49058/]; 관리 위탁 약 8割, 완전 자주관리 약 2割(国交省 2019) [https://www.mlit.go.jp/report/press/totikensangyo16_hh_000198.html].
3. **근거 수치**: 空き家 900만 호, 공가율 13.8%(2023 住宅・土地統計調査) [https://www.stat.go.jp/data/jyutaku/2023/pdf/g_kekka.pdf]; 그중 임대용 443.6만 호(49.3%) [https://www.zenchin.com/news/content-3050.php]; 고령자 입주 거부 오너 약 4割, 7割은 지원 있으면 검토(R65) [https://prtimes.jp/main/html/rd/p/000000026.000068855.html]; 외국인 거절 39.3% [https://www.nikkei.com/article/DGXLASDG31H0D_V00C17A4CR0000/]; 令和6년도 賃貸住宅管理業 조사 [https://www.mlit.go.jp/tochi_fudousan_kensetsugyo/const/tochi_fudousan_kensetsugyo_const_tk3_000001_00087.html](세부 **미확인**).
4. **존재 검증**:
   - ヤモリ(시리즈A 10억 엔 2024-02, 등록자산 1,000억 엔·이용자 5,000명) [https://thebridge.jp/2024/02/yamori-series-a-round-funding]
   - GMO賃貸DX 오너앱(AI 회신·102언어 번역) [https://chintaidx.com/owner/]
   - 家主ダイレクト(Casa, 자주관리 오너용 보증+집금, 누계 10만 건) [https://casa-yd.jp/o01/], [https://prtimes.jp/main/html/rd/p/000000074.000020482.html]
   - オーナーズエージェント(관리회사 지원 800사) [https://owners-age.com/]
   - スマサテ for Owners [https://prtimes.jp/main/html/rd/p/000000023.000017292.html]; 日本情報クリエイト オーナー提案AIロボⅡ [https://www.n-create.co.jp/pr/product/kushitsu_robo/]; TERASS AI賃貸管理 [https://lp.terass.com/partners_1/]; フドカン [https://fudokan.net/blog/column/detail/20240319083856/]
   - 상속: オーナーズ・スタイル 大家さんフェスタ [https://owners-style.net/s/festa/]; 大家DX·いえらぶBB 오너 기능 **미확인**
   - **판정: 오너 수지관리·보증·오너앱·AI 사정은 "이미 존재". "고령 오너 × 외국인 입주 AI 판단·보증 × 다언어 응대 × 상속" 결합은 없음 → "부분 존재". 단, 오너의 8割이 관리회사 위탁·고령층 디지털 접근성 낮음 → D2C는 채널 리스크, 관리회사 경유 B2B2C 또는 마스터리스형이 현실적.**
5. **성장성·미래가치**: 임대용 공가 443만 호+오너 고령화+외국인 입주 수요 증가의 교차점; 공가 해소 수단으로 외국인·먼슬리 전환이 유효하고 당사 보증이 오너 리스크 인식을 낮춤; 大相続時代의 자산 데이터화 수요 [https://kabutan.jp/news/marketnews/?b=n202501270926].
6. **당사 자산 연결**: 공실 물건을 당사 먼슬리 채널(외국인·비즈니스 여행자)로 채우는 "AI 심사+보증+(선별적)전대" 제안이 고령 오너에게 가장 직접적 가치; 宅建업 면허로 서브리스/중개 가능; 다언어 응대는 후보 F 스택 재활용.
7. **규제 리스크**: 賃貸住宅管理業法(200호 이상 등록, 업무관리자), 서브리스 규제(특정전대 중요사항 설명·권유 규제); 宅建業法; 借地借家法(정기차가·전대 승낙); 家賃債務保証業者 등록; 상속은 弁護士法 72条·税理士法 → 제휴 필수; 외국인 입주 판단 AI의 국적 차별 금지 [https://www.moj.go.jp/isa/content/001342229.pdf].
### 후보 H. 한일 크로스보더 "임차인 신용 패스포트" + 외국인 보증 AI 언더라이팅 API (B2B)

1. **아이디어 한 줄**: 당사 민박·먼슬리에서 쌓이는 외국인 게스트의 결제·거주·퇴거 이력을 한·일 양국에서 통용되는 "임차인 신용 패스포트"로 만들고, 일본 家賃保証会社·管理会社와 한국 임대인·보증사에 AI 심사 API로 제공한다(Nova Credit의 주거·한일판).
2. **타겟**: (일본) 家賃保証会社·管理会社 — 외국인 계약 연 10만 건을 처리하는 GTN 같은 전업사 [https://www.gtn.co.jp/business/realestate/rent-guarantor/agency], Credit Saison 외국인 보증(전국 10개 부동산사 경유) [https://www.relonetworkasia.com/blog/credit-saison-introduces-rental-guarantees-to-simplify-housing-for-foreign-residents-in-japan/]; 최종 수요자는 재일 한국인 407,341명 [https://www.nippon.com/ja/news/kd1410172998839256010/] 및 技術・人文知識・国際業務 475,790명 [동상]. (한국) 등록외국인 163.7만 명(2026-06) [https://www.moj.go.kr/bbs/immigration/227/608714/artclView.do]과 이들을 받는 임대인.
3. **근거 수치**: 일본 家賃債務保証 시장 FY2024 2,548.57억 엔(+6.7%), FY2025 예측 2,723.9억 엔(+6.9%), FY2029 3,500억 엔 초과 전망 [https://www.tokyo-takken.or.jp/re-port/78927], [https://www.yano.co.jp/market_reports/C67106400]; 보증회사 이용률 80%(国交省 FY2021) [https://www.mlit.go.jp/common/001153371.pdf]; 외국인의 39.8~40%가 입주 거절 경험 [https://www.jinzaiplus.jp/posts/172], [https://suumo.jp/journal/2025/12/25/214133/]; 외국인 입주자 트러블률은 1.5% 수준이라는 조사 [https://suumo.jp/journal/2025/12/25/214133/]; 全保連은 AI 심사로 심사시간 약 2시간 단축·연 6억 엔 절감 [https://www.nikkei.com/article/DGXZQOJC088VJ0Y3A201C2000000/]; 재일외국인 4,125,395명(+9.5%, 2025 말) [https://www.nippon.com/ja/news/kd1410172998839256010/]; 한국 체류외국인 2,874,278명(2026-06) [https://www.moj.go.kr/bbs/immigration/227/608714/artclView.do].
4. **존재 검증**:
   - Nova Credit(미국) — Credit Passport, 한국 신용정보를 미국식 리포트로 변환. 일본은 지원국 아님. 2025-10 시리즈D 3,500만 달러 [https://www.novacredit.com/credit-passport], [https://www.firstcard.app/learn/nova-credit-review-for-immigrants-2026] → 글로벌 유사모델, 한일 미커버.
   - GTN(일본) — 외국인 전문 家賃保証, 연 약 10만 명 보증 [https://www.gtn.co.jp/] → 보증사이지 크로스보더 신용 데이터 사업자 아님.
   - Credit Saison 외국인 보증 [https://www.relonetworkasia.com/blog/credit-saison-introduces-rental-guarantees-to-simplify-housing-for-foreign-residents-in-japan/].
   - 全保連 AI 심사 [https://www.nikkei.com/article/DGXZQOJC088VJ0Y3A201C2000000/], アールエムトラスト 40만 건 데이터 기반 5분 AI 심사 [https://www.value-press.com/pressrelease/340405] → 내국인 중심 AI 심사.
   - 크레파스플러스(한국) — 통신·스마트폰 데이터 기반 외국인 전용 신용평가모델, 외국인 금융 플랫폼 '원풀' [https://www.unicornfactory.co.kr/article/2025042309420624489] → 금융 대출용, 주거 보증 미포함.
   - 판정: **부분 존재**(각국 내 외국인 보증·AI 심사는 있으나 한↔일 이력 이전형 주거 신용 데이터는 없음). 아시아 크로스보더 임차인 신용 패스포트 스타트업은 검색상 확인 안 됨(**미확인**).
5. **성장성·미래가치**: 재일외국인 +9.5%/년, 한국 체류외국인 +5%/년으로 양국 모두 외국인 임차 수요가 구조적으로 증가하며, 일본 보증 시장은 연 7% 성장 중. 보증사는 "외국인 데이터 부족"으로 보수적 심사(월세의 50~120% 보증료 [https://koreajapanlife.com/entry/japan-rent-guarantor-company-ko])를 하므로 검증된 이력 데이터의 가격 결정력이 크다. 당사 본업(AI 언더라이팅+보증)의 손실률 데이터가 그대로 상품이 된다.
6. **당사 자산 연결**: 한국 민박(Stay)→먼슬리(Bridge)→일본 먼슬리로 이어지는 동일 고객의 결제·거주 이력을 이미 보유 예정; 일본 법인·宅建 면허로 보증사·관리회사와 B2B 계약 가능; AI/개발 역량으로 스코어링 API 구축; 한국 채널로 방일 한국인(워홀 상한 1만 명/년 [https://www.kr.emb-japan.go.kr/itpr_ko/visa_working.html], 재일 한국인 40.7만) 확보.
7. **규제 리스크**: 일본 個人情報保護法(제3자 제공 동의·越境移転 규제), 家賃債務保証業者 登録制度(国交省); 한국 개인정보보호법(국외이전 동의·가명정보 범위), 신용정보법(신용정보업 허가 없이 "신용정보" 수집·제공 시 위법 소지 → 본인 동의 기반 "거주 이력 증명" 형태로 설계 필요, 변호사 검토 필수); 보증업을 직접 하면 한국 보험업법·일본 보증업 규제.

### 후보 I. 외국인 게스트 행동 데이터 기반 인바운드 마케팅·상권 데이터 사업

1. **아이디어 한 줄**: 민박·먼슬리 게스트(동의 기반)의 체류 목적·기간·소비·이동 데이터를 가명화해 한일 지자체·DMO·소매·뷰티 브랜드에 "장기체류 외국인 패널 데이터"로 판매·리포트화.
2. **타겟**: 일본 DMO·지자체(観光庁 DMO 데이터 활용 모델 실증사업 공모 [https://www.mlit.go.jp/kankocho/kobo04_00032.html]), 인바운드 마케팅 대행사, K-beauty·J-beauty 브랜드; 한국 지자체·관광공사.
3. **근거 수치**: 2025 방일 외국인 4,268만 명·소비 9조 4,559억 엔(+16.4%), 1인당 22.9만 엔, 쇼핑 2조 5,490억 엔(27%) [https://www.mlit.go.jp/kankocho/news02_00071.html], [https://yamatogokoro.jp/inbound_data/59160/]; 観光庁 2026년도 예산 1,383억 엔(전년 2.4배, 出国税 3,000엔 인상 재원) [https://yamatogokoro.jp/column/kaisetsu/59024/], [https://www.travelvoice.jp/20251227-159013]; 방한 외래객 2025 1,894만 명 [https://yamatogokoro.jp/inbound_data/59369/]; 방일 후 越境EC 리피트 구매 경험 44.0%(+8.6p) [https://ecclab.empowershop.co.jp/archives/67438].
4. **존재 검증**:
   - ゼンリンデータコム 인바운드 위치정보 분석 [https://www.zenrin-datacom.net/solution/bigdata/inbound]
   - NAVITIME 인바운드 GPS 데이터 [https://data.navitime.co.jp/menu/inbound/]
   - Location AI「インバウンドアナリティクス+」[https://prtimes.jp/main/html/rd/p/000000133.000037476.html]
   - 大阪観光局 DMP [https://www.jtbbwt.com/government/trend/detail/id=1903]
   - BC카드 데이터비즈니스·신한카드 DataBada·한국관광 데이터랩 [https://www.bccard.com/card/html/company/kr/bigdata/business/index.jsp], [https://databada.shinhancard.com/], [https://datalab.visitkorea.or.kr/]
   - 판정: **이미 존재**(단기 관광객 위치·카드 데이터). 다만 "30일 이상 장기체류 외국인의 생활 소비 패널"은 카드·GPS 데이터로 분리 불가하므로 니치 공백은 남음.
5. **성장성**: 인바운드 예산·소비가 매년 최고치이나, 대형 데이터 보유자(통신·카드·지도)가 이미 시장을 점유. 당사 표본은 수백~수천 명 규모라 통계적 가치가 낮고, 매출 규모가 작다(리포트 판매 수준).
6. **당사 자산 연결**: 게스트 국적·체류목적·기간 데이터, 한·일 양국 표본. 그러나 데이터 판매보다 자사 언더라이팅·상품 추천에 내부 활용하는 편이 가치가 크다.
7. **규제 리스크**: 일본 旅館業法·住宅宿泊事業法 상 숙박자명부 정보의 마케팅 목적 2차 이용 금지, 개인정보보호법 이중 규제(법인 최대 1억 엔 벌금) [https://miyako.com/lab/houritsu/kojinjouhouhou-shukuhaku-daichou/]; 한국 개인정보보호법 가명정보는 통계·연구 목적만 동의 없이 가능 [https://www.law.go.kr/lsEfInfoP.do?lsiSeq=195062] → 별도 명시 동의·옵트인 설계 필수.

### 후보 J. AI 통역 하드웨어·서비스 for 민박 체크인·응대

1. **아이디어 한 줄**: 민박·소규모 숙소용 다국어 AI 통역·체크인 단말/앱(여권 확인+숙박자명부+AI 응대).
2. **타겟**: 일본 民泊 사업자, 한국 도시민박 호스트 6,134명(영업 중, 서울 3,869) [https://www.wehome.me/trust/ko/report-urbanstay-202506/].
3. **근거 수치**: 방일 4,268만 명·숙박비 3조 4,617억 엔(36.6%) [https://digirise.ai/chaen-ai-lab/hotel-genai-guide/]; 2026-07-15 観光庁 기술적 조언으로 조례에 의한 ICT 관리(소음계·출입구 카메라·기록 보존) 의무화 가능 [https://www.mlit.go.jp/kankocho/news06_00067.html], [https://www.travelvoice.jp/20260715-160180]; 2025-10 문체부 지침으로 한국 도시민박 통역앱 등 보조수단 허용 [https://www.korea.kr/news/policyNewsView.do?newsId=148950951].
4. **존재 검증**:
   - POCKETALK(92개 언어, 법인 플랜) [https://pocketalk.jp/business]
   - Kotozna In-room(109개 언어, 450개 이상 시설) [https://www.kotozna.com/ja/in-room], [https://value-works.jp/column/kotozna/]
   - アビAiコンシェルジュ(숙박시설 다언어 브라우저 툴 도입 1위) [https://www.ab-net.co.jp/dx/abi-concierge/]
   - AssistBnB 메시지AI(2026-06, 전 언어 24시간 자동응답) [https://oproduct.ai/articles/8673232]
   - 東急 TsugiTsugi ChatGPT 컨시어지 [https://digirise.ai/chaen-ai-lab/hotel-genai-guide/]
   - 판정: **이미 존재**(5개 이상 직접 플레이어).
5. **성장성**: 시장은 크지만 범용 LLM 번역이 상품화되어 단가 하락 중. 하드웨어는 자본 집약적.
6. **당사 자산**: 자사 민박 운영 노하우는 있으나 차별 요소 없음.
7. **규제**: 旅館業法 숙박자명부·여권 사본 보존, 개인정보보호법. → **제외 권고**(후보 F의 "ICT 관리 의무 대응 패키지"에 흡수).

### 후보 K. AI 다국어 임대차 분쟁 조정·원상회복 판정 서비스 (한·일)

1. **아이디어 한 줄**: 외국인 임차인–임대인 간 퇴거 정산·원상회복·보증금 분쟁을 国交省 가이드라인·판례·한국 주임법 기준으로 AI가 다국어로 사전 판정·중재안 제시(ODR), 당사 먼슬리 계약에는 기본 탑재.
2. **타겟**: 일본 재류외국인 412만 명·한국 체류외국인 287만 명 중 임차인, 외국인 입주를 받는 임대인·관리회사, ODR 인증 사업자.
3. **근거 수치**: 일본 원상회복 트러블은 国民生活センター 상담 상위 항목 [https://www.kokusen.go.jp/soudan_topics/data/chintai.html]; 외국인 입주 트러블률 1.5% [https://suumo.jp/journal/2025/12/25/214133/]; 법무성 かいけつサポート ODR 인증 사업자 2025년에도 복수 추가 [https://www.adr.go.jp/]; 한국 임대차분쟁조정위원회 실적 공개 [https://adrhome.reb.or.kr/adrhome/reb/openData/openData.do?Key=10508000000002022101900] — 외국인 접수 건수 **미확인**.
4. **존재 검증**:
   - Send Legal — AI 원상회복 논점정리(개발 중, April Dream) [https://prtimes.jp/main/html/rd/p/000000007.000114321.html]
   - 국토교통성 가이드라인 기반 Dify 챗봇(개인 제작) [https://zenn.dev/yonamine/articles/58d9fa7d3d9680]
   - 退去精算シミュレーター(宅建AI) [https://www.takkenai.jp/tools/taikyo-seisan/]
   - いえらぶ安心保証 11개 언어 통역(3자 통화) [https://ielove-partners.co.jp/media/10758/], ブリッジライフ 8개 언어 콜센터 [https://bridgelife-japan.com/business/business-05/]
   - 판정: **부분 존재**(일본어 단일·계산기 수준. 다국어 AI 판정+ODR 결합은 확인 안 됨).
5. **성장성**: 외국인 임차 증가와 함께 분쟁 건수 증가 논리는 타당하나, 분쟁은 계약당 저빈도 사건이라 독립 매출원으로는 작다. 가치는 "보증 손실률 저감"과 "임대인 설득 도구"로 본업 해자에 붙을 때 발생.
6. **당사 자산**: 자사 먼슬리 계약(한·영·일 표준계약서), 보증 손실 데이터, AI 역량. 자사 계약에 먼저 탑재 → 관리회사 B2B로 확장.
7. **규제**: 일본 弁護士法 제72조(비변호사의 법률사무 취급 금지, 보수 받는 분쟁 개입 시 위반 소지 → 정보 제공·시뮬레이션에 한정하거나 ODR 인증 취득), 한국 변호사법 제109조 동일 취지. 판정 결과의 법적 효력 없음 명시 필요.

### 후보 L. 한국 미용클리닉 일본 진출 MSO + 의료진·스태프 랜딩(주거·비자) 패키지

1. **아이디어 한 줄**: 도쿄 진출하는 한국 피부과·성형외과에 개원 MSO(입지·의료법인 M&A·인허가 코디)와 파견 의료진·코디네이터의 주거(먼슬리)·비자·정착을 번들로 제공.
2. **타겟**: 일본 진출 한국 미용클리닉(2025~26 긴자·신주쿠·신오쿠보에 개원 러시) 및 그 파견 인력.
3. **근거 수치**: 일본 美容医療 시장 2024년 6,310억 엔(+6.2%) [https://www.yakuji.co.jp/entry119850.html]; 한국 내 저가화·일본의 높은 시술 단가가 진출 동기 [https://biyouhifuko.com/news/column/17955/]; 스킨다피부과 긴자점 8월 개원 [https://mdtoday.co.kr/news/view/1065591060450648], 아이디병원 긴자 피부과 1호점 [https://www.idskin.co.kr/board/idnews/view/page/4/wid/44/bid/10978], 오가나셀 긴자원 [https://biyouhifuko.com/news/column/17955/], 오라클 신주쿠 [https://www.oracleclinic.jp/], V&S(벤스) 신주쿠 [https://japan.vandsclinic.co.kr/], 클리닉K 블로썸 신오쿠보 [https://clinickblossom.jp/]; 경営・管理 비자 2025-10-16부터 자본금 3,000만 엔+상근 1명 [https://www.sme-support.co.jp/column/p1303/] — 진출 의사·투자자의 비자 장벽 상승.
4. **존재 검증**:
   - カミーユ行政書士事務所 — 한국 의사·투자자 대상 일본 클리닉 개설·의료법인 M&A 가이드(한국어) [https://kamiyugyousei.com/korean-doctors-and-mso-corporations-open-clinics-in-japan/]
   - 개원 러시 자체가 다수 존재(위 6개 원). MSO 전문 사업자(한국계)는 검색상 소수(**미확인**).
   - 판정: **부분 존재**(행정서사·컨설팅은 있으나 "주거+비자+개원" 번들은 확인 안 됨).
5. **성장성**: 트렌드는 명확하나 진출 클리닉 수는 연 수십 개 수준으로 추정(**미확인**), TAM이 작다. 의료법인 지분 참여 불가(일본 医療法 비영리 원칙)로 MSO 수수료 모델에 한정.
6. **당사 자산**: 일본 법인·宅建(클리닉 입지 중개 가능)·먼슬리 재고·한국 채널(의료계 네트워크는 **미확인**).
7. **규제**: 일본 医療法(의료법인 이사장 의사 요건, 영리법인 개설 불가), 医師法(한국 의사 면허 일본 미인정 → 일본 의사 고용 필수), 医療広告ガイドライン, 経営・管理 비자 강화.

## 3. 검토 후 제외한 아이디어 (존재 검증만 기록)

- **외국인 정착 올인원 AI 앱(생활·행정·비자)**: Linc 생활지원 앱 개발에 3억 엔 조달(2025-07) [https://www.nikkei.com/article/DGXZQOUC22CJJ0S5A720C2000000/], Linc "Global Hub Talent" AI 재류신청서 자동작성(2026-01) [https://www.nikkei.com/article/DGXZQOUC222UB0S5A221C2000000/], NaviNichi.AI(2026-08) [https://companydata.tsujigawa.com/press-20260810-001/], EMYSTI 다문화공생 AI 플랫폼 [https://www.value-press.com/pressrelease/373344], GTN 컨시어지 [https://www.gtn.co.jp/business/realestate/gtn_concierge_service], 자치체 다언어 AI 챗(ObotAI 등) [https://obot-ai.com/function2/] → **이미 존재**. 비자 서류 자동화는 行政書士法 위반 소지도 있음.
- **AI 기반 재류자격 신청 SaaS**: 전문 SaaS는 검색상 미확인이나 Linc가 2026-01 출시 [https://www.nikkei.com/article/DGXZQOUC222UB0S5A221C2000000/]; 行政書士 독점 업무(申請取次) 경계 → 보류.
- **일본 기업 외국인 사원용 借り上げ社宅 B2B**: リロ·クロスハウス·マイナビBiz·GTN 法人 서비스 존재 [https://biz.mynavi.jp/lp_theme/global] → 후보 D의 판매 채널로만 활용.

---

## 4. 순위와 스코어링

채점: 각 항목 1~5점(5=최상). 화이트스페이스(경쟁 부재), 성장성(수치 근거), 적합성(당사 자산 결합), 실현성(1 dev·현 자본·12개월), 규제(5=장벽 낮음). 합계 25점 만점.

| 순위 | 후보 | 화이트스페이스 | 성장성 | 적합성 | 실현성 | 규제 | 합계 | 판정 근거 |
|---|---|---|---|---|---|---|---|---|
| **1** | **A. 일본인 미용의료 회복기 민박/먼슬리 + 일본어 사후관리** | 3 | 5 | 5 | 4 | 2 | **19** | 일본인 60만 환자·성형외과 42% [https://www.mohw.go.kr/board.es?mid=a10503010100&bid=0027&act=view&list_no=1490280]; 회복기 상품화 사업자 없음; 서울시 의료친화숙박 공모(2026-09) [https://www.rapportian.com/news/articleView.html?idxno=240266]; 유치업 등록·의료광고 규제가 감점 |
| **2** | **E. 宅建업자용 외국인 특화 AI SaaS(다언어 重説·외국인 심사 스코어)** | 4 | 4 | 5 | 3 | 3 | **19** | 宅建業者 13.2만 사 [https://www.mlit.go.jp/report/press/tochi_fudousan_kensetsugyo16_hh_000001_00105.html]; 生成AI 카테고리 +116% [https://prtimes.jp/main/html/rd/p/000000065.000038545.html]; 외국인 니치 통합 SaaS 없음; 대형 3사 범용 AI가 위협 |
| **3** | **H. 한일 임차인 신용 패스포트·외국인 보증 AI 언더라이팅 API** | 5 | 4 | 5 | 2 | 2 | **18** | 한일 이력 이전형 주거 신용 데이터 사업자 없음(Nova Credit도 일본 미커버) [https://www.novacredit.com/credit-passport]; 保証 시장 +7% [https://www.tokyo-takken.or.jp/re-port/78927]; 데이터 축적에 시간, 신용정보법·개인정보 국외이전이 장벽 |
| **4** | **F. 민박 ICT 관리 의무 컴플라이언스 AI 패키지** | 4 | 4 | 4 | 3 | 3 | **18** | 2026-07-15 통지 [https://www.mlit.go.jp/kankocho/news06_00067.html] 직후 통합 사업자 없음; 届出 42,070건 [https://www.mlit.go.jp/kankocho/minpaku/business/host/construction_situation.html]; 조례 파편화·PMS 흡수 리스크 |
| **5** | **D. 한국 개발자 일본 랜딩 패키지(채용+먼슬리+보증)** | 3 | 3 | 5 | 3 | 2 | **16** | IT 부족 79만 명 [https://www.nikkei.com/article/DGXZQOUC2425Y0U5A221C2000000/]이나 K-Move 일본 1,531명/년 [https://v.daum.net/v/20251104111647123]로 TAM 작음; 有料職業紹介·파견 허가 필요 |
| 6 | C. K-beauty 게스트 샘플링·패널 데이터 + AI 피부분석 | 3 | 4 | 4 | 2 | 3 | 16 | 한국코스메 일본 시장 +23.1% [https://www.dreamnews.jp/press/0000348216]; 패널 규모·단가 문제 → A의 부가 기능으로 흡수 |
| 7 | G. 고령 個人大家 AI 임대관리(외국인 입주·상속) | 3 | 3 | 4 | 2 | 3 | 15 | 임대용 공가 443.6만 호 [https://www.zenchin.com/news/content-3050.php]; 오너 8割 위탁·고령 채널 난이도 → 관리회사 B2B2C로 E에 흡수 |
| 8 | K. AI 다국어 임대차 분쟁·원상회복 판정(ODR) | 3 | 2 | 3 | 3 | 2 | 13 | 다국어 AI 판정+ODR 결합 없음이나 저빈도·弁護士法 72条 → 자사 계약 기능으로 |
| 8 | L. 한국 클리닉 일본 진출 MSO + 의료진 랜딩 | 3 | 3 | 3 | 2 | 2 | 13 | 긴자·신주쿠 개원 러시 [https://biyouhifuko.com/news/column/17955/]이나 연 수십 건 규모, 医療法·経営管理 비자 3,000만 엔 |
| 10 | B. 한국인 대상 일본 의료(재생의료·검진·치과)+먼슬리 | 2 | 3 | 3 | 2 | 2 | 12 | 일본 의료 인바운드 2~3만 명 [https://mediphone.jp/medico-plus/mt_current_situation/], 미용 수요 근거 없음 |
| 11 | J. AI 통역 체크인 단말·서비스 | 1 | 3 | 2 | 2 | 3 | 11 | Kotozna 450시설 등 5개 이상 존재 → F에 흡수 |
| 12 | I. 외국인 게스트 데이터 인바운드 마케팅 데이터 판매 | 2 | 3 | 2 | 2 | 1 | 10 | ゼンリン·NAVITIME·카드사 선점, 숙박자명부 2차 이용 금지 [https://miyako.com/lab/houritsu/kojinjouhouhou-shukuhaku-daichou/] |

### 상위 5개 실행 제안 (12개월)

1. **A(0~3개월)**: 서울시 '의료친화 숙박시설' 공모(2026-09-14~30) 응모 [https://www.rapportian.com/news/articleView.html?idxno=240266]; 강남 성형외과 2~3곳과 회복기 스테이 제휴(방문간호는 외부 연계); 외국인환자 유치업 등록 요건(자본금 1억 원 또는 종합여행업+5천만 원) [https://news.seoul.go.kr/welfare/archives/531323] 검토 후 등록 여부 결정 — 등록 전에는 병원 직접 알선·수수료 수취 금지; 도쿄 법인에서 귀국 후 LINE 사후관리·제휴 클리닉 경과 상담 채널 운영.
2. **E+H(3~9개월)**: 자사 도쿄 먼슬리 거래에 "외국인 심사 스코어+다언어 重説 보조"를 먼저 적용해 손실률·승인률 레퍼런스 확보 → 관리회사 3곳 파일럿 → 家賃保証会社(GTN·Credit Saison 등)에 스코어 API 제안. 한국 민박 게스트 이력을 동의 기반으로 연결(신용정보법·개인정보 국외이전 변호사 검토 선행).
3. **F(6~12개월)**: 観光庁 ICT 관리 설명회 [https://www.mlit.go.jp/kankocho/topics06_00065.html] 참여, 도쿄 23구 조례 동향 추적; 자사 민박·먼슬리에 소음계·출입 카메라·AI 응대·보고 대시보드를 먼저 설치해 "조례 준수 레퍼런스"를 만든 뒤 관리업자에 판매(기존 PMS와는 연동, 대체 아님).
4. **D(수시)**: KOTRA 일본 잡페어 참가 기업 [https://www.sedaily.com/NewsView/2H0EF1N0QE]에 "입국 전 계약 먼슬리+보증" B2B 상품을 제안. 有料職業紹介 허가 없이 시작하려면 알선 수수료를 받지 않고 주거·보증만 과금.
5. **C(A의 부가)**: 회복기 게스트에 K-beauty 키트+피부 추적(Perfect Corp/Haut.AI API)을 제공하고 브랜드에 리뷰 패널 판매. 薬機法·景表法 스텔스마케팅 규제 준수.

---

## 5. 미확인 항목 (추가 조사 권고)

- 「渡韓ガールズ」 인구 추계(정량 조사 없음); 일본인 성형외과 환자의 평균 체류일
- 일본 医療広告ガイドライン의 해외(한국) 의료기관 소개 사이트 적용 여부(법률 검토)
- 한국 의료법 제27조 제3항(영리 알선 금지)의 해외 의료기관 알선 적용 여부
- 도시민박 내 회복기 케어(간호 처치)의 허용 범위
- IT重説 도입률 "30~40%" 및 전자계약 "18.7%"의 원문 출처
- 한국 국적 技術・人文知識・国際業務 인원(e-Stat 크로스표)
- 2025년 일본 中小企業 生成AI 도입률 단일 공식치, 일본 AI 스타트업 국내 조달 총액 2025
- 個人大家 수 최신 공식치, 令和6년도 賃貸住宅管理業 조사 세부
- 한국 임대차분쟁조정위원회 외국인 접수 건수; 일본 ODR 인증 사업자 중 다언어 대응 여부
- 한국 진출 클리닉의 연간 일본 개원 건수; 한국계 MSO 사업자 존재 여부
- 온다(ONDA)·알스퀘어 등 한국 프롭테크의 일본 진출 현황
- 한국인 대상 일본 미용의료·치과·인간독 수요 정량(검색 트렌드·보도 없음)
- 아시아 크로스보더 임차인 신용 패스포트 스타트업 존재 여부
- 일본 화장품 무상 샘플 반입 시 化粧品製造販売業 허가 요건 세부
- 개별 플레이어 미확인: Meeting Beauty, ボーダーリンク, ベストランド, 大家DX, HRnet, Beds24, Squarehotel, 벤티지, 케이엔에프

---

## 6. 출처 요약

본문 각 수치에 병기한 URL이 1차 근거다. 주요 공식 출처: 보건복지부 외국인환자 통계, 観光庁 인바운드 소비동향조사·民泊 届出 현황·2026-07-15 技術的助言, 出入国在留管理庁 재류외국인 통계, 国交省 宅建業者 통계·家賃債務保証 현황, 矢野経済研究所(화장품·미용의료·家賃保証·부동산테크), IDC Japan, 内閣府 AI推進法·人工知能基本計画, 법무부 출입국 통계월보, 스피다 Japan Startup Finance 2025, THE VC·wowtale 한국 투자 통계.
