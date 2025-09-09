#!/usr/bin/env python3
"""
Unified Service Manager for Atlas
Coordinates all background processing through the Universal Processing Queue
"""

import sys
import os
import time
import threading
import signal
import logging
from pathlib import Path
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from universal_processing_queue import UniversalProcessingQueue
from scripts.atlas_scheduler import AtlasScheduler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/unified_service.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class UnifiedServiceManager:
    """Manages all Atlas background services through unified coordination"""
    
    def __init__(self):
        self.running = False
        self.queue_worker = None
        self.scheduler = None
        self.queue_thread = None
        self.scheduler_thread = None
        
        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        logger.info(f"🛑 Received signal {signum}, shutting down...")
        self.stop()
    
    def start_queue_worker(self):
        """Start Universal Processing Queue worker in separate thread"""
        logger.info("🔄 Starting Universal Processing Queue worker...")
        
        self.queue_worker = UniversalProcessingQueue()
        
        def run_queue_worker():
            try:
                self.queue_worker.process_jobs()  # Run indefinitely
            except Exception as e:
                logger.error(f"❌ Queue worker crashed: {e}")
                self.running = False
        
        self.queue_thread = threading.Thread(target=run_queue_worker, daemon=True)
        self.queue_thread.start()
        logger.info("✅ Queue worker started")
    
    def start_scheduler(self):
        """Start Atlas scheduler in separate thread"""
        logger.info("📅 Starting Atlas scheduler...")
        
        self.scheduler = AtlasScheduler()
        
        def run_scheduler():
            try:
                # Run scheduler loop
                while self.running:
                    try:
                        # Check system health
                        from helpers.resource_monitor import check_system_health
                        if not check_system_health():
                            logger.warning("⚠️ System health check failed, skipping cycle")
                            time.sleep(60)
                            continue
                        
                        # Run scheduled tasks
                        if self.scheduler.should_run_comprehensive():
                            self.scheduler.run_comprehensive_service()
                        
                        if self.scheduler.should_run_transcript_discovery():
                            self.scheduler.run_transcript_discovery()
                        
                        if self.scheduler.should_run_transcript_check():
                            self.scheduler.run_transcript_check()
                        
                        if self.scheduler.should_run_youtube_processing():
                            self.scheduler.run_youtube_processing()
                        
                        # Sleep between checks
                        time.sleep(10)  # Check every 10 seconds
                        
                    except Exception as e:
                        logger.error(f"❌ Scheduler cycle error: {e}")
                        time.sleep(60)  # Wait before retry
                        
            except Exception as e:
                logger.error(f"❌ Scheduler crashed: {e}")
                self.running = False
        
        self.scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        self.scheduler_thread.start()
        logger.info("✅ Scheduler started")
    
    def start(self):
        """Start all services"""
        logger.info("🚀 Starting Atlas Unified Service Manager...")
        
        self.running = True
        
        # Start queue worker first (processes jobs)
        self.start_queue_worker()
        
        # Start scheduler (submits jobs to queue)
        self.start_scheduler()
        
        logger.info("🎉 All services started successfully!")
        
        # Keep main thread alive
        try:
            while self.running:
                # Monitor service health
                if not (self.queue_thread and self.queue_thread.is_alive()):
                    logger.error("❌ Queue worker thread died!")
                    self.running = False
                    break
                
                if not (self.scheduler_thread and self.scheduler_thread.is_alive()):
                    logger.error("❌ Scheduler thread died!")
                    self.running = False
                    break
                
                time.sleep(30)  # Check every 30 seconds
                
        except KeyboardInterrupt:
            logger.info("🛑 Keyboard interrupt received")
            self.stop()
    
    def stop(self):
        """Stop all services gracefully"""
        logger.info("🛑 Stopping all services...")
        
        self.running = False
        
        # Stop queue worker
        if self.queue_worker:
            self.queue_worker.is_running = False
            logger.info("🔄 Queue worker stopped")
        
        # Stop scheduler
        if self.scheduler:
            self.scheduler.cleanup_processes()
            logger.info("📅 Scheduler stopped")
        
        # Wait for threads to finish
        if self.queue_thread and self.queue_thread.is_alive():
            self.queue_thread.join(timeout=5)
        
        if self.scheduler_thread and self.scheduler_thread.is_alive():
            self.scheduler_thread.join(timeout=5)
        
        logger.info("✅ All services stopped")
    
    def status(self):
        """Get service status"""
        status = {
            'running': self.running,
            'queue_worker_alive': self.queue_thread and self.queue_thread.is_alive(),
            'scheduler_alive': self.scheduler_thread and self.scheduler_thread.is_alive(),
            'started_at': datetime.now().isoformat()
        }
        
        if self.queue_worker:
            status['queue_stats'] = self.queue_worker.get_queue_stats()
        
        return status

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Atlas Unified Service Manager')
    parser.add_argument('--status', action='store_true', help='Show service status')
    parser.add_argument('--test', action='store_true', help='Test services and exit')
    
    args = parser.parse_args()
    
    manager = UnifiedServiceManager()
    
    if args.status:
        status = manager.status()
        print("📊 Service Status:")
        for key, value in status.items():
            print(f"  {key}: {value}")
        return
    
    if args.test:
        logger.info("🧪 Testing service components...")
        
        # Test queue worker
        queue = UniversalProcessingQueue()
        stats = queue.get_queue_stats()
        logger.info(f"✅ Queue worker test passed: {stats}")
        
        # Test scheduler
        scheduler = AtlasScheduler()
        logger.info("✅ Scheduler test passed")
        
        logger.info("🎉 All service tests passed!")
        return
    
    # Start services
    try:
        manager.start()
    except Exception as e:
        logger.error(f"❌ Service manager crashed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()