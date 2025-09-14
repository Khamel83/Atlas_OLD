#!/usr/bin/env python3
"""
Google Search Background Worker

Processes Google Search requests from the queue at a controlled rate
to respect API quotas and rate limits.
"""

import asyncio
import logging
import os
import signal
import sys
import time
from datetime import datetime, timedelta
from typing import Optional

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helpers.google_search_queue import GoogleSearchQueue, QueuePriority, QueueStatus
from helpers.google_search_fallback import GoogleSearchFallback

logger = logging.getLogger(__name__)

class GoogleSearchWorker:
    """Background worker for processing Google Search queue"""
    
    def __init__(self):
        self.queue = GoogleSearchQueue()
        self.fallback = GoogleSearchFallback()
        self.running = False
        self.search_interval = 11  # 11 seconds between searches (8k per day limit)
        self.last_search_time = 0
        
    async def start(self):
        """Start the background worker"""
        if self.running:
            logger.warning("Worker is already running")
            return
            
        self.running = True
        logger.info("🚀 Starting Google Search background worker")
        logger.info(f"⏱️  Search interval: {self.search_interval} seconds")
        logger.info(f"📊 Daily quota: {self.queue.daily_quota} searches")
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        try:
            await self._main_loop()
        except Exception as e:
            logger.error(f"Worker crashed: {e}")
            raise
        finally:
            self.running = False
            logger.info("🛑 Google Search worker stopped")
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.running = False
    
    async def _main_loop(self):
        """Main worker loop"""
        consecutive_idle_cycles = 0
        max_idle_cycles = 60  # Sleep longer after 1 hour of inactivity
        
        while self.running:
            try:
                # Check daily quota
                daily_used = self.queue._get_daily_usage()
                if daily_used >= self.queue.daily_quota:
                    logger.warning(f"Daily quota exhausted: {daily_used}/{self.queue.daily_quota}")
                    await self._sleep_until_quota_reset()
                    continue
                
                # Get next search request
                search = self.queue.get_next_search()
                
                if not search:
                    consecutive_idle_cycles += 1
                    if consecutive_idle_cycles > max_idle_cycles:
                        # Sleep longer when idle for extended periods
                        logger.debug("No searches in queue, extending sleep...")
                        await asyncio.sleep(60)  # 1 minute
                        consecutive_idle_cycles = 0
                    else:
                        await asyncio.sleep(10)  # 10 seconds
                    continue
                
                consecutive_idle_cycles = 0
                
                # Respect rate limiting
                await self._wait_for_rate_limit()
                
                # Process the search
                await self._process_search(search)
                
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                await asyncio.sleep(30)  # Wait 30 seconds before retrying
    
    async def _wait_for_rate_limit(self):
        """Wait to respect rate limiting (1 search per 11 seconds)"""
        current_time = time.time()
        time_since_last = current_time - self.last_search_time
        
        if time_since_last < self.search_interval:
            sleep_time = self.search_interval - time_since_last
            logger.debug(f"Rate limiting: sleeping {sleep_time:.1f}s")
            await asyncio.sleep(sleep_time)
        
        self.last_search_time = time.time()
    
    async def _process_search(self, search):
        """Process a single search request"""
        logger.info(f"🔍 Processing search: '{search.query}' (Priority: {search.priority}, Attempt: {search.attempts + 1})")
        
        try:
            # Use the fallback system to perform the search
            result_url = await self._perform_google_search(search.query)
            
            if result_url:
                self.queue.mark_completed(search.id, result_url)
                logger.info(f"✅ Search successful: {result_url}")
            else:
                # No results found, but not an error
                self.queue.mark_failed(search.id, "No search results found", increment_attempts=True)
                logger.info(f"❌ No results found for: {search.query}")
                
        except Exception as e:
            error_msg = str(e)
            
            # Handle rate limiting
            if "429" in error_msg or "rate limit" in error_msg.lower():
                self.queue.mark_rate_limited(search.id)
                logger.warning(f"⏱️  Rate limited, will retry: {search.query}")
                # Add extra delay for rate limiting
                await asyncio.sleep(60)
            else:
                self.queue.mark_failed(search.id, error_msg, increment_attempts=True)
                logger.error(f"❌ Search failed: {search.query} - {error_msg}")
    
    async def _perform_google_search(self, query: str) -> Optional[str]:
        """Perform the actual Google search using the fallback system"""
        try:
            # Create a high-priority search request
            result = await self.fallback.search(query, priority=1)
            return result
            
        except Exception as e:
            logger.error(f"Google search API error: {e}")
            raise
    
    async def _sleep_until_quota_reset(self):
        """Sleep until daily quota resets (midnight UTC)"""
        now = datetime.utcnow()
        tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        sleep_seconds = (tomorrow - now).total_seconds()
        
        logger.info(f"💤 Sleeping {sleep_seconds/3600:.1f} hours until quota reset")
        
        # Sleep in chunks to allow for graceful shutdown
        while sleep_seconds > 0 and self.running:
            chunk_sleep = min(300, sleep_seconds)  # 5-minute chunks
            await asyncio.sleep(chunk_sleep)
            sleep_seconds -= chunk_sleep
    
    def get_stats(self) -> dict:
        """Get worker and queue statistics"""
        queue_status = self.queue.get_queue_status()
        
        return {
            "worker_running": self.running,
            "search_interval_seconds": self.search_interval,
            "last_search_time": self.last_search_time,
            "queue_status": queue_status,
            "fallback_stats": self.fallback.get_stats() if hasattr(self.fallback, 'get_stats') else {}
        }

async def main():
    """Main entry point for the background worker"""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/google_search_worker.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Ensure logs directory exists
    os.makedirs('logs', exist_ok=True)
    
    worker = GoogleSearchWorker()
    
    try:
        await worker.start()
    except KeyboardInterrupt:
        logger.info("Received interrupt signal, shutting down...")
    except Exception as e:
        logger.error(f"Worker failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())