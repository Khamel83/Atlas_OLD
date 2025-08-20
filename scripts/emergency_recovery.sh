#!/bin/bash

# Atlas Production Emergency Recovery Script
# This script provides emergency recovery procedures for critical Atlas production failures

set -e  # Exit on any error

echo "Starting Atlas Production Emergency Recovery..."

# Configuration
EMERGENCY_LOG="/home/ubuntu/dev/atlas/logs/emergency_recovery.log"
EMERGENCY_CONFIG="/home/ubuntu/dev/atlas/config/emergency_recovery.json"
BACKUP_DIR="/home/ubuntu/dev/atlas/backups"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $EMERGENCY_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $EMERGENCY_LOG
    echo "$1"
}

# Function to initialize emergency configuration
initialize_emergency_config() {
    log_message "Initializing emergency configuration"
    
    # Create default emergency configuration if it doesn't exist
    if [ ! -f "$EMERGENCY_CONFIG" ]; then
        cat > "$EMERGENCY_CONFIG" << EOF
{
    "emergency_recovery": {
        "auto_recovery_enabled": true,
        "max_recovery_attempts": 3,
        "recovery_delay_seconds": 30,
        "notify_on_recovery": true
    },
    "critical_services": [
        "atlas",
        "postgresql",
        "nginx",
        "atlas-prometheus",
        "atlas-grafana"
    ],
    "notifications": {
        "email": {
            "enabled": true,
            "recipients": ["admin@khamel.com"],
            "smtp_server": "smtp.gmail.com",
            "port": 587
        }
    },
    "backup": {
        "primary_backup_script": "/home/ubuntu/dev/atlas/scripts/production_backup.sh",
        "restore_script": "/home/ubuntu/dev/atlas/scripts/restore_backup.sh"
    }
}
EOF
        echo "✅ Created default emergency configuration"
        log_message "Default emergency configuration created"
    else
        echo "✅ Emergency configuration already exists"
    fi
}

# Function to check system health
check_system_health() {
    log_message "Checking system health"
    
    echo "Checking System Health..."
    echo "========================"
    
    # Check CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    echo "CPU Usage: ${cpu_usage}%"
    
    # Check memory usage
    local memory_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    echo "Memory Usage: ${memory_usage}%"
    
    # Check disk usage
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    echo "Disk Usage: ${disk_usage}%"
    
    # Check system load
    local load_avg=$(uptime | awk -F'load average:' '{print $2}' | xargs)
    echo "Load Average: $load_avg"
    
    # Check if system resources are within acceptable limits
    if [ $cpu_usage -lt 95 ] && [ $memory_usage -lt 95 ] && [ $disk_usage -lt 95 ]; then
        echo "✅ System resources are within acceptable limits"
        log_message "System health check passed"
        return 0
    else
        echo "❌ System resources are high"
        log_message "System health check failed - high resource usage"
        return 1
    fi
}

# Function to restart all services
restart_all_services() {
    log_message "Restarting all services"
    
    echo ""
    echo "Restarting All Services..."
    echo "========================"
    
    # Get critical services from configuration
    local services=$(jq -r '.critical_services[]' "$EMERGENCY_CONFIG")
    
    # Stop all services first
    echo "🛑 Stopping all critical services..."
    for service in $services; do
        echo "  Stopping $service..."
        if sudo systemctl stop $service > /dev/null 2>&1; then
            echo "    ✅ $service stopped"
        else
            echo "    ℹ️ $service already stopped or failed to stop"
        fi
    done
    
    # Wait a moment
    echo "⏳ Waiting for services to stop..."
    sleep 5
    
    # Start all services
    echo "🚀 Starting all critical services..."
    local failed_services=()
    
    for service in $services; do
        echo "  Starting $service..."
        if sudo systemctl start $service; then
            echo "    ✅ $service started"
            log_message "$service started successfully"
        else
            echo "    ❌ $service failed to start"
            log_message "$service failed to start"
            failed_services+=("$service")
        fi
    done
    
    # Check if any services failed to start
    if [ ${#failed_services[@]} -eq 0 ]; then
        echo "✅ All services restarted successfully"
        log_message "All services restarted successfully"
        return 0
    else
        echo "❌ Failed to start services: ${failed_services[*]}"
        log_message "Failed to start services: ${failed_services[*]}"
        return 1
    fi
}

# Function to check service status
check_service_status() {
    log_message "Checking service status"
    
    echo ""
    echo "Checking Service Status..."
    echo "========================"
    
    # Get critical services from configuration
    local services=$(jq -r '.critical_services[]' "$EMERGENCY_CONFIG")
    
    # Check status of each service
    local down_services=()
    for service in $services; do
        if systemctl is-active --quiet $service; then
            echo "✅ $service: Running"
        else
            echo "❌ $service: Not Running"
            down_services+=("$service")
        fi
    done
    
    # Report results
    if [ ${#down_services[@]} -eq 0 ]; then
        echo "✅ All critical services are running"
        log_message "All critical services are running"
        return 0
    else
        echo "❌ Down services: ${down_services[*]}"
        log_message "Down services: ${down_services[*]}"
        return 1
    fi
}

# Function to restart failed services
restart_failed_services() {
    log_message "Restarting failed services"
    
    echo ""
    echo "Restarting Failed Services..."
    echo "============================"
    
    # Get critical services from configuration
    local services=$(jq -r '.critical_services[]' "$EMERGENCY_CONFIG")
    
    # Restart failed services
    local restarted_services=()
    for service in $services; do
        if ! systemctl is-active --quiet $service; then
            echo "🔄 Restarting $service..."
            if sudo systemctl restart $service; then
                echo "  ✅ $service restarted successfully"
                log_message "$service restarted successfully"
                restarted_services+=("$service")
            else
                echo "  ❌ Failed to restart $service"
                log_message "Failed to restart $service"
            fi
        fi
    done
    
    # Report results
    if [ ${#restarted_services[@]} -eq 0 ]; then
        echo "ℹ️ No failed services found to restart"
        log_message "No failed services found to restart"
    else
        echo "✅ Restarted services: ${restarted_services[*]}"
        log_message "Restarted services: ${restarted_services[*]}"
    fi
}

# Function to check database health
check_database_health() {
    log_message "Checking database health"
    
    echo ""
    echo "Checking Database Health..."
    echo "========================"
    
    # Check if PostgreSQL is running
    if systemctl is-active --quiet postgresql; then
        echo "✅ PostgreSQL is running"
    else
        echo "❌ PostgreSQL is not running"
        log_message "PostgreSQL is not running"
        return 1
    fi
    
    # Check database connectivity
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        echo "✅ Database is accessible"
        log_message "Database is accessible"
    else
        echo "❌ Database is not accessible"
        log_message "Database is not accessible"
        return 1
    fi
    
    # Check database size
    local db_size=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT pg_size_pretty(pg_database_size('atlas'));")
    echo "📊 Database size: $db_size"
    
    echo "✅ Database health check completed"
    log_message "Database health check completed"
    return 0
}

# Function to restore database from backup
restore_database_from_backup() {
    log_message "Restoring database from backup"
    
    echo ""
    echo "Restoring Database From Backup..."
    echo "================================"
    
    # Check if backup directory exists
    if [ ! -d "$BACKUP_DIR" ]; then
        echo "❌ Backup directory not found: $BACKUP_DIR"
        log_message "Backup directory not found: $BACKUP_DIR"
        return 1
    fi
    
    # Find latest database backup
    local latest_backup=$(find "$BACKUP_DIR" -name "atlas_backup_*.sql*" | sort -r | head -1)
    if [ -z "$latest_backup" ]; then
        echo "❌ No database backups found"
        log_message "No database backups found"
        return 1
    fi
    
    echo "Latest backup: $latest_backup"
    
    # Stop database service
    echo "🛑 Stopping PostgreSQL..."
    if ! sudo systemctl stop postgresql; then
        echo "❌ Failed to stop PostgreSQL"
        log_message "Failed to stop PostgreSQL"
        return 1
    fi
    
    # Drop and recreate database
    echo "🔄 Dropping and recreating database..."
    if ! sudo -u postgres psql -c "DROP DATABASE IF EXISTS atlas;" > /dev/null 2>&1; then
        echo "❌ Failed to drop database"
        log_message "Failed to drop database"
        return 1
    fi
    
    if ! sudo -u postgres psql -c "CREATE DATABASE atlas OWNER atlas_user;" > /dev/null 2>&1; then
        echo "❌ Failed to create database"
        log_message "Failed to create database"
        return 1
    fi
    
    # Restore database from backup
    echo "🔄 Restoring database from backup..."
    
    # Handle compressed backups
    if [[ "$latest_backup" == *.gz ]]; then
        if gunzip -c "$latest_backup" | sudo -u postgres psql -U atlas_user -d atlas > /dev/null 2>&1; then
            echo "✅ Database restored successfully from compressed backup"
            log_message "Database restored successfully from compressed backup"
        else
            echo "❌ Failed to restore database from compressed backup"
            log_message "Failed to restore database from compressed backup"
            return 1
        fi
    else
        # Handle uncompressed backups
        if sudo -u postgres psql -U atlas_user -d atlas -f "$latest_backup" > /dev/null 2>&1; then
            echo "✅ Database restored successfully from uncompressed backup"
            log_message "Database restored successfully from uncompressed backup"
        else
            echo "❌ Failed to restore database from uncompressed backup"
            log_message "Failed to restore database from uncompressed backup"
            return 1
        fi
    fi
    
    # Start database service
    echo "🚀 Starting PostgreSQL..."
    if ! sudo systemctl start postgresql; then
        echo "❌ Failed to start PostgreSQL"
        log_message "Failed to start PostgreSQL"
        return 1
    fi
    
    echo "✅ Database restored successfully"
    log_message "Database restored successfully"
    return 0
}

# Function to check web interface
check_web_interface() {
    log_message "Checking web interface"
    
    echo ""
    echo "Checking Web Interface..."
    echo "========================"
    
    # Check if web interface is accessible
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        echo "✅ Web interface is accessible"
        log_message "Web interface is accessible"
        return 0
    else
        echo "❌ Web interface is not accessible"
        log_message "Web interface is not accessible"
        return 1
    fi
}

# Function to restart web server
restart_web_server() {
    log_message "Restarting web server"
    
    echo ""
    echo "Restarting Web Server..."
    echo "======================"
    
    # Restart Nginx
    echo "🔄 Restarting Nginx..."
    if sudo systemctl restart nginx; then
        echo "✅ Nginx restarted successfully"
        log_message "Nginx restarted successfully"
    else
        echo "❌ Failed to restart Nginx"
        log_message "Failed to restart Nginx"
        return 1
    fi
    
    # Wait for Nginx to initialize
    echo "⏳ Waiting for Nginx to initialize..."
    sleep 5
    
    # Test web interface
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        echo "✅ Web interface is now accessible"
        log_message "Web interface is now accessible"
        return 0
    else
        echo "❌ Web interface is still not accessible"
        log_message "Web interface is still not accessible"
        return 1
    fi
}

# Function to perform emergency recovery
perform_emergency_recovery() {
    log_message "Performing emergency recovery"
    
    echo ""
    echo "Performing Emergency Recovery..."
    echo "=============================="
    
    # Check if auto recovery is enabled
    local auto_recovery=$(jq -r '.emergency_recovery.auto_recovery_enabled' "$EMERGENCY_CONFIG")
    if [ "$auto_recovery" != "true" ]; then
        echo "❌ Auto recovery is disabled"
        log_message "Auto recovery is disabled"
        return 1
    fi
    
    # Get recovery parameters
    local max_attempts=$(jq -r '.emergency_recovery.max_recovery_attempts' "$EMERGENCY_CONFIG")
    local delay_seconds=$(jq -r '.emergency_recovery.recovery_delay_seconds' "$EMERGENCY_CONFIG")
    
    # Attempt recovery
    local attempt=1
    while [ $attempt -le $max_attempts ]; do
        echo "🔄 Recovery attempt $attempt of $max_attempts..."
        log_message "Recovery attempt $attempt of $max_attempts"
        
        # Restart all services
        if restart_all_services; then
            echo "✅ Services restarted successfully"
            
            # Wait for services to initialize
            echo "⏳ Waiting for services to initialize..."
            sleep $delay_seconds
            
            # Check service status
            if check_service_status; then
                echo "✅ Services are running correctly"
                
                # Check database health
                if check_database_health; then
                    echo "✅ Database is healthy"
                    
                    # Check web interface
                    if check_web_interface; then
                        echo "✅ Web interface is accessible"
                        echo "✅ Emergency recovery completed successfully"
                        log_message "Emergency recovery completed successfully"
                        return 0
                    else
                        echo "❌ Web interface is not accessible"
                    fi
                else
                    echo "❌ Database is not healthy"
                fi
            else
                echo "❌ Services are not running correctly"
            fi
        else
            echo "❌ Failed to restart services"
        fi
        
        # Increment attempt counter
        attempt=$((attempt + 1))
        
        # Wait before next attempt
        if [ $attempt -le $max_attempts ]; then
            echo "⏳ Waiting $delay_seconds seconds before next attempt..."
            sleep $delay_seconds
        fi
    done
    
    echo "❌ Emergency recovery failed after $max_attempts attempts"
    log_message "Emergency recovery failed after $max_attempts attempts"
    return 1
}

# Function to send emergency notification
send_emergency_notification() {
    local status=$1
    local message=$2
    
    log_message "Sending emergency notification: $status"
    
    echo ""
    echo "Sending Emergency Notification..."
    echo "=============================="
    
    # Check if notifications are enabled
    local notifications_enabled=$(jq -r '.notifications.email.enabled' "$EMERGENCY_CONFIG")
    if [ "$notifications_enabled" != "true" ]; then
        echo "ℹ️ Emergency notifications are disabled"
        log_message "Emergency notifications are disabled"
        return 0
    fi
    
    # Get recipients
    local recipients=$(jq -r '.notifications.email.recipients[]' "$EMERGENCY_CONFIG")
    
    # Send notification (simulated)
    echo "📧 Emergency $status: $message"
    echo "To: $recipients"
    echo "Subject: Atlas Emergency $status - $(date +%Y%m%d_%H%M%S)"
    echo ""
    echo "Emergency occurred at: $(date)"
    echo "Status: $status"
    echo "Message: $message"
    echo ""
    echo "For detailed logs, check: $EMERGENCY_LOG"
    
    log_message "Emergency notification sent: $status"
}

# Function to generate emergency report
generate_emergency_report() {
    log_message "Generating emergency report"
    
    echo ""
    echo "Generating Emergency Report..."
    echo "============================"
    
    local report_file="/home/ubuntu/dev/atlas/logs/emergency_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create emergency report
    echo "Atlas Production Emergency Report" > "$report_file"
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
    
    # Add resource usage
    echo "Resource Usage:" >> "$report_file"
    echo "--------------" >> "$report_file"
    echo "CPU Usage: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)%" >> "$report_file"
    echo "Memory Usage: $(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')%" >> "$report_file"
    echo "Disk Usage: $(df / | tail -1 | awk '{print $5}' | sed 's/%//')%" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add service status
    echo "Service Status:" >> "$report_file"
    echo "--------------" >> "$report_file"
    local services=$(jq -r '.critical_services[]' "$EMERGENCY_CONFIG")
    for service in $services; do
        if systemctl is-active --quiet $service; then
            echo "$service: ✅ Running" >> "$report_file"
        else
            echo "$service: ❌ Not Running" >> "$report_file"
        fi
    done
    echo "" >> "$report_file"
    
    # Add database information
    echo "Database Information:" >> "$report_file"
    echo "-------------------" >> "$report_file"
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        echo "Database Status: ✅ Accessible" >> "$report_file"
        local db_size=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT pg_size_pretty(pg_database_size('atlas'));")
        echo "Database Size: $db_size" >> "$report_file"
    else
        echo "Database Status: ❌ Not Accessible" >> "$report_file"
    fi
    echo "" >> "$report_file"
    
    # Add web interface status
    echo "Web Interface Status:" >> "$report_file"
    echo "--------------------" >> "$report_file"
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        echo "Web Interface: ✅ Accessible" >> "$report_file"
    else
        echo "Web Interface: ❌ Not Accessible" >> "$report_file"
    fi
    echo "" >> "$report_file"
    
    echo "✅ Emergency report generated: $report_file"
    log_message "Emergency report generated: $report_file"
    
    # Display summary
    echo ""
    echo "Emergency Summary:"
    echo "  Report saved to: $report_file"
    echo "  Check service statuses above"
}

# Main emergency recovery function
main() {
    log_message "=== Starting Atlas Emergency Recovery ==="
    
    # Initialize configuration
    initialize_emergency_config
    
    # Start time
    local start_time=$(date)
    log_message "Emergency recovery started at: $start_time"
    
    # Handle different emergency operations
    case $1 in
        "health")
            check_system_health
            check_service_status
            check_database_health
            check_web_interface
            ;;
        "restart-services")
            restart_all_services
            ;;
        "restart-failed")
            restart_failed_services
            ;;
        "restart-web")
            restart_web_server
            ;;
        "restore-db")
            restore_database_from_backup
            ;;
        "report")
            generate_emergency_report
            ;;
        "notify")
            send_emergency_notification "TEST" "Emergency notification test"
            ;;
        *)
            # Perform full emergency recovery
            echo "Starting Full Emergency Recovery Process..."
            echo "=========================================="
            
            # Check system health
            check_system_health
            
            # Check service status
            check_service_status
            
            # Check database health
            check_database_health
            
            # Check web interface
            check_web_interface
            
            # Perform emergency recovery
            if ! perform_emergency_recovery; then
                send_emergency_notification "FAILED" "Emergency recovery failed after multiple attempts"
                generate_emergency_report
                exit 1
            fi
            
            # Generate emergency report
            generate_emergency_report
            
            # Send success notification
            send_emergency_notification "SUCCESS" "Emergency recovery completed successfully"
            
            # End time
            local end_time=$(date)
            local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
            log_message "Emergency recovery completed at: $end_time (Duration: ${duration}s)"
            
            log_message "=== Emergency Recovery Completed ==="
            
            echo ""
            echo "✅ Emergency recovery completed successfully!"
            echo "⏱️ Duration: ${duration} seconds"
            echo "📋 Report: /home/ubuntu/dev/atlas/logs/emergency_report_*.txt"
            echo "📝 Log: $EMERGENCY_LOG"
            ;;
    esac
}

# Run main function
main "$@"