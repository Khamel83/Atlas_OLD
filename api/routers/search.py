"""Search API router for Atlas content search functionality.

Provides FastAPI endpoints for searching content with support for
filtering, pagination, and comprehensive error handling.
"""

import os
import sqlite3
import sys
from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

# Add parent directory to path for module imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from helpers.config import load_config
from helpers.metadata_manager import MetadataManager

router = APIRouter()


def get_metadata_manager() -> MetadataManager:
    """Dependency injection for MetadataManager.
    
    Returns:
        Configured MetadataManager instance
        
    Raises:
        HTTPException: If manager initialization fails
    """
    try:
        config = load_config()
        return MetadataManager(config)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initialize metadata manager: {e}")


class SearchResult(BaseModel):
    """Search result model for API responses."""
    uid: str = Field(..., description="Unique identifier for the content")
    title: str = Field(..., description="Content title")
    source: str = Field(..., description="Content source URL")
    content_type: str = Field(..., description="Type of content (article, document, etc.)")
    excerpt: str = Field(..., description="Content excerpt or snippet")
    score: float = Field(..., ge=0, le=1, description="Relevance score (0-1)")


class SearchResponse(BaseModel):
    """Search API response model."""
    results: List[SearchResult] = Field(default_factory=list, description="List of search results")
    total: int = Field(ge=0, description="Total number of matching results")
    query: str = Field(..., description="Original search query")
    processing_time_ms: Optional[float] = Field(None, description="Query processing time in milliseconds")

def get_search_db_path() -> str:
    """Get the path to the search database.
    
    Returns:
        Path to the search database file
    """
    return os.path.join("data", "enhanced_search.db")

@router.get("/", response_model=SearchResponse)
async def search_content(
    query: str = Query(..., min_length=1, description="Search query string"),
    skip: int = Query(0, ge=0, description="Number of results to skip for pagination"),
    limit: int = Query(20, ge=1, le=100, description="Maximum number of results to return"),
    content_type: Optional[str] = Query(None, description="Filter by content type"),
    manager: MetadataManager = Depends(get_metadata_manager)
) -> SearchResponse:
    """Search content using SQLite full-text search.
    
    Performs full-text search across indexed content with support for
    content type filtering and pagination.
    
    Args:
        query: Search query string (required, minimum 1 character)
        skip: Number of results to skip (default: 0)
        limit: Maximum results to return (1-100, default: 20)
        content_type: Optional content type filter
        manager: Injected MetadataManager dependency
        
    Returns:
        SearchResponse containing results, total count, query, and timing
        
    Raises:
        HTTPException: If search fails or database is unavailable
    """
    import time
    start_time = time.time()
    
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
        
        # Calculate processing time
        processing_time_ms = (time.time() - start_time) * 1000
        
        return SearchResponse(
            results=results, 
            total=total, 
            query=query, 
            processing_time_ms=processing_time_ms
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error performing search: {str(e)}")

@router.post("/index")
async def index_content(
    manager: MetadataManager = Depends(get_metadata_manager)
) -> Dict[str, str]:
    """Index all content for full-text search.
    
    Rebuilds the search index from all available content metadata.
    This operation may take some time for large content collections.
    
    Args:
        manager: Injected MetadataManager dependency
        
    Returns:
        Dictionary with indexing status and count
        
    Raises:
        HTTPException: If indexing fails
    """
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