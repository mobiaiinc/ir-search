# 규칙 (위반하면 깨지는 것)

## 구조

- `SKILL.md`는 저장소 루트에 있어야 한다. `skills/` 디렉터리를 만들지 않는다 — 루트 SKILL.md와 `skills/`가 공존하면 플러그인 로더가 루트 SKILL.md를 스킬로 읽지 않고, 직접 클론 설치(`~/.claude/skills/ir-search/SKILL.md`)는 `skills/` 하위를 보지 않는다
- 서브에이전트는 `agents/ir-*.md`에 둔다. 파일명이 `ir-`로 시작해야 `install.sh`가 링크·제거 대상으로 잡는다
- 스크립트는 `scripts/` 한 단계에 평평하게 둔다. `sys.path.insert(0, <자기 폴더>)` 뒤에 `from fetchlib import …` 하는 방식이라 하위 패키지를 만들면 import가 깨진다
- 참조 문서는 `references/`에 두고 SKILL.md에서 파일명으로 부른다. SKILL.md 본문은 절차만, 형식·템플릿·체크리스트는 references/로 보낸다

## 스크립트

- 표준 라이브러리만 import한다. `curl_cffi`는 `fetchlib._CurlBackend.__init__` 안에서만 지연 import하고, `ImportError`면 urllib 백엔드로 폴백한다. 다른 파일에서 `curl_cffi`를 import하면 안 된다
- 모든 HTTP는 `fetchlib.Fetcher`를 거친다. 크롤러 안에 `urllib.request`나 `time.sleep` 기반 지연을 다시 쓰지 않는다
- 파서(`parse_list`, `page_*`)는 **순수 함수**다: `(html)` 또는 `(fetch, page)`를 받고 목록을 돌려주며 파일·stdout을 건드리지 않는다. 테스트가 가짜 `fetch`를 주입한다
- 파서는 필드를 못 찾으면 빈 문자열을 넣는다. 기본값·추정값을 넣지 않는다. 항목 자체를 못 찾으면 빈 목록을 돌려주고, 호출자가 "0건 파싱" 경고를 낸다
- 로그는 stderr, 데이터는 파일(또는 `--json`일 때 stdout). `survey_state.py run new`처럼 경로를 stdout에 내는 명령은 stdout에 그것만 낸다 (`$(…)`로 받는다)
- 종료 코드: 0 성공, 1 잘못된 입력·워크스페이스 없음, 2 일부 소스 차단(수집은 저장됨)
- 날짜는 `YYYY-MM-DD` 문자열. 파싱은 `fetchlib.norm_date`, 경과 판정은 `fetchlib.is_past`만 쓴다
- 사람이 읽는 출력·파일 내용은 한국어, 코드·주석·CLI 옵션·로그 접두어는 영어

## 상태 파일 호환

- `run.json`, `queue.jsonl`, `worklog.md`, `profile.md`의 기존 필드·줄 형식은 바꾸지 않는다. 필드 추가는 되고, 읽을 때는 `.get()`으로 없는 필드를 허용한다
- `profile.md`에서 스크립트가 파싱하는 것은 `- ` 로 시작하는 줄과 `- 마지막 조사:` 정규식뿐이다. 다른 줄에 의존하는 코드를 넣지 않는다
- 레거시 `ir-search-profile.md` 이관은 유지한다 (v2 사용자)

## 문서 정합

- 판정 규칙(A/B/C, 불명, diff 분류)은 SKILL.md·`references/report-format.md`·`agents/*.md`·`docs/business-rules.md`에 각각 자기 높이로 적혀 있다. 하나를 바꾸면 넷을 확인한다
- 소스의 URL·페이지네이션·파서 특성을 바꾸면 `references/sources.md`와 `docs/engineering-notes.md`를 함께 고친다
- `CLAUDE.md`와 `AGENTS.md`는 바이트 단위로 같아야 한다. 하나만 고치지 않는다 (`diff CLAUDE.md AGENTS.md`가 비어야 한다)
- README.md와 README.en.md의 설치·사용·구성 절은 내용이 대응해야 한다

## 검증 게이트 (커밋 전)

```bash
python3 -m py_compile scripts/*.py
python3 -m unittest discover -s tests -v
python3 -c "import json;[json.load(open(f)) for f in ('.claude-plugin/plugin.json','.claude-plugin/marketplace.json')]"
diff CLAUDE.md AGENTS.md
```

넷 다 통과하지 않으면 커밋하지 않는다. 실제 사이트에 대한 크롤링 검증은 네트워크가 있는 환경에서 별도로 하고 결과 날짜를 `references/sources.md` 상단에 적는다.

## 커밋

- 한 커밋에 한 관심사. 파서 수정과 SKILL.md 절차 변경을 섞지 않는다
- 메시지는 `feat:`, `fix:`, `docs:`, `refactor:` 접두어 + 한 줄 요약 (한국어·영어 무관)
- 실제 사이트 실측으로 파서를 고쳤으면 메시지에 실측 날짜를 적는다
