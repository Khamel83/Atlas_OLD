# Atlas Project - Qwen Context Document

This document provides essential context about the Atlas project for Qwen Code, an interactive CLI agent. It covers the project's purpose, structure, key components, and development guidelines.

## Project Overview

**Atlas** is a sophisticated local-first content ingestion and cognitive amplification platform. It processes articles, YouTube videos, and podcasts into structured knowledge for enhanced thinking and insight generation. The platform is designed to amplify human cognitive capabilities through automated content processing, intelligent analysis, and proactive knowledge surfacing.

### Core Philosophy

Atlas represents a fundamental shift from **passive content storage** to **active cognitive amplification**:

- **Local-First**: All data stored locally on your machine. No cloud dependencies for core features.
- **Cognitive Enhancement**: Tools that amplify human thinking, not just organize information.
- **Resilient Processing**: Handles failures gracefully with comprehensive retry mechanisms.
- **Structured Output**: Clean, portable Markdown ready for any knowledge management system.
- **Privacy-Preserving**: Optional AI features with user-controlled API usage.

### Key Features

1. **Content Ingestion Pipeline**
   - Article Processing: 6-strategy fallback system (Direct HTTP → 12ft.io → Archive.today → Googlebot → Playwright → Wayback)
   - YouTube Integration: Transcript extraction with multi-language support
   - Podcast Processing: OPML parsing and episode download with transcription
   - Robust Retry System: Comprehensive failure handling with persistent queues

2. **Cognitive Amplification Features**
   - Proactive Surfacer: Rediscovers forgotten or stale content for review
   - Temporal Engine: Finds time-aware relationships between content items
   - Socratic Question Generator: Generates deep questions to enhance understanding
   - Active Recall Engine: Schedules spaced repetition for knowledge retention
   - Pattern Detector: Identifies trends in tags, sources, and content patterns

3. **Web Dashboard & API**
   - Interactive web interface for accessing cognitive features
   - RESTful API for programmatic access to all features

## Project Structure

```
Atlas/
├── run.py                    # Main CLI entry point
├── helpers/                  # Core processing modules
│   ├── article_fetcher.py   # Article ingestion (929 lines)
│   ├── youtube_ingestor.py  # YouTube processing (545 lines) 
│   ├── podcast_ingestor.py  # Podcast processing (267 lines)
│   ├── metadata_manager.py  # Content metadata management
│   ├── path_manager.py      # File system organization
│   └── ...                  # 19 supporting modules
├── ask/                      # Cognitive amplification features
│   ├── proactive/           # Content surfacing
│   ├── temporal/            # Time relationships
│   ├── socratic/            # Question generation
│   ├── recall/              # Spaced repetition
│   └── insights/            # Pattern detection
├── web/                      # Web interface
│   ├── app.py               # FastAPI application
│   └── templates/           # HTML templates
├── ingest/                   # Advanced processing pipeline
├── process/                  # Content analysis
├── tests/                    # Comprehensive test suite
├── inputs/                   # Input files (articles.txt, etc.)
└── output/                   # Processed content storage
```

## Development Environment

### Prerequisites

- Python 3.9+
- Git
- Virtual environment (recommended)

### Setup

1. Clone the repository
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the environment:
   ```bash
   cp .env.template .env
   ```

### Configuration

The minimum `.env` setup:
```env
# No mandatory configuration needed to run the application
# but for full AI features, you'll need an OpenRouter API key
OPENROUTER_API_KEY=your_api_key_here
```

For full AI features:
```env
OPENROUTER_API_KEY=your_api_key_here
MODEL=google/gemini-2.0-flash-lite-001
```

## Core Components

### Main Entry Point (`run.py`)

This is the primary CLI interface for running Atlas pipelines. It supports various commands for processing different content types:

- `--articles`: Run article ingestion
- `--podcasts`: Run podcast ingestion
- `--youtube`: Run YouTube ingestion
- `--instapaper-csv`: Process Instapaper CSV file
- `--recategorize`: Run recategorization
- `--all`: Run all ingestion types
- `--urls`: Process URLs from a file

### Helpers

The `helpers/` directory contains core modules for content processing:

- `article_fetcher.py`: Implements the 6-strategy article fetching system
- `podcast_ingestor.py`: Handles podcast feed parsing and episode processing
- `youtube_ingestor.py`: Manages YouTube video ingestion and transcript extraction
- `metadata_manager.py`: Centralized metadata handling for all content types
- `path_manager.py`: Standardized path creation and management
- `config.py`: Configuration loading and management

### Cognitive Features (`ask/`)

The `ask/` directory implements the cognitive amplification features:

- `proactive/`: Proactive content surfacing
- `temporal/`: Time-aware content relationships
- `socratic/`: Socratic question generation
- `recall/`: Spaced repetition scheduling
- `insights/`: Pattern detection and content analysis

### Web Interface (`web/`)

The web interface is built with FastAPI and provides:

- A dashboard for accessing cognitive features
- RESTful API endpoints for all functionality
- HTML templates for rendering the UI

## Development Guidelines

### Code Quality

- Follow existing code patterns and conventions
- Use type hints for all functions
- Write comprehensive docstrings
- Implement robust error handling with logging

### Testing

Atlas includes a comprehensive testing infrastructure:

- Unit tests for individual modules
- Integration tests for end-to-end pipelines
- Run tests with `pytest`
- Aim for high test coverage

### Contributing

All development should be done in feature branches with Pull Requests. Never push directly to `main`.

## Current Status

As of January 2025, Atlas is a functional cognitive amplification platform with:

- Complete content ingestion pipeline
- Full cognitive amplification suite
- Robust error handling and retry mechanisms
- Comprehensive testing infrastructure

The immediate focus is on documentation improvements, configuration streamlining, and advanced feature completion.

## Next Steps

Based on the project roadmap, key areas for development include:

1. **Infrastructure Stability**: Environment setup, testing infrastructure, and documentation accuracy
2. **Advanced Features**: Full-text search, semantic search, and knowledge graph construction
3. **Performance Optimization**: Caching, memory management, and concurrent processing
4. **User Experience**: Simplified setup, better error messages, and enhanced web interface

## Useful Commands

### Running Atlas

```bash
# Process articles from inputs/articles.txt
python run.py --articles

# Process YouTube videos from inputs/youtube.txt  
python run.py --youtube

# Process podcasts from inputs/podcasts.opml
python run.py --podcasts

# Process everything
python run.py --all
```

### Background Service

```bash
# Start the background service
./scripts/start_atlas_service.sh start

# Check service status
./scripts/start_atlas_service.sh status
```

### Testing

```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/unit/
pytest tests/integration/
```

### Status Check

```bash
# Quick status
python atlas_status.py

# Detailed status
python atlas_status.py --detailed
```