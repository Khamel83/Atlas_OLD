# Atlas Installation Guide

Complete installation and setup guide for the Atlas content processing and search system.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Quick Installation](#quick-installation)  
3. [Detailed Setup](#detailed-setup)
4. [Configuration](#configuration)
5. [First Run](#first-run)
6. [Verification](#verification)
7. [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements
- **Operating System**: Linux (Ubuntu 20.04+), macOS (10.15+), Windows 10+ (with WSL2)
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 10GB free space minimum, 50GB+ for large collections
- **Network**: Internet connection for content fetching

### Recommended Requirements
- **RAM**: 16GB for optimal performance
- **Storage**: SSD with 100GB+ free space
- **CPU**: Multi-core processor for concurrent processing
- **Network**: Stable broadband connection

### Dependencies
Atlas will automatically install required Python packages, but you may need:
- `sqlite3` (usually included with Python)
- `curl` (for testing API endpoints)
- `git` (for cloning the repository)

## Quick Installation

### One-Command Setup

```bash
# Clone and setup Atlas
git clone <repository-url> atlas
cd atlas
cp env.template .env
pip install -r requirements.txt
./start_work.sh
```

This will:
1. Clone the Atlas repository
2. Copy the configuration template
3. Install all Python dependencies
4. Start the Atlas system with default settings

### Docker Installation (Alternative)

```bash
# Using Docker Compose
git clone <repository-url> atlas
cd atlas
cp env.template .env
docker-compose up -d
```

## Detailed Setup

### Step 1: Clone Repository

```bash
# Clone from GitHub (replace with actual URL)
git clone https://github.com/your-org/atlas.git
cd atlas

# Or download and extract ZIP file
wget https://github.com/your-org/atlas/archive/main.zip
unzip main.zip
cd atlas-main
```

### Step 2: Python Environment

#### Option A: Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv atlas-env
source atlas-env/bin/activate  # Linux/Mac
# atlas-env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

#### Option B: System-wide Installation
```bash
# Install directly to system Python
pip3 install -r requirements.txt
```

#### Option C: Conda Environment
```bash
# Create conda environment
conda create -n atlas python=3.9
conda activate atlas
pip install -r requirements.txt
```

### Step 3: Configuration

```bash
# Copy configuration template
cp env.template .env

# Edit configuration (see Configuration section below)
nano .env
```

### Step 4: Database Setup

```bash
# Initialize databases (automatic on first run)
python helpers/simple_database.py

# Or run setup script
python scripts/setup_databases.py
```

### Step 5: Verify Installation

```bash
# Test core components
python -c "import sqlite3; print('SQLite OK')"
python -c "from helpers.config import load_config; print('Config OK')"
python atlas_status.py
```

## Configuration

### Environment Variables

Edit the `.env` file to customize Atlas for your environment:

#### Basic Configuration
```bash
# System Settings
API_HOST=0.0.0.0                    # API server host (0.0.0.0 for all interfaces)
API_PORT=8000                       # API server port
DEBUG_MODE=false                    # Enable debug logging

# Database Configuration  
DATABASE_URL=sqlite:///atlas.db     # Main database path
SEARCH_DB_URL=sqlite:///atlas_search.db  # Search database path

# Processing Settings
MAX_CONCURRENT_DOWNLOADS=5          # Simultaneous downloads
RETRY_ATTEMPTS=3                    # Failed content retry attempts
PROCESSING_TIMEOUT=300              # Timeout in seconds
```

#### Content Processing
```bash
# Article Processing
ARTICLE_TIMEOUT=30                  # Article fetch timeout
ENABLE_PAYWALL_BYPASS=false         # Attempt paywall bypass (use carefully)
USER_AGENT_ROTATION=true            # Rotate user agents

# Document Processing
MAX_DOCUMENT_SIZE=52428800          # 50MB max document size
EXTRACT_IMAGES=false                # Extract images from documents
SUPPORTED_FORMATS=pdf,txt,md,docx   # Supported document formats

# Podcast Processing
ENABLE_TRANSCRIPT_FIRST=true        # Prioritize transcripts over audio
MAX_PODCAST_SIZE=104857600          # 100MB max podcast file
TRANSCRIPT_LANGUAGE=en              # Primary transcript language
```

#### Search & Analytics
```bash
# Search Engine
SEARCH_RESULTS_LIMIT=100            # Maximum search results
ENABLE_FUZZY_SEARCH=true            # Enable approximate matching
SEARCH_CACHE_SIZE=1000              # Search result cache size

# Analytics
ENABLE_ANALYTICS=true               # Collect usage analytics
ANALYTICS_RETENTION_DAYS=365        # Keep analytics for 1 year
```

#### External Services (Optional)
```bash
# YouTube (for video processing)
YOUTUBE_API_KEY=your_youtube_key    # Optional: YouTube API key

# OpenAI (for enhanced processing)
OPENAI_API_KEY=your_openai_key      # Optional: OpenAI API key

# Proxy Settings (if needed)
HTTP_PROXY=http://proxy:8080        # HTTP proxy
HTTPS_PROXY=https://proxy:8080      # HTTPS proxy
```

### Content Source Configuration

#### Podcast Configuration
Edit `config/podcasts_full.csv` to add podcast feeds:

```csv
name,feed_url,category,priority,transcript_source
TechNews Daily,https://feeds.example.com/technews,technology,high,rss
Science Weekly,https://feeds.example.com/science,science,medium,website
```

#### Content Directories
Create input directories for different content types:

```bash
mkdir -p inputs/{articles,documents,podcasts,youtube}
mkdir -p logs
mkdir -p output
mkdir -p backups
```

### Advanced Configuration

#### Database Optimization
```bash
# SQLite Performance Settings
SQLITE_CACHE_SIZE=2000              # Cache size in KB
SQLITE_SYNCHRONOUS=1                # Sync mode (0=off, 1=normal, 2=full)
SQLITE_JOURNAL_MODE=WAL             # Journal mode (DELETE, TRUNCATE, WAL)
```

#### Logging Configuration
```bash
# Logging Settings
LOG_LEVEL=INFO                      # DEBUG, INFO, WARNING, ERROR
LOG_MAX_SIZE=10485760               # 10MB max log file size
LOG_BACKUP_COUNT=5                  # Keep 5 log file backups
ENABLE_FILE_LOGGING=true            # Log to files
ENABLE_CONSOLE_LOGGING=true         # Log to console
```

## First Run

### Start Atlas

#### Option 1: Quick Start (Recommended)
```bash
./start_work.sh
```

This script will:
- Check system requirements
- Start all necessary services
- Show system status
- Provide helpful next steps

#### Option 2: Manual Start
```bash
# Start API server
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload &

# Start background service
python atlas_background_service.py &

# Check status
python atlas_status.py
```

#### Option 3: Service Mode
```bash
# Install as system service (Linux)
sudo ./scripts/setup_systemd_service.sh
sudo systemctl start atlas
sudo systemctl enable atlas
```

### Initial Content

Add some initial content to test the system:

```bash
# Add some article URLs
echo "https://example.com/sample-article" > inputs/articles.txt
echo "https://news.ycombinator.com" >> inputs/articles.txt

# Add a document (if you have one)
cp ~/Documents/sample.pdf inputs/

# Add YouTube video (optional)
echo "https://www.youtube.com/watch?v=dQw4w9WgXcQ" > inputs/youtube.txt
```

### Wait for Processing

The background service will automatically process new content every 30 minutes, or you can trigger immediate processing:

```bash
# Process all content immediately
python run.py --all

# Process specific types
python process_articles.py
python process_documents.py
```

## Verification

### Check System Status

```bash
# Comprehensive status check
python atlas_status.py --detailed

# API health check
curl http://localhost:8000/api/v1/health

# Check database
sqlite3 atlas.db ".tables"
```

### Test Search

```bash
# Test search API
curl "http://localhost:8000/api/v1/search/?q=test"

# Test dashboard
open http://localhost:8000/api/v1/dashboard/
# or visit in browser: http://localhost:8000/api/v1/dashboard/
```

### Verify Processing

```bash
# Check processed content
python -c "
from helpers.simple_database import SimpleDatabase
db = SimpleDatabase()
print('Total content items:', len(db.get_all_content()))
"

# Check search index
python -c "
from helpers.enhanced_search_engine import EnhancedSearchEngine
search = EnhancedSearchEngine()
print('Indexed items:', len(search.search('', limit=1000)))
"
```

### Test Core Features

```bash
# Run test suite
python -m pytest tests/ -v

# Run specific integration tests
python tests/test_enhanced_search_integration.py
python tests/test_analytics_dashboard.py
```

## Troubleshooting

### Installation Issues

#### Python Version Error
```bash
# Check Python version
python --version
python3 --version

# If version is too old, install newer Python
# Ubuntu/Debian:
sudo apt update && sudo apt install python3.9

# macOS with Homebrew:
brew install python@3.9
```

#### Dependencies Installation Failed
```bash
# Update pip first
python -m pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt -v

# If specific package fails, install individually
pip install fastapi uvicorn sqlite3
```

#### Permission Errors
```bash
# Fix file permissions
chmod +x start_work.sh
chmod +x scripts/*.sh

# Create necessary directories
mkdir -p logs output inputs backups

# Fix ownership (Linux)
sudo chown -R $USER:$USER .
```

### Runtime Issues

#### Port Already in Use
```bash
# Check what's using port 8000
sudo netstat -tlnp | grep 8000
sudo lsof -i :8000

# Kill process using port
sudo kill $(sudo lsof -ti:8000)

# Or use different port in .env
echo "API_PORT=8080" >> .env
```

#### Database Errors
```bash
# Check database integrity
sqlite3 atlas.db "PRAGMA integrity_check"

# Rebuild database if corrupted
mv atlas.db atlas.db.backup
python helpers/simple_database.py

# Restore from backup if available
cp backups/atlas_*.db atlas.db
```

#### Content Not Processing
```bash
# Check background service
ps aux | grep atlas_background_service

# Check logs
tail -f logs/atlas.log
tail -f logs/processing.log

# Manual processing with debug
DEBUG_MODE=true python run.py --all
```

### Performance Issues

#### Slow Processing
```bash
# Reduce concurrent downloads
echo "MAX_CONCURRENT_DOWNLOADS=2" >> .env

# Check system resources
top
df -h
free -h

# Optimize database
python scripts/optimize_database.py
```

#### High Memory Usage
```bash
# Monitor memory usage
python -c "
import psutil
print('Memory usage:', psutil.virtual_memory())
print('Atlas processes:')
for p in psutil.process_iter(['pid', 'name', 'memory_info']):
    if 'atlas' in p.info['name'].lower():
        print(p.info)
"

# Restart services to clear memory
./scripts/start_atlas_service.sh restart
```

### Getting Help

1. **Check logs**: `ls -la logs/` and examine recent log files
2. **Run diagnostics**: `python atlas_status.py --detailed`
3. **Test components**: Run individual test files in `tests/`
4. **Check GitHub issues**: Search existing issues for similar problems
5. **Create issue**: Provide logs and system information when reporting problems

### Uninstallation

To completely remove Atlas:

```bash
# Stop all services
./scripts/start_atlas_service.sh stop
pkill -f atlas

# Remove virtual environment (if used)
deactivate
rm -rf atlas-env/

# Remove Atlas directory
cd ..
rm -rf atlas/

# Remove system service (if installed)
sudo systemctl stop atlas
sudo systemctl disable atlas
sudo rm /etc/systemd/system/atlas.service
```

## Next Steps

After successful installation:

1. **Add your content**: Place URLs in `inputs/articles.txt` and documents in `inputs/`
2. **Configure podcasts**: Edit `config/podcasts_full.csv` with your podcast feeds
3. **Explore the dashboard**: Visit `http://localhost:8000/api/v1/dashboard/`
4. **Try the search**: Test search functionality with your content
5. **Read the user guide**: See `docs/USER_GUIDE.md` for detailed usage instructions

Welcome to Atlas! Your personal content processing and search system is ready to use.