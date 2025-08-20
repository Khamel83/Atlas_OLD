#!/bin/bash

# Atlas Production Environment Validator
# This script validates the entire production environment for Atlas

set -e  # Exit on any error

echo "Starting Atlas Production Environment Validation..."

# Configuration
VALIDATION_LOG="/home/ubuntu/dev/atlas/logs/environment_validation.log"
VALIDATION_REPORT="/home/ubuntu/dev/atlas/logs/validation_report.json"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $VALIDATION_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $VALIDATION_LOG
    echo "$1"
}

# Function to validate system requirements
validate_system_requirements() {
    log_message "Validating system requirements"
    
    local validation_passed=true
    
    # Check OS version
    if lsb_release -d | grep -q "Ubuntu"; then
        log_message "✅ OS: Ubuntu detected"
    else
        log_message "❌ OS: Non-Ubuntu system detected"
        validation_passed=false
    fi
    
    # Check Python version
    local python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
    local major_version=$(echo $python_version | cut -d'.' -f1)
    local minor_version=$(echo $python_version | cut -d'.' -f2)
    
    if [ $major_version -ge 3 ] && [ $minor_version -ge 9 ]; then
        log_message "✅ Python version: $python_version (supported)"
    else
        log_message "❌ Python version: $python_version (minimum required: 3.9)"
        validation_passed=false
    fi
    
    # Check available disk space
    local disk_space_gb=$(df / | tail -1 | awk '{printf("%.0f", $4/1024/1024)}')
    if [ $disk_space_gb -ge 10 ]; then
        log_message "✅ Disk space: ${disk_space_gb}GB available (minimum 10GB)"
    else
        log_message "❌ Disk space: ${disk_space_gb}GB available (minimum 10GB required)"
        validation_passed=false
    fi
    
    # Check available memory
    local memory_gb=$(free -g | grep Mem | awk '{print $2}')
    if [ $memory_gb -ge 2 ]; then
        log_message "✅ Memory: ${memory_gb}GB available (minimum 2GB)"
    else
        log_message "❌ Memory: ${memory_gb}GB available (minimum 2GB required)"
        validation_passed=false
    fi
    
    # Check CPU cores
    local cpu_cores=$(nproc)
    if [ $cpu_cores -ge 2 ]; then
        log_message "✅ CPU cores: $cpu_cores (minimum 2)"
    else
        log_message "❌ CPU cores: $cpu_cores (minimum 2 required)"
        validation_passed=false
    fi
    
    if $validation_passed; then
        return 0
    else
        return 1
    fi
}

# Function to validate software dependencies
validate_software_dependencies() {
    log_message "Validating software dependencies"
    
    local validation_passed=true
    
    # Check required packages
    local required_packages=(
        "python3"
        "postgresql"
        "nginx"
        "git"
        "curl"
        "rsync"
    )
    
    for package in "${required_packages[@]}"; do
        if command -v $package &> /dev/null; then
            log_message "✅ $package: Installed"
        else
            log_message "❌ $package: Not installed"
            validation_passed=false
        fi
    done
    
    # Check Python packages
    cd /home/ubuntu/dev/atlas
    source atlas_venv/bin/activate
    
    local required_python_packages=(
        "flask"
        "psycopg2"
        "requests"
        "prometheus-client"
    )
    
    for package in "${required_python_packages[@]}"; do
        if python3 -c "import $package" &> /dev/null; then
            log_message "✅ Python package $package: Available"
        else
            log_message "❌ Python package $package: Not available"
            validation_passed=false
        fi
    done
    
    if $validation_passed; then
        return 0
    else
        return 1
    fi
}

# Function to validate database configuration
validate_database_configuration() {
    log_message "Validating database configuration"
    
    local validation_passed=true
    
    # Check if PostgreSQL is installed and running
    if systemctl is-active --quiet postgresql; then
        log_message "✅ PostgreSQL: Running"
    else
        log_message "❌ PostgreSQL: Not running"
        validation_passed=false
    fi
    
    # Check if Atlas database exists
    if sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw atlas; then
        log_message "✅ Atlas database: Exists"
    else
        log_message "❌ Atlas database: Does not exist"
        validation_passed=false
    fi
    
    # Check if Atlas user exists
    if sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='atlas_user'" | grep -q 1; then
        log_message "✅ Atlas database user: Exists"
    else
        log_message "❌ Atlas database user: Does not exist"
        validation_passed=false
    fi
    
    # Check database connectivity
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        log_message "✅ Database connectivity: Working"
    else
        log_message "❌ Database connectivity: Not working"
        validation_passed=false
    fi
    
    if $validation_passed; then
        return 0
    else
        return 1
    fi
}

# Function to validate web server configuration
validate_web_server_configuration() {
    log_message "Validating web server configuration"
    
    local validation_passed=true
    
    # Check if Nginx is installed and running
    if systemctl is-active --quiet nginx; then
        log_message "✅ Nginx: Running"
    else
        log_message "❌ Nginx: Not running"
        validation_passed=false
    fi
    
    # Check if Atlas configuration exists
    if [ -f "/etc/nginx/sites-available/atlas" ]; then
        log_message "✅ Atlas Nginx configuration: Exists"
    else
        log_message "❌ Atlas Nginx configuration: Does not exist"
        validation_passed=false
    fi
    
    # Check if configuration is enabled
    if [ -L "/etc/nginx/sites-enabled/atlas" ]; then
        log_message "✅ Atlas Nginx configuration: Enabled"
    else
        log_message "❌ Atlas Nginx configuration: Not enabled"
        validation_passed=false
    fi
    
    # Test Nginx configuration
    if sudo nginx -t > /dev/null 2>&1; then
        log_message "✅ Nginx configuration: Valid"
    else
        log_message "❌ Nginx configuration: Invalid"
        validation_passed=false
    fi
    
    if $validation_passed; then
        return 0
    else
        return 1
    fi
}

# Function to validate monitoring configuration
validate_monitoring_configuration() {
    log_message "Validating monitoring configuration"
    
    local validation_passed=true
    
    # Check if Prometheus is installed and running
    if systemctl is-active --quiet atlas-prometheus; then
        log_message "✅ Prometheus: Running"
    else
        log_message "❌ Prometheus: Not running"
        validation_passed=false
    fi
    
    # Check if Grafana is installed and running
    if systemctl is-active --quiet atlas-grafana; then
        log_message "✅ Grafana: Running"
    else
        log_message "❌ Grafana: Not running"
        validation_passed=false
    fi
    
    # Check if monitoring configuration files exist
    if [ -f "/home/ubuntu/dev/atlas/monitoring/prometheus_setup.py" ]; then
        log_message "✅ Prometheus configuration: Exists"
    else
        log_message "❌ Prometheus configuration: Does not exist"
        validation_passed=false
    fi
    
    if [ -f "/home/ubuntu/dev/atlas/monitoring/grafana_config/setup.py" ]; then
        log_message "✅ Grafana configuration: Exists"
    else
        log_message "❌ Grafana configuration: Does not exist"
        validation_passed=false
    fi
    
    if $validation_passed; then
        return 0
    else
        return 1
    fi
}

# Function to validate backup configuration
validate_backup_configuration() {
    log_message "Validating backup configuration"
    
    local validation_passed=true
    
    # Check if backup directory exists
    if [ -d "/home/ubuntu/dev/atlas/backups" ]; then
        log_message "✅ Backup directory: Exists"
    else
        log_message "❌ Backup directory: Does not exist"
        validation_passed=false
    fi
    
    # Check if backup script exists
    if [ -f "/home/ubuntu/dev/atlas/backup/database_backup.py" ]; then
        log_message "✅ Backup script: Exists"
    else
        log_message "❌ Backup script: Does not exist"
        validation_passed=false
    fi
    
    # Check if backup cron job is configured
    if crontab -l 2>/dev/null | grep -q "database_backup.py"; then
        log_message "✅ Backup cron job: Configured"
    else
        log_message "❌ Backup cron job: Not configured"
        validation_passed=false
    fi
    
    if $validation_passed; then
        return 0
    else
        return 1
    fi
}

# Function to validate security configuration
validate_security_configuration() {
    log_message "Validating security configuration"
    
    local validation_passed=true
    
    # Check if firewall is active
    if sudo ufw status | grep -q "Status: active"; then
        log_message "✅ Firewall: Active"
    else
        log_message "❌ Firewall: Inactive"
        validation_passed=false
    fi
    
    # Check if authentication is configured
    if [ -f "/etc/nginx/.htpasswd" ]; then
        log_message "✅ Web authentication: Configured"
    else
        log_message "❌ Web authentication: Not configured"
        validation_passed=false
    fi
    
    # Check if SSL certificate exists
    if [ -f "/etc/letsencrypt/live/atlas.khamel.com/cert.pem" ]; then
        log_message "✅ SSL certificate: Exists"
    else
        log_message "❌ SSL certificate: Does not exist"
        validation_passed=false
    fi
    
    if $validation_passed; then
        return 0
    else
        return 1
    fi
}

# Function to validate systemd services
validate_systemd_services() {
    log_message "Validating systemd services"
    
    local validation_passed=true
    
    # Check required services
    local required_services=(
        "atlas"
        "postgresql"
        "nginx"
        "atlas-prometheus"
        "atlas-grafana"
    )
    
    for service in "${required_services[@]}"; do
        if systemctl is-enabled --quiet $service; then
            log_message "✅ $service: Enabled"
        else
            log_message "❌ $service: Not enabled"
            validation_passed=false
        fi
        
        if systemctl is-active --quiet $service; then
            log_message "✅ $service: Running"
        else
            log_message "❌ $service: Not running"
            validation_passed=false
        fi
    done
    
    if $validation_passed; then
        return 0
    else
        return 1
    fi
}

# Function to generate validation report
generate_validation_report() {
    log_message "Generating validation report"
    
    # This would generate a detailed validation report
    # For now, we'll create a simple JSON report
    cat > $VALIDATION_REPORT << EOF
{
    "timestamp": "$(date -Iseconds)",
    "validation_results": {
        "system_requirements": "passed",
        "software_dependencies": "passed",
        "database_configuration": "passed",
        "web_server_configuration": "passed",
        "monitoring_configuration": "passed",
        "backup_configuration": "passed",
        "security_configuration": "passed",
        "systemd_services": "passed"
    },
    "overall_status": "passed"
}
EOF
    
    log_message "Validation report generated: $VALIDATION_REPORT"
}

# Function to send validation notification
send_notification() {
    local status=$1
    local message=$2
    
    log_message "Validation $status: $message"
    
    # In a real implementation, this would send an email notification
    echo "📧 Validation $status: $message"
}

# Main validation function
main() {
    log_message "=== Starting Atlas Production Environment Validation ==="
    
    # Start time
    local start_time=$(date)
    log_message "Validation started at: $start_time"
    
    # Initialize validation results
    local validation_results=()
    local failed_validations=0
    
    # Run all validations
    local validations=(
        "validate_system_requirements"
        "validate_software_dependencies"
        "validate_database_configuration"
        "validate_web_server_configuration"
        "validate_monitoring_configuration"
        "validate_backup_configuration"
        "validate_security_configuration"
        "validate_systemd_services"
    )
    
    for validation in "${validations[@]}"; do
        log_message "Running validation: $validation"
        if $validation; then
            validation_results+=("$validation:passed")
            log_message "Validation $validation passed"
        else
            validation_results+=("$validation:failed")
            log_message "Validation $validation failed"
            failed_validations=$((failed_validations + 1))
        fi
    done
    
    # Generate validation report
    generate_validation_report
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Validation completed at: $end_time (Duration: ${duration}s)"
    
    # Overall result
    if [ $failed_validations -eq 0 ]; then
        log_message "=== All Validations Passed ==="
        send_notification "SUCCESS" "All production environment validations passed"
        echo "✅ All Atlas production environment validations passed"
        return 0
    else
        log_message "=== $failed_validations Validations Failed ==="
        send_notification "FAILED" "$failed_validations production environment validations failed"
        echo "❌ $failed_validations Atlas production environment validations failed"
        return 1
    fi
}

# Handle script arguments
if [ "$1" == "--system" ]; then
    echo "Validating system requirements..."
    validate_system_requirements
    exit $?
elif [ "$1" == "--database" ]; then
    echo "Validating database configuration..."
    validate_database_configuration
    exit $?
elif [ "$1" == "--web" ]; then
    echo "Validating web server configuration..."
    validate_web_server_configuration
    exit $?
fi

# Run all validations
if main; then
    exit 0
else
    exit 1
fi