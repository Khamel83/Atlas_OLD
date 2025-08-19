#!/bin/bash
# Load secrets from universal location OUTSIDE project folder
# Usage: source load_secrets.sh

SECRETS_FILE="$HOME/.secrets/atlas.env"

if [ -f "$SECRETS_FILE" ]; then
    echo "🔐 Loading secrets from $SECRETS_FILE..."
    source "$SECRETS_FILE"
    echo "✅ Secrets loaded successfully for atlas"
    
    # Show confirmation of loaded keys (masked for security)
    for var in OPENROUTER_API_KEY FIRECRAWL_API_KEY DATABASE_URL API_KEY MODEL; do
        if [ ! -z "${!var}" ] && [ "${!var}" != "your_*" ]; then
            echo "✅ $var: ${!var:0:15}..."
        fi
    done
else
    echo "❌ Secrets file not found: $SECRETS_FILE"
    echo ""
    echo "📋 To set up secrets:"
    echo "1. Edit: $SECRETS_FILE"
    echo "2. Add: export API_KEY=\"your-real-key-here\""
    echo "3. Run: source load_secrets.sh"
    exit 1
fi
