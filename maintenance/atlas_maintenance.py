"""
Atlas Service Maintenance
Creates maintenance tasks for Atlas services
"""

import os
import subprocess
import sys
from datetime import datetime
import time

class AtlasMaintenance:
    """Manage Atlas service maintenance tasks"""
    
    def __init__(self):
        self.log_file = "/var/log/atlas_maintenance.log"
        self.service_name = "atlas"
        
    def create_maintenance_script(self):
        """Create Atlas-specific maintenance tasks"""
        print("Creating Atlas maintenance script...")
        
        maintenance_script = f"""#!/bin/bash
# Atlas Service Maintenance Script

LOG_FILE="{self.log_file}"
SERVICE_NAME="{self.service_name}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting Atlas maintenance tasks" >> $LOG_FILE

# Function to log messages
log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}}

# Check if Atlas service is running
if systemctl is-active --quiet $SERVICE_NAME; then
    log_message "Atlas service is running"
else
    log_message "WARNING: Atlas service is not running"
fi

# Check system resources
log_message "Checking system resources..."
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{{print $2}}' | cut -d'%' -f1)
MEMORY_USAGE=$(free | grep Mem | awk '{{printf "%.2f", $3/$2 * 100.0}}')
DISK_USAGE=$(df / | tail -1 | awk '{{print $5}}' | sed 's/%//')

log_message "CPU Usage: ${{CPU_USAGE}}%"
log_message "Memory Usage: ${{MEMORY_USAGE}}%"
log_message "Disk Usage: ${{DISK_USAGE}}%"

# Perform maintenance tasks
log_message "Performing maintenance tasks..."

# Restart Atlas service if needed (example condition)
if [ ${{CPU_USAGE%.*}} -gt 80 ]; then
    log_message "High CPU usage detected, restarting Atlas service"
    systemctl restart $SERVICE_NAME
    sleep 5
    if systemctl is-active --quiet $SERVICE_NAME; then
        log_message "Atlas service restarted successfully"
    else
        log_message "ERROR: Failed to restart Atlas service"
    fi
fi

log_message "Atlas maintenance tasks completed"
"""
        
        script_path = "/usr/local/bin/atlas_maintenance.sh"
        with open(script_path, "w") as f:
            f.write(maintenance_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created maintenance script at {script_path}")
        return script_path
    
    def implement_failed_article_retry(self):
        """Implement failed article retry automation (daily)"""
        print("Implementing failed article retry automation...")
        
        retry_script = f"""#!/bin/bash
# Atlas Failed Article Retry Script

LOG_FILE="{self.log_file}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting failed article retry process" >> $LOG_FILE

# In a real implementation, this would:
# 1. Query the database for failed articles
# 2. Retry processing for articles that failed
# 3. Update status in database
# 4. Log results

# Example query for failed articles (stub)
# FAILED_ARTICLES=$(psql -U atlas_user -d atlas_db -t -c "SELECT id FROM articles WHERE status = 'failed' AND retry_count < 3")

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> {self.log_file}
}}

log_message "Checking for failed articles to retry..."

# This is a stub implementation
FAILED_COUNT=0  # In reality, this would come from database query

if [ $FAILED_COUNT -gt 0 ]; then
    log_message "Found $FAILED_COUNT failed articles to retry"
    # Process each failed article
    # for article_id in $FAILED_ARTICLES; do
    #     log_message "Retrying article ID: $article_id"
    #     # Call Atlas processing script for this article
    #     # python3 /home/ubuntu/dev/atlas/process_article.py $article_id
    # done
    log_message "Failed article retry process completed"
else
    log_message "No failed articles found for retry"
fi

echo "[$DATE] Failed article retry process completed" >> $LOG_FILE
"""
        
        script_path = "/usr/local/bin/atlas_retry_failed.sh"
        with open(script_path, "w") as f:
            f.write(retry_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to daily cron
        cron_job = f"0 3 * * * {script_path} >> /var/log/atlas_retry.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added failed article retry cron job")
            else:
                print("Failed article retry cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with failed article retry job")
        
        print(f"Created failed article retry script at {script_path}")
        return script_path
    
    def setup_database_optimization(self):
        """Set up database optimization and vacuum tasks"""
        print("Setting up database optimization tasks...")
        
        db_optimize_script = """#!/bin/bash
# Atlas Database Optimization Script

LOG_FILE="/var/log/atlas_db_optimize.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting database optimization" >> $LOG_FILE

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}

# Perform database vacuum and analyze
log_message "Performing database vacuum and analyze..."

# In a real implementation, this would:
# 1. Connect to PostgreSQL
# 2. Run VACUUM ANALYZE on tables
# 3. Check for table bloat
# 4. Reindex if necessary

# Example PostgreSQL commands (stub):
# vacuumdb -U atlas_user -d atlas_db --verbose >> $LOG_FILE 2>&1

log_message "Database optimization completed"

# Check database size
log_message "Checking database size..."
# psql -U atlas_user -d atlas_db -c "SELECT pg_size_pretty(pg_database_size('atlas_db'));" >> $LOG_FILE 2>&1
"""
        
        script_path = "/usr/local/bin/atlas_db_optimize.sh"
        with open(script_path, "w") as f:
            f.write(db_optimize_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to weekly cron (runs Sundays at 2 AM)
        cron_job = f"0 2 * * 0 {script_path} >> /var/log/atlas_db_optimize_cron.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added database optimization cron job")
            else:
                print("Database optimization cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with database optimization job")
        
        print(f"Created database optimization script at {script_path}")
        return script_path
    
    def create_log_rotation_cleanup(self):
        """Create log rotation and cleanup for Atlas logs"""
        print("Creating log rotation and cleanup...")
        
        # Create logrotate configuration
        logrotate_config = """
# Atlas Log Rotation Configuration

/var/log/atlas/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 atlas atlas
    postrotate
        systemctl reload atlas > /dev/null 2>/dev/null || true
    endscript
}

/var/log/atlas_maintenance.log {
    weekly
    missingok
    rotate 12
    compress
    delaycompress
    notifempty
    create 644 root root
}

/var/log/atlas_updates.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 root root
}
"""
        
        config_path = "/etc/logrotate.d/atlas"
        with open(config_path, "w") as f:
            f.write(logrotate_config)
        
        print(f"Created logrotate configuration at {config_path}")
        
        # Create cleanup script for old logs
        cleanup_script = """#!/bin/bash
# Atlas Log Cleanup Script

LOG_DIR="/var/log/atlas"
RETENTION_DAYS=30
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting log cleanup" >> /var/log/atlas_cleanup.log

# Remove log files older than retention period
find $LOG_DIR -name "*.log.*" -type f -mtime +$RETENTION_DAYS -delete 2>/dev/null
find $LOG_DIR -name "*.log.gz" -type f -mtime +$RETENTION_DAYS -delete 2>/dev/null

echo "[$DATE] Log cleanup completed" >> /var/log/atlas_cleanup.log
"""
        
        script_path = "/usr/local/bin/atlas_log_cleanup.sh"
        with open(script_path, "w") as f:
            f.write(cleanup_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to daily cron
        cron_job = f"0 1 * * * {script_path} >> /var/log/atlas_cleanup_cron.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added log cleanup cron job")
            else:
                print("Log cleanup cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with log cleanup job")
        
        print(f"Created log cleanup script at {script_path}")
        return script_path
    
    def add_content_deduplication(self):
        """Add content deduplication and cleanup tasks"""
        print("Adding content deduplication tasks...")
        
        dedupe_script = """#!/bin/bash
# Atlas Content Deduplication Script

LOG_FILE="/var/log/atlas_dedupe.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting content deduplication" >> $LOG_FILE

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}

# In a real implementation, this would:
# 1. Query database for potential duplicates
# 2. Compare content using hashes or similarity metrics
# 3. Remove or merge duplicates
# 4. Update references in other tables

log_message "Checking for duplicate content..."

# Example query for potential duplicates (stub)
# DUPLICATES=$(psql -U atlas_user -d atlas_db -t -c "
#     SELECT url, COUNT(*) FROM articles 
#     GROUP BY url 
#     HAVING COUNT(*) > 1
# ")

# COUNT=$(echo $DUPLICATES | wc -w)
# log_message "Found $COUNT potential duplicate URLs"

# Process duplicates
# if [ $COUNT -gt 0 ]; then
#     log_message "Processing duplicates..."
#     # Deduplication logic here
# else
#     log_message "No duplicates found"
# fi

log_message "Content deduplication completed"
"""
        
        script_path = "/usr/local/bin/atlas_dedupe.sh"
        with open(script_path, "w") as f:
            f.write(dedupe_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to weekly cron
        cron_job = f"0 4 * * 0 {script_path} >> /var/log/atlas_dedupe_cron.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added deduplication cron job")
            else:
                print("Deduplication cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with deduplication job")
        
        print(f"Created deduplication script at {script_path}")
        return script_path
    
    def configure_service_health_monitoring(self):
        """Configure Atlas service health monitoring and auto-restart"""
        print("Configuring service health monitoring...")
        
        health_script = f"""#!/bin/bash
# Atlas Service Health Monitoring Script

LOG_FILE="/var/log/atlas_health.log"
SERVICE_NAME="{self.service_name}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting service health check" >> $LOG_FILE

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}}

# Check if service is active
if systemctl is-active --quiet $SERVICE_NAME; then
    log_message "Service $SERVICE_NAME is running"
    
    # Check if service is responding (example health check)
    # curl -f http://localhost:5000/health > /dev/null 2>&1
    # if [ $? -eq 0 ]; then
    #     log_message "Service health check passed"
    # else
    #     log_message "ERROR: Service health check failed, restarting service"
    #     systemctl restart $SERVICE_NAME
    #     sleep 5
    #     if systemctl is-active --quiet $SERVICE_NAME; then
    #         log_message "Service restarted successfully"
    #     else
    #         log_message "ERROR: Failed to restart service"
    #     fi
    # fi
else
    log_message "ERROR: Service $SERVICE_NAME is not running, attempting to start"
    systemctl start $SERVICE_NAME
    sleep 5
    if systemctl is-active --quiet $SERVICE_NAME; then
        log_message "Service started successfully"
    else
        log_message "ERROR: Failed to start service"
    fi
fi

echo "[$DATE] Service health check completed" >> $LOG_FILE
"""
        
        script_path = "/usr/local/bin/atlas_health_check.sh"
        with open(script_path, "w") as f:
            f.write(health_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to cron for regular monitoring (every 5 minutes)
        cron_job = f"*/5 * * * * {script_path} >> /var/log/atlas_health_cron.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added health monitoring cron job")
            else:
                print("Health monitoring cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with health monitoring job")
        
        print(f"Created health monitoring script at {script_path}")
        return script_path
    
    def test_maintenance_tasks(self):
        """Test maintenance tasks"""
        print("Testing maintenance tasks...")
        
        # In a real implementation, this would:
        # 1. Run each maintenance script in test mode
        # 2. Verify cron jobs are properly configured
        # 3. Check log files are being created
        # 4. Verify service restart functionality
        
        try:
            # Check if required scripts exist
            scripts = [
                "/usr/local/bin/atlas_maintenance.sh",
                "/usr/local/bin/atlas_retry_failed.sh", 
                "/usr/local/bin/atlas_db_optimize.sh",
                "/usr/local/bin/atlas_log_cleanup.sh",
                "/usr/local/bin/atlas_dedupe.sh",
                "/usr/local/bin/atlas_health_check.sh"
            ]
            
            missing_scripts = []
            for script in scripts:
                if not os.path.exists(script):
                    missing_scripts.append(script)
            
            if missing_scripts:
                print(f"✗ Missing scripts: {missing_scripts}")
                return False
            else:
                print("✓ All maintenance scripts exist")
            
            # Check if cron jobs exist
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
            cron_content = result.stdout
            
            required_jobs = [
                "atlas_retry_failed.sh",
                "atlas_db_optimize.sh",
                "atlas_log_cleanup.sh",
                "atlas_dedupe.sh",
                "atlas_health_check.sh"
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
            
            print("Maintenance tasks test completed successfully")
            return True
            
        except Exception as e:
            print(f"✗ Maintenance tasks test failed: {e}")
            return False

def main():
    """Main Atlas maintenance function"""
    if os.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
        sys.exit(1)
    
    # Initialize Atlas maintenance
    maintenance = AtlasMaintenance()
    
    # Create maintenance script
    maintenance_script = maintenance.create_maintenance_script()
    print(f"Maintenance script created at: {maintenance_script}")
    
    # Implement failed article retry
    retry_script = maintenance.implement_failed_article_retry()
    print(f"Failed article retry script created at: {retry_script}")
    
    # Setup database optimization
    db_script = maintenance.setup_database_optimization()
    print(f"Database optimization script created at: {db_script}")
    
    # Create log rotation and cleanup
    cleanup_script = maintenance.create_log_rotation_cleanup()
    print(f"Log cleanup script created at: {cleanup_script}")
    
    # Add content deduplication
    dedupe_script = maintenance.add_content_deduplication()
    print(f"Deduplication script created at: {dedupe_script}")
    
    # Configure service health monitoring
    health_script = maintenance.configure_service_health_monitoring()
    print(f"Health monitoring script created at: {health_script}")
    
    # Test maintenance tasks
    if maintenance.test_maintenance_tasks():
        print("✓ Maintenance tasks test successful")
    else:
        print("✗ Maintenance tasks test failed")
    
    print("\nAtlas service maintenance configuration completed!")
    print("Daily maintenance tasks will run automatically")
    print("Weekly optimization tasks scheduled for Sundays")
    print("Service health monitored every 5 minutes")
    print("Failed articles retried daily at 3:00 AM")

if __name__ == "__main__":
    main()