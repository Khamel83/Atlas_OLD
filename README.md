# Atlas - Personal Content Consumption Pipeline

[![Critical Documentation](https://img.shields.io/badge/Documentation-Complete%20Architecture-red)](ATLAS_SYSTEM_DOCUMENTATION.md)
[![Transcript Count](https://img.shields.io/badge/Transcripts-9%2C566%20Extracted-blue)](data/atlas.db)
[![Success Rate](https://img.shields.io/badge/Success%20Rate-100%25%20on%20Real%20Content-green)](your_podcast_processor.py)

**🎯 PERSONAL CONTENT PIPELINE**: Automatically discovers, extracts, and processes transcripts from your 253 priority podcasts into a unified knowledge base.

> **📚 CRITICAL**: See `ATLAS_SYSTEM_DOCUMENTATION.md` for complete architecture, data model, and reconstruction guidance. This contains valuable lessons learned and the 9,566 extracted transcripts that must be preserved.

## 🎯 **System Purpose**
Your personal content consumption tracker that:
- Discovers transcripts from **your specific podcasts** (not generic content)
- Extracts only **real transcripts** (10,000+ characters, not webpage metadata)
- Builds a **searchable knowledge base** of everything you consume
- Processes content **as you consume it** (event-driven, not batch processing)

## 📚 **SYSTEM DOCUMENTATION**

### **🔴 CRITICAL - READ FIRST**
**File**: `ATLAS_SYSTEM_DOCUMENTATION.md`

**Purpose**: Complete architecture documentation that any developer can use to understand, rebuild, or migrate this system without reading the code.

**Contains**:
- ✅ **Database Schema**: Complete table structures for `content` and `episode_queue`
- ✅ **Data Value Assessment**: What's valuable (9,566 transcripts) vs what can be recreated
- ✅ **Architecture Lessons**: What worked (user-specific focus) vs what didn't (continuous processing)
- ✅ **Extraction Patterns**: Working examples like 95,646-character Acquired transcripts
- ✅ **Version 2 Design**: Event-driven N8N workflow recommendations
- ✅ **Migration Strategy**: How to preserve your valuable data during architecture changes

**Why This Exists**: This documentation captures all the hard-won lessons about transcript discovery, quality validation, and user-specific processing so you can rebuild this in any architecture (N8N, event-driven, etc.) while preserving the valuable database of extracted content.

### **🗄️ DATABASE SCHEMA OVERVIEW**
```sql
-- CORE ASSET: 9,566 extracted transcripts
content (
    id, url, title, content, content_type, metadata,
    created_at, updated_at, [ai_* fields], stage, processing_status
)

-- PROCESSING TRACKER: 5,168 episodes in queue
episode_queue (
    id, podcast_name, episode_title, episode_url,
    status, created_at, updated_at
)
```

### **🎯 KEY INSIGHTS FOR REBUILDING**
1. **User-Specific Focus**: Process your 253 podcasts, not generic content
2. **Quality Validation**: 10,000+ character minimum prevents metadata false positives
3. **Event-Driven Preferred**: Process content as consumed, not maintain backlogs
4. **Extraction Patterns**: Site-specific (Acquired uses `rich-text-block-6` pattern)
5. **Data Preservation**: The 9,566 transcripts are the primary asset

---

## 🚀 Quick Start

### **For Immediate Deployment**
```bash
# Start the automated system with continuous monitoring
./enhanced_monitor_atlas_fixed.sh

# Monitor progress in real-time
tail -f logs/enhanced_monitor.log

# Access monitoring dashboard
http://localhost:7445/monitoring/
```

### **For Custom Configuration**
- [CONFIGURATION.md](docs/CONFIGURATION.md) - RSS feeds and podcast settings
- [DEPLOYMENT.md](docs/DEPLOYMENT.md) - System requirements and scaling

## 🎯 What is Atlas?

Atlas is your **fully automated podcast transcript management system** that continuously discovers new episodes, extracts high-quality transcripts, and maintains a comprehensive database without any manual intervention.

### The Problem Atlas Solves

- **Manual transcript hunting**: Tediously searching for transcripts episode by episode
- **Incomplete collections**: Missing transcripts from favorite podcasts
- **Outdated content**: No automatic updates when new episodes release
- **Scalability limits**: Can't process hundreds of podcasts manually
- **Quality inconsistency**: Mix of transcripts with show notes and navigation

### The Atlas Solution

- **Continuous Discovery**: Monitors 190+ RSS feeds for new episodes automatically
- **Intelligent Extraction**: Network-specific patterns for high-quality transcript capture
- **Quality Filtering**: Automated validation ensures only actual transcripts (15-25% success rate)
- **Scalable Processing**: Handles thousands of episodes with background batch processing
- **Zero Maintenance**: Runs 24/7 with scheduled tasks and error recovery

## ✨ Core Features

### 🚀 Automated Processing
- **24/7 Operation**: Continuous background processing without manual intervention
- **RSS Feed Monitoring**: Automatically tracks 190+ podcast feeds for new episodes
- **Batch Processing**: Intelligent queue management with configurable batch sizes
- **Rate Limiting**: Respectful scraping with delays to prevent source blocking

### 🧠 Intelligent Transcript Extraction
- **Network-Specific Patterns**: Custom extraction rules for each podcast platform
- **Quality Validation**: Automated filtering ensures only actual transcripts (15-25% success rate)
- **Multi-Source Search**: Existing cache → Direct scraping → Community sources fallback
- **Duplicate Prevention**: Sophisticated deduplication to avoid duplicate transcripts

### 📊 Real-time Monitoring & Logging
- **Live Progress Tracking**: Real-time logs showing extraction progress and success rates
- **Error Recovery**: Comprehensive error handling with automatic retry mechanisms
- **Performance Metrics**: Detailed statistics on processing speed and success rates
- **Database Status**: Live transcript count and queue status monitoring

### ⚙️ Scheduled Automation
- **Hourly Tasks**: Process 50 episodes per hour from the queue
- **Daily Tasks**: Comprehensive episode discovery and large batch processing
- **Maintenance Tasks**: Automatic cleanup of old errors and database optimization
- **Graceful Shutdown**: Signal handling for safe restarts and updates

### 📧 Gmail Integration (NEW)
- **Real-time Email Processing**: Gmail push notifications with sub-5-second processing
- **iOS Shortcut Support**: Perfect integration with `khamel83+atlas@gmail.com` workflow
- **Dual Label Processing**: Handles both "Atlas" and "Newsletter" labels
- **URL & Attachment Extraction**: Automatically extracts URLs and downloads attachments
- **Content Categorization**: Separate processing for manual bookmarks vs newsletters
- **See**: [GMAIL_INTEGRATION.md](GMAIL_INTEGRATION.md) for complete setup guide

### 🎯 High-Quality Sources
- **Premium Podcasts**: Lex Fridman, EconTalk, Acquired, Conversations with Tyler
- **Academic Content**: 99% Invisible, Planet Money, Practical AI
- **Business & Technology**: Thousands of episodes across multiple domains
- **Community Contributions**: GitHub, Medium, Archive.org sources
- **Personal Bookmarks**: Gmail-sourced content via iOS shortcuts and newsletters

## 🏗️ Architecture

```
┌─────────────────────────┐    ┌──────────────────────┐    ┌─────────────────┐
│   RSS Feeds             │───▶│  Atlas Manager       │───▶│  Transcript DB  │
│   (374+ Sources)        │    │  (24/7 Engine)       │    │  (SQLite)       │
└─────────────────────────┘    └──────────────────────┘    └─────────────────┘
                                       │
                                       ▼
                         ┌──────────────────────────┐
                         │  Enhanced Monitor        │
                         │ • Auto-Restart           │
                         │ • Health Checks          │
                         │ • Resource Monitoring    │
                         │ • Alert System           │
                         └──────────────────────────┘
                                       │
                                       ▼
                         ┌──────────────────────────┐
                         │  Processing Queue       │
                         │ • 5,162 Episodes Pending │
                         │ • Quality Filter        │
                         │ • Error Recovery        │
                         └──────────────────────────┘
```

### Key Components

- **Atlas Manager** ([atlas_manager.py](atlas_manager.py)) - Main automation engine with continuous processing
- **Enhanced Monitor** ([enhanced_monitor_atlas_fixed.sh](enhanced_monitor_atlas_fixed.sh)) - Auto-restart and health monitoring system
- **Monitoring Service** ([monitoring_service.py](monitoring_service.py)) - Real-time dashboard and metrics
- **Episode Processor** ([single_episode_processor.py](single_episode_processor.py)) - Individual episode extraction
- **Transcript Sources** ([helpers/podcast_source_registry.py](helpers/podcast_source_registry.py)) - 5-source registry system
- **Configuration System** ([config/](config/)) - 374 RSS feeds and source patterns

### 🎯 Production Architecture

**Optimized for continuous operation:**
- **Background Processing**: Non-blocking subprocess execution for scalability
- **Queue Management**: SQLite-based episode tracking with status management
- **Signal Handling**: Graceful shutdown and restart capabilities
- **Resource Efficiency**: Minimal memory footprint with filesystem logging
- **Error Recovery**: Automatic retry logic and cleanup of failed operations

## 📚 Documentation

### Getting Started
- [QUICK_START.md](docs/QUICK_START.md) - 30-second setup guide
- [DEPLOYMENT.md](docs/DEPLOYMENT.md) - Detailed installation instructions
- [CONFIGURATION.md](docs/CONFIGURATION.md) - RSS feeds and podcast settings

### Architecture & Design
- [docs/AUTOMATION_ARCHITECTURE.md](docs/AUTOMATION_ARCHITECTURE.md) - Complete system design
- [docs/SCALING_PRINCIPLES.md](docs/SCALING_PRINCIPLES.md) - Scaling for thousands of episodes
- [docs/QUALITY_FILTERING.md](docs/QUALITY_FILTERING.md) - Transcript validation strategies

### Performance & Monitoring
- [docs/PERFORMANCE_METRICS.md](docs/PERFORMANCE_METRICS.md) - Success rates and processing speed
- [docs/ERROR_RECOVERY.md](docs/ERROR_RECOVERY.md) - Error handling and retry mechanisms
- [docs/MONITORING.md](docs/MONITORING.md) - Real-time monitoring and logging

## 🧪 Testing

```bash
# Check system status
ps aux | grep atlas_manager.py    # Verify running process
tail -f logs/atlas_manager.log    # Monitor real-time progress

# Test individual components
python3 single_episode_processor.py test_id test_url test_podcast  # Test episode processing
./start_atlas.sh                  # Test automated startup

# Database verification
sqlite3 data/atlas.db "SELECT COUNT(*) FROM content WHERE content_type = 'podcast_transcript';"
sqlite3 data/atlas.db "SELECT status, COUNT(*) FROM episode_queue GROUP BY status;"
```

**System Status**: ✅ Running with 1,244+ transcripts extracted and processing 5,000+ queued episodes

## 🎯 Real-World Usage

### Example: Automated Transcript Discovery
```bash
# Start the system
./start_atlas.sh
Atlas Manager started with PID: 4063841
✅ Atlas Manager is running successfully

# Monitor progress (real-time logs)
tail -f logs/atlas_manager.log
2025-09-23 15:54:37,197 - INFO - Total transcripts in database: 1244
2025-09-23 15:54:37,205 - INFO - Queue status: {'error': 10, 'found': 1, 'not_found': 109, 'pending': 5068}
2025-09-23 15:55:14,890 - INFO - Added 8 episodes for The NPR Politics Podcast
2025-09-23 15:56:22,729 - INFO - Added 5 episodes for Greatest Of All Talk (Stratechery Plus Edition)
2025-09-23 16:00:31,144 - INFO - Added 3 episodes for Odd Lots
```

### Example: Batch Processing Results
```bash
# Check database growth over time
sqlite3 data/atlas.db "SELECT COUNT(*) FROM content WHERE content_type = 'podcast_transcript';"
1244

# Monitor queue processing
sqlite3 data/atlas.db "SELECT status, COUNT(*) FROM episode_queue GROUP BY status;"
error      | 10
found      | 1
not_found  | 109
pending    | 5068

# System automatically processes 50 episodes per hour
# Expected: 200-300 new transcripts discovered daily
```

## 🛠️ Development

### System Management
```bash
# Start the continuous operation system
./enhanced_monitor_atlas_fixed.sh   # Launch with auto-restart monitoring

# Monitor and debug
tail -f logs/enhanced_monitor.log    # Real-time monitoring logs
curl http://localhost:7445/health    # Health check
http://localhost:7445/monitoring/    # Real-time dashboard

# Process management
ps aux | grep atlas_manager.py      # Check Atlas Manager status
ps aux | grep monitoring_service.py # Check monitoring service status

# Database management
sqlite3 data/atlas.db             # Direct database access
```

### Configuration Management
```bash
# Add new podcasts
echo "new_podcast_name,rss_feed_url" >> config/podcast_rss_feeds.csv

# Update extraction patterns
# Edit config/podcast_sources_cache.json for new source patterns

# Modify processing settings
# Edit atlas_manager.py batch sizes and scheduling
```

## 📈 Performance Metrics

- **Transcript Discovery**: 1,244+ transcripts extracted and growing
- **Processing Rate**: 50 episodes per hour (configurable)
- **Success Rate**: 15-25% of episodes have extractable transcripts
- **Queue Management**: 5,000+ episodes queued for processing
- **Resource Efficiency**: Minimal memory footprint with background processing
- **Error Recovery**: Automatic retry and cleanup mechanisms

## 🤝 Contributing

1. **Understand the architecture**: Review [atlas_manager.py](atlas_manager.py) and processing flow
2. **Test new sources**: Use [single_episode_processor.py](single_episode_processor.py) for testing
3. **Add RSS feeds**: Update [config/podcast_rss_feeds.csv](config/podcast_rss_feeds.csv)
4. **Improve patterns**: Update [config/podcast_sources_cache.json](config/podcast_sources_cache.json)
5. **Monitor performance**: Check logs and database metrics

## 🎊 Status

**✅ FULLY AUTOMATED CONTINUOUS OPERATION SYSTEM: OPERATIONAL**

The Atlas Management System runs continuously and provides:
- **🔒 24/7 Continuous Operation** with auto-restart and health monitoring
- **9,566+ transcripts** extracted from 374 active podcasts
- **5,162 episodes** in processing queue with continuous extraction
- **374+ RSS feeds** monitored for new content (96% expansion)
- **Real-time dashboard** with WebSocket monitoring at http://localhost:7445/monitoring/
- **Auto-restart capabilities** ensuring Atlas never stops running
- **Health monitoring** with resource alerts and automatic recovery

**Core Principle**: Atlas is always running. Every episode is either done or in progress. No manual intervention required. 🚀

---

**Core Documentation:**
- [Continuous Operation Principles](CONTINUOUS_OPERATION.md) - Detailed guide on Atlas's always-running philosophy
- [Real-time Monitoring](README_MONITORING.md) - Dashboard and health monitoring
- [System Status](SYSTEM_STATUS.md) - Current operational metrics

### 🎯 Quick Health Check
```bash
# Single KPI metric for Atlas health and progress
./atlas_health.sh
# Returns: Atlas Health Score (0-100%) - 70+ EXCELLENT, 50+ GOOD, 30+ FAIR, <30 POOR
```

*Atlas truly runs itself - discovering, extracting, and organizing podcast transcripts 24/7 with zero human intervention required.* 🤖