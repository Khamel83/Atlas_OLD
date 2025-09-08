from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import sys

# Add parent directory to Python path for module imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.routers import content, search, cognitive, auth, dashboard, transcription, worker, shortcuts, transcript_search
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Atlas API",
    description="API for the Atlas cognitive amplification platform",
    version="1.0.0"
)

# Add CORS middleware with security restrictions
allowed_origins = ["*"]  # Allow all origins for bookmarklet functionality

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(content.router, prefix="/api/v1/content", tags=["content"])
app.include_router(search.router, prefix="/api/v1/search", tags=["search"])
app.include_router(cognitive.router, prefix="/api/v1/cognitive", tags=["cognitive"])
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["dashboard"])
app.include_router(transcription.router, prefix="/api/v1/transcriptions", tags=["transcription"])
app.include_router(worker.router, prefix="/api/v1/worker", tags=["worker"])
app.include_router(shortcuts.router, prefix="/api/v1/shortcuts", tags=["shortcuts"])
app.include_router(transcript_search.router, prefix="/api/v1/transcripts", tags=["transcript_search"])

@app.get("/api/v1/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def root():
    """Redirect root to mobile dashboard"""
    return RedirectResponse(url="/mobile")

@app.get("/mobile", response_class=HTMLResponse)
async def mobile_dashboard():
    """Mobile dashboard for Atlas status and quick actions"""
    return await get_mobile_dashboard_html()

@app.get("/shortcuts")
async def shortcuts_redirect():
    """Redirect to shortcuts install page"""
    return RedirectResponse(url="/api/v1/shortcuts/install")

@app.get("/bookmarklet")
async def bookmarklet_page():
    """Serve the bookmarklet installation page"""
    from pathlib import Path
    from fastapi import HTTPException
    bookmarklet_path = Path(__file__).parent.parent / "browser_bookmarklet" / "install_bookmarklet.html"
    if bookmarklet_path.exists():
        with open(bookmarklet_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    else:
        raise HTTPException(status_code=404, detail="Bookmarklet page not found")

async def get_mobile_dashboard_html():
    """Generate mobile dashboard HTML with real-time Atlas data"""
    try:
        # Get system status
        sys.path.append('.')
        from helpers.simple_database import SimpleDatabase
        import subprocess
        import psutil
        
        db = SimpleDatabase()
        
        # Get processing stats
        with db.get_connection() as conn:
            total_items = conn.execute('SELECT COUNT(*) FROM content WHERE content IS NOT NULL AND length(content) > 100').fetchone()[0]
            processed_items = conn.execute('SELECT COUNT(*) FROM content WHERE ai_summary IS NOT NULL AND ai_summary != ""').fetchone()[0]
            articles_count = conn.execute('SELECT COUNT(*) FROM content WHERE content_type = "article"').fetchone()[0]
            podcasts_count = conn.execute('SELECT COUNT(*) FROM content WHERE content_type = "podcast"').fetchone()[0]
            
            # Get recently processed items (by updated_at when AI processing completed)
            recent = conn.execute('''
                SELECT id, title, updated_at 
                FROM content 
                WHERE ai_summary IS NOT NULL 
                AND updated_at > datetime('now', '-24 hours')
                ORDER BY updated_at DESC LIMIT 5
            ''').fetchall()
        
        # System info
        disk_usage = psutil.disk_usage('/')
        free_gb = disk_usage.free / (1024**3)
        
        # Processing progress
        progress_pct = (processed_items / total_items * 100) if total_items > 0 else 0
        remaining_items = total_items - processed_items
        
        # Check if mass processing is running
        mass_processing_running = False
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            mass_processing_running = 'mass_ai_reprocessing.py' in result.stdout
        except:
            pass
            
        # Cost calculations for normal operation (not mass processing)
        import datetime
        now = datetime.datetime.now()
        
        if mass_processing_running:
            # Show mass processing costs
            estimated_cost = processed_items * 0.000048
            remaining_cost = remaining_items * 0.000048
            cost_display = f"Spent: ${estimated_cost:.4f} | Remaining: ${remaining_cost:.4f}"
        else:
            # Show normal operation costs (day/week/month)
            with db.get_connection() as conn:
                # Get items processed in last day/week/month
                day_ago = (now - datetime.timedelta(days=1)).isoformat()
                week_ago = (now - datetime.timedelta(days=7)).isoformat()
                month_ago = (now - datetime.timedelta(days=30)).isoformat()
                
                # Count items that were actually processed (updated) in these time periods
                day_items = conn.execute('SELECT COUNT(*) FROM content WHERE ai_summary IS NOT NULL AND updated_at > ? AND updated_at > created_at', (day_ago,)).fetchone()[0]
                week_items = conn.execute('SELECT COUNT(*) FROM content WHERE ai_summary IS NOT NULL AND updated_at > ? AND updated_at > created_at', (week_ago,)).fetchone()[0]
                month_items = conn.execute('SELECT COUNT(*) FROM content WHERE ai_summary IS NOT NULL AND updated_at > ? AND updated_at > created_at', (month_ago,)).fetchone()[0]
                
                day_cost = day_items * 0.000048
                week_cost = week_items * 0.000048
                month_cost = month_items * 0.000048
                
                cost_display = f"Day: ${day_cost:.4f} | Week: ${week_cost:.4f} | Month: ${month_cost:.4f}"
        
        html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atlas Dashboard</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
            font-size: 16px;
            line-height: 1.4;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
        }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 24px;
        }}
        .status-good {{ color: #22c55e; }}
        .status-processing {{ color: #f59e0b; }}
        .status-bad {{ color: #ef4444; }}
        .progress-bar {{
            width: 100%;
            height: 8px;
            background: #e5e7eb;
            border-radius: 4px;
            overflow: hidden;
            margin: 8px 0;
        }}
        .progress-fill {{
            height: 100%;
            background: #22c55e;
            width: {progress_pct:.1f}%;
            transition: width 0.3s ease;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 16px 0;
        }}
        .stat {{
            text-align: center;
        }}
        .stat-value {{
            font-size: 24px;
            font-weight: bold;
            color: #1f2937;
        }}
        .stat-label {{
            color: #6b7280;
            font-size: 14px;
        }}
        .url-input {{
            width: 100%;
            padding: 12px;
            border: 2px solid #e5e7eb;
            border-radius: 8px;
            font-size: 16px;
            margin-bottom: 12px;
        }}
        .btn {{
            background: #2563eb;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
        }}
        .btn:hover {{
            background: #1d4ed8;
        }}
        .recent-item {{
            padding: 8px 0;
            border-bottom: 1px solid #e5e7eb;
            font-size: 14px;
        }}
        .recent-item:last-child {{
            border-bottom: none;
        }}
        .monospace {{
            font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
            font-size: 14px;
        }}
        .refresh-indicator {{
            text-align: center;
            color: #6b7280;
            font-size: 12px;
            margin-top: 16px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧠 Atlas Dashboard</h1>
            <p class="status-good">✅ System Running</p>
        </div>
        
        <div class="card">
            <h2>⚡ Processing Status</h2>
            <div class="{"status-processing" if mass_processing_running or remaining_items > 0 else "status-good"}">
                {"🔄 Mass AI Processing Running" if mass_processing_running else ("🔄 Continuous Processing" if remaining_items > 0 else "✅ Processing Complete")}
            </div>
            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
            <div class="monospace">
                {processed_items:,} / {total_items:,} items processed ({progress_pct:.1f}%)
            </div>
            {f'<div class="monospace">⏱️  ~{remaining_items//500:.0f} hours remaining</div>' if mass_processing_running else ''}
        </div>
        
        <div class="card">
            <h2>📊 Content Library</h2>
            <div class="stats-grid">
                <div class="stat">
                    <div class="stat-value">{articles_count:,}</div>
                    <div class="stat-label">Articles</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{podcasts_count:,}</div>
                    <div class="stat-label">Podcasts</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{processed_items:,}</div>
                    <div class="stat-label">AI Analyzed</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{free_gb:.1f}GB</div>
                    <div class="stat-label">Free Space</div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>💰 Processing Costs</h2>
            <div class="monospace">
                {cost_display}
            </div>
        </div>
        
        <div class="card">
            <h2>🚀 Quick Actions</h2>
            <form id="urlForm">
                <input type="url" class="url-input" id="urlInput" placeholder="Paste URL here (article, YouTube, etc.)" required>
                <button type="submit" class="btn">Save to Atlas</button>
            </form>
        </div>
        
        <div class="card">
            <h2>📝 Recently Processed</h2>
            {''.join([f'<div class="recent-item">#{item[0]}: {item[1][:60]}{"..." if len(item[1]) > 60 else ""}</div>' for item in recent])}
        </div>
    </div>
    
    <div class="refresh-indicator">
        Auto-refresh every 30 seconds
    </div>
    
    <!-- Atlas Dashboards -->
    <div class="card">
        <h2>🧭 Atlas Dashboards</h2>
        <div style="display: grid; gap: 12px; margin-top: 16px;">
            <a href="/api/v1/dashboard/" style="display: block; padding: 12px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-decoration: none; border-radius: 8px; text-align: center; font-weight: 500;">
                📊 Analytics Dashboard
            </a>
            <a href="/api/v1/content/" style="display: block; padding: 12px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; text-decoration: none; border-radius: 8px; text-align: center; font-weight: 500;">
                📚 Content Browser (5,494+ items)
            </a>
        </div>
    </div>
    
    <!-- Quick Tools -->
    <div class="card">
        <h2>🛠️ Atlas Tools</h2>
        <div style="display: grid; gap: 12px; margin-top: 16px;">
            <a href="/bookmarklet" style="display: block; padding: 12px; background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%); color: white; text-decoration: none; border-radius: 8px; text-align: center; font-weight: 500;">
                🔖 Browser Bookmarklet (Save from any browser)
            </a>
            <a href="https://github.com/Khamel83/Atlas/blob/main/quick_start_package/shortcuts/" target="_blank" style="display: block; padding: 12px; background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); color: #333; text-decoration: none; border-radius: 8px; text-align: center; font-weight: 500;">
                📱 iOS Shortcuts (Download links)
            </a>
        </div>
        <div style="margin-top: 16px; padding: 12px; background: #f8f9fa; border-radius: 8px; font-size: 14px; color: #666;">
            💡 <strong>Tip:</strong> Use the bookmarklet on any website to save articles to Atlas instantly
        </div>
    </div>
    
    <div style="text-align: center; margin-top: 30px; padding: 20px; border-top: 1px solid #e5e7eb;">
        <a href="https://github.com/Khamel83/atlas" target="_blank" style="color: #6b7280; text-decoration: none; font-size: 14px;">
            📚 Atlas on GitHub
        </a>
    </div>
    
    <script>
        // Auto-refresh every 30 seconds
        setInterval(() => location.reload(), 30000);
        
        // Handle URL form submission
        document.getElementById('urlForm').addEventListener('submit', async (e) => {{
            e.preventDefault();
            const url = document.getElementById('urlInput').value;
            const btn = e.target.querySelector('.btn');
            
            btn.textContent = 'Saving...';
            btn.disabled = true;
            
            try {{
                const response = await fetch('/api/v1/content/submit-url', {{
                    method: 'POST',
                    headers: {{'Content-Type': 'application/json'}},
                    body: JSON.stringify({{url: url}})
                }});
                
                if (response.ok) {{
                    document.getElementById('urlInput').value = '';
                    btn.textContent = '✅ Saved!';
                    setTimeout(() => location.reload(), 1000);
                }} else {{
                    const error = await response.json();
                    if (response.status === 409) {{
                        btn.textContent = '📋 Already Exists';
                    }} else if (response.status === 422) {{
                        btn.textContent = '🚫 Site Blocked Access';
                    }} else {{
                        btn.textContent = '❌ Failed';
                    }}
                    setTimeout(() => {{
                        btn.textContent = 'Save to Atlas';
                        btn.disabled = false;
                    }}, 3000);
                }}
            }} catch (error) {{
                btn.textContent = '❌ Error';
                setTimeout(() => {{
                    btn.textContent = 'Save to Atlas';
                    btn.disabled = false;
                }}, 2000);
            }}
        }});
    </script>
</body>
</html>
        '''
        
        return html
        
    except Exception as e:
        # Fallback error page
        return f'''
<!DOCTYPE html>
<html>
<head>
    <title>Atlas Dashboard - Error</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family: system-ui; padding: 20px; text-align: center;">
    <h1>Atlas Dashboard</h1>
    <p style="color: red;">Error loading dashboard: {str(e)}</p>
    <p><a href="/docs">View API Docs</a></p>
</body>
</html>
        '''

if __name__ == "__main__":
    import uvicorn
    import os
    from dotenv import load_dotenv
    load_dotenv()
    api_port = int(os.getenv('API_PORT', 7444))
    uvicorn.run(app, host="0.0.0.0", port=api_port)