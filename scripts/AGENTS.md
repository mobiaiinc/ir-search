# scripts/

이 폴더가 소유하는 것: 공고 사이트 접근(`fetchlib.py`), 소스별 파싱(`kstartup_crawl.py`, `sources_crawl.py`), 실행 간 비교(`diff_surveys.py`), 사용자 프로젝트의 `.ir-search/` 상태(`survey_state.py`). 소유하지 않는 것: 판정(A/B/C)과 보고서 작성 — 그것은 모델이 SKILL.md를 따라 한다. 여기 있는 코드는 **판단하지 않고 사실만 옮긴다**.

## 불변조건

- 파서가 돌려주는 값은 페이지에 있던 문자열이거나 빈 문자열이다. 기본값·추정값·"아마 이럴 것" 없음
- 모든 HTTP 요청은 `fetchlib.Fetcher.fetch`를 거친다. 지연·에스컬레이션·차단 판정이 거기 있으므로 우회 경로를 만들면 그 보장이 사라진다
- `Blocked`는 삼키지 않는다. 잡아서 "이 소스 차단"으로 보고하고 종료 코드 2를 낸다
- 표준 라이브러리만. `curl_cffi`는 `fetchlib._CurlBackend` 안에서만 지연 import
- `survey_state.py`만 `.ir-search/`를 쓴다. 크롤러·diff는 인자로 받은 경로에만 쓴다
- `.ir-search/` 파일의 기존 필드는 이름·의미를 바꾸지 않는다. 추가만 한다

## 경계

- 이 폴더는 `SKILL.md`, `references/`, `agents/`를 읽지 않는다. 어떤 스크립트도 마크다운을 파싱하지 않는다 (`profile.md`의 `- ` 줄 출력과 `마지막 조사` 줄 치환은 예외이며 그 두 가지가 전부다)
- 하위 패키지를 만들지 않는다. `sys.path.insert(0, 자기 폴더)` 뒤 `from fetchlib import …` 방식이라 평평해야 한다
- 소스 추가는 `sources_crawl.py`에 `page_<name>(fetch, page) -> (items, has_more)` 하나 + `SOURCES` 등록 + `ALLOWED_DETAIL_HOSTS` 추가. 새 파일을 만들지 않는다 (K-Startup만 스키마가 달라 별도 파일이다)

## 구현 패턴

- 파서: `<tr>…</tr>` 단위로 자르고, 행 안에서 링크 정규식으로 ID를 뽑고, 나머지는 `<td>` 텍스트 목록에서 위치 또는 패턴으로 고른다. 위치가 흔들리는 소스(SMTECH)는 패턴(`~` 포함, 날짜 전체 일치)으로
- 페이지 루프: `seen[id] = item`으로 덮어쓰기 dedup, 새 항목 0건이면 종료
- 날짜: `fetchlib.norm_date` → `YYYY-MM-DD`, 경과 판정 `fetchlib.is_past(s, today)`
- 로그: `log(msg)` → stderr `[ir-search] …`. stdout에는 데이터만
- 상태: JSON 읽고-수정하고-통째로 쓰기. 동시 실행은 가정하지 않는다

## 테스트

- 네트워크 없이 돈다. 파서는 합성 HTML 문자열, `Fetcher`는 가짜 백엔드 객체를 `f.backend`에 꽂아서, 상태는 임시 폴더 + `--root` + `--today`
- 파서를 고치면 그 소스의 합성 HTML 픽스처(`tests/test_parsers.py`)도 실제 마크업에 맞춰 고친다. 픽스처가 실제와 다르면 테스트가 통과해도 의미가 없다 — 실사이트 스모크는 별도
- 확인할 것: 정상 파싱 / 링크 없는 행 건너뛰기 / 빈 페이지 → `([], False)` / 날짜 정규화 / `--drop-expired`가 빈 마감을 남기는지 / 에스컬레이션 순서 / `Blocked`가 올라오는지 / `run new` 거부 / `verify` 큐 자동 종료
