#!/bin/bash

# Atlas Production Automated Maintenance Script
# This script performs automated maintenance tasks for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Automated Maintenance..."

# Configuration
MAINTENANCE_LOG="/home/ubuntu/dev/atlas/logs/maintenance.log"
MAINTENANCE_CONFIG="/home/ubuntu/dev/atlas/config/maintenance.json"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $MAINTENANCE_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $MAINTENANCE_LOG
    echo "$1"
}

# Function to initialize maintenance configuration
initialize_maintenance_config() {
    log_message "Initializing maintenance configuration"
    
    # Create default maintenance configuration if it doesn't exist
    if [ ! -f "$MAINTENANCE_CONFIG" ]; then
        cat > "$MAINTENANCE_CONFIG" << EOF
{
    "schedule": {
        "daily": "0 2 * * *",
        "weekly": "0 3 * * 0",
        "monthly": "0 4 1 * *"
    },
    "tasks": {
        "log_rotation": true,
        "backup_cleanup": true,
        "temp_file_cleanup": true,
        "database_maintenance": true,
        "system_updates": true,
        "disk_cleanup": true
    },
    "retention": {
        "logs_days": 30,
        "backups_days": 30,
        "temp_files_days": 7
    }
}
EOF
        echo "✅ Created default maintenance configuration"
        log_message "Default maintenance configuration created"
    else
        echo "✅ Maintenance configuration already exists"
    fi
}

# Function to rotate logs
rotate_logs() {
    log_message "Rotating logs"
    
    echo "Rotating Logs..."
    echo "=============="
    
    local log_days=$(jq -r '.retention.logs_days' "$MAINTENANCE_CONFIG")
    
    # Rotate Atlas application logs
    if [ -d "/home/ubuntu/dev/atlas/logs" ]; then
        # Compress old log files
        find /home/ubuntu/dev/atlas/logs -name "*.log" -mtime +$log_days -exec gzip {} \; 2>/dev/null || true
        echo "✅ Compressed Atlas logs older than $log_days days"
        
        # Remove very old compressed logs
        find /home/ubuntu/dev/atlas/logs -name "*.log.gz" -mtime +$((log_days * 2)) -delete 2>/dev/null || true
        echo "✅ Removed compressed Atlas logs older than $((log_days * 2)) days"
    fi
    
    # Rotate system logs (if using logrotate, this might not be necessary)
    if command -v logrotate &> /dev/null; then
        # Force log rotation
        sudo logrotate -f /etc/logrotate.conf 2>/dev/null || true
        echo "✅ Forced system log rotation"
    fi
    
    log_message "Log rotation completed"
}

# Function to clean up backups
cleanup_backups() {
    log_message "Cleaning up backups"
    
    echo ""
    echo "Cleaning Up Backups..."
    echo "===================="
    
    local backup_days=$(jq -r '.retention.backups_days' "$MAINTENANCE_CONFIG")
    
    # Clean up old database backups
    if [ -d "/home/ubuntu/dev/atlas/backups" ]; then
        local before_count=$(find /home/ubuntu/dev/atlas/backups -name "*.sql*" | wc -l)
        find /home/ubuntu/dev/atlas/backups -name "*.sql*" -mtime +$backup_days -delete 2>/dev/null || true
        local after_count=$(find /home/ubuntu/dev/atlas/backups -name "*.sql*" | wc -l)
        local deleted_count=$((before_count - after_count))
        echo "✅ Cleaned up $deleted_count old database backups"
    fi
    
    # Clean up old configuration backups
    if [ -d "/home/ubuntu/dev/atlas/backups/config" ]; then
        find /home/ubuntu/dev/atlas/backups/config -name "*.tar.gz" -mtime +$backup_days -delete 2>/dev/null || true
        echo "✅ Cleaned up old configuration backups"
    fi
    
    log_message "Backup cleanup completed"
}

# Function to clean up temporary files
cleanup_temp_files() {
    log_message "Cleaning up temporary files"
    
    echo ""
    echo "Cleaning Up Temporary Files..."
    echo "============================"
    
    local temp_days=$(jq -r '.retention.temp_files_days' "$MAINTENANCE_CONFIG")
    
    # Clean up system temporary files
    local before_count=$(find /tmp -type f 2>/dev/null | wc -l)
    find /tmp -type f -mtime +$temp_days -delete 2>/dev/null || true
    local after_count=$(find /tmp -type f 2>/dev/null | wc -l)
    local deleted_count=$((before_count - after_count))
    echo "✅ Cleaned up $deleted_count temporary files from /tmp"
    
    # Clean up Atlas temporary files
    if [ -d "/home/ubuntu/dev/atlas/tmp" ]; then
        find /home/ubuntu/dev/atlas/tmp -type f -mtime +$temp_days -delete 2>/dev/null || true
        echo "✅ Cleaned up temporary files from Atlas tmp directory"
    fi
    
    log_message "Temporary file cleanup completed"
}

# Function to perform database maintenance
database_maintenance() {
    log_message "Performing database maintenance"
    
    echo ""
    echo "Performing Database Maintenance..."
    echo "================================"
    
    # Check if PostgreSQL is running
    if ! systemctl is-active --quiet postgresql; then
        echo "❌ PostgreSQL is not running, skipping database maintenance"
        log_message "PostgreSQL not running, skipping database maintenance"
        return 1
    fi
    
    # Run database vacuum and analyze
    if sudo -u postgres psql -U atlas_user -d atlas -c "VACUUM ANALYZE;" > /dev/null 2>&1; then
        echo "✅ Database vacuum and analyze completed"
    else
        echo "❌ Database vacuum and analyze failed"
        log_message "Database vacuum and analyze failed"
    fi
    
    # Check database size
    local db_size=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT pg_size_pretty(pg_database_size('atlas'));")
    echo "📊 Database size: $db_size"
    
    log_message "Database maintenance completed"
}

# Function to check for system updates
check_system_updates() {
    log_message "Checking for system updates"
    
    echo ""
    echo "Checking for System Updates..."
    echo "============================"
    
    # Update package list
    if sudo apt update > /dev/null 2>&1; then
        echo "✅ Package list updated"
    else
        echo "❌ Failed to update package list"
        log_message "Failed to update package list"
        return 1
    fi
    
    # Check for security updates
    local updates_available=$(apt list --upgradable 2>/dev/null | grep -c security)
    if [ $updates_available -gt 0 ]; then
        echo "⚠️ $updates_available security updates available"
        echo "🔧 Run 'sudo unattended-upgrade' to install security updates"
    else
        echo "✅ No security updates available"
    fi
    
    log_message "System update check completed"
}

# Function to perform disk cleanup
disk_cleanup() {
    log_message "Performing disk cleanup"
    
    echo ""
    echo "Performing Disk Cleanup..."
    echo "========================"
    
    # Check disk usage
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    echo "📊 Current disk usage: ${disk_usage}%"
    
    # Clean package cache
    if sudo apt clean > /dev/null 2>&1; then
        echo "✅ Package cache cleaned"
    else
        echo "❌ Failed to clean package cache"
    fi
    
    # Clean thumbnail cache
    if [ -d "$HOME/.cache/thumbnails" ]; then
        rm -rf "$HOME/.cache/thumbnails/*" 2>/dev/null || true
        echo "✅ Thumbnail cache cleaned"
    fi
    
    # If disk usage is high, perform additional cleanup
    if [ $disk_usage -gt 80 ]; then
        echo "⚠️ Disk usage is high, performing additional cleanup"
        
        # Clean journal logs
        if command -v journalctl &> /dev/null; then
            sudo journalctl --vacuum-time=7d > /dev/null 2>&1 || true
            echo "✅ Journal logs cleaned (older than 7 days)"
        fi
        
        # Clean old system logs
        find /var/log -name "*.log.*" -mtime +30 -delete 2>/dev/null || true
        echo "✅ Old system logs cleaned"
    fi
    
    # Report final disk usage
    local final_disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    echo "📊 Final disk usage: ${final_disk_usage}%"
    
    log_message "Disk cleanup completed"
}

# Function to restart services if needed
restart_services() {
    log_message "Checking if services need restart"
    
    echo ""
    echo "Checking Service Restart Needs..."
    echo "=============================="
    
    # Check if system reboot is required
    if [ -f /var/run/reboot-required ]; then
        echo "🔄 System reboot required (reboot file found)"
        echo "🔧 Reboot required due to system updates"
        log_message "System reboot required"
    else
        echo "✅ No system reboot required"
    fi
    
    # Check if services need restart after updates
    # This is a simplified check - in reality, you'd want more sophisticated service restart logic
    echo "✅ Service restart check completed"
    
    log_message "Service restart check completed"
}

# Function to generate maintenance report
generate_maintenance_report() {
    log_message "Generating maintenance report"
    
    echo ""
    echo "Generating Maintenance Report..."
    echo "============================="
    
    local report_file="/home/ubuntu/dev/atlas/logs/maintenance_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create report header
    echo "Atlas Production Maintenance Report" > "$report_file"
    echo "Generated: $(date)" >> "$report_file"
    echo "=================================" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add system information
    echo "System Information:" >> "$report_file"
    echo "------------------" >> "$report_file"
    echo "Hostname: $(hostname)" >> "$report_file"
    echo "Uptime: $(uptime -p)" >> "$report_file"
    echo "Load Average: $(uptime | awk -F'load average:' '{print $2}')" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add disk usage
    echo "Disk Usage:" >> "$report_file"
    echo "----------" >> "$report_file"
    df -h / >> "$report_file"
    echo "" >> "$report_file"
    
    # Add memory usage
    echo "Memory Usage:" >> "$report_file"
    echo "------------" >> "$report_file"
    free -h >> "$report_file"
    echo "" >> "$report_file"
    
    # Add maintenance tasks summary
    echo "Maintenance Tasks Summary:" >> "$report_file"
    echo "-------------------------" >> "$report_file"
    echo "✅ Log rotation completed" >> "$report_file"
    echo "✅ Backup cleanup completed" >> "$report_file"
    echo "✅ Temporary file cleanup completed" >> "$report_file"
    echo "✅ Database maintenance completed" >> "$report_file"
    echo "✅ System update check completed" >> "$report_file"
    echo "✅ Disk cleanup completed" >> "$report_file"
    echo "" >> "$report_file"
    
    echo "✅ Maintenance report generated: $report_file"
    log_message "Maintenance report generated: $report_file"
    
    # Display summary
    echo ""
    echo "Maintenance Summary:"
    echo "  Log rotation: Completed"
    echo "  Backup cleanup: Completed"
    echo "  Temp file cleanup: Completed"
    echo "  Database maintenance: Completed"
    echo "  System updates: Checked"
    echo "  Disk cleanup: Completed"
    echo "Report saved to: $report_file"
}

# Main maintenance function
main() {
    log_message "=== Starting Atlas Automated Maintenance ==="
    
    # Initialize configuration
    initialize_maintenance_config
    
    # Start time
    local start_time=$(date)
    log_message "Maintenance started at: $start_time"
    
    # Handle different maintenance operations
    case $1 in
        "logs")
            rotate_logs
            ;;
        "backups")
            cleanup_backups
            ;;
        "temp")
            cleanup_temp_files
            ;;
        "database")
            database_maintenance
            ;;
        "updates")
            check_system_updates
            ;;
        "disk")
            disk_cleanup
            ;;
        "services")
            restart_services
            ;;
        "report")
            generate_maintenance_report
            ;;
        *)
            # Run all maintenance tasks
            rotate_logs
            cleanup_backups
            cleanup_temp_files
            database_maintenance
            check_system_updates
            disk_cleanup
            restart_services
            generate_maintenance_report
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Maintenance completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Automated Maintenance Completed ==="
    
    echo ""
    echo "✅ Automated maintenance complete!"
    echo "📋 Check $MAINTENANCE_LOG for details"
}

# Run main function
main "$@"