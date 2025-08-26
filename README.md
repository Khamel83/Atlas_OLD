# Atlas — Personal Knowledge System

Atlas is a production-ready personal knowledge system for content ingestion, processing, and intelligent querying. Features include:
- Multi-source content ingestion (articles, podcasts, YouTube, documents)
- Smart Mac Mini worker integration for heavy processing
- Cognitive API for advanced content interaction
- Background services with health monitoring

## Zero-Config Quick Start

```bash
# Single command setup from fresh clone
./start_work.sh

# OR enhanced startup with monitoring
./start_atlas.sh
```

This will:
1. Create virtual environment and install dependencies
2. Initialize database with proper schema
3. Create configuration files from templates
4. Start all Atlas services
5. Verify system health

**That's it!** Atlas is now running at http://localhost:8000

## Core Components

### API Endpoints
- **Health**: `GET /health` - System status
- **Content**: `GET /api/v1/content/` - Search and browse content
- **Cognitive**: `GET /api/v1/cognitive/surface` - AI-powered content recommendations
- **Worker**: `POST /api/v1/worker/jobs` - Mac Mini job management

### Key Files
- `start_work.sh` — Zero-config bootstrap script
- `tasks.md` — Current development roadmap
- `CLAUDE.md` — Complete system documentation
- `helpers/` — Core processing modules
- `api/` — FastAPI server implementation

## Architecture

### Smart Content Processing
- **Local Processing**: Articles, small podcasts, documents processed on Atlas
- **Mac Mini Offload**: Heavy transcription, large media files queued for worker
- **Fallback Graceful**: System continues when Mac Mini offline

### Background Services
- **Auto-ingestion**: Monitors inputs/ directory for new content
- **Health monitoring**: Auto-restart failed services
- **Queue management**: Smart job dispatching and retry logic

## Current Status ✅

**PRODUCTION READY** - All core systems operational:
- ✅ **API Endpoints**: 4/4 cognitive endpoints functional
- ✅ **Background Services**: Single stable service (no process leaks)
- ✅ **Mac Mini Integration**: Job queue and worker system operational
- ✅ **Database**: Auto-initialization with proper schema
- ✅ **Zero-Config Setup**: Fresh clone → working system in one command

**Recent Completions**:
- Block 1: API endpoint repair (B1T1-B1T6) ✅
- Block 2: Background service crisis fix (B2T1-B2T6) ✅  
- Block 3: Mac Mini worker integration (B3T1-B3T2) ✅
- Block 4: Bootstrap script enhancement (B4T1) ✅

**In Progress**: Documentation accuracy audit, integration testing

See `tasks.md` for detailed completion status and next steps.

## Configuration

After running the setup script, edit `.env` with your API keys:

```bash
# Required for content processing
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here

# Optional but recommended
NYT_EMAIL=your_nyt_email
NYT_PASSWORD=your_nyt_password
WSJ_EMAIL=your_wsj_email  
WSJ_PASSWORD=your_wsj_password
```

## Usage

### Adding Content
Place content files in `inputs/` directory:
- `articles.txt` - One URL per line
- `youtube.txt` - YouTube URLs  
- `podcasts.csv` - Podcast feeds
- Any `.txt` or `.csv` files with URLs

Content is automatically processed every 30 minutes.

### Monitoring
```bash
# Check system status (if available)
python3 atlas_monitor.py

# View service logs
./scripts/atlas_service.sh logs

# Check API health
curl http://localhost:8000/health
```

### Mac Mini Setup
On your Mac Mini worker:
```bash
# Copy mac_mini_client.py to Mac Mini
python3 mac_mini_client.py --capabilities transcribe_youtube,transcribe_podcast

# Runs continuously, polling Atlas for jobs
```

## Development

See `tasks.md` for current development roadmap and `CLAUDE.md` for comprehensive system documentation.

## Troubleshooting

1. **Service won't start**: Check `logs/` directory for error details
2. **API not responding**: Ensure port 8000 is available 
3. **Database errors**: Delete `atlas.db` and restart to recreate
4. **Permission errors**: Run `chmod +x *.sh` to fix script permissions

For detailed troubleshooting, see `CLAUDE.md` or check `tasks.md` for known issues.