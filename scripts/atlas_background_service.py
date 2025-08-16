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
        self.last_podcast_check = datetime.now() - timedelta(hours=5)  # Force initial run
        self.last_article_retry = datetime.now() - timedelta(hours=13)  # Force initial run
        self.failed_tasks = []  # Track failed tasks for persistent retry
        self.consecutive_failures = 0  # Track consecutive failures for adaptive behavior
        
    def run_command(self, cmd, description, timeout=3600, retries=5):
        """Run a command with intelligent retry and rate limiting"""
        logger.info(f"🔄 Starting: {description}")
        
        for attempt in range(retries):
            try:
                os.chdir(self.base_dir)
                
                # Add random delay to avoid rate limiting (1-5 seconds)
                if attempt > 0:
                    delay = min(60 * (2 ** attempt), 300) + (time.time() % 10)  # Exponential backoff with jitter
                    logger.info(f"⏳ Waiting {delay:.1f}s before retry (exponential backoff)...")
                    time.sleep(delay)
                
                result = subprocess.run(
                    f"bash -c 'source atlas_venv/bin/activate && {cmd}'",
                    shell=True, 
                    capture_output=True, 
                    text=True, 
                    timeout=timeout
                )
                
                if result.returncode == 0:
                    logger.info(f"✅ Completed: {description}")
                    if result.stdout.strip():
                        # Show more output but keep it manageable
                        output = result.stdout[:1000] + "..." if len(result.stdout) > 1000 else result.stdout
                        logger.info(f"Output: {output}")
                    
                    # Remove from failed tasks if it was there
                    self.failed_tasks = [task for task in self.failed_tasks if task['description'] != description]
                    self.consecutive_failures = 0  # Reset on success
                    return True
                else:
                    # Check for specific error patterns
                    error_text = result.stderr.lower()
                    if any(pattern in error_text for pattern in ['rate limit', '429', 'too many requests']):
                        logger.warning(f"🚦 Rate limited on {description} (attempt {attempt + 1}/{retries})")
                        continue  # Will trigger exponential backoff
                    elif any(pattern in error_text for pattern in ['network', 'connection', 'timeout']):
                        logger.warning(f"🌐 Network issue on {description} (attempt {attempt + 1}/{retries})")
                        continue
                    else:
                        logger.error(f"❌ Failed: {description} (attempt {attempt + 1}/{retries})")
                        logger.error(f"Error: {result.stderr[:500]}...")
                    
            except subprocess.TimeoutExpired:
                logger.warning(f"⏰ Timeout: {description} (attempt {attempt + 1}/{retries}) - continuing to retry")
            except Exception as e:
                logger.error(f"💥 Exception in {description}: {e} (attempt {attempt + 1}/{retries})")
        
        # Add to failed tasks for persistent retry
        failed_task = {
            'description': description,
            'cmd': cmd,
            'last_attempt': datetime.now(),
            'failure_count': getattr(next((t for t in self.failed_tasks if t['description'] == description), {}), 'failure_count', 0) + 1
        }
        
        # Update or add failed task
        self.failed_tasks = [t for t in self.failed_tasks if t['description'] != description]
        self.failed_tasks.append(failed_task)
        self.consecutive_failures += 1
        
        logger.error(f"❌ All {retries} attempts failed for: {description} - added to persistent retry queue (failure #{failed_task['failure_count']})")
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

    def article_processing(self):
        """Process new articles from inputs/articles.txt"""
        logger.info("📄 Running article processing...")
        
        # Check if articles.txt has content
        articles_file = self.base_dir / "inputs" / "articles.txt"
        if articles_file.exists() and articles_file.stat().st_size > 0:
            self.run_command(
                "python run.py --articles",
                "New article processing",
                timeout=3600  # 1 hour
            )
    
    def file_processing(self):
        """Process any files in inputs directory"""
        logger.info("📁 Running comprehensive file processing...")
        
        # Check for various input files
        inputs_dir = self.base_dir / "inputs"
        if inputs_dir.exists():
            # Check for YouTube videos
            youtube_file = inputs_dir / "youtube.txt"
            if youtube_file.exists() and youtube_file.stat().st_size > 0:
                self.run_command(
                    "python run.py --youtube",
                    "YouTube video processing",
                    timeout=3600
                )
            
            # Check for Instapaper exports
            for csv_file in inputs_dir.glob("*.csv"):
                if "instapaper" in csv_file.name.lower():
                    self.run_command(
                        f"python run.py --instapaper-csv {csv_file}",
                        f"Instapaper CSV processing: {csv_file.name}",
                        timeout=1800
                    )
            
            # Process any other URL files
            for txt_file in inputs_dir.glob("*.txt"):
                if (txt_file.name not in ["articles.txt", "youtube.txt"] and 
                    txt_file.stat().st_size > 0):
                    self.run_command(
                        f"python run.py --urls {txt_file}",
                        f"URL file processing: {txt_file.name}",
                        timeout=1800
                    )
    
    def comprehensive_processing(self):
        """Run comprehensive Atlas processing"""
        logger.info("🌍 Running comprehensive Atlas processing...")
        
        # Process all types if there's any content
        self.run_command(
            "python run.py --all",
            "Comprehensive Atlas processing",
            timeout=7200  # 2 hours
        )
    
    def document_processing(self):
        """Process any documents or special files"""
        logger.info("📄 Checking for document processing...")
        
        # Check if there are processing scripts to run
        process_scripts = [
            "process_podcasts.py",
            "process_priority_podcasts.py"
        ]
        
        for script in process_scripts:
            script_path = self.base_dir / script
            if script_path.exists():
                self.run_command(
                    f"python {script}",
                    f"Running {script}",
                    timeout=1800
                )
    
    def article_retry_maintenance(self):
        """Retry failed articles with enhanced strategies"""
        logger.info("🔄 Running article retry maintenance...")
        
        # Check if we have retry_failed_articles.py
        retry_script = self.base_dir / "retry_failed_articles.py"
        if retry_script.exists():
            self.run_command(
                "python retry_failed_articles.py --limit 50",
                "Article retry processing", 
                timeout=1800  # 30 minutes  
            )
    
    def skyvern_recovery(self):
        """Run Skyvern-enhanced recovery on failed articles"""
        logger.info("🚀 Running Skyvern recovery...")
        
        self.run_command(
            "python retry_failed_articles.py --use-skyvern --limit 25",
            "Skyvern enhanced recovery",
            timeout=2400  # 40 minutes
        )

    def retry_failed_tasks(self):
        """Retry previously failed tasks with exponential backoff"""
        if not self.failed_tasks:
            return
            
        logger.info(f"🔄 Retrying {len(self.failed_tasks)} failed tasks...")
        
        # Sort by last attempt time (oldest first)
        self.failed_tasks.sort(key=lambda x: x['last_attempt'])
        
        tasks_to_retry = []
        for task in self.failed_tasks:
            # Progressive backoff: wait longer for tasks that have failed more
            wait_minutes = min(60 * (2 ** (task['failure_count'] - 1)), 720)  # Max 12 hours
            time_since_attempt = datetime.now() - task['last_attempt']
            
            if time_since_attempt > timedelta(minutes=wait_minutes):
                tasks_to_retry.append(task)
        
        for task in tasks_to_retry[:3]:  # Limit to 3 retries per cycle
            logger.info(f"🔄 Retrying failed task: {task['description']} (failure #{task['failure_count']})")
            success = self.run_command(task['cmd'], task['description'], timeout=1800, retries=2)
            if success:
                logger.info(f"✅ Successfully recovered: {task['description']}")

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
            
        # Report on persistent failures
        if self.failed_tasks:
            logger.info(f"⚠️  {len(self.failed_tasks)} tasks in retry queue")
            recent_failures = [t for t in self.failed_tasks if (datetime.now() - t['last_attempt']) < timedelta(hours=24)]
            if recent_failures:
                logger.info(f"🔄 {len(recent_failures)} recent failures (last 24h)")
        
        if self.consecutive_failures > 5:
            logger.warning(f"🚨 {self.consecutive_failures} consecutive failures - system may need attention")

    def run_cycle(self):
        """Run one maintenance cycle"""
        logger.info("🚀 Starting Atlas comprehensive ingestion cycle...")
        
        # Run podcast maintenance every 4 hours
        if datetime.now() - self.last_podcast_check > timedelta(hours=4):
            self.podcast_maintenance()
            self.last_podcast_check = datetime.now()
        
        # Process new articles every cycle (30 minutes)
        self.article_processing()
        
        # Process new files every cycle
        self.file_processing()
        
        # Run document processing every cycle
        self.document_processing()
        
        # Comprehensive processing every 2 hours
        if not hasattr(self, 'last_comprehensive_run'):
            self.last_comprehensive_run = datetime.now() - timedelta(hours=3)
        if datetime.now() - self.last_comprehensive_run > timedelta(hours=2):
            self.comprehensive_processing()
            self.last_comprehensive_run = datetime.now()
        
        # Article retry maintenance every 8 hours
        if datetime.now() - self.last_article_retry > timedelta(hours=8):
            self.article_retry_maintenance()
            self.last_article_retry = datetime.now()
        
        # Skyvern recovery every 6 hours
        if not hasattr(self, 'last_skyvern_run'):
            self.last_skyvern_run = datetime.now() - timedelta(hours=7)
        if datetime.now() - self.last_skyvern_run > timedelta(hours=6):
            self.skyvern_recovery()
            self.last_skyvern_run = datetime.now()
        
        # Retry failed tasks every cycle
        self.retry_failed_tasks()
            
        # System status every cycle
        self.system_status_check()
        
        logger.info("✅ Comprehensive ingestion cycle complete")

    def run(self):
        """Main service loop"""
        logger.info("🌟 Atlas Background Service starting...")
        
        try:
            # Run initial cycle immediately
            self.run_cycle()
            
            while self.running:
                # Sleep for 30 minutes between cycles
                logger.info("😴 Sleeping for 30 minutes until next cycle...")
                time.sleep(1800)
                
                self.run_cycle()
                
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