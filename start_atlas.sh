#!/bin/bash
# Atlas Zero-Config Startup Script
# Complete setup from fresh clone

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

# Check and setup Python environment
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️ Virtual environment not found. Creating...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    echo -e "${BLUE}📦 Installing dependencies...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}✅ Dependencies installed${NC}"
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

# Initialize database if needed
echo -e "${BLUE}🗄️ Setting up database...${NC}"
if [ ! -f "atlas.db" ]; then
    echo -e "${YELLOW}⚠️ Database not found. Creating...${NC}"
    python3 -c "from helpers.simple_database import SimpleDatabase; db = SimpleDatabase(); print('Database initialized')"
    echo -e "${GREEN}✅ Database created${NC}"
else
    echo -e "${GREEN}✅ Database found${NC}"
fi

# Stop any existing services
echo -e "${BLUE}🛑 Stopping existing services...${NC}"
if [ -f "scripts/atlas_service.sh" ]; then
    ./scripts/atlas_service.sh stop >/dev/null 2>&1 || true
fi
pkill -f "atlas" >/dev/null 2>&1 || true

# Start Atlas service
echo -e "${BLUE}🚀 Starting Atlas services...${NC}"
if [ -f "scripts/atlas_service.sh" ]; then
    ./scripts/atlas_service.sh start
else
    echo -e "${RED}❌ Service manager not found${NC}"
    exit 1
fi

# Wait a moment for services to start
sleep 5

# Check system health
echo -e "${BLUE}🔍 Checking system health...${NC}"
if [ -f "atlas_monitor.py" ]; then
    python3 atlas_monitor.py
else
    echo -e "${YELLOW}⚠️ Monitor not found, checking processes...${NC}"
    ps aux | grep atlas | grep -v grep || echo "No Atlas processes found"
fi

# Show status summary
echo ""
echo -e "${GREEN}✅ Atlas startup complete!${NC}"
echo ""
echo -e "${BLUE}📋 What's running:${NC}"
echo "  • Smart dispatcher API server"
echo "  • Background content processing (articles, podcasts, transcripts)"  
echo "  • Health monitoring with auto-restart"
echo "  • Unified transcript discovery (ATP + all podcasts)"
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