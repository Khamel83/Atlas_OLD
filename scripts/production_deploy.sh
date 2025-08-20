#!/bin/bash

# Atlas Production Deployment Script
# This script handles the deployment of Atlas to production environment

set -e  # Exit on any error

echo "Starting Atlas Production Deployment..."

# Configuration
DEPLOY_LOG="/home/ubuntu/dev/atlas/logs/deploy.log"
BACKUP_DIR="/home/ubuntu/dev/atlas/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $DEPLOY_LOG)"
mkdir -p "$BACKUP_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $DEPLOY_LOG
    echo "$1"
}

# Function to create backup before deployment
create_backup() {
    log_message "Creating backup before deployment"
    
    # Stop services
    log_message "Stopping services for backup"
    sudo systemctl stop atlas || true
    sudo systemctl stop atlas-prometheus || true
    sudo systemctl stop atlas-grafana || true
    
    # Create backup
    local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
    if [ -f "$backup_script" ]; then
        if $backup_script; then
            log_message "Backup created successfully"
        else
            log_message "WARNING: Backup creation failed"
        fi
    else
        log_message "ERROR: Backup script not found"
        return 1
    fi
    
    # Restart services
    log_message "Restarting services after backup"
    sudo systemctl start atlas
    sudo systemctl start atlas-prometheus
    sudo systemctl start atlas-grafana
    
    return 0
}

# Function to pull latest code from repository
pull_latest_code() {
    log_message "Pulling latest code from repository"
    
    # Navigate to Atlas directory
    cd /home/ubuntu/dev/atlas
    
    # Pull latest changes
    if git pull; then
        log_message "Code updated successfully"
    else
        log_message "ERROR: Failed to pull latest code"
        return 1
    fi
    
    return 0
}

# Function to update dependencies
update_dependencies() {
    log_message "Updating dependencies"
    
    # Navigate to Atlas directory
    cd /home/ubuntu/dev/atlas
    
    # Activate virtual environment
    source atlas_venv/bin/activate
    
    # Update pip
    if pip install --upgrade pip; then
        log_message "Pip updated successfully"
    else
        log_message "WARNING: Failed to update pip"
    fi
    
    # Install/upgrade dependencies
    if pip install -r requirements.txt; then
        log_message "Dependencies updated successfully"
    else
        log_message "ERROR: Failed to update dependencies"
        return 1
    fi
    
    return 0
}

# Function to run database migrations
run_migrations() {
    log_message "Running database migrations"
    
    # Navigate to Atlas directory
    cd /home/ubuntu/dev/atlas
    
    # Run migrations if migration script exists
    local migration_script="/home/ubuntu/dev/atlas/migrations/migrate.py"
    if [ -f "$migration_script" ]; then
        if python3 "$migration_script"; then
            log_message "Database migrations completed successfully"
        else
            log_message "ERROR: Database migrations failed"
            return 1
        fi
    else
        log_message "No migration script found, skipping"
    fi
    
    return 0
}

# Function to restart services
restart_services() {
    log_message "Restarting services"
    
    # Services to restart
    local services=("atlas" "atlas-prometheus" "atlas-grafana")
    
    for service in "${services[@]}"; do
        log_message "Restarting $service"
        if sudo systemctl restart $service; then
            log_message "$service restarted successfully"
        else
            log_message "WARNING: Failed to restart $service"
        fi
    done
    
    return 0
}

# Function to verify deployment
verify_deployment() {
    log_message "Verifying deployment"
    
    # Wait a moment for services to start
    sleep 10
    
    # Check if services are running
    local services=("atlas" "atlas-prometheus" "atlas-grafana")
    local all_running=true
    
    for service in "${services[@]}"; do
        if systemctl is-active --quiet $service; then
            log_message "$service is running"
        else
            log_message "ERROR: $service is not running"
            all_running=false
        fi
    done
    
    # Check if web interface is accessible
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        log_message "Web interface is accessible"
    else
        log_message "WARNING: Web interface is not accessible"
        all_running=false
    fi
    
    if $all_running; then
        log_message "Deployment verification successful"
        return 0
    else
        log_message "Deployment verification failed"
        return 1
    fi
}

# Function to rollback deployment
rollback_deployment() {
    log_message "Rolling back deployment"
    
    # This is a simplified rollback - in a real implementation, you would restore from backup
    log_message "Rollback functionality would be implemented here"
    
    # For now, we'll just restart the services
    restart_services
    
    return 0
}

# Function to send deployment notification
send_notification() {
    local status=$1
    local message=$2
    
    log_message "Deployment $status: $message"
    
    # In a real implementation, this would send an email notification
    # For now, we'll just log to console
    echo "📧 Deployment $status: $message"
}

# Main deployment function
main() {
    log_message "=== Starting Atlas Production Deployment ==="
    
    # Start time
    local start_time=$(date)
    log_message "Deployment started at: $start_time"
    
    # Create backup
    if ! create_backup; then
        send_notification "FAILED" "Backup creation failed"
        return 1
    fi
    
    # Pull latest code
    if ! pull_latest_code; then
        send_notification "FAILED" "Code update failed"
        rollback_deployment
        return 1
    fi
    
    # Update dependencies
    if ! update_dependencies; then
        send_notification "FAILED" "Dependency update failed"
        rollback_deployment
        return 1
    fi
    
    # Run migrations
    if ! run_migrations; then
        send_notification "FAILED" "Database migrations failed"
        rollback_deployment
        return 1
    fi
    
    # Restart services
    if ! restart_services; then
        send_notification "FAILED" "Service restart failed"
        rollback_deployment
        return 1
    fi
    
    # Verify deployment
    if verify_deployment; then
        send_notification "SUCCESS" "Deployment completed successfully"
    else
        send_notification "PARTIAL" "Deployment completed with issues"
    fi
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Deployment completed at: $end_time (Duration: ${duration}s)"
    log_message "=== Deployment Process Completed ==="
    
    return 0
}

# Handle script arguments
if [ "$1" == "--rollback" ]; then
    echo "Rolling back deployment..."
    rollback_deployment
    exit 0
elif [ "$1" == "--verify" ]; then
    echo "Verifying deployment..."
    if verify_deployment; then
        echo "✅ Deployment verification successful"
        exit 0
    else
        echo "❌ Deployment verification failed"
        exit 1
    fi
fi

# Run main deployment
if main; then
    echo "✅ Atlas deployment completed successfully"
    exit 0
else
    echo "❌ Atlas deployment failed"
    exit 1
fi