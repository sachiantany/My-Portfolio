#!/bin/bash
# Usage:
#   ./apply-theme.sh              — apply the active theme in theme.config.json
#   ./apply-theme.sh blue-theme   — switch to blue-theme and apply
#   ./apply-theme.sh dark-theme   — switch back to dark theme and apply
#   ./apply-theme.sh --list       — list available themes

set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
CONFIG="$ROOT/theme.config.json"

cd "$ROOT"

if [ "$1" = "--list" ]; then
  echo "Available themes:"
  python3 -c "
import json
c = json.load(open('$CONFIG'))
for k, v in c['themes'].items():
    marker = ' ← active' if k == c['active'] else ''
    print(f'  {k}{marker}')
    print(f'    {v[\"description\"]}')
"
  exit 0
fi

# If a theme name is given, update the config
if [ -n "$1" ]; then
  python3 -c "
import json, sys
c = json.load(open('$CONFIG'))
name = sys.argv[1]
if name not in c['themes']:
    print(f'Unknown theme: {name}')
    print('Run ./apply-theme.sh --list to see available themes')
    sys.exit(1)
c['active'] = name
with open('$CONFIG', 'w') as f:
    json.dump(c, f, indent=2)
    f.write('\n')
" "$1"
fi

# Read active theme from config
ACTIVE=$(python3 -c "import json; c=json.load(open('$CONFIG')); print(c['active'])")
FILE=$(python3 -c "import json; c=json.load(open('$CONFIG')); print(c['themes'][c['active']]['file'])")
DESC=$(python3 -c "import json; c=json.load(open('$CONFIG')); print(c['themes'][c['active']]['description'])")

if [ ! -f "$FILE" ]; then
  echo "Error: theme file not found: $FILE"
  exit 1
fi

cp "$FILE" "$ROOT/index.html"
echo "Theme applied: $ACTIVE"
echo "  $DESC"
echo "  index.html updated"
