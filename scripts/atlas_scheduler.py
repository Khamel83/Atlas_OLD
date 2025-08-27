#!/usr/bin/env python3
"""
Atlas Background Scheduler
Runs the comprehensive processing service on schedule.
"""

import time
import argparse
import logging
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/atlas_scheduler.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AtlasScheduler:
    """Atlas background task scheduler."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.last_comprehensive_run = None
        self.last_transcript_run = None
        self.comprehensive_interval = 2 * 60 * 60  # 2 hours
        self.transcript_interval = 4 * 60 * 60  # 4 hours
        # Use atlas_venv Python, not system Python
        self.python_executable = str(self.project_root / "atlas_venv" / "bin" / "python3")
        
    def should_run_comprehensive(self) -> bool:
        """Check if comprehensive cycle should run."""
        if not self.last_comprehensive_run:
            return True
        return (datetime.now() - self.last_comprehensive_run).seconds >= self.comprehensive_interval
        
    def should_run_transcript_discovery(self) -> bool:
        """Check if enhanced transcript discovery should run."""
        if not self.last_transcript_run:
            return True
        return (datetime.now() - self.last_transcript_run).seconds >= self.transcript_interval
        
    def run_comprehensive_service(self) -> bool:
        """Run the comprehensive processing service."""
        try:
            logger.info("🚀 Starting comprehensive processing cycle...")
            
            result = subprocess.run([
                self.python_executable, str(self.project_root / "atlas_comprehensive_service.py")
            ], cwd=self.project_root, timeout=7200)  # 2 hour timeout
            
            if result.returncode == 0:
                logger.info("✅ Comprehensive processing completed successfully")
                self.last_comprehensive_run = datetime.now()
                return True
            else:
                logger.error(f"❌ Comprehensive processing failed with code {result.returncode}")
                return False
                
        except subprocess.TimeoutExpired:
            logger.error("❌ Comprehensive processing timed out after 2 hours")
            return False
        except Exception as e:
            logger.error(f"❌ Comprehensive processing error: {e}")
            return False
            
    def run_transcript_discovery(self) -> bool:
        """Run enhanced transcript discovery."""
        try:
            logger.info("🎙️ Starting enhanced transcript discovery...")
            
            result = subprocess.run([
                self.python_executable, str(self.project_root / "enhanced_transcript_discovery.py")
            ], cwd=self.project_root, timeout=3600)  # 1 hour timeout
            
            if result.returncode == 0:
                logger.info("✅ Enhanced transcript discovery completed successfully")
                self.last_transcript_run = datetime.now()
                return True
            else:
                logger.error(f"❌ Enhanced transcript discovery failed with code {result.returncode}")
                return False
                
        except subprocess.TimeoutExpired:
            logger.error("❌ Enhanced transcript discovery timed out after 1 hour")
            return False
        except Exception as e:
            logger.error(f"❌ Enhanced transcript discovery error: {e}")
            return False
            
    def run_scheduler(self):
        """Main scheduler loop."""
        logger.info("🕐 Atlas Background Scheduler started")
        logger.info(f"   Comprehensive cycle: every {self.comprehensive_interval//3600} hours")
        logger.info(f"   Transcript discovery: every {self.transcript_interval//3600} hours")
        
        # Run once immediately on startup
        logger.info("🔄 Running initial comprehensive cycle...")
        self.run_comprehensive_service()
        
        while True:
            try:
                # Check if we should run transcript discovery
                if self.should_run_transcript_discovery():
                    self.run_transcript_discovery()
                
                # Check if we should run comprehensive processing
                elif self.should_run_comprehensive():
                    self.run_comprehensive_service()
                
                # Sleep for 10 minutes before checking again
                time.sleep(600)
                
            except KeyboardInterrupt:
                logger.info("🛑 Scheduler stopped by user")
                break
            except Exception as e:
                logger.error(f"❌ Scheduler error: {e}")
                time.sleep(300)  # Wait 5 minutes on error

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Atlas Background Scheduler')
    parser.add_argument('--start', action='store_true', help='Start the scheduler')
    args = parser.parse_args()

    if args.start:
        # Ensure logs directory exists
        Path('logs').mkdir(exist_ok=True)
        
        scheduler = AtlasScheduler()
        scheduler.run_scheduler()
    else:
        print("Usage: atlas_scheduler.py --start")