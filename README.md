# 🧠 Atlas - Personal AI Knowledge System

> **Production-Ready Personal AI with Single-Model Architecture**  
> Transform your digital life into an intelligent knowledge companion powered by optimal AI.

Atlas is your personal AI that captures everything you read, hear, and think—then uses **Gemini 2.5 Flash Lite** (the optimal model with 57% more value per dollar) to provide cognitive analysis across all your information.

## ✨ What Makes Atlas Special

🎯 **Single Optimal Model** - Gemini 2.5 Flash Lite for all workloads (cheapest + highest quality)  
🎤 **Voice-First Design** - "Hey Siri, save to Atlas" captures thoughts instantly  
🧠 **6 Cognitive Features** - AI that thinks *with* you, not just *for* you  
📱 **Mobile-First Interface** - Complete content management from your phone  
🔍 **Advanced Search & Filtering** - Find content by date, type, source, or meaning  
📺 **YouTube Integration** - Automatic video processing with transcript extraction  
🎙️ **Mac Mini Audio Processing** - Dedicated transcription with Whisper for high-quality audio processing  
📻 **PODEMOS Ad-Free Feeds** - Personal clean podcast feeds with ads removed  
⚡ **Production Ready** - 100% working with comprehensive testing and validation  

## 🎯 Single Model Architecture 

After comprehensive testing of 5 models across 5 workloads with real Atlas content, we selected **Gemini 2.5 Flash Lite** as the universal model for all Atlas cognitive features:

### Model Performance Results
| Model | Success Rate | Quality Score | Cost/1M Tokens | Value Score |
|-------|-------------|---------------|----------------|-------------|
| **🏆 Gemini 2.5 Flash Lite** | **100%** | **9.5/10** | **$0.05** | **190** |
| Mistral 7B Instruct | 100% | 8.5/10 | $0.07 | 121 |
| GPT-4o Mini | 100% | 9.2/10 | $0.15 | 61 |
| Llama 3.1 8B | 100% | 8.8/10 | $0.08 | 110 |

*Value Score = Quality Score ÷ (Cost per 1K tokens × 1000)*

**Why Gemini 2.5 Flash Lite?**
- ✅ **Cheapest**: $0.05/1M tokens (30% cheaper than alternatives)  
- ✅ **Highest Quality**: 9.5/10 quality score in comprehensive testing
- ✅ **Universal**: 100% success rate across all 5 workloads  
- ✅ **Fastest**: Ultra-low latency optimized for real-time use
- ✅ **Best Value**: 57% more value per dollar than next best option

### Supported Workloads
All powered by the single optimal model:
- **🏷️ Tags**: Generate relevant content tags (avg: 60 tokens, $0.000003)
- **📝 Summary**: Create concise summaries (avg: 150 tokens, $0.000008)
- **❓ Socratic**: Generate thought-provoking questions (avg: 250 tokens, $0.000012)
- **🔍 Patterns**: Identify key themes and insights (avg: 250 tokens, $0.000012)
- **💡 Recommendations**: Suggest follow-up actions (avg: 250 tokens, $0.000012)

## 🚀 Get Started in 10 Minutes

### 1. Complete Setup (Recommended)
```bash
git clone https://github.com/Khamel83/atlas.git
cd atlas
./scripts/atlas_complete_setup.sh
```
**This unified script handles everything:**
- 📱 Telegram notifications
- 🔔 Uptime Kuma monitoring  
- 📺 YouTube API
- 💻 Mac Mini integration
- 🤖 AI API keys
- ⚙️ SystemD services
- 🧪 Testing & validation

### 2. Alternative: Basic Installation
```bash
git clone https://github.com/Khamel83/atlas.git
cd atlas
./quick_install.sh
```

### 3. Required Setup (5 minutes)

**🔑 Get OpenRouter API Key** (Required - Powers all AI features):
1. Visit [OpenRouter.ai](https://openrouter.ai) and create account
2. Generate API key (starts with `sk-or-v1-`)
3. Add to `.env`: `OPENROUTER_API_KEY=sk-or-v1-your-key-here`
4. Cost: ~$1-5/month for typical usage

### 3. Install iOS Shortcuts

**📱 From Your Phone (Easiest):**
```bash
./get_mobile_url.sh  # Shows URL to open on iPhone
```
Then tap each shortcut to install

**💻 From Computer:**
```bash
./install_shortcuts.sh
```

### 4. Test Your Installation
```bash
# 1. Try voice capture
# Say: "Hey Siri, save to Atlas"
# Speak: "This is my first Atlas note"

# 2. Visit your AI dashboard
open http://localhost:7444  # Main Atlas dashboard
# Or directly access:
open http://localhost:7444/mobile  # Mobile-optimized interface  
open http://localhost:7444/ask/html  # Desktop cognitive interface
```

**That's it!** Atlas is now learning from your information and ready to help you think.

---

## 🔧 Optional Advanced Features

**Want YouTube, Mac Mini processing, or ad-free podcasts?** 

👉 **[📋 Complete External Setup Guide](docs/user-guides/EXTERNAL_REQUIREMENTS_GUIDE.md)** - Step-by-step instructions for:

- **📺 YouTube Integration** - Auto-process your subscriptions (Free with Google account)
- **🎙️ Mac Mini Audio Processing** - Dedicated Whisper transcription (Hardware required)  
- **📻 PODEMOS Ad-Free Podcasts** - Private RSS feeds without ads (Oracle OCI account)
- **📧 Email Integration** - Process forwarded emails (Any IMAP email)

**Core Atlas works perfectly without these!** Each feature has detailed setup instructions and troubleshooting.

## 🧠 Cognitive Features

Atlas includes 6 AI-powered cognitive features that work like a thinking partner:

### 🔄 **Proactive Content Surfacer**
Automatically surfaces relevant forgotten content with actionable buttons.
*"While working on your marketing strategy, I noticed you saved an article about customer psychology last month..."*
- ✅ Mark as reviewed to update your learning patterns
- ⏰ Snooze for later to resurface at the right time

### ⏰ **Temporal Relationship Engine**  
Identifies patterns and connections across time in your knowledge.
*"Your thinking about remote work has evolved - here's how your perspective changed over 6 months."*

### ❓ **Socratic Question Generator**
Creates thoughtful questions that deepen your understanding of topics.
*"You've read a lot about productivity. What if the real issue isn't time management but attention management?"*

### 📚 **Active Recall System**
Uses spaced repetition to help you remember and internalize important concepts.
*"Time to review: What were the key insights from that book on systems thinking you loved?"*

### 🧩 **Pattern Detection**
Discovers themes, connections, and insights across your entire knowledge base.
*"I've noticed you're collecting information about three related trends. Here's how they connect..."*

### 💡 **Content Recommendations**
Suggests relevant content based on your interests, goals, and current projects.
*"Based on your recent research, you might find this article on behavioral economics interesting..."*

## 📱 How You'll Use Atlas

### **🎤 Voice Capture Anywhere**
- Walking: "Hey Siri, save to Atlas" → capture thoughts instantly
- Driving: Voice-record meeting notes and action items  
- Commuting: Save article ideas and inspiration

### **🎙️ Automated Podcast Ingestion**
- Automatically fetches and processes podcast episodes from RSS feeds based on your prioritized list.
- Supports both historical episode processing and continuous ingestion of new releases.
- Integrates with the Smart Transcription Pipeline for high-quality transcripts.

### **🎬 YouTube Content Processing**
- **Automated YouTube Integration**: Monitors your YouTube subscriptions and history for new videos
- **Smart Content Discovery**: Processes YouTube videos with transcript extraction and metadata
- **Scheduled Processing**: Runs every 5 hours to discover and process new YouTube content
- **Atlas Integration**: YouTube videos stored with proper metadata and searchable through Atlas
- **Rate-Limited Processing**: Respects YouTube API limits while maximizing content discovery

### **🧹 PODEMOS Personal Ad-Free Podcasts**
- **Complete Ad Removal Pipeline**: Automatically removes advertisements from podcast episodes
- **OPML Import**: Import your podcast subscriptions from Overcast or other podcast apps
- **AI-Powered Ad Detection**: Advanced pattern matching identifies sponsor reads and dynamic ads
- **Mac Mini Integration**: Leverages dedicated Mac Mini hardware for Whisper transcription
- **High-Quality Audio Processing**: Uses FFmpeg to maintain audio quality while removing ads
- **Private RSS Feeds**: Generates clean, private RSS feeds hosted on Oracle OCI
- **2AM Processing**: Automated daily processing delivers clean episodes by 2:20 AM
- **Real-Time Monitoring**: Comprehensive monitoring and alerting for processing pipeline

### **💻 Web & Document Processing**
- **📱 Mobile Web**: `https://atlas.khamel.com/mobile` - Full Atlas access from any device
- **🖱️ Browser Extensions**: Right-click "Send to Atlas" on any web page (install on each browsing device)
- **📖 Universal Bookmarklet**: Works on any device - manual bookmark creation
- **📥 File Drop**: Drop files into Atlas directories for processing
- **📧 Email Forward**: Email content to Atlas inbox

### **🔍 Intelligent Search & Discovery**
- Search by meaning: "articles about leadership challenges"
- Advanced filters: Date, content type, source filtering
- Mobile content management: Delete, tag, archive from your phone
- AI insights: "What patterns do you see in my productivity research?"

### **📚 Learning & Growth**
- Active recall quizzes on important concepts
- Pattern recognition across your interests
- Thoughtful questions that deepen understanding

## 🔧 Content Quality & Reprocessing

Atlas includes intelligent content quality analysis and automatic reprocessing:

### **📊 Semantic Quality Evaluation**
- Analyzes 6 quality dimensions: error detection, language quality, structure, completeness, topic relevance, and information density
- Moves beyond simple character counting to assess actual content meaning and usefulness
- Identifies and flags problematic content: Wayback errors, fake transcripts, paywalled content, extraction failures

### **🔄 Automatic Content Reprocessing**  
- Background pipeline continuously improves low-quality content
- Re-extracts failed downloads using improved methods
- Cleans HTML-heavy content and reconstructs partial articles
- Includes comprehensive processing for podcast transcripts, ensuring high-quality, searchable audio content.
- **Recent Performance**: Eliminated all failed content (565→0 items, 100% success rate)

### **⚙️ Quality Management Interface**
- View quality scores and issues for all content
- One-click reprocessing buttons in web interface
- Real-time reprocessing status and progress tracking
- Mobile-friendly quality indicators and management

## 🏗️ Architecture Overview

Atlas is built on a bulletproof, production-ready architecture:

- **🐍 Python 3.9+** - Core processing engine
- **⚡ FastAPI** - High-performance web API
- **🧠 Advanced NLP** - Semantic understanding and AI analysis
- **📊 Vector Database** - Semantic search and similarity matching
- **🍎 Apple Integration** - Native Shortcuts and iOS extensions
- **🛡️ Bulletproof Process Management** - Memory leak prevention and stability

### **🎬 YouTube Processing System**
- **YouTube Data API v3** - Subscription monitoring and video discovery
- **pytube & youtube-transcript-api** - Video metadata and transcript extraction
- **Atlas Scheduler Integration** - Automated processing every 5 hours
- **Rate Limiting & Caching** - Respects API limits and prevents duplicates

### **🧹 PODEMOS Ad Removal Pipeline**
- **Mac Mini Whisper Integration** - Dedicated hardware transcription via SSH task queue
- **Advanced Ad Detection** - 8 pattern types with confidence scoring and machine learning
- **FFmpeg Audio Processing** - High-quality ad segment removal preserving audio fidelity
- **RSS Feed Generation** - Clean, private feeds with Oracle OCI hosting infrastructure
- **Automated Scheduling** - 2AM daily processing with 20-minute SLA guarantee
- **Real-time Monitoring** - Comprehensive health checks, alerting, and failure recovery

### **🎙️ Mac Mini Audio Processing Infrastructure**
- **SSH Task Queue** - Secure file-based task submission from Atlas to Mac Mini
- **Whisper Model Management** - Multiple model sizes (base, small, medium) for quality/speed optimization
- **Graceful Degradation** - Atlas continues operating if Mac Mini unavailable
- **Task Result Polling** - Efficient status checking and result retrieval
- **Audio Format Support** - Handles MP3, M4A, WAV, and other common podcast formats

## 📖 Complete Documentation

### **🚀 Getting Started**
- [📋 Mission & Progress Review](MISSION_PROGRESS_REVIEW.md) - What Atlas achieves and current status
- [🔧 External Requirements Guide](docs/user-guides/EXTERNAL_REQUIREMENTS_GUIDE.md) - **All optional setups (YouTube, Mac Mini, PODEMOS, Email)**
- [⚙️ Setup Guide](docs/user-guides/SETUP_GUIDE.md) - Detailed installation and configuration
- [🚀 Quick Start](quick_start_package/QUICK_START.md) - 10-minute basic setup

### **📱 User Guides**
- [📱 Mac User Guide](docs/user-guides/MAC_USER_GUIDE.md) - Complete Apple integration and shortcuts
- [📲 Mobile Guide](docs/user-guides/MOBILE_GUIDE.md) - iPhone/iPad workflows and mobile interface
- [📥 Ingestion Guide](docs/user-guides/INGESTION_GUIDE.md) - **Complete YouTube, PODEMOS, and content workflows**
- [🔍 Search Guide](docs/user-guides/SEARCH_GUIDE.md) - Advanced search and content discovery

### **🔧 System Management**
- [🛠️ Troubleshooting Guide](docs/user-guides/TROUBLESHOOTING_GUIDE.md) - **Comprehensive problem solving and diagnostics**
- [🔧 Maintenance Guide](docs/user-guides/MAINTENANCE_GUIDE.md) - Keep Atlas running smoothly
- [🤖 Automation Guide](docs/user-guides/AUTOMATION_GUIDE.md) - Advanced workflow automation

### **🏗️ Technical Documentation**
- [🏛️ System Architecture](docs/UNIFIED_SYSTEM_ARCHITECTURE.md) - Complete technical architecture overview
- [📡 API Documentation](docs/API_DOCUMENTATION.md) - All endpoints including YouTube, PODEMOS, Mac Mini
- [📋 Consolidation Audit](CONSOLIDATION_AUDIT.md) - System cleanup and duplicate removal process

## 🛠️ System Requirements

**macOS (Recommended):**
- macOS 11.0+ (Big Sur or later)
- 4GB RAM (8GB recommended)
- 10GB free disk space
- Python 3.9+

**Linux (Supported):**
- Ubuntu 20.04+ or equivalent
- 4GB RAM, 10GB disk space
- Python 3.9+

**Windows:**
- Windows 10+ with WSL2
- Follow Linux installation in WSL

**Optional Mac Mini Audio Processing:**
- Mac Mini with macOS 12+ (for dedicated Whisper transcription)
- SSH access configured between Atlas server and Mac Mini
- 8GB+ RAM recommended for Whisper models
- OpenAI Whisper installed (`pip install openai-whisper`)
- Setup scripts: `scripts/setup_mac_mini_ssh.sh` and `scripts/install_mac_mini_software.sh`

## 🚨 Status & Health

Atlas includes comprehensive health monitoring:

```bash
# Check system status
python3 atlas_status.py

# Detailed health report  
python3 atlas_status.py --detailed

# Performance monitoring
python3 atlas_monitor.py --real-time
```

**Current Status**: ✅ Production Ready  
**Uptime**: Bulletproof process management prevents memory leaks  
**Performance**: Handles 240,026+ indexed items with sub-second search  

## 🤝 Contributing

Atlas is actively developed and welcomes contributions:

1. **🐛 Bug Reports** - [Create an issue](https://github.com/Khamel83/atlas/issues)
2. **💡 Feature Requests** - Share your ideas
3. **📚 Documentation** - Help improve guides and examples
4. **🔧 Code Contributions** - See [CONTRIBUTING.md](CONTRIBUTING.md)

**Development Setup:**
```bash
git clone https://github.com/Khamel83/atlas.git
cd atlas
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 atlas_service_manager.py start --dev
```

## 📄 License

Atlas is released under the MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

Atlas builds on incredible open-source projects:
- **FastAPI** - Modern Python web framework
- **Sentence Transformers** - Semantic embeddings  
- **Whisper** - Speech recognition
- **spaCy** - Natural language processing

## 🔗 Quick Links

### **📋 Essential Documentation**
- **🚀 [Quick Start](quick_start_package/QUICK_START.md)** - Get running in 10 minutes  
- **🔧 [External Setup Guide](docs/user-guides/EXTERNAL_REQUIREMENTS_GUIDE.md)** - YouTube, Mac Mini, PODEMOS, Email setup
- **📥 [Content Processing Guide](docs/user-guides/INGESTION_GUIDE.md)** - All content capture workflows
- **🛠️ [Troubleshooting Guide](docs/user-guides/TROUBLESHOOTING_GUIDE.md)** - Fix any issues
- **📋 [Mission & Progress](MISSION_PROGRESS_REVIEW.md)** - What Atlas achieves

### **🎯 Access Points**
- **🎯 Main Dashboard** - Central navigation hub (`http://localhost:7444`)
- **📱 Mobile Interface** - Touch-optimized content management (`/mobile`)
- **🧠 Desktop Dashboard** - Full cognitive features (`/ask/html`)
- **⚙️ System Management** - Jobs and scheduling (`/jobs/html`)

### **🔗 Resources**
- **📱 [Download Shortcuts](shortcuts/)** - Apple Shortcuts for Mac/iOS
- **📖 [Full Documentation](docs/user-guides/)** - Complete user guides
- **🐛 [Report Issues](https://github.com/Khamel83/atlas/issues)** - Bug reports and features

---

<div align="center">

**🧠 Atlas: Where Your Knowledge Meets AI Intelligence**

[Get Started](quick_start_package/QUICK_START.md) • [Documentation](docs/user-guides/) • [Community](https://github.com/Khamel83/atlas/discussions)

</div>