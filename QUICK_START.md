# Atlas Quick Start Guide

This guide provides the bare minimum steps to get Atlas up and running in 10 minutes.

## Prerequisites

- Python 3.9+ installed
- Git installed
- Basic familiarity with command line

## 1. Installation

First, clone the repository and set up the environment:

```bash
# Clone the repository
git clone <repository-url>
cd atlas

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Configuration

Create your configuration file from the template:

```bash
# Copy the template to create your config file
cp .env.template .env
```

Open the `.env` file in a text editor and configure at minimum:

```env
# Optional but recommended: For AI features
OPENROUTER_API_KEY=your_api_key_here
```

**Important**: 
- For full AI-powered features, you'll need an OpenRouter API key
- Without an API key, basic content ingestion will still work
- See `.env.template` for all available configuration options

## 3. Set Up Input Files

Atlas expects input files in the `inputs/` directory:

```bash
# For articles - add URLs one per line
echo "https://example.com/article1" >> inputs/articles.txt
echo "https://example.com/article2" >> inputs/articles.txt

# For YouTube - add video URLs one per line  
echo "https://youtube.com/watch?v=example1" >> inputs/youtube.txt

# For podcasts - add OPML file or URLs
# podcasts.opml should contain your podcast subscriptions
```

## 4. Test Your Setup

Verify everything is working:

```bash
# Test basic functionality
python run.py --help

# Process a few articles to test
python run.py --articles
```

## 5. Running Atlas

With the configuration in place, you can now run Atlas:

```bash
# Process all content types
python run.py --all

# Or process specific types:
python run.py --articles    # Process URLs from inputs/articles.txt
python run.py --youtube     # Process URLs from inputs/youtube.txt  
python run.py --podcasts    # Process OPML from inputs/podcasts.opml

# Process a custom URL file
python run.py --urls path/to/your/urls.txt

# Process Instapaper export
python run.py --instapaper-csv path/to/export.csv

# Recategorize existing content
python run.py --recategorize
```

## 6. Explore Your Data

After processing, your content will be organized in the `DATA_DIRECTORY` you specified:

```
output/
├── articles/
│   ├── metadata/     # JSON metadata for each article
│   ├── markdown/     # Clean markdown content
│   └── html/         # Original HTML (if available)
├── youtube/
│   ├── metadata/     # Video metadata
│   ├── transcripts/  # Video transcripts
│   └── markdown/     # Processed content
└── podcasts/
    ├── metadata/     # Episode metadata
    ├── audio/        # Downloaded audio files
    └── transcripts/  # Audio transcripts
```

## 7. Web Interface (Optional)

Atlas includes cognitive amplification features accessible via web UI:

```bash
# Start the web server
uvicorn web.app:app --reload --port 8000
```

Access the interface at: [http://localhost:8000/ask/html](http://localhost:8000/ask/html)

The web interface provides:
- **Proactive Surfacing**: Rediscover forgotten content
- **Pattern Detection**: Find trends in your content
- **Temporal Analysis**: Time-based content relationships
- **Question Generation**: Socratic questioning for deeper insights
- **Recall Scheduling**: Spaced repetition for knowledge retention

## Troubleshooting

### Common Issues

**"No module named X" errors:**
```bash
# Make sure you're in the virtual environment
source venv/bin/activate
pip install -r requirements.txt
```

**"Permission denied" errors:**
```bash
# Check file permissions and ownership
chmod +x run.py
```

**API rate limits:**
```bash
# Reduce processing speed by adding delays
# Edit your .env file and reduce batch sizes
```

**Empty input files:**
```bash
# Make sure your input files have content
ls -la inputs/
cat inputs/articles.txt
```

### Getting Help

1. Check the full documentation in `docs/`
2. Review configuration options in `.env.example`
3. Run with verbose logging: `LOG_LEVEL=DEBUG python run.py --articles`
4. Check the troubleshooting guide: `docs/environment-troubleshooting.md`

## Next Steps

Once you have Atlas running:

1. **Explore the Web UI** - Try the cognitive amplification features
2. **Set up automation** - Use the scheduler for regular content processing
3. **Customize processing** - Modify configurations for your specific needs
4. **Review the docs** - Learn about advanced features in `docs/`

---

*This quick start gets you running with Atlas. For detailed configuration options and advanced features, see the full documentation in the `docs/` directory.*