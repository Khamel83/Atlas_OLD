#!/usr/bin/env python3
"""
Atlas Production Readiness Report Generator

This script generates a comprehensive report on the production readiness of the Atlas system,
checking all critical components and providing a status overview.

Features:
- System status checks
- Service health verification
- Security assessment
- Performance metrics
- Backup and recovery validation
- Monitoring and alerting status
"""

import os
import sys
import subprocess
import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/home/ubuntu/dev/atlas/logs/production_readiness.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("AtlasReadinessReport")


class AtlasReadinessReport:
    def __init__(self):
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "system_info": {},
            "services": {},
            "security": {},
            "performance": {},
            "backup": {},
            "monitoring": {},
            "overall_status": "UNKNOWN",
        }

        # Create logs directory if it doesn't exist
        Path("/home/ubuntu/dev/atlas/logs").mkdir(parents=True, exist_ok=True)

    def check_system_info(self):
        """Check basic system information"""
        logger.info("Checking system information...")

        try:
            # Get hostname
            hostname = subprocess.run(
                ["hostname"], capture_output=True, text=True
            ).stdout.strip()

            # Get OS info
            os_info = subprocess.run(
                ["lsb_release", "-d"], capture_output=True, text=True
            ).stdout.strip()

            # Get uptime
            uptime = subprocess.run(
                ["uptime", "-p"], capture_output=True, text=True
            ).stdout.strip()

            self.report["system_info"] = {
                "hostname": hostname,
                "os": os_info,
                "uptime": uptime,
            }

            logger.info("System information check completed")
        except Exception as e:
            logger.error(f"Error checking system information: {str(e)}")
            self.report["system_info"] = {"error": str(e)}

    def check_services(self):
        """Check the status of all critical services"""
        logger.info("Checking service status...")

        services = {
            "atlas": "Atlas Main Service",
            "postgresql": "PostgreSQL Database",
            "nginx": "Nginx Web Server",
            "atlas-prometheus": "Prometheus Monitoring",
            "atlas-grafana": "Grafana Dashboard",
        }

        service_status = {}

        for service_name, service_desc in services.items():
            try:
                result = subprocess.run(
                    ["systemctl", "is-active", service_name],
                    capture_output=True,
                    text=True,
                )
                status = result.stdout.strip()
                service_status[service_name] = {
                    "description": service_desc,
                    "status": status,
                    "running": status == "active",
                }
            except Exception as e:
                logger.error(f"Error checking {service_name}: {str(e)}")
                service_status[service_name] = {
                    "description": service_desc,
                    "status": "error",
                    "running": False,
                    "error": str(e),
                }

        self.report["services"] = service_status
        logger.info("Service status check completed")

    def check_security(self):
        """Check security configuration"""
        logger.info("Checking security configuration...")

        security_status = {}

        # Check if firewall is active
        try:
            result = subprocess.run(
                ["sudo", "ufw", "status"], capture_output=True, text=True
            )
            firewall_active = "Status: active" in result.stdout
            security_status["firewall"] = {
                "active": firewall_active,
                "status": "active" if firewall_active else "inactive",
            }
        except Exception as e:
            logger.error(f"Error checking firewall: {str(e)}")
            security_status["firewall"] = {
                "active": False,
                "status": "error",
                "error": str(e),
            }

        # Check SSL certificate
        ssl_cert_path = "/etc/letsencrypt/live/atlas.khamel.com/cert.pem"
        if os.path.exists(ssl_cert_path):
            try:
                # Check certificate expiration
                result = subprocess.run(
                    ["openssl", "x509", "-in", ssl_cert_path, "-noout", "-enddate"],
                    capture_output=True,
                    text=True,
                )

                if result.returncode == 0:
                    expiry_info = result.stdout.strip().split("=")[1]
                    security_status["ssl_certificate"] = {
                        "exists": True,
                        "expiry": expiry_info,
                        "status": "valid",
                    }
                else:
                    security_status["ssl_certificate"] = {
                        "exists": True,
                        "status": "error",
                        "error": "Failed to read certificate",
                    }
            except Exception as e:
                logger.error(f"Error checking SSL certificate: {str(e)}")
                security_status["ssl_certificate"] = {
                    "exists": True,
                    "status": "error",
                    "error": str(e),
                }
        else:
            security_status["ssl_certificate"] = {"exists": False, "status": "missing"}

        # Check authentication configuration
        nginx_auth_path = "/etc/nginx/.htpasswd"
        security_status["authentication"] = {
            "configured": os.path.exists(nginx_auth_path),
            "status": (
                "configured" if os.path.exists(nginx_auth_path) else "not configured"
            ),
        }

        self.report["security"] = security_status
        logger.info("Security configuration check completed")

    def check_performance(self):
        """Check system performance metrics"""
        logger.info("Checking performance metrics...")

        performance_status = {}

        try:
            # Check disk usage
            result = subprocess.run(["df", "/"], capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")
                if len(lines) > 1:
                    usage_info = lines[1].split()
                    usage_percent = int(usage_info[4].rstrip("%"))
                    performance_status["disk_usage"] = {
                        "percent": usage_percent,
                        "status": (
                            "critical"
                            if usage_percent > 90
                            else "warning" if usage_percent > 80 else "normal"
                        ),
                    }

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
                        performance_status["memory_usage"] = {
                            "percent": round(usage_percent, 2),
                            "status": (
                                "critical"
                                if usage_percent > 90
                                else "warning" if usage_percent > 80 else "normal"
                            ),
                        }

            # Check CPU load
            with open("/proc/loadavg", "r") as f:
                load_info = f.read().strip().split()
                load_avg = float(load_info[0])
                performance_status["cpu_load"] = {
                    "average": load_avg,
                    "status": "high" if load_avg > 2.0 else "normal",
                }

        except Exception as e:
            logger.error(f"Error checking performance metrics: {str(e)}")
            performance_status["error"] = str(e)

        self.report["performance"] = performance_status
        logger.info("Performance metrics check completed")

    def check_backup(self):
        """Check backup configuration and status"""
        logger.info("Checking backup configuration...")

        backup_status = {}

        # Check if backup directory exists
        backup_dir = "/home/ubuntu/dev/atlas/backups"
        backup_status["directory_exists"] = os.path.exists(backup_dir)

        if os.path.exists(backup_dir):
            try:
                # Count backup files
                backup_files = [
                    f
                    for f in os.listdir(backup_dir)
                    if f.startswith("atlas_backup_") and f.endswith(".sql.gz")
                ]
                backup_status["backup_count"] = len(backup_files)

                # Check latest backup
                if backup_files:
                    latest_backup = max(backup_files)
                    backup_status["latest_backup"] = latest_backup
                    # Check if backup is recent (within 2 days)
                    backup_status["recent_backup"] = (
                        "within 2 days"
                        in subprocess.run(
                            [
                                "find",
                                backup_dir,
                                "-name",
                                latest_backup,
                                "-mtime",
                                "-2",
                            ],
                            capture_output=True,
                            text=True,
                        ).stdout
                    )
                else:
                    backup_status["recent_backup"] = False

            except Exception as e:
                logger.error(f"Error checking backup files: {str(e)}")
                backup_status["error"] = str(e)
        else:
            backup_status["backup_count"] = 0
            backup_status["recent_backup"] = False

        # Check backup cron job
        try:
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
            backup_status["cron_configured"] = "database_backup.py" in result.stdout
        except Exception as e:
            logger.error(f"Error checking backup cron: {str(e)}")
            backup_status["cron_configured"] = False

        self.report["backup"] = backup_status
        logger.info("Backup configuration check completed")

    def check_monitoring(self):
        """Check monitoring and alerting configuration"""
        logger.info("Checking monitoring configuration...")

        monitoring_status = {}

        # Check if monitoring services are running
        prometheus_running = False
        grafana_running = False

        try:
            result = subprocess.run(
                ["systemctl", "is-active", "atlas-prometheus"],
                capture_output=True,
                text=True,
            )
            prometheus_running = result.stdout.strip() == "active"

            result = subprocess.run(
                ["systemctl", "is-active", "atlas-grafana"],
                capture_output=True,
                text=True,
            )
            grafana_running = result.stdout.strip() == "active"
        except Exception as e:
            logger.error(f"Error checking monitoring services: {str(e)}")

        monitoring_status["prometheus_running"] = prometheus_running
        monitoring_status["grafana_running"] = grafana_running

        # Check if alert manager is configured
        alert_manager_path = "/home/ubuntu/dev/atlas/monitoring/alert_manager.py"
        monitoring_status["alert_manager_configured"] = os.path.exists(
            alert_manager_path
        )

        # Check if log monitoring is configured
        log_monitor_path = "/home/ubuntu/dev/atlas/maintenance/system_updates.py"
        monitoring_status["log_monitoring_configured"] = os.path.exists(
            log_monitor_path
        )

        self.report["monitoring"] = monitoring_status
        logger.info("Monitoring configuration check completed")

    def generate_overall_status(self):
        """Generate overall system status"""
        logger.info("Generating overall status...")

        # Check if all critical services are running
        critical_services = ["atlas", "postgresql", "nginx"]
        services_running = all(
            self.report["services"].get(service, {}).get("running", False)
            for service in critical_services
        )

        # Check if security is properly configured
        ssl_valid = (
            self.report["security"].get("ssl_certificate", {}).get("status") == "valid"
        )
        firewall_active = (
            self.report["security"].get("firewall", {}).get("active", False)
        )
        auth_configured = (
            self.report["security"].get("authentication", {}).get("configured", False)
        )
        security_ok = ssl_valid and firewall_active and auth_configured

        # Check if performance is within acceptable limits
        disk_ok = (
            self.report["performance"].get("disk_usage", {}).get("status") != "critical"
        )
        memory_ok = (
            self.report["performance"].get("memory_usage", {}).get("status")
            != "critical"
        )
        cpu_ok = self.report["performance"].get("cpu_load", {}).get("status") != "high"
        performance_ok = disk_ok and memory_ok and cpu_ok

        # Check if backup is configured and recent
        backup_configured = self.report["backup"].get("directory_exists", False)
        recent_backup = self.report["backup"].get("recent_backup", False)
        backup_ok = backup_configured and recent_backup

        # Check if monitoring is configured
        monitoring_ok = (
            self.report["monitoring"].get("prometheus_running", False)
            and self.report["monitoring"].get("grafana_running", False)
            and self.report["monitoring"].get("alert_manager_configured", False)
        )

        # Determine overall status
        if (
            services_running
            and security_ok
            and performance_ok
            and backup_ok
            and monitoring_ok
        ):
            self.report["overall_status"] = "READY"
        elif services_running and performance_ok:
            self.report["overall_status"] = "WARNING"
        else:
            self.report["overall_status"] = "NOT_READY"

        logger.info(f"Overall status: {self.report['overall_status']}")

    def generate_report(self):
        """Generate the complete readiness report"""
        logger.info("Generating production readiness report...")

        # Run all checks
        self.check_system_info()
        self.check_services()
        self.check_security()
        self.check_performance()
        self.check_backup()
        self.check_monitoring()
        self.generate_overall_status()

        # Save report to file
        report_file = f"/home/ubuntu/dev/atlas/logs/production_readiness_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w") as f:
            json.dump(self.report, f, indent=2)

        logger.info(f"Report saved to {report_file}")
        return self.report

    def print_summary(self):
        """Print a human-readable summary of the report"""
        print("\n" + "=" * 60)
        print("ATLAS PRODUCTION READINESS REPORT")
        print("=" * 60)
        print(f"Generated: {self.report['timestamp']}")
        print(f"Overall Status: {self.report['overall_status']}")

        # System Info
        print("\n--- SYSTEM INFORMATION ---")
        sys_info = self.report.get("system_info", {})
        if "error" not in sys_info:
            print(f"Hostname: {sys_info.get('hostname', 'N/A')}")
            print(f"OS: {sys_info.get('os', 'N/A')}")
            print(f"Uptime: {sys_info.get('uptime', 'N/A')}")
        else:
            print(f"Error: {sys_info['error']}")

        # Services
        print("\n--- SERVICE STATUS ---")
        services = self.report.get("services", {})
        for service_name, service_info in services.items():
            status_icon = "✅" if service_info.get("running", False) else "❌"
            print(
                f"{status_icon} {service_info.get('description', service_name)}: {service_info.get('status', 'unknown')}"
            )

        # Security
        print("\n--- SECURITY STATUS ---")
        security = self.report.get("security", {})

        # Firewall
        firewall = security.get("firewall", {})
        status_icon = "✅" if firewall.get("active", False) else "❌"
        print(f"{status_icon} Firewall: {firewall.get('status', 'unknown')}")

        # SSL Certificate
        ssl_cert = security.get("ssl_certificate", {})
        if ssl_cert.get("exists", False):
            status_icon = "✅" if ssl_cert.get("status") == "valid" else "❌"
            print(f"{status_icon} SSL Certificate: {ssl_cert.get('status', 'unknown')}")
            if "expiry" in ssl_cert:
                print(f"    Expiry: {ssl_cert['expiry']}")
        else:
            print("❌ SSL Certificate: missing")

        # Authentication
        auth = security.get("authentication", {})
        status_icon = "✅" if auth.get("configured", False) else "❌"
        print(f"{status_icon} Authentication: {auth.get('status', 'unknown')}")

        # Performance
        print("\n--- PERFORMANCE METRICS ---")
        performance = self.report.get("performance", {})

        # Disk Usage
        disk_usage = performance.get("disk_usage", {})
        if disk_usage:
            status_icon = (
                "✅"
                if disk_usage.get("status") == "normal"
                else "⚠️" if disk_usage.get("status") == "warning" else "❌"
            )
            print(f"{status_icon} Disk Usage: {disk_usage.get('percent', 'N/A')}%")

        # Memory Usage
        memory_usage = performance.get("memory_usage", {})
        if memory_usage:
            status_icon = (
                "✅"
                if memory_usage.get("status") == "normal"
                else "⚠️" if memory_usage.get("status") == "warning" else "❌"
            )
            print(f"{status_icon} Memory Usage: {memory_usage.get('percent', 'N/A')}%")

        # CPU Load
        cpu_load = performance.get("cpu_load", {})
        if cpu_load:
            status_icon = "✅" if cpu_load.get("status") == "normal" else "❌"
            print(f"{status_icon} CPU Load: {cpu_load.get('average', 'N/A')}")

        # Backup
        print("\n--- BACKUP STATUS ---")
        backup = self.report.get("backup", {})
        status_icon = "✅" if backup.get("directory_exists", False) else "❌"
        print(
            f"{status_icon} Backup Directory: {'exists' if backup.get('directory_exists', False) else 'missing'}"
        )

        if backup.get("directory_exists", False):
            print(f"    Backup Count: {backup.get('backup_count', 'N/A')}")
            status_icon = "✅" if backup.get("recent_backup", False) else "❌"
            print(
                f"{status_icon} Recent Backup: {'yes' if backup.get('recent_backup', False) else 'no'}"
            )

        status_icon = "✅" if backup.get("cron_configured", False) else "❌"
        print(
            f"{status_icon} Backup Cron: {'configured' if backup.get('cron_configured', False) else 'not configured'}"
        )

        # Monitoring
        print("\n--- MONITORING STATUS ---")
        monitoring = self.report.get("monitoring", {})
        status_icon = "✅" if monitoring.get("prometheus_running", False) else "❌"
        print(
            f"{status_icon} Prometheus: {'running' if monitoring.get('prometheus_running', False) else 'not running'}"
        )

        status_icon = "✅" if monitoring.get("grafana_running", False) else "❌"
        print(
            f"{status_icon} Grafana: {'running' if monitoring.get('grafana_running', False) else 'not running'}"
        )

        status_icon = (
            "✅" if monitoring.get("alert_manager_configured", False) else "❌"
        )
        print(
            f"{status_icon} Alert Manager: {'configured' if monitoring.get('alert_manager_configured', False) else 'not configured'}"
        )

        status_icon = (
            "✅" if monitoring.get("log_monitoring_configured", False) else "❌"
        )
        print(
            f"{status_icon} Log Monitoring: {'configured' if monitoring.get('log_monitoring_configured', False) else 'not configured'}"
        )

        print("\n" + "=" * 60)

        # Recommendations
        print("RECOMMENDATIONS:")
        if self.report["overall_status"] == "READY":
            print("✅ System is ready for production use!")
        elif self.report["overall_status"] == "WARNING":
            print("⚠️ System can run but needs attention:")
            if not security_ok:
                print("   - Review security configuration")
            if not backup_ok:
                print("   - Check backup configuration")
            if not monitoring_ok:
                print("   - Verify monitoring setup")
        else:
            print("❌ System is NOT ready for production:")
            if not services_running:
                print("   - Start all required services")
            if not security_ok:
                print("   - Configure security settings")
            if not performance_ok:
                print("   - Address performance issues")
            if not backup_ok:
                print("   - Fix backup configuration")
            if not monitoring_ok:
                print("   - Set up monitoring and alerting")


def main():
    """Main function"""
    print("Atlas Production Readiness Report Generator")
    print("=" * 45)

    # Create and run report
    reporter = AtlasReadinessReport()
    report = reporter.generate_report()
    reporter.print_summary()

    # Return appropriate exit code
    if report["overall_status"] == "READY":
        return 0
    elif report["overall_status"] == "WARNING":
        return 1
    else:
        return 2


if __name__ == "__main__":
    sys.exit(main())
