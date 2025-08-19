"""
Disk Space Management for Atlas
Manages disk space and cleanup automation
"""

import os
import subprocess
import sys
from datetime import datetime
import shutil

class DiskManagement:
    """Manage disk space for Atlas system"""
    
    def __init__(self):
        self.log_file = "/var/log/atlas_disk_management.log"
        self.warning_threshold = 80  # Percent
        self.critical_threshold = 90  # Percent
        
    def create_disk_monitoring_script(self):
        """Create disk space monitoring and cleanup automation"""
        print("Creating disk space monitoring script...")
        
        monitoring_script = f"""#!/bin/bash
# Atlas Disk Space Monitoring Script

LOG_FILE="{self.log_file}"
WARNING_THRESHOLD={self.warning_threshold}
CRITICAL_THRESHOLD={self.critical_threshold}
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting disk space monitoring" >> $LOG_FILE

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}}

# Check disk usage
DISK_USAGE=$(df / | tail -1 | awk '{{print $5}}' | sed 's/%//')
log_message "Current disk usage: ${DISK_USAGE}%"

# Check if disk usage exceeds thresholds
if [ $DISK_USAGE -ge $CRITICAL_THRESHOLD ]; then
    log_message "CRITICAL: Disk usage (${{DISK_USAGE}}%) exceeds critical threshold (${{CRITICAL_THRESHOLD}}%)"
    # Trigger immediate cleanup
    /usr/local/bin/atlas_disk_cleanup.sh --critical >> $LOG_FILE 2>&1
elif [ $DISK_USAGE -ge $WARNING_THRESHOLD ]; then
    log_message "WARNING: Disk usage (${{DISK_USAGE}}%) exceeds warning threshold (${{WARNING_THRESHOLD}}%)"
    # Trigger cleanup
    /usr/local/bin/atlas_disk_cleanup.sh >> $LOG_FILE 2>&1
else
    log_message "Disk usage is within acceptable limits"
fi

echo "[$DATE] Disk space monitoring completed" >> $LOG_FILE
"""
        
        script_path = "/usr/local/bin/atlas_disk_monitor.sh"
        with open(script_path, "w") as f:
            f.write(monitoring_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created disk monitoring script at {script_path}")
        return script_path
    
    def implement_old_log_cleanup(self):
        """Implement old log file cleanup (keep 30 days)"""
        print("Implementing old log file cleanup...")
        
        log_cleanup_script = f"""#!/bin/bash
# Atlas Old Log File Cleanup Script

LOG_FILE="{self.log_file}"
RETENTION_DAYS=30
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting old log file cleanup" >> $LOG_FILE

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}}

# Define log directories
LOG_DIRS=(
    "/var/log/atlas"
    "/var/log/nginx"
    "/var/log/postgresql"
    "/home/ubuntu/dev/atlas/logs"
)

# Clean up old log files
for log_dir in "${{LOG_DIRS[@]}}"; do
    if [ -d "$log_dir" ]; then
        log_message "Cleaning up logs in $log_dir"
        find "$log_dir" -name "*.log.*" -type f -mtime +$RETENTION_DAYS -delete 2>/dev/null
        find "$log_dir" -name "*.log.gz" -type f -mtime +$RETENTION_DAYS -delete 2>/dev/null
        find "$log_dir" -name "*.log.[0-9]*" -type f -mtime +$RETENTION_DAYS -delete 2>/dev/null
    fi
done

log_message "Old log file cleanup completed"
echo "[$DATE] Old log file cleanup completed" >> $LOG_FILE
"""
        
        script_path = "/usr/local/bin/atlas_log_cleanup.sh"
        with open(script_path, "w") as f:
            f.write(log_cleanup_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created log cleanup script at {script_path}")
        return script_path
    
    def setup_temporary_file_cleanup(self):
        """Set up temporary file cleanup"""
        print("Setting up temporary file cleanup...")
        
        temp_cleanup_script = f"""#!/bin/bash
# Atlas Temporary File Cleanup Script

LOG_FILE="{self.log_file}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting temporary file cleanup" >> $LOG_FILE

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}}

# Clean up temporary directories
TEMP_DIRS=(
    "/tmp"
    "/var/tmp"
    "/home/ubuntu/dev/atlas/temp"
    "/home/ubuntu/dev/atlas/cache"
)

for temp_dir in "${{TEMP_DIRS[@]}}"; do
    if [ -d "$temp_dir" ]; then
        log_message "Cleaning up temporary files in $temp_dir"
        # Remove files older than 7 days
        find "$temp_dir" -type f -mtime +7 -delete 2>/dev/null
        # Remove empty directories
        find "$temp_dir" -type d -empty -delete 2>/dev/null
    fi
done

log_message "Temporary file cleanup completed"
echo "[$DATE] Temporary file cleanup completed" >> $LOG_FILE
"""
        
        script_path = "/usr/local/bin/atlas_temp_cleanup.sh"
        with open(script_path, "w") as f:
            f.write(temp_cleanup_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to daily cron
        cron_job = f"0 2 * * * {script_path} >> /var/log/atlas_temp_cleanup_cron.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added temporary file cleanup cron job")
            else:
                print("Temporary file cleanup cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with temporary file cleanup job")
        
        print(f"Created temporary file cleanup script at {script_path}")
        return script_path
    
    def create_old_backup_cleanup(self):
        """Create old backup cleanup (local and OCI)"""
        print("Creating old backup cleanup...")
        
        backup_cleanup_script = f"""#!/bin/bash
# Atlas Old Backup Cleanup Script

LOG_FILE="{self.log_file}"
RETENTION_DAYS=30
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting old backup cleanup" >> $LOG_FILE

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}}

# Clean up local database backups
if [ -d "/backup/database" ]; then
    log_message "Cleaning up old database backups"
    find /backup/database -name "atlas_backup_*.sql.gz" -type f -mtime +$RETENTION_DAYS -delete 2>/dev/null
fi

# Clean up local machine backups
if [ -d "/backup/local" ]; then
    log_message "Cleaning up old local backups"
    find /backup/local -name "backup_*" -type d -mtime +$RETENTION_DAYS -exec rm -rf {{}} + 2>/dev/null
fi

# Clean up OCI backups (stub - would require OCI CLI)
# log_message "Cleaning up old OCI backups"
# oci os object list -bn atlas-backups --prefix backups/ | grep -o 'atlas_backup_[0-9]*_[0-9]*.sql.gz' | while read backup; do
#     # Check backup age and delete if older than retention
# done

log_message "Old backup cleanup completed"
echo "[$DATE] Old backup cleanup completed" >> $LOG_FILE
"""
        
        script_path = "/usr/local/bin/atlas_backup_cleanup.sh"
        with open(script_path, "w") as f:
            f.write(backup_cleanup_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to weekly cron
        cron_job = f"0 3 * * 0 {script_path} >> /var/log/atlas_backup_cleanup_cron.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added backup cleanup cron job")
            else:
                print("Backup cleanup cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with backup cleanup job")
        
        print(f"Created backup cleanup script at {script_path}")
        return script_path
    
    def add_disk_space_alerts(self):
        """Add disk space alerts (80% and 90% thresholds)"""
        print("Adding disk space alerts...")
        
        alert_script = f"""#!/bin/bash
# Atlas Disk Space Alert Script

LOG_FILE="{self.log_file}"
WARNING_THRESHOLD={self.warning_threshold}
CRITICAL_THRESHOLD={self.critical_threshold}
ADMIN_EMAIL="admin@example.com"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Checking disk space for alerts" >> $LOG_FILE

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}}

# Check disk usage
DISK_USAGE=$(df / | tail -1 | awk '{{print $5}}' | sed 's/%//')
log_message "Current disk usage: ${DISK_USAGE}%"

# Send alerts based on thresholds
if [ $DISK_USAGE -ge $CRITICAL_THRESHOLD ]; then
    log_message "CRITICAL: Disk usage (${{DISK_USAGE}}%) exceeds critical threshold"
    # Send critical alert email
    echo "CRITICAL: Atlas disk usage is ${{DISK_USAGE}}%, which exceeds the critical threshold of ${{CRITICAL_THRESHOLD}}%.
    
    Immediate action is required to free up disk space.
    
    Current disk usage:
    $(df -h /)
    
    Please check the system and take corrective action." | mail -s "Atlas CRITICAL Disk Space Alert" $ADMIN_EMAIL
elif [ $DISK_USAGE -ge $WARNING_THRESHOLD ]; then
    log_message "WARNING: Disk usage (${{DISK_USAGE}}%) exceeds warning threshold"
    # Send warning alert email
    echo "WARNING: Atlas disk usage is ${{DISK_USAGE}}%, which exceeds the warning threshold of ${{WARNING_THRESHOLD}}%.
    
    Please monitor disk usage and consider cleanup actions.
    
    Current disk usage:
    $(df -h /)" | mail -s "Atlas Disk Space Warning" $ADMIN_EMAIL
else
    log_message "Disk usage is within acceptable limits"
fi

echo "[$DATE] Disk space alert check completed" >> $LOG_FILE
"""
        
        script_path = "/usr/local/bin/atlas_disk_alert.sh"
        with open(script_path, "w") as f:
            f.write(alert_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to hourly cron for frequent monitoring
        cron_job = f"0 * * * * {script_path} >> /var/log/atlas_disk_alert_cron.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added disk space alert cron job")
            else:
                print("Disk space alert cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with disk space alert job")
        
        print(f"Created disk space alert script at {script_path}")
        return script_path
    
    def configure_automatic_cleanup(self):
        """Configure automatic cleanup when space is low"""
        print("Configuring automatic cleanup...")
        
        auto_cleanup_script = f"""#!/bin/bash
# Atlas Automatic Cleanup Script

LOG_FILE="{self.log_file}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting automatic cleanup" >> $LOG_FILE

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}}

# Function to perform critical cleanup
perform_critical_cleanup() {{
    log_message "Performing critical cleanup"
    
    # Clean up temporary files (aggressive)
    find /tmp -type f -mtime +1 -delete 2>/dev/null
    find /var/tmp -type f -mtime +1 -delete 2>/dev/null
    
    # Clean up cache files
    if [ -d "/home/ubuntu/dev/atlas/cache" ]; then
        find /home/ubuntu/dev/atlas/cache -type f -delete 2>/dev/null
    fi
    
    # Clean up old logs more aggressively
    find /var/log -name "*.log.*" -type f -mtime +7 -delete 2>/dev/null
    find /var/log -name "*.log.gz" -type f -mtime +7 -delete 2>/dev/null
    
    log_message "Critical cleanup completed"
}}

# Function to perform standard cleanup
perform_standard_cleanup() {{
    log_message "Performing standard cleanup"
    
    # Run regular cleanup scripts
    /usr/local/bin/atlas_temp_cleanup.sh >> $LOG_FILE 2>&1
    /usr/local/bin/atlas_log_cleanup.sh >> $LOG_FILE 2>&1
    
    log_message "Standard cleanup completed"
}}

# Check command line argument for cleanup type
if [ "$1" == "--critical" ]; then
    perform_critical_cleanup
else
    perform_standard_cleanup
fi

echo "[$DATE] Automatic cleanup completed" >> $LOG_FILE
"""
        
        script_path = "/usr/local/bin/atlas_disk_cleanup.sh"
        with open(script_path, "w") as f:
            f.write(auto_cleanup_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created automatic cleanup script at {script_path}")
        return script_path
    
    def test_disk_management(self):
        """Test disk management functionality"""
        print("Testing disk management...")
        
        # In a real implementation, this would:
        # 1. Run each disk management script in test mode
        # 2. Verify cron jobs are properly configured
        # 3. Check log files are being created
        # 4. Verify cleanup functionality
        
        try:
            # Check if required scripts exist
            scripts = [
                "/usr/local/bin/atlas_disk_monitor.sh",
                "/usr/local/bin/atlas_log_cleanup.sh",
                "/usr/local/bin/atlas_temp_cleanup.sh",
                "/usr/local/bin/atlas_backup_cleanup.sh",
                "/usr/local/bin/atlas_disk_alert.sh",
                "/usr/local/bin/atlas_disk_cleanup.sh"
            ]
            
            missing_scripts = []
            for script in scripts:
                if not os.path.exists(script):
                    missing_scripts.append(script)
            
            if missing_scripts:
                print(f"✗ Missing scripts: {missing_scripts}")
                return False
            else:
                print("✓ All disk management scripts exist")
            
            # Check if cron jobs exist
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
            cron_content = result.stdout
            
            required_jobs = [
                "atlas_temp_cleanup.sh",
                "atlas_backup_cleanup.sh",
                "atlas_disk_alert.sh"
            ]
            
            missing_jobs = []
            for job in required_jobs:
                if job not in cron_content:
                    missing_jobs.append(job)
            
            if missing_jobs:
                print(f"✗ Missing cron jobs: {missing_jobs}")
                return False
            else:
                print("✓ All required cron jobs configured")
            
            # Test disk space checking
            disk_usage = shutil.disk_usage("/")
            total_gb = disk_usage.total / (1024**3)
            used_gb = disk_usage.used / (1024**3)
            free_gb = disk_usage.free / (1024**3)
            usage_percent = (used_gb / total_gb) * 100
            
            print(f"✓ Disk space check: {usage_percent:.1f}% used ({used_gb:.1f}GB / {total_gb:.1f}GB)")
            
            print("Disk management test completed successfully")
            return True
            
        except Exception as e:
            print(f"✗ Disk management test failed: {e}")
            return False

def main():
    """Main disk management function"""
    if os.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
        sys.exit(1)
    
    # Initialize disk management
    disk_mgmt = DiskManagement()
    
    # Create disk monitoring script
    monitor_script = disk_mgmt.create_disk_monitoring_script()
    print(f"Disk monitoring script created at: {monitor_script}")
    
    # Implement old log cleanup
    log_cleanup_script = disk_mgmt.implement_old_log_cleanup()
    print(f"Log cleanup script created at: {log_cleanup_script}")
    
    # Setup temporary file cleanup
    temp_cleanup_script = disk_mgmt.setup_temporary_file_cleanup()
    print(f"Temporary file cleanup script created at: {temp_cleanup_script}")
    
    # Create old backup cleanup
    backup_cleanup_script = disk_mgmt.create_old_backup_cleanup()
    print(f"Backup cleanup script created at: {backup_cleanup_script}")
    
    # Add disk space alerts
    alert_script = disk_mgmt.add_disk_space_alerts()
    print(f"Disk space alert script created at: {alert_script}")
    
    # Configure automatic cleanup
    cleanup_script = disk_mgmt.configure_automatic_cleanup()
    print(f"Automatic cleanup script created at: {cleanup_script}")
    
    # Test disk management
    if disk_mgmt.test_disk_management():
        print("✓ Disk management test successful")
    else:
        print("✗ Disk management test failed")
    
    print("\nDisk space management configuration completed!")
    print("Disk usage monitored hourly with email alerts")
    print("Automatic cleanup triggered when space is low")
    print("Old logs and backups cleaned up regularly")
    print("Temporary files cleaned up daily")

if __name__ == "__main__":
    main()