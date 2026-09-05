#!/usr/bin/env bash
# install.sh — put the ir-search skill (and its two subagents) where Claude Code finds them.
#
#   ./install.sh                     user-level:    ~/.claude/skills/ir-search + ~/.claude/agents/ir-*.md
#   ./install.sh --project DIR       project-level: DIR/.claude/skills/ir-search + DIR/.claude/agents/ir-*.md
#   ./install.sh --copy              copy instead of symlink (no live updates from this checkout)
#   ./install.sh --uninstall [--project DIR]
#
# Symlinks are the default so `git pull` in this checkout updates the installed skill.
# Plugin-marketplace install is the alternative that needs no script:
#   /plugin marketplace add mobiaiinc/ir-search
#   /plugin install ir-search@ir-search
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_BASE="$HOME/.claude"
MODE="link"
ACTION="install"

while [ $# -gt 0 ]; do
  case "$1" in
    --project) TARGET_BASE="$(cd "$2" && pwd)/.claude"; shift 2 ;;
    --copy) MODE="copy"; shift ;;
    --uninstall) ACTION="uninstall"; shift ;;
    -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 1 ;;
  esac
done

SKILL_DST="$TARGET_BASE/skills/ir-search"
AGENT_DST="$TARGET_BASE/agents"

if [ "$ACTION" = "uninstall" ]; then
  rm -rf "$SKILL_DST"
  for a in "$HERE"/agents/ir-*.md; do rm -f "$AGENT_DST/$(basename "$a")"; done
  echo "removed $SKILL_DST and $AGENT_DST/ir-*.md"
  exit 0
fi

# --- preflight -------------------------------------------------------------
[ -f "$HERE/SKILL.md" ] || { echo "✗ SKILL.md not found next to install.sh" >&2; exit 1; }
command -v python3 >/dev/null || { echo "✗ python3 is required (3.8+)" >&2; exit 1; }
PYV="$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' \
  || { echo "✗ python3 $PYV found; 3.8+ required" >&2; exit 1; }
python3 -m py_compile "$HERE"/scripts/*.py || { echo "✗ scripts do not compile" >&2; exit 1; }

# --- install ---------------------------------------------------------------
mkdir -p "$(dirname "$SKILL_DST")" "$AGENT_DST"
if [ -e "$SKILL_DST" ] || [ -L "$SKILL_DST" ]; then
  if [ -L "$SKILL_DST" ] && [ "$(readlink "$SKILL_DST")" = "$HERE" ]; then
    echo "· skill already linked: $SKILL_DST"
  else
    echo "✗ $SKILL_DST exists and is not a link to this checkout — remove it or run --uninstall first" >&2
    exit 1
  fi
else
  if [ "$MODE" = "link" ]; then
    ln -s "$HERE" "$SKILL_DST"
    echo "✓ skill linked:  $SKILL_DST → $HERE"
  else
    mkdir -p "$SKILL_DST"
    cp -R "$HERE/SKILL.md" "$HERE/scripts" "$HERE/references" "$HERE/LICENSE" "$SKILL_DST/"
    echo "✓ skill copied:  $SKILL_DST"
  fi
fi

for a in "$HERE"/agents/ir-*.md; do
  dst="$AGENT_DST/$(basename "$a")"
  if [ "$MODE" = "link" ]; then
    ln -sfn "$a" "$dst"
  else
    cp "$a" "$dst"
  fi
  echo "✓ agent:         $dst"
done

# --- optional dependency ---------------------------------------------------
if python3 -c 'import curl_cffi' 2>/dev/null; then
  echo "✓ curl_cffi present (browser TLS fingerprint)"
else
  echo "! curl_cffi not installed — crawlers fall back to urllib and may be blocked by the sites' WAF."
  echo "  install with:  pip install 'curl_cffi>=0.15'"
fi

cat <<EOF

Done. In Claude Code, open a project folder and say:
  우리 아이템에 맞는 지원사업 전수조사 해줘
or invoke /ir-search. Survey state will live in <project>/.ir-search/.
EOF
