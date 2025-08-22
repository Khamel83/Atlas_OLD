\"\"\"
Content Management API for Atlas
Provides endpoints for managing content ingestion, processing, and metadata.
\"\"\"

from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Query
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
import uuid
from datetime import datetime
import json

# Create router for content management endpoints
content_router = APIRouter(prefix=\"/content\", tags=[\"content management\"])

# Import Atlas helpers
from helpers.metadata_manager import MetadataManager
from helpers.article_fetcher import ArticleFetcher
from helpers.youtube_ingestor import YouTubeIngestor
from helpers.podcast_ingestor import PodcastIngestor

# Initialize core components
metadata_manager = MetadataManager()

class ContentItem(BaseModel):
    uid: str
    title: str
    content_type: str
    status: str
    created_at: str
    updated_at: str
    tags: List[str]
    notes: str
    content_path: Optional[str] = None
    url: Optional[str] = None
    author: Optional[str] = None
    word_count: Optional[int] = None

class ContentCreate(BaseModel):
    urls: List[str]
    content_type: str = \"article\"  # article, youtube, podcast
    tags: List[str] = []
    notes: str = \"\"

class ContentUpdate(BaseModel):
    title: Optional[str] = None
    tags: Optional[List[str]] = None
    notes: Optional[str] = None
    status: Optional[str] = None

class ContentListResponse(BaseModel):
    items: List[ContentItem]
    total: int
    page: int
    per_page: int

class ContentProcessResponse(BaseModel):
    success: bool
    message: str
    content_id: Optional[str] = None
    processing_time: Optional[float] = None

@content_router.get(\"/items\", response_model=ContentListResponse)
async def list_content(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, le=100),
    content_type: Optional[str] = None,
    status: Optional[str] = None,
    tags: Optional[List[str]] = Query(None)
):
    \"\"\"List content items with pagination and filtering\"\"\"
    try:
        # Get all metadata
        filters = {}
        if content_type:
            filters[\"content_type\"] = content_type
        if status:
            filters[\"status\"] = status
        if tags:
            filters[\"tags\"] = tags
            
        all_metadata = metadata_manager.get_all_metadata(filters)
        
        # Apply pagination
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_metadata = all_metadata[start_idx:end_idx]
        
        # Convert to ContentItem objects
        items = []
        for meta in paginated_metadata:
            items.append(ContentItem(
                uid=getattr(meta, \"uid\", \"\"),
                title=getattr(meta, \"title\", \"\"),
                content_type=getattr(meta, \"content_type\", {}).get(\"value\", \"\"),
                status=getattr(meta, \"status\", {}).get(\"value\", \"\"),
                created_at=getattr(meta, \"created_at\", \"\"),
                updated_at=getattr(meta, \"updated_at\", \"\"),
                tags=getattr(meta, \"tags\", []),
                notes=getattr(meta, \"notes\", \"\"),
                content_path=getattr(meta, \"content_path\", None),
                url=getattr(meta, \"url\", None),
                author=getattr(meta, \"author\", None),
                word_count=getattr(meta, \"word_count\", None)
            ))
        
        return ContentListResponse(
            items=items,
            total=len(all_metadata),
            page=page,
            per_page=per_page
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f\"Error listing content: {str(e)}\")

@content_router.get(\"/items/{content_id}\", response_model=ContentItem)
async def get_content(content_id: str):
    \"\"\"Get a specific content item by ID\"\"\"
    try:
        # Find metadata by UID
        all_metadata = metadata_manager.get_all_metadata()
        content_meta = None
        for meta in all_metadata:
            if getattr(meta, \"uid\", None) == content_id:
                content_meta = meta
                break
        
        if not content_meta:
            raise HTTPException(status_code=404, detail=\"Content not found\")
        
        return ContentItem(
            uid=getattr(content_meta, \"uid\", \"\"),
            title=getattr(content_meta, \"title\", \"\"),
            content_type=getattr(content_meta, \"content_type\", {}).get(\"value\", \"\"),
            status=getattr(content_meta, \"status\", {}).get(\"value\", \"\"),
            created_at=getattr(content_meta, \"created_at\", \"\"),
            updated_at=getattr(content_meta, \"updated_at\", \"\"),
            tags=getattr(content_meta, \"tags\", []),
            notes=getattr(content_meta, \"notes\", \"\"),
            content_path=getattr(content_meta, \"content_path\", None),
            url=getattr(content_meta, \"url\", None),
            author=getattr(content_meta, \"author\", None),
            word_count=getattr(content_meta, \"word_count\", None)
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f\"Error retrieving content: {str(e)}\")

@content_router.post(\"/items\", response_model=ContentProcessResponse)
async def create_content(content_data: ContentCreate):
    \"\"\"Submit new content for processing\"\"\"
    try:
        processed_count = 0
        errors = []
        
        for url in content_data.urls:
            try:
                if content_data.content_type == \"article\":
                    # Process article
                    fetcher = ArticleFetcher()
                    result = fetcher.fetch_article(url)
                    if result.get(\"status\") == \"success\":
                        processed_count += 1
                    else:
                        errors.append(f\"Failed to process {url}: {result.get('error', 'Unknown error')}\")
                elif content_data.content_type == \"youtube\":
                    # Process YouTube video
                    ingestor = YouTubeIngestor()
                    result = ingestor.process_video(url)
                    if result.get(\"status\") == \"success\":
                        processed_count += 1
                    else:
                        errors.append(f\"Failed to process {url}: {result.get('error', 'Unknown error')}\")
                elif content_data.content_type == \"podcast\":
                    # Process podcast
                    ingestor = PodcastIngestor()
                    result = ingestor.process_podcast(url)
                    if result.get(\"status\") == \"success\":
                        processed_count += 1
                    else:
                        errors.append(f\"Failed to process {url}: {result.get('error', 'Unknown error')}\")
                else:
                    errors.append(f\"Unsupported content type: {content_data.content_type}\")
            except Exception as e:
                errors.append(f\"Error processing {url}: {str(e)}\")
        
        if processed_count > 0:
            return ContentProcessResponse(
                success=True,
                message=f\"Successfully queued {processed_count} items for processing. {len(errors)} errors occurred.\",
                processing_time=0.0  # In a real implementation, this would be the actual processing time
            )
        else:
            return ContentProcessResponse(
                success=False,
                message=f\"Failed to process any items. Errors: {'; '.join(errors)}\"
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f\"Error creating content: {str(e)}\")

@content_router.put(\"/items/{content_id}\", response_model=ContentItem)
async def update_content(content_id: str, update_data: ContentUpdate):
    \"\"\"Update a content item\"\"\"
    try:
        # Find metadata by UID
        all_metadata = metadata_manager.get_all_metadata()
        content_meta = None
        for meta in all_metadata:
            if getattr(meta, \"uid\", None) == content_id:
                content_meta = meta
                break
        
        if not content_meta:
            raise HTTPException(status_code=404, detail=\"Content not found\")
        
        # Update fields if provided
        if update_data.title is not None:
            content_meta.title = update_data.title
        if update_data.tags is not None:
            content_meta.tags = update_data.tags
        if update_data.notes is not None:
            content_meta.notes = update_data.notes
        if update_data.status is not None:
            content_meta.status = {\"value\": update_data.status}
        
        # Update the metadata
        metadata_manager.save_metadata(content_meta)
        
        return ContentItem(
            uid=getattr(content_meta, \"uid\", \"\"),
            title=getattr(content_meta, \"title\", \"\"),
            content_type=getattr(content_meta, \"content_type\", {}).get(\"value\", \"\"),
            status=getattr(content_meta, \"status\", {}).get(\"value\", \"\"),
            created_at=getattr(content_meta, \"created_at\", \"\"),
            updated_at=getattr(content_meta, \"updated_at\", \"\"),
            tags=getattr(content_meta, \"tags\", []),
            notes=getattr(content_meta, \"notes\", \"\"),
            content_path=getattr(content_meta, \"content_path\", None),
            url=getattr(content_meta, \"url\", None),
            author=getattr(content_meta, \"author\", None),
            word_count=getattr(content_meta, \"word_count\", None)
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f\"Error updating content: {str(e)}\")

@content_router.delete(\"/items/{content_id}\")
async def delete_content(content_id: str):
    \"\"\"Delete a content item\"\"\"
    try:
        # Find metadata by UID
        all_metadata = metadata_manager.get_all_metadata()
        content_meta = None
        for meta in all_metadata:
            if getattr(meta, \"uid\", None) == content_id:
                content_meta = meta
                break
        
        if not content_meta:
            raise HTTPException(status_code=404, detail=\"Content not found\")
        
        # In a real implementation, you would also delete the content files
        # For now, we'll just remove the metadata
        metadata_manager.delete_metadata(content_id)
        
        return {\"message\": \"Content deleted successfully\"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f\"Error deleting content: {str(e)}\")

@content_router.post(\"/items/{content_id}/process\")
async def reprocess_content(content_id: str):
    \"\"\"Reprocess a content item\"\"\"
    try:
        # Find metadata by UID
        all_metadata = metadata_manager.get_all_metadata()
        content_meta = None
        for meta in all_metadata:
            if getattr(meta, \"uid\", None) == content_id:
                content_meta = meta
                break
        
        if not content_meta:
            raise HTTPException(status_code=404, detail=\"Content not found\")
        
        # Get the URL and content type
        url = getattr(content_meta, \"url\", None)
        content_type = getattr(content_meta, \"content_type\", {}).get(\"value\", \"article\")
        
        if not url:
            raise HTTPException(status_code=400, detail=\"Content URL not available for reprocessing\")
        
        # Reprocess based on content type
        if content_type == \"article\":
            fetcher = ArticleFetcher()
            result = fetcher.fetch_article(url)
        elif content_type == \"youtube\":
            ingestor = YouTubeIngestor()
            result = ingestor.process_video(url)
        elif content_type == \"podcast\":
            ingestor = PodcastIngestor()
            result = ingestor.process_podcast(url)
        else:
            raise HTTPException(status_code=400, detail=f\"Unsupported content type: {content_type}\")
        
        if result.get(\"status\") == \"success\":    
            return {\"message\": \"Content reprocessed successfully\"}
        else:
            raise HTTPException(status_code=500, detail=f\"Reprocessing failed: {result.get('error', 'Unknown error')}\")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f\"Error reprocessing content: {str(e)}\")

# Health check for content management service
@content_router.get(\"/health\")
async def content_health_check():
    \"\"\"Health check for content management service\"\"\"
    try:
        # Get content statistics
        all_metadata = metadata_manager.get_all_metadata()
        content_stats = {}
        for meta in all_metadata:
            content_type = getattr(meta, \"content_type\", {}).get(\"value\", \"unknown\")
            content_stats[content_type] = content_stats.get(content_type, 0) + 1
        
        return {
            \"status\": \"healthy\",
            \"service\": \"Atlas Content Management Service\",
            \"total_content_items\": len(all_metadata),
            \"content_by_type\": content_stats
        }
    except Exception as e:
        return {
            \"status\": \"unhealthy\",
            \"service\": \"Atlas Content Management Service\",
            \"error\": str(e)
        }