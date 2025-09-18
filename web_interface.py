#!/usr/bin/env python3
"""
Simplified Web Interface for Atlas

Provides a clean, user-friendly web interface for the Atlas content management system.
Built with FastAPI and static HTML/CSS/JS for simplicity and reliability.
"""

import sys
import os
import logging
from pathlib import Path
from typing import Optional
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

from core.database import get_database, Content
from core.processor import get_processor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Atlas Web Interface")

# Set up static files and templates
static_dir = project_root / "web" / "static"
templates_dir = project_root / "web" / "templates"

# Create directories if they don't exist
static_dir.mkdir(parents=True, exist_ok=True)
templates_dir.mkdir(parents=True, exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Set up templates
templates = Jinja2Templates(directory=str(templates_dir))


# Pydantic models
class ContentForm(BaseModel):
    content: str
    title: Optional[str] = None
    source: Optional[str] = None


class SearchForm(BaseModel):
    query: str
    limit: int = 50


# Create static files
def create_static_files():
    """Create necessary static files for the web interface"""

    # Create CSS
    css_content = """
/* Atlas Web Interface - Simple, Clean Design */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: #f5f5f5;
    color: #333;
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.header h1 {
    font-size: 2rem;
    font-weight: 600;
}

.header p {
    opacity: 0.9;
    margin-top: 0.5rem;
}

.nav {
    background: white;
    border-bottom: 1px solid #e0e0e0;
    padding: 1rem 0;
    margin-bottom: 2rem;
}

.nav-links {
    display: flex;
    gap: 2rem;
    list-style: none;
}

.nav-links a {
    text-decoration: none;
    color: #666;
    font-weight: 500;
    transition: color 0.3s;
}

.nav-links a:hover, .nav-links a.active {
    color: #667eea;
}

.card {
    background: white;
    border-radius: 8px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.card h2 {
    color: #333;
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #555;
}

.form-control {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    font-size: 1rem;
    transition: border-color 0.3s;
}

.form-control:focus {
    outline: none;
    border-color: #667eea;
}

textarea.form-control {
    resize: vertical;
    min-height: 120px;
}

.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    font-weight: 500;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-primary {
    background: #667eea;
    color: white;
}

.btn-primary:hover {
    background: #5a6fd8;
}

.btn-secondary {
    background: #6c757d;
    color: white;
}

.btn-secondary:hover {
    background: #5a6268;
}

.btn-success {
    background: #28a745;
    color: white;
}

.btn-success:hover {
    background: #218838;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.stat-card {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.stat-number {
    font-size: 2rem;
    font-weight: 700;
    color: #667eea;
}

.stat-label {
    color: #666;
    margin-top: 0.5rem;
}

.content-list {
    list-style: none;
}

.content-item {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: box-shadow 0.3s;
}

.content-item:hover {
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.content-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #333;
    margin-bottom: 0.5rem;
}

.content-meta {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: #666;
}

.content-type {
    background: #667eea;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
}

.content-stage {
    background: #28a745;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
}

.content-summary {
    color: #555;
    line-height: 1.6;
}

.alert {
    padding: 1rem;
    border-radius: 6px;
    margin-bottom: 1rem;
}

.alert-success {
    background: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.alert-error {
    background: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.loading {
    text-align: center;
    padding: 2rem;
    color: #666;
}

.footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 4rem;
}

@media (max-width: 768px) {
    .container {
        padding: 0 15px;
    }

    .nav-links {
        flex-direction: column;
        gap: 1rem;
    }

    .stats-grid {
        grid-template-columns: 1fr;
    }

    .content-meta {
        flex-direction: column;
        gap: 0.5rem;
    }
}
"""

    # Create JavaScript
    js_content = """
// Atlas Web Interface - Interactive Functions
class AtlasWeb {
    constructor() {
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupFormHandlers();
    }

    setupEventListeners() {
        // Form submissions
        document.querySelectorAll('form').forEach(form => {
            form.addEventListener('submit', this.handleFormSubmit.bind(this));
        });

        // Search input
        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            searchInput.addEventListener('input', this.debounce(this.handleSearch.bind(this), 300));
        }

        // Content type filter
        const typeFilter = document.getElementById('type-filter');
        if (typeFilter) {
            typeFilter.addEventListener('change', this.handleTypeFilter.bind(this));
        }
    }

    setupFormHandlers() {
        // Content form
        const contentForm = document.getElementById('content-form');
        if (contentForm) {
            contentForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.addContent();
            });
        }

        // Search form
        const searchForm = document.getElementById('search-form');
        if (searchForm) {
            searchForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.performSearch();
            });
        }
    }

    async addContent() {
        const form = document.getElementById('content-form');
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;

        try {
            // Show loading state
            submitBtn.textContent = 'Adding...';
            submitBtn.disabled = true;

            const formData = new FormData(form);
            const data = {
                content: formData.get('content'),
                title: formData.get('title'),
                source: formData.get('source')
            };

            const response = await fetch('/api/content', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                this.showAlert('Content added successfully!', 'success');
                form.reset();

                // Refresh content list if on dashboard
                if (window.location.pathname === '/') {
                    await this.refreshContentList();
                }
            } else {
                this.showAlert(`Error: ${result.detail}`, 'error');
            }
        } catch (error) {
            this.showAlert('Network error: ' + error.message, 'error');
        } finally {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    }

    async performSearch() {
        const query = document.getElementById('search-query').value;
        if (!query.trim()) return;

        try {
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: query,
                    limit: 50
                })
            });

            const result = await response.json();

            if (response.ok) {
                this.displaySearchResults(result.results, query);
            } else {
                this.showAlert(`Search error: ${result.detail}`, 'error');
            }
        } catch (error) {
            this.showAlert('Search error: ' + error.message, 'error');
        }
    }

    displaySearchResults(results, query) {
        const resultsContainer = document.getElementById('search-results');
        if (!resultsContainer) return;

        if (results.length === 0) {
            resultsContainer.innerHTML = `
                <div class="alert alert-info">
                    No results found for "${query}"
                </div>
            `;
            return;
        }

        const resultsHtml = results.map(item => `
            <div class="content-item">
                <div class="content-title">${this.escapeHtml(item.title)}</div>
                <div class="content-meta">
                    <span class="content-type">${item.content_type || 'Unknown'}</span>
                    <span class="content-stage">Stage ${item.stage}</span>
                    <span>${new Date(item.created_at).toLocaleDateString()}</span>
                </div>
                ${item.ai_summary ? `<div class="content-summary">${this.escapeHtml(item.ai_summary)}</div>` : ''}
            </div>
        `).join('');

        resultsContainer.innerHTML = resultsHtml;
    }

    async refreshContentList() {
        try {
            const response = await fetch('/api/content?limit=10');
            const result = await response.json();

            if (response.ok) {
                this.updateContentList(result.results);
            }
        } catch (error) {
            console.error('Error refreshing content list:', error);
        }
    }

    updateContentList(contents) {
        const container = document.getElementById('recent-content');
        if (!container) return;

        const html = contents.map(item => `
            <div class="content-item">
                <div class="content-title">${this.escapeHtml(item.title)}</div>
                <div class="content-meta">
                    <span class="content-type">${item.content_type || 'Unknown'}</span>
                    <span class="content-stage">Stage ${item.stage}</span>
                    <span>${new Date(item.created_at).toLocaleDateString()}</span>
                </div>
                ${item.ai_summary ? `<div class="content-summary">${this.escapeHtml(item.ai_summary)}</div>` : ''}
            </div>
        `).join('');

        container.innerHTML = html || '<p>No content yet.</p>';
    }

    handleSearch(event) {
        const query = event.target.value;
        if (query.length > 2) {
            this.performSearch();
        }
    }

    handleTypeFilter(event) {
        const type = event.target.value;
        // Implement type filtering
        console.log('Filter by type:', type);
    }

    showAlert(message, type = 'info') {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type}`;
        alertDiv.textContent = message;

        const container = document.querySelector('.container');
        container.insertBefore(alertDiv, container.firstChild);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new AtlasWeb();
});
"""

    # Create HTML template for base layout
    base_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Atlas - Digital Filing Cabinet{% endblock %}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>🗂️ Atlas</h1>
            <p>Your Simple Digital Filing Cabinet</p>
        </div>
    </header>

    <nav class="nav">
        <div class="container">
            <ul class="nav-links">
                <li><a href="/" {% if request.path == '/' %}class="active"{% endif %}>Dashboard</a></li>
                <li><a href="/add" {% if request.path == '/add' %}class="active"{% endif %}>Add Content</a></li>
                <li><a href="/search" {% if request.path == '/search' %}class="active"{% endif %}>Search</a></li>
                <li><a href="/stats" {% if request.path == '/stats' %}class="active"{% endif %}>Statistics</a></li>
            </ul>
        </div>
    </nav>

    <main class="container">
        {% block content %}{% endblock %}
    </main>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 Atlas - Simple Content Management</p>
        </div>
    </footer>

    <script src="/static/script.js"></script>
</body>
</html>
"""

    # Write files
    (static_dir / "style.css").write_text(css_content)
    (static_dir / "script.js").write_text(js_content)
    (templates_dir / "base.html").write_text(base_template)

    # Create page templates
    dashboard_template = """{% extends "base.html" %}

{% block title %}Atlas - Dashboard{% endblock %}

{% block content %}
    <div class="card">
        <h2>Welcome to Atlas</h2>
        <p>Your simple digital filing cabinet for organizing and processing content from various sources.</p>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">{{ total_content }}</div>
            <div class="stat-label">Total Items</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{{ content_types }}</div>
            <div class="stat-label">Content Types</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{{ recent_items }}</div>
            <div class="stat-label">Recent Items</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{{ processed_items }}</div>
            <div class="stat-label">Processed</div>
        </div>
    </div>

    <div class="card">
        <h2>Quick Actions</h2>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <a href="/add" class="btn btn-primary">Add Content</a>
            <a href="/search" class="btn btn-secondary">Search Content</a>
            <a href="/stats" class="btn btn-secondary">View Statistics</a>
        </div>
    </div>

    <div class="card">
        <h2>Recent Content</h2>
        <div id="recent-content">
            {% for item in recent_content %}
            <div class="content-item">
                <div class="content-title">{{ item.title }}</div>
                <div class="content-meta">
                    <span class="content-type">{{ item.content_type or 'Unknown' }}</span>
                    <span class="content-stage">Stage {{ item.stage }}</span>
                    <span>{{ item.created_at }}</span>
                </div>
                {% if item.ai_summary %}
                <div class="content-summary">{{ item.ai_summary[:200] }}...</div>
                {% endif %}
            </div>
            {% endfor %}
            {% if not recent_content %}
            <p>No content yet. <a href="/add">Add some content</a> to get started.</p>
            {% endif %}
        </div>
    </div>
{% endblock %}"""

    add_content_template = """{% extends "base.html" %}

{% block title %}Atlas - Add Content{% endblock %}

{% block content %}
    <div class="card">
        <h2>Add New Content</h2>
        <p>Add content to your Atlas filing cabinet. You can add URLs, text, or RSS feeds.</p>

        <form id="content-form">
            <div class="form-group">
                <label for="content">Content *</label>
                <textarea id="content" name="content" class="form-control" placeholder="Enter URL, text content, or RSS feed URL..." required></textarea>
            </div>

            <div class="form-group">
                <label for="title">Title (Optional)</label>
                <input type="text" id="title" name="title" class="form-control" placeholder="Enter title or leave blank for auto-generation">
            </div>

            <div class="form-group">
                <label for="source">Source (Optional)</label>
                <input type="text" id="source" name="source" class="form-control" placeholder="e.g., Web, RSS, Manual">
            </div>

            <button type="submit" class="btn btn-primary">Add Content</button>
        </form>
    </div>

    <div class="card">
        <h2>Tips</h2>
        <ul style="margin-left: 1.5rem;">
            <li><strong>URLs:</strong> Enter web page URLs to extract and store content</li>
            <li><strong>Text:</strong> Paste text content directly for storage and analysis</li>
            <li><strong>RSS:</strong> Add RSS feed URLs to automatically fetch new articles</li>
            <li><strong>Batch:</strong> Add multiple items by separating them with newlines</li>
        </ul>
    </div>
{% endblock %}"""

    search_template = """{% extends "base.html" %}

{% block title %}Atlas - Search{% endblock %}

{% block content %}
    <div class="card">
        <h2>Search Content</h2>
        <p>Search through all your stored content using keywords and phrases.</p>

        <form id="search-form">
            <div class="form-group">
                <label for="search-query">Search Query</label>
                <input type="text" id="search-query" name="query" class="form-control" placeholder="Enter search terms..." required>
            </div>

            <button type="submit" class="btn btn-primary">Search</button>
        </form>
    </div>

    <div id="search-results">
        <!-- Search results will appear here -->
    </div>
{% endblock %}"""

    stats_template = """{% extends "base.html" %}

{% block title %}Atlas - Statistics{% endblock %}

{% block content %}
    <div class="card">
        <h2>System Statistics</h2>
        <p>Overview of your Atlas content management system.</p>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">{{ stats.total_content }}</div>
            <div class="stat-label">Total Items</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{{ stats.with_ai_summaries }}</div>
            <div class="stat-label">With AI Summaries</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{{ content_types|length }}</div>
            <div class="stat-label">Content Types</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{{ recent_activity }}</div>
            <div class="stat-label">Recent Activity</div>
        </div>
    </div>

    {% if stats.by_type %}
    <div class="card">
        <h2>Content by Type</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            {% for type_info in stats.by_type %}
            <div class="stat-card">
                <div class="stat-number">{{ type_info.count }}</div>
                <div class="stat-label">{{ type_info.type }}</div>
            </div>
            {% endfor %}
        </div>
    </div>
    {% endif %}

    {% if stats.by_stage %}
    <div class="card">
        <h2>Content by Processing Stage</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            {% for stage_info in stats.by_stage %}
            <div class="stat-card">
                <div class="stat-number">{{ stage_info.count }}</div>
                <div class="stat-label">Stage {{ stage_info.stage }}</div>
            </div>
            {% endfor %}
        </div>
    </div>
    {% endif %}
{% endblock %}"""

    # Write templates
    (templates_dir / "dashboard.html").write_text(dashboard_template)
    (templates_dir / "add.html").write_text(add_content_template)
    (templates_dir / "search.html").write_text(search_template)
    (templates_dir / "stats.html").write_text(stats_template)

    logger.info("Static files created successfully")


# FastAPI endpoints
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Dashboard page"""
    try:
        db = get_database()
        stats = db.get_statistics()

        # Get recent content
        recent_content = []
        try:
            with db.pool.get_connection() as conn:
                cursor = conn.execute("""
                    SELECT id, title, content_type, created_at, stage, ai_summary
                    FROM content
                    ORDER BY created_at DESC
                    LIMIT 5
                """)
                rows = cursor.fetchall()
                recent_content = [
                    {
                        "id": row[0],
                        "title": row[1],
                        "content_type": row[2],
                        "created_at": row[3],
                        "stage": row[4],
                        "ai_summary": row[5]
                    }
                    for row in rows
                ]
        except Exception as e:
            logger.error(f"Error getting recent content: {e}")

        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "total_content": stats.get('total_content', 0),
            "content_types": len(stats.get('by_type', {})),
            "recent_items": len(recent_content),
            "processed_items": stats.get('with_ai_summaries', 0),
            "recent_content": recent_content
        })
    except Exception as e:
        logger.error(f"Dashboard error: {e}")
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "total_content": 0,
            "content_types": 0,
            "recent_items": 0,
            "processed_items": 0,
            "recent_content": []
        })


@app.get("/add", response_class=HTMLResponse)
async def add_content_page(request: Request):
    """Add content page"""
    return templates.TemplateResponse("add.html", {"request": request})


@app.get("/search", response_class=HTMLResponse)
async def search_page(request: Request):
    """Search page"""
    return templates.TemplateResponse("search.html", {"request": request})


@app.get("/stats", response_class=HTMLResponse)
async def stats_page(request: Request):
    """Statistics page"""
    try:
        db = get_database()
        stats = db.get_statistics()

        # Calculate recent activity (last 7 days)
        recent_activity = 0
        try:
            with db.pool.get_connection() as conn:
                cursor = conn.execute("""
                    SELECT COUNT(*) FROM content
                    WHERE created_at >= datetime('now', '-7 days')
                """)
                recent_activity = cursor.fetchone()[0]
        except Exception as e:
            logger.error(f"Error calculating recent activity: {e}")

        return templates.TemplateResponse("stats.html", {
            "request": request,
            "stats": stats,
            "content_types": stats.get('by_type', []),
            "recent_activity": recent_activity
        })
    except Exception as e:
        logger.error(f"Stats page error: {e}")
        return templates.TemplateResponse("stats.html", {
            "request": request,
            "stats": {"total_content": 0, "with_ai_summaries": 0},
            "content_types": [],
            "recent_activity": 0
        })


@app.get("/api/health")
async def api_health():
    """Health check for web interface"""
    try:
        db = get_database()
        stats = db.get_statistics()
        return {
            "status": "healthy",
            "total_content": stats.get('total_content', 0),
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {"status": "unhealthy", "error": str(e)}


class ContentRequest(BaseModel):
    """Model for content creation requests"""
    title: str
    content: str = ""
    url: str = ""
    content_type: str = "article"


@app.post("/api/content")
async def api_create_content(request: Request):
    """Legacy content creation for form data"""
    try:
        data = await request.json()
        db = get_database()

        content = Content(
            title=data.get("title", "Untitled"),
            content=data.get("content", ""),
            url=data.get("url", ""),
            content_type=data.get("content_type", "article")
        )

        content_id = db.store_content(content)

        return {
            "success": True,
            "content_id": content_id,
            "message": "Content created successfully"
        }
    except Exception as e:
        logger.error(f"Content creation failed: {e}")
        return {"success": False, "error": str(e)}


@app.get("/api/content")
async def api_list_content(limit: int = 20):
    """List content via API"""
    try:
        db = get_database()
        content_list = db.get_recent_content(limit)

        return {
            "success": True,
            "content": [
                {
                    "id": c.id,
                    "title": c.title,
                    "url": c.url,
                    "content_type": c.content_type,
                    "created_at": c.created_at
                }
                for c in content_list
            ]
        }
    except Exception as e:
        logger.error(f"Content listing failed: {e}")
        return {"success": False, "error": str(e)}


@app.get("/api/search")
async def api_search(q: str = "", limit: int = 20):
    """Search content via API"""
    try:
        db = get_database()
        results = db.search_content(q, limit)

        return {
            "success": True,
            "results": [
                {
                    "id": c.id,
                    "title": c.title,
                    "url": c.url,
                    "content_type": c.content_type,
                    "created_at": c.created_at
                }
                for c in results
            ]
        }
    except Exception as e:
        logger.error(f"Search failed: {e}")
        return {"success": False, "error": str(e)}


def main():
    """Create static files and start the web interface"""
    create_static_files()

    print("🌐 Starting Atlas Web Interface...")
    print("📊 Web interface available at: http://localhost:8000")
    print("📱 Features:")
    print("   • Clean, responsive design")
    print("   • Content addition and management")
    print("   • Search functionality")
    print("   • Statistics dashboard")
    print("   • Mobile-friendly interface")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )


if __name__ == "__main__":
    main()