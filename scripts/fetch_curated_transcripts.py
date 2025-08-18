#!/usr/bin/env python3
"""
Fetch transcripts for curated podcasts only.
Respects user preferences and priorities.
"""

import os
import subprocess
import logging
import time

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/ubuntu/dev/atlas/logs/curated_transcript_fetch.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Fetch transcripts for curated podcasts"""
    logger.info("🎯 Starting curated transcript fetching...")
    
    os.chdir('/home/ubuntu/dev/atlas')
    
    # Fetch transcripts from the 16 curated podcasts only
    cmd = "source atlas_venv/bin/activate && PYTHONPATH=. python -m modules.podcasts.cli fetch-transcripts --all"
    
    try:
        logger.info("🔄 Fetching transcripts from curated podcasts...")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=1800)  # 30 min timeout
        
        if result.returncode == 0:
            logger.info("✅ Transcript fetching completed successfully")
            logger.info(f"Output: {result.stdout}")
        else:
            logger.error(f"❌ Transcript fetching failed")
            logger.error(f"Error: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        logger.error("⏰ Transcript fetching timed out after 30 minutes")
    except Exception as e:
        logger.error(f"💥 Exception during transcript fetching: {e}")
    
    # Check final stats
    logger.info("📊 Checking final results...")
    stats_cmd = "source atlas_venv/bin/activate && PYTHONPATH=. python -m modules.podcasts.cli doctor"
    try:
        result = subprocess.run(stats_cmd, shell=True, capture_output=True, text=True, timeout=60)
        logger.info(f"Final stats:\n{result.stdout}")
    except:
        logger.error("Could not get final stats")

if __name__ == "__main__":
    main()