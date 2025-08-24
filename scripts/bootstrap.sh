#!/usr/bin/env bash
set -euo pipefail
# One-time helper: create .env from template if missing and run preflight.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ ! -f "$ROOT/.env" && -f "$ROOT/.env.template" ]]; then
  cp "$ROOT/.env.template" "$ROOT/.env"
  echo "Filled $ROOT/.env from template. Edit values now."
fi

bash "$ROOT/scripts/preflight.sh"
