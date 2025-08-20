#!/bin/bash

# Atlas Production Maintenance Script
# This script performs routine maintenance tasks for Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Maintenance..."

# Configuration
LOG_FILE="/home/ubuntu/dev/atlas/logs/maintenance.log"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $LOG_FILE)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $LOG_FILE
    echo "$1"
}

# Function to optimize database
optimize_database() {
    log_message "Starting database optimization"
    
    # Run VACUUM ANALYZE to optimize database performance
    if sudo -u postgres psql -U atlas_user -d atlas -c "VACUUM ANALYZE;"; then
        log_message "Database optimization completed successfully"
    else
        log_message "ERROR: Database optimization failed"
        return 1
    fi
    
    return 0
}

# Function to clean logs
clean_logs() {
    log_message "Starting log cleanup"
    
    # Clean Atlas logs older than 30 days
    local atlas_cleaned=0
    if [ -d "/home/ubuntu/dev/atlas/logs" ]; then
        for log_file in $(find /home/ubuntu/dev/atlas/logs -name "*.log" -mtime +30); do
            rm "$log_file"
            atlas_cleaned=$((atlas_cleaned + 1))
        done
        log_message "Cleaned $atlas_cleaned Atlas log files"
    fi
    
    # Clean system logs
    if command -v journalctl &> /dev/null; then
        if sudo journalctl --vacuum-time=30d; then
            log_message "System logs cleaned (older than 30 days)"
        else
            log_message "WARNING: Failed to clean system logs"
        fi
    fi
    
    return 0
}

# Function to clean temporary files
clean_temp_files() {
    log_message "Starting temporary file cleanup"
    
    # Clean temporary files older than 7 days
    local temp_cleaned=0
    for temp_file in $(find /tmp -type f -mtime +7 2>/dev/null); do
        rm "$temp_file"
        temp_cleaned=$((temp_cleaned + 1))
    done
    log_message "Cleaned $temp_cleaned temporary files"
    
    # Clean Atlas temporary files
    local atlas_temp_cleaned=0
    if [ -d "/home/ubuntu/dev/atlas/tmp" ]; then
        for temp_file in $(find /home/ubuntu/dev/atlas/tmp -type f -mtime +7 2>/dev/null); do
            rm "$temp_file"
            atlas_temp_cleaned=$((atlas_temp_cleaned + 1))
        done
        log_message "Cleaned $atlas_temp_cleaned Atlas temporary files"
    fi
    
    return 0
}

# Function to check and restart failed services
check_and_restart_services() {
    log_message "Checking and restarting failed services"
    
    # Services to check
    local services=("atlas" "atlas-prometheus" "atlas-grafana")
    local restarted_count=0
    
    for service in "${services[@]}"; do
        if ! systemctl is-active --quiet $service; then
            log_message "Restarting failed service: $service"
            if sudo systemctl restart $service; then
                log_message "Successfully restarted $service"
                restarted_count=$((restarted_count + 1))
            else
                log_message "ERROR: Failed to restart $service"
            fi
        fi
    done
    
    log_message "Restarted $restarted_count services"
    return 0
}

# Function to update system security packages
update_security_packages() {
    log_message "Updating security packages"
    
    # Update package list
    if sudo apt update; then
        log_message "Package list updated"
    else
        log_message "ERROR: Failed to update package list"
        return 1
    fi
    
    # Upgrade security packages only
    if sudo unattended-upgrade -d; then
        log_message "Security packages updated successfully"
    else
        log_message "WARNING: Security package update may have failed"
    fi
    
    return 0
}

# Function to check disk space and send alerts if needed
check_disk_space() {
    log_message "Checking disk space"
    
    local usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    if [ $usage -gt 90 ]; then
        log_message "CRITICAL: Disk usage is at ${usage}%"
        # In a real implementation, this would send an alert
        echo "🚨 CRITICAL: Disk usage is at ${usage}%"
    elif [ $usage -gt 80 ]; then
        log_message "WARNING: Disk usage is at ${usage}%"
        # In a real implementation, this would send an alert
        echo "⚠️ WARNING: Disk usage is at ${usage}%"
    else
        log_message "Disk usage is normal: ${usage}%"
    fi
    
    return 0
}

# Function to rotate logs
rotate_logs() {
    log_message "Rotating logs"
    
    # Force log rotation
    if sudo logrotate -f /etc/logrotate.conf; then
        log_message "Log rotation completed successfully"
    else
        log_message "WARNING: Log rotation may have failed"
    fi
    
    return 0
}

# Function to check SSL certificate expiration
check_ssl_certificate() {
    log_message "Checking SSL certificate expiration"
    
    # Check if SSL certificate exists
    if [ -f "/etc/letsencrypt/live/atlas.khamel.com/cert.pem" ]; then
        local expiry_date=$(openssl x509 -in /etc/letsencrypt/live/atlas.khamel.com/cert.pem -noout -enddate | cut -d= -f2)
        local expiry_seconds=$(date -d "$expiry_date" +%s)
        local current_seconds=$(date +%s)
        local days_until_expiry=$(( (expiry_seconds - current_seconds) / 86400 ))
        
        if [ $days_until_expiry -lt 0 ]; then
            log_message "CRITICAL: SSL certificate expired on $expiry_date"
            echo "🚨 CRITICAL: SSL certificate expired on $expiry_date"
        elif [ $days_until_expiry -lt 7 ]; then
            log_message "WARNING: SSL certificate expires in $days_until_expiry days ($expiry_date)"
            echo "⚠️ WARNING: SSL certificate expires in $days_until_expiry days ($expiry_date)"
        elif [ $days_until_expiry -lt 30 ]; then
            log_message "NOTICE: SSL certificate expires in $days_until_expiry days ($expiry_date)"
        else
            log_message "SSL certificate is valid for $days_until_expiry days"
        fi
    else
        log_message "WARNING: SSL certificate not found"
    fi
    
    return 0
}

# Function to retry failed articles
retry_failed_articles() {
    log_message "Retrying failed articles"
    
    # Run retry script if it exists
    if [ -f "/home/ubuntu/dev/atlas/retry_failed_articles.py" ]; then
        if python3 /home/ubuntu/dev/atlas/retry_failed_articles.py; then
            log_message "Failed articles retry process completed"
        else
            log_message "WARNING: Failed articles retry process may have failed"
        fi
    else
        log_message "NOTICE: Retry script not found"
    fi
    
    return 0
}

# Main maintenance function
main() {
    log_message "=== Starting Atlas Maintenance Process ==="
    
    # Start time
    local start_time=$(date)
    log_message "Maintenance process started at: $start_time"
    
    # Perform maintenance tasks
    local tasks=(
        "optimize_database"
        "clean_logs"
        "clean_temp_files"
        "check_and_restart_services"
        "update_security_packages"
        "check_disk_space"
        "rotate_logs"
        "check_ssl_certificate"
        "retry_failed_articles"
    )
    
    local failed_tasks=0
    
    for task in "${tasks[@]}"; do
        log_message "Executing task: $task"
        if ! $task; then
            log_message "ERROR: Task $task failed"
            failed_tasks=$((failed_tasks + 1))
        fi
    done
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Maintenance process completed at: $end_time (Duration: ${duration}s)"
    
    if [ $failed_tasks -eq 0 ]; then
        log_message "=== Maintenance Process Completed Successfully ==="
        echo "✅ Atlas maintenance completed successfully"
        return 0
    else
        log_message "=== Maintenance Process Completed with $failed_tasks failures ==="
        echo "⚠️ Atlas maintenance completed with $failed_tasks failures"
        return 1
    fi
}

# Run main function
if main; then
    exit 0
else
    exit 1
fi