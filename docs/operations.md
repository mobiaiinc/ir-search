# 운영: 설치·검증·배포

## 전제

- Python 3.8 이상 (`datetime.date.fromisoformat`, f-string 사용). 3.11에서 검증됨
- 선택: `curl_cffi>=0.15` — 없으면 urllib 폴백. 실제 사이트 대부분이 TLS 지문을 보므로 실사용에는 사실상 필요
- 네트워크: 크롤러는 `*.go.kr`·`nipa.kr`·`kocca.kr`로 HTTPS 직접 접속. 사내 프록시가 CONNECT를 막으면 크롤러가 "network error"를 3회 재시도 후 실패한다 — 프록시 정책을 열어야지 코드로 우회하지 않는다

## 개발 환경 세팅 (순서대로)

```bash
git clone https://github.com/mobiaiinc/ir-search.git && cd ir-search
# 1 컴파일 · 2 네트워크 없는 테스트 · 3 선택 의존성(실사이트 확인 전에만) · 4 실사이트 스모크(네트워크 필요)
# 주의: zsh 대화형 셸은 명령 뒤의 '# 주석'을 인자로 넘긴다 — 주석은 줄을 따로 쓴다
python3 -m py_compile scripts/*.py
python3 -m unittest discover -s tests -v
python3 -m pip install --user 'curl_cffi>=0.15'
python3 scripts/kstartup_crawl.py list -o /tmp/ks.jsonl --max-pages 2
```

4단계는 "fetch backend: curl_cffi"와 "page 1: 15 parsed"가 stderr에 나오면 정상이다. `0 items parsed`면 사이트 개편 또는 차단 — `docs/engineering-notes.md`의 구분법으로 판단한다.

## 로컬 설치 (사용자 관점)

세 방식 중 하나. 결과는 같다: Claude Code가 `SKILL.md`를 스킬로, `agents/ir-*.md`를 서브에이전트로 본다.

```bash
# A. 사용자 전역 (심링크 — git pull이 곧 업데이트)
./install.sh
# B. 특정 프로젝트에만
./install.sh --project ~/work/my-startup
# C. 플러그인 마켓플레이스 (Claude Code 안에서)
/plugin marketplace add mobiaiinc/ir-search
/plugin install ir-search@ir-search
```

`install.sh --copy`는 심링크 대신 복사(Windows·심링크 불가 환경). 제거는 `./install.sh --uninstall [--project DIR]`. 플러그인 설치 시 스킬 호출명은 `/ir-search:ir-search`, 직접 설치 시 `/ir-search`.

## 사용자 프로젝트에서의 첫 실행

```bash
cd ~/work/my-startup
python3 ~/.claude/skills/ir-search/scripts/survey_state.py init     # .ir-search/ 생성 (레거시 프로필 이관)
python3 ~/.claude/skills/ir-search/scripts/survey_state.py status   # 비어 있음을 확인
```

이후는 SKILL.md가 절차대로 부른다. 사람이 직접 볼 파일: `.ir-search/profile.md`(편집 가능), `worklog.md`, `queue.jsonl`(`queue list`로 보기), `decisions.md`, `runs/<날짜>/report.md`.

## 검증 게이트

커밋 전 네 가지가 모두 통과해야 한다 (순서 무관):

```bash
python3 -m py_compile scripts/*.py
python3 -m unittest discover -s tests
python3 -c "import json;[json.load(open(f)) for f in ('.claude-plugin/plugin.json','.claude-plugin/marketplace.json')]"
diff CLAUDE.md AGENTS.md && echo same
```

파서를 고쳤으면 실사이트 스모크(위 4단계)를 네트워크 있는 곳에서 돌리고, 결과 날짜를 `references/sources.md` 상단 "실측 검증" 문구에 갱신한다.

## 배포 (플러그인 버전 올리기)

1. `CHANGELOG.md` 맨 위에 `## vX.Y.Z (날짜)` 항목 추가
2. `.claude-plugin/plugin.json`과 `marketplace.json`의 `version`을 같은 값으로
3. 검증 게이트 통과 → 커밋 → `main`에 병합 → `git tag vX.Y.Z && git push --tags`
4. 플러그인 사용자는 `/plugin marketplace update ir-search` → `/plugin update ir-search@ir-search`. 심링크 설치 사용자는 `git pull`

버전 규칙: 워크스페이스 파일 형식이나 CLI 인터페이스가 비호환으로 바뀌면 major, 소스 추가·옵션 추가는 minor, 파서 수정은 patch.

## 환경 변수

| 변수 | 역할 | 기본 |
|---|---|---|
| `IR_SEARCH_ROOT` | `survey_state.py`의 워크스페이스 위치 강제 (`--root`와 같음) | 없음 → cwd에서 위로 탐색 |
| `CLAUDE_PLUGIN_ROOT` | 플러그인 설치 시 Claude Code가 주는 스킬 폴더. SKILL.md가 `scripts/` 경로 기준으로 언급 | Claude Code가 설정 |

그 외 설정 파일은 없다. 지연·페이지 상한·타임아웃은 스크립트 상수와 CLI 옵션이다.
