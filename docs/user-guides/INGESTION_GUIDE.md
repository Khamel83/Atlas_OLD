# Atlas Content Ingestion User Guide

This guide provides step-by-step instructions for every way to get content into Atlas. Whether you're saving web articles, processing documents, or capturing voice memos, this guide will help you successfully ingest content into your Atlas system.

## Table of Contents

0. [Setup: Install iOS Shortcuts](#setup-install-ios-shortcuts)
1. [Articles](#articles)
2. [Documents](#documents)
3. [Podcasts](#podcasts)
4. [YouTube Videos](#youtube-videos)
5. [Email Integration](#email-integration)
6. [Voice Memos](#voice-memos)
7. [Screenshots](#screenshots)
8. [Quick Start: Add Your First Content](#quick-start-add-your-first-content)

## Setup: Install iOS Shortcuts

**📱 For Mobile Content Capture:**

Many of the methods in this guide use iOS shortcuts. Install them first:

```bash
# Get mobile installation URL
./get_mobile_url.sh

# Or install from computer
./install_shortcuts.sh
```

Then open the URL on your iPhone and tap each shortcut to install.

**Available Shortcuts:**
- **Capture Thought** - "Hey Siri, save to Atlas"
- **Voice Memo to Atlas** - Audio transcription
- **Screenshot to Atlas** - OCR text extraction
- **Save to Atlas** - Web page capture

## Articles

### How to save web articles

Atlas supports multiple ways to save web articles:

#### Method 1: URL List File
1. Create a text file with one URL per line
2. Save the file as `inputs/articles.txt`
3. Run article ingestion:
   ```bash
   python run.py --articles
   ```

#### Method 2: Instapaper CSV
1. Export your Instapaper library as CSV
2. Save the file as `inputs/instapaper_export.csv`
3. Run article ingestion:
   ```bash
   python run.py --articles
   ```

#### Method 3: Browser Extension
1. Install the Atlas browser extension
2. Click the Atlas icon while browsing any webpage
3. Select "Save Current Page" or "Save Article Content"

#### Method 4: Apple Shortcuts
1. Use the "Save to Atlas" iOS shortcut
2. Share any webpage to the shortcut
3. Content is automatically sent to Atlas

### Supported Article Sources
- Any public webpage URL
- RSS feeds
- News sites
- Blogs
- Research papers
- Documentation

### Troubleshooting Article Ingestion
- **"Failed to fetch" errors**: Try again later or use a different fetching strategy
- **"Content too long"**: Article may be too large for processing
- **"Duplicate content"**: Article has already been processed
- **"Unsupported format"**: URL may not be a standard article

## Documents

### How to process PDFs, Word docs, and text files

Atlas can process various document formats:

#### Method 1: File Drop
1. Place documents in `inputs/New Docs/`
2. Atlas automatically processes new files

#### Method 2: Direct Processing
```bash
python run.py --urls path/to/document_list.txt
```

### Supported Document Formats
- PDF (.pdf)
- Word Documents (.docx)
- Text Files (.txt)
- Markdown (.md)
- HTML (.html)

### Document Processing Features
- Text extraction
- Metadata analysis
- Content categorization
- Search indexing
- Cognitive insights

### Troubleshooting Document Processing
- **"Unsupported format"**: File extension may not be recognized
- **"Corrupted file"**: Document may be damaged
- **"Extraction failed"**: OCR may be needed for scanned documents
- **"Too large"**: Document exceeds size limits

## Podcasts

### How to add RSS feeds and process episodes

Atlas can automatically discover, download, and transcribe podcast episodes:

#### Method 1: OPML Import
1. Export your podcast subscriptions as OPML
2. Save the file as `inputs/podcasts.opml`
3. Run podcast ingestion:
   ```bash
   python run.py --podcasts
   ```

#### Method 2: Direct RSS Feed
1. Add RSS feed URLs to `inputs/podcasts.opml`
2. Run podcast ingestion:
   ```bash
   python run.py --podcasts
   ```

### Podcast Processing Features
- Automatic episode discovery
- Audio download
- Speech-to-text transcription
- Content analysis
- Metadata extraction

### Supported Podcast Sources
- Any RSS feed with audio enclosures
- Major podcast platforms (Apple Podcasts, Spotify, etc.)
- Independent podcasters
- Internal company podcasts

### Troubleshooting Podcast Processing
- **"Feed not found"**: RSS URL may be incorrect
- **"No episodes"**: Feed may be empty or private
- **"Download failed"**: Audio file may be unavailable
- **"Transcription failed"**: Audio quality may be poor

## YouTube Videos

### How to save videos for transcript processing

Atlas can extract transcripts from YouTube videos:

#### Method 1: History Import
1. Export your YouTube watch history
2. Save as `inputs/youtube_history.json`
3. Run YouTube ingestion:
   ```bash
   python run.py --youtube
   ```

#### Method 2: Video URL List
1. Create a text file with YouTube URLs
2. Save as `inputs/youtube.txt`
3. Run YouTube ingestion:
   ```bash
   python run.py --youtube
   ```

### YouTube Processing Features
- Automatic transcript extraction
- Content analysis
- Metadata extraction
- Search indexing
- Cognitive insights

### Supported YouTube Content
- Public videos with captions
- Videos with auto-generated captions
- Playlists
- Channels

### Troubleshooting YouTube Processing
- **"No captions available"**: Video may not have captions enabled
- **"Private video"**: Video may be private or unavailable
- **"Transcript extraction failed"**: Captions may be disabled or corrupted
- **"Rate limited"**: Too many requests in a short time

## Email Integration

### How to forward emails to Atlas

Atlas can process emails sent to a dedicated address:

#### Method 1: IMAP Integration
1. Configure email account in Atlas settings
2. Atlas automatically checks for new emails
3. Emails are processed and indexed

#### Method 2: Forwarding
1. Forward emails to your Atlas email address
2. Atlas processes incoming emails automatically

### Email Processing Features
- Content extraction
- Attachment processing
- Metadata analysis
- Search indexing
- Categorization

### Supported Email Providers
- Gmail
- Outlook/Hotmail
- Yahoo Mail
- Custom IMAP servers
- Corporate email systems

### Troubleshooting Email Processing
- **"Authentication failed"**: Check email credentials
- **"Connection timeout"**: Network or server issues
- **"Attachment too large"**: File exceeds size limits
- **"Unsupported format"**: Email format may not be recognized

## Voice Memos

### How to record and transcribe audio notes

Atlas can process voice memos and transcribe them to text:

#### Method 1: Apple Shortcuts
1. Use the "Voice Memo to Atlas" iOS shortcut
2. Record your voice memo
3. Atlas automatically transcribes and processes

#### Method 2: File Upload
1. Record audio and save as WAV, MP3, or M4A
2. Place file in `inputs/voice_memos/`
3. Atlas processes new files automatically

### Voice Memo Processing Features
- Speech-to-text transcription
- Content analysis
- Metadata extraction
- Search indexing
- Categorization

### Supported Audio Formats
- WAV (.wav)
- MP3 (.mp3)
- M4A (.m4a)
- FLAC (.flac)
- OGG (.ogg)

### Troubleshooting Voice Memo Processing
- **"Transcription failed"**: Audio quality may be poor
- **"Unsupported format"**: File extension may not be recognized
- **"Too long"**: Audio file exceeds duration limits
- **"No speech detected"**: Recording may be empty or silent

## Screenshots

### How to OCR and save image text

Atlas can extract text from screenshots and images:

#### Method 1: Apple Shortcuts
1. Use the "Screenshot to Atlas" iOS shortcut
2. Take a screenshot
3. Atlas automatically OCRs and processes

#### Method 2: File Upload
1. Save images as JPG or PNG
2. Place files in `inputs/screenshots/`
3. Atlas processes new files automatically

### Screenshot Processing Features
- Optical character recognition (OCR)
- Content analysis
- Metadata extraction
- Search indexing
- Categorization

### Supported Image Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- TIFF (.tiff)

### Troubleshooting Screenshot Processing
- **"OCR failed"**: Image quality may be poor
- **"Unsupported format"**: File extension may not be recognized
- **"No text detected"**: Image may not contain readable text
- **"Too large"**: Image file exceeds size limits

## Quick Start: Add Your First Content

### 5-Minute Setup

1. **Create your first article list**:
   ```bash
   echo "https://example.com/article1" > inputs/articles.txt
   echo "https://example.com/article2" >> inputs/articles.txt
   ```

2. **Process your articles**:
   ```bash
   python run.py --articles
   ```

3. **View your content**:
   - Open your web browser to `https://atlas.khamel.com`
   - Navigate to the content management section
   - Browse your processed articles

4. **Try cognitive features**:
   - Visit `https://atlas.khamel.com/ask/html`
   - Explore the Proactive Surfacer, Pattern Detector, and other features

5. **Set up automation**:
   - Create a cron job to run ingestion daily:
     ```bash
     crontab -e
     # Add this line to run daily at 2 AM:
     # 0 2 * * * cd /home/ubuntu/dev/atlas && python run.py --all
     ```

### Next Steps

After your first content is processed:
- Configure email integration for automatic email processing
- Set up podcast feeds for regular episode processing
- Install the browser extension for one-click web capture
- Try the iOS shortcuts for mobile content capture
- Explore cognitive features in the web dashboard

## Troubleshooting Common Ingestion Failures

### General Troubleshooting Steps

1. **Check logs**:
   ```bash
   tail -f logs/atlas_service.log
   ```

2. **Verify Atlas is running**:
   ```bash
   python atlas_service_manager.py status
   ```

3. **Check disk space**:
   ```bash
   df -h
   ```

4. **Restart services**:
   ```bash
   python atlas_service_manager.py restart
   ```

### Common Error Messages and Solutions

- **"Connection refused"**: Atlas service may not be running
- **"Permission denied"**: Check file permissions
- **"File not found"**: Verify file paths and names
- **"Invalid format"**: File may be corrupted or in unsupported format
- **"Rate limited"**: Too many requests - wait and try again
- **"Out of memory"**: System may need more RAM or processing should be reduced

## File Size Limits and Supported Formats

### File Size Limits

- **Articles**: No specific limit (content is fetched from web)
- **Documents**: 100MB maximum
- **Podcasts**: 500MB maximum per episode
- **YouTube Videos**: Transcripts only (no file size limit)
- **Emails**: 25MB maximum including attachments
- **Voice Memos**: 100MB maximum
- **Screenshots**: 50MB maximum

### Supported Formats Summary

| Content Type | Supported Formats |
|--------------|-------------------|
| Articles | Any web URL |
| Documents | PDF, DOCX, TXT, MD, HTML |
| Podcasts | Any RSS feed with audio |
| YouTube | Videos with captions |
| Email | IMAP-compatible providers |
| Voice Memos | WAV, MP3, M4A, FLAC, OGG |
| Screenshots | JPG, PNG, GIF, BMP, TIFF |

## Advanced Ingestion Configuration

### Environment Variables

Configure ingestion behavior through the `.env` file:

```bash
# Article processing
MAX_ARTICLE_RETRIES=3
ARTICLE_TIMEOUT=300
ARTICLE_STRATEGIES=direct,12ft,archive,googlebot,playwright,wayback

# Podcast processing
PODCAST_DOWNLOAD_TIMEOUT=600
PODCAST_MAX_SIZE=524288000  # 500MB in bytes
PODCAST_TRANSCRIPTION_MODEL=base

# YouTube processing
YOUTUBE_TRANSCRIPTION_MODEL=base
YOUTUBE_TIMEOUT=300

# Document processing
DOCUMENT_MAX_SIZE=104857600  # 100MB in bytes
OCR_ENABLED=true
```

### Custom Processing Scripts

Create custom processing scripts in `/scripts/custom_ingestion/`:

```python
#!/usr/bin/env python3
# custom_ingestor.py
from helpers.metadata_manager import MetadataManager
from helpers.config import load_config

def process_custom_content(content, metadata):
    """Custom processing logic"""
    config = load_config()
    manager = MetadataManager(config)
    
    # Your custom processing logic here
    processed_content = content.upper()  # Example transformation
    
    return processed_content
```

## Getting Help

### Community Support

Join the Atlas community:
- Discord: https://discord.gg/atlas
- Reddit: r/AtlasPlatform
- GitHub Discussions: https://github.com/your-username/atlas/discussions

### Professional Support

For enterprise support:
- Email: support@atlas-platform.com
- Phone: +1 (555) 123-4567
- SLA: 24-hour response time

### Reporting Issues

Report bugs and issues on GitHub:
- Repository: https://github.com/your-username/atlas
- Issue Template: Include logs and reproduction steps