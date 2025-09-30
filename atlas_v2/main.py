#!/usr/bin/env python3
"""
Atlas v2 - Event-Driven Content Pipeline
Main application entry point

Architecture:
- FastAPI webhook receiver
- Modular processing pipeline (INGEST → EXTRACT → VALIDATE → STORE)
- Scheduler for backlog processing
- SQLite for persistence
- Forever-free OCI deployment

Key Principles:
1. Never re-fetch existing content
2. Preserve all data
3. Event-driven primary, batch secondary
4. CSV/JSON configurable
5. Docker portable
"""

import os
import logging
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Header, BackgroundTasks
from fastapi.responses import JSONResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from typing import Optional, Dict, Any
import uvicorn

from modules.processor import ContentProcessor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager
from modules.id_generator import generate_content_id
from modules.validator import ContentValidator

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/atlas_v2.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Global components
config_manager = ConfigManager()
db_manager = DatabaseManager()
processor = ContentProcessor(db_manager, config_manager)
validator = ContentValidator()
scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown"""
    logger.info("🚀 Starting Atlas v2...")

    # Initialize database
    await db_manager.initialize()

    # Start background scheduler for aggressive backlog processing
    scheduler.add_job(
        process_backlog,
        IntervalTrigger(minutes=5),  # Process every 5 minutes for faster backlog clearing
        id='backlog_processor',
        name='Process backlog every 5 minutes'
    )
    scheduler.start()
    logger.info("📅 Background scheduler started")

    yield

    # Cleanup
    scheduler.shutdown()
    await db_manager.close()
    logger.info("🛑 Atlas v2 shutdown complete")

app = FastAPI(
    title="Atlas v2",
    description="Event-Driven Content Pipeline",
    version="2.0.0",
    lifespan=lifespan
)

@app.post("/webhook/vejla")
async def receive_vejla_webhook(
    payload: Dict[str, Any],
    background_tasks: BackgroundTasks,
    authorization: Optional[str] = Header(None)
):
    """
    Receive webhook from Vejla when content is saved

    Expected payload:
    {
        "type": "podcast" | "newsletter" | "youtube" | "article",
        "url": "https://...",
        "source": "Hard Fork",
        "metadata": {
            "title": "...",
            "date": "2025-09-29",
            "duration_minutes": 45
        }
    }
    """
    # Verify authentication
    webhook_token = os.getenv('WEBHOOK_SECRET_TOKEN')
    if webhook_token and authorization != f"Bearer {webhook_token}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        # Generate unique ID
        content_id = generate_content_id(
            source=payload.get('source', 'unknown'),
            content_type=payload.get('type', 'unknown'),
            url=payload['url'],
            metadata=payload.get('metadata', {})
        )

        # Check if already exists
        if await db_manager.content_exists(content_id):
            logger.info(f"⏭️ Skipping existing content: {content_id}")
            return {
                "status": "skipped",
                "reason": "content_already_exists",
                "content_id": content_id
            }

        # Queue for processing
        await db_manager.enqueue_content(
            content_id=content_id,
            source_url=payload['url'],
            source_name=payload.get('source', 'unknown'),
            content_type=payload.get('type', 'unknown'),
            metadata=payload.get('metadata', {}),
            priority='high'  # Webhook events are high priority
        )

        # Process immediately in background
        background_tasks.add_task(process_single_item, content_id)

        logger.info(f"📥 Queued content for processing: {content_id}")

        return {
            "status": "queued",
            "content_id": content_id,
            "estimated_processing_time_minutes": 2
        }

    except Exception as e:
        logger.error(f"❌ Webhook processing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    try:
        # Check database connection
        db_healthy = await db_manager.health_check()

        # Get queue size
        queue_size = await db_manager.get_queue_size()

        # Get last processed timestamp
        last_processed = await db_manager.get_last_processed_timestamp()

        return {
            "status": "healthy",
            "version": "2.0.0",
            "database_healthy": db_healthy,
            "queue_size": queue_size,
            "last_processed": last_processed,
            "scheduler_running": scheduler.running
        }
    except Exception as e:
        logger.error(f"❌ Health check failed: {e}")
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "error": str(e)
            }
        )

@app.get("/stats")
async def get_stats():
    """Get processing statistics"""
    try:
        stats = await db_manager.get_processing_stats()
        return stats
    except Exception as e:
        logger.error(f"❌ Stats retrieval failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

async def process_single_item(content_id: str):
    """Process a single content item through the pipeline"""
    try:
        logger.info(f"🔄 Processing {content_id}")

        # Update status to processing
        await db_manager.update_queue_status(content_id, 'processing')

        # Run through processing pipeline
        result = await processor.process_content(content_id)

        if result['status'] == 'success':
            logger.info(f"✅ Successfully processed {content_id}")
            await db_manager.update_queue_status(content_id, 'completed')
        elif result['status'] == 'retry':
            logger.warning(f"🔄 Retrying {content_id}: {result['message']}")
            await db_manager.update_queue_status(content_id, 'retry')
        else:
            logger.error(f"❌ Failed to process {content_id}: {result['message']}")
            await db_manager.update_queue_status(content_id, 'failed')

    except Exception as e:
        logger.error(f"❌ Processing error for {content_id}: {e}")
        await db_manager.update_queue_status(content_id, 'failed')

async def process_backlog():
    """Process pending items from the backlog queue"""
    try:
        logger.info("📋 Starting backlog processing...")

        # Get pending items (limited batch size)
        pending_items = await db_manager.get_pending_items(limit=50)

        if not pending_items:
            logger.info("📋 No pending items to process")
            return

        logger.info(f"📋 Processing {len(pending_items)} pending items")

        # Process each item
        for item in pending_items:
            await process_single_item(item['content_id'])

            # Small delay to avoid overwhelming the system
            await asyncio.sleep(1)

        logger.info(f"📋 Backlog processing complete: {len(pending_items)} items")

    except Exception as e:
        logger.error(f"❌ Backlog processing failed: {e}")

def main():
    """Main entry point"""
    # Load environment variables
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    workers = int(os.getenv('WORKERS', 1))

    logger.info(f"🎯 Starting Atlas v2 on {host}:{port}")

    # Start the server
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        workers=workers,
        access_log=True,
        reload=False
    )

if __name__ == "__main__":
    main()