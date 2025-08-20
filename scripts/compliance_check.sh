#!/bin/bash

# Atlas Production Compliance Checker
# This script verifies compliance with production standards and best practices

set -e  # Exit on any error

echo "Starting Atlas Production Compliance Check..."

# Configuration
COMPLIANCE_LOG="/home/ubuntu/dev/atlas/logs/compliance_check.log"
COMPLIANCE_REPORT="/home/ubuntu/dev/atlas/logs/compliance_report.json"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $COMPLIANCE_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $COMPLIANCE_LOG
    echo "$1"
}

# Function to check system security compliance
check_system_security() {
    log_message "Checking system security compliance"
    
    echo "System Security Compliance Check:"
    echo "================================="
    
    local compliance_issues=0
    
    # Check if firewall is active
    if sudo ufw status | grep -q "Status: active"; then
        echo "✅ Firewall is active"
    else
        echo "❌ Firewall is not active"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    # Check SSH configuration
    local ssh_config="/etc/ssh/sshd_config"
    if [ -f "$ssh_config" ]; then
        if grep -q "^PasswordAuthentication no" "$ssh_config"; then
            echo "✅ SSH password authentication is disabled"
        else
            echo "❌ SSH password authentication is enabled"
            compliance_issues=$((compliance_issues + 1))
        fi
        
        if grep -q "^PermitRootLogin no" "$ssh_config"; then
            echo "✅ SSH root login is disabled"
        else
            echo "❌ SSH root login is not disabled"
            compliance_issues=$((compliance_issues + 1))
        fi
    else
        echo "❌ SSH configuration file not found"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    # Check for unnecessary services
    local insecure_services=("telnet" "ftp" "rsh")
    for service in "${insecure_services[@]}"; do
        if systemctl is-active --quiet "$service"; then
            echo "❌ Insecure service running: $service"
            compliance_issues=$((compliance_issues + 1))
        fi
    done
    
    log_message "System security compliance check completed with $compliance_issues issues"
    return $compliance_issues
}

# Function to check data protection compliance
check_data_protection() {
    log_message "Checking data protection compliance"
    
    echo "Data Protection Compliance Check:"
    echo "================================="
    
    local compliance_issues=0
    
    # Check SSL certificate
    local ssl_cert="/etc/letsencrypt/live/atlas.khamel.com/cert.pem"
    if [ -f "$ssl_cert" ]; then
        # Check certificate expiration
        local expiry_date=$(openssl x509 -in "$ssl_cert" -noout -enddate | cut -d= -f2)
        local expiry_seconds=$(date -d "$expiry_date" +%s)
        local current_seconds=$(date +%s)
        local days_until_expiry=$(( (expiry_seconds - current_seconds) / 86400 ))
        
        if [ $days_until_expiry -gt 30 ]; then
            echo "✅ SSL certificate is valid (expires in $days_until_expiry days)"
        elif [ $days_until_expiry -gt 0 ]; then
            echo "⚠️ SSL certificate expires soon (in $days_until_expiry days)"
            compliance_issues=$((compliance_issues + 1))
        else
            echo "❌ SSL certificate has expired"
            compliance_issues=$((compliance_issues + 1))
        fi
    else
        echo "❌ SSL certificate not found"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    # Check file permissions
    local sensitive_files=(
        "/home/ubuntu/dev/atlas/.env:environment file"
        "/etc/nginx/.htpasswd:authentication file"
        "/home/ubuntu/dev/atlas/backups:backup directory"
    )
    
    for file_info in "${sensitive_files[@]}"; do
        local file_path=$(echo $file_info | cut -d: -f1)
        local description=$(echo $file_info | cut -d: -f2)
        
        if [ -e "$file_path" ]; then
            local permissions=$(stat -c %a "$file_path")
            case $permissions in
                600|640|700)
                    echo "✅ $description has secure permissions ($permissions)"
                    ;;
                *)
                    echo "❌ $description has insecure permissions ($permissions)"
                    compliance_issues=$((compliance_issues + 1))
                    ;;
            esac
        else
            echo "❌ $description not found"
            compliance_issues=$((compliance_issues + 1))
        fi
    done
    
    log_message "Data protection compliance check completed with $compliance_issues issues"
    return $compliance_issues
}

# Function to check backup compliance
check_backup_compliance() {
    log_message "Checking backup compliance"
    
    echo "Backup Compliance Check:"
    echo "========================"
    
    local compliance_issues=0
    
    # Check if backup directory exists
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        echo "✅ Backup directory exists"
        
        # Check for recent backups
        local recent_backups=$(find "$backup_dir" -name "*.sql*" -mtime -2 | wc -l)
        if [ $recent_backups -gt 0 ]; then
            echo "✅ Recent backups found ($recent_backups in last 2 days)"
        else
            echo "❌ No recent backups found"
            compliance_issues=$((compliance_issues + 1))
        fi
        
        # Check backup retention
        local total_backups=$(find "$backup_dir" -name "*.sql*" | wc -l)
        if [ $total_backups -gt 5 ]; then
            echo "✅ Sufficient backup retention ($total_backups backups)"
        else
            echo "⚠️ Limited backup retention ($total_backups backups)"
            # This is a warning, not a compliance failure
        fi
    else
        echo "❌ Backup directory does not exist"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    # Check if backup script exists
    local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
    if [ -f "$backup_script" ]; then
        echo "✅ Backup script exists"
    else
        echo "❌ Backup script does not exist"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    # Check if backup cron job is configured
    if crontab -l 2>/dev/null | grep -q "production_backup.sh"; then
        echo "✅ Backup cron job is configured"
    else
        echo "❌ Backup cron job is not configured"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    log_message "Backup compliance check completed with $compliance_issues issues"
    return $compliance_issues
}

# Function to check monitoring compliance
check_monitoring_compliance() {
    log_message "Checking monitoring compliance"
    
    echo "Monitoring Compliance Check:"
    echo "============================"
    
    local compliance_issues=0
    
    # Check if required monitoring services are running
    local monitoring_services=("atlas-prometheus" "atlas-grafana")
    for service in "${monitoring_services[@]}"; do
        if systemctl is-active --quiet "$service"; then
            echo "✅ $service is running"
        else
            echo "❌ $service is not running"
            compliance_issues=$((compliance_issues + 1))
        fi
    done
    
    # Check if alert manager is configured
    local alert_manager="/home/ubuntu/dev/atlas/monitoring/alert_manager.py"
    if [ -f "$alert_manager" ]; then
        echo "✅ Alert manager is configured"
    else
        echo "❌ Alert manager is not configured"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    # Check if log monitoring is configured
    local log_files=(
        "/var/log/auth.log"
        "/var/log/nginx/error.log"
        "/home/ubuntu/dev/atlas/logs/atlas_background.log"
    )
    
    local monitored_logs=0
    for log_file in "${log_files[@]}"; do
        if [ -f "$log_file" ]; then
            monitored_logs=$((monitored_logs + 1))
        fi
    done
    
    if [ $monitored_logs -ge 2 ]; then
        echo "✅ Sufficient log monitoring ($monitored_logs log files monitored)"
    else
        echo "❌ Insufficient log monitoring ($monitored_logs log files monitored)"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    log_message "Monitoring compliance check completed with $compliance_issues issues"
    return $compliance_issues
}

# Function to check update compliance
check_update_compliance() {
    log_message "Checking update compliance"
    
    echo "Update Compliance Check:"
    echo "========================"
    
    local compliance_issues=0
    
    # Check for pending security updates
    if apt list --upgradable 2>/dev/null | grep -q security; then
        echo "❌ Security updates are pending"
        compliance_issues=$((compliance_issues + 1))
    else
        echo "✅ No pending security updates"
    fi
    
    # Check if unattended upgrades are configured
    if [ -f "/etc/apt/apt.conf.d/20auto-upgrades" ]; then
        if grep -q "1" /etc/apt/apt.conf.d/20auto-upgrades; then
            echo "✅ Unattended upgrades are configured"
        else
            echo "❌ Unattended upgrades are not configured"
            compliance_issues=$((compliance_issues + 1))
        fi
    else
        echo "❌ Unattended upgrades configuration not found"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    log_message "Update compliance check completed with $compliance_issues issues"
    return $compliance_issues
}

# Function to check access control compliance
check_access_control() {
    log_message "Checking access control compliance"
    
    echo "Access Control Compliance Check:"
    echo "================================"
    
    local compliance_issues=0
    
    # Check user accounts
    local allowed_users=("ubuntu")
    local current_users=$(cut -d: -f1 /etc/passwd)
    
    for user in $current_users; do
        if [[ ! " ${allowed_users[@]} " =~ " ${user} " ]] && [ "$user" != "root" ]; then
            # Check if user has a system account (UID < 1000)
            local uid=$(id -u "$user")
            if [ $uid -ge 1000 ]; then
                echo "❌ Unauthorized user account: $user"
                compliance_issues=$((compliance_issues + 1))
            fi
        fi
    done
    
    # Check sudo access
    if groups ubuntu | grep -q sudo; then
        echo "✅ ubuntu user has sudo access"
    else
        echo "❌ ubuntu user does not have sudo access"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    # Check SSH key-based authentication
    local ssh_dir="/home/ubuntu/.ssh"
    if [ -d "$ssh_dir" ] && [ -f "$ssh_dir/authorized_keys" ]; then
        local key_count=$(wc -l < "$ssh_dir/authorized_keys")
        if [ $key_count -gt 0 ]; then
            echo "✅ SSH key-based authentication is configured ($key_count keys)"
        else
            echo "❌ No SSH keys configured for ubuntu user"
            compliance_issues=$((compliance_issues + 1))
        fi
    else
        echo "❌ SSH directory or authorized_keys file not found"
        compliance_issues=$((compliance_issues + 1))
    fi
    
    log_message "Access control compliance check completed with $compliance_issues issues"
    return $compliance_issues
}

# Function to generate compliance report
generate_compliance_report() {
    log_message "Generating compliance report"
    
    # This would generate a detailed compliance report
    # For now, we'll create a simple JSON report
    cat > $COMPLIANCE_REPORT << EOF
{
    "timestamp": "$(date -Iseconds)",
    "compliance_checks": {
        "system_security": "see logs",
        "data_protection": "see logs",
        "backup": "see logs",
        "monitoring": "see logs",
        "updates": "see logs",
        "access_control": "see logs"
    },
    "overall_status": "see logs",
    "recommendations": [
        "Review and address any failed compliance checks",
        "Implement continuous compliance monitoring",
        "Conduct regular compliance audits",
        "Update documentation for compliance procedures"
    ]
}
EOF
    
    log_message "Compliance report generated: $COMPLIANCE_REPORT"
}

# Function to send compliance notification
send_notification() {
    local status=$1
    local message=$2
    
    log_message "Compliance check $status: $message"
    
    # In a real implementation, this would send an email notification
    echo "📧 Compliance check $status: $message"
}

# Main compliance checking function
main() {
    log_message "=== Starting Atlas Compliance Check ==="
    
    # Start time
    local start_time=$(date)
    log_message "Compliance check started at: $start_time"
    
    # Initialize counters
    local total_checks=0
    local failed_checks=0
    
    # Run all compliance checks
    echo "Running compliance checks..."
    echo "============================"
    
    # System Security
    total_checks=$((total_checks + 1))
    if ! check_system_security; then
        failed_checks=$((failed_checks + 1))
    fi
    echo ""
    
    # Data Protection
    total_checks=$((total_checks + 1))
    if ! check_data_protection; then
        failed_checks=$((failed_checks + 1))
    fi
    echo ""
    
    # Backup
    total_checks=$((total_checks + 1))
    if ! check_backup_compliance; then
        failed_checks=$((failed_checks + 1))
    fi
    echo ""
    
    # Monitoring
    total_checks=$((total_checks + 1))
    if ! check_monitoring_compliance; then
        failed_checks=$((failed_checks + 1))
    fi
    echo ""
    
    # Updates
    total_checks=$((total_checks + 1))
    if ! check_update_compliance; then
        failed_checks=$((failed_checks + 1))
    fi
    echo ""
    
    # Access Control
    total_checks=$((total_checks + 1))
    if ! check_access_control; then
        failed_checks=$((failed_checks + 1))
    fi
    echo ""
    
    # Generate compliance report
    generate_compliance_report
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Compliance check completed at: $end_time (Duration: ${duration}s)"
    
    # Summary
    local passed_checks=$((total_checks - failed_checks))
    echo "Compliance Check Summary:"
    echo "========================="
    echo "Total Checks: $total_checks"
    echo "Passed: $passed_checks"
    echo "Failed: $failed_checks"
    
    if [ $failed_checks -eq 0 ]; then
        log_message "=== All Compliance Checks Passed ==="
        send_notification "SUCCESS" "All compliance checks passed ($passed_checks/$total_checks)"
        echo "✅ All Atlas compliance checks passed"
        return 0
    else
        log_message "=== $failed_checks Compliance Checks Failed ==="
        send_notification "FAILED" "$failed_checks compliance checks failed ($passed_checks/$total_checks)"
        echo "❌ $failed_checks Atlas compliance checks failed"
        return 1
    fi
}

# Handle script arguments
if [ "$1" == "--security" ]; then
    echo "Checking system security compliance..."
    check_system_security
    exit $?
elif [ "$1" == "--backup" ]; then
    echo "Checking backup compliance..."
    check_backup_compliance
    exit $?
elif [ "$1" == "--monitoring" ]; then
    echo "Checking monitoring compliance..."
    check_monitoring_compliance
    exit $?
fi

# Run full compliance check
if main; then
    exit 0
else
    exit 1
fi