# Atlas Personal Knowledge Management System

> **🚀 Production-Ready Personal AI Assistant**  
> Transform any content into searchable, intelligent knowledge with automatic processing, semantic search, and AI-powered insights.

[![Atlas Reliability](https://img.shields.io/badge/reliability-24%2F7-green)](https://github.com/Khamel83/Atlas)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Live Demo](https://img.shields.io/badge/live_demo-atlas.khamel.com-blue)](https://atlas.khamel.com)

## ✨ What is Atlas?

Atlas is a **bulletproof personal knowledge management system** that automatically processes, indexes, and makes searchable any content you feed it:

- 📰 **Articles & Web Pages** - Save from any website with instant processing
- 🎙️ **Podcast Transcripts** - Automatic discovery and full-text search
- 🎬 **YouTube Videos** - API-based collection and transcript extraction
- 📧 **Email Archives** - Import and search your email history
- 📄 **Documents** - PDFs, text files, notes, and more
- 🧠 **AI Insights** - Semantic search, content recommendations, and intelligent analysis

**Perfect for**: Researchers, knowledge workers, students, content creators, and anyone who needs to organize and retrieve information efficiently.

> **🌟 Live Demo Available**: [atlas.khamel.com](https://atlas.khamel.com) - See Atlas dashboard with real content processing in action!

## 🎯 Key Features

### 🔍 **Intelligent Search & Discovery**
- **Semantic search** across all content types
- **Auto-categorization** with AI-powered tagging
- **Content recommendations** based on reading patterns
- **Full-text search** with advanced filtering

### 🤖 **AI-Powered Insights**
- **Socratic questioning** to deepen understanding
- **Pattern detection** across your knowledge base  
- **Automatic summaries** and key insights extraction
- **Content quality analysis** and improvement suggestions

### 🛡️ **Enterprise-Grade Reliability**
- **24/7 operation** with automatic recovery
- **Bulletproof process management** preventing memory leaks
- **Comprehensive monitoring** and alerting
- **Automatic backups** and corruption prevention

### 📱 **Cross-Platform Access**
- **Web dashboard** with modern, responsive UI
- **iOS shortcuts** for quick content capture
- **Browser extensions** for one-click saving
- **API access** for custom integrations

## 🚀 Quick Start (10 Minutes)

### 1. **Installation**
```bash
git clone https://github.com/Khamel83/Atlas.git
cd Atlas
./config/install_shortcuts.sh  # Complete setup
```

### 2. **Start Atlas**
```bash
python atlas_service_manager.py start --daemon
```

### 3. **Access Your Knowledge**
- **Web Dashboard**: http://localhost:7444
- **Mobile Interface**: http://localhost:7444/mobile  
- **API Documentation**: http://localhost:7444/docs
- **Live Demo**: https://atlas.khamel.com

### 4. **Add Content**
- **iOS**: "Hey Siri, save to Atlas" (after installing shortcuts)
- **Web**: Use the dashboard upload interface
- **API**: POST to `/api/v1/content/`

## 📊 System Status

Check system health anytime:
```bash
python atlas_status.py --detailed
```

**Real-time monitoring** available at: http://localhost:7444/monitoring

## 🏗️ Architecture

Atlas uses a **bulletproof microservices architecture**:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Interface │    │   FastAPI Server │    │  Background     │
│   Dashboard     │◄──►│   REST API       │◄──►│  Processing     │
│   Mobile UI     │    │   Authentication │    │  Queue Workers  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   SQLite + WAL   │
                       │   Full-text FTS  │  
                       │   Auto Backups   │
                       └──────────────────┘
```

### Core Components

- **atlas_service_manager.py** - Main service orchestrator with SystemD integration
- **atlas_status.py** - Health monitoring and system diagnostics
- **api/** - FastAPI REST services with authentication
- **web/** - Modern web dashboard and mobile interface
- **helpers/** - Core processing, search, and AI modules
- **scripts/** - Background workers and maintenance tasks

## 🔧 Configuration

Atlas uses environment-based configuration for security and flexibility:

```bash
cp .env.template .env
# Edit .env with your settings
```

### Key Settings

```env
# Database
ATLAS_DATABASE_PATH=/home/user/atlas/data/atlas.db

# API Configuration  
API_PORT=7444
API_HOST=0.0.0.0

# AI Services (optional)
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here

# Notifications
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
```

## 🧠 AI Features

Atlas includes six sophisticated AI modules:

1. **🔍 Proactive Search** - Surface relevant content automatically
2. **⏰ Temporal Analysis** - Track information over time  
3. **🤔 Socratic Questioning** - Generate thought-provoking questions
4. **🧩 Pattern Detection** - Find connections across content
5. **💡 Active Recall** - Spaced repetition for knowledge retention
6. **📊 Content Recommendations** - Suggest related and valuable content

Access via: http://localhost:7444/ask/

## 📱 iOS Integration

Install the complete iOS shortcuts package:

```bash
./config/install_shortcuts.sh
```

**Available Shortcuts:**
- 📝 "Save to Atlas" - Save current webpage or selection
- 🎙️ "Voice Note to Atlas" - Record and transcribe voice notes
- 📸 "Photo to Atlas" - OCR and save image text
- 🔍 "Search Atlas" - Voice search your knowledge base

## 🔒 Security & Privacy

- **Local-first** - All data stays on your machine
- **Encrypted storage** - Sensitive data protected at rest
- **Secure API** - JWT authentication with rate limiting  
- **Privacy-focused** - No external data transmission (unless explicitly configured)

## 🛠️ Development

### Running Tests
```bash
python -m pytest tests/ -v
```

### Development Mode
```bash
python atlas_service_manager.py start --dev
```

### Adding Custom Processors
```python
from helpers.content_processor import BaseProcessor

class CustomProcessor(BaseProcessor):
    def process(self, content):
        # Your custom processing logic
        return processed_content
```

## 📈 Monitoring & Observability

Atlas includes comprehensive monitoring:

- **📊 Real-time metrics** at `/metrics` (Prometheus format)
- **📝 Structured logging** with JSON format and rotation
- **🚨 Intelligent alerting** with pattern detection
- **📱 Telegram notifications** for critical events
- **📈 Performance dashboards** with trends and capacity planning

## 🔍 Source Discovery System

Atlas includes an intelligent **Source Discovery System** that continuously finds and processes unprocessed content from all your sources:

### **How It Works**
- **Automatic Discovery**: Every 2 hours, Atlas scans for unprocessed work
- **Multiple Sources**: Instapaper CSV exports, unprocessed podcast episodes, RSS feeds
- **Stage 0 Processing**: Discovered content enters the processing pipeline at stage 0
- **Unified Pipeline**: All content flows through the same 0-599 stage progression

### **Supported Sources**
- **📄 Instapaper CSV Exports**: Automatically processes uploaded CSV files from `uploads/` directory
- **🎙️ Podcast Episodes**: Finds episodes marked `processed=0` in the database
- **🔮 Future**: RSS feeds, YouTube channels, email archives, file watchers

### **Monitoring Discovery**
```bash
# Check discovery activity
tail -f logs/atlas_scheduler.log | grep "source inventory"

# View discovered items at stage 0
sqlite3 data/atlas.db "SELECT COUNT(*) FROM content WHERE metadata LIKE '%discovery_stage%0%';"

# Watch processing progress
tail -f logs/universal_queue.log | grep "✅ AI processing completed"
```

### **Manual Discovery**
```bash
# Test source discovery manually
python3 helpers/source_inventory.py

# Run discovery and view results
python3 -c "from helpers.source_inventory import discover_unprocessed_work; print(discover_unprocessed_work())"
```

### **Configuration**
The discovery system runs automatically via the Atlas Scheduler:
- **Interval**: Every 2 hours
- **Batch Limit**: 1000 items per discovery run
- **Integration**: Seamless with existing processing pipeline

## 🚨 Troubleshooting

### Common Issues

**Service won't start:**
```bash
python atlas_status.py --detailed
# Check logs in logs/atlas/
```

**Background processing not working:**
```bash
# Check if comprehensive service exists
ls -la atlas_comprehensive_service.py
# Check database path in queue system
python -c "from universal_processing_queue import UniversalProcessingQueue; print('Queue system OK')"
```

**Services killed immediately after starting:**
```bash
# Fixed in latest version - aggressive cleanup bug resolved
# Restart with: python atlas_service_manager.py restart
```

**Transcript discovery failing:**
```bash
# Test transcript orchestrator
python transcript_orchestrator.py --test --podcast "Test Podcast" --episode "Test Episode"
```

**Database corruption:**
```bash
python -c "from helpers.database_config import test_database_integrity; print(test_database_integrity())"
```

## 🎬 YouTube Integration

Atlas now includes full YouTube API integration for both video collection and podcast transcript lookup:

### **YouTube API Features** ✅
- **Podcast Transcript Search**: Search YouTube for podcast episodes by name and topic
- **Video Metadata Extraction**: Get titles, channels, descriptions, and links
- **Automated Processing**: Integrated with Atlas scheduler for 2 AM daily runs
- **Fallback System**: YouTube as primary transcript source when other methods fail

### **Setup & Configuration**
```bash
# Test YouTube API integration
python3 test_youtube_simple.py

# View scheduler status
python3 scheduler_youtube_integration.py

# Manual transcript lookup
python3 -c "
from helpers.podcast_transcript_lookup_simple import PodcastTranscriptLookup
lookup = PodcastTranscriptLookup()
result = lookup.lookup_transcript('Huberman Lab', 'sleep')
print(f'Success: {result.success}')
if result.success:
    print(f'Transcript length: {len(result.transcript)}')
"
```

### **Scheduler Integration**
- **Daily Collection**: 2:00 AM automatic YouTube history processing
- **Transcript Lookup**: Every 30 minutes processes pending transcript requests
- **Database Storage**: All results stored in Atlas database with proper staging
- **Retry Logic**: Failed lookups automatically retry with exponential backoff

### **API Key Requirements**
The system uses your YouTube Data API v3 key (already configured in `.env`):
- `YOUTUBE_API_KEY=AIzaSyBKXQRpYgK8RZJzKqAmGn0Pxk3rjQcswz4`
- No browser authentication required for API-based features
- Full search and metadata extraction capabilities

**Firewall blocking domain access:**
```bash
# For Pi-hole setups, allow specific ports
sudo ufw allow in on [PUBLIC_INTERFACE] to any port 443 proto tcp
sudo ufw allow in on [PUBLIC_INTERFACE] to any port 80 proto tcp
```

**Performance issues:**
```bash
python scripts/performance_optimizer.py --analyze
```

### Getting Help

1. **Check logs**: `tail -f logs/atlas/atlas_service.json.log`
2. **System status**: `python atlas_status.py --detailed`
3. **Health check**: `curl localhost:7444/health`
4. **View documentation**: `docs/`

## 📋 Recent Updates

### Version 2024-09-11 - Critical Fixes
**🔧 Background Processing Restored**
- Fixed missing `atlas_comprehensive_service.py` causing scheduler failures
- Corrected database path in `universal_processing_queue.py` (atlas.db → data/atlas.db)  
- Implemented actual AI processing logic (was placeholder sleep calls)
- AI processing pipeline now generates real summaries and tags

**🛡️ Service Management Fixed**
- Resolved aggressive cleanup bug killing services immediately after startup
- Modified `bulletproof_process_manager.py` to prevent premature process termination
- Services now start and remain running properly

**🎙️ Transcript Discovery**
- Created missing `transcript_orchestrator.py` for podcast transcript discovery
- Added support for Lex Fridman, Joe Rogan, and generic transcript sources
- Integrated Mac Mini fallback transcription capability

**🔥 Firewall & Domain Access**
- Fixed atlas.khamel.com accessibility with UFW firewall rules
- Maintained Pi-hole security while allowing public access to Atlas

**📊 Processing Statistics**
- Background AI processing: 0/7,553 → 10+/7,553 items processed
- Real AI summaries and content analysis working
- Dashboard stats now show accurate processing metrics

## 🤝 Contributing

We welcome contributions! Please see:
- [Contributing Guidelines](docs/CONTRIBUTING.md)
- [Development Setup](docs/development/setup.md)
- [Architecture Overview](docs/architecture/overview.md)

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

Built with love using:
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [SQLite](https://sqlite.org/) - Reliable, serverless database
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - HTML/XML parsing
- [Sentence Transformers](https://www.sbert.net/) - Semantic embeddings

---

<div align="center">

**Atlas Personal Knowledge Management System**  
*Transform information into knowledge, knowledge into wisdom.*

[🚀 Get Started](#-quick-start-10-minutes) • [📚 Documentation](docs/) • [🐛 Report Bug](issues/) • [✨ Request Feature](issues/)

</div>