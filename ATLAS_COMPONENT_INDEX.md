# Atlas Component Index

**Purpose**: Know what exists before building new functionality  
**Updated**: Auto-generated from codebase analysis

---

## 🎯 **CORE PROCESSING CAPABILITIES**

### **Article Processing** ✅ PHASE 3 COMPLETE
- **Primary**: `helpers/article_manager.py` (Phases 3&4 consolidation complete)
- **Interface**: `helpers/base_article_strategy.py` (standardized strategy interface)
- **Compatibility**: `helpers/article_compatibility.py` (backward compatibility layer)
- **Strategies**: 9 unified strategies with intelligent cascade and statistics
- **Use For**: Any URL content fetching, bulk processing, paywall bypass, error recovery
- **Features**: Real-time success tracking, bulk processing, failed article recovery
- **Don't Rebuild**: Article fetching, strategy management, statistics tracking

### **Transcript Processing** 
- **Primary**: `helpers/transcript_manager.py` (after Phase 2 consolidation)
- **Sources**: ATP, Network scrapers, Universal discovery  
- **Use For**: Podcast transcripts, search, enhancement, indexing
- **Don't Rebuild**: Transcript scraping, podcast processing, search

### **Content Processing** ✅ PHASE 4 COMPLETE
- **Primary**: `helpers/content_pipeline.py` (Phase 4 consolidation complete)
- **Integration**: `helpers/content_integration.py` (unified workflows)
- **Unified Interface**: `UnifiedContentProcessor` for complete article→content processing
- **Pipeline Stages**: 9 configurable stages (detect, classify, process, extract, summarize, cluster, analyze, insights, export)
- **Use For**: Complete content analysis, multi-stage processing, quality scoring
- **Features**: Configurable pipeline, bulk processing, comprehensive statistics
- **Don't Rebuild**: Content processing pipelines, quality analysis, multi-format export

---

## 🔧 **INFRASTRUCTURE & UTILITIES**

### **Configuration Management**
- **Primary**: `helpers/config.py` + `config/atlas.yaml`
- **Use For**: All configuration needs, environment variables, settings
- **Don't Rebuild**: Config loading, environment management

### **Search & Indexing**
- **Primary**: `helpers/search_engine.py`, search indices
- **Use For**: Full-text search, content discovery, ranking
- **Don't Rebuild**: Search infrastructure, indexing systems

### **Background Processing**
- **Primary**: Unified background service
- **Use For**: Scheduled tasks, continuous processing, monitoring
- **Don't Rebuild**: Service management, scheduling systems

---

## 📊 **INTEGRATION POINTS**

### **External APIs**
- **YouTube**: `helpers/youtube_ingestor.py`
- **Email**: `helpers/email_ingestor.py` + auth manager
- **Apple**: `apple_shortcuts/` directory
- **AI Services**: Model selector, API clients

### **Storage & Export**
- **Database**: SQLite with search indices
- **Export Formats**: Markdown, JSON, HTML, Anki, Notion
- **File Management**: Organized output structure

---

## ⚡ **DECISION FRAMEWORK**

**Before building anything new, ask:**

1. **Does this fit into an existing component?**
   - Article processing → ArticleManager
   - Transcript work → TranscriptManager  
   - Content analysis → ContentPipeline

2. **Is this a new integration?**
   - Add to `integrations/` directory
   - Use existing auth patterns
   - Follow established API patterns

3. **Is this infrastructure?**
   - Extend existing utilities
   - Use unified configuration
   - Integrate with monitoring

**Only create new components for genuinely new problem domains**

---

## 🎯 **COMPONENT HEALTH STATUS**

### **Consolidated (Phase 2+)**
- ✅ TranscriptManager - Single source for all transcript processing
- ✅ ArticleManager - Single source for all article processing  
- ✅ ContentPipeline - Single source for all content processing

### **Established & Stable**
- ✅ Configuration system - `config/atlas.yaml`
- ✅ Search infrastructure - Full-text + ranking
- ✅ Background services - Unified processing

### **Integration Points** 
- ✅ YouTube API integration
- ✅ Email processing pipeline
- ✅ Apple Shortcuts framework

---

**UPDATE THIS INDEX**: After each major feature addition or consolidation