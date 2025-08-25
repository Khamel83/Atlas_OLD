#!/usr/bin/env python3
"""
Simple Search API for Atlas - bypasses FTS5 issues
"""

from fastapi import FastAPI, Query
from typing import List, Dict, Any
import uvicorn
import sqlite3
from helpers.simple_database import SimpleDatabase

app = FastAPI(title="Atlas Simple Search")

@app.get("/search")
def search_content(
    q: str = Query(..., description="Search query"),
    limit: int = Query(10, description="Number of results"),
    content_type: str = Query(None, description="Filter by content type")
):
    """Simple content search using LIKE queries"""
    
    db = SimpleDatabase()
    conn = db.get_connection()
    cursor = conn.cursor()
    
    # Build query
    base_query = """
        SELECT id, title, url, content_type, 
               substr(content, 1, 200) as excerpt,
               created_at
        FROM content 
        WHERE (content LIKE ? OR title LIKE ?)
    """
    
    params = [f"%{q}%", f"%{q}%"]
    
    if content_type:
        base_query += " AND content_type = ?"
        params.append(content_type)
    
    base_query += " ORDER BY created_at DESC LIMIT ?"
    params.append(limit)
    
    cursor.execute(base_query, params)
    results = cursor.fetchall()
    
    # Format results
    search_results = []
    for row in results:
        search_results.append({
            "id": row[0],
            "title": row[1],
            "url": row[2] or "",
            "content_type": row[3],
            "excerpt": row[4].strip() if row[4] else "",
            "created_at": row[5]
        })
    
    conn.close()
    
    return {
        "query": q,
        "total_results": len(search_results),
        "results": search_results
    }

@app.get("/stats")
def get_stats():
    """Get database statistics"""
    db = SimpleDatabase()
    conn = db.get_connection()
    cursor = conn.cursor()
    
    # Total count
    cursor.execute('SELECT COUNT(*) FROM content')
    total = cursor.fetchone()[0]
    
    # By content type
    cursor.execute('''
        SELECT content_type, COUNT(*) 
        FROM content 
        GROUP BY content_type 
        ORDER BY COUNT(*) DESC
    ''')
    types = cursor.fetchall()
    
    conn.close()
    
    return {
        "total_records": total,
        "content_types": dict(types)
    }

if __name__ == "__main__":
    print("🚀 Starting Atlas Simple Search API on port 8002...")
    uvicorn.run(app, host="0.0.0.0", port=8002)