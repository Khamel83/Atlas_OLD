#!/bin/bash
# Atlas Standard Startup Script
# One command to start everything

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🎯 Atlas Standard Startup${NC}"
echo "================================="

# Get current directory
ATLAS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ATLAS_DIR"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️ Virtual environment not found. Creating...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    echo -e "${GREEN}✅ Virtual environment found${NC}"
    source venv/bin/activate
fi

# Check configuration
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠️ Configuration file not found. Creating from template...${NC}"
    if [ -f "env.template" ]; then
        cp env.template .env
        echo -e "${YELLOW}📝 Please edit .env file with your API keys${NC}"
    else
        echo -e "${RED}❌ No env.template found. Please create .env manually${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✅ Configuration found${NC}"
fi

# Stop any existing services
echo -e "${BLUE}🛑 Stopping existing services...${NC}"
python3 atlas_service_manager.py stop >/dev/null 2>&1 || true

# Start robust service manager
echo -e "${BLUE}🚀 Starting Atlas services...${NC}"
python3 atlas_service_manager.py start --daemon &
MANAGER_PID=$!

# Wait a moment for services to start
sleep 5

# Check system health
echo -e "${BLUE}🔍 Checking system health...${NC}"
python3 atlas_monitor.py

# Show status summary
echo ""
echo -e "${GREEN}✅ Atlas startup complete!${NC}"
echo ""
echo -e "${BLUE}📋 What's running:${NC}"
echo "  • Smart dispatcher API server"
echo "  • Background content processing"  
echo "  • Health monitoring with auto-restart"
echo "  • Podcast transcript discovery"
echo ""
echo -e "${BLUE}🎯 Usage:${NC}"
echo "  python3 atlas_monitor.py        # Check status anytime"
echo "  python3 atlas_service_manager.py status  # Detailed service info"
echo ""
echo -e "${YELLOW}⚠️  Note: Atlas is running but won't auto-start on reboot${NC}"
echo -e "${BLUE}🛠️  To install as system service (like PiHole):${NC}"
echo "  ./install_systemd_service.sh    # Makes Atlas start on boot!"
echo ""
echo -e "${BLUE}🔄 Services will auto-restart if they fail${NC}"
echo -e "${BLUE}📊 Mac Mini jobs queue automatically when content arrives${NC}"
echo ""
echo -e "${GREEN}Atlas is ready for production use!${NC}"