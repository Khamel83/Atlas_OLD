from fastapi import APIRouter, HTTPException, Query, Depends, File, UploadFile
from pydantic import BaseModel
from typing import List, Optional
import os
import sys
import uuid
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from helpers.metadata_manager import MetadataManager, ContentType, ProcessingStatus
from helpers.config import load_config
from ingest.link_dispatcher import process_url_file

router = APIRouter()

# Dependency to get metadata manager
def get_metadata_manager():
    config = load_config()
    return MetadataManager(config)

class ContentItem(BaseModel):
    uid: str
    title: str
    source: str
    content_type: str
    status: str
    created_at: str
    updated_at: str
    tags: List[str]
    content_path: Optional[str] = None

class ContentListResponse(BaseModel):
    items: List[ContentItem]
    total: int

class ContentSubmission(BaseModel):
    url: str

class BookmarkletSave(BaseModel):
    title: str
    url: str
    content: str
    content_type: str = "article"

@router.get("/", response_model=ContentListResponse)
async def list_content(
    skip: int = 0,
    limit: int = 50,
    content_type: Optional[str] = None,
    tags: Optional[List[str]] = Query(None),
    manager: MetadataManager = Depends(get_metadata_manager)
):
    """List all content with pagination and filtering"""
    try:
        # Prepare filters
        filters = {}
        if content_type:
            filters["content_type"] = content_type
        if tags:
            filters["tags"] = tags
            
        # Get all metadata
        all_metadata = manager.get_all_metadata(filters)
        
        # Apply pagination
        paginated_metadata = all_metadata[skip:skip+limit]
        
        # Convert to ContentItem objects
        items = []
        for metadata in paginated_metadata:
            items.append(ContentItem(
                uid=metadata.uid,
                title=metadata.title,
                source=metadata.source,
                content_type=metadata.content_type.value,
                status=metadata.status.value,
                created_at=metadata.created_at,
                updated_at=metadata.updated_at,
                tags=metadata.tags,
                content_path=metadata.content_path
            ))
        
        return ContentListResponse(items=items, total=len(all_metadata))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing content: {str(e)}")

@router.get("/{content_id}", response_model=ContentItem)
async def get_content(
    content_id: str,
    manager: MetadataManager = Depends(get_metadata_manager)
):
    """Get a specific content item by ID"""
    try:
        metadata = manager.load_metadata(content_id)
        if not metadata:
            raise HTTPException(status_code=404, detail="Content not found")
            
        return ContentItem(
            uid=metadata.uid,
            title=metadata.title,
            source=metadata.source,
            content_type=metadata.content_type.value,
            status=metadata.status.value,
            created_at=metadata.created_at,
            updated_at=metadata.updated_at,
            tags=metadata.tags,
            content_path=metadata.content_path
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving content: {str(e)}")

@router.post("/submit-url", response_model=ContentItem)
async def submit_url_for_processing(
    submission: ContentSubmission,
    manager: MetadataManager = Depends(get_metadata_manager)
):
    """Submit a URL for content processing"""
    try:
        # Create a temporary file with the URL for processing
        temp_file = f"/tmp/atlas_url_submission_{uuid.uuid4()}.txt"
        with open(temp_file, "w") as f:
            f.write(submission.url)
        
        # Process the URL
        config = load_config()
        results = process_url_file(temp_file, config)
        
        # Clean up temp file
        os.remove(temp_file)
        
        # Check if processing was successful
        if results["successful"] and len(results["successful"]) > 0:
            # Load the metadata for the processed content - results["successful"] contains file IDs
            content_id = results["successful"][0]
            metadata = manager.load_metadata(content_id)
            
            if metadata:
                return ContentItem(
                    uid=metadata.uid,
                    title=metadata.title,
                    source=metadata.source,
                    content_type=metadata.content_type.value,
                    status=metadata.status.value,
                    created_at=metadata.created_at,
                    updated_at=metadata.updated_at,
                    tags=metadata.tags,
                    content_path=metadata.content_path
                )
            else:
                raise HTTPException(status_code=500, detail="Content processed but metadata not found")
        elif results.get("duplicate") and len(results["duplicate"]) > 0:
            # URL was skipped as duplicate
            raise HTTPException(status_code=409, detail=f"URL already exists in Atlas: {submission.url}")
        elif results["failed"] and len(results["failed"]) > 0:
            # Processing failed
            raise HTTPException(status_code=422, detail=f"Failed to extract content - website may be blocking automated access")
        else:
            # Unknown state
            raise HTTPException(status_code=500, detail="Unknown processing result")
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error submitting URL: {str(e)}")

@router.post("/save", response_model=dict)
async def save_bookmarklet_content(
    save_data: BookmarkletSave,
    manager: MetadataManager = Depends(get_metadata_manager)
):
    """Save content directly from browser bookmarklet"""
    try:
        # Save content to database using the simple database helper
        from helpers.simple_database import SimpleDatabase
        db = SimpleDatabase()
        with db.get_connection() as conn:
            cursor = conn.execute("""
                INSERT INTO content (title, url, content, content_type, created_at, updated_at)
                VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))
            """, (save_data.title, save_data.url, save_data.content, save_data.content_type))
            conn.commit()
            content_db_id = cursor.lastrowid
        
        return {
            "status": "success",
            "message": f"Content saved successfully: {save_data.title}",
            "id": content_db_id,
            "title": save_data.title
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving content: {str(e)}")

@router.post("/upload-file")
async def upload_file_for_processing(
    file: UploadFile = File(...),
    manager: MetadataManager = Depends(get_metadata_manager)
):
    """Upload a file for content processing"""
    try:
        # Save uploaded file temporarily
        temp_file = f"/tmp/atlas_file_upload_{uuid.uuid4()}_{file.filename}"
        with open(temp_file, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # For now, just acknowledge the upload
        # In a full implementation, this would trigger processing
        return {"message": f"File {file.filename} uploaded successfully", "temp_path": temp_file}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

@router.delete("/{content_id}")
async def delete_content(
    content_id: str,
    manager: MetadataManager = Depends(get_metadata_manager)
):
    """Delete a content item"""
    try:
        # Load metadata first to get file paths
        metadata = manager.load_metadata(content_id)
        if not metadata:
            raise HTTPException(status_code=404, detail="Content not found")
        
        # Delete the metadata file
        manager.delete_metadata(content_id)
        
        # Attempt to delete associated files if they exist
        if metadata.content_path and os.path.exists(metadata.content_path):
            os.remove(metadata.content_path)
        
        # Delete from any other storage locations based on content type
        # This would be expanded based on the actual file structure
        
        return {"message": f"Content {content_id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting content: {str(e)}")