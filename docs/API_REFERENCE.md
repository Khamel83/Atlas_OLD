# Atlas API Reference

Complete API documentation for the Atlas content processing and search system.

## Base URL

```
http://localhost:8000/api/v1/
```

## Authentication

Currently, Atlas operates in single-user mode without authentication. All endpoints are publicly accessible on the configured host and port.

## Content-Type

All API responses return `application/json` unless otherwise specified.

## Rate Limiting

- **Default limits**: 100 requests/minute, 1000 requests/hour per IP
- **Rate limit headers** included in responses:
  - `X-RateLimit-Limit`: Maximum requests allowed
  - `X-RateLimit-Remaining`: Requests remaining in current window
  - `X-RateLimit-Reset`: Time when the rate limit resets

## API Endpoints

### Health Check

Check API server health and connectivity.

```http
GET /health
```

**Response**
```json
{
    "status": "healthy"
}
```

**Status Codes**
- `200` - Service healthy
- `503` - Service unavailable

---

### Search Content

Search across all indexed content with filtering and ranking.

```http
GET /search/
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string | Yes | Search query |
| `type` | string | No | Content type filter (`article`, `document`, `podcast`, `youtube`) |
| `limit` | integer | No | Number of results (default: 10, max: 100) |
| `after` | string | No | ISO date for results after this date |
| `before` | string | No | ISO date for results before this date |
| `sort` | string | No | Sort order (`relevance`, `date`, `title`) |

**Example Requests**

```bash
# Basic search
GET /search/?q=artificial intelligence

# Filtered search
GET /search/?q=python&type=document&limit=20

# Date-filtered search  
GET /search/?q=technology&after=2024-01-01&sort=date
```

**Response**
```json
{
    "results": [
        {
            "id": "12345",
            "title": "Introduction to Machine Learning",
            "content_type": "article",
            "url": "https://example.com/ml-intro",
            "excerpt": "Machine learning is a subset of artificial intelligence...",
            "score": 0.85,
            "created_at": "2024-03-15T10:30:00Z",
            "word_count": 2500,
            "tags": ["AI", "machine learning", "technology"]
        }
    ],
    "total": 42,
    "query": "artificial intelligence",
    "filters": {
        "type": null,
        "after": null,
        "before": null
    },
    "processing_time_ms": 23.5
}
```

**Status Codes**
- `200` - Success
- `400` - Invalid query parameters
- `429` - Rate limit exceeded

---

### Get Content

Retrieve content items with optional filtering and pagination.

```http
GET /content/
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | string | No | Content type filter |
| `limit` | integer | No | Number of items (default: 10, max: 100) |
| `offset` | integer | No | Pagination offset (default: 0) |
| `sort` | string | No | Sort order (`date`, `title`, `type`) |
| `order` | string | No | Sort direction (`asc`, `desc`) |

**Example Requests**

```bash
# Get recent articles
GET /content/?type=article&limit=20&sort=date&order=desc

# Paginated content
GET /content/?limit=50&offset=100
```

**Response**
```json
{
    "items": [
        {
            "id": "12345",
            "title": "Sample Article Title",
            "content_type": "article",
            "url": "https://example.com/article",
            "summary": "Brief summary of the content...",
            "created_at": "2024-03-15T10:30:00Z",
            "updated_at": "2024-03-15T10:30:00Z",
            "word_count": 1250,
            "read_time_minutes": 5,
            "tags": ["technology", "programming"],
            "metadata": {
                "author": "John Doe",
                "published_date": "2024-03-15",
                "source": "example.com"
            }
        }
    ],
    "total": 1250,
    "limit": 20,
    "offset": 0,
    "has_more": true
}
```

---

### Analytics Data

Get comprehensive analytics about content processing and system performance.

```http
GET /analytics/
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `period` | string | No | Time period (`24h`, `7d`, `30d`, `all`) |
| `breakdown` | string | No | Data breakdown (`type`, `source`, `date`) |

**Example Requests**

```bash
# Get all analytics
GET /analytics/

# Get weekly breakdown
GET /analytics/?period=7d&breakdown=type
```

**Response**
```json
{
    "summary": {
        "total_content": 5432,
        "total_searches": 890,
        "processing_success_rate": 0.85,
        "average_processing_time_ms": 1250,
        "disk_usage_mb": 2048,
        "last_updated": "2024-03-15T14:30:00Z"
    },
    "content_by_type": {
        "article": 3200,
        "document": 1500,
        "podcast": 580,
        "youtube": 152
    },
    "processing_stats": {
        "successful": 4621,
        "failed": 811,
        "pending": 45,
        "retry_queue": 12
    },
    "search_analytics": {
        "total_queries": 890,
        "unique_queries": 654,
        "average_results": 12.5,
        "popular_terms": ["AI", "python", "technology", "data"]
    },
    "performance_metrics": {
        "api_response_time_ms": 45.2,
        "search_response_time_ms": 23.8,
        "database_query_time_ms": 12.1,
        "uptime_hours": 168.5
    }
}
```

---

### Dashboard Interface

Get the HTML dashboard interface for web browser access.

```http
GET /dashboard/
```

**Response**
- Returns HTML content for the dashboard interface
- Includes embedded CSS and JavaScript
- Fully responsive design for mobile and desktop

**Status Codes**
- `200` - Dashboard loaded successfully
- `500` - Internal server error

---

### Content Details

Get detailed information about a specific content item.

```http
GET /content/{content_id}
```

**Path Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `content_id` | string | Yes | Unique identifier for content item |

**Response**
```json
{
    "id": "12345",
    "title": "Complete Article Title",
    "content_type": "article",
    "url": "https://example.com/full-article",
    "content": "Full article content...",
    "summary": "Generated summary...",
    "created_at": "2024-03-15T10:30:00Z",
    "updated_at": "2024-03-15T10:30:00Z",
    "word_count": 2500,
    "read_time_minutes": 10,
    "tags": ["AI", "technology", "future"],
    "metadata": {
        "author": "Jane Smith",
        "published_date": "2024-03-14",
        "source": "example.com",
        "language": "en",
        "quality_score": 0.92
    },
    "processing_info": {
        "processed_at": "2024-03-15T10:30:00Z",
        "processing_time_ms": 1250,
        "strategy_used": "direct_fetch",
        "success": true
    }
}
```

**Status Codes**
- `200` - Content found
- `404` - Content not found
- `500` - Server error

---

### Content Upload

Upload documents or content for processing.

```http
POST /content/upload
```

**Request Body**
- `multipart/form-data` with file upload
- Supported formats: PDF, TXT, MD, DOCX, HTML

**Example**
```bash
curl -X POST \
  http://localhost:8000/api/v1/content/upload \
  -F "file=@document.pdf" \
  -F "title=Optional Custom Title" \
  -F "tags=tag1,tag2,tag3"
```

**Response**
```json
{
    "success": true,
    "content_id": "67890",
    "message": "File uploaded and queued for processing",
    "filename": "document.pdf",
    "size_bytes": 524288,
    "estimated_processing_time_seconds": 30
}
```

---

### Processing Status

Check the status of content processing operations.

```http
GET /processing/status
```

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `content_id` | string | No | Check status of specific content |
| `type` | string | No | Filter by content type |

**Response**
```json
{
    "overall_status": "active",
    "queue_size": 23,
    "processing": 3,
    "completed_today": 156,
    "failed_today": 12,
    "services": {
        "article_processor": {
            "status": "running",
            "last_run": "2024-03-15T14:25:00Z",
            "success_rate": 0.87
        },
        "document_processor": {
            "status": "running", 
            "last_run": "2024-03-15T14:20:00Z",
            "success_rate": 0.94
        },
        "search_indexer": {
            "status": "running",
            "last_run": "2024-03-15T14:15:00Z",
            "items_indexed": 1250
        }
    }
}
```

---

### System Configuration

Get and update system configuration (admin only).

```http
GET /config/
POST /config/
```

**GET Response**
```json
{
    "processing": {
        "max_concurrent_downloads": 5,
        "retry_attempts": 3,
        "article_timeout_seconds": 30
    },
    "search": {
        "results_limit": 100,
        "enable_fuzzy_search": true,
        "cache_size": 1000
    },
    "system": {
        "api_host": "0.0.0.0",
        "api_port": 8000,
        "debug_mode": false
    }
}
```

**POST Request** (Update configuration)
```json
{
    "processing.max_concurrent_downloads": 3,
    "search.results_limit": 200
}
```

---

## Error Responses

All endpoints return consistent error responses:

```json
{
    "error": {
        "code": "INVALID_QUERY", 
        "message": "Search query cannot be empty",
        "details": {
            "parameter": "q",
            "provided_value": "",
            "expected": "non-empty string"
        }
    },
    "request_id": "req_abc123",
    "timestamp": "2024-03-15T14:30:00Z"
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|------------|-------------|
| `INVALID_QUERY` | 400 | Malformed or invalid query parameters |
| `CONTENT_NOT_FOUND` | 404 | Requested content item not found |
| `RATE_LIMIT_EXCEEDED` | 429 | API rate limit exceeded |
| `INTERNAL_ERROR` | 500 | Unexpected server error |
| `SERVICE_UNAVAILABLE` | 503 | Service temporarily unavailable |

## SDK Examples

### Python

```python
import requests

# Initialize client
base_url = "http://localhost:8000/api/v1"

# Search content
def search_content(query, content_type=None, limit=10):
    params = {"q": query, "limit": limit}
    if content_type:
        params["type"] = content_type
    
    response = requests.get(f"{base_url}/search/", params=params)
    return response.json()

# Get analytics
def get_analytics(period="7d"):
    params = {"period": period}
    response = requests.get(f"{base_url}/analytics/", params=params)
    return response.json()

# Example usage
results = search_content("machine learning", content_type="article")
print(f"Found {results['total']} articles")

analytics = get_analytics("30d")
print(f"Total content: {analytics['summary']['total_content']}")
```

### JavaScript

```javascript
// Atlas API client
class AtlasAPI {
    constructor(baseUrl = 'http://localhost:8000/api/v1') {
        this.baseUrl = baseUrl;
    }
    
    async search(query, options = {}) {
        const params = new URLSearchParams({
            q: query,
            ...options
        });
        
        const response = await fetch(`${this.baseUrl}/search/?${params}`);
        return response.json();
    }
    
    async getAnalytics(period = '7d') {
        const response = await fetch(`${this.baseUrl}/analytics/?period=${period}`);
        return response.json();
    }
    
    async getContent(options = {}) {
        const params = new URLSearchParams(options);
        const response = await fetch(`${this.baseUrl}/content/?${params}`);
        return response.json();
    }
}

// Example usage
const atlas = new AtlasAPI();

atlas.search('artificial intelligence', { type: 'article', limit: 20 })
    .then(results => console.log(`Found ${results.total} articles`));

atlas.getAnalytics('30d')
    .then(analytics => console.log(`Total: ${analytics.summary.total_content}`));
```

### cURL Examples

```bash
# Health check
curl -X GET http://localhost:8000/api/v1/health

# Search with filters
curl -G http://localhost:8000/api/v1/search/ \
    -d q="machine learning" \
    -d type="article" \
    -d limit=20 \
    -d sort="relevance"

# Get analytics
curl -X GET "http://localhost:8000/api/v1/analytics/?period=30d"

# Upload content
curl -X POST http://localhost:8000/api/v1/content/upload \
    -F "file=@document.pdf" \
    -F "title=Research Paper" \
    -F "tags=AI,research,paper"

# Get content details
curl -X GET http://localhost:8000/api/v1/content/12345
```

## Rate Limiting

Atlas implements rate limiting to ensure stable performance:

- **Per-IP limits**: 100 requests/minute, 1000 requests/hour
- **Global limits**: 10,000 requests/hour across all IPs
- **Burst allowance**: Short bursts up to 150 requests/minute

### Rate Limit Headers

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1647345600
X-RateLimit-Retry-After: 60
```

## Pagination

For endpoints returning lists, use `limit` and `offset`:

```bash
# First page (0-19)
GET /content/?limit=20&offset=0

# Second page (20-39)  
GET /content/?limit=20&offset=20

# Third page (40-59)
GET /content/?limit=20&offset=40
```

## Webhook Support

Atlas supports webhooks for real-time notifications:

```http
POST /webhooks/
```

**Webhook Events**
- `content.processed` - New content processed
- `search.query` - Search query performed
- `system.error` - System error occurred

For webhook configuration, see the main Atlas documentation.