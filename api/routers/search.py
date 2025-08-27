"""Search API router for Atlas content search functionality.

Provides FastAPI endpoints for searching content with support for
filtering, pagination, and comprehensive error handling.
"""

import json
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
    # Enhanced with structured insights
    summary: Optional[str] = Field(None, description="AI-generated summary")
    topics: Optional[List[str]] = Field(None, description="Key topics extracted")
    entities: Optional[List[str]] = Field(None, description="Named entities found")
    quality_score: Optional[float] = Field(None, description="Content quality score (0-1)")
    sentiment: Optional[str] = Field(None, description="Content sentiment")


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
        
        # Attach main atlas database for insights
        atlas_db_path = "data/atlas.db"
        has_insights = os.path.exists(atlas_db_path)
        if has_insights:
            cursor.execute(f"ATTACH DATABASE '{atlas_db_path}' AS atlas")
        
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
        
        if has_insights:
            # Enhanced query with insights data
            sql = f"""
            SELECT DISTINCT 
                si.content_id,
                si.title, 
                si.url,
                si.content_type,
                SUBSTR(si.content, 1, 200) as excerpt,
                CASE 
                    WHEN si.title LIKE ? THEN 1.0
                    WHEN si.content LIKE ? THEN 0.8
                    ELSE 0.6
                END as score,
                ci.summary,
                ci.key_topics,
                ci.entities,
                ci.extraction_quality,
                ci.sentiment
            FROM search_index si
            LEFT JOIN atlas.content_insights ci ON si.content_id = ci.content_id
            WHERE si.content LIKE ? OR si.title LIKE ? {where_clause}
            ORDER BY score DESC, LENGTH(si.content) DESC
            LIMIT ? OFFSET ?
            """
        else:
            # Fallback to basic query
            sql = f"""
            SELECT DISTINCT content_id, title, url, content_type, 
                   SUBSTR(content, 1, 200) as excerpt,
                   CASE 
                       WHEN title LIKE ? THEN 1.0
                       WHEN content LIKE ? THEN 0.8
                       ELSE 0.6
                   END as score,
                   NULL, NULL, NULL, NULL, NULL
            FROM search_index 
            WHERE content LIKE ? OR title LIKE ? {where_clause}
            ORDER BY score DESC, LENGTH(content) DESC
            LIMIT ? OFFSET ?
            """
        
        like_query = f"%{query}%"
        cursor.execute(sql, (like_query, like_query, like_query, like_query, limit, skip))
        rows = cursor.fetchall()
        
        # Convert to SearchResult objects
        results = []
        for row in rows:
            # Basic fields
            uid = row[0]
            title = row[1] if row[1] else "Untitled"
            source = row[2] if row[2] else ""
            content_type = row[3] if row[3] else "unknown"
            excerpt = row[4] if row[4] else ""
            score = row[5] if row[5] is not None else 0.0
            
            # Enhanced fields from insights (if available)
            summary = None
            topics = None
            entities = None
            quality_score = None
            sentiment = None
            
            if has_insights and len(row) > 6:
                summary = row[6]
                
                # Parse JSON fields safely
                try:
                    if row[7]:  # key_topics
                        topics_data = json.loads(row[7]) if isinstance(row[7], str) else row[7]
                        if isinstance(topics_data, list):
                            topics = [t.get('name', str(t)) if isinstance(t, dict) else str(t) for t in topics_data]
                except (json.JSONDecodeError, AttributeError):
                    topics = None
                
                try:
                    if row[8]:  # entities
                        entities_data = json.loads(row[8]) if isinstance(row[8], str) else row[8]
                        if isinstance(entities_data, list):
                            entities = [e.get('name', str(e)) if isinstance(e, dict) else str(e) for e in entities_data]
                except (json.JSONDecodeError, AttributeError):
                    entities = None
                
                quality_score = row[9] if row[9] is not None else None
                sentiment = row[10]
            
            results.append(SearchResult(
                uid=uid,
                title=title,
                source=source,
                content_type=content_type,
                excerpt=excerpt,
                score=score,
                summary=summary,
                topics=topics,
                entities=entities,
                quality_score=quality_score,
                sentiment=sentiment
            ))
        
        # Get total count of unique results
        count_sql = f"""
        SELECT COUNT(DISTINCT content_id) 
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