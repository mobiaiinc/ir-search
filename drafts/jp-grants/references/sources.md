# jp-grants 소스 레지스트리 (초안 · 전부 미검증)

접근 전 첫 페이지를 받아 서버렌더링·페이지네이션·締切 표기를 확인하고 날짜를 적는다.

## 통합 포털

- **jGrants** — **https://www.jgrants-portal.go.jp/** (デジタル庁). 국가·자치체 보조금 검색 + 전자신청(gBizID)
  - 공개 검색 API(로그인 불필요)로 기억: `https://api.jgrants-portal.go.jp/exp/v1/public/subsidies?keyword=…&sort=created_date&order=DESC&acceptance=1` → 목록(JSON: id, title, subsidy_max_limit, acceptance_start/end_datetime, target_area_search…), 상세 `…/public/subsidies/id/<id>` — **형식·필수 파라미터 확인 필요**
  - 신청 화면은 접근하지 않는다
- **J-Net21 支援情報ヘッドライン** — https://j-net21.smrj.go.jp/snavi/ (中小機構). 국가·자치체·公益法人 공모를 매일 집계. 分野·地域 필터, RSS 있음으로 기억
- **ミラサポplus 制度ナビ** — https://mirasapo-plus.go.jp/ (経産省). 제도 검색. 締切보다 제도 소개 위주

## 省庁·独法

- 経済産業省 公募情報 — https://www.meti.go.jp/information/publicoffer/kobo.html
- 中小企業庁 — https://www.chusho.meti.go.jp/ (補助金 특설: ものづくり·IT導入·持続化·省力化 등은 각 事務局 사이트)
- NEDO 公募 — https://www.nedo.go.jp/koubo/ (AI·에너지·스타트업 NEP/STS)
- IPA — https://www.ipa.go.jp/ (未踏, AI 관련 공모)
- 総務省 — 地域·ICT 실증
- 内閣府 SBIR — 政府調達형 지원
- 日本貿易振興機構 JETRO — 외국기업 유치·対日投資(한국 법인의 일본 진출 지원은 여기가 먼저)

## 자치체 (프로필 소재지 기준으로 선택)

- 東京都: 産業労働局 / 東京都中小企業振興公社 助成金 https://www.tokyo-kosha.or.jp/support/josei/ (創業助成 등) / TOKYO創業ステーション / 東京都 스타트업 지원
- 大阪: 大阪府·大阪市·大阪産業局
- 福岡市: スタートアップ 지원(グローバル創業·雇用創出特区)
- 그 외 都道府県 産業振興財団·よろず支援拠点

## AI 관련 (이름에 AI가 없는 것 포함)

- 経産省 GENIAC(基盤モデル 개발), IPA AI 관련 공모, NEDO AI·ロボット
- 자치체 DX·AI導入 支援(東京都 中小企業デジタルツール導入促進 등), 中小企業省力化投資補助金(カタログ型)
- 검토 시 "DX", "省力化", "生産性向上", "デジタル化" 제목을 AI 후보로 본다

## 공통 원칙

- 공개 페이지만. gBizID 로그인·電子申請 화면 자동화 없음
- 締切은 日時(JST)·方式(電子/郵送/メール)·必着/消印을 같이 기록
- 公募要領 PDF가 본문이면 텍스트 추출본을 details/에, 실패 시 "PDF 참조 + URL"
