#!/usr/bin/env python3
"""
Bulk podcast processing script for Atlas.
Runs discovery and transcript fetching for all podcasts in the background.
"""

import os
import sys
import subprocess
import time
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/ubuntu/dev/atlas/logs/bulk_podcast_processing.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_command(cmd, description):
    """Run a command and log the results"""
    logger.info(f"Starting: {description}")
    logger.info(f"Command: {cmd}")
    
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=3600  # 1 hour timeout
        )
        
        if result.returncode == 0:
            logger.info(f"✅ Completed: {description}")
            if result.stdout:
                logger.info(f"Output: {result.stdout}")
        else:
            logger.error(f"❌ Failed: {description}")
            logger.error(f"Error: {result.stderr}")
            
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        logger.error(f"⏰ Timeout: {description}")
        return False
    except Exception as e:
        logger.error(f"💥 Exception in {description}: {e}")
        return False

def main():
    """Main bulk processing workflow"""
    logger.info("🚀 Starting bulk podcast processing...")
    
    # Change to Atlas directory
    os.chdir('/home/ubuntu/dev/atlas')
    
    # Activate virtual environment and set PYTHONPATH
    base_cmd = "source atlas_venv/bin/activate && PYTHONPATH=. "
    
    # Step 1: Run bulk discovery on all podcasts
    discovery_cmd = base_cmd + "python -m modules.podcasts.cli discover --all"
    if not run_command(discovery_cmd, "Bulk discovery for all 190 podcasts"):
        logger.error("Discovery failed, stopping")
        return
    
    # Step 2: Fetch transcripts for all discovered episodes
    fetch_cmd = base_cmd + "python -m modules.podcasts.cli fetch-transcripts --all"
    if not run_command(fetch_cmd, "Bulk transcript fetching"):
        logger.error("Transcript fetching failed")
        return
    
    # Step 3: Check final stats
    stats_cmd = base_cmd + "python -m modules.podcasts.cli doctor"
    run_command(stats_cmd, "Final system status check")
    
    logger.info("🎉 Bulk podcast processing complete!")

if __name__ == "__main__":
    main()