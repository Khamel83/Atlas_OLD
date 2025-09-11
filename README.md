# Atlas Personal Knowledge Management System

> **🚀 Production-Ready Personal AI Assistant**  
> Transform any content into searchable, intelligent knowledge with automatic processing, semantic search, and AI-powered insights.

[![Atlas Reliability](https://img.shields.io/badge/reliability-24%2F7-green)](https://github.com/yourusername/atlas)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## ✨ What is Atlas?

Atlas is a **bulletproof personal knowledge management system** that automatically processes, indexes, and makes searchable any content you feed it:

- 📰 **Articles & Web Pages** - Save from any website with instant processing
- 🎙️ **Podcast Transcripts** - Automatic discovery and full-text search  
- 📧 **Email Archives** - Import and search your email history
- 📄 **Documents** - PDFs, text files, notes, and more
- 🧠 **AI Insights** - Semantic search, content recommendations, and intelligent analysis

**Perfect for**: Researchers, knowledge workers, students, content creators, and anyone who needs to organize and retrieve information efficiently.

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
git clone https://github.com/yourusername/atlas.git
cd atlas
./config/install_shortcuts.sh  # Complete setup
```

### 2. **Start Atlas**
```bash
python atlas_service_manager.py start --daemon
```

### 3. **Access Your Knowledge**
- **Web Dashboard**: http://localhost:8000
- **Mobile Interface**: http://localhost:8000/mobile  
- **API Documentation**: http://localhost:8000/docs

### 4. **Add Content**
- **iOS**: "Hey Siri, save to Atlas" (after installing shortcuts)
- **Web**: Use the dashboard upload interface
- **API**: POST to `/api/v1/content/`

## 📊 System Status

Check system health anytime:
```bash
python atlas_status.py --detailed
```

**Real-time monitoring** available at: http://localhost:8000/monitoring

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
API_PORT=8000
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

Access via: http://localhost:8000/ask/

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

## 🚨 Troubleshooting

### Common Issues

**Service won't start:**
```bash
python atlas_status.py --detailed
# Check logs in logs/atlas/
```

**Database corruption:**
```bash
python -c "from helpers.database_config import test_database_integrity; print(test_database_integrity())"
```

**Performance issues:**
```bash
python scripts/performance_optimizer.py --analyze
```

### Getting Help

1. **Check logs**: `tail -f logs/atlas/atlas_service.json.log`
2. **System status**: `python atlas_status.py --detailed`
3. **Health check**: `curl localhost:8000/health`
4. **View documentation**: `docs/`

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