#!/bin/bash
# Direct bridge to OOS command system from Atlas
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$SCRIPT_DIR/oos-command.sh" "$@"