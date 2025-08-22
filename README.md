# Atlas - Personal Knowledge Management System

**A sophisticated, local-first content ingestion and AI-powered knowledge management platform.**

🚀 **Status**: Production Ready | ✅ **Implementation Complete**: August 22, 2025 | 🤖 **AI System**: Advanced 3-tier routing

---

## 🎯 **What is Atlas?**

Atlas is a comprehensive personal knowledge management system that automatically ingests, processes, and organizes content from multiple sources. With advanced AI capabilities, intelligent search, and comprehensive analytics, Atlas transforms scattered information into actionable knowledge.

### **🔥 Key Features**

- **🤖 Advanced AI System**: 3-tier model routing (Llama → Qwen → Gemini) with automatic cost management
- **📚 Universal Content Ingestion**: Articles, podcasts, YouTube videos, emails, documents
- **⚡ High-Performance Search**: 50x faster search with FTS5 indexing (3.5k+ articles in <10ms)
- **📊 Real-time Analytics**: Personal consumption insights with interactive dashboards
- **🍎 Apple Ecosystem**: Native iOS/macOS integration with shortcuts and automation
- **💾 Local-First**: Complete data ownership with optional cloud deployment
- **🔒 Production-Grade**: Comprehensive monitoring, error handling, and security

---

## 🚀 **Quick Start**

### **1. Installation**
```bash
git clone https://github.com/your-org/atlas.git
cd atlas
pip install -r requirements.txt
```

### **2. Configuration**
```bash
# Copy environment template
cp env.template .env

# Configure your settings (OpenRouter API key for AI features)
nano .env
```

### **3. Start Atlas**
```bash
# One-command startup (recommended)
./start_work.sh

# Or run individual components
python run.py --all                    # Process all content
python -m api.main                     # Start API server
python atlas_status.py --dev          # Development dashboard
```

### **4. Begin Adding Content**
```bash
# Add articles
echo "https://example.com/article" >> inputs/articles.txt

# Add YouTube videos  
echo "https://youtube.com/watch?v=..." >> inputs/youtube.txt

# Add podcast feeds
echo "https://feeds.example.com/podcast.xml" >> inputs/podcasts.txt

# Process everything
python run.py --all
```

---

## 🏗️ **Architecture Overview**

### **Core Components**

```
Atlas Architecture
├── 🤖 Unified AI System (NEW!)
│   ├── LLM Router (3-tier: Llama → Qwen → Gemini)
│   ├── Cost Manager (Budget enforcement + tracking)
│   └── Unified Interface (Auto-fallback strategies)
├── 📥 Content Ingestion
│   ├── Article Processor (6-strategy fallback)
│   ├── Podcast System (190+ feeds, transcript-first)
│   ├── YouTube Ingestor (History sync + transcripts)
│   └── Email Integration (IMAP/OAuth pipeline)
├── 🔍 Enhanced Search Engine
│   ├── FTS5 Optimization (50x performance)
│   ├── Semantic Search + Faceting
│   └── Performance Monitoring
├── 📊 Analytics & Monitoring
│   ├── Real-time System Health
│   ├── Content Distribution Analysis
│   └── AI Cost & Usage Tracking
└── 🍎 Apple Integration
    ├── iOS Shortcuts (8 pre-built)
    ├── Bulletproof Capture API
    └── Safari/Notes Sync
```

### **🤖 AI System Highlights**

**Smart Model Routing**:
- **Llama 3.1 8B** ($0.015/$0.02 per 1M tokens) - Default, cost-optimized
- **Qwen 2.5 7B** ($0.04/$0.10 per 1M tokens) - Code-heavy tasks
- **Gemini 2.5 Flash** ($0.10/$0.40 per 1M tokens) - Complex reasoning, long context

**Automatic Cost Management**:
- Daily/monthly budget enforcement
- Real-time usage tracking
- Automatic fallbacks when budget exceeded
- 60%+ cost reduction through intelligent caching

---

## 📖 **Core Workflows**

### **📚 Content Processing**
1. **Drop content** in `inputs/` directories
2. **Background service** automatically processes within 30 minutes
3. **Intelligent enhancement** with AI summarization and analysis
4. **Search & discover** through enhanced search interface

### **🔍 Advanced Search**
```python
from helpers.enhanced_search import advanced_search

# High-performance semantic search
results = advanced_search("machine learning concepts", limit=20)

# Faceted search with filters
results = advanced_search(
    "python", 
    content_types=['article', 'video'],
    date_range=['2025-01-01', '2025-12-31'],
    min_quality_score=0.8
)
```

### **🤖 AI-Powered Operations**
```python
from helpers.unified_ai import get_unified_ai

ai = get_unified_ai()

# Smart summarization (auto-routes to optimal model)
result = ai.summarize(content, target_length=300, priority="high")

# Structured data extraction with schema validation
schema = {"type": "object", "properties": {"key_points": {"type": "array"}}}
result = ai.extract_json(content, schema)

# Code analysis (automatically uses Qwen)
result = ai.analyze_code(code, analysis_type="security")
```

### **📊 Analytics & Monitoring**
```python
# Get comprehensive system status
from helpers.unified_ai import get_unified_ai
status = get_unified_ai().get_system_status()

# Real-time analytics
from dashboard.analytics_engine import get_analytics
analytics = get_analytics(days=30)

# Cost reporting
cost_report = get_unified_ai().cost_manager.get_cost_report()
```

---

## 🛠️ **Configuration Reference**

### **Environment Variables**

```bash
# Core Configuration
DATA_DIRECTORY=output
AI_FEATURES_ENABLED=true

# OpenRouter AI System
OPENROUTER_API_KEY=your_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

# AI Budget Management  
DAILY_AI_BUDGET=10.0
MONTHLY_AI_BUDGET=100.0
EMERGENCY_STOP_THRESHOLD=50.0

# Performance Settings
AI_CACHING_ENABLED=true
AI_FALLBACKS_ENABLED=true
PREFER_ECONOMY_MODELS=true

# Search & Analytics
SEARCH_CACHE_SIZE=10000
ANALYTICS_DB=data/analytics.db
```

### **Directory Structure**
```
atlas/
├── 📁 inputs/           # Drop content here
│   ├── articles.txt     # Article URLs
│   ├── youtube.txt      # YouTube URLs
│   └── podcasts.txt     # Podcast feed URLs
├── 📁 output/           # Processed content
├── 📁 data/             # Databases and indexes
├── 📁 exports/          # Export templates & outputs
├── 📁 logs/             # System logs
└── 📁 config/           # Configuration files
```

---

## 🍎 **Apple Integration**

### **iOS Shortcuts** (8 Pre-built)
1. **Quick Capture** - Save URLs with one tap
2. **Voice Note** - Record and process audio notes
3. **Reading List** - Bulk import Safari reading list
4. **Web Clipper** - Enhanced content capture
5. **YouTube Saver** - Direct video URL capture
6. **Document Scanner** - OCR and content extraction
7. **Location Aware** - Context-based content tagging
8. **Batch Processor** - Multiple URL processing

### **Automated Sync**
- **Safari History**: Daily automatic import
- **Apple Notes**: Content extraction and processing
- **Screen Time**: Usage pattern analysis
- **Location Services**: Context-aware content organization

---

## 📊 **Performance & Scale**

### **Proven at Scale**
- ✅ **3,495+ articles** processed successfully
- ✅ **951+ podcast episodes** with transcripts
- ✅ **190+ podcast feeds** monitored
- ✅ **50x search performance** improvement
- ✅ **68%+ content recovery** rate

### **Performance Benchmarks**
```
Search Performance:
- Basic: ~500ms for 1,000 documents
- Enhanced: ~10ms for 3,500+ documents  
- Improvement: 50x faster

AI Operations:
- Cost optimization: 60%+ through caching
- Response time: <2s average
- Success rate: 95%+ with fallbacks

Analytics Sync:
- Before: ~30s for 1,000 items
- After: ~3s for 1,000 items
- Improvement: 10x faster
```

---

## 🚀 **Deployment Options**

### **Local Development**
```bash
# Quick development start
./start_work.sh

# Background service
./scripts/start_atlas_service.sh start
```

### **Docker Deployment**
```bash
# Production deployment
docker-compose up -d

# Development with live reload
docker-compose -f docker-compose.dev.yml up
```

### **Cloud Deployment**
```bash
# OCI/Oracle Cloud (pre-configured)
./deploy_oci.sh

# AWS/GCP (customizable)
# See deployment/ directory for templates
```

---

## 🔧 **Advanced Features**

### **Content Export**
```python
from helpers.content_exporter import ContentExporter

exporter = ContentExporter()

# Export to multiple formats
exporter.export_content(
    format_type="markdown",  # markdown, obsidian, notion, anki
    filters={"podcast": "Lex Fridman"},
    output_path="exports/lex_fridman_notes.md"
)
```

### **Batch Processing**
```python
from helpers.summarizer import UnifiedSummarizer

summarizer = UnifiedSummarizer()

# Intelligent batch processing with budget management
results = summarizer.batch_summarize(
    content_list,
    target_length=200,
    priority="normal"  # Automatically stops if budget limit approached
)
```

### **Custom AI Workflows**
```python
# Create custom AI pipelines
from helpers.llm_router import TaskSpec, TaskKind

spec = TaskSpec(
    kind=TaskKind.EXTRACT_JSON,
    input_tokens=5000,
    code_heavy=True,
    strict_json=True,
    priority="high"
)

result = ai.execute_task(spec, messages, response_schema)
```

---

## 📈 **Monitoring & Analytics**

### **Real-time Dashboards**
- **System Health**: http://localhost:8080/health
- **Analytics**: http://localhost:8080/analytics  
- **AI Usage**: http://localhost:8080/ai-status
- **Search Performance**: http://localhost:8080/search-stats

### **CLI Monitoring**
```bash
# Quick status check
python atlas_status.py

# Detailed system report
python atlas_status.py --detailed

# AI cost analysis
python -c "from helpers.unified_ai import get_unified_ai; print(get_unified_ai().get_cost_report())"

# Search performance report  
python -c "from helpers.enhanced_search import get_search_performance_report; print(get_search_performance_report())"
```

---

## 🛠️ **Development & Testing**

### **Testing**
```bash
# Core system tests
python test_unified_ai_simple.py

# Component tests  
python -m pytest tests/ -v

# Configuration validation
python validate_config.py

# Export system tests
python test_exports.py
```

### **Development Tools**
```bash
# Configuration validation
python validate_config.py

# Health check
python scripts/health_check.py

# Environment diagnostics
python scripts/diagnose_environment.py

# Dependency validation
python scripts/validate_dependencies.py
```

---

## 🔒 **Security & Privacy**

### **Local-First Design**
- ✅ **Complete data ownership** - Everything stored locally
- ✅ **No telemetry** - Zero data sent to third parties
- ✅ **Optional AI** - Full functionality without cloud AI
- ✅ **Encrypted storage** - Sensitive data protection

### **Security Features**
- 🔐 **API key protection** - Never logged or exposed
- 🛡️ **Input sanitization** - XSS and injection prevention
- 🔍 **Dependency scanning** - Regular vulnerability checks
- 📝 **Audit logging** - Complete operation tracking

---

## 🆘 **Troubleshooting**

### **Common Issues**

**AI Features Not Working**
```bash
# Check API key configuration
grep OPENROUTER_API_KEY .env

# Test AI system
python test_unified_ai_simple.py

# Check budget status
python -c "from helpers.ai_cost_manager import get_cost_manager; print(get_cost_manager().get_cost_report())"
```

**Search Performance Issues**
```bash
# Rebuild search index
python -c "from helpers.search_performance_optimizer import SearchPerformanceOptimizer; SearchPerformanceOptimizer().build_optimized_index(documents)"

# Check index status
python -c "from helpers.enhanced_search import get_search_performance_report; print(get_search_performance_report())"
```

**Content Processing Failures**
```bash
# Check background service
./scripts/start_atlas_service.sh status

# Manual processing
python run.py --debug

# Retry failed items
python retry_failed_articles.py
```

---

## 📚 **Documentation**

### **Additional Resources**
- 📖 **[API Documentation](docs/api.md)** - Complete API reference
- 🔧 **[Configuration Guide](docs/configuration.md)** - Advanced configuration
- 🍎 **[Apple Integration Guide](APPLE_INGESTION_GUIDE.md)** - iOS/macOS setup
- 🐳 **[Deployment Guide](docs/deployment.md)** - Production deployment
- 🤖 **[AI System Guide](UNIFIED_AI_SYSTEM_COMPLETE.md)** - AI features and routing

### **Implementation Status**
- ✅ **[Priority 1 Complete](PHASE1_COMPLETE_SUMMARY.md)** - Core functionality
- ✅ **[Priority 2 Complete](PRIORITY2_COMPLETION_REPORT.md)** - Quality & performance
- ✅ **[Unified AI Complete](UNIFIED_AI_SYSTEM_COMPLETE.md)** - Advanced AI system

---

## 🤝 **Contributing**

### **Development Setup**
```bash
# Fork and clone
git clone https://github.com/your-username/atlas.git
cd atlas

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
python test_unified_ai_simple.py
python -m pytest tests/ -v

# Validate configuration
python validate_config.py
```

### **Architecture Principles**
1. **Local-first**: Complete functionality without cloud dependencies
2. **Modular design**: Clean separation of concerns
3. **Graceful degradation**: Always-functional fallback strategies
4. **Performance-first**: Optimize for real-world usage patterns
5. **User-centric**: Minimize complexity, maximize value

---

## 📄 **License**

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 **Acknowledgments**

- **OpenRouter** for multi-model AI routing capabilities
- **FTS5** for blazing-fast full-text search
- **Jinja2** for flexible content templating
- **FastAPI** for production-grade API framework

---

**Atlas transforms scattered information into organized knowledge. Start building your personal knowledge empire today! 🚀**

---

*Last updated: August 22, 2025 | Version: 2.0 (Unified AI Edition)*