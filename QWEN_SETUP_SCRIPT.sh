#!/bin/bash
# Qwen-Coder Setup Script for Atlas Development
# Run this before starting autonomous development

echo "🤖 Setting up Qwen-Coder for Atlas development..."

# Ensure we're in the right directory
cd /home/ubuntu/dev/atlas || {
    echo "❌ Cannot find Atlas directory"
    echo "💡 Run from: /home/ubuntu/dev/atlas"
    exit 1
}

# Install Qwen-Code CLI if not present
if ! command -v qwen &> /dev/null; then
    echo "📦 Installing Qwen-Code CLI..."
    npm install -g @qwen-code/qwen-code@latest || {
        echo "⚠️  NPM installation failed, continuing..."
    }
fi

# Run startup to check system status
echo "📊 Checking Atlas status..."
./start_work.sh || {
    echo "⚠️  Startup script failed, but continuing..."
}

# Display current status
echo ""
echo "🎯 Atlas Development Environment Ready"
echo "=" * 50

# Show key information for the AI
echo "📁 Current Directory: $(pwd)"
echo "🐍 Python: $(python3 --version 2>/dev/null || echo 'Not found')"
echo "📦 Node: $(node --version 2>/dev/null || echo 'Not found')"
echo "🔧 Git Branch: $(git branch --show-current 2>/dev/null || echo 'Unknown')"

# Check if background service is running
BG_PID=$(ps aux | grep atlas_background_service.py | grep -v grep | awk '{print $2}' | head -1)
if [ ! -z "$BG_PID" ]; then
    echo "🔄 Background Service: Running (PID $BG_PID)"
else
    echo "❌ Background Service: Not running"
fi

# Show file counts
ARTICLES=$(find output/articles/metadata -name "*.json" 2>/dev/null | wc -l)
HTML_FILES=$(find inputs/saved_html -name "*.html" 2>/dev/null | wc -l)
echo "📊 Content: $ARTICLES articles processed, $HTML_FILES HTML files remaining"

echo ""
echo "📋 Next Steps for Qwen-Coder:"
echo "1. Read QWEN_CODER_INSTRUCTIONS.md thoroughly"
echo "2. Study CLAUDE.md for project context"
echo "3. Review docs/specs/ for implementation details"
echo "4. Start with Block 7.1: Advanced Siri Shortcuts"
echo ""
echo "🚀 Ready for autonomous development!"
echo "=" * 50