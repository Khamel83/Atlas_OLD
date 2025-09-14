#!/usr/bin/env python3
"""
URL Processing Worker - Processes URLs from unified ingestion queue
"""

import sqlite3
import json
import time
import logging
import sys
from pathlib import Path
from datetime import datetime

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class URLWorker:
    """Worker to process URL jobs from the unified queue"""
    
    def __init__(self, db_path="atlas.db"):
        self.db_path = db_path
        self.worker_id = f"url_worker_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.running = False
    
    def get_next_job(self):
        """Get next URL processing job from queue"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                UPDATE worker_jobs 
                SET status = 'running', assigned_worker = ?, assigned_at = ?
                WHERE id = (
                    SELECT id FROM worker_jobs 
                    WHERE status = 'pending' AND type = 'url_processing'
                    ORDER BY priority DESC, created_at ASC 
                    LIMIT 1
                )
                RETURNING id, type, data, priority, status, created_at
            """, (self.worker_id, datetime.now().isoformat()))
            
            row = cursor.fetchone()
            if row:
                return {
                    'id': row[0],
                    'type': row[1], 
                    'data': json.loads(row[2]),
                    'priority': row[3],
                    'status': row[4],
                    'created_at': row[5]
                }
            return None
    
    def process_url_job(self, job):
        """Process a single URL job"""
        try:
            url = job['data']['url']
            source = job['data'].get('source', 'unknown')
            
            logger.info(f"Processing URL: {url} (source: {source})")
            
            # Use FailsafeIngestor for reliable URL processing
            from helpers.failsafe_ingestor import FailsafeIngestor
            
            # Process the URL directly
            ingestor = FailsafeIngestor()
            success = ingestor.process_content(url, {'source': source, 'job_id': job['id']})
            
            # Mark job as completed based on success
            if success:
                self.complete_job(job['id'], f"Processed successfully")
                logger.info(f"✅ Completed: {url}")
                return True
            else:
                self.fail_job(job['id'], f"Processing failed")
                logger.error(f"❌ Failed: {url}")
                return False
            
        except Exception as e:
            error_msg = f"Failed to process URL: {str(e)}"
            logger.error(f"❌ {error_msg}")
            self.fail_job(job['id'], error_msg)
            return False
    
    def complete_job(self, job_id, result):
        """Mark job as completed"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                UPDATE worker_jobs 
                SET status = 'completed', completed_at = ?, result = ?
                WHERE id = ?
            """, (datetime.now().isoformat(), result, job_id))
            conn.commit()
    
    def fail_job(self, job_id, error):
        """Mark job as failed"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                UPDATE worker_jobs 
                SET status = 'failed', completed_at = ?, result = ?, retry_count = retry_count + 1
                WHERE id = ?
            """, (datetime.now().isoformat(), error, job_id))
            conn.commit()
    
    def run(self):
        """Main worker loop"""
        logger.info(f"🚀 Starting URL worker {self.worker_id}")
        self.running = True
        
        processed_count = 0
        
        while self.running:
            try:
                job = self.get_next_job()
                if job:
                    success = self.process_url_job(job)
                    if success:
                        processed_count += 1
                        logger.info(f"📊 Processed {processed_count} URLs so far")
                else:
                    # No jobs available, wait a bit
                    time.sleep(5)
                    
            except KeyboardInterrupt:
                logger.info("👋 Worker stopped by user")
                break
            except Exception as e:
                logger.error(f"Worker error: {e}")
                time.sleep(10)  # Wait before retrying
        
        logger.info(f"✅ Worker finished. Processed {processed_count} URLs total")

def main():
    worker = URLWorker()
    try:
        worker.run()
    except KeyboardInterrupt:
        logger.info("Worker stopped")

if __name__ == "__main__":
    main()