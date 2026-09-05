# 현황

기준: v3.0.0 (2026-09-05, 같은 날 드라이런·정렬 수정 반영). "검증됨"은 이 저장소의 테스트(네트워크 없음) 또는 실사이트 실측으로 확인한 것이고, "구현됨"은 코드는 있으나 그 확인이 없는 것이다.

## 완료

| 영역 | 상태 | 근거 |
|---|---|---|
| K-Startup 목록·상세 파서 | 실측 검증 (2026-07-11) · 합성 HTML 테스트 통과 | `tests/test_parsers.py` |
| 기업마당·NIPA·KOCCA·SMTECH 파서 | 실측 검증 (2026-07-11) · 합성 HTML 테스트 통과 | 같은 파일 |
| 공용 HTTP (`fetchlib`) — 지문 사다리·차단 판정·재시도·지연 | 가짜 백엔드 테스트 통과. **실사이트 실측 없음** (개발 환경이 `*.go.kr` CONNECT를 거부) | `tests/test_fetchlib.py` |
| `--drop-expired` | 테스트 통과 (빈 마감·"상시" 유지) | 같은 파일 |
| diff (`diff_surveys`) — 신규/종료/마감변경/미갱신 소스, 파생 파일 제외 | 테스트 통과 | `tests/test_diff.py` |
| 워크스페이스 (`survey_state`) — init/이관/run/queue/decide/status | 테스트 통과 | `tests/test_state.py` |
| SKILL.md 워크플로 (재개·diff·큐·서브에이전트 위임) | CLI 경로 드라이런 통과 (2026-09-05: `init` 이관 → `status` → `run new` → 거부 → `stage` → `queue add`/중복/`done` → `decide` → `run finish` → `status` → `run new --mode auto`가 diff로 시작). **실제 Claude Code 세션에서 모델이 절차를 따르는 end-to-end는 아직** | 수동 실행 |
| 서브에이전트 2개 | 작성됨. 실제 위임 실행 없음 | — |
| 플러그인 매니페스트 · install.sh | JSON 유효성 확인 · `--project` 링크 / 재실행 idempotent / 사용자 전역 `--copy` / 양쪽 `--uninstall` 동작 확인 (2026-09-05) | 수동 실행 |
| `run last`/`run current` 정렬 | `started` 기준으로 고침 (같은 날 10회 이상 실행 시 `-10` < `-2` 문제) · 테스트 추가 | `tests/test_state.py` |
| README (한/영) · CHANGELOG | 갱신됨 | — |

## 남은 것 (우선순위순)

1. **실사이트 스모크** — 네트워크 있는 환경에서 5개 소스 `list --max-pages 2`를 돌려 `fetchlib` 경로(특히 curl_cffi 설치 상태에서의 사다리)를 확인하고 `references/sources.md` 실측 날짜 갱신
2. **모델 주도 end-to-end** — 실제 프로젝트 폴더에서 `/ir-search`를 한 번 끝까지 돌려 SKILL.md 절차에 빠진 명령·어색한 분기를 찾는다 (CLI 경로는 드라이런으로 확인됨). 특히 세션을 일부러 끊고 `status` → 재개가 되는지, 서브에이전트 위임이 실제로 일어나는지
3. **큐·워크로그 형식 정합** — 이 계정에서 접근 가능한 저장소(J-Booster·dryforge·taste-skill)에는 워크로그·큐 대응물이 없어 자체 형식을 유지했다 (결정 0007). 다른 조직(mobiAI-Inc)의 프로젝트에서 쓰는 HANDOFF·worklog 형식을 맞추려면 그 저장소를 세션에 붙여 주면 필드 추가로 대응한다
4. 지역 기관(테크노파크·지역 콘텐츠진흥원) 소스 추가 — `sources.md`에 미검증으로만 있음
5. CCEI(창조경제혁신센터) JS 목록의 내부 API 경로 확인 후 파서 추가 검토

## 막힌 것

- 개발 컨테이너에서 공고 사이트로의 HTTPS가 프록시 정책으로 거부되어 1번을 여기서 못 한다. 코드로 우회하지 않는다 (정책)
