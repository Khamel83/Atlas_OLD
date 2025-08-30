#!/bin/bash

# Atlas One-Command Installer
# Gets Atlas running in under 5 minutes

set -e  # Exit on any error

echo "🚀 Atlas One-Command Installer"
echo "=============================="
echo ""

# Check system requirements
echo "🔍 Checking system requirements..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+ first."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED="3.8"

if [ "$(printf '%s\n' "$REQUIRED" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED" ]; then 
    echo "❌ Python $PYTHON_VERSION found. Requires Python $REQUIRED or higher."
    exit 1
fi

echo "✅ Python $PYTHON_VERSION found"

# Check disk space
AVAILABLE=$(df . | awk 'NR==2{print $4}')
REQUIRED_KB=2097152  # 2GB in KB

if [ "$AVAILABLE" -lt "$REQUIRED_KB" ]; then
    echo "❌ Insufficient disk space. Need 2GB+, have $(($AVAILABLE/1024))MB"
    exit 1
fi

echo "✅ Sufficient disk space available"

# Check if we're in atlas directory
if [ ! -f "CLAUDE.md" ] || [ ! -f "atlas_status.py" ]; then
    echo "❌ Run this script from the Atlas root directory"
    exit 1
fi

echo "✅ Atlas directory confirmed"
echo ""

# Create virtual environment
echo "🐍 Setting up Python environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment exists"
fi

# Activate and install requirements
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1

# Install main requirements
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt > /dev/null 2>&1
    echo "✅ Main dependencies installed"
fi

# Copy environment template
echo "⚙️ Setting up configuration..."
if [ ! -f ".env" ]; then
    if [ -f "development/configs/env.template" ]; then
        cp development/configs/env.template .env
        echo "✅ Environment file created from template"
    else
        echo "⚠️  No .env template found - you may need to configure manually"
    fi
else
    echo "✅ Environment file exists"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs data input output backups
echo "✅ Directories created"

# Test the installation
echo ""
echo "🧪 Testing installation..."

if ./venv/bin/python atlas_status.py --help > /dev/null 2>&1; then
    echo "✅ Atlas status command works"
else
    echo "❌ Atlas status test failed"
    exit 1
fi

if ./venv/bin/python -c "from helpers.config import load_config; print('Config OK')" > /dev/null 2>&1; then
    echo "✅ Configuration loading works"
else
    echo "❌ Configuration test failed" 
    exit 1
fi

# Test core modules
if ./venv/bin/python -c "import ask.recall.recall_engine; print('Ask modules OK')" > /dev/null 2>&1; then
    echo "✅ Cognitive modules accessible"
else
    echo "❌ Cognitive modules test failed"
    exit 1
fi

echo ""
echo "🎉 Installation Complete!"
echo "======================="
echo ""
echo "✅ Atlas is ready to use!"
echo ""
echo "📋 Next steps:"
echo "   1. Start Atlas:     ./start_work.sh"
echo "   2. Check status:    ./venv/bin/python atlas_status.py"  
echo "   3. Open dashboard:  http://localhost:8000/ask/html"
echo "   4. Install shortcuts: cd shortcuts && ./install_shortcuts.sh"
echo ""
echo "📖 See QUICK_START_GUIDE.md for detailed next steps"
echo ""
echo "🎊 Welcome to Atlas - Your AI Knowledge System!"