# ⚡ Atlas Quick Start Guide

Get Atlas running on your system in under 10 minutes!

## 🎯 What You'll Get

- **Personal AI Assistant** - Intelligent content processing and insights
- **Content Capture** - Save articles, podcasts, documents from anywhere  
- **Smart Search** - Find anything with AI-powered semantic search
- **Apple Integration** - Voice capture with "Hey Siri" shortcuts
- **Web Dashboard** - Beautiful interface for all your content

## 🚀 5-Minute Setup

### Step 1: Download and Install
```bash
# Clone the repository
git clone https://github.com/your-username/atlas.git
cd atlas

# Install dependencies (one command does everything)
./scripts/setup_wizard.py
```

### Step 2: Start Atlas
```bash
# Start all services
./start_work.sh

# Check everything is running
./venv/bin/python atlas_status.py
```

### Step 3: Open Your Dashboard
Open http://localhost:8000/ask/html in your browser

You should see the Atlas dashboard with cognitive features like:
- 🧠 **Proactive Content Surfacing** - Find forgotten gems
- ⏰ **Temporal Analysis** - Connect ideas across time  
- ❓ **Socratic Questioning** - Deepen your thinking
- 🔁 **Active Recall** - Spaced repetition learning
- 🔍 **Pattern Detection** - Find hidden connections

## 📱 Add iPhone/iPad Shortcuts (Optional)

```bash
# Install Apple Shortcuts for voice capture
cd shortcuts
./install_shortcuts.sh

# Configure with your server URL
./configure_shortcuts.py
```

Test with: **"Hey Siri, Capture Thought"**

## 🎉 You're Ready!

### Add Your First Content

1. **Article**: Paste a URL into the dashboard
2. **Document**: Upload a PDF or text file
3. **Voice Note**: Use "Hey Siri, Capture Thought"
4. **Quick Note**: Use the web dashboard text box

### Explore Features

1. **Ask Questions**: Use the cognitive features to analyze content
2. **Search Everything**: Semantic search finds related concepts  
3. **Get Insights**: Pattern detection reveals connections
4. **Build Knowledge**: Active recall helps you remember

## 📚 Next Steps

- **Read User Guides**: `docs/user-guides/` for detailed workflows
- **Customize**: Edit `.env` file for your preferences
- **Automate**: Set up RSS feeds and email forwarding
- **Mobile**: Full iPhone/iPad integration available

## 🆘 Need Help?

- **Status Check**: `./venv/bin/python atlas_status.py`
- **Troubleshooting**: See `TROUBLESHOOTING.md`
- **User Guides**: Complete documentation in `docs/user-guides/`
- **Support**: Create an issue on GitHub

## 🔧 System Requirements

- **OS**: macOS, Linux, or Windows (WSL2)
- **Python**: 3.8+ (installed automatically)
- **Memory**: 4GB+ recommended
- **Storage**: 2GB for base system + your content
- **Network**: Internet connection for AI features

---

**Welcome to Atlas!** 🎊 Your personal AI knowledge system is ready to amplify your thinking.