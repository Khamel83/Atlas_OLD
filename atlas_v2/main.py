#!/usr/bin/env python3
"""
Atlas - Event-Driven Content Pipeline
Main application entry point

Architecture:
- FastAPI webhook receiver
- Enhanced processing pipeline with bulletproof reliability
- Intelligent queue management with deduplication
- Production-grade error handling with circuit breakers
- Dead letter queue for non-processable URLs
- Real-time monitoring and auto-fix capabilities
- SQLite for persistence
- Forever-free OCI deployment

Key Principles:
1. Never re-fetch existing content
2. Bulletproof duplicate prevention
3. Event-driven primary, batch secondary
4. Self-healing and auto-recovery
5. Production-ready reliability
"""

import os
import logging
import asyncio
from contextlib import asynccontextmanager
from datetime import datetime
from fastapi import FastAPI, HTTPException, Header, BackgroundTasks
from fastapi.responses import JSONResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from typing import Optional, Dict, Any
import uvicorn

from modules.enhanced_processor import EnhancedProcessor, get_enhanced_processor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager
from modules.id_generator import generate_content_id
from modules.validator import ContentValidator
from modules.intelligent_monitor import get_intelligent_monitor
from modules.stuck_items_monitor import get_stuck_items_monitor

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
validator = ContentValidator()
scheduler = AsyncIOScheduler()

# Enhanced processor (initialized in lifespan)
enhanced_processor = None

# Intelligent monitor (initialized in lifespan)
intelligent_monitor = None

# Stuck items monitor (initialized in lifespan)
stuck_items_monitor = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown"""
    logger.info("🚀 Starting Atlas with Enhanced Reliability...")

    # Initialize database
    await db_manager.initialize()

    # Initialize enhanced processor
    global enhanced_processor
    enhanced_processor = await get_enhanced_processor(db_manager, config_manager)
    logger.info("⚡ Enhanced processor initialized")

    # Initialize intelligent monitor
    global intelligent_monitor
    intelligent_monitor = await get_intelligent_monitor(db_manager, config_manager)
    logger.info("🤖 Intelligent monitor initialized")

    # Initialize stuck items monitor
    global stuck_items_monitor
    stuck_items_monitor = await get_stuck_items_monitor(db_manager)
    logger.info("🔍 Stuck items monitor initialized")

    # Start background scheduler for enhanced backlog processing
    scheduler.add_job(
        process_backlog_enhanced,
        IntervalTrigger(minutes=5),  # Process every 5 minutes for faster backlog clearing
        id='backlog_processor',
        name='Process backlog every 5 minutes'
    )

    # Start intelligent monitoring
    if intelligent_monitor:
        scheduler.add_job(
            intelligent_monitor.health_check_with_auto_fix,
            IntervalTrigger(minutes=2),  # Check every 2 minutes for auto-fix
            id='intelligent_monitor',
            name='Intelligent monitoring with auto-fix'
        )

    # Start stuck items monitoring
    if stuck_items_monitor:
        scheduler.add_job(
            stuck_items_monitor.generate_health_report,
            IntervalTrigger(minutes=30),  # Check every 30 minutes for stuck items
            id='stuck_items_monitor',
            name='Stuck items monitoring and prevention'
        )
    scheduler.start()
    logger.info("📅 Background scheduler started")

    yield

    # Cleanup
    scheduler.shutdown()
    await db_manager.close()
    logger.info("🛑 Atlas shutdown complete")

app = FastAPI(
    title="Atlas",
    description="Event-Driven Content Pipeline with Production-Grade Reliability",
    version="1.0.0",
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
    # Verify authentication - disabled for testing
    # webhook_token = os.getenv('WEBHOOK_SECRET_TOKEN')
    # if webhook_token and authorization != f"Bearer {webhook_token}":
    #     raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        # Generate unique ID
        content_id = generate_content_id(
            source=payload.get('source', 'unknown'),
            content_type=payload.get('content_type', 'unknown'),
            url=payload.get('content_url', payload.get('url', '')),
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

        # Use enhanced processor for bulletproof queue management
        if enhanced_processor is None:
            raise HTTPException(status_code=503, detail="Enhanced processor not available")

        # Process with enhanced duplicate prevention and reliability
        result = await enhanced_processor.process_content_webhook(
            url=payload['url'],
            source_name=payload.get('source', 'unknown'),
            content_type=payload.get('type', 'unknown'),
            metadata=payload.get('metadata', {})
        )

        logger.info(f"📥 Content processing result: {result}")

        # Map enhanced processor response to webhook response
        if result["status"] == "skipped":
            return {
                "status": "skipped",
                "reason": result["reason"],
                "content_id": result["content_id"]
            }
        elif result["status"] == "rejected":
            return {
                "status": "rejected",
                "reason": result["reason"],
                "content_id": result.get("content_id")
            }
        elif result["status"] == "error":
            return {
                "status": "error",
                "reason": result["reason"],
                "message": result["message"]
            }
        else:
            # Processing started or completed successfully
            return {
                "status": result["status"],
                "content_id": result["content_id"],
                "message": result.get("message", ""),
                "processing_time_seconds": result.get("processing_time", 0),
                "estimated_processing_time_minutes": 2
            }

    except Exception as e:
        logger.error(f"❌ Webhook processing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Enhanced health check endpoint with comprehensive monitoring"""
    try:
        # Use enhanced processor health check if available
        if enhanced_processor is not None:
            health_result = await enhanced_processor.health_check()

            # Add scheduler status
            health_result["scheduler_running"] = scheduler.running

            return health_result
        else:
            # Fallback to basic health check
            db_healthy = await db_manager.health_check()
            queue_size = await db_manager.get_queue_size()
            last_processed = await db_manager.get_last_processed_timestamp()

            return {
                "status": "healthy",
                "version": "1.0.0",
                "database_healthy": db_healthy,
                "queue_size": queue_size,
                "last_processed": last_processed,
                "scheduler_running": scheduler.running,
                "enhanced_features": False
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
    """Get enhanced processing statistics"""
    try:
        # Use enhanced processor stats if available
        if enhanced_processor is not None:
            comprehensive_stats = await enhanced_processor.get_comprehensive_stats()
            return comprehensive_stats
        else:
            # Fallback to basic stats
            stats = await db_manager.get_processing_stats()
            return {
                **stats,
                "enhanced_features": False
            }
    except Exception as e:
        logger.error(f"❌ Stats retrieval failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health/enhanced")
async def enhanced_health_check():
    """Enhanced health check with comprehensive monitoring"""
    try:
        if enhanced_processor is not None:
            # Use enhanced processor health check
            health_result = await enhanced_processor.health_check()

            # Add queue health metrics
            queue_stats = await enhanced_processor.get_queue_health()
            health_result["queue_health"] = queue_stats

            # Add intelligent monitoring status
            if intelligent_monitor is not None:
                monitor_health = await intelligent_monitor.health_check_with_auto_fix()
                health_result["intelligent_monitoring"] = monitor_health

            return health_result
        else:
            return {
                "status": "degraded",
                "reason": "Enhanced processor not available",
                "enhanced_features": False,
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        logger.error(f"❌ Enhanced health check failed: {e}")
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "error": str(e),
                "enhanced_features": False
            }
        )

@app.get("/health/stuck-items")
async def stuck_items_health_check():
    """Stuck items monitoring and prevention health check"""
    try:
        if stuck_items_monitor is not None:
            health_report = await stuck_items_monitor.generate_health_report()
            return health_report
        else:
            return {
                "status": "disabled",
                "reason": "Stuck items monitor not available",
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        logger.error(f"❌ Stuck items health check failed: {e}")
        return JSONResponse(
            status_code=503,
            content={
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
        )

@app.post("/process-backlog")
async def manual_backlog_processing(background_tasks: BackgroundTasks, limit: int = 10):
    """Manually trigger backlog processing (for testing and manual operation)"""
    try:
        if enhanced_processor is None:
            raise HTTPException(status_code=503, detail="Enhanced processor not available")

        # Process in background to avoid blocking
        background_tasks.add_task(
            enhanced_processor.process_backlog_enhanced,
            limit=min(limit, 100)  # Cap at 100 for safety
        )

        return {
            "status": "triggered",
            "message": f"Backlog processing triggered with limit {limit}",
            "estimated_processing_time_minutes": (limit / 20)  # Rough estimate
        }

    except Exception as e:
        logger.error(f"❌ Manual backlog processing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/recover-stuck-documents")
async def manual_document_recovery(background_tasks: BackgroundTasks, limit: int = 100):
    """Manually trigger stuck document recovery"""
    try:
        # Import document recovery
        from document_recovery import DocumentRecovery

        # Run recovery in background to avoid blocking
        async def run_recovery():
            recovery = DocumentRecovery(db_manager)
            await recovery.full_recovery(max_documents=min(limit, 1000))

        background_tasks.add_task(run_recovery)

        return {
            "status": "triggered",
            "message": f"Document recovery triggered with limit {limit}",
            "estimated_processing_time_minutes": (limit / 10),  # Rough estimate
            "recovery_type": "stuck_documents"
        }

    except Exception as e:
        logger.error(f"❌ Manual document recovery failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

async def process_single_item_enhanced(content_id: str):
    """Process a single content item using enhanced processor with bulletproof reliability"""
    try:
        logger.info(f"🔄 Processing {content_id} with enhanced reliability")

        # Use enhanced processor with comprehensive error handling
        if enhanced_processor is None:
            logger.error("❌ Enhanced processor not initialized")
            return

        result = await enhanced_processor._process_single_item_with_retry(content_id)

        if result['status'] == 'success':
            logger.info(f"✅ Successfully processed {content_id}: {result['message']}")
        elif result['status'] == 'retry':
            logger.warning(f"🔄 Retrying {content_id}: {result['message']}")
        else:
            logger.error(f"❌ Failed to process {content_id}: {result['message']}")

    except Exception as e:
        logger.error(f"❌ Enhanced processing error for {content_id}: {e}")

async def process_single_item(content_id: str):
    """Legacy process function for backward compatibility"""
    await process_single_item_enhanced(content_id)

async def process_backlog_enhanced():
    """Process pending items using enhanced processor with reliability features"""
    try:
        if enhanced_processor is None:
            logger.warning("⚠️ Enhanced processor not available, skipping backlog processing")
            return

        logger.info("📋 Starting enhanced backlog processing...")

        # Use enhanced backlog processing with intelligent queue management
        result = await enhanced_processor.process_backlog_enhanced(limit=50)

        logger.info(f"📋 Enhanced backlog processing complete: {result}")

    except Exception as e:
        logger.error(f"❌ Enhanced backlog processing failed: {e}")

def main():
    """Main entry point"""
    # Load environment variables
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    workers = int(os.getenv('WORKERS', 1))

    logger.info(f"🎯 Starting Atlas on {host}:{port}")

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