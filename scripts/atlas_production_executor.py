#!/usr/bin/env python3
"""
Atlas Production Executor

This script manages the execution of Atlas in a production environment,
handling service management, monitoring, and maintenance tasks.

Features:
- Service lifecycle management
- Health monitoring and reporting
- Automated maintenance and updates
- Backup and recovery operations
- Performance optimization
"""

import os
import sys
import time
import subprocess
import logging
import signal
import psutil
from datetime import datetime, timedelta
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/home/ubuntu/dev/atlas/logs/atlas_production.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("AtlasProductionExecutor")


class AtlasProductionExecutor:
    def __init__(self):
        self.running = True

        # Create logs directory if it doesn't exist
        Path("/home/ubuntu/dev/atlas/logs").mkdir(parents=True, exist_ok=True)

        # Register signal handlers for graceful shutdown
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)

    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.running = False

    def start_services(self):
        """Start all Atlas services"""
        logger.info("Starting Atlas services...")

        services = [
            "atlas.service",
            "atlas-prometheus.service",
            "atlas-grafana.service",
        ]

        for service in services:
            try:
                result = subprocess.run(
                    ["sudo", "systemctl", "start", service],
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    logger.info(f"Started {service}")
                else:
                    logger.error(f"Failed to start {service}: {result.stderr}")
            except Exception as e:
                logger.error(f"Error starting {service}: {str(e)}")

    def stop_services(self):
        """Stop all Atlas services"""
        logger.info("Stopping Atlas services...")

        services = [
            "atlas.service",
            "atlas-prometheus.service",
            "atlas-grafana.service",
        ]

        for service in services:
            try:
                result = subprocess.run(
                    ["sudo", "systemctl", "stop", service],
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    logger.info(f"Stopped {service}")
                else:
                    logger.error(f"Failed to stop {service}: {result.stderr}")
            except Exception as e:
                logger.error(f"Error stopping {service}: {str(e)}")

    def restart_services(self):
        """Restart all Atlas services"""
        logger.info("Restarting Atlas services...")

        services = [
            "atlas.service",
            "atlas-prometheus.service",
            "atlas-grafana.service",
        ]

        for service in services:
            try:
                result = subprocess.run(
                    ["sudo", "systemctl", "restart", service],
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    logger.info(f"Restarted {service}")
                else:
                    logger.error(f"Failed to restart {service}: {result.stderr}")
            except Exception as e:
                logger.error(f"Error restarting {service}: {str(e)}")

    def check_service_status(self):
        """Check the status of all Atlas services"""
        logger.info("Checking Atlas service status...")

        services = [
            "atlas.service",
            "atlas-prometheus.service",
            "atlas-grafana.service",
        ]

        status_report = {}

        for service in services:
            try:
                result = subprocess.run(
                    ["sudo", "systemctl", "is-active", service],
                    capture_output=True,
                    text=True,
                )
                status = result.stdout.strip()
                status_report[service] = status
                if status == "active":
                    logger.info(f"{service} is running")
                else:
                    logger.warning(f"{service} is {status}")
            except Exception as e:
                logger.error(f"Error checking {service} status: {str(e)}")
                status_report[service] = "error"

        return status_report

    def run_health_check(self):
        """Run comprehensive health check"""
        logger.info("Running comprehensive health check...")

        # Check system resources
        self.check_system_resources()

        # Check service status
        self.check_service_status()

        # Check disk space
        self.check_disk_space()

        # Check database connectivity
        self.check_database()

        logger.info("Health check completed")

    def check_system_resources(self):
        """Check system resource usage"""
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        logger.info(f"CPU usage: {cpu_percent}%")

        # Memory usage
        memory = psutil.virtual_memory()
        logger.info(
            f"Memory usage: {memory.percent}% ({memory.used / (1024**3):.2f}GB / {memory.total / (1024**3):.2f}GB)"
        )

        # Load average
        load_avg = os.getloadavg()
        logger.info(
            f"Load average: {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}"
        )

    def check_disk_space(self):
        """Check disk space usage"""
        disk = psutil.disk_usage("/")
        usage_percent = (disk.used / disk.total) * 100
        logger.info(
            f"Disk usage: {usage_percent:.1f}% ({disk.used / (1024**3):.2f}GB / {disk.total / (1024**3):.2f}GB)"
        )

        if usage_percent > 90:
            logger.warning("Disk usage is critically high!")
        elif usage_percent > 80:
            logger.warning("Disk usage is high")

    def check_database(self):
        """Check database connectivity"""
        try:
            # This is a placeholder - in a real implementation, you would check actual database connectivity
            result = subprocess.run(
                ["pg_isready", "-U", "atlas_user", "-d", "atlas"],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                logger.info("Database is accessible")
            else:
                logger.error("Database is not accessible")
        except Exception as e:
            logger.error(f"Error checking database: {str(e)}")

    def run_backup(self):
        """Run backup process"""
        logger.info("Starting backup process...")

        try:
            result = subprocess.run(
                ["python3", "/home/ubuntu/dev/atlas/backup/database_backup.py"],
                capture_output=True,
                text=True,
                timeout=600,
            )

            if result.returncode == 0:
                logger.info("Backup completed successfully")
            else:
                logger.error(f"Backup failed: {result.stderr}")
        except subprocess.TimeoutExpired:
            logger.error("Backup timed out")
        except Exception as e:
            logger.error(f"Error during backup: {str(e)}")

    def run_maintenance(self):
        """Run maintenance tasks"""
        logger.info("Starting maintenance tasks...")

        try:
            result = subprocess.run(
                ["python3", "/home/ubuntu/dev/atlas/maintenance/atlas_maintenance.py"],
                capture_output=True,
                text=True,
                timeout=600,
            )

            if result.returncode == 0:
                logger.info("Maintenance completed successfully")
            else:
                logger.error(f"Maintenance failed: {result.stderr}")
        except subprocess.TimeoutExpired:
            logger.error("Maintenance timed out")
        except Exception as e:
            logger.error(f"Error during maintenance: {str(e)}")

    def run_update_check(self):
        """Check for and apply system updates"""
        logger.info("Checking for system updates...")

        try:
            # Update package list
            subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True)

            # Check for security updates
            result = subprocess.run(
                ["apt", "list", "--upgradable"], capture_output=True, text=True
            )

            if "security" in result.stdout:
                logger.info("Security updates available")
                # In a production environment, you might want to automatically apply security updates
                # For now, we'll just log that they're available
            else:
                logger.info("No security updates available")
        except Exception as e:
            logger.error(f"Error checking for updates: {str(e)}")

    def generate_status_report(self):
        """Generate a status report"""
        logger.info("Generating status report...")

        report = {
            "timestamp": datetime.now().isoformat(),
            "services": self.check_service_status(),
            "system": {
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": (
                    psutil.disk_usage("/").used / psutil.disk_usage("/").total
                )
                * 100,
            },
        }

        # Save report to file
        report_file = f"/home/ubuntu/dev/atlas/logs/status_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        import json

        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)

        logger.info(f"Status report saved to {report_file}")
        return report

    def execute_all_tasks(self):
        """Execute all Atlas production tasks - one-time execution"""
        logger.info("Executing all Atlas production tasks...")

        # Start services
        self.start_services()

        # Run health check
        self.run_health_check()

        # Run maintenance
        self.run_maintenance()

        # Run backup
        self.run_backup()

        # Generate status report
        self.generate_status_report()

        logger.info("All Atlas production tasks completed")

    def run(self):
        """Main execution loop"""
        logger.info("Atlas Production Executor started")

        # Start services
        self.start_services()

        # Main loop
        while self.running:
            try:
                # Run health check every 5 minutes
                self.run_health_check()

                # Run maintenance every hour
                self.run_maintenance()

                # Check for updates daily
                self.run_update_check()

                # Generate status report every 10 minutes
                self.generate_status_report()

                # Wait before next cycle
                time.sleep(300)  # 5 minutes

            except Exception as e:
                logger.error(f"Error in production executor loop: {str(e)}")
                time.sleep(60)  # Wait 1 minute before retrying

        logger.info("Atlas Production Executor stopped")


def main():
    """Main function"""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        executor = AtlasProductionExecutor()

        if command == "start":
            executor.start_services()
        elif command == "stop":
            executor.stop_services()
        elif command == "restart":
            executor.restart_services()
        elif command == "status":
            executor.check_service_status()
        elif command == "health":
            executor.run_health_check()
        elif command == "backup":
            executor.run_backup()
        elif command == "maintenance":
            executor.run_maintenance()
        elif command == "report":
            executor.generate_status_report()
        else:
            print(f"Unknown command: {command}")
            print(
                "Available commands: start, stop, restart, status, health, backup, maintenance, report"
            )
            return 1
    else:
        # Run in continuous mode
        executor = AtlasProductionExecutor()
        try:
            executor.run()
        except KeyboardInterrupt:
            logger.info("Production executor interrupted by user")
        except Exception as e:
            logger.error(f"Unexpected error in production executor: {str(e)}")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
