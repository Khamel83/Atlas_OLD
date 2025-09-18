#!/bin/bash
# Atlas Simple Startup Script

echo "🚀 Starting Atlas - Your Digital Filing Cabinet"
echo "=============================================="

# Check if we're in the right directory
if [ ! -f "web_interface.py" ]; then
    echo "❌ Error: Please run this script from the Atlas directory"
    exit 1
fi

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
fi

# Check if required packages are installed
echo "🔍 Checking dependencies..."
python3 -c "import fastapi, uvicorn, sqlite3" 2>/dev/null || {
    echo "❌ Missing dependencies. Installing..."
    pip install -r requirements.txt
}

# Start Atlas web interface
echo "🌐 Starting Atlas web interface on port 7444..."
echo "📱 Atlas will be available at: https://atlas.khamel.com"
echo "🏠 Or locally at: http://localhost:7444"
echo ""
echo "Press Ctrl+C to stop Atlas"
echo ""

python3 web_interface.py