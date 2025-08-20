#!/bin/bash

# Atlas Production Monitoring Script
# This script continuously monitors Atlas production environment and sends alerts

set -e  # Exit on any error

echo "Starting Atlas Production Monitoring..."

# Configuration
ALERT_EMAIL="admin@khamel.com"
LOG_FILE="/home/ubuntu/dev/atlas/logs/monitoring.log"
CHECK_INTERVAL=60  # seconds

# Function to send alert
send_alert() {
    local subject=$1
    local message=$2
    
    echo "$(date): ALERT - $subject" >> $LOG_FILE
    echo "$message" >> $LOG_FILE
    
    # In a real implementation, this would send an email
    # For now, we'll just log to file
    echo "🚨 ALERT: $subject"
    echo "$message"
}

# Function to check service status
check_service_status() {
    local service=$1
    local name=$2
    
    if ! systemctl is-active --quiet $service; then
        send_alert "Service Down" "$name service is not running"
        return 1
    fi
    return 0
}

# Function to check disk space
check_disk_space() {
    local usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    if [ $usage -gt 90 ]; then
        send_alert "Disk Space Critical" "Disk usage is at ${usage}%"
        return 1
    elif [ $usage -gt 80 ]; then
        send_alert "Disk Space Warning" "Disk usage is at ${usage}%"
        return 1
    fi
    return 0
}

# Function to check memory usage
check_memory_usage() {
    local usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    
    if [ $usage -gt 90 ]; then
        send_alert "Memory Usage Critical" "Memory usage is at ${usage}%"
        return 1
    elif [ $usage -gt 80 ]; then
        send_alert "Memory Usage Warning" "Memory usage is at ${usage}%"
        return 1
    fi
    return 0
}

# Function to check database connectivity
check_database() {
    if ! sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        send_alert "Database Connection Failed" "Cannot connect to Atlas database"
        return 1
    fi
    return 0
}

# Function to check web service
check_web_service() {
    if ! curl -f -s http://localhost:5000/health > /dev/null 2>&1; then
        # Try alternative health check
        if ! curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
            send_alert "Web Service Unreachable" "Atlas web service is not responding"
            return 1
        fi
    fi
    return 0
}

# Function to check backup status
check_backup_status() {
    # Check if backup directory exists
    if [ ! -d "/home/ubuntu/dev/atlas/backups" ]; then
        send_alert "Backup Directory Missing" "Backup directory not found"
        return 1
    fi
    
    # Check if recent backups exist
    local backup_count=$(find /home/ubuntu/dev/atlas/backups -name "*.sql*" -mtime -2 | wc -l)
    if [ $backup_count -eq 0 ]; then
        send_alert "No Recent Backups" "No backups created in the last 2 days"
        return 1
    fi
    return 0
}

# Function to check SSL certificate
check_ssl_certificate() {
    # Check if SSL certificate exists and is valid
    if [ -f "/etc/letsencrypt/live/atlas.khamel.com/cert.pem" ]; then
        local expiry_date=$(openssl x509 -in /etc/letsencrypt/live/atlas.khamel.com/cert.pem -noout -enddate | cut -d= -f2)
        local expiry_seconds=$(date -d "$expiry_date" +%s)
        local current_seconds=$(date +%s)
        local days_until_expiry=$(( (expiry_seconds - current_seconds) / 86400 ))
        
        if [ $days_until_expiry -lt 0 ]; then
            send_alert "SSL Certificate Expired" "SSL certificate expired on $expiry_date"
            return 1
        elif [ $days_until_expiry -lt 7 ]; then
            send_alert "SSL Certificate Expiring Soon" "SSL certificate expires in $days_until_expiry days"
            return 1
        fi
    fi
    return 0
}

# Main monitoring loop
echo "$(date): Starting Atlas monitoring loop" >> $LOG_FILE

while true; do
    echo "$(date): Running monitoring checks" >> $LOG_FILE
    
    # Perform all checks
    check_service_status "atlas" "Atlas Main Service"
    check_service_status "postgresql" "PostgreSQL Database"
    check_service_status "nginx" "Nginx Web Server"
    check_disk_space
    check_memory_usage
    check_database
    check_web_service
    check_backup_status
    check_ssl_certificate
    
    # Wait before next check
    sleep $CHECK_INTERVAL
done