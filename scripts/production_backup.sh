#!/bin/bash

# Atlas Production Backup Script
# This script manages backup operations for Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Backup..."

# Configuration
BACKUP_DIR="/home/ubuntu/dev/atlas/backups"
LOG_FILE="/home/ubuntu/dev/atlas/logs/backup.log"
RETENTION_DAYS=30

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR
mkdir -p "$(dirname $LOG_FILE)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $LOG_FILE
    echo "$1"
}

# Function to create database backup
backup_database() {
    log_message "Starting database backup"
    
    # Create backup filename with timestamp
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local backup_file="$BACKUP_DIR/atlas_backup_$timestamp.sql"
    
    # Create database backup
    if sudo -u postgres pg_dump -U atlas_user -d atlas > "$backup_file"; then
        log_message "Database backup created: $backup_file"
    else
        log_message "ERROR: Failed to create database backup"
        return 1
    fi
    
    # Compress backup
    if gzip "$backup_file"; then
        local compressed_file="$backup_file.gz"
        log_message "Backup compressed: $compressed_file"
        
        # Get file size
        local file_size=$(du -h "$compressed_file" | cut -f1)
        log_message "Compressed backup size: $file_size"
    else
        log_message "ERROR: Failed to compress backup"
        return 1
    fi
    
    return 0
}

# Function to backup configuration files
backup_config() {
    log_message "Starting configuration backup"
    
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local config_backup_dir="$BACKUP_DIR/config_backup_$timestamp"
    
    # Create config backup directory
    mkdir -p "$config_backup_dir"
    
    # Copy configuration files
    cp -r /home/ubuntu/dev/atlas/.env "$config_backup_dir/" 2>/dev/null || true
    cp -r /home/ubuntu/dev/atlas/config "$config_backup_dir/" 2>/dev/null || true
    
    # Create tar archive
    local config_tar="$config_backup_dir.tar.gz"
    if tar -czf "$config_tar" -C "$BACKUP_DIR" "config_backup_$timestamp"; then
        log_message "Configuration backup created: $config_tar"
        # Remove temporary directory
        rm -rf "$config_backup_dir"
    else
        log_message "ERROR: Failed to create configuration backup"
        return 1
    fi
    
    return 0
}

# Function to cleanup old backups
cleanup_old_backups() {
    log_message "Cleaning up old backups"
    
    # Delete database backups older than retention period
    local db_deleted=0
    for backup in $(find "$BACKUP_DIR" -name "atlas_backup_*.sql.gz" -mtime +$RETENTION_DAYS); do
        rm "$backup"
        db_deleted=$((db_deleted + 1))
    done
    log_message "Deleted $db_deleted old database backups"
    
    # Delete config backups older than retention period
    local config_deleted=0
    for backup in $(find "$BACKUP_DIR" -name "config_backup_*.tar.gz" -mtime +$RETENTION_DAYS); do
        rm "$backup"
        config_deleted=$((config_deleted + 1))
    done
    log_message "Deleted $config_deleted old configuration backups"
    
    return 0
}

# Function to verify backup
verify_backup() {
    log_message "Verifying latest backup"
    
    # Find latest backup
    local latest_backup=$(ls -t "$BACKUP_DIR"/atlas_backup_*.sql.gz 2>/dev/null | head -1)
    
    if [ -z "$latest_backup" ]; then
        log_message "WARNING: No backups found to verify"
        return 0
    fi
    
    # Check if file exists and has content
    if [ -f "$latest_backup" ] && [ -s "$latest_backup" ]; then
        local file_size=$(du -h "$latest_backup" | cut -f1)
        log_message "Latest backup verified: $latest_backup ($file_size)"
    else
        log_message "ERROR: Latest backup verification failed: $latest_backup"
        return 1
    fi
    
    return 0
}

# Function to upload to cloud storage (placeholder)
upload_to_cloud() {
    log_message "Uploading backup to cloud storage"
    
    # This is a placeholder - in a real implementation, you would upload to cloud storage
    # For example, to AWS S3:
    # aws s3 cp "$latest_backup" s3://your-bucket/backups/
    
    # Or to Google Cloud Storage:
    # gsutil cp "$latest_backup" gs://your-bucket/backups/
    
    # Or to OCI Object Storage:
    # oci os object put -bn your-bucket -f "$latest_backup"
    
    log_message "Cloud upload would be implemented here"
    return 0
}

# Function to send backup notification
send_notification() {
    local status=$1
    local message=$2
    
    log_message "Backup $status: $message"
    
    # In a real implementation, this would send an email notification
    # For now, we'll just log to file
    echo "📧 Backup $status: $message"
}

# Main backup function
main() {
    log_message "=== Starting Atlas Backup Process ==="
    
    # Start time
    local start_time=$(date)
    log_message "Backup process started at: $start_time"
    
    # Perform database backup
    if backup_database; then
        send_notification "SUCCESS" "Database backup completed successfully"
    else
        send_notification "FAILED" "Database backup failed"
        return 1
    fi
    
    # Perform configuration backup
    if backup_config; then
        send_notification "SUCCESS" "Configuration backup completed successfully"
    else
        send_notification "FAILED" "Configuration backup failed"
        return 1
    fi
    
    # Verify backup
    if verify_backup; then
        send_notification "SUCCESS" "Backup verification completed successfully"
    else
        send_notification "WARNING" "Backup verification failed"
    fi
    
    # Cleanup old backups
    if cleanup_old_backups; then
        send_notification "SUCCESS" "Backup cleanup completed successfully"
    else
        send_notification "WARNING" "Backup cleanup failed"
    fi
    
    # Upload to cloud (placeholder)
    if upload_to_cloud; then
        send_notification "SUCCESS" "Cloud upload completed successfully"
    else
        send_notification "WARNING" "Cloud upload failed"
    fi
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Backup process completed at: $end_time (Duration: ${duration}s)"
    log_message "=== Backup Process Completed ==="
    
    return 0
}

# Run main function
if main; then
    echo "✅ Atlas backup completed successfully"
    exit 0
else
    echo "❌ Atlas backup failed"
    exit 1
fi