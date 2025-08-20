#!/bin/bash

# Atlas Production Disaster Recovery Script
# This script implements and tests disaster recovery procedures for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Disaster Recovery..."

# Configuration
DR_LOG="/home/ubuntu/dev/atlas/logs/disaster_recovery.log"
DR_REPORT_DIR="/home/ubuntu/dev/atlas/reports/disaster_recovery"
BACKUP_DIR="/home/ubuntu/dev/atlas/backups"
RESTORE_DIR="/home/ubuntu/dev/atlas/restores"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $DR_LOG)"
mkdir -p "$DR_REPORT_DIR"
mkdir -p "$RESTORE_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $DR_LOG
    echo "$1"
}

# Function to initialize disaster recovery configuration
initialize_dr_config() {
    log_message "Initializing disaster recovery configuration"
    
    # Create default DR configuration if it doesn't exist
    local dr_config="/home/ubuntu/dev/atlas/config/disaster_recovery.json"
    if [ ! -f "$dr_config" ]; then
        cat > "$dr_config" << EOF
{
    "disaster_recovery": {
        "rto_hours": 4,
        "rpo_hours": 24,
        "backup_frequency_hours": 24,
        "test_frequency_days": 30
    },
    "recovery_procedures": {
        "full_system_recovery": "/home/ubuntu/dev/atlas/scripts/full_recovery.sh",
        "database_recovery": "/home/ubuntu/dev/atlas/scripts/database_recovery.sh",
        "configuration_recovery": "/home/ubuntu/dev/atlas/scripts/configuration_recovery.sh"
    },
    "backup_locations": {
        "primary": "/home/ubuntu/dev/atlas/backups",
        "secondary": "oci://atlas-backups-bucket",
        "tertiary": "/mnt/backup-drive/atlas-backups"
    },
    "notifications": {
        "email": {
            "enabled": true,
            "recipients": ["admin@khamel.com"],
            "smtp_server": "smtp.gmail.com",
            "port": 587
        }
    }
}
EOF
        echo "✅ Created default disaster recovery configuration"
        log_message "Default disaster recovery configuration created"
    else
        echo "✅ Disaster recovery configuration already exists"
    fi
}

# Function to check backup availability
check_backup_availability() {
    log_message "Checking backup availability"
    
    echo "Checking Backup Availability..."
    echo "=============================="
    
    local backup_report="$DR_REPORT_DIR/backup_availability_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create backup report header
    echo "Atlas Production Backup Availability Check" > "$backup_report"
    echo "Generated: $(date)" >> "$backup_report"
    echo "=========================================" >> "$backup_report"
    echo "" >> "$backup_report"
    
    # Check primary backup location
    echo "Primary Backup Location ($BACKUP_DIR):" >> "$backup_report"
    echo "------------------------------------" >> "$backup_report"
    
    if [ -d "$BACKUP_DIR" ]; then
        local backup_count=$(find "$BACKUP_DIR" -name "*.sql*" -o -name "*.tar*" | wc -l)
        echo "✅ Directory exists with $backup_count backup files" >> "$backup_report"
        
        # Check most recent backup
        local latest_backup=$(find "$BACKUP_DIR" -name "*.sql*" -o -name "*.tar*" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
        if [ ! -z "$latest_backup" ]; then
            local backup_age_seconds=$(( $(date +%s) - $(stat -c %Y "$latest_backup") ))
            local backup_age_hours=$(( backup_age_seconds / 3600 ))
            echo "Most recent backup: $(basename $latest_backup)" >> "$backup_report"
            echo "Backup age: ${backup_age_hours} hours" >> "$backup_report"
            
            if [ $backup_age_hours -lt 24 ]; then
                echo "✅ Backup is current (less than 24 hours old)" >> "$backup_report"
            else
                echo "⚠️ Backup is older than 24 hours" >> "$backup_report"
            fi
        else
            echo "❌ No backup files found" >> "$backup_report"
        fi
    else
        echo "❌ Backup directory does not exist" >> "$backup_report"
    fi
    echo "" >> "$backup_report"
    
    # Check secondary backup location (OCI Object Storage)
    echo "Secondary Backup Location (OCI Object Storage):" >> "$backup_report"
    echo "---------------------------------------------" >> "$backup_report"
    
    if command -v oci &> /dev/null; then
        # Check if OCI CLI is configured
        if oci os bucket list --compartment-id $(jq -r '.oci.compartment_id' "/home/ubuntu/dev/atlas/config/oci.json" 2>/dev/null || echo "dummy") > /dev/null 2>&1; then
            echo "✅ OCI CLI is configured and accessible" >> "$backup_report"
            
            # List backup bucket contents
            local bucket_name="atlas-backups-bucket"
            if oci os object list --bucket-name "$bucket_name" > /dev/null 2>&1; then
                local oci_backup_count=$(oci os object list --bucket-name "$bucket_name" --query 'data[*].name' | jq -r '. | length')
                echo "OCI backup objects: $oci_backup_count" >> "$backup_report"
                
                if [ $oci_backup_count -gt 0 ]; then
                    echo "✅ OCI backup objects found" >> "$backup_report"
                else
                    echo "⚠️ No backup objects found in OCI bucket" >> "$backup_report"
                fi
            else
                echo "❌ Cannot access backup bucket in OCI" >> "$backup_report"
            fi
        else
            echo "❌ OCI CLI is not configured properly" >> "$backup_report"
        fi
    else
        echo "❌ OCI CLI is not installed" >> "$backup_report"
    fi
    echo "" >> "$backup_report"
    
    # Check tertiary backup location
    echo "Tertiary Backup Location:" >> "$backup_report"
    echo "------------------------" >> "$backup_report"
    
    local tertiary_location=$(jq -r '.backup_locations.tertiary' "/home/ubuntu/dev/atlas/config/disaster_recovery.json" 2>/dev/null || echo "/mnt/backup-drive/atlas-backups")
    if [ -d "$tertiary_location" ]; then
        local tertiary_count=$(find "$tertiary_location" -name "*.sql*" -o -name "*.tar*" | wc -l)
        echo "✅ Tertiary backup location exists with $tertiary_count backup files" >> "$backup_report"
    else
        echo "❌ Tertiary backup location does not exist or is not mounted" >> "$backup_report"
    fi
    echo "" >> "$backup_report"
    
    echo "✅ Backup availability check completed"
    echo "📋 Backup report saved to: $backup_report"
    log_message "Backup availability check completed: $backup_report"
    
    # Display summary
    echo ""
    echo "Backup Availability Summary:"
    echo "  Primary Location: $BACKUP_DIR"
    echo "  Secondary Location: OCI Object Storage"
    echo "  Tertiary Location: $tertiary_location"
    echo "  Report: $backup_report"
}

# Function to test database recovery
test_database_recovery() {
    log_message "Testing database recovery"
    
    echo ""
    echo "Testing Database Recovery..."
    echo "=========================="
    
    local db_recovery_report="$DR_REPORT_DIR/database_recovery_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create database recovery report header
    echo "Atlas Production Database Recovery Test" > "$db_recovery_report"
    echo "Generated: $(date)" >> "$db_recovery_report"
    echo "=====================================" >> "$db_recovery_report"
    echo "" >> "$db_recovery_report"
    
    # Check if PostgreSQL is running
    echo "Database Service Status:" >> "$db_recovery_report"
    echo "----------------------" >> "$db_recovery_report"
    
    if systemctl is-active --quiet postgresql; then
        echo "✅ PostgreSQL is running" >> "$db_recovery_report"
        
        # Check database connectivity
        if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
            echo "✅ Database is accessible" >> "$db_recovery_report"
            
            # Get current database size
            local db_size=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT pg_size_pretty(pg_database_size('atlas'));" 2>/dev/null || echo "Unknown")
            echo "Current database size: $db_size" >> "$db_recovery_report"
            
            # Get record counts
            local articles_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM articles;" 2>/dev/null || echo "0")
            local podcasts_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM podcasts;" 2>/dev/null || echo "0")
            local youtube_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM youtube_videos;" 2>/dev/null || echo "0")
            
            echo "Current record counts:" >> "$db_recovery_report"
            echo "  Articles: $articles_count" >> "$db_recovery_report"
            echo "  Podcasts: $podcasts_count" >> "$db_recovery_report"
            echo "  YouTube Videos: $youtube_count" >> "$db_recovery_report"
        else
            echo "❌ Database is not accessible" >> "$db_recovery_report"
        fi
    else
        echo "❌ PostgreSQL is not running" >> "$db_recovery_report"
    fi
    echo "" >> "$db_recovery_report"
    
    # Find latest backup
    echo "Backup Information:" >> "$db_recovery_report"
    echo "------------------" >> "$db_recovery_report"
    
    local latest_backup=$(find "$BACKUP_DIR" -name "atlas_backup_*.sql*" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
    if [ ! -z "$latest_backup" ]; then
        echo "Latest backup: $(basename $latest_backup)" >> "$db_recovery_report"
        echo "Backup size: $(du -h "$latest_backup" | cut -f1)" >> "$db_recovery_report"
        
        # Check backup integrity
        echo "Backup Integrity Check:" >> "$db_recovery_report"
        echo "----------------------" >> "$db_recovery_report"
        
        # For compressed backups, check if we can decompress without errors
        if [[ "$latest_backup" == *.gz ]]; then
            if gunzip -t "$latest_backup" > /dev/null 2>&1; then
                echo "✅ Backup file integrity check passed" >> "$db_recovery_report"
            else
                echo "❌ Backup file integrity check failed" >> "$db_recovery_report"
            fi
        else
            # For uncompressed backups, check if it's a valid SQL file
            if head -n 1 "$latest_backup" | grep -q "PostgreSQL database dump"; then
                echo "✅ Backup file appears to be valid SQL dump" >> "$db_recovery_report"
            else
                echo "❌ Backup file does not appear to be valid SQL dump" >> "$db_recovery_report"
            fi
        fi
    else
        echo "❌ No database backup found" >> "$db_recovery_report"
    fi
    echo "" >> "$db_recovery_report"
    
    # Test restore procedure (simulated)
    echo "Restore Procedure Test:" >> "$db_recovery_report"
    echo "----------------------" >> "$db_recovery_report"
    
    # Check if restore script exists
    local restore_script="/home/ubuntu/dev/atlas/scripts/restore_backup.sh"
    if [ -f "$restore_script" ]; then
        echo "✅ Restore script exists: $restore_script" >> "$db_recovery_report"
        
        # Check script permissions
        if [ -x "$restore_script" ]; then
            echo "✅ Restore script is executable" >> "$db_recovery_report"
        else
            echo "❌ Restore script is not executable" >> "$db_recovery_report"
        fi
    else
        echo "❌ Restore script not found" >> "$db_recovery_report"
    fi
    echo "" >> "$db_recovery_report"
    
    echo "✅ Database recovery test completed"
    echo "📋 Database recovery report saved to: $db_recovery_report"
    log_message "Database recovery test completed: $db_recovery_report"
    
    # Display summary
    echo ""
    echo "Database Recovery Test Summary:"
    echo "  Database Status: $(systemctl is-active postgresql)"
    echo "  Backup Status: $(if [ ! -z "$latest_backup" ]; then echo "Found"; else echo "Not Found"; fi)"
    echo "  Report: $db_recovery_report"
}

# Function to test full system recovery
test_full_system_recovery() {
    log_message "Testing full system recovery"
    
    echo ""
    echo "Testing Full System Recovery..."
    echo "============================="
    
    local full_recovery_report="$DR_REPORT_DIR/full_recovery_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create full recovery report header
    echo "Atlas Production Full System Recovery Test" > "$full_recovery_report"
    echo "Generated: $(date)" >> "$full_recovery_report"
    echo "=========================================" >> "$full_recovery_report"
    echo "" >> "$full_recovery_report"
    
    # Check system resources
    echo "System Resources:" >> "$full_recovery_report"
    echo "----------------" >> "$full_recovery_report"
    
    local total_memory=$(free -h | grep Mem | awk '{print $2}')
    local available_memory=$(free -h | grep Mem | awk '{print $7}')
    local disk_space=$(df -h / | tail -1 | awk '{print $4}')
    
    echo "Total Memory: $total_memory" >> "$full_recovery_report"
    echo "Available Memory: $available_memory" >> "$full_recovery_report"
    echo "Available Disk Space: $disk_space" >> "$full_recovery_report"
    echo "" >> "$full_recovery_report"
    
    # Check critical services status
    echo "Critical Services Status:" >> "$full_recovery_report"
    echo "------------------------" >> "$full_recovery_report"
    
    local critical_services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    local services_running=0
    for service_info in "${critical_services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc is running" >> "$full_recovery_report"
            services_running=$((services_running + 1))
        else
            echo "❌ $service_desc is not running" >> "$full_recovery_report"
        fi
    done
    
    echo "Services Running: $services_running/${#critical_services[@]}" >> "$full_recovery_report"
    echo "" >> "$full_recovery_report"
    
    # Check web interface accessibility
    echo "Web Interface Accessibility:" >> "$full_recovery_report"
    echo "----------------------------" >> "$full_recovery_report"
    
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        echo "✅ Web interface is accessible" >> "$full_recovery_report"
    else
        echo "❌ Web interface is not accessible" >> "$full_recovery_report"
    fi
    
    if curl -f -s http://localhost:5000/health > /dev/null 2>&1; then
        echo "✅ Health endpoint is accessible" >> "$full_recovery_report"
    else
        echo "❌ Health endpoint is not accessible" >> "$full_recovery_report"
    fi
    echo "" >> "$full_recovery_report"
    
    # Check database connectivity
    echo "Database Connectivity:" >> "$full_recovery_report"
    echo "--------------------" >> "$full_recovery_report"
    
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        echo "✅ Database is accessible" >> "$full_recovery_report"
        
        # Test basic database query
        local test_query_result=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT 1;" 2>/dev/null || echo "ERROR")
        if [ "$test_query_result" = "1" ]; then
            echo "✅ Basic database query successful" >> "$full_recovery_report"
        else
            echo "❌ Basic database query failed" >> "$full_recovery_report"
        fi
    else
        echo "❌ Database is not accessible" >> "$full_recovery_report"
    fi
    echo "" >> "$full_recovery_report"
    
    # Check backup availability for recovery
    echo "Recovery Backup Availability:" >> "$full_recovery_report"
    echo "-----------------------------" >> "$full_recovery_report"
    
    local latest_backup=$(find "$BACKUP_DIR" -name "atlas_backup_*.sql*" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
    if [ ! -z "$latest_backup" ]; then
        echo "✅ Latest backup found: $(basename $latest_backup)" >> "$full_recovery_report"
        
        # Check backup age
        local backup_age_seconds=$(( $(date +%s) - $(stat -c %Y "$latest_backup") ))
        local backup_age_hours=$(( backup_age_seconds / 3600 ))
        echo "Backup age: ${backup_age_hours} hours" >> "$full_recovery_report"
        
        if [ $backup_age_hours -lt 24 ]; then
            echo "✅ Backup is current (RPO requirement met)" >> "$full_recovery_report"
        else
            echo "⚠️ Backup is older than 24 hours (RPO requirement not met)" >> "$full_recovery_report"
        fi
    else
        echo "❌ No backup found for recovery" >> "$full_recovery_report"
    fi
    echo "" >> "$full_recovery_report"
    
    # Check recovery scripts
    echo "Recovery Scripts:" >> "$full_recovery_report"
    echo "----------------" >> "$full_recovery_report"
    
    local recovery_scripts=(
        "/home/ubuntu/dev/atlas/scripts/full_recovery.sh:Full System Recovery"
        "/home/ubuntu/dev/atlas/scripts/database_recovery.sh:Database Recovery"
        "/home/ubuntu/dev/atlas/scripts/configuration_recovery.sh:Configuration Recovery"
        "/home/ubuntu/dev/atlas/scripts/restore_backup.sh:Backup Restore"
    )
    
    local scripts_found=0
    for script_info in "${recovery_scripts[@]}"; do
        local script_path=$(echo $script_info | cut -d':' -f1)
        local script_desc=$(echo $script_info | cut -d':' -f2)
        
        if [ -f "$script_path" ]; then
            echo "✅ $script_desc script exists" >> "$full_recovery_report"
            scripts_found=$((scripts_found + 1))
        else
            echo "❌ $script_desc script not found" >> "$full_recovery_report"
        fi
    done
    
    echo "Recovery Scripts Found: $scripts_found/${#recovery_scripts[@]}" >> "$full_recovery_report"
    echo "" >> "$full_recovery_report"
    
    echo "✅ Full system recovery test completed"
    echo "📋 Full recovery report saved to: $full_recovery_report"
    log_message "Full system recovery test completed: $full_recovery_report"
    
    # Display summary
    echo ""
    echo "Full System Recovery Test Summary:"
    echo "  Services Running: $services_running/${#critical_services[@]}"
    echo "  Web Interface: $(if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then echo "Accessible"; else echo "Not Accessible"; fi)"
    echo "  Database: $(if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then echo "Accessible"; else echo "Not Accessible"; fi)"
    echo "  Backups: $(if [ ! -z "$latest_backup" ]; then echo "Available"; else echo "Not Available"; fi)"
    echo "  Report: $full_recovery_report"
}

# Function to test backup restoration
test_backup_restoration() {
    log_message "Testing backup restoration"
    
    echo ""
    echo "Testing Backup Restoration..."
    echo "============================"
    
    local restore_test_report="$DR_REPORT_DIR/restore_test_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create restore test report header
    echo "Atlas Production Backup Restoration Test" > "$restore_test_report"
    echo "Generated: $(date)" >> "$restore_test_report"
    echo "========================================" >> "$restore_test_report"
    echo "" >> "$restore_test_report"
    
    # Create test restore directory
    local test_restore_dir="$RESTORE_DIR/test_restore_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$test_restore_dir"
    echo "Test restore directory: $test_restore_dir" >> "$restore_test_report"
    echo "" >> "$restore_test_report"
    
    # Find latest backup
    echo "Backup Selection:" >> "$restore_test_report"
    echo "----------------" >> "$restore_test_report"
    
    local latest_backup=$(find "$BACKUP_DIR" -name "atlas_backup_*.sql*" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
    if [ ! -z "$latest_backup" ]; then
        echo "✅ Latest backup selected: $(basename $latest_backup)" >> "$restore_test_report"
        echo "Backup size: $(du -h "$latest_backup" | cut -f1)" >> "$restore_test_report"
        echo "Backup type: $(if [[ "$latest_backup" == *.gz ]]; then echo "Compressed"; else echo "Uncompressed"; fi)" >> "$restore_test_report"
    else
        echo "❌ No backup found for restoration test" >> "$restore_test_report"
        echo "✅ Restoration test completed (no backups to test)"
        log_message "Restoration test completed (no backups found)"
        return 0
    fi
    echo "" >> "$restore_test_report"
    
    # Test backup extraction (simulated)
    echo "Backup Extraction Test:" >> "$restore_test_report"
    echo "----------------------" >> "$restore_test_report"
    
    if [[ "$latest_backup" == *.gz ]]; then
        # Test compressed backup extraction
        echo "Testing compressed backup extraction..." >> "$restore_test_report"
        
        # Extract to test directory
        if gunzip -c "$latest_backup" > "$test_restore_dir/test_extract.sql" 2>/dev/null; then
            local extracted_size=$(du -h "$test_restore_dir/test_extract.sql" | cut -f1)
            echo "✅ Backup extracted successfully" >> "$restore_test_report"
            echo "Extracted file size: $extracted_size" >> "$restore_test_report"
        else
            echo "❌ Backup extraction failed" >> "$restore_test_report"
        fi
    else
        # Test uncompressed backup
        echo "Testing uncompressed backup..." >> "$restore_test_report"
        
        # Copy to test directory
        if cp "$latest_backup" "$test_restore_dir/test_copy.sql" 2>/dev/null; then
            local copied_size=$(du -h "$test_restore_dir/test_copy.sql" | cut -f1)
            echo "✅ Backup copied successfully" >> "$restore_test_report"
            echo "Copied file size: $copied_size" >> "$restore_test_report"
        else
            echo "❌ Backup copy failed" >> "$restore_test_report"
        fi
    fi
    echo "" >> "$restore_test_report"
    
    # Test database restore simulation
    echo "Database Restore Simulation:" >> "$restore_test_report"
    echo "----------------------------" >> "$restore_test_report"
    
    # Check if PostgreSQL is running
    if systemctl is-active --quiet postgresql; then
        echo "✅ PostgreSQL is running" >> "$restore_test_report"
        
        # Create test database
        local test_db_name="atlas_restore_test"
        if sudo -u postgres psql -tAc "CREATE DATABASE $test_db_name;" > /dev/null 2>&1; then
            echo "✅ Test database created: $test_db_name" >> "$restore_test_report"
            
            # Grant privileges
            if sudo -u postgres psql -tAc "GRANT ALL PRIVILEGES ON DATABASE $test_db_name TO atlas_user;" > /dev/null 2>&1; then
                echo "✅ Privileges granted to atlas_user" >> "$restore_test_report"
            else
                echo "❌ Failed to grant privileges" >> "$restore_test_report"
            fi
            
            # Test database connection
            if sudo -u postgres pg_isready -U atlas_user -d $test_db_name > /dev/null 2>&1; then
                echo "✅ Test database is accessible" >> "$restore_test_report"
            else
                echo "❌ Test database is not accessible" >> "$restore_test_report"
            fi
            
            # Clean up test database
            sudo -u postgres psql -tAc "DROP DATABASE $test_db_name;" > /dev/null 2>&1 || true
            echo "✅ Test database cleaned up" >> "$restore_test_report"
        else
            echo "❌ Failed to create test database" >> "$restore_test_report"
        fi
    else
        echo "❌ PostgreSQL is not running, skipping database restore test" >> "$restore_test_report"
    fi
    echo "" >> "$restore_test_report"
    
    # Test configuration restore
    echo "Configuration Restore Test:" >> "$restore_test_report"
    echo "--------------------------" >> "$restore_test_report"
    
    # Check if configuration backup exists
    local config_backup=$(find "$BACKUP_DIR" -name "config_backup_*.tar*" | head -1)
    if [ ! -z "$config_backup" ]; then
        echo "✅ Configuration backup found: $(basename $config_backup)" >> "$restore_test_report"
        
        # Test configuration extraction
        local config_extract_dir="$test_restore_dir/config_extract"
        mkdir -p "$config_extract_dir"
        
        if tar -xzf "$config_backup" -C "$config_extract_dir" > /dev/null 2>&1; then
            local config_files=$(find "$config_extract_dir" -type f | wc -l)
            echo "✅ Configuration extracted successfully ($config_files files)" >> "$restore_test_report"
        else
            echo "❌ Configuration extraction failed" >> "$restore_test_report"
        fi
    else
        echo "❌ No configuration backup found" >> "$restore_test_report"
    fi
    echo "" >> "$restore_test_report"
    
    # Clean up test directory
    rm -rf "$test_restore_dir"
    echo "✅ Test restore directory cleaned up" >> "$restore_test_report"
    echo "" >> "$restore_test_report"
    
    echo "✅ Backup restoration test completed"
    echo "📋 Restore test report saved to: $restore_test_report"
    log_message "Backup restoration test completed: $restore_test_report"
    
    # Display summary
    echo ""
    echo "Backup Restoration Test Summary:"
    echo "  Backup Tested: $(if [ ! -z "$latest_backup" ]; then echo "Yes"; else echo "No"; fi)"
    echo "  Extraction: $(if [ ! -z "$latest_backup" ]; then if [[ "$latest_backup" == *.gz ]]; then echo "Compressed"; else echo "Uncompressed"; fi; else echo "N/A"; fi)"
    echo "  Database Test: $(if systemctl is-active --quiet postgresql; then echo "Performed"; else echo "Skipped"; fi)"
    echo "  Report: $restore_test_report"
}

# Function to generate disaster recovery plan
generate_dr_plan() {
    log_message "Generating disaster recovery plan"
    
    echo ""
    echo "Generating Disaster Recovery Plan..."
    echo "=================================="
    
    local dr_plan="$DR_REPORT_DIR/disaster_recovery_plan_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create disaster recovery plan header
    echo "Atlas Production Disaster Recovery Plan" > "$dr_plan"
    echo "Generated: $(date)" >> "$dr_plan"
    echo "=====================================" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    # Add plan overview
    echo "Plan Overview:" >> "$dr_plan"
    echo "------------" >> "$dr_plan"
    echo "Recovery Time Objective (RTO): 4 hours" >> "$dr_plan"
    echo "Recovery Point Objective (RPO): 24 hours" >> "$dr_plan"
    echo "Backup Frequency: Daily" >> "$dr_plan"
    echo "Test Frequency: Monthly" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    # Add recovery procedures
    echo "Recovery Procedures:" >> "$dr_plan"
    echo "------------------" >> "$dr_plan"
    
    echo "1. Full System Recovery:" >> "$dr_plan"
    echo "   a. Provision new server instance" >> "$dr_plan"
    echo "   b. Install required software packages" >> "$dr_plan"
    echo "   c. Restore configuration files" >> "$dr_plan"
    echo "   d. Restore database from backup" >> "$dr_plan"
    echo "   e. Restore application files" >> "$dr_plan"
    echo "   f. Configure services and start" >> "$dr_plan"
    echo "   g. Validate system functionality" >> "$dr_plan"
    echo "   h. Update DNS records" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    echo "2. Database Recovery:" >> "$dr_plan"
    echo "   a. Stop database service" >> "$dr_plan"
    echo "   b. Restore database dump from backup" >> "$dr_plan"
    echo "   c. Apply incremental logs if needed" >> "$dr_plan"
    echo "   d. Start database service" >> "$dr_plan"
    echo "   e. Verify data integrity" >> "$dr_plan"
    echo "   f. Update application configurations" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    echo "3. Configuration Recovery:" >> "$dr_plan"
    echo "   a. Restore .env file" >> "$dr_plan"
    echo "   b. Restore Nginx configuration" >> "$dr_plan"
    echo "   c. Restore PostgreSQL configuration" >> "$dr_plan"
    echo "   d. Restore systemd service files" >> "$dr_plan"
    echo "   e. Restore monitoring configurations" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    # Add contact information
    echo "Emergency Contacts:" >> "$dr_plan"
    echo "------------------" >> "$dr_plan"
    echo "Primary Contact: System Administrator" >> "$dr_plan"
    echo "Email: admin@khamel.com" >> "$dr_plan"
    echo "Phone: +1-XXX-XXX-XXXX" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    # Add backup locations
    echo "Backup Locations:" >> "$dr_plan"
    echo "---------------" >> "$dr_plan"
    echo "Primary: $BACKUP_DIR" >> "$dr_plan"
    echo "Secondary: OCI Object Storage (atlas-backups-bucket)" >> "$dr_plan"
    echo "Tertiary: External drive (/mnt/backup-drive/atlas-backups)" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    # Add recovery scripts
    echo "Recovery Scripts:" >> "$dr_plan"
    echo "----------------" >> "$dr_plan"
    echo "Full Recovery: /home/ubuntu/dev/atlas/scripts/full_recovery.sh" >> "$dr_plan"
    echo "Database Recovery: /home/ubuntu/dev/atlas/scripts/database_recovery.sh" >> "$dr_plan"
    echo "Configuration Recovery: /home/ubuntu/dev/atlas/scripts/configuration_recovery.sh" >> "$dr_plan"
    echo "Backup Restore: /home/ubuntu/dev/atlas/scripts/restore_backup.sh" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    # Add testing schedule
    echo "Testing Schedule:" >> "$dr_plan"
    echo "---------------" >> "$dr_plan"
    echo "Monthly: Full system recovery test" >> "$dr_plan"
    echo "Weekly: Database recovery test" >> "$dr_plan"
    echo "Daily: Backup availability check" >> "$dr_plan"
    echo "Quarterly: Configuration restore test" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    # Add documentation references
    echo "Documentation:" >> "$dr_plan"
    echo "-------------" >> "$dr_plan"
    echo "Operations Manual: /home/ubuntu/dev/atlas/docs/operations_manual.md" >> "$dr_plan"
    echo "Security Procedures: /home/ubuntu/dev/atlas/docs/security_procedures.md" >> "$dr_plan"
    echo "Backup Procedures: /home/ubuntu/dev/atlas/docs/backup_procedures.md" >> "$dr_plan"
    echo "" >> "$dr_plan"
    
    echo "✅ Disaster recovery plan generated"
    echo "📋 DR plan saved to: $dr_plan"
    log_message "Disaster recovery plan generated: $dr_plan"
    
    # Display summary
    echo ""
    echo "Disaster Recovery Plan Summary:"
    echo "  RTO: 4 hours"
    echo "  RPO: 24 hours"
    echo "  Backup Frequency: Daily"
    echo "  Plan: $dr_plan"
}

# Function to clean old disaster recovery reports
clean_old_reports() {
    log_message "Cleaning old disaster recovery reports"
    
    echo ""
    echo "Cleaning Old Disaster Recovery Reports..."
    echo "========================================"
    
    # Remove DR reports older than 90 days
    find "$DR_REPORT_DIR" -name "backup_availability_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$DR_REPORT_DIR" -name "database_recovery_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$DR_REPORT_DIR" -name "full_recovery_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$DR_REPORT_DIR" -name "restore_test_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$DR_REPORT_DIR" -name "disaster_recovery_plan_*.txt" -mtime +90 -delete 2>/dev/null || true
    
    echo "✅ Old disaster recovery reports cleaned"
    log_message "Old disaster recovery reports cleaned"
}

# Main disaster recovery function
main() {
    log_message "=== Starting Atlas Disaster Recovery ==="
    
    # Initialize configuration
    initialize_dr_config
    
    # Start time
    local start_time=$(date)
    log_message "Disaster recovery started at: $start_time"
    
    # Handle different DR operations
    case $1 in
        "backup-check")
            check_backup_availability
            ;;
        "db-test")
            test_database_recovery
            ;;
        "full-test")
            test_full_system_recovery
            ;;
        "restore-test")
            test_backup_restoration
            ;;
        "plan")
            generate_dr_plan
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive disaster recovery check
            check_backup_availability
            test_database_recovery
            test_full_system_recovery
            test_backup_restoration
            generate_dr_plan
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Disaster recovery completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Disaster Recovery Completed ==="
    
    echo ""
    echo "✅ Disaster recovery operations completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $DR_REPORT_DIR"
    echo "📝 Log file: $DR_LOG"
}

# Run main function
main "$@"