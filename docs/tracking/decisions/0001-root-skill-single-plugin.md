# 0001 — SKILL.md를 루트에 두고 단일 스킬 플러그인으로 포장

## 맥락
v2까지의 설치법은 `git clone … ~/.claude/skills/ir-search`였고 SKILL.md가 루트에 있었다. v3에서 플러그인 마켓플레이스 설치와 서브에이전트(`agents/`)를 추가하면서, 다른 플러그인들처럼 `skills/ir-search/SKILL.md` 구조로 옮길지 정해야 했다.

## 결정
SKILL.md는 루트에 남긴다. `.claude-plugin/plugin.json`만 추가해 "루트 SKILL.md + `skills/` 없음 = 단일 스킬 플러그인" 규칙으로 인식되게 한다. `agents/`는 플러그인 루트에 두고, 직접 클론 설치에서는 `install.sh`가 `~/.claude/agents/`로 링크한다.

## 대안
- `skills/ir-search/`로 이동: 플러그인 관례에 맞지만 기존 클론 설치가 전부 깨지고, `install.sh` 없이는 클론 설치가 불가능해진다. 스킬 하나짜리 저장소에서 얻는 것이 없다
- 루트 SKILL.md와 `skills/` 둘 다 유지: 플러그인 로더가 `skills/`가 있으면 루트를 무시하므로 중복이 아니라 누락이 된다

## 결과
- `skills/` 디렉터리를 만들 수 없다 (standards의 구조 규칙)
- 스킬을 둘 이상으로 늘리려면 이 결정을 뒤집어야 한다 (그때는 `install.sh`가 하위 폴더를 링크하도록 바꾼다)
- 플러그인 설치 시 호출명이 `ir-search:ir-search`로 겹쳐 보인다 — 감수
