#!/bin/bash

# Atlas Production Compliance Checker
# This script checks the Atlas production environment for compliance with security and operational best practices

set -e  # Exit on any error

echo "Starting Atlas Production Compliance Check..."

# Configuration
COMPLIANCE_LOG="/home/ubuntu/dev/atlas/logs/compliance_check.log"
COMPLIANCE_REPORT_DIR="/home/ubuntu/dev/atlas/reports/compliance"
CONFIG_DIR="/home/ubuntu/dev/atlas/config"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $COMPLIANCE_LOG)"
mkdir -p "$COMPLIANCE_REPORT_DIR"
mkdir -p "$CONFIG_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $COMPLIANCE_LOG
    echo "$1"
}

# Function to check system security compliance
check_system_security() {
    log_message "Checking system security compliance"
    
    echo "Checking System Security Compliance..."
    echo "===================================="
    
    local security_report="$COMPLIANCE_REPORT_DIR/system_security_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create security report header
    echo "Atlas Production System Security Compliance Check" > "$security_report"
    echo "Generated: $(date)" >> "$security_report"
    echo "=================================================" >> "$security_report"
    echo "" >> "$security_report"
    
    # Initialize counters
    local passed_checks=0
    local failed_checks=0
    
    # Check if firewall is active
    echo "Firewall Status:" >> "$security_report"
    echo "---------------" >> "$security_report"
    if sudo ufw status | grep -q "Status: active"; then
        echo "✅ Firewall is active" >> "$security_report"
        passed_checks=$((passed_checks + 1))
    else
        echo "❌ Firewall is not active" >> "$security_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$security_report"
    
    # Check SSH configuration
    echo "SSH Configuration:" >> "$security_report"
    echo "-----------------" >> "$security_report"
    if [ -f "/etc/ssh/sshd_config" ]; then
        # Check if password authentication is disabled
        if grep -q "^PasswordAuthentication no" "/etc/ssh/sshd_config"; then
            echo "✅ SSH password authentication is disabled" >> "$security_report"
            passed_checks=$((passed_checks + 1))
        else
            echo "❌ SSH password authentication is enabled" >> "$security_report"
            failed_checks=$((failed_checks + 1))
        fi
        
        # Check if root login is disabled
        if grep -q "^PermitRootLogin no" "/etc/ssh/sshd_config"; then
            echo "✅ SSH root login is disabled" >> "$security_report"
            passed_checks=$((passed_checks + 1))
        else
            echo "❌ SSH root login is enabled" >> "$security_report"
            failed_checks=$((failed_checks + 1))
        fi
        
        # Check SSH port
        local ssh_port=$(grep "^Port" "/etc/ssh/sshd_config" | awk '{print $2}')
        if [ -z "$ssh_port" ]; then
            ssh_port=22
        fi
        echo "  SSH Port: $ssh_port" >> "$security_report"
    else
        echo "❌ SSH configuration file not found" >> "$security_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$security_report"
    
    # Check for unnecessary services
    echo "Unnecessary Services:" >> "$security_report"
    echo "-------------------" >> "$security_report"
    local unnecessary_services=("telnet" "ftp" "rsh" "rexec")
    local services_found=0
    
    for service in "${unnecessary_services[@]}"; do
        if systemctl list-unit-files | grep -q "^$service"; then
            echo "❌ Unnecessary service found: $service" >> "$security_report"
            failed_checks=$((failed_checks + 1))
            services_found=$((services_found + 1))
        fi
    done
    
    if [ $services_found -eq 0 ]; then
        echo "✅ No unnecessary services found" >> "$security_report"
        passed_checks=$((passed_checks + 1))
    fi
    echo "" >> "$security_report"
    
    # Check system updates
    echo "System Updates:" >> "$security_report"
    echo "--------------" >> "$security_report"
    if apt list --upgradable 2>/dev/null | grep -q security; then
        local security_updates=$(apt list --upgradable 2>/dev/null | grep security | wc -l)
        echo "⚠️ Security updates available: $security_updates" >> "$security_report"
        echo "   Run 'sudo unattended-upgrade' to install security updates" >> "$security_report"
        failed_checks=$((failed_checks + 1))
    else
        echo "✅ No security updates pending" >> "$security_report"
        passed_checks=$((passed_checks + 1))
    fi
    echo "" >> "$security_report"
    
    # Summary
    echo "System Security Summary:" >> "$security_report"
    echo "----------------------" >> "$security_report"
    echo "Passed Checks: $passed_checks" >> "$security_report"
    echo "Failed Checks: $failed_checks" >> "$security_report"
    echo "Overall Status: " >> "$security_report"
    if [ $failed_checks -eq 0 ]; then
        echo "  ✅ COMPLIANT" >> "$security_report"
    else
        echo "  ❌ NON-COMPLIANT" >> "$security_report"
    fi
    echo "" >> "$security_report"
    
    echo "✅ System security compliance check completed"
    echo "📋 Security report saved to: $security_report"
    log_message "System security compliance check completed: $security_report"
    
    # Display summary
    echo ""
    echo "System Security Summary:"
    echo "  Passed Checks: $passed_checks"
    echo "  Failed Checks: $failed_checks"
    if [ $failed_checks -eq 0 ]; then
        echo "  Status: ✅ COMPLIANT"
    else
        echo "  Status: ❌ NON-COMPLIANT"
    fi
    echo "  Report: $security_report"
}

# Function to check application security compliance
check_application_security() {
    log_message "Checking application security compliance"
    
    echo ""
    echo "Checking Application Security Compliance..."
    echo "=========================================="
    
    local app_security_report="$COMPLIANCE_REPORT_DIR/app_security_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create application security report header
    echo "Atlas Production Application Security Compliance Check" > "$app_security_report"
    echo "Generated: $(date)" >> "$app_security_report"
    echo "=======================================================" >> "$app_security_report"
    echo "" >> "$app_security_report"
    
    # Initialize counters
    local passed_checks=0
    local failed_checks=0
    
    # Check web server security
    echo "Web Server Security:" >> "$app_security_report"
    echo "-------------------" >> "$app_security_report"
    
    # Check if Nginx is running
    if systemctl is-active --quiet nginx; then
        echo "✅ Nginx is running" >> "$app_security_report"
        passed_checks=$((passed_checks + 1))
        
        # Check SSL configuration
        if [ -f "/etc/nginx/sites-available/atlas" ]; then
            if grep -q "ssl_certificate" "/etc/nginx/sites-available/atlas"; then
                echo "✅ SSL is configured for web interface" >> "$app_security_report"
                passed_checks=$((passed_checks + 1))
            else
                echo "❌ SSL is not configured for web interface" >> "$app_security_report"
                failed_checks=$((failed_checks + 1))
            fi
            
            # Check authentication configuration
            if grep -q "auth_basic" "/etc/nginx/sites-available/atlas"; then
                echo "✅ Authentication is configured for web interface" >> "$app_security_report"
                passed_checks=$((passed_checks + 1))
            else
                echo "❌ Authentication is not configured for web interface" >> "$app_security_report"
                failed_checks=$((failed_checks + 1))
            fi
        else
            echo "❌ Nginx configuration file not found" >> "$app_security_report"
            failed_checks=$((failed_checks + 1))
        fi
    else
        echo "❌ Nginx is not running" >> "$app_security_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$app_security_report"
    
    # Check application configuration security
    echo "Application Configuration Security:" >> "$app_security_report"
    echo "-----------------------------------" >> "$app_security_report"
    
    # Check .env file permissions
    local env_file="/home/ubuntu/dev/atlas/.env"
    if [ -f "$env_file" ]; then
        local env_permissions=$(stat -c "%a" "$env_file")
        if [ "$env_permissions" = "600" ] || [ "$env_permissions" = "640" ]; then
            echo "✅ .env file has secure permissions ($env_permissions)" >> "$app_security_report"
            passed_checks=$((passed_checks + 1))
        else
            echo "❌ .env file has insecure permissions ($env_permissions)" >> "$app_security_report"
            failed_checks=$((failed_checks + 1))
        fi
        
        # Check for sensitive information in .env
        if grep -q "PASSWORD\|SECRET\|KEY" "$env_file"; then
            echo "ℹ️ .env file contains sensitive information (review manually)" >> "$app_security_report"
        fi
    else
        echo "❌ .env file not found" >> "$app_security_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$app_security_report"
    
    # Check database security
    echo "Database Security:" >> "$app_security_report"
    echo "------------------" >> "$app_security_report"
    
    # Check if PostgreSQL is running
    if systemctl is-active --quiet postgresql; then
        echo "✅ PostgreSQL is running" >> "$app_security_report"
        passed_checks=$((passed_checks + 1))
        
        # Check database connectivity
        if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
            echo "✅ Database is accessible" >> "$app_security_report"
            passed_checks=$((passed_checks + 1))
        else
            echo "❌ Database is not accessible" >> "$app_security_report"
            failed_checks=$((failed_checks + 1))
        fi
        
        # Check database user permissions
        local db_user_check=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT rolname FROM pg_roles WHERE rolname = 'atlas_user';" 2>/dev/null || echo "")
        if [ ! -z "$db_user_check" ]; then
            echo "✅ Database user 'atlas_user' exists" >> "$app_security_report"
            passed_checks=$((passed_checks + 1))
        else
            echo "❌ Database user 'atlas_user' does not exist" >> "$app_security_report"
            failed_checks=$((failed_checks + 1))
        fi
    else
        echo "❌ PostgreSQL is not running" >> "$app_security_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$app_security_report"
    
    # Check monitoring security
    echo "Monitoring Security:" >> "$app_security_report"
    echo "-------------------" >> "$app_security_report"
    
    # Check if Prometheus is running
    if systemctl is-active --quiet atlas-prometheus; then
        echo "✅ Prometheus is running" >> "$app_security_report"
        passed_checks=$((passed_checks + 1))
        
        # Check if Prometheus is bound to localhost only
        local prometheus_config="/home/ubuntu/dev/atlas/monitoring/prometheus.yml"
        if [ -f "$prometheus_config" ]; then
            if grep -q "web.listen-address: localhost:9090" "$prometheus_config"; then
                echo "✅ Prometheus is bound to localhost only" >> "$app_security_report"
                passed_checks=$((passed_checks + 1))
            else
                echo "⚠️ Prometheus may be accessible externally (check configuration)" >> "$app_security_report"
            fi
        else
            echo "❌ Prometheus configuration not found" >> "$app_security_report"
            failed_checks=$((failed_checks + 1))
        fi
    else
        echo "❌ Prometheus is not running" >> "$app_security_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$app_security_report"
    
    # Check Grafana security
    echo "Grafana Security:" >> "$app_security_report"
    echo "----------------" >> "$app_security_report"
    
    # Check if Grafana is running
    if systemctl is-active --quiet atlas-grafana; then
        echo "✅ Grafana is running" >> "$app_security_report"
        passed_checks=$((passed_checks + 1))
        
        # Check Grafana admin password
        local grafana_config="/etc/grafana/grafana.ini"
        if [ -f "$grafana_config" ]; then
            if grep -q "admin_password = admin" "$grafana_config"; then
                echo "❌ Grafana admin password is default ('admin')" >> "$app_security_report"
                failed_checks=$((failed_checks + 1))
            else
                echo "✅ Grafana admin password is not default" >> "$app_security_report"
                passed_checks=$((passed_checks + 1))
            fi
        else
            echo "❌ Grafana configuration not found" >> "$app_security_report"
            failed_checks=$((failed_checks + 1))
        fi
    else
        echo "❌ Grafana is not running" >> "$app_security_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$app_security_report"
    
    # Summary
    echo "Application Security Summary:" >> "$app_security_report"
    echo "----------------------------" >> "$app_security_report"
    echo "Passed Checks: $passed_checks" >> "$app_security_report"
    echo "Failed Checks: $failed_checks" >> "$app_security_report"
    echo "Overall Status: " >> "$app_security_report"
    if [ $failed_checks -eq 0 ]; then
        echo "  ✅ COMPLIANT" >> "$app_security_report"
    else
        echo "  ❌ NON-COMPLIANT" >> "$app_security_report"
    fi
    echo "" >> "$app_security_report"
    
    echo "✅ Application security compliance check completed"
    echo "📋 Application security report saved to: $app_security_report"
    log_message "Application security compliance check completed: $app_security_report"
    
    # Display summary
    echo ""
    echo "Application Security Summary:"
    echo "  Passed Checks: $passed_checks"
    echo "  Failed Checks: $failed_checks"
    if [ $failed_checks -eq 0 ]; then
        echo "  Status: ✅ COMPLIANT"
    else
        echo "  Status: ❌ NON-COMPLIANT"
    fi
    echo "  Report: $app_security_report"
}

# Function to check data protection compliance
check_data_protection() {
    log_message "Checking data protection compliance"
    
    echo ""
    echo "Checking Data Protection Compliance..."
    echo "====================================="
    
    local data_protection_report="$COMPLIANCE_REPORT_DIR/data_protection_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create data protection report header
    echo "Atlas Production Data Protection Compliance Check" > "$data_protection_report"
    echo "Generated: $(date)" >> "$data_protection_report"
    echo "==================================================" >> "$data_protection_report"
    echo "" >> "$data_protection_report"
    
    # Initialize counters
    local passed_checks=0
    local failed_checks=0
    
    # Check SSL certificate validity
    echo "SSL Certificate:" >> "$data_protection_report"
    echo "---------------" >> "$data_protection_report"
    
    local cert_file="/etc/letsencrypt/live/atlas.khamel.com/cert.pem"
    if [ -f "$cert_file" ]; then
        # Check certificate expiration
        local cert_expiry=$(openssl x509 -in "$cert_file" -noout -enddate 2>/dev/null | cut -d= -f2)
        if [ ! -z "$cert_expiry" ]; then
            local expiry_seconds=$(date -d "$cert_expiry" +%s 2>/dev/null)
            local current_seconds=$(date +%s)
            
            if [ $current_seconds -lt $expiry_seconds ]; then
                local days_until_expiry=$(( (expiry_seconds - current_seconds) / 86400 ))
                echo "✅ SSL certificate is valid (expires in $days_until_expiry days)" >> "$data_protection_report"
                passed_checks=$((passed_checks + 1))
                
                if [ $days_until_expiry -lt 30 ]; then
                    echo "⚠️ SSL certificate expires soon (less than 30 days)" >> "$data_protection_report"
                fi
            else
                echo "❌ SSL certificate has expired" >> "$data_protection_report"
                failed_checks=$((failed_checks + 1))
            fi
        else
            echo "❌ Unable to check SSL certificate expiration" >> "$data_protection_report"
            failed_checks=$((failed_checks + 1))
        fi
    else
        echo "❌ SSL certificate not found" >> "$data_protection_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$data_protection_report"
    
    # Check database encryption
    echo "Database Encryption:" >> "$data_protection_report"
    echo "--------------------" >> "$data_protection_report"
    
    # Check if PostgreSQL has SSL enabled
    if sudo -u postgres psql -tAc "SHOW ssl;" 2>/dev/null | grep -q "on"; then
        echo "✅ Database SSL is enabled" >> "$data_protection_report"
        passed_checks=$((passed_checks + 1))
    else
        echo "❌ Database SSL is not enabled" >> "$data_protection_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$data_protection_report"
    
    # Check backup encryption
    echo "Backup Encryption:" >> "$data_protection_report"
    echo "-----------------" >> "$data_protection_report"
    
    # Check if backup script exists and implements encryption
    local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
    if [ -f "$backup_script" ]; then
        if grep -q "encryption\|gpg\|openssl" "$backup_script"; then
            echo "✅ Backup encryption appears to be implemented" >> "$data_protection_report"
            passed_checks=$((passed_checks + 1))
        else
            echo "⚠️ Backup encryption not found in backup script" >> "$data_protection_report"
            # Not counting as failed since it's a warning
        fi
    else
        echo "❌ Backup script not found" >> "$data_protection_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$data_protection_report"
    
    # Check file permissions
    echo "File Permissions:" >> "$data_protection_report"
    echo "-----------------" >> "$data_protection_report"
    
    # Check sensitive files
    local sensitive_files=(
        "/home/ubuntu/dev/atlas/.env:Environment file"
        "/etc/nginx/.htpasswd:Authentication file"
        "/home/ubuntu/dev/atlas/backups:Backup directory"
    )
    
    local permission_issues=0
    for file_info in "${sensitive_files[@]}"; do
        local file_path=$(echo $file_info | cut -d: -f1)
        local file_desc=$(echo $file_info | cut -d: -f2)
        
        if [ -e "$file_path" ]; then
            local permissions=$(stat -c "%a" "$file_path" 2>/dev/null)
            
            # Check if permissions are secure
            if [ "$permissions" = "600" ] || [ "$permissions" = "640" ] || [ "$permissions" = "700" ]; then
                echo "✅ $file_desc has secure permissions ($permissions)" >> "$data_protection_report"
                passed_checks=$((passed_checks + 1))
            else
                echo "❌ $file_desc has insecure permissions ($permissions)" >> "$data_protection_report"
                failed_checks=$((failed_checks + 1))
                permission_issues=$((permission_issues + 1))
            fi
        else
            echo "❌ $file_desc not found" >> "$data_protection_report"
            failed_checks=$((failed_checks + 1))
        fi
    done
    
    if [ $permission_issues -eq 0 ]; then
        echo "✅ All sensitive files have secure permissions" >> "$data_protection_report"
        passed_checks=$((passed_checks + 1))
    else
        echo "❌ Some sensitive files have insecure permissions" >> "$data_protection_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$data_protection_report"
    
    # Summary
    echo "Data Protection Summary:" >> "$data_protection_report"
    echo "----------------------" >> "$data_protection_report"
    echo "Passed Checks: $passed_checks" >> "$data_protection_report"
    echo "Failed Checks: $failed_checks" >> "$data_protection_report"
    echo "Overall Status: " >> "$data_protection_report"
    if [ $failed_checks -eq 0 ]; then
        echo "  ✅ COMPLIANT" >> "$data_protection_report"
    else
        echo "  ❌ NON-COMPLIANT" >> "$data_protection_report"
    fi
    echo "" >> "$data_protection_report"
    
    echo "✅ Data protection compliance check completed"
    echo "📋 Data protection report saved to: $data_protection_report"
    log_message "Data protection compliance check completed: $data_protection_report"
    
    # Display summary
    echo ""
    echo "Data Protection Summary:"
    echo "  Passed Checks: $passed_checks"
    echo "  Failed Checks: $failed_checks"
    if [ $failed_checks -eq 0 ]; then
        echo "  Status: ✅ COMPLIANT"
    else
        echo "  Status: ❌ NON-COMPLIANT"
    fi
    echo "  Report: $data_protection_report"
}

# Function to check operational compliance
check_operational_compliance() {
    log_message "Checking operational compliance"
    
    echo ""
    echo "Checking Operational Compliance..."
    echo "================================="
    
    local operational_report="$COMPLIANCE_REPORT_DIR/operational_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create operational compliance report header
    echo "Atlas Production Operational Compliance Check" > "$operational_report"
    echo "Generated: $(date)" >> "$operational_report"
    echo "=============================================" >> "$operational_report"
    echo "" >> "$operational_report"
    
    # Initialize counters
    local passed_checks=0
    local failed_checks=0
    
    # Check monitoring configuration
    echo "Monitoring Configuration:" >> "$operational_report"
    echo "------------------------" >> "$operational_report"
    
    # Check if all monitoring services are running
    local monitoring_services=("atlas-prometheus" "atlas-grafana")
    local monitoring_running=0
    
    for service in "${monitoring_services[@]}"; do
        if systemctl is-active --quiet $service; then
            echo "✅ $service is running" >> "$operational_report"
            monitoring_running=$((monitoring_running + 1))
        else
            echo "❌ $service is not running" >> "$operational_report"
            failed_checks=$((failed_checks + 1))
        fi
    done
    
    if [ $monitoring_running -eq ${#monitoring_services[@]} ]; then
        echo "✅ All monitoring services are running" >> "$operational_report"
        passed_checks=$((passed_checks + 1))
    else
        echo "❌ Some monitoring services are not running" >> "$operational_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$operational_report"
    
    # Check backup configuration
    echo "Backup Configuration:" >> "$operational_report"
    echo "---------------------" >> "$operational_report"
    
    # Check if backup directory exists
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        echo "✅ Backup directory exists" >> "$operational_report"
        passed_checks=$((passed_checks + 1))
        
        # Check if backup script exists
        local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
        if [ -f "$backup_script" ]; then
            echo "✅ Backup script exists" >> "$operational_report"
            passed_checks=$((passed_checks + 1))
            
            # Check if backup cron job is configured
            if crontab -l 2>/dev/null | grep -q "production_backup.sh"; then
                echo "✅ Backup cron job is configured" >> "$operational_report"
                passed_checks=$((passed_checks + 1))
            else
                echo "❌ Backup cron job is not configured" >> "$operational_report"
                failed_checks=$((failed_checks + 1))
            fi
        else
            echo "❌ Backup script not found" >> "$operational_report"
            failed_checks=$((failed_checks + 1))
        fi
    else
        echo "❌ Backup directory not found" >> "$operational_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$operational_report"
    
    # Check logging configuration
    echo "Logging Configuration:" >> "$operational_report"
    echo "---------------------" >> "$operational_report"
    
    # Check if log directory exists
    local log_dir="/home/ubuntu/dev/atlas/logs"
    if [ -d "$log_dir" ]; then
        echo "✅ Log directory exists" >> "$operational_report"
        passed_checks=$((passed_checks + 1))
        
        # Check if log rotation is configured
        if [ -f "/etc/logrotate.d/atlas" ]; then
            echo "✅ Log rotation is configured" >> "$operational_report"
            passed_checks=$((passed_checks + 1))
        else
            echo "❌ Log rotation is not configured" >> "$operational_report"
            failed_checks=$((failed_checks + 1))
        fi
    else
        echo "❌ Log directory not found" >> "$operational_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$operational_report"
    
    # Check systemd services
    echo "Systemd Services:" >> "$operational_report"
    echo "----------------" >> "$operational_report"
    
    # Check if critical services are configured to start on boot
    local critical_services=("atlas" "postgresql" "nginx")
    local services_enabled=0
    
    for service in "${critical_services[@]}"; do
        if systemctl is-enabled --quiet $service; then
            echo "✅ $service is enabled to start on boot" >> "$operational_report"
            services_enabled=$((services_enabled + 1))
        else
            echo "❌ $service is not enabled to start on boot" >> "$operational_report"
            failed_checks=$((failed_checks + 1))
        fi
    done
    
    if [ $services_enabled -eq ${#critical_services[@]} ]; then
        echo "✅ All critical services are enabled to start on boot" >> "$operational_report"
        passed_checks=$((passed_checks + 1))
    else
        echo "❌ Some critical services are not enabled to start on boot" >> "$operational_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$operational_report"
    
    # Check user management
    echo "User Management:" >> "$operational_report"
    echo "----------------" >> "$operational_report"
    
    # Check if only authorized users have access
    local authorized_users=("ubuntu")
    local current_users=$(cut -d: -f1 /etc/passwd)
    local unauthorized_users=0
    
    while IFS= read -r user; do
        if [[ ! " ${authorized_users[*]} " =~ " ${user} " ]]; then
            # Skip system users
            if [ "$user" != "root" ] && [ "$user" != "daemon" ] && [ "$user" != "bin" ] && [ "$user" != "sys" ] && [ "$user" != "sync" ] && [ "$user" != "games" ] && [ "$user" != "man" ] && [ "$user" != "lp" ] && [ "$user" != "mail" ] && [ "$user" != "news" ] && [ "$user" != "uucp" ] && [ "$user" != "proxy" ] && [ "$user" != "www-data" ] && [ "$user" != "backup" ] && [ "$user" != "list" ] && [ "$user" != "irc" ] && [ "$user" != "gnats" ] && [ "$user" != "nobody" ] && [ "$user" != "systemd-network" ] && [ "$user" != "systemd-resolve" ] && [ "$user" != "syslog" ] && [ "$user" != "messagebus" ] && [ "$user" != "landscape" ] && [ "$user" != "_apt" ] && [ "$user" != "uuidd" ] && [ "$user" != "whoopsie" ] && [ "$user" != "sshd" ] && [ "$user" != "pollinate" ] && [ "$user" != "postgres" ]; then
                echo "❌ Unauthorized user found: $user" >> "$operational_report"
                unauthorized_users=$((unauthorized_users + 1))
                failed_checks=$((failed_checks + 1))
            fi
        fi
    done <<< "$current_users"
    
    if [ $unauthorized_users -eq 0 ]; then
        echo "✅ No unauthorized users found" >> "$operational_report"
        passed_checks=$((passed_checks + 1))
    else
        echo "❌ Unauthorized users found" >> "$operational_report"
        failed_checks=$((failed_checks + 1))
    fi
    echo "" >> "$operational_report"
    
    # Summary
    echo "Operational Compliance Summary:" >> "$operational_report"
    echo "------------------------------" >> "$operational_report"
    echo "Passed Checks: $passed_checks" >> "$operational_report"
    echo "Failed Checks: $failed_checks" >> "$operational_report"
    echo "Overall Status: " >> "$operational_report"
    if [ $failed_checks -eq 0 ]; then
        echo "  ✅ COMPLIANT" >> "$operational_report"
    else
        echo "  ❌ NON-COMPLIANT" >> "$operational_report"
    fi
    echo "" >> "$operational_report"
    
    echo "✅ Operational compliance check completed"
    echo "📋 Operational report saved to: $operational_report"
    log_message "Operational compliance check completed: $operational_report"
    
    # Display summary
    echo ""
    echo "Operational Compliance Summary:"
    echo "  Passed Checks: $passed_checks"
    echo "  Failed Checks: $failed_checks"
    if [ $failed_checks -eq 0 ]; then
        echo "  Status: ✅ COMPLIANT"
    else
        echo "  Status: ❌ NON-COMPLIANT"
    fi
    echo "  Report: $operational_report"
}

# Function to generate compliance summary
generate_compliance_summary() {
    log_message "Generating compliance summary"
    
    echo ""
    echo "Generating Compliance Summary..."
    echo "=============================="
    
    local summary_report="$COMPLIANCE_REPORT_DIR/compliance_summary_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create compliance summary report header
    echo "Atlas Production Compliance Summary" > "$summary_report"
    echo "Generated: $(date)" >> "$summary_report"
    echo "==================================" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add system information
    echo "System Information:" >> "$summary_report"
    echo "------------------" >> "$summary_report"
    echo "Hostname: $(hostname)" >> "$summary_report"
    echo "OS: $(lsb_release -d | cut -f2)" >> "$summary_report"
    echo "Kernel: $(uname -r)" >> "$summary_report"
    echo "Checked by: $(whoami)" >> "$summary_report"
    echo "Check time: $(date)" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Aggregate compliance results
    echo "Compliance Summary:" >> "$summary_report"
    echo "------------------" >> "$summary_report"
    
    # Count total passed and failed checks
    local total_passed=0
    local total_failed=0
    
    # Check system security results
    local system_security_report=$(ls -t $COMPLIANCE_REPORT_DIR/system_security_*.txt 2>/dev/null | head -1)
    if [ -f "$system_security_report" ]; then
        local system_passed=$(grep "Passed Checks:" "$system_security_report" | awk '{print $3}')
        local system_failed=$(grep "Failed Checks:" "$system_security_report" | awk '{print $3}')
        total_passed=$((total_passed + system_passed))
        total_failed=$((total_failed + system_failed))
    fi
    
    # Check application security results
    local app_security_report=$(ls -t $COMPLIANCE_REPORT_DIR/app_security_*.txt 2>/dev/null | head -1)
    if [ -f "$app_security_report" ]; then
        local app_passed=$(grep "Passed Checks:" "$app_security_report" | awk '{print $3}')
        local app_failed=$(grep "Failed Checks:" "$app_security_report" | awk '{print $3}')
        total_passed=$((total_passed + app_passed))
        total_failed=$((total_failed + app_failed))
    fi
    
    # Check data protection results
    local data_protection_report=$(ls -t $COMPLIANCE_REPORT_DIR/data_protection_*.txt 2>/dev/null | head -1)
    if [ -f "$data_protection_report" ]; then
        local data_passed=$(grep "Passed Checks:" "$data_protection_report" | awk '{print $3}')
        local data_failed=$(grep "Failed Checks:" "$data_protection_report" | awk '{print $3}')
        total_passed=$((total_passed + data_passed))
        total_failed=$((total_failed + data_failed))
    fi
    
    # Check operational compliance results
    local operational_report=$(ls -t $COMPLIANCE_REPORT_DIR/operational_*.txt 2>/dev/null | head -1)
    if [ -f "$operational_report" ]; then
        local op_passed=$(grep "Passed Checks:" "$operational_report" | awk '{print $3}')
        local op_failed=$(grep "Failed Checks:" "$operational_report" | awk '{print $3}')
        total_passed=$((total_passed + op_passed))
        total_failed=$((total_failed + op_failed))
    fi
    
    echo "Total Passed Checks: $total_passed" >> "$summary_report"
    echo "Total Failed Checks: $total_failed" >> "$summary_report"
    echo "Overall Compliance Status: " >> "$summary_report"
    
    if [ $total_failed -eq 0 ]; then
        echo "  ✅ FULLY COMPLIANT" >> "$summary_report"
    elif [ $total_failed -lt 5 ]; then
        echo "  ⚠️ MOSTLY COMPLIANT (Minor issues)" >> "$summary_report"
    else
        echo "  ❌ NON-COMPLIANT (Significant issues)" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Add recommendations
    echo "Recommendations:" >> "$summary_report"
    echo "--------------" >> "$summary_report"
    
    if [ $total_failed -eq 0 ]; then
        echo "✅ System is fully compliant with security and operational best practices" >> "$summary_report"
        echo "✅ Continue regular compliance checks and monitoring" >> "$summary_report"
    else
        echo "❌ Address the failed compliance checks immediately" >> "$summary_report"
        echo "❌ Review detailed reports in $COMPLIANCE_REPORT_DIR" >> "$summary_report"
        echo "❌ Implement recommended security measures" >> "$summary_report"
        echo "❌ Schedule regular compliance reviews" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Add next steps
    echo "Next Steps:" >> "$summary_report"
    echo "----------" >> "$summary_report"
    echo "1. Review detailed compliance reports" >> "$summary_report"
    echo "2. Address failed compliance checks" >> "$summary_report"
    echo "3. Implement recommended security measures" >> "$summary_report"
    echo "4. Schedule regular compliance reviews" >> "$summary_report"
    echo "5. Document compliance procedures" >> "$summary_report"
    echo "" >> "$summary_report"
    
    echo "✅ Compliance summary generated"
    echo "📋 Summary report saved to: $summary_report"
    log_message "Compliance summary generated: $summary_report"
    
    # Display summary
    echo ""
    echo "Compliance Summary:"
    echo "  Total Passed Checks: $total_passed"
    echo "  Total Failed Checks: $total_failed"
    if [ $total_failed -eq 0 ]; then
        echo "  Status: ✅ FULLY COMPLIANT"
    elif [ $total_failed -lt 5 ]; then
        echo "  Status: ⚠️ MOSTLY COMPLIANT (Minor issues)"
    else
        echo "  Status: ❌ NON-COMPLIANT (Significant issues)"
    fi
    echo "  Report: $summary_report"
}

# Function to clean old compliance reports
clean_old_reports() {
    log_message "Cleaning old compliance reports"
    
    echo ""
    echo "Cleaning Old Compliance Reports..."
    echo "================================"
    
    # Remove compliance reports older than 90 days
    find "$COMPLIANCE_REPORT_DIR" -name "system_security_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$COMPLIANCE_REPORT_DIR" -name "app_security_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$COMPLIANCE_REPORT_DIR" -name "data_protection_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$COMPLIANCE_REPORT_DIR" -name "operational_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$COMPLIANCE_REPORT_DIR" -name "compliance_summary_*.txt" -mtime +90 -delete 2>/dev/null || true
    
    echo "✅ Old compliance reports cleaned"
    log_message "Old compliance reports cleaned"
}

# Main compliance checker function
main() {
    log_message "=== Starting Atlas Compliance Check ==="
    
    # Start time
    local start_time=$(date)
    log_message "Compliance check started at: $start_time"
    
    # Handle different compliance operations
    case $1 in
        "system")
            check_system_security
            ;;
        "application")
            check_application_security
            ;;
        "data")
            check_data_protection
            ;;
        "operational")
            check_operational_compliance
            ;;
        "summary")
            generate_compliance_summary
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive compliance check
            check_system_security
            check_application_security
            check_data_protection
            check_operational_compliance
            generate_compliance_summary
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Compliance check completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Compliance Check Completed ==="
    
    echo ""
    echo "✅ Compliance check complete!"
    echo "📊 Reports saved to: $COMPLIANCE_REPORT_DIR"
    echo "📝 Log file: $COMPLIANCE_LOG"
}

# Run main function
main "$@"