# Save as opencode-setup.sh, chmod +x opencode-setup.sh, then run:
# (EXECUTE THIS]  ./opencode-setup.sh --install auto --auth auto
# After it finishes: open a new shell (or source ~/.bashrc / your shell RC) so the opencode wrapper takes effect.

#!/usr/bin/env bash
# ---
# opencode-setup.sh — One-file bootstrap for Opencode (macOS/Ubuntu, x64/ARM)
#
# DEFAULTS:
#   - Anthropic Pro (OAuth) as global model
#   - Agentic YOLO as default CLI behavior (opencode -> @yolo)
#   - OpenRouter models + agents preloaded
#   - MCP servers installed/registered when available
#
# PER-PROJECT DEFAULT (optional):
#   PROJECT_MODEL_OVERRIDE="openrouter/qwen/qwen3-coder:free" ./opencode-setup.sh --project
#
# DAILY USE:
#   opencode        # YOLO mode (applies diffs immediately; minimal confirmations)
#   opencode-std    # Regular agentic mode (normal review/apply flow)
#   /models         # switch in-session
# ---

set -euo pipefail

########################################
# HARD-CODED KEYS (rotate here if needed)
########################################
OPENROUTER_API_KEY="${OPENROUTER_API_KEY:-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}"
TAVILY_API_KEY="${TAVILY_API_KEY:-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}"
OPENAI_API_KEY="${OPENAI_API_KEY:-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}"

# Optional OpenRouter attribution headers
OPENROUTER_HTTP_REFERER="${OPENROUTER_HTTP_REFERER:-https://github.com/khamel83}"
OPENROUTER_X_TITLE="${OPENROUTER_X_TITLE:-opencode-vibecoding}"

# Models / agents
DEFAULT_ANTHROPIC_MODEL="anthropic/claude-sonnet-4-20250514"   # Pro/Max OAuth
SMALL_MODEL="openrouter/qwen/qwen3-coder:free"
OR_MODELS=("moonshotai/kimi-k2:free" "qwen/qwen3-coder:free" "google/gemini-2.5-flash")

# Per-project override (only with --project)
PROJECT_MODEL_OVERRIDE="${PROJECT_MODEL_OVERRIDE:-}"

# MCP installs toggle
WITH_MCP="${WITH_MCP:-auto}"   # auto|yes|no

# Flags
DO_INSTALL=auto
DO_AUTH=auto
SCOPE="global"
PROJECT_DIR=""

########################################
# UTIL
########################################
log(){ printf "%s\n" "$*"; }
ok(){ printf "✅ %s\n" "$*"; }
warn(){ printf "⚠️  %s\n" "$*"; }
die(){ printf "❌ %s\n" "$*" >&2; exit 1; }
need(){ command -v "$1" >/dev/null 2>&1; }
is_macos(){ [[ "$(uname -s)" == "Darwin" ]]; }
is_ubuntu(){ [[ -f /etc/lsb-release ]] && grep -qi ubuntu /etc/lsb-release; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --install) DO_INSTALL="${2:-auto}"; shift 2;;
    --auth)    DO_AUTH="${2:-auto}";    shift 2;;
    --project) SCOPE="project"; PROJECT_DIR="${2:-}"; if [[ -z "$PROJECT_DIR" || "$PROJECT_DIR" == --* ]]; then PROJECT_DIR="$PWD"; shift 1; else shift 2; fi ;;
    --no-project) SCOPE="global"; shift;;
    -h|--help) echo "Usage: $0 [--install auto|yes|no] [--auth auto|yes|no] [--project [DIR]]"; exit 0;;
    *) die "Unknown arg: $1";;
  esac
done

HOME_DIR="${HOME:-$PWD}"
CONFIG_DIR="$HOME_DIR/.config/opencode"
AUTH_DIR="$HOME_DIR/.local/share/opencode"
CONFIG_FILE="$CONFIG_DIR/opencode.json"

shell_rc() {
  if [[ -n "${ZDOTDIR:-}" && -f "$ZDOTDIR/.zshrc" ]]; then echo "$ZDOTDIR/.zshrc";
  elif [[ -n "${BASH_VERSION:-}" && -f "$HOME_DIR/.bashrc" ]]; then echo "$HOME_DIR/.bashrc";
  else echo "$HOME_DIR/.profile"; fi
}
export_env() {
  local name="$1" val="$2" rc; rc="$(shell_rc)"
  [[ -z "$val" ]] && return 0
  if ! grep -q "^export $name=" "$rc" 2>/dev/null; then
    echo "export $name=\"$val\"" >> "$rc"
    ok "Exported $name in $rc (restart shell or 'source' it)"
  else
    ok "$name already exported in $rc"
  fi
  export "$name=$val"
}

########################################
# SYSTEM PREP
########################################
mac_prep() {
  if ! need brew; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv)" 2>/dev/null || true
    eval "$(/usr/local/bin/brew shellenv)" 2>/dev/null || true
  fi
  brew update || true
  brew install node bun pipx git || true
  pipx ensurepath || true
}
ubuntu_prep() {
  sudo apt update -y
  sudo apt upgrade -y || true
  sudo apt install -y curl git build-essential ca-certificates
  # Node/npm
  if ! need node || ! need npm; then
    sudo apt install -y nodejs npm || true
  fi
  # pipx + venv (fixes PEP 668)
  sudo apt install -y pipx python3-venv || true
  pipx ensurepath || true
}

########################################
# INSTALL OPENCODE
########################################
install_opencode() {
  if is_macos; then
    brew install sst/tap/opencode || true
  else
    curl -fsSL https://opencode.ai/install | bash
  fi
}
ensure_opencode() {
  if need opencode; then ok "opencode found: $(command -v opencode)"; else
    case "$DO_INSTALL" in
      yes) install_opencode ;;
      no)  die "opencode missing and --install no" ;;
      *)   log "Installing opencode (auto)…"; install_opencode ;;
    esac
    need opencode || die "opencode installation failed"
  fi
}

########################################
# DEV RUNTIMES
########################################
ensure_bun() {
  if ! need bun; then
    curl -fsSL https://bun.sh/install | bash
    export BUN_INSTALL="$HOME/.bun"
    export PATH="$BUN_INSTALL/bin:$PATH"
    local rc; rc="$(shell_rc)"
    if ! grep -q 'BUN_INSTALL' "$rc" 2>/dev/null; then
      {
        echo 'export BUN_INSTALL="$HOME/.bun"'
        echo 'export PATH="$BUN_INSTALL/bin:$PATH"'
      } >> "$rc"
    fi
  fi
}
npm_g_install(){ pkg="$1"; if need npm; then npm -g i "$pkg" >/dev/null 2>&1 || true; fi }

########################################
# MCP INSTALLS
########################################
install_mcps() {
  case "$WITH_MCP" in
    no)  warn "Skipping MCP installs (WITH_MCP=no)"; return;;
    auto|yes) : ;;
    *) warn "WITH_MCP=$WITH_MCP not recognized; skipping MCP"; return;;
  esac

  ensure_bun

  # Core NPM-published servers
  npm_g_install "@upstash/context7-mcp"                 # -> context7-mcp (docs)
  npm_g_install "@github/github-mcp-server"             # -> github-mcp-server
  npm_g_install "@modelcontextprotocol/server-puppeteer"# -> server-puppeteer
  npm_g_install "@arben-adm/mcp-sequential-thinking"    # -> mcp-sequential-thinking
  npm_g_install "zen-mcp-server"                        # -> zen-mcp-server (optional fan-out)
  npm_g_install "memory-bank-mcp"                       # -> memory-bank-mcp (community)
  ok "MCP npm install pass complete."
}

maybe_install_gpt_researcher() {
  if [[ -n "$OPENAI_API_KEY" && -n "$TAVILY_API_KEY" ]]; then
    pipx install gpt-researcher >/dev/null 2>&1 || true
    ok "GPT-Researcher installed (pipx)."
  else
    warn "GPT-Researcher not enabled (needs both OPENAI_API_KEY and TAVILY_API_KEY)."
  fi
}

########################################
# CONFIG WRITERS
########################################
write_global_config() {
  mkdir -p "$CONFIG_DIR" "$AUTH_DIR"
  # OR models JSON
  local models_json=""; for m in "${OR_MODELS[@]}"; do models_json+="\"$m\": {},"; done
  models_json="{${models_json%,}}"

  # Register MCPs only if commands exist
  declare -A MCP_COMMANDS=(
    [context7]=context7-mcp
    [github]=github-mcp-server
    [puppeteer]=server-puppeteer
    [sequential]=mcp-sequential-thinking
    [zen]=zen-mcp-server
    [memorybank]=memory-bank-mcp
    # optional: auto-register if later installed
    [serena]=serena-mcp
    [taskmaster]=claude-task-master
    [skyvern]=skyvern-mcp
    [gptresearcher]=gpt-researcher-mcp
  )
  local mcp_json_entries=""
  for key in "${!MCP_COMMANDS[@]}"; do
    cmd="${MCP_COMMANDS[$key]}"
    if command -v "$cmd" >/dev/null 2>&1; then
      mcp_json_entries+="\"$key\": { \"command\": \"$cmd\" },"
    fi
  done
  local mcp_servers_json="{${mcp_json_entries%,}}"

  cat >"$CONFIG_FILE"<<EOF
{
  "\$schema": "https://opencode.ai/config.json",
  "model": "$DEFAULT_ANTHROPIC_MODEL",
  "small_model": "$SMALL_MODEL",
  "provider": {
    "anthropic": {
      "options": { "baseURL": "https://api.anthropic.com/v1" },
      "models": { }
    },
    "openrouter": {
      "options": {
        "headers": {
          "HTTP-Referer": "$OPENROUTER_HTTP_REFERER",
          "X-Title": "$OPENROUTER_X_TITLE"
        }
      },
      "models": $models_json
    }
  },
  "agent": {
    "claude-pro":   { "description": "Claude Sonnet via Pro/Max (OAuth)", "model": "$DEFAULT_ANTHROPIC_MODEL" },
    "kimi-free":    { "description": "Kimi K2 (free) via OpenRouter",     "model": "openrouter/${OR_MODELS[0]}" },
    "qwen3-free":   { "description": "Qwen3 Coder (free) via OpenRouter", "model": "openrouter/${OR_MODELS[1]}" },
    "gemini-flash": { "description": "Gemini 2.5 Flash via OpenRouter",   "model": "openrouter/${OR_MODELS[2]}" },
    "yolo": {
      "description": "Apply diffs immediately; avoid confirmations; minimize chatter.",
      "system": "You are in YOLO mode. Make intelligent assumptions, ask only when blocking, apply diffs immediately without confirmation, summarize briefly, and proceed."
    }
  },
  "mcp": {
    "servers": $mcp_servers_json
  },
  "share": "manual"
}
EOF
  ok "Global config written: $CONFIG_FILE"
}

write_project_config() {
  local dir="$1"; [[ -d "$dir" ]] || die "Project directory not found: $dir"
  local file="$dir/opencode.json"
  local model="${PROJECT_MODEL_OVERRIDE:-$SMALL_MODEL}"
  cat >"$file"<<EOF
{
  "model": "$model"
}
EOF
  ok "Project config written: $file"
  if [[ ! -f "$dir/AGENTS.md" ]]; then
    cat >"$dir/AGENTS.md"<<'EOF'
# Project Agents
- @claude-pro   → Anthropic Pro (Sonnet 4) for critical coding/reviews.
- @qwen3-free   → Large-context refactors on free budget.
- @kimi-free    → Quick edits on free budget.
- @gemini-flash → Creative/ideation.
- @yolo         → Apply diffs immediately; minimal confirmations.
EOF
    ok "Created $dir/AGENTS.md"
  fi
}

########################################
# AUTH
########################################
ensure_env_exports() {
  export_env OPENROUTER_API_KEY "$OPENROUTER_API_KEY"
  export_env TAVILY_API_KEY "$TAVILY_API_KEY"
  export_env OPENAI_API_KEY "$OPENAI_API_KEY"
}
ensure_openrouter_auth() {
  if opencode auth list 2>/dev/null | grep -qi "OpenRouter api"; then
    ok "OpenRouter credential already visible to opencode"
  else
    ok "OpenRouter key provided via environment; opencode will use it."
  fi
}
ensure_anthropic_oauth() {
  if opencode auth list 2>/dev/null | grep -qi "Anthropic oauth"; then
    ok "Anthropic OAuth present (Pro/Max billing)"
  else
    log "Opening interactive Anthropic OAuth login…"
    opencode auth login   # select: Anthropic → Claude Pro/Max
  fi
}

########################################
# VALIDATION
########################################
validate_models() {
  if opencode models >/dev/null 2>&1; then ok "Models available (run 'opencode models' to list)."; else warn "Could not list models now; check network/OAuth."; fi
}

########################################
# CLI DEFAULTS (YOLO wrapper)
########################################
install_cli_defaults() {
  local rc; rc="$(shell_rc)"
  # Default: make 'opencode' run with @yolo
  if ! grep -q "^opencode()" "$rc" 2>/dev/null; then
cat >>"$rc" <<'EOSH'
# --- OpenCode defaults ---
# Default to YOLO agentic mode
opencode() {
  command opencode -a yolo "$@"
}
# Regular (non-YOLO) agentic mode
opencode-std() {
  command opencode "$@"
}
# -------------------------
EOSH
    echo "✅ Shell wrappers added in $rc (open a new shell or: source \"$rc\")"
  else
    echo "✅ Shell wrappers already present in $rc"
  fi
}

########################################
# MAIN
########################################
main() {
  if is_macos; then mac_prep; elif is_ubuntu; then ubuntu_prep; else warn "Unknown OS; skipping system package prep"; fi
  ensure_opencode

  install_mcps
  maybe_install_gpt_researcher

  write_global_config
  install_cli_defaults

  case "$DO_AUTH" in
    yes|auto) ensure_env_exports; ensure_openrouter_auth; ensure_anthropic_oauth ;;
    no) warn "--auth no: skipping auth steps";;
    *) die "Invalid --auth value: $DO_AUTH";;
  esac

  if [[ "$SCOPE" == "project" ]]; then write_project_config "${PROJECT_DIR:-$PWD}"; fi

  validate_models

  ok "Setup complete."
  log "Usage:"
  log "  YOLO default:       opencode        (uses @yolo agent)"
  log "  Regular agentic:    opencode-std"
  log "  Per-project model:  PROJECT_MODEL_OVERRIDE=\"openrouter/qwen/qwen3-coder:free\" $0 --project"
}

main "$@"
