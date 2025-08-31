import datetime
import os
import sys
from urllib.parse import urlencode

# Add parent directory to Python path for module imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# Cognitive Features
try:
    from ask.insights.pattern_detector import PatternDetector
    from ask.proactive.surfacer import ProactiveSurfacer
    from ask.recall.recall_engine import RecallEngine
    from ask.socratic.question_engine import QuestionEngine
    from ask.temporal.temporal_engine import TemporalEngine
    ASK_AVAILABLE = True
except ImportError:
    ASK_AVAILABLE = False

from helpers.metadata_manager import MetadataManager
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# For demo: instantiate with default config (replace with real config/manager in production)
def get_metadata_manager():
    try:
        from helpers.config import load_config

        config = load_config()
    except Exception:
        config = {}
    return MetadataManager(config)


app = FastAPI(title="Atlas Cognitive Platform")

templates = Jinja2Templates(directory="web/templates")

# Path to the scheduler's SQLite job store (should match Atlas scheduler)
JOBSTORE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "scheduler.db"
)  # Unified job store for persistence

# Simple in-memory log for job runs (MVP)
job_logs = {}


def log_job_run(job_id, message):
    """Append a log entry for a job (in-memory, last 50 entries)."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    job_logs.setdefault(job_id, []).append(f"[{now}] {message}")
    job_logs[job_id] = job_logs[job_id][-50:]


# APScheduler instance (paused, for inspection and management only)
scheduler = BackgroundScheduler(
    jobstores={"default": SQLAlchemyJobStore(url=f"sqlite:///{JOBSTORE_PATH}")}
)
scheduler.start(paused=True)


# Dummy function for new jobs (MVP)
def dummy_job():
    """A placeholder job function for demonstration purposes."""
    log_job_run("dummy", "Dummy job executed.")
    print("Dummy job executed.")


# Map job IDs to their log file paths for ingestion jobs
INGESTION_LOG_PATHS = {
    "weekly_article_ingestion": os.path.join(
        os.path.dirname(__file__), "..", "output", "articles", "ingest.log"
    ),
    "weekly_podcast_ingestion": os.path.join(
        os.path.dirname(__file__), "..", "output", "podcasts", "ingest.log"
    ),
    "weekly_youtube_ingestion": os.path.join(
        os.path.dirname(__file__), "..", "output", "youtube", "ingest.log"
    ),
}


def read_log_tail(log_path, n=50):
    """Read the last n lines from a log file."""
    try:
        with open(log_path, "r") as f:
            lines = f.readlines()
        return lines[-n:]
    except Exception:
        return ["No log file found or unable to read log."]


@app.get("/", response_class=HTMLResponse)
def root():
    """Atlas main dashboard with navigation to all features."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Atlas - Personal AI Dashboard</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 2rem;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            h1 {
                font-size: 3rem;
                text-align: center;
                margin-bottom: 1rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            .subtitle {
                text-align: center;
                font-size: 1.2rem;
                margin-bottom: 3rem;
                opacity: 0.9;
            }
            .dashboard-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-bottom: 3rem;
            }
            .dashboard-card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 2rem;
                text-decoration: none;
                color: white;
                transition: all 0.3s ease;
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            .dashboard-card:hover {
                transform: translateY(-5px);
                background: rgba(255, 255, 255, 0.2);
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            .dashboard-icon {
                font-size: 3rem;
                text-align: center;
                margin-bottom: 1rem;
            }
            .dashboard-title {
                font-size: 1.5rem;
                font-weight: 600;
                text-align: center;
                margin-bottom: 1rem;
            }
            .dashboard-description {
                text-align: center;
                opacity: 0.8;
                font-size: 0.9rem;
            }
            .quick-links {
                text-align: center;
                margin-top: 2rem;
            }
            .quick-link {
                display: inline-block;
                margin: 0 1rem;
                padding: 0.5rem 1rem;
                background: rgba(255, 255, 255, 0.2);
                border-radius: 25px;
                text-decoration: none;
                color: white;
                font-size: 0.9rem;
                transition: all 0.3s ease;
            }
            .quick-link:hover {
                background: rgba(255, 255, 255, 0.3);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧠 Atlas</h1>
            <p class="subtitle">Your Personal AI Knowledge System</p>
            
            <div class="dashboard-grid">
                <a href="/mobile" class="dashboard-card">
                    <div class="dashboard-icon">📱</div>
                    <div class="dashboard-title">Mobile Dashboard</div>
                    <div class="dashboard-description">Touch-optimized interface with content management, search filters, and all cognitive features</div>
                </a>
                
                <a href="/ask/html" class="dashboard-card">
                    <div class="dashboard-icon">🧠</div>
                    <div class="dashboard-title">Cognitive AI</div>
                    <div class="dashboard-description">6 AI-powered features: proactive surfacing, temporal analysis, Socratic questions, active recall</div>
                </a>
                
                <a href="/jobs/html" class="dashboard-card">
                    <div class="dashboard-icon">⚙️</div>
                    <div class="dashboard-title">System Management</div>
                    <div class="dashboard-description">Background jobs, scheduling, ingestion pipelines, and system monitoring</div>
                </a>
            </div>
            
            <div class="quick-links">
                <a href="/ask/proactive" class="quick-link">🔄 Proactive API</a>
                <a href="/ask/temporal" class="quick-link">⏰ Temporal API</a>
                <a href="/ask/patterns" class="quick-link">🔍 Patterns API</a>
                <a href="/ask/recall" class="quick-link">🧠 Recall API</a>
                <a href="/jobs" class="quick-link">📊 Jobs API</a>
            </div>
        </div>
    </body>
    </html>
    """


@app.get("/jobs", response_class=JSONResponse)
def list_jobs():
    """Return all jobs as JSON (API endpoint)."""
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append(
            {
                "id": job.id,
                "name": job.name,
                "next_run_time": str(job.next_run_time),
                "trigger": str(job.trigger),
                "func": str(job.func_ref),
                "args": job.args,
                "kwargs": job.kwargs,
                "enabled": not job.paused if hasattr(job, "paused") else True,
            }
        )
    return {"jobs": jobs}


# Enhance jobs_html to show last run status and timestamp for ingestion jobs
@app.get("/jobs/html", response_class=HTMLResponse)
def jobs_html(request: Request, msg: str = "", error: str = ""):
    """Main jobs UI: list jobs, show messages/errors."""
    jobs = []
    for job in scheduler.get_jobs():
        job_info = {
            "id": job.id,
            "name": job.name,
            "next_run_time": str(job.next_run_time),
            "trigger": str(job.trigger),
            "func": str(job.func_ref),
            "args": job.args,
            "kwargs": job.kwargs,
            "enabled": not job.paused if hasattr(job, "paused") else True,
        }
        # For ingestion jobs, try to get last run status and timestamp from log file
        if job.id in INGESTION_LOG_PATHS:
            log_path = INGESTION_LOG_PATHS[job.id]
            try:
                with open(log_path, "r") as f:
                    lines = f.readlines()
                # Look for last status line
                last_status = None
                last_time = None
                for line in reversed(lines):
                    if "ingestion complete" in line.lower() or "error" in line.lower():
                        last_status = (
                            "Success" if "complete" in line.lower() else "Error"
                        )
                        # Try to extract timestamp if present
                        if line.startswith("["):
                            last_time = line.split("]")[0].strip("[]")
                        break
                job_info["last_status"] = last_status or "Unknown"
                job_info["last_time"] = last_time or "-"
            except Exception:
                job_info["last_status"] = "-"
                job_info["last_time"] = "-"
        else:
            job_info["last_status"] = "-"
            job_info["last_time"] = "-"
        jobs.append(job_info)
    return templates.TemplateResponse(
        "jobs.html", {"request": request, "jobs": jobs, "msg": msg, "error": error}
    )


@app.get("/jobs/{job_id}/edit", response_class=HTMLResponse)
def edit_job_form(request: Request, job_id: str, msg: str = "", error: str = ""):
    """Render the edit form for a job (cron string only)."""
    job = scheduler.get_job(job_id)
    if not job:
        return RedirectResponse(url="/jobs/html?error=Job+not+found", status_code=303)
    cron_str = (
        job.trigger.cronspec if hasattr(job.trigger, "cronspec") else str(job.trigger)
    )
    return templates.TemplateResponse(
        "edit_job.html",
        {
            "request": request,
            "job": {"id": job.id, "name": job.name, "cron": cron_str},
            "msg": msg,
            "error": error,
        },
    )


@app.post("/jobs/{job_id}/edit")
def edit_job(job_id: str, cron: str = Form(...)):
    """Update a job's cron schedule."""
    job = scheduler.get_job(job_id)
    if job:
        try:
            trigger = CronTrigger.from_crontab(cron)
            scheduler.reschedule_job(job_id, trigger=trigger)
            log_job_run(job_id, f"Job rescheduled to cron: {cron}")
            params = urlencode({"msg": "Job updated."})
            return RedirectResponse(url=f"/jobs/html?{params}", status_code=303)
        except Exception as e:
            print(f"Error editing job: {e}")
            params = urlencode({"error": f"Invalid cron string: {cron}"})
            return RedirectResponse(
                url=f"/jobs/{job_id}/edit?{params}", status_code=303
            )
    return RedirectResponse(url="/jobs/html", status_code=303)


@app.post("/jobs/{job_id}/trigger")
def trigger_job(job_id: str):
    """Manually trigger a job to run immediately."""
    job = scheduler.get_job(job_id)
    if job:
        try:
            job.modify(next_run_time=None)
            scheduler.wakeup()
            log_job_run(job_id, "Job manually triggered.")
            params = urlencode({"msg": "Job triggered."})
            return RedirectResponse(url=f"/jobs/html?{params}", status_code=303)
        except Exception as e:
            print(f"Error triggering job: {e}")
            params = urlencode({"error": "Failed to trigger job."})
            return RedirectResponse(url=f"/jobs/html?{params}", status_code=303)
    return RedirectResponse(url="/jobs/html", status_code=303)





@app.post("/jobs/{job_id}/enable")
def enable_job(job_id: str):
    """Enable (resume) a paused job."""
    job = scheduler.get_job(job_id)
    if job:
        scheduler.resume_job(job_id)
        log_job_run(job_id, "Job enabled.")
        params = urlencode({"msg": "Job enabled."})
        return RedirectResponse(url=f"/jobs/html?{params}", status_code=303)
    return RedirectResponse(url="/jobs/html", status_code=303)


@app.post("/jobs/{job_id}/disable")
def disable_job(job_id: str):
    """Disable (pause) a job."""
    job = scheduler.get_job(job_id)
    if job:
        scheduler.pause_job(job_id)
        log_job_run(job_id, "Job disabled.")
        params = urlencode({"msg": "Job disabled."})
        return RedirectResponse(url=f"/jobs/html?{params}", status_code=303)
    return RedirectResponse(url="/jobs/html", status_code=303)


@app.post("/jobs/{job_id}/delete")
def delete_job(job_id: str):
    """Delete a job from the scheduler."""
    scheduler.remove_job(job_id)
    log_job_run(job_id, "Job deleted.")
    params = urlencode({"msg": "Job deleted."})
    return RedirectResponse(url=f"/jobs/html?{params}", status_code=303)


@app.post("/jobs/add")
def add_job(name: str = Form(...), cron: str = Form(...)):
    """Add a new job with the given name and cron string (dummy function)."""
    try:
        trigger = CronTrigger.from_crontab(cron)
        scheduler.add_job(dummy_job, trigger, id=name, name=name, replace_existing=True)
        log_job_run(name, f"Job added with cron: {cron}")
        params = urlencode({"msg": "Job added."})
        return RedirectResponse(url=f"/jobs/html?{params}", status_code=303)
    except Exception as e:
        print(f"Error adding job: {e}")
        params = urlencode({"error": f"Invalid cron string: {cron}"})
        return RedirectResponse(url=f"/jobs/html?{params}", status_code=303)


# Future endpoints:
# - GET /jobs/{job_id}/logs (view logs)


@app.get("/ask/proactive", response_class=JSONResponse)
def ask_proactive():
    """Surface forgotten/stale content (top 5)."""
    mgr = get_metadata_manager()
    surfacer = ProactiveSurfacer(mgr)
    items = surfacer.surface_forgotten_content(n=5)
    return {
        "forgotten": [
            {
                "title": getattr(i, "title", None),
                "updated_at": getattr(i, "updated_at", None),
            }
            for i in items
        ]
    }


@app.get("/ask/temporal", response_class=JSONResponse)
def ask_temporal():
    """Show time-aware content relationships (max 10)."""
    mgr = get_metadata_manager()
    engine = TemporalEngine(mgr)
    rels = engine.get_time_aware_relationships(max_delta_days=2)
    return {
        "relationships": [
            {
                "from": getattr(a, "title", None),
                "to": getattr(b, "title", None),
                "days": d,
            }
            for a, b, d in rels[:10]
        ]
    }


@app.post("/ask/socratic", response_class=JSONResponse)
def ask_socratic(content: str = Form(...)):
    """Generate Socratic questions from content."""
    engine = QuestionEngine()
    questions = engine.generate_questions(content)
    return {"questions": questions}


@app.get("/ask/recall", response_class=JSONResponse)
def ask_recall():
    """Show most overdue items for spaced repetition (top 5)."""
    mgr = get_metadata_manager()
    engine = RecallEngine(mgr)
    items = engine.schedule_spaced_repetition(n=5)
    return {
        "due_for_review": [
            {
                "title": getattr(i, "title", None),
                "last_reviewed": getattr(i, "type_specific", {}).get(
                    "last_reviewed", None
                ),
            }
            for i in items
        ]
    }


@app.get("/ask/patterns", response_class=JSONResponse)
def ask_patterns():
    """Show top tags and sources (top 5)."""
    mgr = get_metadata_manager()
    detector = PatternDetector(mgr)
    patterns = detector.find_patterns(n=5)
    return {"top_tags": patterns["top_tags"], "top_sources": patterns["top_sources"]}


@app.get("/ask/html", response_class=HTMLResponse)
async def ask_dashboard(request: Request, feature: str = ""):
    """Render the cognitive amplification dashboard with the selected feature."""
    mgr = get_metadata_manager()
    data = None
    if feature == "proactive":
        surfacer = ProactiveSurfacer(mgr)
        data = {
            "forgotten": [
                {
                    "title": getattr(i, "title", None),
                    "updated_at": getattr(i, "updated_at", None),
                }
                for i in surfacer.surface_forgotten_content(n=5)
            ]
        }
    elif feature == "temporal":
        engine = TemporalEngine(mgr)
        rels = engine.get_time_aware_relationships(max_delta_days=2)
        data = {
            "relationships": [
                {
                    "from": getattr(a, "title", None),
                    "to": getattr(b, "title", None),
                    "days": d,
                }
                for a, b, d in rels[:10]
            ]
        }
    elif feature == "recall":
        engine = RecallEngine(mgr)
        items = engine.schedule_spaced_repetition(n=5)
        data = {
            "due_for_review": [
                {
                    "title": getattr(i, "title", None),
                    "last_reviewed": getattr(i, "type_specific", {}).get(
                        "last_reviewed", None
                    ),
                }
                for i in items
            ]
        }
    elif feature == "patterns":
        detector = PatternDetector(mgr)
        patterns = detector.find_patterns(n=5)
        data = {
            "top_tags": patterns["top_tags"],
            "top_sources": patterns["top_sources"],
        }
    # Socratic handled by POST
    return templates.TemplateResponse(
        "ask_dashboard.html", {"request": request, "feature": feature, "data": data}
    )


@app.post("/ask/html", response_class=HTMLResponse)
async def ask_dashboard_post(
    request: Request, feature: str = Form(""), content: str = Form("")
):
    """Handle Socratic question form submission."""
    data = None
    if feature == "socratic" and content:
        engine = QuestionEngine()
        questions = engine.generate_questions(content)
        data = {"questions": questions}
    return templates.TemplateResponse(
        "ask_dashboard.html", {"request": request, "feature": feature, "data": data}
    )


# Mobile-optimized routes
@app.get("/mobile", response_class=HTMLResponse)
async def mobile_dashboard(request: Request, feature: str = "", search: str = "", 
                          date_filter: str = "", type_filter: str = "", source_filter: str = ""):
    """Mobile-optimized cognitive dashboard."""
    data = None
    recent_content = None
    
    if not ASK_AVAILABLE:
        return templates.TemplateResponse(
            "mobile_dashboard.html", 
            {"request": request, "feature": feature, "data": {"error": "Cognitive features not available"}}
        )
    
    mgr = get_metadata_manager()
    
    # Handle content browsing
    if feature == "browse" or not feature:
        import sqlite3
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        # Build WHERE conditions based on filters
        where_conditions = ["title IS NOT NULL AND title != ''"]
        params = []
        
        if search:
            where_conditions.append("(title LIKE ? OR content LIKE ?)")
            params.extend([f'%{search}%', f'%{search}%'])
        
        if type_filter:
            where_conditions.append("content_type LIKE ?")
            params.append(f'%{type_filter}%')
        
        if date_filter:
            import datetime
            today = datetime.date.today()
            if date_filter == "today":
                where_conditions.append("DATE(created_at) = ?")
                params.append(today.isoformat())
            elif date_filter == "week":
                week_ago = today - datetime.timedelta(days=7)
                where_conditions.append("DATE(created_at) >= ?")
                params.append(week_ago.isoformat())
            elif date_filter == "month":
                month_ago = today - datetime.timedelta(days=30)
                where_conditions.append("DATE(created_at) >= ?")
                params.append(month_ago.isoformat())
            elif date_filter == "year":
                year_ago = today - datetime.timedelta(days=365)
                where_conditions.append("DATE(created_at) >= ?")
                params.append(year_ago.isoformat())
        
        where_clause = " AND ".join(where_conditions)
        
        cursor.execute(f"""
            SELECT id, title, content, content_type, created_at 
            FROM content 
            WHERE {where_clause}
            ORDER BY created_at DESC 
            LIMIT 20
        """, params)
        
        recent_content = [
            {
                "id": row[0],
                "title": row[1],
                "content": row[2],
                "content_type": row[3], 
                "created_at": row[4]
            }
            for row in cursor.fetchall()
        ]
        conn.close()
    
    # Handle cognitive features (same logic as desktop)
    elif feature == "proactive":
        try:
            surfacer = ProactiveSurfacer(mgr)
            forgotten = surfacer.surface_forgotten_content(n=10)
            data = {
                "forgotten": [
                    {"title": getattr(f, "title", "Untitled"), "updated_at": getattr(f, "updated_at", "Unknown")}
                    for f in forgotten
                ]
            }
        except Exception as e:
            print(f"Proactive error: {e}")
            data = {"forgotten": [{"title": "Demo: Machine Learning Article", "updated_at": "2024-08-15"}, 
                                 {"title": "Demo: Python Best Practices", "updated_at": "2024-08-10"}]}
    elif feature == "temporal":
        engine = TemporalEngine(mgr)
        rels = engine.identify_temporal_relationships(n=10)
        data = {
            "relationships": [
                {
                    "from": getattr(a, "title", None),
                    "to": getattr(b, "title", None),
                    "days": d,
                }
                for a, b, d in rels[:10]
            ]
        }
    elif feature == "recall":
        engine = RecallEngine(mgr)
        items = engine.schedule_spaced_repetition(n=10)
        data = {
            "due_for_review": [
                {
                    "title": getattr(i, "title", None),
                    "last_reviewed": getattr(i, "type_specific", {}).get("last_reviewed", None),
                }
                for i in items
            ]
        }
    elif feature == "patterns":
        detector = PatternDetector(mgr)
        patterns = detector.find_patterns(n=10)
        data = {
            "top_tags": patterns.get("top_tags", []),
            "top_sources": patterns.get("top_sources", []),
        }
    
    return templates.TemplateResponse(
        "mobile_dashboard.html", 
        {
            "request": request, 
            "feature": feature, 
            "data": data,
            "recent_content": recent_content,
            "search": search,
            "date_filter": date_filter,
            "type_filter": type_filter,
            "source_filter": source_filter
        }
    )


@app.post("/mobile", response_class=HTMLResponse)
async def mobile_dashboard_post(request: Request, feature: str = Form(""), content: str = Form("")):
    """Handle mobile form submissions."""
    data = None
    if feature == "socratic" and content:
        engine = QuestionEngine()
        questions = engine.generate_questions(content)
        data = {"questions": questions}
    
    return templates.TemplateResponse(
        "mobile_dashboard.html", 
        {"request": request, "feature": feature, "data": data}
    )


# Content Management API Endpoints
@app.delete("/mobile/content/{content_id}")
async def delete_content(content_id: int):
    """Delete content item"""
    try:
        import sqlite3
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM content WHERE id = ?", (content_id,))
        if cursor.rowcount == 0:
            conn.close()
            return {"success": False, "error": "Content not found"}
        
        conn.commit()
        conn.close()
        return {"success": True, "message": "Content deleted successfully"}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.post("/mobile/content/{content_id}/tags")
async def tag_content(content_id: int, tags: str = Form(...)):
    """Add tags to content item"""
    try:
        import sqlite3
        import json
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        # Check if content exists
        cursor.execute("SELECT tags FROM content WHERE id = ?", (content_id,))
        result = cursor.fetchone()
        if not result:
            conn.close()
            return {"success": False, "error": "Content not found"}
        
        # Parse existing tags
        existing_tags = json.loads(result[0] or "[]")
        new_tags = [tag.strip() for tag in tags.split(",") if tag.strip()]
        
        # Merge tags (avoid duplicates)
        all_tags = list(set(existing_tags + new_tags))
        
        cursor.execute("UPDATE content SET tags = ? WHERE id = ?", 
                      (json.dumps(all_tags), content_id))
        conn.commit()
        conn.close()
        
        return {"success": True, "message": f"Tags added: {', '.join(new_tags)}", "tags": all_tags}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.post("/mobile/content/{content_id}/archive")
async def archive_content(content_id: int):
    """Archive content item"""
    try:
        import sqlite3
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        cursor.execute("UPDATE content SET archived = 1 WHERE id = ?", (content_id,))
        if cursor.rowcount == 0:
            conn.close()
            return {"success": False, "error": "Content not found"}
        
        conn.commit()
        conn.close()
        return {"success": True, "message": "Content archived successfully"}
    except Exception as e:
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Atlas Mobile Web Interface...")
    print("📱 Mobile dashboard: http://localhost:8002/mobile")
    print("🖥️  Desktop dashboard: http://localhost:8002/ask/html")
    uvicorn.run(app, host="0.0.0.0", port=8002)

