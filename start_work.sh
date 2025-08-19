#!/bin/bash
# Atlas Development Startup Script
# Never fails, always gets you working quickly

echo "🚀 Starting Atlas Development Session..."

# Change to Atlas directory
cd /home/ubuntu/dev/atlas 2>/dev/null || {
    echo "❌ Cannot find Atlas directory"
    echo "💡 Run from: /home/ubuntu/dev/atlas"
    exit 1
}

# Run the status dashboard
echo "📊 Checking Atlas status..."
python3 atlas_status.py --dev 2>/dev/null || {
    echo "⚠️  Status script failed, but continuing..."
    echo "✅ You can still work normally!"
}

# Load secrets if available
echo ""
echo "🔐 Loading secrets..."
if [ -f "load_secrets.sh" ]; then
    source load_secrets.sh 2>/dev/null || {
        echo "⚠️  Secrets loading failed"
        echo "💡 Run manually: source load_secrets.sh"
    }
else
    echo "⚠️  No secrets loader found"
    echo "💡 Run: bash /home/ubuntu/setup_secrets.sh"
fi

# Activate virtual environment if available
echo ""
echo "🐍 Activating virtual environment..."
if [ -d "atlas_venv" ]; then
    source atlas_venv/bin/activate 2>/dev/null || {
        echo "⚠️  Virtual env failed to activate"
        echo "💡 Run manually: source atlas_venv/bin/activate"
    }
    echo "✅ Virtual environment active"
else
    echo "⚠️  No virtual environment found"
    echo "💡 Create with: python3 -m venv atlas_venv"
fi

echo ""
echo "🎯 Ready for Atlas development!"
echo "💡 Common commands:"
echo "   python run.py --all              # Full processing"
echo "   python atlas_status.py          # Quick status"  
echo "   python atlas_status.py --detailed # Detailed status"
echo ""