# Atlas v2: Event-Driven Content Pipeline

**Transform any URL into searchable knowledge.** Atlas v2 is a lean, event-driven content processing system optimized for free infrastructure that preserves all your data forever.

## 🎯 What Atlas v2 Does

- **URL → Knowledge:** Send any podcast, article, or video URL → get structured, searchable content
- **Event-Driven:** Immediate processing when you encounter content (via Vejla integration)
- **Data Preservation:** Never loses data, migrates all existing content
- **Free Forever:** Runs on OCI Always-Free ARM instance ($0/month indefinitely)
- **Zero Maintenance:** Set it and forget it

## 🚀 Quick Start

### Local Development

```bash
# Clone and start
git clone <atlas-v2-repo>
cd atlas_v2

# Start with Docker
docker-compose up -d

# Test webhook
curl -X POST http://localhost:8000/webhook/vejla \
  -H "Content-Type: application/json" \
  -d '{"type":"podcast","url":"https://acquired.fm/episodes/berkshire-hathaway-2024","source":"Acquired"}'

# Check status
curl http://localhost:8000/health
```

### OCI Always-Free Deployment

```bash
# SSH to OCI instance
ssh -i ~/.ssh/oci_key ubuntu@<your-oci-ip>

# Install Docker
sudo apt update && sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER && newgrp docker

# Deploy Atlas v2
git clone <atlas-v2-repo> && cd atlas_v2
docker-compose up -d

# Verify running
curl http://localhost:8000/health
```

## 📊 Your Data Scale (Discovered)

Atlas v2 discovered significantly more data than expected:

- **25,831** total content items
- **13,209** large content pieces (>10K chars)
- **9,454** podcast transcripts
- **1,997** email archives
- **1,754** articles
- **5,337** episode queue items (5,163 pending)
- **33,303** markdown files
- **102,009** JSON files

**All data will be preserved and migrated to Atlas v2.**

## 🏗️ Architecture

### Event-Driven Pipeline
```
Vejla URL → Webhook → INGEST → EXTRACT → VALIDATE → STORE
                          ↓
                    Backlog Processor (every 6 hours)
```

### Content Lifecycle
1. **INGEST**: Raw content saved to `content/raw/{id}.html`
2. **EXTRACT**: Convert to markdown, save to `content/processed/{id}.md`
3. **VALIDATE**: Quality checks (word count, content type validation)
4. **STORE**: Update database, create metadata JSON

### Unique ID System
Every piece of content gets ONE immutable ID:
- `hardfork-podcast-123-2025-09-29-ai-regulation`
- `stratechery-newsletter-2025-09-29-bundling-unbundling`
- `acquired-podcast-2025-09-29-tobi-lutke-interview`

## 📱 Vejla Integration

**Seamless URL Capture:** Any URL you encounter → automatically processed

1. Install [Vejla](https://sindresorhus.com/velja) on macOS
2. Configure rules to send podcast/article URLs to Atlas v2 webhook
3. Create Shortcuts automation for webhook calls
4. URLs get processed immediately when you encounter them

[→ Complete Vejla Setup Guide](VEJLA_INTEGRATION.md)

## 🆓 Forever-Free Infrastructure

**OCI Always-Free Tier:**
- 4 ARM cores, 24GB RAM
- 200GB storage, 10TB/month network
- **Cost: $0/month indefinitely**
- Caveat: Login every 90 days (not a cost, just account maintenance)

**Atlas v2 Resource Usage:**
- RAM: 2-4GB typical, 8GB peak
- CPU: <20% (I/O-bound)
- Storage: 50GB (room for 50K transcripts)

## 🔧 Configuration

All configuration via CSV/JSON files - no code changes needed:

### `config/sources.csv`
```csv
source_name,type,rss_url,website_url,extraction_method,rate_limit_seconds,priority,enabled
Hard Fork,podcast,https://feeds.megaphone.fm/hardfork,https://www.nytimes.com/column/hard-fork,direct_site,3,1,true
Stratechery,newsletter,,https://stratechery.com,article_page,5,1,true
Acquired,podcast,https://acquired.fm/rss,https://www.acquired.fm,direct_site,2,1,true
```

### Webhook Authentication
```bash
# Set secure webhook token
echo "WEBHOOK_SECRET_TOKEN=your-secure-token" > .env
```

## 📈 Monitoring

### Health Check
```bash
curl http://localhost:8000/health
```

### Processing Stats
```bash
curl http://localhost:8000/stats
```

### Logs
```bash
docker logs atlas-v2 --tail 50
```

## 🔄 Data Migration

Atlas v2 includes comprehensive migration from your existing Atlas installation:

```python
# Run migration script
python atlas_v2_migration.py

# Preserves:
# - All 25,831 content items
# - All 5,337 queue items
# - All processing history
# - All metadata
```

**Migration guarantees:**
- ✅ No data loss
- ✅ All URLs preserved
- ✅ All content preserved
- ✅ Original data kept as backup

## 🛡️ OOS Integration

Atlas v2 integrates with OOS (development process tool) while maintaining clear boundaries:

- **Atlas = The Product** (what you're building)
- **OOS = Development Process** (how you build it)

**Communication:** Atlas → `oos_requests.txt` → OOS processes independently

**OOS provides:**
- Token optimization (40-60% reduction)
- Git hooks (prevent API key commits)
- Slash commands (`/optimize`, `/smart-commit`)

## 🔍 Content Processing

### Quality Validation
- **Podcasts:** Word count matches duration (80 WPM ± 50%)
- **Articles:** Minimum 1,000 words
- **Transcripts:** >10,000 characters
- **All content:** Not mostly navigation/boilerplate

### Extraction Patterns
Site-specific extraction rules in `config/extraction_patterns.json`:
```json
{
  "acquired.fm": {
    "transcript_selector": "div.rich-text-block-6",
    "min_chars": 10000
  }
}
```

### Rate Limiting
- Domain-specific limits
- Hourly quotas
- Respectful crawling

## 📁 File Structure

```
atlas_v2/
├── main.py                 # FastAPI application
├── modules/
│   ├── database.py         # SQLite async operations
│   ├── id_generator.py     # Unique ID generation
│   ├── processor.py        # Content processing pipeline
│   └── validator.py        # Quality validation
├── config/
│   ├── sources.csv         # Content sources
│   └── extraction_patterns.json
├── content/
│   ├── raw/               # Original HTML/XML
│   ├── processed/         # Markdown + JSON metadata
│   └── failed/           # Failed extraction logs
├── data/
│   └── atlas_v2.db       # SQLite database
└── logs/
    └── atlas_v2.log      # Application logs
```

## 🎯 Success Criteria

Atlas v2 is successful when:

- ✅ **Data Preserved:** All 25,831 items migrated
- ✅ **Event-Driven:** Vejla webhooks process in <60 seconds
- ✅ **Free Forever:** OCI Always-Free deployment
- ✅ **Zero Re-fetching:** Never downloads existing content
- ✅ **CSV Config:** All changes via config files
- ✅ **Portable:** Same Docker image runs everywhere
- ✅ **Low Maintenance:** <15 minutes/week

## 🚨 Critical Principles

1. **Never Lose Data:** All original data preserved
2. **Never Re-fetch:** Check existence before downloading
3. **Event-Driven First:** Immediate processing via webhooks
4. **Configurable:** CSV/JSON for all behavior
5. **Free Forever:** OCI Always-Free compatible
6. **Portable:** Docker runs on OCI/RPi4/Mac Mini

## 📚 Documentation

- [Vejla Integration Guide](VEJLA_INTEGRATION.md) - URL capture automation
- [OCI Deployment Guide](OCI_DEPLOYMENT.md) - Free cloud hosting
- [Migration Guide](MIGRATION.md) - Preserve existing data
- [API Reference](API.md) - Webhook and REST endpoints

## 🤝 Support

- **Issues:** Create issues in this repo
- **Questions:** Check existing documentation first
- **Contributions:** Follow [contribution guidelines](CONTRIBUTING.md)

---

**Atlas v2: Transform any URL into searchable knowledge, automatically, forever free.**