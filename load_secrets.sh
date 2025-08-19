#!/bin/bash
# Universal Secrets Loader - Works for ALL projects
# Usage: source load_secrets.sh

# Load secrets from universal location OUTSIDE dev folder
SECRETS_FILE="$HOME/.secrets/atlas.env"

if [ -f "$SECRETS_FILE" ]; then
    echo "🔐 Loading secrets from $SECRETS_FILE..."
    source "$SECRETS_FILE"
    echo "✅ Secrets loaded successfully"
    echo "✅ Using model: $MODEL"
    echo "✅ OpenRouter API key: ${OPENROUTER_API_KEY:0:20}..."
    echo "✅ Firecrawl API key: ${FIRECRAWL_API_KEY:0:15}..."
else
    echo "❌ Secrets file not found: $SECRETS_FILE"
    echo ""
    echo "📋 To set up universal secrets:"
    echo "1. mkdir -p ~/.secrets"
    echo "2. Create ~/.secrets/atlas.env with your API keys"
    echo "3. chmod 600 ~/.secrets/atlas.env"
    echo "4. Run: source load_secrets.sh"
    exit 1
fi