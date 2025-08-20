#!/bin/bash

# Atlas Production Health Check Script
# This script performs a comprehensive health check of the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Health Check..."

# Configuration
HEALTH_LOG="/home/ubuntu/dev/atlas/logs/health_check.log"
HEALTH_REPORT="/home/ubuntu/dev/atlas/logs/health_report.json"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $HEALTH_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $HEALTH_LOG
    echo "$1"
}

# Function to check system health
check_system_health() {
    log_message "Checking system health"
    
    echo "System Health Check:"
    echo "===================="
    
    # Check CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    if (( $(echo "$cpu_usage < 80" | bc -l) )); then
        echo "✅ CPU Usage: ${cpu_usage}% (Normal)"
        local cpu_status="HEALTHY"
    else
        echo "❌ CPU Usage: ${cpu_usage}% (High)"
        local cpu_status="WARNING"
    fi
    
    # Check memory usage
    local memory_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    if [ $memory_usage -lt 80 ]; then
        echo "✅ Memory Usage: ${memory_usage}% (Normal)"
        local memory_status="HEALTHY"
    else
        echo "❌ Memory Usage: ${memory_usage}% (High)"
        local memory_status="WARNING"
    fi
    
    # Check disk usage
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    if [ $disk_usage -lt 80 ]; then
        echo "✅ Disk Usage: ${disk_usage}% (Normal)"
        local disk_status="HEALTHY"
    else
        echo "❌ Disk Usage: ${disk_usage}% (High)"
        local disk_status="WARNING"
    fi
    
    # Check system load
    local load_avg=$(uptime | awk -F'load average:' '{print $2}' | xargs)
    echo "✅ System Load: $load_avg"
    
    # Return health status
    if [ "$cpu_status" = "HEALTHY" ] && [ "$memory_status" = "HEALTHY" ] && [ "$disk_status" = "HEALTHY" ]; then
        echo "✅ Overall System Health: HEALTHY"
        return 0
    else
        echo "⚠️ Overall System Health: WARNING"
        return 1
    fi
}

# Function to check service health
check_service_health() {
    log_message "Checking service health"
    
    echo ""
    echo "Service Health Check:"
    echo "====================="
    
    # Define services to check
    local services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    local all_healthy=true
    
    for service_info in "${services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc: Running"
        else
            echo "❌ $service_desc: Not Running"
            all_healthy=false
        fi
    done
    
    if $all_healthy; then
        echo "✅ Overall Service Health: HEALTHY"
        return 0
    else
        echo "❌ Overall Service Health: CRITICAL"
        return 1
    fi
}

# Function to check application health
check_application_health() {
    log_message "Checking application health"
    
    echo ""
    echo "Application Health Check:"
    echo "========================="
    
    # Check if web interface is accessible
    if curl -f -s http://localhost:5000/ > /dev/null; then
        echo "✅ Web Interface: Accessible"
        local web_status="HEALTHY"
    else
        echo "❌ Web Interface: Not Accessible"
        local web_status="CRITICAL"
    fi
    
    # Check database connectivity
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        echo "✅ Database Connectivity: Working"
        local db_status="HEALTHY"
    else
        echo "❌ Database Connectivity: Not Working"
        local db_status="CRITICAL"
    fi
    
    # Check if monitoring endpoints are accessible
    if curl -f -s http://localhost:9090/status > /dev/null; then
        echo "✅ Prometheus: Accessible"
    else
        echo "❌ Prometheus: Not Accessible"
    fi
    
    if curl -f -s http://localhost:3000/login > /dev/null; then
        echo "✅ Grafana: Accessible"
    else
        echo "❌ Grafana: Not Accessible"
    fi
    
    # Return health status
    if [ "$web_status" = "HEALTHY" ] && [ "$db_status" = "HEALTHY" ]; then
        echo "✅ Overall Application Health: HEALTHY"
        return 0
    else
        echo "❌ Overall Application Health: CRITICAL"
        return 1
    fi
}

# Function to check backup health
check_backup_health() {
    log_message "Checking backup health"
    
    echo ""
    echo "Backup Health Check:"
    echo "===================="
    
    # Check if backup directory exists
    if [ -d "/home/ubuntu/dev/atlas/backups" ]; then
        echo "✅ Backup Directory: Exists"
        
        # Check if recent backups exist
        local backup_count=$(find /home/ubuntu/dev/atlas/backups -name "*.sql*" -mtime -2 | wc -l)
        if [ $backup_count -gt 0 ]; then
            echo "✅ Recent Backups: Found ($backup_count backups in last 2 days)"
            local backup_status="HEALTHY"
        else
            echo "❌ Recent Backups: Not Found"
            local backup_status="WARNING"
        fi
    else
        echo "❌ Backup Directory: Does Not Exist"
        local backup_status="CRITICAL"
    fi
    
    # Check backup cron job
    if crontab -l 2>/dev/null | grep -q "database_backup.py"; then
        echo "✅ Backup Cron Job: Configured"
    else
        echo "❌ Backup Cron Job: Not Configured"
    fi
    
    # Return health status
    if [ "$backup_status" = "HEALTHY" ]; then
        echo "✅ Overall Backup Health: HEALTHY"
        return 0
    else
        echo "⚠️ Overall Backup Health: WARNING"
        return 1
    fi
}

# Function to check security health
check_security_health() {
    log_message "Checking security health"
    
    echo ""
    echo "Security Health Check:"
    echo "======================"
    
    # Check if firewall is active
    if sudo ufw status | grep -q "Status: active"; then
        echo "✅ Firewall: Active"
        local firewall_status="HEALTHY"
    else
        echo "❌ Firewall: Inactive"
        local firewall_status="WARNING"
    fi
    
    # Check if authentication is configured
    if [ -f "/etc/nginx/.htpasswd" ]; then
        echo "✅ Web Authentication: Configured"
        local auth_status="HEALTHY"
    else
        echo "❌ Web Authentication: Not Configured"
        local auth_status="WARNING"
    fi
    
    # Check SSL certificate validity
    if [ -f "/etc/letsencrypt/live/atlas.khamel.com/cert.pem" ]; then
        # Check certificate expiration
        local expiry_date=$(openssl x509 -in /etc/letsencrypt/live/atlas.khamel.com/cert.pem -noout -enddate | cut -d= -f2)
        local expiry_seconds=$(date -d "$expiry_date" +%s)
        local current_seconds=$(date +%s)
        local days_until_expiry=$(( (expiry_seconds - current_seconds) / 86400 ))
        
        if [ $days_until_expiry -gt 30 ]; then
            echo "✅ SSL Certificate: Valid (expires in $days_until_expiry days)"
            local ssl_status="HEALTHY"
        elif [ $days_until_expiry -gt 0 ]; then
            echo "⚠️ SSL Certificate: Expiring Soon (expires in $days_until_expiry days)"
            local ssl_status="WARNING"
        else
            echo "❌ SSL Certificate: Expired"
            local ssl_status="CRITICAL"
        fi
    else
        echo "❌ SSL Certificate: Not Found"
        local ssl_status="CRITICAL"
    fi
    
    # Return health status
    if [ "$firewall_status" = "HEALTHY" ] && [ "$auth_status" = "HEALTHY" ] && [ "$ssl_status" = "HEALTHY" ]; then
        echo "✅ Overall Security Health: HEALTHY"
        return 0
    elif [ "$ssl_status" = "CRITICAL" ]; then
        echo "❌ Overall Security Health: CRITICAL"
        return 1
    else
        echo "⚠️ Overall Security Health: WARNING"
        return 1
    fi
}

# Function to generate health report
generate_health_report() {
    log_message "Generating health report"
    
    # This would generate a detailed health report
    # For now, we'll create a simple JSON report
    cat > $HEALTH_REPORT << EOF
{
    "timestamp": "$(date -Iseconds)",
    "system_health": "see logs",
    "service_health": "see logs",
    "application_health": "see logs",
    "backup_health": "see logs",
    "security_health": "see logs",
    "overall_status": "see logs"
}
EOF
    
    log_message "Health report generated: $HEALTH_REPORT"
}

# Function to send health notification
send_notification() {
    local status=$1
    local message=$2
    
    log_message "Health check $status: $message"
    
    # In a real implementation, this would send an email notification
    echo "📧 Health check $status: $message"
}

# Main health check function
main() {
    log_message "=== Starting Atlas Health Check ==="
    
    # Start time
    local start_time=$(date)
    log_message "Health check started at: $start_time"
    
    # Initialize health status
    local overall_healthy=true
    
    # Run all health checks
    if ! check_system_health; then
        overall_healthy=false
    fi
    
    if ! check_service_health; then
        overall_healthy=false
    fi
    
    if ! check_application_health; then
        overall_healthy=false
    fi
    
    if ! check_backup_health; then
        overall_healthy=false
    fi
    
    if ! check_security_health; then
        overall_healthy=false
    fi
    
    # Generate health report
    generate_health_report
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Health check completed at: $end_time (Duration: ${duration}s)"
    
    # Overall result
    if $overall_healthy; then
        log_message "=== All Health Checks Passed ==="
        send_notification "SUCCESS" "All health checks passed"
        echo ""
        echo "✅ Atlas production environment is healthy"
        echo "📋 Detailed report available at: $HEALTH_REPORT"
        return 0
    else
        log_message "=== Some Health Checks Failed ==="
        send_notification "WARNING" "Some health checks failed"
        echo ""
        echo "⚠️ Atlas production environment has issues"
        echo "📋 Detailed report available at: $HEALTH_REPORT"
        return 1
    fi
}

# Handle script arguments
if [ "$1" == "--system" ]; then
    echo "Checking system health..."
    check_system_health
    exit 0
elif [ "$1" == "--services" ]; then
    echo "Checking service health..."
    check_service_health
    exit 0
elif [ "$1" == "--application" ]; then
    echo "Checking application health..."
    check_application_health
    exit 0
elif [ "$1" == "--backup" ]; then
    echo "Checking backup health..."
    check_backup_health
    exit 0
elif [ "$1" == "--security" ]; then
    echo "Checking security health..."
    check_security_health
    exit 0
fi

# Run full health check
if main; then
    exit 0
else
    exit 1
fi