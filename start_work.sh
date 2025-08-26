#!/bin/bash
# Atlas Zero-Config Bootstrap Script
# Single command from fresh clone to working system

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Atlas Zero-Config Bootstrap${NC}"
echo "==================================="

# Get current directory
ATLAS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ATLAS_DIR"

# Check system requirements
echo -e "${BLUE}🔍 Checking system requirements...${NC}"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found. Please install python3${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python 3 found${NC}"

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo -e "${YELLOW}⚠️ pip3 not found. Installing...${NC}"
    sudo apt update && sudo apt install -y python3-pip
fi
echo -e "${GREEN}✅ pip3 found${NC}"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️ Virtual environment not found. Creating...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${GREEN}✅ Virtual environment found${NC}"
fi

# Activate virtual environment
echo -e "${BLUE}📦 Activating virtual environment...${NC}"
source venv/bin/activate

# Install dependencies
if [ ! -f "venv/.installed" ]; then
    echo -e "${BLUE}📦 Installing dependencies...${NC}"
    pip install -r requirements.txt
    touch venv/.installed
    echo -e "${GREEN}✅ Dependencies installed${NC}"
else
    echo -e "${GREEN}✅ Dependencies already installed${NC}"
fi

# Setup configuration
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠️ Configuration file not found. Creating from template...${NC}"
    if [ -f "env.template" ]; then
        cp env.template .env
        echo -e "${GREEN}✅ Configuration file created${NC}"
        echo -e "${YELLOW}📝 Please edit .env file with your API keys${NC}"
    else
        echo -e "${RED}❌ No env.template found. Creating minimal .env${NC}"
        cat > .env << EOF
# Atlas Configuration
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here

# Database
DATABASE_PATH=atlas.db

# API Settings
API_HOST=0.0.0.0
API_PORT=8000

# Processing Settings
MAX_CONCURRENT_JOBS=3
JOB_TIMEOUT=3600
EOF
        echo -e "${GREEN}✅ Minimal .env created${NC}"
    fi
else
    echo -e "${GREEN}✅ Configuration found${NC}"
fi

# Initialize database
echo -e "${BLUE}🗄️ Setting up database...${NC}"
if [ ! -f "atlas.db" ]; then
    echo -e "${YELLOW}⚠️ Database not found. Creating...${NC}"
    python3 -c "
from helpers.simple_database import SimpleDatabase
try:
    db = SimpleDatabase()
    print('✅ Database initialized')
except Exception as e:
    print(f'❌ Database setup failed: {e}')
    exit(1)
"
    echo -e "${GREEN}✅ Database created${NC}"
else
    echo -e "${GREEN}✅ Database found${NC}"
fi

# Create directories
echo -e "${BLUE}📁 Creating directories...${NC}"
mkdir -p logs output inputs evaluation retries docs/reports
echo -e "${GREEN}✅ Directories created${NC}"

# Stop any existing services
echo -e "${BLUE}🛑 Stopping existing services...${NC}"
if [ -f "scripts/atlas_service.sh" ]; then
    ./scripts/atlas_service.sh stop >/dev/null 2>&1 || true
fi
pkill -f "atlas" >/dev/null 2>&1 || true
echo -e "${GREEN}✅ Existing services stopped${NC}"

# Start Atlas service
echo -e "${BLUE}🚀 Starting Atlas services...${NC}"
if [ -f "scripts/atlas_service.sh" ]; then
    ./scripts/atlas_service.sh start
    echo -e "${GREEN}✅ Atlas service started${NC}"
else
    echo -e "${YELLOW}⚠️ Service manager not found, starting manually...${NC}"
    nohup python3 run.py > logs/atlas.log 2>&1 &
    echo -e "${GREEN}✅ Atlas started manually${NC}"
fi

# Wait for services to start
sleep 5

# Test API connectivity
echo -e "${BLUE}🔍 Testing system health...${NC}"
if command -v curl &> /dev/null; then
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo -e "${GREEN}✅ API server responding${NC}"
    else
        echo -e "${YELLOW}⚠️ API server not responding (may take longer to start)${NC}"
    fi
else
    echo -e "${YELLOW}⚠️ curl not found, skipping API test${NC}"
fi

# Check processes
ATLAS_PROCESSES=$(ps aux | grep atlas | grep -v grep | wc -l)
if [ "$ATLAS_PROCESSES" -gt 0 ]; then
    echo -e "${GREEN}✅ $ATLAS_PROCESSES Atlas processes running${NC}"
else
    echo -e "${YELLOW}⚠️ No Atlas processes detected${NC}"
fi

# Success message
echo ""
echo -e "${GREEN}🎉 Atlas Bootstrap Complete!${NC}"
echo ""
echo -e "${BLUE}📋 What's ready:${NC}"
echo "  • Virtual environment activated"
echo "  • Dependencies installed"
echo "  • Database initialized"
echo "  • Configuration files created"
echo "  • Services started"
echo ""
echo -e "${BLUE}🎯 Next steps:${NC}"
echo "  1. Edit .env with your API keys"
echo "  2. Add content to inputs/ directory"
echo "  3. Run: python3 atlas_monitor.py (if available)"
echo "  4. Access API at: http://localhost:8000"
echo ""
echo -e "${GREEN}🚀 Atlas is ready for use!${NC}"