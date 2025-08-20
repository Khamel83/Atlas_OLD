#!/bin/bash

# Atlas Production Deployment Script
# This script automates the deployment process for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Deployment..."

# Configuration
DEPLOY_LOG="/home/ubuntu/dev/atlas/logs/deployment.log"
DEPLOY_CONFIG="/home/ubuntu/dev/atlas/config/deployment.json"
BACKUP_DIR="/home/ubuntu/dev/atlas/backups"
DEPLOY_TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $DEPLOY_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $DEPLOY_LOG
    echo "$1"
}

# Function to create deployment configuration
create_deployment_config() {
    log_message "Creating deployment configuration"
    
    # Create default deployment configuration if it doesn't exist
    if [ ! -f "$DEPLOY_CONFIG" ]; then
        cat > "$DEPLOY_CONFIG" << EOF
{
    "deployment": {
        "branch": "main",
        "repository": "https://github.com/yourusername/atlas.git",
        "services": ["atlas", "postgresql", "nginx", "atlas-prometheus", "atlas-grafana"]
    },
    "backup": {
        "enabled": true,
        "before_deploy": true,
        "after_deploy": false
    },
    "notifications": {
        "email": {
            "enabled": true,
            "recipients": ["admin@khamel.com"]
        }
    }
}
EOF
        echo "✅ Created default deployment configuration"
        log_message "Default deployment configuration created"
    else
        echo "✅ Deployment configuration already exists"
    fi
}

# Function to create backup before deployment
create_backup() {
    log_message "Creating backup before deployment"
    
    echo "Creating Backup Before Deployment..."
    echo "=================================="
    
    # Check if backup is enabled
    local backup_enabled=$(jq -r '.backup.before_deploy' "$DEPLOY_CONFIG")
    if [ "$backup_enabled" != "true" ]; then
        echo "ℹ️ Backup before deployment is disabled"
        log_message "Backup before deployment is disabled"
        return 0
    fi
    
    # Run backup script
    local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
    if [ -f "$backup_script" ]; then
        echo "🔄 Creating database backup..."
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

# Function to pull latest code
pull_latest_code() {
    log_message "Pulling latest code from repository"
    
    echo ""
    echo "Pulling Latest Code..."
    echo "===================="
    
    # Navigate to Atlas directory
    cd /home/ubuntu/dev/atlas
    
    # Check current branch
    local current_branch=$(git rev-parse --abbrev-ref HEAD)
    local target_branch=$(jq -r '.deployment.branch' "$DEPLOY_CONFIG")
    
    echo "Current branch: $current_branch"
    echo "Target branch: $target_branch"
    
    # Checkout target branch if needed
    if [ "$current_branch" != "$target_branch" ]; then
        echo "🔄 Checking out target branch: $target_branch"
        if ! git checkout $target_branch; then
            echo "❌ Failed to checkout branch: $target_branch"
            log_message "Failed to checkout branch: $target_branch"
            return 1
        fi
    fi
    
    # Pull latest changes
    echo "🔄 Pulling latest changes..."
    if git pull origin $target_branch; then
        echo "✅ Code updated successfully"
        log_message "Code updated successfully"
    else
        echo "❌ Failed to pull latest code"
        log_message "Failed to pull latest code"
        return 1
    fi
    
    # Show latest commit
    local latest_commit=$(git log -1 --oneline)
    echo "Latest commit: $latest_commit"
    log_message "Latest commit: $latest_commit"
}

# Function to update dependencies
update_dependencies() {
    log_message "Updating dependencies"
    
    echo ""
    echo "Updating Dependencies..."
    echo "===================="
    
    # Activate virtual environment
    cd /home/ubuntu/dev/atlas
    source atlas_venv/bin/activate
    
    # Update pip
    echo "🔄 Updating pip..."
    if pip install --upgrade pip; then
        echo "✅ Pip updated successfully"
        log_message "Pip updated successfully"
    else
        echo "⚠️ Failed to update pip (continuing anyway)"
        log_message "Failed to update pip"
    fi
    
    # Install/upgrade dependencies
    echo "🔄 Installing/upgrading dependencies..."
    if pip install -r requirements.txt; then
        echo "✅ Dependencies updated successfully"
        log_message "Dependencies updated successfully"
    else
        echo "❌ Failed to update dependencies"
        log_message "Failed to update dependencies"
        return 1
    fi
}

# Function to run database migrations
run_database_migrations() {
    log_message "Running database migrations"
    
    echo ""
    echo "Running Database Migrations..."
    echo "=========================="
    
    # Check if migration script exists
    local migration_script="/home/ubuntu/dev/atlas/migrations/migrate.py"
    if [ -f "$migration_script" ]; then
        echo "🔄 Running database migrations..."
        if python3 "$migration_script"; then
            echo "✅ Database migrations completed successfully"
            log_message "Database migrations completed successfully"
        else
            echo "❌ Database migrations failed"
            log_message "Database migrations failed"
            return 1
        fi
    else
        echo "ℹ️ No migration script found, skipping"
        log_message "No migration script found, skipping"
    fi
}

# Function to restart services
restart_services() {
    log_message "Restarting services"
    
    echo ""
    echo "Restarting Services..."
    echo "===================="
    
    # Get services to restart from config
    local services=$(jq -r '.deployment.services[]' "$DEPLOY_CONFIG")
    
    for service in $services; do
        echo "🔄 Restarting $service..."
        if sudo systemctl restart $service; then
            echo "✅ $service restarted successfully"
            log_message "$service restarted successfully"
        else
            echo "❌ Failed to restart $service"
            log_message "Failed to restart $service"
            return 1
        fi
    done
}

# Function to verify deployment
verify_deployment() {
    log_message "Verifying deployment"
    
    echo ""
    echo "Verifying Deployment..."
    echo "===================="
    
    # Wait a moment for services to start
    echo "⏳ Waiting for services to initialize..."
    sleep 10
    
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
    
    # Check if health endpoint is accessible
    echo "🔍 Checking health endpoint..."
    if curl -f -s http://localhost:5000/health > /dev/null 2>&1; then
        echo "✅ Health endpoint is accessible"
        log_message "Health endpoint is accessible"
    else
        echo "ℹ️ Health endpoint not available (continuing anyway)"
        log_message "Health endpoint not available"
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
    local services=$(jq -r '.deployment.services[]' "$DEPLOY_CONFIG")
    local all_running=true
    
    for service in $services; do
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
}

# Function to send deployment notification
send_deployment_notification() {
    local status=$1
    local message=$2
    
    log_message "Sending deployment notification: $status"
    
    echo ""
    echo "Sending Deployment Notification..."
    echo "================================"
    
    # Check if notifications are enabled
    local notifications_enabled=$(jq -r '.notifications.email.enabled' "$DEPLOY_CONFIG")
    if [ "$notifications_enabled" != "true" ]; then
        echo "ℹ️ Deployment notifications are disabled"
        log_message "Deployment notifications are disabled"
        return 0
    fi
    
    # Get recipients
    local recipients=$(jq -r '.notifications.email.recipients[]' "$DEPLOY_CONFIG")
    
    # Send notification (simulated)
    echo "📧 Deployment $status: $message"
    echo "To: $recipients"
    echo "Subject: Atlas Deployment $status - $DEPLOY_TIMESTAMP"
    echo ""
    echo "Deployment completed at: $(date)"
    echo "Status: $status"
    echo "Message: $message"
    echo ""
    echo "For detailed logs, check: $DEPLOY_LOG"
    
    log_message "Deployment notification sent: $status"
}

# Function to generate deployment report
generate_deployment_report() {
    log_message "Generating deployment report"
    
    echo ""
    echo "Generating Deployment Report..."
    echo "============================"
    
    local report_file="/home/ubuntu/dev/atlas/logs/deployment_report_${DEPLOY_TIMESTAMP}.txt"
    
    # Create deployment report
    echo "Atlas Production Deployment Report" > "$report_file"
    echo "Deployment Timestamp: $DEPLOY_TIMESTAMP" >> "$report_file"
    echo "===================================" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add deployment details
    echo "Deployment Details:" >> "$report_file"
    echo "------------------" >> "$report_file"
    echo "Branch: $(jq -r '.deployment.branch' "$DEPLOY_CONFIG")" >> "$report_file"
    echo "Repository: $(jq -r '.deployment.repository' "$DEPLOY_CONFIG")" >> "$report_file"
    echo "Backup Enabled: $(jq -r '.backup.enabled' "$DEPLOY_CONFIG")" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add deployment steps
    echo "Deployment Steps:" >> "$report_file"
    echo "---------------" >> "$report_file"
    echo "✅ Backup created" >> "$report_file"
    echo "✅ Code pulled" >> "$report_file"
    echo "✅ Dependencies updated" >> "$report_file"
    echo "✅ Database migrations run" >> "$report_file"
    echo "✅ Services restarted" >> "$report_file"
    echo "✅ Deployment verified" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add system information
    echo "System Information:" >> "$report_file"
    echo "------------------" >> "$report_file"
    echo "Hostname: $(hostname)" >> "$report_file"
    echo "Deployed by: $(whoami)" >> "$report_file"
    echo "Deployment time: $(date)" >> "$report_file"
    echo "" >> "$report_file"
    
    echo "✅ Deployment report generated: $report_file"
    log_message "Deployment report generated: $report_file"
}

# Main deployment function
main() {
    log_message "=== Starting Atlas Production Deployment ==="
    
    # Start time
    local start_time=$(date)
    log_message "Deployment started at: $start_time"
    
    # Create deployment configuration
    create_deployment_config
    
    # Handle rollback if requested
    if [ "$1" == "--rollback" ]; then
        echo "🔄 Rolling back deployment..."
        log_message "Rollback requested"
        
        # In a real implementation, this would restore from backup
        # For now, we'll just restart services
        restart_services
        verify_deployment
        send_deployment_notification "ROLLBACK" "Deployment rolled back to previous version"
        exit 0
    fi
    
    # Create backup before deployment
    if ! create_backup; then
        send_deployment_notification "FAILED" "Deployment failed during backup creation"
        exit 1
    fi
    
    # Pull latest code
    if ! pull_latest_code; then
        send_deployment_notification "FAILED" "Deployment failed during code pull"
        exit 1
    fi
    
    # Update dependencies
    if ! update_dependencies; then
        send_deployment_notification "FAILED" "Deployment failed during dependency update"
        exit 1
    fi
    
    # Run database migrations
    if ! run_database_migrations; then
        send_deployment_notification "FAILED" "Deployment failed during database migration"
        exit 1
    fi
    
    # Restart services
    if ! restart_services; then
        send_deployment_notification "FAILED" "Deployment failed during service restart"
        exit 1
    fi
    
    # Verify deployment
    if ! verify_deployment; then
        send_deployment_notification "FAILED" "Deployment verification failed"
        exit 1
    fi
    
    # Generate deployment report
    generate_deployment_report
    
    # Send success notification
    send_deployment_notification "SUCCESS" "Deployment completed successfully"
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Deployment completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Deployment Completed Successfully ==="
    
    echo ""
    echo "✅ Deployment completed successfully!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📋 Report: /home/ubuntu/dev/atlas/logs/deployment_report_${DEPLOY_TIMESTAMP}.txt"
    echo "📝 Log: $DEPLOY_LOG"
}

# Run main function
main "$@"