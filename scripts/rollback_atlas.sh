#!/bin/bash

# Atlas Production Rollback Script
# This script rolls back the Atlas production environment to a previous stable state

set -e  # Exit on any error

echo "Starting Atlas Production Rollback..."

# Configuration
ROLLBACK_LOG="/home/ubuntu/dev/atlas/logs/rollback.log"
ROLLBACK_CONFIG="/home/ubuntu/dev/atlas/config/rollback.json"
BACKUP_DIR="/home/ubuntu/dev/atlas/backups"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $ROLLBACK_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $ROLLBACK_LOG
    echo "$1"
}

# Function to initialize rollback configuration
initialize_rollback_config() {
    log_message "Initializing rollback configuration"
    
    # Create default rollback configuration if it doesn't exist
    if [ ! -f "$ROLLBACK_CONFIG" ]; then
        cat > "$ROLLBACK_CONFIG" << EOF
{
    "rollback": {
        "max_rollback_points": 10,
        "auto_backup_before_rollback": true,
        "confirm_before_rollback": true
    },
    "backup": {
        "database_backup_script": "/home/ubuntu/dev/atlas/scripts/production_backup.sh",
        "restore_script": "/home/ubuntu/dev/atlas/scripts/restore_backup.sh"
    },
    "notifications": {
        "email": {
            "enabled": true,
            "recipients": ["admin@khamel.com"]
        }
    }
}
EOF
        echo "✅ Created default rollback configuration"
        log_message "Default rollback configuration created"
    else
        echo "✅ Rollback configuration already exists"
    fi
}

# Function to list available rollback points
list_rollback_points() {
    log_message "Listing available rollback points"
    
    echo "Available Rollback Points:"
    echo "========================="
    
    # Check if backup directory exists
    if [ ! -d "$BACKUP_DIR" ]; then
        echo "❌ Backup directory not found: $BACKUP_DIR"
        log_message "Backup directory not found: $BACKUP_DIR"
        return 1
    fi
    
    # List database backups
    echo "Database Backups:"
    echo "----------------"
    local db_backups=$(find "$BACKUP_DIR" -name "*.sql.gz" -o -name "*.sql" | sort -r)
    if [ -z "$db_backups" ]; then
        echo "  No database backups found"
    else
        local count=1
        while IFS= read -r backup; do
            local timestamp=$(basename "$backup" | sed 's/atlas_backup_//' | sed 's/\.sql.*//')
            local size=$(du -h "$backup" | cut -f1)
            echo "  $count. $(basename $backup) ($size) - $timestamp"
            count=$((count + 1))
        done <<< "$db_backups"
    fi
    
    # List configuration backups
    echo ""
    echo "Configuration Backups:"
    echo "--------------------"
    local config_backups=$(find "$BACKUP_DIR" -name "config_backup_*" | sort -r)
    if [ -z "$config_backups" ]; then
        echo "  No configuration backups found"
    else
        local count=1
        while IFS= read -r backup; do
            local timestamp=$(basename "$backup" | sed 's/config_backup_//' | sed 's/\.tar.*//')
            local size=$(du -h "$backup" 2>/dev/null | cut -f1)
            echo "  $count. $(basename $backup) ($size) - $timestamp"
            count=$((count + 1))
        done <<< "$config_backups"
    fi
    
    log_message "Rollback points listed"
}

# Function to create backup before rollback
create_backup_before_rollback() {
    log_message "Creating backup before rollback"
    
    echo ""
    echo "Creating Backup Before Rollback..."
    echo "================================"
    
    # Check if backup before rollback is enabled
    local auto_backup=$(jq -r '.rollback.auto_backup_before_rollback' "$ROLLBACK_CONFIG")
    if [ "$auto_backup" != "true" ]; then
        echo "ℹ️ Auto backup before rollback is disabled"
        log_message "Auto backup before rollback is disabled"
        return 0
    fi
    
    # Run backup script
    local backup_script=$(jq -r '.backup.database_backup_script' "$ROLLBACK_CONFIG")
    if [ -f "$backup_script" ]; then
        echo "🔄 Creating database backup before rollback..."
        if $backup_script; then
            echo "✅ Database backup created successfully"
            log_message "Database backup created successfully"
        else
            echo "❌ Database backup failed"
            log_message "Database backup failed"
            return 1
        fi
    else
        echo "❌ Backup script not found: $backup_script"
        log_message "Backup script not found: $backup_script"
        return 1
    fi
}

# Function to select rollback point
select_rollback_point() {
    log_message "Selecting rollback point"
    
    echo ""
    echo "Select Rollback Point:"
    echo "===================="
    
    # List available backups
    list_rollback_points
    
    # Prompt for selection
    echo ""
    read -p "Enter backup number to rollback to (or 'cancel' to abort): " selection
    
    if [ "$selection" = "cancel" ] || [ "$selection" = "Cancel" ]; then
        echo "❌ Rollback cancelled by user"
        log_message "Rollback cancelled by user"
        return 1
    fi
    
    # Validate selection
    if ! [[ "$selection" =~ ^[0-9]+$ ]] || [ "$selection" -lt 1 ]; then
        echo "❌ Invalid selection"
        log_message "Invalid selection: $selection"
        return 1
    fi
    
    # Get selected backup
    local db_backups=$(find "$BACKUP_DIR" -name "*.sql.gz" -o -name "*.sql" | sort -r)
    local selected_backup=""
    local count=1
    
    while IFS= read -r backup; do
        if [ $count -eq $selection ]; then
            selected_backup="$backup"
            break
        fi
        count=$((count + 1))
    done <<< "$db_backups"
    
    if [ -z "$selected_backup" ]; then
        echo "❌ Selected backup not found"
        log_message "Selected backup not found"
        return 1
    fi
    
    echo "Selected backup: $selected_backup"
    log_message "Selected rollback point: $selected_backup"
    
    # Confirm rollback
    local confirm_rollback=$(jq -r '.rollback.confirm_before_rollback' "$ROLLBACK_CONFIG")
    if [ "$confirm_rollback" = "true" ]; then
        echo ""
        read -p "⚠️ Are you sure you want to rollback to this backup? (yes/no): " confirm
        
        if [ "$confirm" != "yes" ] && [ "$confirm" != "Yes" ] && [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
            echo "❌ Rollback cancelled by user"
            log_message "Rollback cancelled by user"
            return 1
        fi
    fi
    
    # Store selected backup for later use
    echo "$selected_backup" > "/tmp/atlas_rollback_selected"
    log_message "Rollback point selected and stored"
}

# Function to stop services before rollback
stop_services() {
    log_message "Stopping services before rollback"
    
    echo ""
    echo "Stopping Services Before Rollback..."
    echo "=================================="
    
    # Define services to stop
    local services=(
        "atlas"
        "postgresql"
        "nginx"
        "atlas-prometheus"
        "atlas-grafana"
    )
    
    # Stop each service
    for service in "${services[@]}"; do
        echo "🛑 Stopping $service..."
        if sudo systemctl stop $service; then
            echo "✅ $service stopped successfully"
            log_message "$service stopped successfully"
        else
            echo "❌ Failed to stop $service"
            log_message "Failed to stop $service"
            # Continue with other services even if one fails
        fi
    done
    
    # Wait a moment for services to stop
    sleep 5
}

# Function to restore database from backup
restore_database() {
    log_message "Restoring database from backup"
    
    echo ""
    echo "Restoring Database From Backup..."
    echo "=============================="
    
    # Get selected backup
    if [ ! -f "/tmp/atlas_rollback_selected" ]; then
        echo "❌ No rollback point selected"
        log_message "No rollback point selected"
        return 1
    fi
    
    local backup_file=$(cat "/tmp/atlas_rollback_selected")
    echo "Restoring from backup: $backup_file"
    
    # Check if backup file exists
    if [ ! -f "$backup_file" ]; then
        echo "❌ Backup file not found: $backup_file"
        log_message "Backup file not found: $backup_file"
        return 1
    fi
    
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
    if [[ "$backup_file" == *.gz ]]; then
        if gunzip -c "$backup_file" | sudo -u postgres psql -U atlas_user -d atlas > /dev/null 2>&1; then
            echo "✅ Database restored successfully from compressed backup"
            log_message "Database restored successfully from compressed backup"
        else
            echo "❌ Failed to restore database from compressed backup"
            log_message "Failed to restore database from compressed backup"
            return 1
        fi
    else
        # Handle uncompressed backups
        if sudo -u postgres psql -U atlas_user -d atlas -f "$backup_file" > /dev/null 2>&1; then
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
}

# Function to restore configuration
restore_configuration() {
    log_message "Restoring configuration from backup"
    
    echo ""
    echo "Restoring Configuration From Backup..."
    echo "===================================="
    
    # Check if configuration backup exists
    local config_backup=$(find "$BACKUP_DIR" -name "config_backup_*" | sort -r | head -1)
    if [ -z "$config_backup" ]; then
        echo "ℹ️ No configuration backup found, skipping configuration restore"
        log_message "No configuration backup found, skipping configuration restore"
        return 0
    fi
    
    echo "Restoring configuration from: $config_backup"
    
    # Extract configuration backup
    local temp_dir="/tmp/atlas_config_restore_$$"
    mkdir -p "$temp_dir"
    
    if tar -xzf "$config_backup" -C "$temp_dir" > /dev/null 2>&1; then
        echo "✅ Configuration backup extracted successfully"
        log_message "Configuration backup extracted successfully"
    else
        echo "❌ Failed to extract configuration backup"
        log_message "Failed to extract configuration backup"
        rm -rf "$temp_dir"
        return 1
    fi
    
    # Restore configuration files
    local config_files=(
        ".env"
        "config/*"
    )
    
    for config_file in "${config_files[@]}"; do
        local source_file="$temp_dir/$(basename $config_backup | sed 's/\.tar\.gz//')/$config_file"
        local dest_file="/home/ubuntu/dev/atlas/$config_file"
        
        if [ -f "$source_file" ]; then
            echo "🔄 Restoring $config_file..."
            if cp "$source_file" "$dest_file" 2>/dev/null; then
                echo "✅ $config_file restored successfully"
                log_message "$config_file restored successfully"
            else
                echo "❌ Failed to restore $config_file"
                log_message "Failed to restore $config_file"
            fi
        fi
    done
    
    # Clean up temporary directory
    rm -rf "$temp_dir"
    log_message "Configuration restore completed"
}

# Function to restart services after rollback
restart_services() {
    log_message "Restarting services after rollback"
    
    echo ""
    echo "Restarting Services After Rollback..."
    echo "=================================="
    
    # Define services to restart
    local services=(
        "postgresql"
        "atlas"
        "nginx"
        "atlas-prometheus"
        "atlas-grafana"
    )
    
    # Start each service
    for service in "${services[@]}"; do
        echo "🚀 Starting $service..."
        if sudo systemctl start $service; then
            echo "✅ $service started successfully"
            log_message "$service started successfully"
        else
            echo "❌ Failed to start $service"
            log_message "Failed to start $service"
            # Continue with other services even if one fails
        fi
    done
    
    # Wait for services to initialize
    echo "⏳ Waiting for services to initialize..."
    sleep 10
}

# Function to verify rollback
verify_rollback() {
    log_message "Verifying rollback"
    
    echo ""
    echo "Verifying Rollback..."
    echo "=================="
    
    # Check if web interface is accessible
    echo "🔍 Checking web interface accessibility..."
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        echo "✅ Web interface is accessible"
        log_message "Web interface is accessible"
    else
        echo "❌ Web interface is not accessible"
        log_message "Web interface is not accessible"
        return 1
    fi
    
    # Check database connectivity
    echo "🔍 Checking database connectivity..."
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        echo "✅ Database is accessible"
        log_message "Database is accessible"
    else
        echo "❌ Database is not accessible"
        log_message "Database is not accessible"
        return 1
    fi
    
    # Check if all services are running
    echo "🔍 Checking service statuses..."
    local services=(
        "atlas"
        "postgresql"
        "nginx"
        "atlas-prometheus"
        "atlas-grafana"
    )
    
    local all_running=true
    for service in "${services[@]}"; do
        if systemctl is-active --quiet $service; then
            echo "✅ $service is running"
        else
            echo "❌ $service is not running"
            all_running=false
        fi
    done
    
    if $all_running; then
        echo "✅ All services are running"
        log_message "All services are running"
    else
        echo "❌ Some services are not running"
        log_message "Some services are not running"
        return 1
    fi
    
    echo "✅ Rollback verification completed successfully"
    log_message "Rollback verification completed successfully"
}

# Function to send rollback notification
send_rollback_notification() {
    local status=$1
    local message=$2
    
    log_message "Sending rollback notification: $status"
    
    echo ""
    echo "Sending Rollback Notification..."
    echo "=============================="
    
    # Check if notifications are enabled
    local notifications_enabled=$(jq -r '.notifications.email.enabled' "$ROLLBACK_CONFIG")
    if [ "$notifications_enabled" != "true" ]; then
        echo "ℹ️ Rollback notifications are disabled"
        log_message "Rollback notifications are disabled"
        return 0
    fi
    
    # Get recipients
    local recipients=$(jq -r '.notifications.email.recipients[]' "$ROLLBACK_CONFIG")
    
    # Send notification (simulated)
    echo "📧 Rollback $status: $message"
    echo "To: $recipients"
    echo "Subject: Atlas Rollback $status - $(date +%Y%m%d_%H%M%S)"
    echo ""
    echo "Rollback completed at: $(date)"
    echo "Status: $status"
    echo "Message: $message"
    echo ""
    echo "For detailed logs, check: $ROLLBACK_LOG"
    
    log_message "Rollback notification sent: $status"
}

# Function to generate rollback report
generate_rollback_report() {
    log_message "Generating rollback report"
    
    echo ""
    echo "Generating Rollback Report..."
    echo "=========================="
    
    local report_file="/home/ubuntu/dev/atlas/logs/rollback_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create rollback report
    echo "Atlas Production Rollback Report" > "$report_file"
    echo "Generated: $(date)" >> "$report_file"
    echo "================================" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add rollback details
    echo "Rollback Details:" >> "$report_file"
    echo "---------------" >> "$report_file"
    echo "Timestamp: $(date)" >> "$report_file"
    if [ -f "/tmp/atlas_rollback_selected" ]; then
        echo "Rolled back to: $(cat /tmp/atlas_rollback_selected)" >> "$report_file"
    fi
    echo "" >> "$report_file"
    
    # Add system information
    echo "System Information:" >> "$report_file"
    echo "------------------" >> "$report_file"
    echo "Hostname: $(hostname)" >> "$report_file"
    echo "Rolled back by: $(whoami)" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add service status after rollback
    echo "Service Status After Rollback:" >> "$report_file"
    echo "----------------------------" >> "$report_file"
    local services=(
        "atlas"
        "postgresql"
        "nginx"
        "atlas-prometheus"
        "atlas-grafana"
    )
    
    for service in "${services[@]}"; do
        if systemctl is-active --quiet $service; then
            echo "$service: ✅ Running" >> "$report_file"
        else
            echo "$service: ❌ Not Running" >> "$report_file"
        fi
    done
    echo "" >> "$report_file"
    
    echo "✅ Rollback report generated: $report_file"
    log_message "Rollback report generated: $report_file"
    
    # Display summary
    echo ""
    echo "Rollback Summary:"
    echo "  Report saved to: $report_file"
    echo "  Check service status above"
}

# Function to clean up temporary files
cleanup_temp_files() {
    log_message "Cleaning up temporary files"
    
    echo ""
    echo "Cleaning Up Temporary Files..."
    echo "============================"
    
    # Remove temporary files
    rm -f "/tmp/atlas_rollback_selected" 2>/dev/null || true
    
    echo "✅ Temporary files cleaned up"
    log_message "Temporary files cleaned up"
}

# Main rollback function
main() {
    log_message "=== Starting Atlas Rollback ==="
    
    # Initialize configuration
    initialize_rollback_config
    
    # Start time
    local start_time=$(date)
    log_message "Rollback started at: $start_time"
    
    # Handle different rollback operations
    case $1 in
        "list")
            list_rollback_points
            exit 0
            ;;
        "select")
            select_rollback_point
            exit 0
            ;;
        "restore-db")
            restore_database
            exit 0
            ;;
        "restore-config")
            restore_configuration
            exit 0
            ;;
        "verify")
            verify_rollback
            exit 0
            ;;
        *)
            # Perform full rollback
            echo "Starting Full Rollback Process..."
            echo "================================"
            
            # Create backup before rollback
            if ! create_backup_before_rollback; then
                send_rollback_notification "FAILED" "Rollback failed during backup creation"
                cleanup_temp_files
                exit 1
            fi
            
            # Select rollback point
            if ! select_rollback_point; then
                send_rollback_notification "CANCELLED" "Rollback cancelled by user"
                cleanup_temp_files
                exit 1
            fi
            
            # Stop services
            stop_services
            
            # Restore database
            if ! restore_database; then
                send_rollback_notification "FAILED" "Rollback failed during database restore"
                restart_services  # Try to restart services to restore to previous state
                cleanup_temp_files
                exit 1
            fi
            
            # Restore configuration
            restore_configuration
            
            # Restart services
            restart_services
            
            # Verify rollback
            if ! verify_rollback; then
                send_rollback_notification "FAILED" "Rollback verification failed"
                cleanup_temp_files
                exit 1
            fi
            
            # Generate rollback report
            generate_rollback_report
            
            # Send success notification
            send_rollback_notification "SUCCESS" "Rollback completed successfully"
            
            # Clean up temporary files
            cleanup_temp_files
            
            # End time
            local end_time=$(date)
            local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
            log_message "Rollback completed at: $end_time (Duration: ${duration}s)"
            
            log_message "=== Rollback Completed Successfully ==="
            
            echo ""
            echo "✅ Rollback completed successfully!"
            echo "⏱️ Duration: ${duration} seconds"
            ;;
    esac
    
    echo "📋 Check $ROLLBACK_LOG for detailed logs"
}

# Run main function
main "$@"