# 0007 — 하네스 문서 체계는 dryforge, 에이전트·스킬 배치는 J-Booster 관례를 따르고, 워크스페이스 형식은 자체 유지

## 맥락
"다른 프로젝트에 적용된 스킬·하네스·결정·워크로그·큐·스크래핑을 참고해 설계하라"는 요구가 있었다. 이 계정에서 실제로 읽을 수 있었던 참고 저장소는 셋이다: **dryforge**(바운디드 오토노미 플러그인 하네스 — `CLAUDE.md`/`AGENTS.md` + `docs/{architecture,business-rules,security,standards,engineering-notes,operations,contracts,tracking/}` 문서 체계, 서브에이전트는 독립 검증에만, 근거 없는 완료 주장 금지), **J-Booster**(`.claude/agents/*.md`에 `name/description(MUST BE USED·USE PROACTIVELY)/tools/model` 프론트매터, `.claude/skills/<name>/{SKILL.md,scripts/,references/}` 배치, planner→writers→reviewer 파이프라인과 `outputs/`·`review-report.md`), **taste-skill**(단일 스킬 저장소). 사용자의 다른 조직(mobiAI-Inc) 프로젝트에서 쓰는 HANDOFF·worklog 형식은 접근 권한이 없어 읽지 못했다.

## 결정
- 저장소 하네스(`docs/`, 트래킹, 결정 기록)는 dryforge의 문서 체계와 원칙(가치 있는 내용만, 한 문서 한 높이, 트래킹은 상태·미해결·결정)을 따른다
- 서브에이전트 정의는 J-Booster의 프론트매터 관례를 따르고, 역할 분리(추출·검수는 서브에이전트, 판정은 상위)는 결정 0006대로 둔다. `install.sh --project`가 J-Booster식 `.claude/agents/`·`.claude/skills/` 배치를 만든다
- 사용자 프로젝트의 `.ir-search/`(profile · worklog · queue · decisions · runs)는 참고 저장소에 대응물이 없으므로 결정 0002·0003의 자체 형식을 유지한다. 다른 형식이 제시되면 필드 추가로 맞춘다

## 대안
- dryforge를 실제 의존성으로 두고 `ready`/`go`로 이 저장소를 운영: 스킬 사용자에게 무관한 의존성이 생기고, 스킬 실행(조사)과 스킬 개발(코드 수정)은 다른 수명 주기다. 문서 체계만 차용한다
- J-Booster처럼 이 저장소 안에 `.claude/skills/ir-search/`를 두기: 결정 0001(루트 SKILL.md 단일 스킬 플러그인)과 충돌하고, 클론 설치가 깨진다. 대신 `install.sh --project`가 사용자 프로젝트 쪽에 그 배치를 만든다
- 접근 못 한 프로젝트의 형식을 추측해 맞추기: 추측으로 형식을 바꾸면 나중에 두 번 바꾼다

## 결과
- 새 문서를 추가할 때 dryforge 슬롯 밖의 파일(예: `docs/faq.md`)을 만들지 않는다. 있는 슬롯에 넣거나 트래킹에 둔다
- 다른 조직 프로젝트의 워크로그·큐 형식이 필요하면 그 저장소를 세션에 붙이는 것이 선행 조건이다 (status 남은 것 3번)
