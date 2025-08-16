#!/usr/bin/env python3
"""
Atlas Unified Background Service
Handles all continuous background processing in one organized service.
"""

import os
import sys
import time
import subprocess
import threading
import logging
from datetime import datetime, timedelta
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/ubuntu/dev/atlas/logs/atlas_background_service.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('AtlasBackgroundService')

class AtlasBackgroundService:
    def __init__(self):
        self.base_dir = Path('/home/ubuntu/dev/atlas')
        self.running = True
        self.last_podcast_check = datetime.now()
        self.last_article_retry = datetime.now()
        
    def run_command(self, cmd, description, timeout=3600, retries=3):
        """Run a command with logging and auto-retry"""
        logger.info(f"🔄 Starting: {description}")
        
        for attempt in range(retries):
            try:
                os.chdir(self.base_dir)
                result = subprocess.run(
                    f"source atlas_venv/bin/activate && {cmd}",
                    shell=True, 
                    capture_output=True, 
                    text=True, 
                    timeout=timeout
                )
                
                if result.returncode == 0:
                    logger.info(f"✅ Completed: {description}")
                    if result.stdout.strip():
                        logger.info(f"Output: {result.stdout[:500]}...")
                    return True
                else:
                    logger.error(f"❌ Failed: {description} (attempt {attempt + 1}/{retries})")
                    logger.error(f"Error: {result.stderr[:500]}...")
                    if attempt < retries - 1:
                        logger.info(f"🔄 Retrying in 60 seconds...")
                        time.sleep(60)
                    
            except subprocess.TimeoutExpired:
                logger.error(f"⏰ Timeout: {description} (attempt {attempt + 1}/{retries})")
                if attempt < retries - 1:
                    logger.info(f"🔄 Retrying in 60 seconds...")
                    time.sleep(60)
            except Exception as e:
                logger.error(f"💥 Exception in {description}: {e} (attempt {attempt + 1}/{retries})")
                if attempt < retries - 1:
                    logger.info(f"🔄 Retrying in 60 seconds...")
                    time.sleep(60)
        
        logger.error(f"❌ All {retries} attempts failed for: {description}")
        return False

    def podcast_maintenance(self):
        """Check for new podcast episodes and transcripts"""
        logger.info("🎙️ Running podcast maintenance...")
        
        # Discover new episodes (quick check)
        self.run_command(
            "PYTHONPATH=. python -m modules.podcasts.cli discover --all",
            "Podcast episode discovery",
            timeout=1800  # 30 minutes
        )
        
        # Fetch any new transcripts found
        self.run_command(
            "PYTHONPATH=. python -m modules.podcasts.cli fetch-transcripts --all",
            "Podcast transcript fetching", 
            timeout=1800  # 30 minutes
        )

    def article_retry_maintenance(self):
        """Retry failed articles with enhanced strategies"""
        logger.info("📄 Running article retry maintenance...")
        
        # Check if we have retry_failed_articles.py
        retry_script = self.base_dir / "retry_failed_articles.py"
        if retry_script.exists():
            self.run_command(
                "python retry_failed_articles.py --limit 50",
                "Article retry processing",
                timeout=1800  # 30 minutes  
            )

    def system_status_check(self):
        """Check overall system health"""
        logger.info("🏥 System health check...")
        
        # Check database sizes
        try:
            db_path = self.base_dir / "data" / "podcasts" / "atlas_podcasts.db"
            if db_path.exists():
                size_mb = db_path.stat().st_size / (1024 * 1024)
                logger.info(f"📊 Podcast database: {size_mb:.1f}MB")
        except Exception as e:
            logger.error(f"Error checking database: {e}")

    def run_cycle(self):
        """Run one maintenance cycle"""
        logger.info("🚀 Starting Atlas background maintenance cycle...")
        
        # Podcast maintenance every 4 hours
        if datetime.now() - self.last_podcast_check > timedelta(hours=4):
            self.podcast_maintenance()
            self.last_podcast_check = datetime.now()
        
        # Article retry maintenance every 12 hours
        if datetime.now() - self.last_article_retry > timedelta(hours=12):
            self.article_retry_maintenance()
            self.last_article_retry = datetime.now()
            
        # System status every cycle
        self.system_status_check()
        
        logger.info("✅ Maintenance cycle complete")

    def run(self):
        """Main service loop"""
        logger.info("🌟 Atlas Background Service starting...")
        
        try:
            while self.running:
                self.run_cycle()
                
                # Sleep for 1 hour between cycles
                logger.info("😴 Sleeping for 1 hour until next cycle...")
                time.sleep(3600)
                
        except KeyboardInterrupt:
            logger.info("🛑 Shutdown requested...")
        except Exception as e:
            logger.error(f"💥 Service error: {e}")
        finally:
            logger.info("🏁 Atlas Background Service stopped")

def main():
    service = AtlasBackgroundService()
    service.run()

if __name__ == "__main__":
    main()