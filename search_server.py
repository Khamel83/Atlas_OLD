#!/usr/bin/env python3
"""
Simple Search Server for Atlas

Actually works with the 5,772 processed articles
"""

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import re
from pathlib import Path

app = FastAPI(title="Atlas Simple Search")

# Serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the search interface"""
    with open("simple_search.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/search")
async def search(q: str = Query(..., description="Search query")):
    """Search the Atlas database"""
    
    if len(q.strip()) < 2:
        return JSONResponse({"results": [], "total": 0, "query": q})
    
    try:
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        # Build search query - search in both title and content
        search_terms = q.strip().split()
        conditions = []
        params = []
        
        for term in search_terms:
            # Search both title and content
            condition = "(title LIKE ? OR content LIKE ?)"
            conditions.append(condition)
            params.extend([f"%{term}%", f"%{term}%"])
        
        where_clause = " AND ".join(conditions)
        
        # Get total count
        count_query = f"SELECT COUNT(*) FROM content WHERE {where_clause}"
        cursor.execute(count_query, params)
        total = cursor.fetchone()[0]
        
        # Get results with limit
        query = f"""
            SELECT title, content, url 
            FROM content 
            WHERE {where_clause}
            ORDER BY 
                CASE WHEN title LIKE ? THEN 1 ELSE 2 END,
                LENGTH(content) DESC
            LIMIT 20
        """
        
        # Add title match boost parameter
        title_boost_param = f"%{q}%"
        cursor.execute(query, params + [title_boost_param])
        
        results = []
        for title, content, url in cursor.fetchall():
            # Clean up content for display
            clean_content = re.sub(r'\s+', ' ', content).strip()
            
            # Highlight search terms (basic)
            display_title = title
            display_content = clean_content
            
            for term in search_terms:
                pattern = re.compile(re.escape(term), re.IGNORECASE)
                display_title = pattern.sub(f"**{term}**", display_title)
                # Don't highlight content to avoid breaking HTML
            
            results.append({
                "title": title,
                "content": clean_content,
                "url": url,
                "display_title": display_title
            })
        
        conn.close()
        
        return JSONResponse({
            "results": results,
            "total": total,
            "query": q,
            "found": len(results)
        })
        
    except Exception as e:
        print(f"Search error: {e}")
        return JSONResponse({
            "results": [],
            "total": 0,
            "query": q,
            "error": str(e)
        })

@app.get("/simple-search")
async def simple_search(q: str = Query(..., description="Simple search query")):
    """Backup search method"""
    
    try:
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        # Very simple search - just LIKE
        query = """
            SELECT title, content, url 
            FROM content 
            WHERE title LIKE ? OR content LIKE ?
            ORDER BY 
                CASE WHEN title LIKE ? THEN 1 ELSE 2 END
            LIMIT 10
        """
        
        search_param = f"%{q}%"
        cursor.execute(query, [search_param, search_param, search_param])
        
        results = []
        for title, content, url in cursor.fetchall():
            results.append({
                "title": title,
                "content": re.sub(r'\s+', ' ', content).strip(),
                "url": url
            })
        
        conn.close()
        
        return JSONResponse({
            "results": results,
            "total": len(results),
            "query": q
        })
        
    except Exception as e:
        return JSONResponse({
            "results": [],
            "total": 0,
            "query": q,
            "error": str(e)
        })

@app.get("/stats")
async def get_stats():
    """Get database statistics"""
    
    try:
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        # Get basic stats
        cursor.execute("SELECT COUNT(*) FROM content")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM content WHERE title LIKE '%TRANSCRIPT%'")
        transcripts = cursor.fetchone()[0]
        
        cursor.execute("SELECT AVG(LENGTH(content)) FROM content")
        avg_length = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM content WHERE LENGTH(content) > 10000")
        long_articles = cursor.fetchone()[0]
        
        # Sample recent articles
        cursor.execute("SELECT title FROM content ORDER BY created_at DESC LIMIT 5")
        recent = [row[0] for row in cursor.fetchall()]
        
        conn.close()
        
        return JSONResponse({
            "total_articles": total,
            "transcripts": transcripts,
            "articles": total - transcripts,
            "avg_length": int(avg_length) if avg_length else 0,
            "long_articles": long_articles,
            "recent_titles": recent
        })
        
    except Exception as e:
        return JSONResponse({"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)