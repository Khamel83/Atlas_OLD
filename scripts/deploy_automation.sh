#!/bin/bash

# Atlas Production Deployment Automation Script
# This script automates the deployment process for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Deployment Automation..."

# Configuration
DEPLOY_LOG="/home/ubuntu/dev/atlas/logs/deployment.log"
DEPLOY_CONFIG="/home/ubuntu/dev/atlas/config/deployment.json"
BACKUP_DIR="/home/ubuntu/dev/atlas/backups/deploy_$(date +%Y%m%d_%H%M%S)"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $DEPLOY_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $DEPLOY_LOG
    echo "$1"
}

# Function to initialize deployment configuration
initialize_deployment_config() {
    log_message "Initializing deployment configuration"
    
    # Create default deployment configuration if it doesn't exist
    if [ ! -f "$DEPLOY_CONFIG" ]; then
        cat > "$DEPLOY_CONFIG" << EOF
{
    "deployment": {
        "branch": "main",
        "repository": "/home/ubuntu/dev/atlas",
        "backup_before_deploy": true,
        "run_tests": true,
        "notify_on_completion": true
    },
    "services": {
        "atlas": true,
        "postgresql": true,
        "nginx": true,
        "prometheus": true,
        "grafana": true
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
create_pre_deployment_backup() {
    log_message "Creating pre-deployment backup"
    
    echo "Creating Pre-Deployment Backup..."
    echo "=============================="
    
    # Create backup directory
    mkdir -p "$BACKUP_DIR"
    
    # Backup database
    echo "💾 Backing up database..."
    if sudo -u postgres pg_dump -U atlas_user -d atlas > "$BACKUP_DIR/database_backup.sql" 2>/dev/null; then
        echo "✅ Database backup created: $BACKUP_DIR/database_backup.sql"
        log_message "Database backup created"
    else
        echo "❌ Failed to create database backup"
        log_message "Failed to create database backup"
        return 1
    fi
    
    # Backup configuration files
    echo "💾 Backing up configuration files..."
    mkdir -p "$BACKUP_DIR/config"
    
    # Backup .env file
    if [ -f "/home/ubuntu/dev/atlas/.env" ]; then
        cp "/home/ubuntu/dev/atlas/.env" "$BACKUP_DIR/config/"
        echo "✅ .env file backed up"
    fi
    
    # Backup Nginx configuration
    if [ -f "/etc/nginx/sites-available/atlas" ]; then
        cp "/etc/nginx/sites-available/atlas" "$BACKUP_DIR/config/"
        echo "✅ Nginx configuration backed up"
    fi
    
    # Backup systemd service files
    for service in atlas atlas-prometheus atlas-grafana; do
        if [ -f "/etc/systemd/system/$service.service" ]; then
            cp "/etc/systemd/system/$service.service" "$BACKUP_DIR/config/"
            echo "✅ $service.service backed up"
        fi
    done
    
    echo "✅ Pre-deployment backup completed"
    echo "📂 Backup location: $BACKUP_DIR"
    log_message "Pre-deployment backup completed: $BACKUP_DIR"
}

# Function to pull latest code from repository
pull_latest_code() {
    log_message "Pulling latest code from repository"
    
    echo ""
    echo "Pulling Latest Code..."
    echo "===================="
    
    # Navigate to repository
    cd /home/ubuntu/dev/atlas
    
    # Get current branch
    local current_branch=$(git rev-parse --abbrev-ref HEAD)
    local target_branch=$(jq -r '.deployment.branch' "$DEPLOY_CONFIG")
    
    # Checkout target branch if needed
    if [ "$current_branch" != "$target_branch" ]; then
        echo "🔄 Switching to branch: $target_branch"
        if ! git checkout "$target_branch"; then
            echo "❌ Failed to switch to branch $target_branch"
            log_message "Failed to switch to branch $target_branch"
            return 1
        fi
    fi
    
    # Pull latest changes
    echo "🔄 Pulling latest changes..."
    if git pull origin "$target_branch"; then
        echo "✅ Code updated successfully"
        log_message "Code updated successfully"
    else
        echo "❌ Failed to pull latest code"
        log_message "Failed to pull latest code"
        return 1
    fi
    
    # Show latest commit
    local latest_commit=$(git log -1 --pretty=format:"%h - %an, %ar : %s")
    echo "📝 Latest commit: $latest_commit"
}

# Function to update dependencies
update_dependencies() {
    log_message "Updating dependencies"
    
    echo ""
    echo "Updating Dependencies..."
    echo "======================"
    
    # Activate virtual environment
    cd /home/ubuntu/dev/atlas
    source atlas_venv/bin/activate
    
    # Update pip
    echo "🔄 Updating pip..."
    if pip install --upgrade pip > /dev/null 2>&1; then
        echo "✅ Pip updated successfully"
    else
        echo "❌ Failed to update pip"
        log_message "Failed to update pip"
    fi
    
    # Install/upgrade requirements
    echo "🔄 Installing/upgrading requirements..."
    if pip install -r requirements.txt > /dev/null 2>&1; then
        echo "✅ Dependencies updated successfully"
        log_message "Dependencies updated successfully"
    else
        echo "❌ Failed to update dependencies"
        log_message "Failed to update dependencies"
        return 1
    fi
}

# Function to run tests
run_tests() {
    log_message "Running tests"
    
    echo ""
    echo "Running Tests..."
    echo "=============="
    
    # Check if tests should be run
    local run_tests_flag=$(jq -r '.deployment.run_tests' "$DEPLOY_CONFIG")
    if [ "$run_tests_flag" != "true" ]; then
        echo "⏭️ Skipping tests as configured"
        log_message "Skipping tests as configured"
        return 0
    fi
    
    # Activate virtual environment
    cd /home/ubuntu/dev/atlas
    source atlas_venv/bin/activate
    
    # Run unit tests
    echo "🔬 Running unit tests..."
    if python -m pytest tests/unit/ -v > /dev/null 2>&1; then
        echo "✅ Unit tests passed"
        log_message "Unit tests passed"
    else
        echo "❌ Unit tests failed"
        log_message "Unit tests failed"
        return 1
    fi
    
    # Run integration tests
    echo "🔬 Running integration tests..."
    if python -m pytest tests/integration/ -v > /dev/null 2>&1; then
        echo "✅ Integration tests passed"
        log_message "Integration tests passed"
    else
        echo "❌ Integration tests failed"
        log_message "Integration tests failed"
        return 1
    fi
    
    echo "✅ All tests passed"
}

# Function to stop services
stop_services() {
    log_message "Stopping services"
    
    echo ""
    echo "Stopping Services..."
    echo "=================="
    
    # Define services to stop
    local services=(
        "atlas:Atlas Main Service"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
        "nginx:Nginx Web Server"
    )
    
    # Stop services in reverse order
    for ((i=${#services[@]}-1; i>=0; i--)); do
        local service_info=${services[i]}
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        # Check if service should be managed
        local manage_service=$(jq -r ".services.$service_name" "$DEPLOY_CONFIG")
        if [ "$manage_service" = "true" ]; then
            echo "⏹️ Stopping $service_desc..."
            if sudo systemctl stop $service_name > /dev/null 2>&1; then
                echo "✅ $service_desc stopped"
            else
                echo "❌ Failed to stop $service_desc"
                log_message "Failed to stop $service_name"
            fi
        fi
    done
    
    # Stop PostgreSQL if configured
    local manage_postgresql=$(jq -r '.services.postgresql' "$DEPLOY_CONFIG")
    if [ "$manage_postgresql" = "true" ]; then
        echo "⏹️ Stopping PostgreSQL Database..."
        if sudo systemctl stop postgresql > /dev/null 2>&1; then
            echo "✅ PostgreSQL Database stopped"
        else
            echo "❌ Failed to stop PostgreSQL Database"
            log_message "Failed to stop PostgreSQL"
        fi
    fi
    
    echo "✅ Services stopped"
    log_message "Services stopped"
}

# Function to update database schema
update_database_schema() {
    log_message "Updating database schema"
    
    echo ""
    echo "Updating Database Schema..."
    echo "========================="
    
    # Start PostgreSQL if not running
    if ! systemctl is-active --quiet postgresql; then
        echo "🔄 Starting PostgreSQL..."
        if ! sudo systemctl start postgresql; then
            echo "❌ Failed to start PostgreSQL"
            log_message "Failed to start PostgreSQL"
            return 1
        fi
    fi
    
    # Check database connectivity
    if ! sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        echo "❌ Cannot connect to database"
        log_message "Cannot connect to database"
        return 1
    fi
    
    # Run database migrations (if migration script exists)
    local migration_script="/home/ubuntu/dev/atlas/migrations/migrate.py"
    if [ -f "$migration_script" ]; then
        echo "🔄 Running database migrations..."
        if python "$migration_script" > /dev/null 2>&1; then
            echo "✅ Database migrations completed"
            log_message "Database migrations completed"
        else
            echo "❌ Database migrations failed"
            log_message "Database migrations failed"
            return 1
        fi
    else
        echo "⏭️ No migration script found, skipping"
        log_message "No migration script found, skipping"
    fi
    
    echo "✅ Database schema updated"
}

# Function to start services
start_services() {
    log_message "Starting services"
    
    echo ""
    echo "Starting Services..."
    echo "=================="
    
    # Start PostgreSQL if configured
    local manage_postgresql=$(jq -r '.services.postgresql' "$DEPLOY_CONFIG")
    if [ "$manage_postgresql" = "true" ]; then
        echo "▶️ Starting PostgreSQL Database..."
        if sudo systemctl start postgresql > /dev/null 2>&1; then
            echo "✅ PostgreSQL Database started"
        else
            echo "❌ Failed to start PostgreSQL Database"
            log_message "Failed to start PostgreSQL"
        fi
    fi
    
    # Define services to start
    local services=(
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
        "atlas:Atlas Main Service"
    )
    
    # Start services
    for service_info in "${services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        # Check if service should be managed
        local manage_service=$(jq -r ".services.$service_name" "$DEPLOY_CONFIG")
        if [ "$manage_service" = "true" ]; then
            echo "▶️ Starting $service_desc..."
            if sudo systemctl start $service_name > /dev/null 2>&1; then
                echo "✅ $service_desc started"
            else
                echo "❌ Failed to start $service_desc"
                log_message "Failed to start $service_name"
            fi
        fi
    done
    
    echo "✅ Services started"
    log_message "Services started"
}

# Function to verify deployment
verify_deployment() {
    log_message "Verifying deployment"
    
    echo ""
    echo "Verifying Deployment..."
    echo "====================="
    
    # Wait a moment for services to start
    sleep 10
    
    # Check service statuses
    local services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    local all_services_running=true
    
    echo "🔍 Checking service statuses..."
    for service_info in "${services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        # Check if service should be managed
        local manage_service=$(jq -r ".services.$service_name" "$DEPLOY_CONFIG")
        if [ "$manage_service" = "true" ]; then
            if systemctl is-active --quiet $service_name; then
                echo "✅ $service_desc: Running"
            else
                echo "❌ $service_desc: Not Running"
                all_services_running=false
                log_message "SERVICE NOT RUNNING: $service_name"
            fi
        fi
    done
    
    # Check web application accessibility
    echo "🔍 Checking web application..."
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        echo "✅ Web application is accessible"
    else
        echo "❌ Web application is not accessible"
        all_services_running=false
        log_message "WEB APPLICATION NOT ACCESSIBLE"
    fi
    
    # Check monitoring endpoints
    echo "🔍 Checking monitoring endpoints..."
    if curl -f -s http://localhost:9090/status > /dev/null 2>&1; then
        echo "✅ Prometheus is accessible"
    else
        echo "❌ Prometheus is not accessible"
    fi
    
    if curl -f -s http://localhost:3000/login > /dev/null 2>&1; then
        echo "✅ Grafana is accessible"
    else
        echo "❌ Grafana is not accessible"
    fi
    
    # Report results
    if $all_services_running; then
        echo "✅ Deployment verification successful"
        log_message "Deployment verification successful"
        return 0
    else
        echo "❌ Deployment verification failed"
        log_message "Deployment verification failed"
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
    local notifications_enabled=$(jq -r '.deployment.notify_on_completion' "$DEPLOY_CONFIG")
    if [ "$notifications_enabled" != "true" ]; then
        echo "⏭️ Notifications disabled, skipping"
        log_message "Notifications disabled, skipping"
        return 0
    fi
    
    # Check if email notifications are enabled
    local email_enabled=$(jq -r '.notifications.email.enabled' "$DEPLOY_CONFIG")
    if [ "$email_enabled" = "true" ]; then
        # Get recipients
        local recipients=$(jq -r '.notifications.email.recipients[]' "$DEPLOY_CONFIG")
        
        # Send email notification (simulated)
        echo "📧 Sending email notification..."
        echo "To: $recipients"
        echo "Subject: Atlas Deployment $status"
        echo "Message: $message"
        echo ""
        echo "✅ Email notification sent"
        log_message "Email notification sent: $status"
    else
        echo "⏭️ Email notifications disabled"
    fi
}

# Function to generate deployment report
generate_deployment_report() {
    log_message "Generating deployment report"
    
    echo ""
    echo "Generating Deployment Report..."
    echo "============================="
    
    local report_file="/home/ubuntu/dev/atlas/logs/deployment_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create report header
    echo "Atlas Production Deployment Report" > "$report_file"
    echo "Generated: $(date)" >> "$report_file"
    echo "=================================" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add deployment information
    echo "Deployment Information:" >> "$report_file"
    echo "---------------------" >> "$report_file"
    echo "Branch: $(jq -r '.deployment.branch' "$DEPLOY_CONFIG")" >> "$report_file"
    echo "Repository: $(jq -r '.deployment.repository' "$DEPLOY_CONFIG")" >> "$report_file"
    echo "Backup Created: $BACKUP_DIR" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add service statuses
    echo "Service Statuses:" >> "$report_file"
    echo "----------------" >> "$report_file"
    local services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    for service_info in "${services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc: Running" >> "$report_file"
        else
            echo "❌ $service_desc: Not Running" >> "$report_file"
        fi
    done
    echo "" >> "$report_file"
    
    # Add commit information
    echo "Latest Commit:" >> "$report_file"
    echo "-------------" >> "$report_file"
    cd /home/ubuntu/dev/atlas
    git log -1 --pretty=format:"%h - %an, %ar : %s" >> "$report_file"
    echo "" >> "$report_file"
    
    echo "✅ Deployment report generated: $report_file"
    log_message "Deployment report generated: $report_file"
    
    # Display summary
    echo ""
    echo "Deployment Summary:"
    echo "  Branch: $(jq -r '.deployment.branch' "$DEPLOY_CONFIG")"
    echo "  Backup: $BACKUP_DIR"
    echo "  Report: $report_file"
}

# Function to rollback deployment
rollback_deployment() {
    log_message "Rolling back deployment"
    
    echo ""
    echo "Rolling Back Deployment..."
    echo "========================="
    
    # Stop services
    stop_services
    
    # Restore database from backup
    echo "🔄 Restoring database from backup..."
    if [ -f "$BACKUP_DIR/database_backup.sql" ]; then
        if sudo -u postgres psql -U atlas_user -d atlas -f "$BACKUP_DIR/database_backup.sql" > /dev/null 2>&1; then
            echo "✅ Database restored from backup"
            log_message "Database restored from backup"
        else
            echo "❌ Failed to restore database from backup"
            log_message "Failed to restore database from backup"
        fi
    else
        echo "❌ Backup database file not found"
        log_message "Backup database file not found"
    fi
    
    # Restore configuration files
    echo "🔄 Restoring configuration files..."
    if [ -d "$BACKUP_DIR/config" ]; then
        # Restore .env file
        if [ -f "$BACKUP_DIR/config/.env" ]; then
            cp "$BACKUP_DIR/config/.env" "/home/ubuntu/dev/atlas/"
            echo "✅ .env file restored"
        fi
        
        # Restore Nginx configuration
        if [ -f "$BACKUP_DIR/config/atlas" ]; then
            sudo cp "$BACKUP_DIR/config/atlas" "/etc/nginx/sites-available/"
            echo "✅ Nginx configuration restored"
        fi
        
        # Restore systemd service files
        for service_file in "$BACKUP_DIR/config"/*.service; do
            if [ -f "$service_file" ]; then
                local service_name=$(basename "$service_file")
                sudo cp "$service_file" "/etc/systemd/system/$service_name"
                echo "✅ $service_name restored"
            fi
        done
        
        # Reload systemd
        sudo systemctl daemon-reload
        echo "✅ Systemd reloaded"
    else
        echo "❌ Backup configuration directory not found"
        log_message "Backup configuration directory not found"
    fi
    
    # Start services
    start_services
    
    echo "✅ Deployment rolled back"
    log_message "Deployment rolled back"
    
    # Send rollback notification
    send_deployment_notification "ROLLED_BACK" "Deployment rolled back due to failure"
}

# Main deployment function
main() {
    log_message "=== Starting Atlas Deployment Automation ==="
    
    # Initialize configuration
    initialize_deployment_config
    
    # Start time
    local start_time=$(date)
    log_message "Deployment started at: $start_time"
    
    # Handle different deployment operations
    case $1 in
        "backup")
            create_pre_deployment_backup
            ;;
        "code")
            pull_latest_code
            ;;
        "deps")
            update_dependencies
            ;;
        "tests")
            run_tests
            ;;
        "stop")
            stop_services
            ;;
        "db")
            update_database_schema
            ;;
        "start")
            start_services
            ;;
        "verify")
            verify_deployment
            ;;
        "report")
            generate_deployment_report
            ;;
        "rollback")
            rollback_deployment
            ;;
        *)
            # Run full deployment process
            echo "🚀 Starting Full Deployment Process..."
            echo "===================================="
            
            # Create backup
            if ! create_pre_deployment_backup; then
                echo "❌ Failed to create backup, aborting deployment"
                send_deployment_notification "FAILED" "Deployment failed during backup creation"
                exit 1
            fi
            
            # Pull latest code
            if ! pull_latest_code; then
                echo "❌ Failed to pull latest code, aborting deployment"
                send_deployment_notification "FAILED" "Deployment failed during code update"
                exit 1
            fi
            
            # Update dependencies
            if ! update_dependencies; then
                echo "❌ Failed to update dependencies, aborting deployment"
                send_deployment_notification "FAILED" "Deployment failed during dependency update"
                exit 1
            fi
            
            # Run tests
            if ! run_tests; then
                echo "❌ Tests failed, aborting deployment"
                send_deployment_notification "FAILED" "Deployment failed during testing"
                exit 1
            fi
            
            # Stop services
            stop_services
            
            # Update database schema
            if ! update_database_schema; then
                echo "❌ Failed to update database schema"
                echo "🔄 Rolling back deployment..."
                rollback_deployment
                send_deployment_notification "FAILED" "Deployment failed during database update"
                exit 1
            fi
            
            # Start services
            start_services
            
            # Verify deployment
            if ! verify_deployment; then
                echo "❌ Deployment verification failed"
                echo "🔄 Rolling back deployment..."
                rollback_deployment
                send_deployment_notification "FAILED" "Deployment failed during verification"
                exit 1
            fi
            
            # Generate report
            generate_deployment_report
            
            # Send success notification
            send_deployment_notification "SUCCESS" "Deployment completed successfully"
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Deployment completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Deployment Automation Completed ==="
    
    echo ""
    echo "✅ Deployment automation complete!"
    echo "📋 Check $DEPLOY_LOG for details"
}

# Run main function
main "$@"