#!/usr/bin/env python3
"""
Atlas Background Service

This script runs as a systemd service to continuously process content and manage
Atlas operations in the background.

Features:
- Continuously processes content from queues
- Monitors system health and performance
- Manages automated tasks and scheduling
- Handles error recovery and retry logic
- Provides status reporting and logging
"""

import os
import sys
import time
import signal
import subprocess
import logging
from datetime import datetime, timedelta
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/home/ubuntu/dev/atlas/logs/atlas_background.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("AtlasBackgroundService")


class AtlasBackgroundService:
    def __init__(self):
        self.running = True
        self.last_health_check = datetime.now()
        self.last_maintenance = datetime.now()

        # Create logs directory if it doesn't exist
        Path("/home/ubuntu/dev/atlas/logs").mkdir(parents=True, exist_ok=True)

        # Register signal handlers for graceful shutdown
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)

    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.running = False

    def run_content_processing(self):
        """Run content processing tasks"""
        try:
            # Check for articles to process
            result = subprocess.run(
                ["python3", "/home/ubuntu/dev/atlas/run.py", "--articles"],
                capture_output=True,
                text=True,
                timeout=300,
            )

            if result.returncode == 0:
                logger.info("Article processing completed successfully")
            else:
                logger.warning(
                    f"Article processing completed with warnings: {result.stderr}"
                )

        except subprocess.TimeoutExpired:
            logger.error("Article processing timed out")
        except Exception as e:
            logger.error(f"Error during article processing: {str(e)}")

    def run_podcast_processing(self):
        """Run podcast processing tasks"""
        try:
            # Check for podcasts to process
            result = subprocess.run(
                ["python3", "/home/ubuntu/dev/atlas/run.py", "--podcasts"],
                capture_output=True,
                text=True,
                timeout=600,
            )

            if result.returncode == 0:
                logger.info("Podcast processing completed successfully")
            else:
                logger.warning(
                    f"Podcast processing completed with warnings: {result.stderr}"
                )

        except subprocess.TimeoutExpired:
            logger.error("Podcast processing timed out")
        except Exception as e:
            logger.error(f"Error during podcast processing: {str(e)}")

    def run_youtube_processing(self):
        """Run YouTube processing tasks"""
        try:
            # Check for YouTube videos to process
            result = subprocess.run(
                ["python3", "/home/ubuntu/dev/atlas/run.py", "--youtube"],
                capture_output=True,
                text=True,
                timeout=600,
            )

            if result.returncode == 0:
                logger.info("YouTube processing completed successfully")
            else:
                logger.warning(
                    f"YouTube processing completed with warnings: {result.stderr}"
                )

        except subprocess.TimeoutExpired:
            logger.error("YouTube processing timed out")
        except Exception as e:
            logger.error(f"Error during YouTube processing: {str(e)}")

    def check_health(self):
        """Perform system health checks"""
        try:
            # Check disk space
            result = subprocess.run(["df", "/"], capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")
                if len(lines) > 1:
                    usage_info = lines[1].split()
                    usage_percent = int(usage_info[4].rstrip("%"))
                    if usage_percent > 90:
                        logger.warning(f"Disk usage is high: {usage_percent}%")
                    else:
                        logger.info(f"Disk usage: {usage_percent}%")

            # Check memory usage
            result = subprocess.run(["free"], capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")
                if len(lines) > 1:
                    mem_info = lines[1].split()
                    if len(mem_info) >= 7:
                        total_mem = int(mem_info[1])
                        avail_mem = int(mem_info[6])
                        usage_percent = ((total_mem - avail_mem) / total_mem) * 100
                        if usage_percent > 80:
                            logger.warning(
                                f"Memory usage is high: {usage_percent:.1f}%"
                            )
                        else:
                            logger.info(f"Memory usage: {usage_percent:.1f}%")

            # Check service status
            services = ["postgresql", "nginx"]
            for service in services:
                result = subprocess.run(
                    ["systemctl", "is-active", service], capture_output=True, text=True
                )
                if result.returncode == 0 and result.stdout.strip() == "active":
                    logger.info(f"Service {service} is running")
                else:
                    logger.warning(f"Service {service} is not active")

        except Exception as e:
            logger.error(f"Error during health check: {str(e)}")

    def run_maintenance(self):
        """Run maintenance tasks"""
        try:
            # Run maintenance script
            result = subprocess.run(
                ["python3", "/home/ubuntu/dev/atlas/maintenance/atlas_maintenance.py"],
                capture_output=True,
                text=True,
                timeout=300,
            )

            if result.returncode == 0:
                logger.info("Maintenance tasks completed successfully")
            else:
                logger.warning(
                    f"Maintenance tasks completed with warnings: {result.stderr}"
                )

        except subprocess.TimeoutExpired:
            logger.error("Maintenance tasks timed out")
        except Exception as e:
            logger.error(f"Error during maintenance: {str(e)}")

    def process_retry_queue(self):
        """Process items in the retry queue"""
        try:
            # Run retry script
            result = subprocess.run(
                ["python3", "/home/ubuntu/dev/atlas/retry_failed_articles.py"],
                capture_output=True,
                text=True,
                timeout=300,
            )

            if result.returncode == 0:
                logger.info("Retry queue processing completed successfully")
            else:
                logger.warning(
                    f"Retry queue processing completed with warnings: {result.stderr}"
                )

        except subprocess.TimeoutExpired:
            logger.error("Retry queue processing timed out")
        except Exception as e:
            logger.error(f"Error during retry queue processing: {str(e)}")

    def run(self):
        """Main service loop"""
        logger.info("Atlas Background Service started")

        # Processing intervals in seconds
        content_processing_interval = 300  # 5 minutes
        health_check_interval = 60  # 1 minute
        maintenance_interval = 3600  # 1 hour
        retry_queue_interval = 1800  # 30 minutes

        last_content_processing = datetime.now() - timedelta(
            seconds=content_processing_interval
        )
        last_retry_queue = datetime.now() - timedelta(seconds=retry_queue_interval)

        while self.running:
            current_time = datetime.now()

            # Run content processing periodically
            if (
                current_time - last_content_processing
            ).total_seconds() >= content_processing_interval:
                logger.info("Starting content processing cycle")
                self.run_content_processing()
                self.run_podcast_processing()
                self.run_youtube_processing()
                last_content_processing = current_time

            # Run retry queue processing periodically
            if (
                current_time - last_retry_queue
            ).total_seconds() >= retry_queue_interval:
                logger.info("Processing retry queue")
                self.process_retry_queue()
                last_retry_queue = current_time

            # Run health checks periodically
            if (
                current_time - self.last_health_check
            ).total_seconds() >= health_check_interval:
                self.check_health()
                self.last_health_check = current_time

            # Run maintenance tasks periodically
            if (
                current_time - self.last_maintenance
            ).total_seconds() >= maintenance_interval:
                logger.info("Starting maintenance tasks")
                self.run_maintenance()
                self.last_maintenance = current_time

            # Sleep briefly to prevent excessive CPU usage
            time.sleep(10)

        logger.info("Atlas Background Service stopped")


if __name__ == "__main__":
    # Change to the Atlas directory
    os.chdir("/home/ubuntu/dev/atlas")

    # Create and run the service
    service = AtlasBackgroundService()
    try:
        service.run()
    except KeyboardInterrupt:
        logger.info("Service interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error in background service: {str(e)}")
        sys.exit(1)

    logger.info("Atlas Background Service shutdown complete")
