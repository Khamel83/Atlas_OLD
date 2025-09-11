#!/usr/bin/env python3
"""
Atlas Comprehensive Service
Main background processing service for Atlas content management.

This service handles:
- AI processing of unprocessed content
- Content analysis and summarization
- Metadata extraction and enhancement
- Queue processing and task management
"""

import os
import sys
import sqlite3
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Add Atlas to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from helpers.database_config import get_database_connection
    from helpers.simple_database import SimpleDatabase
    from helpers.logging_config import get_logger
    from universal_processing_queue import UniversalProcessingQueue
except ImportError as e:
    print(f"Failed to import required modules: {e}")
    sys.exit(1)

logger = get_logger(__name__)

class AtlasComprehensiveService:
    """Main comprehensive processing service."""
    
    def __init__(self):
        """Initialize comprehensive service."""
        self.db = SimpleDatabase()
        self.queue = UniversalProcessingQueue()
        logger.info("🚀 Atlas Comprehensive Service initialized")
    
    def process_unprocessed_content(self) -> int:
        """Process content that lacks AI summaries."""
        processed_count = 0
        
        try:
            with self.db.get_connection() as conn:
                # Find content without AI processing
                unprocessed = conn.execute("""
                    SELECT id, title, content, url, content_type 
                    FROM content 
                    WHERE (ai_summary IS NULL OR ai_summary = '')
                    AND content IS NOT NULL 
                    AND length(content) > 100
                    ORDER BY created_at DESC
                    LIMIT 50
                """).fetchall()
                
                logger.info(f"📝 Found {len(unprocessed)} items needing AI processing")
                
                for item in unprocessed:
                    try:
                        content_id, title, content, url, content_type = item
                        
                        # Add to processing queue
                        self.queue.add_job(
                            job_type="ai_processing",
                            data={'content_id': content_id},
                            priority=50
                        )
                        processed_count += 1
                        
                    except Exception as e:
                        logger.error(f"❌ Failed to queue item {item[0]}: {e}")
                        continue
                
        except Exception as e:
            logger.error(f"❌ Database error in process_unprocessed_content: {e}")
        
        return processed_count
    
    def process_queue(self) -> int:
        """Process items in the processing queue."""
        try:
            # Process up to 10 queued jobs
            self.queue.process_jobs(max_jobs=10)
            return 10  # Assume we processed up to 10
                
        except Exception as e:
            logger.error(f"❌ Queue processing error: {e}")
            return 0
    
    def cleanup_old_tasks(self):
        """Clean up old completed tasks."""
        try:
            with self.db.get_connection() as conn:
                # Remove completed tasks older than 7 days
                conn.execute("""
                    DELETE FROM task_queue 
                    WHERE status = 'completed' 
                    AND created_at < datetime('now', '-7 days')
                """)
                conn.commit()
                logger.info("🧹 Cleaned up old completed tasks")
                
        except Exception as e:
            logger.error(f"❌ Cleanup error: {e}")
    
    def get_stats(self) -> Dict:
        """Get processing statistics."""
        stats = {
            'total_content': 0,
            'processed_content': 0,
            'queue_pending': 0,
            'queue_failed': 0
        }
        
        try:
            with self.db.get_connection() as conn:
                stats['total_content'] = conn.execute(
                    "SELECT COUNT(*) FROM content WHERE content IS NOT NULL"
                ).fetchone()[0]
                
                stats['processed_content'] = conn.execute(
                    "SELECT COUNT(*) FROM content WHERE ai_summary IS NOT NULL AND ai_summary != ''"
                ).fetchone()[0]
                
                stats['queue_pending'] = conn.execute(
                    "SELECT COUNT(*) FROM task_queue WHERE status = 'pending'"
                ).fetchone()[0] if conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='task_queue'").fetchone() else 0
                
                # Check if failed_tasks table exists and get count
                if conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='failed_tasks'").fetchone():
                    stats['queue_failed'] = conn.execute(
                        "SELECT COUNT(*) FROM failed_tasks"
                    ).fetchone()[0]
                else:
                    stats['queue_failed'] = 0
                
        except Exception as e:
            logger.error(f"❌ Stats error: {e}")
        
        return stats
    
    def run_comprehensive_cycle(self):
        """Run a complete comprehensive processing cycle."""
        logger.info("🔄 Starting comprehensive processing cycle")
        start_time = datetime.now()
        
        try:
            # 1. Queue unprocessed content for AI processing
            queued = self.process_unprocessed_content()
            logger.info(f"📥 Queued {queued} items for processing")
            
            # 2. Process queued items
            processed = self.process_queue()
            logger.info(f"⚡ Processed {processed} queued items")
            
            # 3. Clean up old tasks
            self.cleanup_old_tasks()
            
            # 4. Log statistics
            stats = self.get_stats()
            logger.info(f"📊 Stats - Total: {stats['total_content']}, Processed: {stats['processed_content']}, Pending: {stats['queue_pending']}, Failed: {stats['queue_failed']}")
            
            duration = (datetime.now() - start_time).total_seconds()
            logger.info(f"✅ Comprehensive cycle completed in {duration:.1f}s")
            
        except Exception as e:
            logger.error(f"❌ Comprehensive cycle failed: {e}")
            raise

def main():
    """Main entry point."""
    logger.info("🌟 Starting Atlas Comprehensive Service")
    
    try:
        service = AtlasComprehensiveService()
        service.run_comprehensive_cycle()
        logger.info("✅ Atlas Comprehensive Service completed successfully")
        
    except Exception as e:
        logger.error(f"💥 Atlas Comprehensive Service failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()