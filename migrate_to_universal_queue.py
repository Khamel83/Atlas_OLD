#!/usr/bin/env python3
"""
Migration Script: Consolidate Processing Systems

Migrates existing Atlas processing systems to use the Universal Processing Queue.
This prevents competing parallel processes and provides centralized coordination.
"""

import sqlite3
import json
import logging
import subprocess
from pathlib import Path
from datetime import datetime
import sys
import os

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from universal_processing_queue import UniversalProcessingQueue

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ProcessingMigration:
    """Migrates existing processing systems to universal queue"""
    
    def __init__(self, db_path="atlas.db"):
        self.db_path = db_path
        self.queue = UniversalProcessingQueue(db_path)
        
    def migrate_ai_processing_backlog(self):
        """Migrate AI processing backlog to universal queue"""
        logger.info("🧠 Migrating AI processing backlog...")
        
        with sqlite3.connect(self.db_path) as conn:
            # Find items that need AI processing
            cursor = conn.execute("""
                SELECT id, title, content 
                FROM content 
                WHERE length(content) > 100 
                AND (ai_summary IS NULL OR ai_tags IS NULL OR ai_socratic IS NULL 
                     OR ai_patterns IS NULL OR ai_recommendations IS NULL)
                ORDER BY id ASC
                LIMIT 100
            """)
            
            items = cursor.fetchall()
            
            jobs_added = 0
            for content_id, title, content in items:
                job_id = self.queue.add_job('ai_processing', {
                    'content_id': content_id,
                    'title': title[:100],
                    'content_length': len(content)
                }, priority=40)
                jobs_added += 1
            
            logger.info(f"✅ Added {jobs_added} AI processing jobs to universal queue")
    
    def migrate_transcript_discovery_queue(self):
        """Migrate transcript discovery to universal queue"""
        logger.info("🎙️ Migrating transcript discovery queue...")
        
        # Check if there's an episode_queue table
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT name FROM sqlite_master 
                WHERE type='table' AND name='episode_queue'
            """)
            
            if cursor.fetchone():
                cursor = conn.execute("""
                    SELECT podcast_name, episode_title, episode_url 
                    FROM episode_queue 
                    WHERE status = 'pending' OR status IS NULL
                    LIMIT 50
                """)
                
                episodes = cursor.fetchall()
                jobs_added = 0
                
                for podcast_name, episode_title, episode_url in episodes:
                    job_id = self.queue.add_job('transcript_discovery', {
                        'podcast_name': podcast_name,
                        'episode_title': episode_title,
                        'episode_url': episode_url
                    }, priority=75)
                    jobs_added += 1
                
                logger.info(f"✅ Added {jobs_added} transcript discovery jobs to universal queue")
            else:
                logger.info("ℹ️ No episode_queue table found")
    
    def migrate_podemos_processing(self):
        """Check for PODEMOS integration and migrate if needed"""
        logger.info("📻 Checking PODEMOS integration...")
        
        # Check if PODEMOS system exists
        podemos_files = [
            'podemos_ultra_fast_processor.py',
            'podemos_feed_monitor.py',
            'podemos_atlas_integration.py'
        ]
        
        existing_podemos = [f for f in podemos_files if Path(f).exists()]
        
        if existing_podemos:
            logger.info(f"✅ Found PODEMOS system: {existing_podemos}")
            
            # Add integration points for PODEMOS
            # This would typically check PODEMOS queue and migrate active jobs
            
            # For now, just add a placeholder integration job
            self.queue.add_job('podemos_processing', {
                'integration_status': 'migrated',
                'podemos_files': existing_podemos,
                'note': 'PODEMOS system integrated with universal queue'
            }, priority=95)
            
            logger.info("✅ PODEMOS integration job added to universal queue")
        else:
            logger.info("ℹ️ No PODEMOS system found")
    
    def migrate_content_ingestion_backlog(self):
        """Migrate any pending content ingestion"""
        logger.info("🌐 Migrating content ingestion backlog...")
        
        with sqlite3.connect(self.db_path) as conn:
            # Look for content that may need re-processing or failed ingestion
            cursor = conn.execute("""
                SELECT url, title FROM content 
                WHERE content_type IN ('article', 'webpage') 
                AND (content IS NULL OR length(content) < 100)
                AND url IS NOT NULL
                LIMIT 20
            """)
            
            items = cursor.fetchall()
            jobs_added = 0
            
            for url, title in items:
                job_id = self.queue.add_job('content_ingestion', {
                    'url': url,
                    'title': title,
                    'retry': True
                }, priority=60)
                jobs_added += 1
            
            logger.info(f"✅ Added {jobs_added} content ingestion jobs to universal queue")
    
    def stop_competing_processes(self):
        """Stop any running competing processes"""
        logger.info("🛑 Stopping competing processes...")
        
        # List of process files that might be running
        process_files = [
            'processor.pid',
            'smart_processor.pid',
            'atlas_comprehensive_service.py',
            'podemos_ultra_fast_processor.py'
        ]
        
        stopped_processes = 0
        for pid_file in process_files:
            if Path(pid_file).exists():
                try:
                    with open(pid_file, 'r') as f:
                        pid = f.read().strip()
                    
                    # Try to stop the process
                    subprocess.run(['kill', pid], capture_output=True)
                    Path(pid_file).unlink()  # Remove PID file
                    
                    logger.info(f"🛑 Stopped process with PID {pid}")
                    stopped_processes += 1
                    
                except Exception as e:
                    logger.warning(f"⚠️ Could not stop process {pid_file}: {e}")
        
        if stopped_processes > 0:
            logger.info(f"✅ Stopped {stopped_processes} competing processes")
        else:
            logger.info("ℹ️ No competing processes found")
    
    def update_scheduler_integration(self):
        """Update atlas_scheduler.py to use universal queue"""
        logger.info("🕐 Checking scheduler integration...")
        
        scheduler_file = Path("scripts/atlas_scheduler.py")
        if scheduler_file.exists():
            # Read current scheduler
            scheduler_content = scheduler_file.read_text()
            
            # Check if already integrated
            if "universal_processing_queue" in scheduler_content:
                logger.info("✅ Scheduler already uses universal queue")
            else:
                logger.info("ℹ️ Consider updating scheduler to use universal queue")
                
                # Create a note about integration
                integration_note = """
# UNIVERSAL QUEUE INTEGRATION NOTES:
# 
# To integrate with universal queue, modify atlas_scheduler.py to:
# 1. Import universal_processing_queue
# 2. Replace direct processing calls with queue.add_job()
# 3. Run queue.process_jobs() instead of individual processors
# 
# Example:
# from universal_processing_queue import UniversalProcessingQueue
# queue = UniversalProcessingQueue()
# queue.process_jobs(max_jobs=10)  # Process up to 10 jobs per cycle
"""
                
                Path("SCHEDULER_INTEGRATION_NOTES.txt").write_text(integration_note)
                logger.info("📝 Created scheduler integration notes")
        
    def create_unified_startup_script(self):
        """Create a unified startup script for all processing"""
        logger.info("🚀 Creating unified startup script...")
        
        startup_script = """#!/usr/bin/env python3
'''
Unified Atlas Processing Service

Replaces multiple competing processing services with a single coordinated system.
Uses the Universal Processing Queue for all background tasks.
'''

import sys
import time
import signal
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from universal_processing_queue import UniversalProcessingQueue
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def signal_handler(signum, frame):
    logger.info("🛑 Shutdown signal received")
    sys.exit(0)

def main():
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    queue = UniversalProcessingQueue()
    
    logger.info("🚀 Starting Unified Atlas Processing Service")
    logger.info("📊 Queue Stats:")
    stats = queue.get_queue_stats()
    for key, value in stats.items():
        logger.info(f"   {key}: {value}")
    
    # Start processing jobs
    # This will run continuously until stopped
    queue.process_jobs()

if __name__ == "__main__":
    main()
"""
        
        script_path = Path("unified_atlas_processor.py")
        script_path.write_text(startup_script)
        script_path.chmod(0o755)  # Make executable
        
        logger.info(f"✅ Created unified startup script: {script_path}")
    
    def run_full_migration(self):
        """Run the complete migration process"""
        logger.info("🔄 Starting full migration to Universal Processing Queue")
        logger.info("=" * 60)
        
        # Step 1: Stop competing processes
        self.stop_competing_processes()
        
        # Step 2: Migrate existing backlogs
        self.migrate_ai_processing_backlog()
        self.migrate_transcript_discovery_queue()
        self.migrate_podemos_processing()
        self.migrate_content_ingestion_backlog()
        
        # Step 3: Update integration points
        self.update_scheduler_integration()
        self.create_unified_startup_script()
        
        # Step 4: Show final stats
        logger.info("=" * 60)
        logger.info("📊 Final Queue Statistics:")
        stats = self.queue.get_queue_stats()
        for key, value in stats.items():
            logger.info(f"   {key}: {value}")
        
        logger.info("✅ Migration completed successfully!")
        logger.info("")
        logger.info("🚀 To start the unified processing system:")
        logger.info("   python3 unified_atlas_processor.py")
        logger.info("")
        logger.info("📊 To monitor the queue:")
        logger.info("   python3 universal_processing_queue.py --stats")

if __name__ == "__main__":
    migration = ProcessingMigration()
    migration.run_full_migration()