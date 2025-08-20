#!/bin/bash

# Atlas Production Recovery Script
# This script helps recover Atlas production environment in case of failures

set -e  # Exit on any error

echo "Atlas Production Recovery System"
echo "================================"

# Function to restore from backup
restore_from_backup() {
    echo "Starting backup restoration..."
    
    # Check if backup directory exists
    if [ ! -d "/home/ubuntu/dev/atlas/backups" ]; then
        echo "❌ Backup directory not found!"
        return 1
    fi
    
    # List available backups
    echo "Available backups:"
    ls -t /home/ubuntu/dev/atlas/backups/*.sql.gz.enc 2>/dev/null || echo "No encrypted backups found"
    ls -t /home/ubuntu/dev/atlas/backups/*.sql.gz 2>/dev/null || echo "No compressed backups found"
    ls -t /home/ubuntu/dev/atlas/backups/*.sql 2>/dev/null || echo "No uncompressed backups found"
    
    echo "Please select a backup file to restore:"
    read -p "Backup file path: " backup_file
    
    if [ ! -f "$backup_file" ]; then
        echo "❌ Backup file not found!"
        return 1
    fi
    
    # Stop services
    echo "Stopping Atlas services..."
    sudo systemctl stop atlas || true
    sudo systemctl stop atlas-prometheus || true
    sudo systemctl stop atlas-grafana || true
    
    # Restore database
    echo "Restoring database from $backup_file..."
    
    # Handle different backup formats
    if [[ "$backup_file" == *.enc ]]; then
        echo "Decrypting backup..."
        # This would require the encryption key
        echo "❌ Encrypted backups require manual decryption first"
        return 1
    elif [[ "$backup_file" == *.gz ]]; then
        echo "Decompressing backup..."
        gunzip -c "$backup_file" > "/tmp/restore.sql"
        restore_file="/tmp/restore.sql"
    else
        restore_file="$backup_file"
    fi
    
    # Drop and recreate database
    echo "Recreating database..."
    sudo -u postgres psql -c "DROP DATABASE IF EXISTS atlas;" || true
    sudo -u postgres psql -c "CREATE DATABASE atlas OWNER atlas_user;" || true
    
    # Restore database
    echo "Restoring database contents..."
    sudo -u postgres psql -U atlas_user -d atlas -f "$restore_file"
    
    # Clean up temporary files
    if [ "$restore_file" == "/tmp/restore.sql" ]; then
        rm "$restore_file"
    fi
    
    # Restart services
    echo "Restarting Atlas services..."
    sudo systemctl start atlas
    sudo systemctl start atlas-prometheus
    sudo systemctl start atlas-grafana
    
    echo "✅ Database restoration completed!"
}

# Function to restart all services
restart_all_services() {
    echo "Restarting all Atlas services..."
    
    services=("atlas" "atlas-prometheus" "atlas-grafana" "postgresql" "nginx")
    
    for service in "${services[@]}"; do
        echo "Restarting $service..."
        sudo systemctl restart $service || echo "⚠️  Failed to restart $service"
    done
    
    echo "✅ All services restarted!"
}

# Function to clear logs and temp files
clear_logs_and_temp() {
    echo "Clearing logs and temporary files..."
    
    # Clear Atlas logs
    if [ -d "/home/ubuntu/dev/atlas/logs" ]; then
        rm -f /home/ubuntu/dev/atlas/logs/*.log
        echo "✅ Atlas logs cleared"
    fi
    
    # Clear system logs
    sudo journalctl --vacuum-time=1d
    echo "✅ System logs cleared"
    
    # Clear temporary files
    sudo find /tmp -type f -mtime +7 -delete
    echo "✅ Temporary files cleared"
}

# Function to check and fix permissions
fix_permissions() {
    echo "Fixing file permissions..."
    
    # Set ownership for Atlas directory
    sudo chown -R ubuntu:ubuntu /home/ubuntu/dev/atlas
    echo "✅ Atlas directory ownership fixed"
    
    # Set permissions for sensitive files
    if [ -f "/home/ubuntu/dev/atlas/.env" ]; then
        chmod 600 /home/ubuntu/dev/atlas/.env
        echo "✅ Environment file permissions fixed"
    fi
    
    # Set permissions for backup files
    if [ -d "/home/ubuntu/dev/atlas/backups" ]; then
        chmod 600 /home/ubuntu/dev/atlas/backups/*
        echo "✅ Backup file permissions fixed"
    fi
}

# Function to reinstall dependencies
reinstall_dependencies() {
    echo "Reinstalling dependencies..."
    
    # Activate virtual environment
    cd /home/ubuntu/dev/atlas
    source atlas_venv/bin/activate
    
    # Reinstall Python dependencies
    pip install --upgrade pip
    pip install -r requirements.txt
    
    echo "✅ Dependencies reinstalled"
}

# Function to reset database
reset_database() {
    echo "Resetting database..."
    
    # Stop services
    sudo systemctl stop atlas || true
    
    # Drop and recreate database
    sudo -u postgres psql -c "DROP DATABASE IF EXISTS atlas;" || true
    sudo -u postgres psql -c "CREATE DATABASE atlas OWNER atlas_user;" || true
    
    # Restart service
    sudo systemctl start atlas
    
    echo "✅ Database reset completed"
}

# Function to update system
update_system() {
    echo "Updating system packages..."
    
    sudo apt update
    sudo apt upgrade -y
    
    echo "✅ System updated"
}

# Main menu
show_menu() {
    echo ""
    echo "Recovery Options:"
    echo "1. Restore from backup"
    echo "2. Restart all services"
    echo "3. Clear logs and temporary files"
    echo "4. Fix file permissions"
    echo "5. Reinstall dependencies"
    echo "6. Reset database"
    echo "7. Update system"
    echo "8. Run full recovery (options 2-7)"
    echo "9. Exit"
    echo ""
}

# Full recovery function
full_recovery() {
    echo "Running full recovery..."
    restart_all_services
    clear_logs_and_temp
    fix_permissions
    reinstall_dependencies
    update_system
    echo "✅ Full recovery completed!"
}

# Main execution
while true; do
    show_menu
    read -p "Select an option (1-9): " choice
    
    case $choice in
        1)
            restore_from_backup
            ;;
        2)
            restart_all_services
            ;;
        3)
            clear_logs_and_temp
            ;;
        4)
            fix_permissions
            ;;
        5)
            reinstall_dependencies
            ;;
        6)
            reset_database
            ;;
        7)
            update_system
            ;;
        8)
            full_recovery
            ;;
        9)
            echo "Exiting recovery system..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please select 1-9."
            ;;
    esac
done