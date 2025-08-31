# 🧠 Atlas - Personal AI Knowledge System

> Transform your digital life into an intelligent knowledge companion that learns, connects, and amplifies your thinking.

Atlas is your personal AI that captures everything you read, hear, and think—then uses cognitive AI to help you discover patterns, make connections, and gain insights across all your information.

## ✨ What Makes Atlas Special

🎤 **Voice-First Design** - "Hey Siri, save to Atlas" captures thoughts instantly  
🧠 **6 Cognitive Features** - AI that thinks *with* you, not just *for* you  
📱 **Mobile-First Interface** - Complete content management from your phone  
🔍 **Advanced Search & Filtering** - Find content by date, type, source, or meaning  
⚡ **Zero Maintenance** - Runs quietly in the background, no configuration needed  

## 🚀 Get Started in 10 Minutes

### Quick Install (macOS)
```bash
git clone https://github.com/your-org/atlas.git
cd atlas
./quick_install.sh
```

### Install iOS Shortcuts

**📱 From Your Phone (Easiest):**
```bash
./get_mobile_url.sh  # Shows URL to open on iPhone
```
Then tap each shortcut to install

**💻 From Computer:**
```bash
./install_shortcuts.sh
```

### Test Your Installation
```bash
# 1. Try voice capture
# Say: "Hey Siri, save to Atlas"
# Speak: "This is my first Atlas note"

# 2. Visit your AI dashboard
open http://localhost:8000/mobile  # Mobile-optimized interface
open http://localhost:8000/ask/html  # Desktop interface
```

**That's it!** Atlas is now learning from your information and ready to help you think.

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

### **💻 Web & Document Processing**
- One-click save articles with browser bookmarklet
- Drop PDFs into `~/Documents/Atlas/articles/` for automatic processing
- Email important content to your Atlas inbox

### **🔍 Intelligent Search & Discovery**
- Search by meaning: "articles about leadership challenges"
- Advanced filters: Date, content type, source filtering
- Mobile content management: Delete, tag, archive from your phone
- AI insights: "What patterns do you see in my productivity research?"

### **📚 Learning & Growth**
- Active recall quizzes on important concepts
- Pattern recognition across your interests
- Thoughtful questions that deepen understanding

## 🏗️ Architecture Overview

Atlas is built on a bulletproof, production-ready architecture:

- **🐍 Python 3.9+** - Core processing engine
- **⚡ FastAPI** - High-performance web API
- **🧠 Advanced NLP** - Semantic understanding and AI analysis
- **📊 Vector Database** - Semantic search and similarity matching
- **🍎 Apple Integration** - Native Shortcuts and iOS extensions
- **🛡️ Bulletproof Process Management** - Memory leak prevention and stability

## 📖 Documentation

**New Users:**
- [📱 Mac User Guide](docs/user-guides/MAC_USER_GUIDE.md) - Complete Apple integration
- [🚀 Quick Start](quick_start_package/QUICK_START.md) - 10-minute setup  
- [📲 Mobile Guide](docs/user-guides/MOBILE_GUIDE.md) - iPhone/iPad workflows

**Power Users:**  
- [📥 Ingestion Guide](docs/user-guides/INGESTION_GUIDE.md) - All content capture methods
- [🔍 Search Guide](docs/user-guides/SEARCH_GUIDE.md) - Advanced search techniques
- [⚙️ Setup Guide](docs/user-guides/SETUP_GUIDE.md) - Detailed configuration

**Maintenance:**
- [🔧 Maintenance Guide](docs/user-guides/MAINTENANCE_GUIDE.md) - Keep Atlas running smoothly
- [🤖 Automation Guide](docs/user-guides/AUTOMATION_GUIDE.md) - Workflow automation

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

1. **🐛 Bug Reports** - [Create an issue](https://github.com/your-org/atlas/issues)
2. **💡 Feature Requests** - Share your ideas
3. **📚 Documentation** - Help improve guides and examples
4. **🔧 Code Contributions** - See [CONTRIBUTING.md](CONTRIBUTING.md)

**Development Setup:**
```bash
git clone https://github.com/your-org/atlas.git
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

- **🚀 [Quick Start Guide](quick_start_package/QUICK_START.md)** - Get running in 10 minutes
- **📱 [Download Shortcuts](shortcuts/)** - Apple Shortcuts for Mac/iOS
- **📱 [Mobile Interface](http://localhost:8000/mobile)** - Touch-optimized with content management  
- **🧠 [Desktop Dashboard](http://localhost:8000/ask/html)** - Full cognitive features
- **📖 [Full Documentation](docs/user-guides/)** - Complete user guides
- **🐛 [Report Issues](https://github.com/your-org/atlas/issues)** - Bug reports and features

---

<div align="center">

**🧠 Atlas: Where Your Knowledge Meets AI Intelligence**

[Get Started](quick_start_package/QUICK_START.md) • [Documentation](docs/user-guides/) • [Community](https://github.com/your-org/atlas/discussions)

</div>