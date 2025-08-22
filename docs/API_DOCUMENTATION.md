# Atlas API Documentation

## Overview

The Atlas API provides a unified interface for all cognitive amplification features, content management, and system analytics. It combines both new FastAPI-based endpoints and existing Flask-based services.

## API Structure

### New FastAPI Endpoints

1. **Authentication API** (`/auth/*`)
   - User registration and login
   - API key management
   - JWT token authentication

2. **Content Management API** (`/content/*`)
   - List, create, update, and delete content items
   - Content processing and reprocessing
   - Content statistics and health checks

3. **Cognitive Features API** (`/cognitive/*`)
   - Proactive content surfacing
   - Temporal relationship analysis
   - Socratic question generation
   - Spaced repetition recall
   - Pattern detection and insights

### Existing Flask Endpoints

1. **Analytics API** (`/api/analytics/*`)
   - System metrics
   - Content processing statistics
   - User engagement analytics
   - Dashboard data

2. **Search API** (`/api/search/*`)
   - Full-text search
   - Semantic search
   - Document indexing and management

3. **Capture API** (`/api/capture/*`)
   - Content capture from Apple devices
   - Capture status tracking
   - Recent captures listing

## Authentication

Most endpoints require authentication. You can use either:

1. **JWT Tokens** (for user authentication)
2. **API Keys** (for service-to-service communication)

### Getting a JWT Token

```bash
curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/json" \
     -d '{"username": "user", "password": "password"}'
```

### Using an API Key

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     http://localhost:8000/content/items
```

## Core Endpoints

### Health Check

```bash
GET /health
```

Returns the overall health status of the API.

### Authentication

```bash
POST /auth/register
POST /auth/login
POST /auth/api-keys
GET  /auth/api-keys
DELETE /auth/api-keys/{key_id}
```

### Content Management

```bash
GET    /content/items
GET    /content/items/{content_id}
POST   /content/items
PUT    /content/items/{content_id}
DELETE /content/items/{content_id}
POST   /content/items/{content_id}/process
GET    /content/health
```

### Cognitive Features

```bash
GET  /cognitive/proactive/items
POST /cognitive/proactive/items/{content_id}/mark-surfaced
GET  /cognitive/proactive/stats

GET  /cognitive/temporal/relationships
GET  /cognitive/temporal/insights

POST /cognitive/socratic/questions
GET  /cognitive/socratic/questions/{content_id}

GET  /cognitive/recall/items
POST /cognitive/recall/items/{content_id}/mark-reviewed
GET  /cognitive/recall/analytics

GET  /cognitive/patterns/tags
GET  /cognitive/patterns/insights

GET  /cognitive/health
```

## Running the API

To start the unified API server:

```bash
cd /path/to/atlas
python api/unified_server.py
```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- FastAPI Docs: `http://localhost:8000/docs`
- FastAPI ReDoc: `http://localhost:8000/redoc`