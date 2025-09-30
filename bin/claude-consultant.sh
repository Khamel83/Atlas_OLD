#!/bin/bash
# Direct bridge to OOS consultant command
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OOS_DIR="$SCRIPT_DIR/../oos"
"$OOS_DIR/bin/oos-command.sh" consultant "$@"
