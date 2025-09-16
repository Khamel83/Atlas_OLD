"""
Simple REST API for Atlas

Provides mobile and desktop integration endpoints for the simplified Atlas system.
FastAPI-based with automatic documentation and CORS support.
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import asyncio
import logging
from datetime import datetime
import uvicorn

from core.database import get_database, Content
from core.processor import get_processor, ProcessingResult


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Atlas API",
    description="Simple API for Atlas content management system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware for mobile/web access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for API
class ContentRequest(BaseModel):
    """Request model for adding content"""
    content: str = Field(..., description="Content to process (URL, text, etc.)")
    title: Optional[str] = Field(None, description="Optional title for the content")
    source: Optional[str] = Field(None, description="Source of the content")


class ContentResponse(BaseModel):
    """Response model for content operations"""
    id: int
    title: str
    url: Optional[str]
    content_type: str
    created_at: str
    updated_at: str
    stage: int
    ai_summary: Optional[str]
    ai_tags: Optional[str]


class BatchContentRequest(BaseModel):
    """Request model for batch content processing"""
    items: List[ContentRequest] = Field(..., description="List of content items to process")


class SearchRequest(BaseModel):
    """Request model for search operations"""
    query: str = Field(..., description="Search query")
    limit: int = Field(50, description="Maximum number of results")
    offset: int = Field(0, description="Offset for pagination")


class HealthResponse(BaseModel):
    """Response model for health checks"""
    status: str
    database: str
    processor: str
    total_content: int
    timestamp: str


# Dependency to get database instance
async def get_db():
    """Get database instance"""
    return get_database()


# Dependency to get processor instance
async def get_proc():
    """Get processor instance"""
    return get_processor()


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Atlas API",
        "version": "1.0.0",
        "description": "Simple content management system API",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "content": "/content",
            "search": "/search",
            "stats": "/stats"
        }
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    try:
        db = get_database()
        processor = get_processor()

        # Check database
        stats = db.get_statistics()
        db_status = "healthy" if stats else "unhealthy"

        # Check processor
        processor_health = await processor.health_check()
        proc_status = processor_health['status']

        overall_status = "healthy"
        if db_status == "unhealthy" or proc_status == "degraded":
            overall_status = "degraded"
        elif db_status == "unhealthy" and proc_status == "degraded":
            overall_status = "unhealthy"

        return HealthResponse(
            status=overall_status,
            database=db_status,
            processor=proc_status,
            total_content=stats.get('total_content', 0) if stats else 0,
            timestamp=datetime.utcnow().isoformat()
        )
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/content", response_model=ContentResponse)
async def add_content(
    request: ContentRequest,
    background_tasks: BackgroundTasks,
    db=Depends(get_db),
    processor=Depends(get_proc)
):
    """Add and process new content"""
    try:
        # Process content in background
        result = await processor.process(
            request.content,
            title=request.title or f"Content - {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}"
        )

        if not result.success:
            raise HTTPException(status_code=400, detail=result.error)

        # Return processed content
        return ContentResponse(
            id=result.content.id,
            title=result.content.title,
            url=result.content.url,
            content_type=result.content.content_type,
            created_at=result.content.created_at,
            updated_at=result.content.updated_at,
            stage=result.content.stage,
            ai_summary=result.content.ai_summary,
            ai_tags=result.content.ai_tags
        )
    except Exception as e:
        logger.error(f"Failed to add content: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/content/batch")
async def add_content_batch(
    request: BatchContentRequest,
    background_tasks: BackgroundTasks,
    db=Depends(get_db),
    processor=Depends(get_proc)
):
    """Add and process multiple content items"""
    try:
        results = await processor.process_batch([
            item.content for item in request.items
        ])

        successful = 0
        failed = 0
        processed_items = []

        for i, result in enumerate(results):
            if isinstance(result, Exception):
                failed += 1
                logger.error(f"Item {i+1} failed: {result}")
            elif result.success:
                successful += 1
                processed_items.append({
                    "id": result.content.id,
                    "title": result.content.title,
                    "status": "success"
                })
            else:
                failed += 1
                logger.error(f"Item {i+1} failed: {result.error}")

        return {
            "total_items": len(request.items),
            "successful": successful,
            "failed": failed,
            "processed_items": processed_items
        }
    except Exception as e:
        logger.error(f"Batch processing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/content/{content_id}", response_model=ContentResponse)
async def get_content(content_id: int, db=Depends(get_db)):
    """Get specific content by ID"""
    try:
        content = db.get_content(content_id)
        if not content:
            raise HTTPException(status_code=404, detail="Content not found")

        return ContentResponse(
            id=content.id,
            title=content.title,
            url=content.url,
            content_type=content.content_type,
            created_at=content.created_at,
            updated_at=content.updated_at,
            stage=content.stage,
            ai_summary=content.ai_summary,
            ai_tags=content.ai_tags
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get content {content_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search")
async def search_content(request: SearchRequest, db=Depends(get_db)):
    """Search content"""
    try:
        results = db.search_content(
            request.query,
            limit=request.limit,
            offset=request.offset
        )

        return {
            "query": request.query,
            "limit": request.limit,
            "offset": request.offset,
            "total_results": len(results),
            "results": [
                {
                    "id": content.id,
                    "title": content.title,
                    "url": content.url,
                    "content_type": content.content_type,
                    "created_at": content.created_at,
                    "stage": content.stage,
                    "ai_summary": content.ai_summary
                }
                for content in results
            ]
        }
    except Exception as e:
        logger.error(f"Search failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/content")
async def list_content(
    limit: int = 50,
    offset: int = 0,
    content_type: Optional[str] = None,
    stage: Optional[int] = None,
    db=Depends(get_db)
):
    """List content with optional filtering"""
    try:
        # Build query conditions
        conditions = []
        params = []

        if content_type:
            conditions.append("content_type = ?")
            params.append(content_type)

        if stage is not None:
            conditions.append("stage = ?")
            params.append(stage)

        # Build WHERE clause
        where_clause = ""
        if conditions:
            where_clause = "WHERE " + " AND ".join(conditions)

        # Build query
        query = f"""
            SELECT id, title, url, content_type, created_at, updated_at, stage, ai_summary
            FROM content
            {where_clause}
            ORDER BY created_at DESC
            LIMIT ? OFFSET ?
        """
        params.extend([limit, offset])

        # Execute query
        conn = db.get_connection()
        cursor = conn.execute(query, params)
        rows = cursor.fetchall()

        # Convert to response format
        results = []
        for row in rows:
            results.append({
                "id": row[0],
                "title": row[1],
                "url": row[2],
                "content_type": row[3],
                "created_at": row[4],
                "updated_at": row[5],
                "stage": row[6],
                "ai_summary": row[7]
            })

        return {
            "limit": limit,
            "offset": offset,
            "total_results": len(results),
            "results": results
        }
    except Exception as e:
        logger.error(f"Failed to list content: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats")
async def get_stats(db=Depends(get_db)):
    """Get system statistics"""
    try:
        stats = db.get_statistics()
        return stats
    except Exception as e:
        logger.error(f"Failed to get stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/content/{content_id}")
async def delete_content(content_id: int, db=Depends(get_db)):
    """Delete content by ID"""
    try:
        success = db.delete_content(content_id)
        if not success:
            raise HTTPException(status_code=404, detail="Content not found")

        return {"message": "Content deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete content {content_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/content/types")
async def get_content_types(db=Depends(get_db)):
    """Get available content types"""
    try:
        conn = db.get_connection()
        cursor = conn.execute("""
            SELECT DISTINCT content_type, COUNT(*) as count
            FROM content
            GROUP BY content_type
            ORDER BY count DESC
        """)
        results = cursor.fetchall()

        return {
            "content_types": [
                {"type": row[0], "count": row[1]}
                for row in results
            ]
        }
    except Exception as e:
        logger.error(f"Failed to get content types: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.on_event("startup")
async def startup_event():
    """Startup event handler"""
    logger.info("Atlas API starting up...")
    try:
        # Initialize database and processor
        db = get_database()
        processor = get_processor()
        logger.info("Database and processor initialized successfully")
    except Exception as e:
        logger.error(f"Startup failed: {e}")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler"""
    logger.info("Atlas API shutting down...")
    try:
        # Cleanup processor resources
        processor = get_processor()
        await processor.close()
        logger.info("Processor resources cleaned up")
    except Exception as e:
        logger.error(f"Shutdown cleanup failed: {e}")


if __name__ == "__main__":
    # Run the API server
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=7444,
        reload=True,
        log_level="info"
    )