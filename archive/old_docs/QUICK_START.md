# 🚀 Atlas Quick Start Guide

> **Get Atlas running in 10 minutes with this step-by-step guide**

## 🌟 Try It First - Live Demo

**Before installing locally**, see Atlas in action:
👉 **[atlas.khamel.com](https://atlas.khamel.com)** - Live demo with real content

## 📋 Prerequisites

- **Python 3.9+** installed
- **Git** installed
- **15GB free disk space** (recommended)

## ⚡ Quick Installation

### 1. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/Khamel83/Atlas.git
cd Atlas

# Run the quick install script
./config/quick_install.sh
```

### 2. Start Atlas
```bash
# Start all services
python atlas_service_manager.py start --daemon

# Check status
python atlas_status.py
```

### 3. Access Atlas
Open your browser and visit:
- **🏠 Main Dashboard**: http://localhost:7444
- **📱 Mobile Interface**: http://localhost:7444/mobile
- **📚 API Docs**: http://localhost:7444/docs
- **🧠 AI Features**: http://localhost:7444/ask/

## 📱 Add Content

### Web Interface
1. Go to http://localhost:7444
2. Click "Add Content"
3. Paste any URL or upload files

### iOS Shortcuts (Recommended)
```bash
# Install iOS shortcuts
./config/install_shortcuts.sh
```

Then say: **"Hey Siri, save to Atlas"** to capture content from any app!

## 🔧 Configuration

Edit `.env` file to customize:
```env
# Change port if needed
API_PORT=7444

# Add AI API keys (optional)
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

## ❓ Troubleshooting

### Service Won't Start
```bash
# Check detailed status
python atlas_status.py --detailed

# Check logs
tail -f logs/atlas/atlas_service.json.log
```

### Port Already in Use
```bash
# Change port in .env file
echo "API_PORT=8080" >> .env

# Restart services
python atlas_service_manager.py restart
```

### Database Issues
```bash
# Check database health
python -c "from helpers.database_config import test_database_integrity; print(test_database_integrity())"
```

## 🎯 What to Do Next

1. **📚 Read the [Full Documentation](README.md)**
2. **🔍 Try the [AI Features](http://localhost:7444/ask/)**
3. **📱 Set up [iOS Integration](config/install_shortcuts.sh)**
4. **🔧 Explore [Configuration Options](.env.template)**

## 🆘 Need Help?

- **📖 Documentation**: [docs/](docs/)
- **🐛 Issues**: [GitHub Issues](https://github.com/Khamel83/Atlas/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Khamel83/Atlas/discussions)

---

**🎉 Welcome to Atlas!** Your personal AI knowledge system is ready to transform how you capture, organize, and discover information.