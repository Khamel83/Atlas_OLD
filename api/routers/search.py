from fastapi import APIRouter, HTTPException, Query, Depends
from pydantic import BaseModel
from typing import List, Optional
import os
import sys
import sqlite3

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from helpers.metadata_manager import MetadataManager
from helpers.config import load_config

router = APIRouter()

# Dependency to get metadata manager
def get_metadata_manager():
    config = load_config()
    return MetadataManager(config)

class SearchResult(BaseModel):
    uid: str
    title: str
    source: str
    content_type: str
    excerpt: str
    score: float

class SearchResponse(BaseModel):
    results: List[SearchResult]
    total: int

def get_search_db_path():
    """Get the path to the search database"""
    return os.path.join("data", "enhanced_search.db")

@router.get("/", response_model=SearchResponse)
async def search_content(
    query: str,
    skip: int = 0,
    limit: int = 20,
    content_type: Optional[str] = None,
    manager: MetadataManager = Depends(get_metadata_manager)
):
    """Search content using SQLite full-text search"""
    try:
        # Check if search database exists
        db_path = get_search_db_path()
        if not os.path.exists(db_path):
            # Try to create index if it doesn't exist
            await index_content(manager)
        
        # Connect to search database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Build FTS query
        fts_query = f'"{query}"'  # Exact phrase match
        
        # Prepare filters
        filters = []
        if content_type:
            filters.append(f"content_type = '{content_type}'")
        
        # Build WHERE clause
        where_clause = ""
        if filters:
            where_clause = "AND " + " AND ".join(filters)
        
        # Execute search query using our populated search_index table
        sql = f"""
        SELECT content_id, title, url, content_type, 
               SUBSTR(content, 1, 200) as excerpt,
               1.0 as score
        FROM search_index 
        WHERE content LIKE ? OR title LIKE ? {where_clause}
        ORDER BY 
            CASE 
                WHEN title LIKE ? THEN 1
                WHEN content LIKE ? THEN 2
                ELSE 3
            END,
            LENGTH(content) DESC
        LIMIT ? OFFSET ?
        """
        
        like_query = f"%{query}%"
        cursor.execute(sql, (like_query, like_query, like_query, like_query, limit, skip))
        rows = cursor.fetchall()
        
        # Convert to SearchResult objects
        results = []
        for row in rows:
            results.append(SearchResult(
                uid=row[0],
                title=row[1] if row[1] else "Untitled",
                source=row[2] if row[2] else "",
                content_type=row[3] if row[3] else "unknown",
                excerpt=row[4] if row[4] else "",
                score=row[5] if row[5] is not None else 0.0
            ))
        
        # Get total count
        count_sql = f"""
        SELECT COUNT(*) 
        FROM search_index 
        WHERE content LIKE ? OR title LIKE ? {where_clause}
        """
        cursor.execute(count_sql, (like_query, like_query))
        total = cursor.fetchone()[0]
        
        conn.close()
        
        return SearchResponse(results=results, total=total)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error performing search: {str(e)}")

@router.post("/index")
async def index_content(
    manager: MetadataManager = Depends(get_metadata_manager)
):
    """Index all content for search"""
    try:
        # Get all metadata
        all_metadata = manager.get_all_metadata()
        
        # Create or connect to search database
        db_path = get_search_db_path()
        # Ensure output directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create FTS table if it doesn't exist
        cursor.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS search_index USING fts5(
            uid, title, source, content_type, content, rank
        )
        """)
        
        # Clear existing index
        cursor.execute("DELETE FROM search_index")
        
        # Index each content item
        indexed_count = 0
        for metadata in all_metadata:
            # Read content if available
            content_text = ""
            if metadata.content_path and os.path.exists(metadata.content_path):
                try:
                    with open(metadata.content_path, 'r', encoding='utf-8') as f:
                        content_text = f.read()
                except Exception:
                    pass  # Skip if can't read
            
            # Insert into search index
            cursor.execute("""
            INSERT INTO search_index (uid, title, source, content_type, content)
            VALUES (?, ?, ?, ?, ?)
            """, (
                metadata.uid,
                metadata.title,
                metadata.source,
                metadata.content_type.value,
                content_text
            ))
            indexed_count += 1
        
        conn.commit()
        conn.close()
        
        return {"message": f"Indexed {indexed_count} content items"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error indexing content: {str(e)}")