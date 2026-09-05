# .ir-search/ 워크스페이스 규격

프로젝트 폴더 안의 `.ir-search/`는 ir-search의 **유일한 지속 상태 저장소**다. 조사에 관해 다음 세션이 알아야 할 것은 전부 여기에 있고, 여기 없는 것은 없는 것으로 취급한다 (에이전트 메모리·대화 기록에 의존하지 않는다). 모든 파일은 `scripts/survey_state.py`가 만들고 갱신하며, 사람이 손으로 고쳐도 된다.

```
<project>/.ir-search/
├── profile.md        신청자(아이템) 프로필 — 조사의 입력
├── worklog.md        실행 기록 (append-only) — 무엇을 언제 조사했나
├── queue.jsonl       열린 작업 항목 — 다음에 할 일
├── decisions.md      판정·구성 결정과 이유 — 왜 그렇게 판단했나
└── runs/
    └── YYYYMMDD[-N]/ 한 번의 조사 실행
        ├── run.json          단계 마커 + 메타 (재개 지점)
        ├── kstartup.jsonl    원시 수집 결과 (소스별 파일)
        ├── bizinfo.jsonl
        ├── new_items.jsonl   diff 모드: 신규 검토 대상
        ├── details/          상세공고 원문 텍스트
        ├── verified.jsonl    (선택) 서브에이전트의 구조화 추출 결과
        └── report.md         보고서
```

`.ir-search/`를 git에 커밋할지는 프로젝트가 정한다. 공고 원문(`details/`)은 크기가 크므로 보통 `runs/*/details/`만 ignore하고 나머지는 커밋해 팀이 공유한다.

## profile.md

```markdown
# ir-search 프로필
- 대상: <프로젝트명 (아이템 한 줄)>
- 창업 단계: <예비창업자 / 개인사업자 / 법인 N년차>
- 지역 연고: <소재지 (이전 가능: ...)>
- 대표자: <연령대 / 성별 / 소속>
- 필요한 것: <자금, 공간, R&D, ...>
- 소스 구성: <kstartup, bizinfo, ...>
- 마지막 조사: <runs/... 경로> (<YYYY-MM-DD>)
```

- `- ` 로 시작하는 줄만 스크립트가 읽는다 (`status`가 그대로 출력). 그 아래 자유 메모를 붙여도 된다
- `마지막 조사`는 `run finish`가 갱신한다. 손으로 고치지 않는다
- `소스 구성`은 diff 모드가 "직전과 같은 소스"를 재현하는 근거다. 소스를 바꾸면 이 줄도 바꾸고, 바꾼 이유를 `decisions.md`에 남긴다
- 프로필 축 외의 개인정보(주민번호·계좌·연락처)는 넣지 않는다

## worklog.md

완료된 실행마다 `run finish`가 한 항목을 **끝에 추가**한다. 수정하지 않고 추가만 한다.

```markdown
## 2026-09-05 — 전수조사 (full) · .ir-search/runs/20260905
- 소스: kstartup 262 / bizinfo 300
- 후보 31 → 상세검증 31 → A 5 / B 4 / C 6
- 보고서: .ir-search/runs/20260905/report.md
- 기준(diff 베이스라인): .ir-search/runs/20260811     ← diff 모드일 때만
- 메모: 첫 조사. NIPA는 차단되어 수동 확인으로 남김
```

워크로그는 "이 프로젝트에서 지원사업 조사를 얼마나 자주, 어떤 범위로 했나"를 한 파일로 답한다. 한 실행에 대한 상세는 `runs/<날짜>/run.json`에 있다.

## queue.jsonl

한 줄에 한 항목. `survey_state.py queue add/done/list`로 다룬다.

| 필드 | 뜻 |
|---|---|
| `id` | `q001`부터 순번 |
| `type` | `verify` 상세검증 대기 · `manual` 수동 확인 · `apply` 신청 진행 · `followup` 후속 확인(유선확인 등) · `resurvey` 재조사 예정 |
| `title` | 공고 제목 또는 할 일 |
| `url`, `source`, `ref` | 공고 URL / 소스명 / 공고 ID (같은 `type`+`ref`(또는 `url`)가 열려 있으면 중복 등록되지 않는다) |
| `deadline` | `YYYY-MM-DD`. 모르면 빈 값 → 표에 "불명" |
| `note` | 자유 메모 |
| `run` | 등록 당시 진행 중이던 실행 폴더명. `verify` 항목은 그 실행의 `run finish` 때 자동으로 닫힌다 |
| `status`, `added`, `closed` | `open`/`done`, 등록일, 종료일 |

`queue list`는 열린 항목을 종류 → 마감순으로 정렬한 마크다운 표로 내고, 오늘 기준 D-day를 계산한다. D-3 이하와 D-Day는 ⚠️, 지난 것은 "(지남)"으로 표시된다. 지난 `apply` 항목은 diff 모드에서 "기회 소멸"로 보고한 뒤 닫는다.

큐의 역할 두 가지:
1. **체크포인트** — 2단계에서 뽑은 후보를 `verify`로 넣어 두면, 세션이 끊겨도 다음 세션은 큐만 보고 3단계를 이어간다
2. **사용자 액션 트래커** — 조사가 끝난 뒤에도 `apply`/`followup`/`resurvey`가 남아 "다음에 무엇을 언제까지"를 답한다. 채팅 응답 끝에 `queue list`를 붙이는 이유

## decisions.md

다른 선택도 가능했던 결정만 기록한다. `survey_state.py decide`가 끝에 추가한다.

```markdown
## 2026-09-05 — 프리팁스 A→B 하향
- 결정: A그룹이 아니라 B그룹으로 분류
- 이유: 공고문 "비수도권 소재 법인" 요건. 프로필은 예비창업자(충남)이므로 법인 설립이 트리거
- 대상: pbancSn 1779xx
- 실행: .ir-search/runs/20260905
```

기록 대상의 예: 판정 등급 변경과 그 근거 / 사용자가 판정을 뒤집은 경우 / 소스 추가·제외와 이유 / 프레이밍 각도 채택·기각 / `--max-pages` 같은 수집 범위 결정. 기록하지 않는 것: 원문에 명시되어 있어 달리 판단할 여지가 없는 것 (그건 보고서에 있다).

## runs/<날짜>/run.json

```json
{
  "started": "2026-09-05T10:12:00",
  "mode": "full",                 // full | diff
  "sources": ["kstartup", "bizinfo"],
  "stage": "verify",              // collect → review → verify → report → done
  "baseline": ".../runs/20260811",  // diff 모드일 때 직전 완료 실행
  "stage_log": [{"stage": "review", "at": "..."}, ...],
  "finished": "...", "report": "...", "counts": {...}, "candidates": 31, "verified": 31,
  "verdicts": {"A": 5, "B": 4, "C": 6}, "note": ""
}
```

- `stage`가 `done`이 아닌 실행이 있으면 `status`가 "진행 중"으로 보여 주고, 새 `run new`는 거부한다 (`--force`로 강제 가능). 끊긴 조사를 조용히 버리지 않기 위한 규칙이다
- `run last`는 `done`인 실행 중 가장 최근을 준다 — diff 모드의 베이스라인
- 같은 날 두 번째 실행은 `YYYYMMDD-2`
