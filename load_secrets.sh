#!/bin/bash
# Load secrets from secure file
# Usage: source load_secrets.sh

if [ -f .env.secure ]; then
    echo "Loading secure environment variables..."
    source .env.secure
    echo "✅ Secrets loaded successfully"
    echo "✅ Using model: $MODEL"
    echo "✅ OpenRouter API key: ${OPENROUTER_API_KEY:0:20}..."
    echo "✅ Firecrawl API key: ${FIRECRAWL_API_KEY:0:15}..."
else
    echo "❌ .env.secure file not found!"
    echo "Create .env.secure with your API keys first"
    exit 1
fi