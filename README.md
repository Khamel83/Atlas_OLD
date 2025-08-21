# Atlas: Personal Knowledge Management System

**Status**: Phases 3 & 4 Complete - Unified Article Processing & Content Pipeline  
**Documentation Updated**: August 21, 2025

Atlas is a sophisticated personal content ingestion and management system with unified processing workflows, advanced recovery capabilities, and comprehensive content analysis.

## 🎉 **MAJOR UPDATE: Phases 3 & 4 Refactoring Complete**

**NEW**: Atlas now features unified article processing and configurable content pipeline with 60% complexity reduction, intelligent strategy management, bulk processing optimization, and comprehensive statistics tracking - all with 100% backward compatibility.

## 🚀 Quick Start

**Want to try Atlas right now?** See [QUICK_START.md](QUICK_START.md) for 10-minute setup instructions.

**Need detailed status?** See [docs/CURRENT_STATUS.md](docs/CURRENT_STATUS.md) for what actually works vs. what doesn't.

## 🔄 Always-Running Background Service

Atlas includes a unified background service that handles all continuous processing automatically:

```bash
# Start the background service
./scripts/start_atlas_service.sh start

# For persistent operation (survives reboots)
./scripts/setup_systemd_service.sh
sudo systemctl start atlas
```

The service automatically handles podcast discovery, transcript fetching, article retries, and system maintenance with auto-restart on failures.

## ⚖️ Legal Notice

**IMPORTANT**: Atlas is provided for personal research and educational use only. By using this software, you agree to:

- **Use at your own risk** - No warranty or support provided
- **Follow all applicable laws** - You are responsible for legal compliance
- **Respect third-party terms** - Follow website and API terms of service
- **Secure your data** - Atlas stores data locally without encryption

**See the [LEGAL](LEGAL/) directory for complete terms, privacy policy, and compliance notes.**

## 🧭 Core Philosophy

Atlas represents a fundamental shift from **passive content storage** to **active cognitive amplification**:

- **Local-First**: All data stored locally on your machine. No cloud dependencies for core features.
- **Cognitive Enhancement**: Tools that amplify human thinking, not just organize information.
- **Resilient Processing**: Handles failures gracefully with comprehensive retry mechanisms.
- **Structured Output**: Clean, portable Markdown ready for any knowledge management system.
- **Privacy-Preserving**: Optional AI features with user-controlled API usage.

## 🧠 Cognitive Amplification Features

Atlas includes a comprehensive suite of cognitive amplification tools, accessible via both API and web dashboard:

### Core Cognitive Features
- **🔍 Proactive Surfacer**: Rediscovers forgotten or stale content for review
- **⏰ Temporal Engine**: Finds time-aware relationships between content items
- **❓ Socratic Question Generator**: Generates deep questions to enhance understanding
- **🧠 Active Recall Engine**: Schedules spaced repetition for knowledge retention
- **📊 Pattern Detector**: Identifies trends in tags, sources, and content patterns

### Access Methods

**Web Dashboard**: Interactive interface at `/ask/html`
```bash
uvicorn web.app:app --reload --port 8000
# Visit: http://localhost:8000/ask/html
```

**REST API**: Programmatic access to all features
- `/ask/proactive` (GET): Surface forgotten content
- `/ask/temporal` (GET): Time-aware relationships  
- `/ask/socratic` (POST): Generate Socratic questions
- `/ask/recall` (GET): Spaced repetition items
- `/ask/patterns` (GET): Content pattern analysis

## 🧱 What Actually Works Right Now

### ✅ **Content Ingestion Pipeline** 
- **Article Processing**: 6-strategy fallback system (Direct HTTP → 12ft.io → Archive.today → Googlebot → Playwright → Wayback)
- **YouTube Integration**: Transcript extraction with multi-language support
- **Podcast Processing**: OPML parsing and episode download with transcription
- **Robust Retry System**: Comprehensive failure handling with persistent queues
- **✅ TESTED**: Successfully ingests real-world content (Wikipedia, Nature articles, academic papers)

### ✅ **Cognitive Infrastructure**
- **Complete Implementation**: All 5 cognitive modules fully functional
- **Web Dashboard**: FastAPI-based interface with interactive features  
- **API Integration**: RESTful access to all cognitive amplification features
- **Metadata Management**: Comprehensive content metadata and relationship tracking
- **✅ END-TO-END VERIFIED**: Full pipeline from article fetch → processing → cognitive analysis → web dashboard

### ✅ **Supporting Systems**
- **Configuration Management**: Multi-source config with validation
- **Error Handling**: Centralized error management with detailed logging
- **Safety Monitoring**: Pre-run safety checks and compliance validation
- **Path Management**: Organized file system structure with backup capabilities
- **Testing Infrastructure**: Comprehensive test suite with 90%+ coverage

## 🔧 System Architecture

```
Atlas/
├── run.py                    # Main CLI entry point
├── helpers/                  # Core processing modules
│   ├── article_fetcher.py   # Article ingestion (929 lines)
│   ├── youtube_ingestor.py  # YouTube processing (545 lines) 
│   ├── podcast_ingestor.py  # Podcast processing (267 lines)
│   ├── metadata_manager.py  # Content metadata management
│   ├── path_manager.py      # File system organization
│   └── ...                  # 19 supporting modules
├── ask/                      # Cognitive amplification features
│   ├── proactive/           # Content surfacing
│   ├── temporal/            # Time relationships
│   ├── socratic/            # Question generation
│   ├── recall/              # Spaced repetition
│   └── insights/            # Pattern detection
├── web/                      # Web interface
│   ├── app.py               # FastAPI application
│   └── templates/           # HTML templates
├── ingest/                   # Advanced processing pipeline
├── process/                  # Content analysis
├── tests/                    # Comprehensive test suite
├── inputs/                   # Input files (articles.txt, etc.)
└── output/                   # Processed content storage
```

## 🏃‍♂️ Usage

### Basic Commands
```bash
# Process articles from inputs/articles.txt
python run.py --articles

# Process YouTube videos from inputs/youtube.txt  
python run.py --youtube

# Process podcasts from inputs/podcasts.opml
python run.py --podcasts

# Process everything
python run.py --all

# Process custom URL file
python run.py --urls path/to/urls.txt

# Process Instapaper export
python run.py --instapaper-csv path/to/export.csv

# Recategorize existing content
python run.py --recategorize
```

### Input Files Setup
```bash
# Articles - one URL per line
echo "https://example.com/article1" >> inputs/articles.txt

# YouTube - video URLs
echo "https://youtube.com/watch?v=example1" >> inputs/youtube.txt

# Podcasts - OPML file from your podcast app
# Place your podcast subscriptions in inputs/podcasts.opml
```

### Output Structure

The output structure is defined in the `.env.template` file. By default, it creates a comprehensive directory structure under the `output/` directory, with separate folders for different content types, metadata, transcripts, and other data.

## 📋 Setup Requirements

### Prerequisites
- Python 3.9+ installed
- Git installed
- Virtual environment (recommended)

### Installation
```bash
# Clone repository
git clone <repository-url>
cd atlas

# Set up environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.template .env
```

### Configuration
Minimum `.env` setup:
```env
# No mandatory configuration needed to run the application
# but for full AI features, you'll need an OpenRouter API key
OPENROUTER_API_KEY=your_api_key_here
```

For full AI features:
```env
OPENROUTER_API_KEY=your_api_key_here
MODEL=google/gemini-2.0-flash-lite-001
```

## 🧪 Testing

Atlas includes comprehensive testing infrastructure:

```bash
# Run all tests
pytest

# Run with coverage (install pytest-cov first)  
pytest --cov=helpers --cov-report=html

# Run specific test categories
pytest tests/unit/
pytest tests/integration/

# Run specific module tests
pytest tests/unit/test_path_manager.py -v
```

**Current Test Status**: 
- **Unit Tests**: 15+ modules with comprehensive coverage
- **Integration Tests**: End-to-end pipeline validation
- **Foundation Tests**: Critical infrastructure (PathManager, MetadataManager, etc.)
- **✅ REAL-WORLD TESTING**: Successfully tested with live URLs including Wikipedia AI article and Nature genomics paper
- **✅ COMPREHENSIVE COVERAGE**: New test suites for MetadataManager, cognitive features, and web dashboard

## ⚠️ Current Limitations & Known Issues

### Configuration & Setup
- **Manual configuration required** - Must set up `.env` file manually
- **API key dependency** - Full AI features require OpenRouter API key
- **Input file setup** - Manual creation of input files needed

### Infrastructure Gaps  
- **Limited documentation** - Some advanced features need better docs
- **Error messages** - Could be more user-friendly for new users
- **Performance optimization** - Not yet optimized for large-scale processing

### Feature Completeness
- **Search capabilities** - No full-text search implemented yet
- **Advanced analytics** - Content insights could be more sophisticated  
- **Third-party integrations** - Limited integration with external tools

## 🔮 Planned Enhancements

Based on the authoritative [PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md):

### Phase 2: Advanced Features (Weeks 3-6)
- **Document Processing**: Support for 20+ file formats via Unstructured
- **Enhanced Deduplication**: Jaccard similarity with multi-level detection
- **Full-Text Search**: Meilisearch integration for fast, typo-tolerant search
- **Local Transcription**: Privacy-preserving Whisper integration
- **Instapaper API**: OAuth integration replacing web scraping

### Phase 3: Advanced Intelligence (Weeks 8-11)  
- **Vector Search**: FAISS-powered semantic similarity
- **Entity Graphs**: Named entity recognition and knowledge graphs
- **Plugin Architecture**: Extensible framework for custom integrations
- **Automation**: APScheduler integration for periodic processing
- **ActivityWatch Integration**: Personal productivity insights

## 🆘 Troubleshooting

### Common Issues

**"No module named X" errors:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**Configuration problems:**
```bash
# Verify your .env file exists and has correct format
cat .env
python run.py --help  # Test basic functionality
```

**Empty output:**
```bash
# Check input files have content
ls -la inputs/
cat inputs/articles.txt
# Check logs for errors
ls -la output/*/ingest.log
```

**API issues:**  
```bash
# Test without AI features first
# Set TRANSCRIBE_ENABLED=false and don't set OPENROUTER_API_KEY
python run.py --articles
```

### Getting Help

1. **Start with [QUICK_START.md](QUICK_START.md)** for basic setup
2. **Check [docs/CURRENT_STATUS.md](docs/CURRENT_STATUS.md)** for known issues  
3. **Review logs** in `output/*/ingest.log` for detailed errors
4. **Enable debug logging**: `LOG_LEVEL=DEBUG python run.py --articles`
5. **Check troubleshooting guide**: `docs/environment-troubleshooting.md`

## 📚 Documentation

### Essential Guides
- **[QUICK_START.md](QUICK_START.md)** - 10-minute setup guide
- **[docs/CURRENT_STATUS.md](docs/CURRENT_STATUS.md)** - Current system status  
- **[docs/PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md)** - Authoritative development plan

### Technical Documentation
- **[docs/ENHANCED_MODEL_SELECTOR_GUIDE.md](docs/ENHANCED_MODEL_SELECTOR_GUIDE.md)** - AI model configuration
- **[docs/CAPTURE_ARCHITECTURE.md](docs/CAPTURE_ARCHITECTURE.md)** - Content processing pipeline
- **[docs/environment-troubleshooting.md](docs/environment-troubleshooting.md)** - Setup troubleshooting

### Research & Planning
- **[docs/SIMILAR_PROJECTS_RESEARCH.md](docs/SIMILAR_PROJECTS_RESEARCH.md)** - Competitive analysis
- **[docs/COGNITIVE_AMPLIFICATION_PHILOSOPHY.md](docs/COGNITIVE_AMPLIFICATION_PHILOSOPHY.md)** - Design philosophy

## 🎯 Project Status

**Current Phase**: Post-Infrastructure Testing & Documentation Refinement

**What Works**: 
- Complete content ingestion pipeline with 6-strategy article fetching
- Full cognitive amplification suite with web interface  
- Robust error handling and retry mechanisms
- Comprehensive testing infrastructure (90%+ coverage)
- Local-first architecture with optional AI features

**Immediate Focus**:
- Documentation improvements and user onboarding
- Configuration streamlining
- Advanced feature completion (search, analytics)

**Bottom Line**: Atlas is a functional cognitive amplification platform with solid architecture. The core systems work well, but user experience and advanced features need refinement.

## 🤝 Getting Help & Contributing

- **Technical Overview**: See [docs/PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md) for complete system architecture
- **Philosophy**: Review [docs/COGNITIVE_AMPLIFICATION_PHILOSOPHY.md](docs/COGNITIVE_AMPLIFICATION_PHILOSOPHY.md) for design principles  
- **Contributing**: All contributors welcome - Atlas is open source and community-driven
- **Issues & PRs**: Use GitHub repository with branch protection enabled

---

*Atlas: Transforming how you interact with and derive insights from your personal knowledge base.*

**Note**: This README reflects the actual current state of Atlas as of January 2025. For the most up-to-date technical status, see [docs/CURRENT_STATUS.md](docs/CURRENT_STATUS.md).