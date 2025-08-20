#!/bin/bash

# Atlas Production Legal Compliance Script
# This script ensures legal compliance for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Legal Compliance..."

# Configuration
COMPLIANCE_LOG="/home/ubuntu/dev/atlas/logs/legal_compliance.log"
COMPLIANCE_REPORT_DIR="/home/ubuntu/dev/atlas/reports/compliance"
COMPLIANCE_CONFIG="/home/ubuntu/dev/atlas/config/compliance.json"
POLICY_DIR="/home/ubuntu/dev/atlas/docs/policies"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $COMPLIANCE_LOG)"
mkdir -p "$COMPLIANCE_REPORT_DIR"
mkdir -p "$POLICY_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $COMPLIANCE_LOG
    echo "$1"
}

# Function to initialize compliance configuration
initialize_compliance_config() {
    log_message "Initializing compliance configuration"
    
    # Create default compliance configuration if it doesn't exist
    if [ ! -f "$COMPLIANCE_CONFIG" ]; then
        cat > "$COMPLIANCE_CONFIG" << EOF
{
    "compliance": {
        "regulations": [
            "gdpr",
            "ccpa",
            "hipaa",
            "soc2"
        ],
        "standards": [
            "iso27001",
            "nist_csf"
        ],
        "jurisdictions": [
            "eu",
            "us",
            "global"
        ]
    },
    "data_protection": {
        "encryption_required": true,
        "data_retention_months": 24,
        "right_to_delete": true,
        "data_portability": true
    },
    "privacy": {
        "privacy_policy_required": true,
        "cookie_consent_required": true,
        "data_processing_agreement": true
    },
    "security": {
        "access_control_required": true,
        "audit_logging_required": true,
        "incident_response_required": true
    },
    "reporting": {
        "frequency": "quarterly",
        "recipients": ["legal@khamel.com", "admin@khamel.com"],
        "format": "pdf"
    }
}
EOF
        echo "✅ Created default compliance configuration"
        log_message "Default compliance configuration created"
    else
        echo "✅ Compliance configuration already exists"
    fi
}

# Function to check data protection compliance
check_data_protection_compliance() {
    log_message "Checking data protection compliance"
    
    echo "Checking Data Protection Compliance..."
    echo "======================================"
    
    local data_protection_report="$COMPLIANCE_REPORT_DIR/data_protection_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create data protection report header
    echo "Atlas Production Data Protection Compliance Check" > "$data_protection_report"
    echo "Generated: $(date)" >> "$data_protection_report"
    echo "===================================================" >> "$data_protection_report"
    echo "" >> "$data_protection_report"
    
    # Get data protection requirements
    local encryption_required=$(jq -r '.data_protection.encryption_required' "$COMPLIANCE_CONFIG")
    local data_retention_months=$(jq -r '.data_protection.data_retention_months' "$COMPLIANCE_CONFIG")
    local right_to_delete=$(jq -r '.data_protection.right_to_delete' "$COMPLIANCE_CONFIG")
    local data_portability=$(jq -r '.data_protection.data_portability' "$COMPLIANCE_CONFIG")
    
    echo "Data Protection Requirements:" >> "$data_protection_report"
    echo "----------------------------" >> "$data_protection_report"
    echo "Encryption Required: $encryption_required" >> "$data_protection_report"
    echo "Data Retention: ${data_retention_months} months" >> "$data_protection_report"
    echo "Right to Delete: $right_to_delete" >> "$data_protection_report"
    echo "Data Portability: $data_portability" >> "$data_protection_report"
    echo "" >> "$data_protection_report"
    
    # Check encryption compliance
    echo "Encryption Compliance:" >> "$data_protection_report"
    echo "---------------------" >> "$data_protection_report"
    
    local encryption_compliant=true
    
    # Check database encryption
    if sudo -u postgres psql -tAc "SHOW ssl;" 2>/dev/null | grep -q "on"; then
        echo "✅ Database SSL encryption is enabled" >> "$data_protection_report"
    else
        echo "❌ Database SSL encryption is not enabled" >> "$data_protection_report"
        encryption_compliant=false
    fi
    
    # Check backup encryption
    local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
    if [ -f "$backup_script" ] && grep -q "encryption\|gpg\|openssl" "$backup_script"; then
        echo "✅ Backup encryption is implemented" >> "$data_protection_report"
    elif [ -f "$backup_script" ]; then
        echo "❌ Backup encryption not found in backup script" >> "$data_protection_report"
        encryption_compliant=false
    else
        echo "❌ Backup script not found" >> "$data_protection_report"
        encryption_compliant=false
    fi
    
    # Check file encryption
    local sensitive_files=(
        "/home/ubuntu/dev/atlas/.env:Environment file"
        "/etc/nginx/.htpasswd:Authentication file"
        "/home/ubuntu/dev/atlas/backups:Backup directory"
    )
    
    local file_encryption_issues=0
    for file_info in "${sensitive_files[@]}"; do
        local file_path=$(echo $file_info | cut -d: -f1)
        local file_desc=$(echo $file_info | cut -d: -f2)
        
        if [ -e "$file_path" ]; then
            # Check if file is properly secured
            local permissions=$(stat -c "%a" "$file_path" 2>/dev/null)
            if [ "$permissions" = "600" ] || [ "$permissions" = "640" ] || [ "$permissions" = "700" ]; then
                echo "✅ $file_desc has secure permissions ($permissions)" >> "$data_protection_report"
            else
                echo "❌ $file_desc has insecure permissions ($permissions)" >> "$data_protection_report"
                file_encryption_issues=$((file_encryption_issues + 1))
                encryption_compliant=false
            fi
        else
            echo "❌ $file_desc not found" >> "$data_protection_report"
            file_encryption_issues=$((file_encryption_issues + 1))
            encryption_compliant=false
        fi
    done
    
    if [ $file_encryption_issues -eq 0 ]; then
        echo "✅ All sensitive files have secure permissions" >> "$data_protection_report"
    else
        echo "❌ Some sensitive files have insecure permissions" >> "$data_protection_report"
    fi
    echo "" >> "$data_protection_report"
    
    # Check data retention compliance
    echo "Data Retention Compliance:" >> "$data_protection_report"
    echo "-------------------------" >> "$data_protection_report"
    
    local retention_compliant=true
    
    # Check backup retention
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        # Count backups older than retention period
        local old_backups=$(find "$backup_dir" -name "*.sql*" -mtime +$((data_retention_months * 30)) | wc -l)
        if [ $old_backups -eq 0 ]; then
            echo "✅ No backups older than ${data_retention_months} months found" >> "$data_protection_report"
        else
            echo "❌ $old_backups backups found that are older than ${data_retention_months} months" >> "$data_protection_report"
            retention_compliant=false
        fi
        
        # Check log retention
        local log_dir="/home/ubuntu/dev/atlas/logs"
        if [ -d "$log_dir" ]; then
            local old_logs=$(find "$log_dir" -name "*.log" -mtime +$((data_retention_months * 30)) | wc -l)
            if [ $old_logs -eq 0 ]; then
                echo "✅ No logs older than ${data_retention_months} months found" >> "$data_protection_report"
            else
                echo "❌ $old_logs log files found that are older than ${data_retention_months} months" >> "$data_protection_report"
                retention_compliant=false
            fi
        else
            echo "❌ Log directory not found" >> "$data_protection_report"
            retention_compliant=false
        fi
    else
        echo "❌ Backup directory not found" >> "$data_protection_report"
        retention_compliant=false
    fi
    echo "" >> "$data_protection_report"
    
    # Check right to delete compliance
    echo "Right to Delete Compliance:" >> "$data_protection_report"
    echo "---------------------------" >> "$data_protection_report"
    
    local delete_compliant=true
    
    # Check if delete functionality exists
    local delete_script="/home/ubuntu/dev/atlas/scripts/delete_user_data.sh"
    if [ -f "$delete_script" ]; then
        echo "✅ User data deletion script exists" >> "$data_protection_report"
    else
        echo "❌ User data deletion script not found" >> "$data_protection_report"
        echo "   Recommendation: Implement user data deletion functionality" >> "$data_protection_report"
        delete_compliant=false
    fi
    echo "" >> "$data_protection_report"
    
    # Check data portability compliance
    echo "Data Portability Compliance:" >> "$data_protection_report"
    echo "---------------------------" >> "$data_protection_report"
    
    local portability_compliant=true
    
    # Check if data export functionality exists
    local export_script="/home/ubuntu/dev/atlas/scripts/export_user_data.sh"
    if [ -f "$export_script" ]; then
        echo "✅ User data export script exists" >> "$data_protection_report"
    else
        echo "❌ User data export script not found" >> "$data_protection_report"
        echo "   Recommendation: Implement user data export functionality" >> "$data_protection_report"
        portability_compliant=false
    fi
    echo "" >> "$data_protection_report"
    
    # Summary
    echo "Data Protection Compliance Summary:" >> "$data_protection_report"
    echo "----------------------------------" >> "$data_protection_report"
    
    if $encryption_required && $encryption_compliant; then
        echo "✅ Encryption: COMPLIANT" >> "$data_protection_report"
    elif $encryption_required; then
        echo "❌ Encryption: NON-COMPLIANT" >> "$data_protection_report"
    else
        echo "ℹ️ Encryption: Not Required" >> "$data_protection_report"
    fi
    
    if [ $data_retention_months -gt 0 ] && $retention_compliant; then
        echo "✅ Data Retention: COMPLIANT" >> "$data_protection_report"
    elif [ $data_retention_months -gt 0 ]; then
        echo "❌ Data Retention: NON-COMPLIANT" >> "$data_protection_report"
    else
        echo "ℹ️ Data Retention: Not Required" >> "$data_protection_report"
    fi
    
    if $right_to_delete && $delete_compliant; then
        echo "✅ Right to Delete: COMPLIANT" >> "$data_protection_report"
    elif $right_to_delete; then
        echo "❌ Right to Delete: NON-COMPLIANT" >> "$data_protection_report"
    else
        echo "ℹ️ Right to Delete: Not Required" >> "$data_protection_report"
    fi
    
    if $data_portability && $portability_compliant; then
        echo "✅ Data Portability: COMPLIANT" >> "$data_protection_report"
    elif $data_portability; then
        echo "❌ Data Portability: NON-COMPLIANT" >> "$data_protection_report"
    else
        echo "ℹ️ Data Portability: Not Required" >> "$data_protection_report"
    fi
    echo "" >> "$data_protection_report"
    
    # Overall compliance status
    echo "Overall Data Protection Compliance:" >> "$data_protection_report"
    echo "-----------------------------------" >> "$data_protection_report"
    
    local overall_compliant=true
    if $encryption_required && ! $encryption_compliant; then
        overall_compliant=false
    fi
    if [ $data_retention_months -gt 0 ] && ! $retention_compliant; then
        overall_compliant=false
    fi
    if $right_to_delete && ! $delete_compliant; then
        overall_compliant=false
    fi
    if $data_portability && ! $portability_compliant; then
        overall_compliant=false
    fi
    
    if $overall_compliant; then
        echo "✅ OVERALL DATA PROTECTION COMPLIANT" >> "$data_protection_report"
    else
        echo "❌ OVERALL DATA PROTECTION NON-COMPLIANT" >> "$data_protection_report"
    fi
    echo "" >> "$data_protection_report"
    
    # Recommendations
    echo "Recommendations:" >> "$data_protection_report"
    echo "--------------" >> "$data_protection_report"
    
    if $overall_compliant; then
        echo "✅ Continue current data protection practices" >> "$data_protection_report"
        echo "✅ Schedule regular compliance reviews" >> "$data_protection_report"
        echo "✅ Monitor for regulatory changes" >> "$data_protection_report"
    else
        echo "❌ Address non-compliance issues immediately" >> "$data_protection_report"
        echo "❌ Implement missing data protection measures" >> "$data_protection_report"
        echo "❌ Review and update data protection policies" >> "$data_protection_report"
    fi
    echo "" >> "$data_protection_report"
    
    echo "✅ Data protection compliance check completed"
    echo "📋 Data protection report saved to: $data_protection_report"
    log_message "Data protection compliance check completed: $data_protection_report"
    
    # Display summary
    echo ""
    echo "Data Protection Compliance Summary:"
    echo "  Encryption Required: $encryption_required"
    echo "  Encryption Compliant: $encryption_compliant"
    echo "  Data Retention: ${data_retention_months} months"
    echo "  Retention Compliant: $retention_compliant"
    echo "  Right to Delete Required: $right_to_delete"
    echo "  Delete Compliant: $delete_compliant"
    echo "  Data Portability Required: $data_portability"
    echo "  Portability Compliant: $portability_compliant"
    if $overall_compliant; then
        echo "  Status: ✅ COMPLIANT"
    else
        echo "  Status: ❌ NON-COMPLIANT"
    fi
    echo "  Report: $data_protection_report"
}

# Function to check privacy compliance
check_privacy_compliance() {
    log_message "Checking privacy compliance"
    
    echo ""
    echo "Checking Privacy Compliance..."
    echo "============================="
    
    local privacy_report="$COMPLIANCE_REPORT_DIR/privacy_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create privacy report header
    echo "Atlas Production Privacy Compliance Check" > "$privacy_report"
    echo "Generated: $(date)" >> "$privacy_report"
    echo "=========================================" >> "$privacy_report"
    echo "" >> "$privacy_report"
    
    # Get privacy requirements
    local privacy_policy_required=$(jq -r '.privacy.privacy_policy_required' "$COMPLIANCE_CONFIG")
    local cookie_consent_required=$(jq -r '.privacy.cookie_consent_required' "$COMPLIANCE_CONFIG")
    local data_processing_agreement=$(jq -r '.privacy.data_processing_agreement' "$COMPLIANCE_CONFIG")
    
    echo "Privacy Requirements:" >> "$privacy_report"
    echo "--------------------" >> "$privacy_report"
    echo "Privacy Policy Required: $privacy_policy_required" >> "$privacy_report"
    echo "Cookie Consent Required: $cookie_consent_required" >> "$privacy_report"
    echo "Data Processing Agreement: $data_processing_agreement" >> "$privacy_report"
    echo "" >> "$privacy_report"
    
    # Check privacy policy compliance
    echo "Privacy Policy Compliance:" >> "$privacy_report"
    echo "--------------------------" >> "$privacy_report"
    
    local privacy_policy_compliant=true
    
    # Check if privacy policy exists
    local privacy_policy_file="$POLICY_DIR/privacy_policy.md"
    if [ -f "$privacy_policy_file" ]; then
        echo "✅ Privacy policy document exists" >> "$privacy_report"
        
        # Check policy content
        local policy_size=$(wc -c < "$privacy_policy_file")
        if [ $policy_size -gt 1000 ]; then
            echo "✅ Privacy policy has sufficient content" >> "$privacy_report"
        else
            echo "❌ Privacy policy content appears insufficient" >> "$privacy_report"
            privacy_policy_compliant=false
        fi
        
        # Check policy last update
        local policy_modified=$(stat -c %Y "$privacy_policy_file")
        local policy_age_days=$(( ($(date +%s) - policy_modified) / 86400 ))
        if [ $policy_age_days -lt 365 ]; then
            echo "✅ Privacy policy was updated within the last year" >> "$privacy_report"
        else
            echo "❌ Privacy policy has not been updated in over a year" >> "$privacy_report"
            privacy_policy_compliant=false
        fi
    else
        echo "❌ Privacy policy document not found" >> "$privacy_report"
        echo "   Expected location: $privacy_policy_file" >> "$privacy_report"
        privacy_policy_compliant=false
    fi
    echo "" >> "$privacy_report"
    
    # Check cookie consent compliance
    echo "Cookie Consent Compliance:" >> "$privacy_report"
    echo "--------------------------" >> "$privacy_report"
    
    local cookie_consent_compliant=true
    
    # Check if cookie consent mechanism exists
    local cookie_consent_script="/home/ubuntu/dev/atlas/web/cookie_consent.js"
    if [ -f "$cookie_consent_script" ]; then
        echo "✅ Cookie consent script exists" >> "$privacy_report"
        
        # Check for essential cookie consent functionality
        if grep -q "consent\|cookie\|accept" "$cookie_consent_script"; then
            echo "✅ Cookie consent functionality detected" >> "$privacy_report"
        else
            echo "❌ Cookie consent functionality not properly implemented" >> "$privacy_report"
            cookie_consent_compliant=false
        fi
    else
        echo "❌ Cookie consent script not found" >> "$privacy_report"
        echo "   Expected location: $cookie_consent_script" >> "$privacy_report"
        cookie_consent_compliant=false
    fi
    
    # Check if cookie banner is displayed
    local web_template="/home/ubuntu/dev/atlas/web/templates/base.html"
    if [ -f "$web_template" ]; then
        if grep -q "cookie-consent\|privacy-banner\|cookie-banner" "$web_template"; then
            echo "✅ Cookie consent banner detected in web template" >> "$privacy_report"
        else
            echo "❌ Cookie consent banner not found in web template" >> "$privacy_report"
            cookie_consent_compliant=false
        fi
    else
        echo "❌ Web template not found" >> "$privacy_report"
        echo "   Expected location: $web_template" >> "$privacy_report"
        cookie_consent_compliant=false
    fi
    echo "" >> "$privacy_report"
    
    # Check data processing agreement compliance
    echo "Data Processing Agreement Compliance:" >> "$privacy_report"
    echo "-------------------------------------" >> "$privacy_report"
    
    local dpa_compliant=true
    
    # Check if DPA exists
    local dpa_file="$POLICY_DIR/data_processing_agreement.md"
    if [ -f "$dpa_file" ]; then
        echo "✅ Data Processing Agreement exists" >> "$privacy_report"
        
        # Check DPA content
        local dpa_size=$(wc -c < "$dpa_file")
        if [ $dpa_size -gt 5000 ]; then
            echo "✅ Data Processing Agreement has sufficient content" >> "$privacy_report"
        else
            echo "❌ Data Processing Agreement content appears insufficient" >> "$privacy_report"
            dpa_compliant=false
        fi
    else
        echo "❌ Data Processing Agreement not found" >> "$privacy_report"
        echo "   Expected location: $dpa_file" >> "$privacy_report"
        dpa_compliant=false
    fi
    echo "" >> "$privacy_report"
    
    # Check user data handling
    echo "User Data Handling:" >> "$privacy_report"
    echo "------------------" >> "$privacy_report"
    
    # Check if user data collection is documented
    local user_data_documented=false
    
    # Check application configuration
    local env_file="/home/ubuntu/dev/atlas/.env"
    if [ -f "$env_file" ]; then
        if grep -q "USER_DATA\|PERSONAL_DATA" "$env_file"; then
            echo "✅ User data collection parameters detected in environment" >> "$privacy_report"
            user_data_documented=true
        fi
    fi
    
    # Check if user data processing is logged
    local audit_log="/home/ubuntu/dev/atlas/logs/audit.log"
    if [ -f "$audit_log" ]; then
        echo "✅ Audit logging is implemented" >> "$privacy_report"
        user_data_documented=true
    else
        echo "❌ Audit logging not found" >> "$privacy_report"
    fi
    
    if ! $user_data_documented; then
        echo "ℹ️ No user data collection or processing detected" >> "$privacy_report"
    fi
    echo "" >> "$privacy_report"
    
    # Summary
    echo "Privacy Compliance Summary:" >> "$privacy_report"
    echo "--------------------------" >> "$privacy_report"
    
    if $privacy_policy_required && $privacy_policy_compliant; then
        echo "✅ Privacy Policy: COMPLIANT" >> "$privacy_report"
    elif $privacy_policy_required; then
        echo "❌ Privacy Policy: NON-COMPLIANT" >> "$privacy_report"
    else
        echo "ℹ️ Privacy Policy: Not Required" >> "$privacy_report"
    fi
    
    if $cookie_consent_required && $cookie_consent_compliant; then
        echo "✅ Cookie Consent: COMPLIANT" >> "$privacy_report"
    elif $cookie_consent_required; then
        echo "❌ Cookie Consent: NON-COMPLIANT" >> "$privacy_report"
    else
        echo "ℹ️ Cookie Consent: Not Required" >> "$privacy_report"
    fi
    
    if $data_processing_agreement && $dpa_compliant; then
        echo "✅ Data Processing Agreement: COMPLIANT" >> "$privacy_report"
    elif $data_processing_agreement; then
        echo "❌ Data Processing Agreement: NON-COMPLIANT" >> "$privacy_report"
    else
        echo "ℹ️ Data Processing Agreement: Not Required" >> "$privacy_report"
    fi
    echo "" >> "$privacy_report"
    
    # Overall privacy compliance status
    echo "Overall Privacy Compliance:" >> "$privacy_report"
    echo "--------------------------" >> "$privacy_report"
    
    local overall_privacy_compliant=true
    if $privacy_policy_required && ! $privacy_policy_compliant; then
        overall_privacy_compliant=false
    fi
    if $cookie_consent_required && ! $cookie_consent_compliant; then
        overall_privacy_compliant=false
    fi
    if $data_processing_agreement && ! $dpa_compliant; then
        overall_privacy_compliant=false
    fi
    
    if $overall_privacy_compliant; then
        echo "✅ OVERALL PRIVACY COMPLIANT" >> "$privacy_report"
    else
        echo "❌ OVERALL PRIVACY NON-COMPLIANT" >> "$privacy_report"
    fi
    echo "" >> "$privacy_report"
    
    # Recommendations
    echo "Recommendations:" >> "$privacy_report"
    echo "--------------" >> "$privacy_report"
    
    if $overall_privacy_compliant; then
        echo "✅ Continue current privacy compliance practices" >> "$privacy_report"
        echo "✅ Review privacy policies annually" >> "$privacy_report"
        echo "✅ Stay updated on privacy regulations" >> "$privacy_report"
    else
        echo "❌ Address privacy compliance gaps immediately" >> "$privacy_report"
        if $privacy_policy_required && ! $privacy_policy_compliant; then
            echo "   - Update and publish privacy policy" >> "$privacy_report"
        fi
        if $cookie_consent_required && ! $cookie_consent_compliant; then
            echo "   - Implement cookie consent mechanism" >> "$privacy_report"
        fi
        if $data_processing_agreement && ! $dpa_compliant; then
            echo "   - Create and implement Data Processing Agreement" >> "$privacy_report"
        fi
        echo "✅ Schedule regular privacy compliance reviews" >> "$privacy_report"
    fi
    echo "" >> "$privacy_report"
    
    echo "✅ Privacy compliance check completed"
    echo "📋 Privacy report saved to: $privacy_report"
    log_message "Privacy compliance check completed: $privacy_report"
    
    # Display summary
    echo ""
    echo "Privacy Compliance Summary:"
    echo "  Privacy Policy Required: $privacy_policy_required"
    echo "  Privacy Policy Compliant: $privacy_policy_compliant"
    echo "  Cookie Consent Required: $cookie_consent_required"
    echo "  Cookie Consent Compliant: $cookie_consent_compliant"
    echo "  Data Processing Agreement Required: $data_processing_agreement"
    echo "  DPA Compliant: $dpa_compliant"
    if $overall_privacy_compliant; then
        echo "  Status: ✅ COMPLIANT"
    else
        echo "  Status: ❌ NON-COMPLIANT"
    fi
    echo "  Report: $privacy_report"
}

# Function to check security compliance
check_security_compliance() {
    log_message "Checking security compliance"
    
    echo ""
    echo "Checking Security Compliance..."
    echo "=============================="
    
    local security_report="$COMPLIANCE_REPORT_DIR/security_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create security report header
    echo "Atlas Production Security Compliance Check" > "$security_report"
    echo "Generated: $(date)" >> "$security_report"
    echo "=========================================" >> "$security_report"
    echo "" >> "$security_report"
    
    # Get security requirements
    local access_control_required=$(jq -r '.security.access_control_required' "$COMPLIANCE_CONFIG")
    local audit_logging_required=$(jq -r '.security.audit_logging_required' "$COMPLIANCE_CONFIG")
    local incident_response_required=$(jq -r '.security.incident_response_required' "$COMPLIANCE_CONFIG")
    
    echo "Security Requirements:" >> "$security_report"
    echo "--------------------" >> "$security_report"
    echo "Access Control Required: $access_control_required" >> "$security_report"
    echo "Audit Logging Required: $audit_logging_required" >> "$security_report"
    echo "Incident Response Required: $incident_response_required" >> "$security_report"
    echo "" >> "$security_report"
    
    # Check access control compliance
    echo "Access Control Compliance:" >> "$security_report"
    echo "--------------------------" >> "$security_report"
    
    local access_control_compliant=true
    
    # Check if authentication is implemented
    local nginx_config="/etc/nginx/sites-available/atlas"
    if [ -f "$nginx_config" ]; then
        if grep -q "auth_basic" "$nginx_config"; then
            echo "✅ Basic authentication is implemented for web interface" >> "$security_report"
        else
            echo "❌ Basic authentication not found in Nginx configuration" >> "$security_report"
            access_control_compliant=false
        fi
    else
        echo "❌ Nginx configuration not found" >> "$security_report"
        access_control_compliant=false
    fi
    
    # Check SSH access control
    if [ -f "/etc/ssh/sshd_config" ]; then
        # Check if password authentication is disabled
        if grep -q "^PasswordAuthentication no" "/etc/ssh/sshd_config"; then
            echo "✅ SSH password authentication is disabled" >> "$security_report"
        else
            echo "❌ SSH password authentication is enabled" >> "$security_report"
            access_control_compliant=false
        fi
        
        # Check if root login is disabled
        if grep -q "^PermitRootLogin no" "/etc/ssh/sshd_config"; then
            echo "✅ SSH root login is disabled" >> "$security_report"
        else
            echo "❌ SSH root login is enabled" >> "$security_report"
            access_control_compliant=false
        fi
    else
        echo "❌ SSH configuration file not found" >> "$security_report"
        access_control_compliant=false
    fi
    
    # Check database access control
    if systemctl is-active --quiet postgresql; then
        # Check if database has proper user permissions
        if sudo -u postgres psql -tAc "SELECT rolname FROM pg_roles WHERE rolname = 'atlas_user';" 2>/dev/null | grep -q "atlas_user"; then
            echo "✅ Database user 'atlas_user' exists" >> "$security_report"
        else
            echo "❌ Database user 'atlas_user' does not exist" >> "$security_report"
            access_control_compliant=false
        fi
    else
        echo "❌ PostgreSQL is not running" >> "$security_report"
        access_control_compliant=false
    fi
    echo "" >> "$security_report"
    
    # Check audit logging compliance
    echo "Audit Logging Compliance:" >> "$security_report"
    echo "------------------------" >> "$security_report"
    
    local audit_logging_compliant=true
    
    # Check if audit logging is implemented
    local audit_log_dir="/home/ubuntu/dev/atlas/logs"
    if [ -d "$audit_log_dir" ]; then
        local audit_log_file="$audit_log_dir/audit.log"
        if [ -f "$audit_log_file" ]; then
            echo "✅ Audit logging is implemented" >> "$security_report"
            
            # Check if audit log is being populated
            local audit_entries=$(wc -l < "$audit_log_file")
            if [ $audit_entries -gt 0 ]; then
                echo "✅ Audit log contains entries" >> "$security_report"
            else
                echo "❌ Audit log is empty" >> "$security_report"
                audit_logging_compliant=false
            fi
        else
            echo "❌ Audit log file not found" >> "$security_report"
            audit_logging_compliant=false
        fi
    else
        echo "❌ Logs directory not found" >> "$security_report"
        audit_logging_compliant=false
    fi
    
    # Check system logging
    local syslog_file="/var/log/syslog"
    if [ -f "$syslog_file" ]; then
        echo "✅ System logging is available" >> "$security_report"
    else
        echo "❌ System logging not available" >> "$security_report"
        audit_logging_compliant=false
    fi
    echo "" >> "$security_report"
    
    # Check incident response compliance
    echo "Incident Response Compliance:" >> "$security_report"
    echo "----------------------------" >> "$security_report"
    
    local incident_response_compliant=true
    
    # Check if incident response procedures exist
    local incident_response_doc="$POLICY_DIR/incident_response.md"
    if [ -f "$incident_response_doc" ]; then
        echo "✅ Incident response procedures documented" >> "$security_report"
        
        # Check if document has sufficient content
        local ir_doc_size=$(wc -c < "$incident_response_doc")
        if [ $ir_doc_size -gt 1000 ]; then
            echo "✅ Incident response document has sufficient content" >> "$security_report"
        else
            echo "❌ Incident response document content appears insufficient" >> "$security_report"
            incident_response_compliant=false
        fi
    else
        echo "❌ Incident response procedures not documented" >> "$security_report"
        echo "   Expected location: $incident_response_doc" >> "$security_report"
        incident_response_compliant=false
    fi
    
    # Check if incident response team is defined
    local compliance_config="/home/ubuntu/dev/atlas/config/compliance.json"
    if [ -f "$compliance_config" ] && grep -q "incident_response_team" "$compliance_config"; then
        echo "✅ Incident response team is defined" >> "$security_report"
    else
        echo "❌ Incident response team not defined" >> "$security_report"
        incident_response_compliant=false
    fi
    echo "" >> "$security_report"
    
    # Check security monitoring
    echo "Security Monitoring:" >> "$security_report"
    echo "------------------" >> "$security_report"
    
    # Check if monitoring services are running
    local monitoring_services=(
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    local monitoring_running=0
    for service_info in "${monitoring_services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc is running" >> "$security_report"
            monitoring_running=$((monitoring_running + 1))
        else
            echo "❌ $service_desc is not running" >> "$security_report"
        fi
    done
    
    if [ $monitoring_running -eq ${#monitoring_services[@]} ]; then
        echo "✅ All monitoring services are running" >> "$security_report"
    else
        echo "❌ Some monitoring services are not running" >> "$security_report"
    fi
    echo "" >> "$security_report"
    
    # Check security updates
    echo "Security Updates:" >> "$security_report"
    echo "----------------" >> "$security_report"
    
    # Check if automatic security updates are configured
    if [ -f "/etc/apt/apt.conf.d/20auto-upgrades" ]; then
        if grep -q "Unattended-Upgrade.*1" "/etc/apt/apt.conf.d/20auto-upgrades"; then
            echo "✅ Automatic security updates are configured" >> "$security_report"
        else
            echo "❌ Automatic security updates are not configured" >> "$security_report"
        fi
    else
        echo "❌ Automatic update configuration not found" >> "$security_report"
    fi
    
    # Check for pending security updates
    local security_updates=$(apt list --upgradable 2>/dev/null | grep security | wc -l)
    if [ $security_updates -gt 0 ]; then
        echo "⚠️ $security_updates security updates are pending" >> "$security_report"
        echo "   Recommendation: Install pending security updates" >> "$security_report"
    else
        echo "✅ No pending security updates" >> "$security_report"
    fi
    echo "" >> "$security_report"
    
    # Summary
    echo "Security Compliance Summary:" >> "$security_report"
    echo "---------------------------" >> "$security_report"
    
    if $access_control_required && $access_control_compliant; then
        echo "✅ Access Control: COMPLIANT" >> "$security_report"
    elif $access_control_required; then
        echo "❌ Access Control: NON-COMPLIANT" >> "$security_report"
    else
        echo "ℹ️ Access Control: Not Required" >> "$security_report"
    fi
    
    if $audit_logging_required && $audit_logging_compliant; then
        echo "✅ Audit Logging: COMPLIANT" >> "$security_report"
    elif $audit_logging_required; then
        echo "❌ Audit Logging: NON-COMPLIANT" >> "$security_report"
    else
        echo "ℹ️ Audit Logging: Not Required" >> "$security_report"
    fi
    
    if $incident_response_required && $incident_response_compliant; then
        echo "✅ Incident Response: COMPLIANT" >> "$security_report"
    elif $incident_response_required; then
        echo "❌ Incident Response: NON-COMPLIANT" >> "$security_report"
    else
        echo "ℹ️ Incident Response: Not Required" >> "$security_report"
    fi
    
    if [ $monitoring_running -eq ${#monitoring_services[@]} ]; then
        echo "✅ Security Monitoring: OPERATIONAL" >> "$security_report"
    else
        echo "❌ Security Monitoring: PARTIALLY OPERATIONAL" >> "$security_report"
    fi
    echo "" >> "$security_report"
    
    # Overall security compliance status
    echo "Overall Security Compliance:" >> "$security_report"
    echo "----------------------------" >> "$security_report"
    
    local overall_security_compliant=true
    if $access_control_required && ! $access_control_compliant; then
        overall_security_compliant=false
    fi
    if $audit_logging_required && ! $audit_logging_compliant; then
        overall_security_compliant=false
    fi
    if $incident_response_required && ! $incident_response_compliant; then
        overall_security_compliant=false
    fi
    
    if $overall_security_compliant; then
        echo "✅ OVERALL SECURITY COMPLIANT" >> "$security_report"
    else
        echo "❌ OVERALL SECURITY NON-COMPLIANT" >> "$security_report"
    fi
    echo "" >> "$security_report"
    
    # Recommendations
    echo "Recommendations:" >> "$security_report"
    echo "--------------" >> "$security_report"
    
    if $overall_security_compliant; then
        echo "✅ Continue current security compliance practices" >> "$security_report"
        echo "✅ Schedule regular security assessments" >> "$security_report"
        echo "✅ Monitor for security vulnerabilities" >> "$security_report"
    else
        echo "❌ Address security compliance gaps immediately" >> "$security_report"
        if $access_control_required && ! $access_control_compliant; then
            echo "   - Implement proper access controls" >> "$security_report"
        fi
        if $audit_logging_required && ! $audit_logging_compliant; then
            echo "   - Implement audit logging" >> "$security_report"
        fi
        if $incident_response_required && ! $incident_response_compliant; then
            echo "   - Document incident response procedures" >> "$security_report"
        fi
        if [ $monitoring_running -lt ${#monitoring_services[@]} ]; then
            echo "   - Ensure all monitoring services are running" >> "$security_report"
        fi
        echo "✅ Schedule regular security compliance reviews" >> "$security_report"
    fi
    echo "" >> "$security_report"
    
    echo "✅ Security compliance check completed"
    echo "📋 Security report saved to: $security_report"
    log_message "Security compliance check completed: $security_report"
    
    # Display summary
    echo ""
    echo "Security Compliance Summary:"
    echo "  Access Control Required: $access_control_required"
    echo "  Access Control Compliant: $access_control_compliant"
    echo "  Audit Logging Required: $audit_logging_required"
    echo "  Audit Logging Compliant: $audit_logging_compliant"
    echo "  Incident Response Required: $incident_response_required"
    echo "  Incident Response Compliant: $incident_response_compliant"
    echo "  Monitoring Services Running: $monitoring_running/${#monitoring_services[@]}"
    if $overall_security_compliant; then
        echo "  Status: ✅ COMPLIANT"
    else
        echo "  Status: ❌ NON-COMPLIANT"
    fi
    echo "  Report: $security_report"
}

# Function to generate compliance report
generate_compliance_report() {
    log_message "Generating compliance report"
    
    echo ""
    echo "Generating Compliance Report..."
    echo "=============================="
    
    local compliance_report="$COMPLIANCE_REPORT_DIR/compliance_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create compliance report header
    echo "Atlas Production Compliance Report" > "$compliance_report"
    echo "Generated: $(date)" >> "$compliance_report"
    echo "=================================" >> "$compliance_report"
    echo "" >> "$compliance_report"
    
    # Add system information
    echo "System Information:" >> "$compliance_report"
    echo "------------------" >> "$compliance_report"
    echo "Hostname: $(hostname)" >> "$compliance_report"
    echo "OS: $(lsb_release -d | cut -f2)" >> "$compliance_report"
    echo "Kernel: $(uname -r)" >> "$compliance_report"
    echo "Uptime: $(uptime -p)" >> "$compliance_report"
    echo "" >> "$compliance_report"
    
    # Add compliance requirements
    echo "Compliance Requirements:" >> "$compliance_report"
    echo "-----------------------" >> "$compliance_report"
    
    # Get regulations
    local regulations=$(jq -r '.compliance.regulations[]' "$COMPLIANCE_CONFIG")
    echo "Regulations:" >> "$compliance_report"
    while IFS= read -r regulation; do
        echo "  - $(echo $regulation | tr '[:lower:]' '[:upper:]')" >> "$compliance_report"
    done <<< "$regulations"
    
    # Get standards
    local standards=$(jq -r '.compliance.standards[]' "$COMPLIANCE_CONFIG")
    echo "Standards:" >> "$compliance_report"
    while IFS= read -r standard; do
        echo "  - $(echo $standard | tr '[:lower:]' '[:upper:]')" >> "$compliance_report"
    done <<< "$standards"
    
    # Get jurisdictions
    local jurisdictions=$(jq -r '.compliance.jurisdictions[]' "$COMPLIANCE_CONFIG")
    echo "Jurisdictions:" >> "$compliance_report"
    while IFS= read -r jurisdiction; do
        echo "  - $(echo $jurisdiction | tr '[:lower:]' '[:upper:]')" >> "$compliance_report"
    done <<< "$jurisdictions"
    echo "" >> "$compliance_report"
    
    # Add compliance status
    echo "Compliance Status:" >> "$compliance_report"
    echo "-----------------" >> "$compliance_report"
    
    # Get latest compliance check results
    local latest_data_protection_report=$(ls -t $COMPLIANCE_REPORT_DIR/data_protection_*.txt 2>/dev/null | head -1)
    local latest_privacy_report=$(ls -t $COMPLIANCE_REPORT_DIR/privacy_*.txt 2>/dev/null | head -1)
    local latest_security_report=$(ls -t $COMPLIANCE_REPORT_DIR/security_*.txt 2>/dev/null | head -1)
    
    # Extract data protection compliance status
    local data_protection_compliant="UNKNOWN"
    if [ ! -z "$latest_data_protection_report" ] && [ -f "$latest_data_protection_report" ]; then
        if grep -q "OVERALL DATA PROTECTION COMPLIANT" "$latest_data_protection_report"; then
            data_protection_compliant="COMPLIANT"
        elif grep -q "OVERALL DATA PROTECTION NON-COMPLIANT" "$latest_data_protection_report"; then
            data_protection_compliant="NON-COMPLIANT"
        fi
    fi
    
    # Extract privacy compliance status
    local privacy_compliant="UNKNOWN"
    if [ ! -z "$latest_privacy_report" ] && [ -f "$latest_privacy_report" ]; then
        if grep -q "OVERALL PRIVACY COMPLIANT" "$latest_privacy_report"; then
            privacy_compliant="COMPLIANT"
        elif grep -q "OVERALL PRIVACY NON-COMPLIANT" "$latest_privacy_report"; then
            privacy_compliant="NON-COMPLIANT"
        fi
    fi
    
    # Extract security compliance status
    local security_compliant="UNKNOWN"
    if [ ! -z "$latest_security_report" ] && [ -f "$latest_security_report" ]; then
        if grep -q "OVERALL SECURITY COMPLIANT" "$latest_security_report"; then
            security_compliant="COMPLIANT"
        elif grep -q "OVERALL SECURITY NON-COMPLIANT" "$latest_security_report"; then
            security_compliant="NON-COMPLIANT"
        fi
    fi
    
    echo "Data Protection: $data_protection_compliant" >> "$compliance_report"
    echo "Privacy: $privacy_compliant" >> "$compliance_report"
    echo "Security: $security_compliant" >> "$compliance_report"
    echo "" >> "$compliance_report"
    
    # Add policy compliance
    echo "Policy Compliance:" >> "$compliance_report"
    echo "----------------" >> "$compliance_report"
    
    # Check if required policies exist
    local policy_files=(
        "$POLICY_DIR/privacy_policy.md:Privacy Policy"
        "$POLICY_DIR/terms_of_service.md:Terms of Service"
        "$POLICY_DIR/data_processing_agreement.md:Data Processing Agreement"
        "$POLICY_DIR/incident_response.md:Incident Response Procedures"
        "$POLICY_DIR/security_policy.md:Security Policy"
    )
    
    local policies_compliant=0
    local total_policies=${#policy_files[@]}
    
    for policy_info in "${policy_files[@]}"; do
        local policy_file=$(echo $policy_info | cut -d':' -f1)
        local policy_name=$(echo $policy_info | cut -d':' -f2)
        
        if [ -f "$policy_file" ]; then
            local policy_size=$(wc -c < "$policy_file")
            if [ $policy_size -gt 1000 ]; then
                echo "✅ $policy_name: COMPLIANT" >> "$compliance_report"
                policies_compliant=$((policies_compliant + 1))
            else
                echo "❌ $policy_name: INSUFFICIENT CONTENT" >> "$compliance_report"
            fi
        else
            echo "❌ $policy_name: MISSING" >> "$compliance_report"
        fi
    done
    
    echo "Policy Compliance Rate: $policies_compliant/$total_policies" >> "$compliance_report"
    echo "" >> "$compliance_report"
    
    # Add technical compliance
    echo "Technical Compliance:" >> "$compliance_report"
    echo "-------------------" >> "$compliance_report"
    
    # Check encryption
    local encryption_status="UNKNOWN"
    if sudo -u postgres psql -tAc "SHOW ssl;" 2>/dev/null | grep -q "on"; then
        encryption_status="ENABLED"
    else
        encryption_status="DISABLED"
    fi
    echo "Database Encryption: $encryption_status" >> "$compliance_report"
    
    # Check backups
    local backup_status="UNKNOWN"
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        local backup_count=$(find "$backup_dir" -name "*.sql*" | wc -l)
        if [ $backup_count -gt 0 ]; then
            backup_status="ACTIVE"
        else
            backup_status="NO BACKUPS"
        fi
    else
        backup_status="BACKUP DIR MISSING"
    fi
    echo "Backups: $backup_status" >> "$compliance_report"
    
    # Check monitoring
    local monitoring_status="UNKNOWN"
    if systemctl is-active --quiet atlas-prometheus && systemctl is-active --quiet atlas-grafana; then
        monitoring_status="ACTIVE"
    elif systemctl is-active --quiet atlas-prometheus || systemctl is-active --quiet atlas-grafana; then
        monitoring_status="PARTIALLY ACTIVE"
    else
        monitoring_status="INACTIVE"
    fi
    echo "Monitoring: $monitoring_status" >> "$compliance_report"
    
    # Check access controls
    local access_control_status="UNKNOWN"
    if [ -f "/etc/nginx/sites-available/atlas" ] && grep -q "auth_basic" "/etc/nginx/sites-available/atlas"; then
        access_control_status="CONFIGURED"
    else
        access_control_status="NOT CONFIGURED"
    fi
    echo "Access Controls: $access_control_status" >> "$compliance_report"
    echo "" >> "$compliance_report"
    
    # Overall compliance status
    echo "Overall Compliance Status:" >> "$compliance_report"
    echo "-------------------------" >> "$compliance_report"
    
    local overall_compliant=true
    if [ "$data_protection_compliant" = "NON-COMPLIANT" ] || [ "$data_protection_compliant" = "UNKNOWN" ]; then
        overall_compliant=false
    fi
    if [ "$privacy_compliant" = "NON-COMPLIANT" ] || [ "$privacy_compliant" = "UNKNOWN" ]; then
        overall_compliant=false
    fi
    if [ "$security_compliant" = "NON-COMPLIANT" ] || [ "$security_compliant" = "UNKNOWN" ]; then
        overall_compliant=false
    fi
    
    if $overall_compliant; then
        echo "✅ OVERALL COMPLIANT" >> "$compliance_report"
    else
        echo "❌ OVERALL NON-COMPLIANT" >> "$compliance_report"
    fi
    echo "" >> "$compliance_report"
    
    # Recommendations
    echo "Recommendations:" >> "$compliance_report"
    echo "--------------" >> "$compliance_report"
    
    if $overall_compliant; then
        echo "✅ Continue current compliance practices" >> "$compliance_report"
        echo "✅ Schedule regular compliance assessments" >> "$compliance_report"
        echo "✅ Monitor for regulatory changes" >> "$compliance_report"
        echo "✅ Review policies annually" >> "$compliance_report"
    else
        echo "❌ Address compliance gaps immediately" >> "$compliance_report"
        if [ "$data_protection_compliant" = "NON-COMPLIANT" ] || [ "$data_protection_compliant" = "UNKNOWN" ]; then
            echo "   - Review data protection compliance" >> "$compliance_report"
        fi
        if [ "$privacy_compliant" = "NON-COMPLIANT" ] || [ "$privacy_compliant" = "UNKNOWN" ]; then
            echo "   - Review privacy compliance" >> "$compliance_report"
        fi
        if [ "$security_compliant" = "NON-COMPLIANT" ] || [ "$security_compliant" = "UNKNOWN" ]; then
            echo "   - Review security compliance" >> "$compliance_report"
        fi
        echo "✅ Implement missing policies" >> "$compliance_report"
        echo "✅ Enhance technical compliance measures" >> "$compliance_report"
    fi
    echo "" >> "$compliance_report"
    
    # Next review date
    echo "Next Compliance Review:" >> "$compliance_report"
    echo "----------------------" >> "$compliance_report"
    local next_review_date=$(date -d "+90 days" +"%Y-%m-%d")
    echo "Scheduled Review Date: $next_review_date" >> "$compliance_report"
    echo "Review Frequency: Quarterly" >> "$compliance_report"
    echo "" >> "$compliance_report"
    
    echo "✅ Compliance report generated"
    echo "📋 Compliance report saved to: $compliance_report"
    log_message "Compliance report generated: $compliance_report"
    
    # Display summary
    echo ""
    echo "Compliance Report Summary:"
    echo "  Regulations: $(echo "$regulations" | wc -l) loaded"
    echo "  Standards: $(echo "$standards" | wc -l) loaded"
    echo "  Jurisdictions: $(echo "$jurisdictions" | wc -l) loaded"
    echo "  Policies: $policies_compliant/$total_policies compliant"
    echo "  Data Protection: $data_protection_compliant"
    echo "  Privacy: $privacy_compliant"
    echo "  Security: $security_compliant"
    if $overall_compliant; then
        echo "  Status: ✅ COMPLIANT"
    else
        echo "  Status: ❌ NON-COMPLIANT"
    fi
    echo "  Report: $compliance_report"
}

# Function to create compliance policy
create_compliance_policy() {
    local policy_type=$1
    local policy_title=$2
    
    log_message "Creating compliance policy: $policy_type"
    
    echo ""
    echo "Creating Compliance Policy: $policy_type..."
    echo "=========================================="
    
    local policy_file="$POLICY_DIR/${policy_type}_$(date +%Y%m%d_%H%M%S).md"
    
    # Create policy header
    echo "# $policy_title" > "$policy_file"
    echo "" >> "$policy_file"
    echo "## Version" >> "$policy_file"
    echo "" >> "$policy_file"
    echo "Version 1.0" >> "$policy_file"
    echo "Effective Date: $(date +%Y-%m-%d)" >> "$policy_file"
    echo "Last Updated: $(date +%Y-%m-%d)" >> "$policy_file"
    echo "" >> "$policy_file"
    
    # Add policy content based on type
    case $policy_type in
        "privacy_policy")
            cat >> "$policy_file" << 'EOF'
## Purpose

This Privacy Policy describes how Atlas ("we", "us", or "our") collects, uses, and protects your personal information when you use our services.

## Information We Collect

### Personal Information
- Name
- Email address
- Account credentials
- Usage data
- Device information

### Automatically Collected Information
- IP addresses
- Browser type and version
- Operating system
- Pages visited
- Time and date of visits
- Referring website addresses

## How We Use Your Information

We use your information to:
- Provide and maintain our services
- Improve and personalize user experience
- Communicate with you
- Process transactions
- Send administrative information
- Comply with legal obligations
- Protect our rights and property

## Data Protection Rights

Depending on your location, you may have the following rights:
- Right to access your personal data
- Right to rectify inaccurate data
- Right to erase your data
- Right to restrict processing
- Right to data portability
- Right to object
- Right to withdraw consent

## Data Security

We implement appropriate technical and organizational measures to protect your personal data, including:
- Encryption of data in transit and at rest
- Access controls and authentication
- Regular security assessments
- Employee training on data protection

## Data Retention

We retain your personal data for as long as necessary to fulfill the purposes outlined in this policy, unless a longer retention period is required or permitted by law.

## International Data Transfers

Your information may be transferred to and maintained on computers located outside of your state, province, country or other governmental jurisdiction where the data protection laws may differ from those in your jurisdiction.

## Changes to This Policy

We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Last Updated" date.

## Contact Us

If you have any questions about this Privacy Policy, please contact us at:
- Email: privacy@khamel.com
- Address: Khamel.com, USA
EOF
            ;;
        "terms_of_service")
            cat >> "$policy_file" << 'EOF'
## Terms of Service

These Terms of Service ("Terms") govern your access to and use of the Atlas services, including our website, applications, and related services (collectively, the "Service").

## Acceptance of Terms

By accessing or using the Service, you agree to be bound by these Terms and all applicable laws and regulations. If you disagree with any part of the terms, then you may not access the Service.

## Use of Service

### Eligibility
You must be at least 13 years of age to use the Service. By agreeing to these Terms, you represent that you meet this requirement.

### Account Registration
To access certain features of the Service, you may be required to register for an account. You agree to provide accurate and complete information when creating your account and to update such information to keep it accurate and current.

### User Conduct
You agree not to:
- Violate any applicable laws or regulations
- Interfere with or disrupt the Service
- Attempt to gain unauthorized access to the Service
- Transmit any viruses or malicious code
- Engage in any activity that could damage our systems

## Intellectual Property

The Service and its original content, features, and functionality are and will remain the exclusive property of Atlas and its licensors. The Service is protected by copyright, trademark, and other laws of both the United States and foreign countries.

## Disclaimer of Warranties

THE SERVICE IS PROVIDED ON AN "AS IS" AND "AS AVAILABLE" BASIS. THE SERVICE IS PROVIDED WITHOUT WARRANTIES OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, OR COURSE OF PERFORMANCE.

## Limitation of Liability

IN NO EVENT SHALL ATLAS, NOR ITS DIRECTORS, EMPLOYEES, PARTNERS, AGENTS, SUPPLIERS, OR AFFILIATES, BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR PUNITIVE DAMAGES, INCLUDING WITHOUT LIMITATION, LOSS OF PROFITS, DATA, USE, GOODWILL, OR OTHER LOSSES, ARISING OUT OF OR IN CONNECTION WITH THE USE OF THE SERVICE.

## Governing Law

These Terms shall be governed and construed in accordance with the laws of the United States of America, without regard to its conflict of law provisions.

## Changes to Terms

We reserve the right, at our sole discretion, to modify or replace these Terms at any time. If a revision is material, we will provide at least 30 days' notice prior to any new terms taking effect.

## Contact Information

If you have any questions about these Terms, please contact us at:
- Email: legal@khamel.com
- Address: Khamel.com, USA
EOF
            ;;
        "data_processing_agreement")
            cat >> "$policy_file" << 'EOF'
## Data Processing Agreement

This Data Processing Agreement ("Agreement") supplements the Terms of Service and governs the processing of personal data by Atlas as a data processor on behalf of the data controller.

## Definitions

- "Data Controller": The entity that determines the purposes and means of the processing of personal data.
- "Data Processor": Atlas, which processes personal data on behalf of the data controller.
- "Personal Data": Any information relating to an identified or identifiable natural person.
- "Processing": Any operation performed on personal data.

## Scope of Processing

The data processor will process personal data only on documented instructions from the data controller, including with regard to transfers of personal data to a third country or an international organization.

## Processor Obligations

The data processor will:
- Process personal data only on documented instructions from the data controller
- Ensure that persons authorized to process the personal data have committed themselves to confidentiality
- Implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk
- Assist the data controller in ensuring compliance with data subject rights
- Assist the data controller in relation to data protection impact assessments
- Delete or return all personal data to the data controller after the end of the provision of services

## Sub-processing

The data processor may engage sub-processors only with the prior written consent of the data controller and remain fully liable to the data controller for the performance of the sub-processor's obligations.

## Security Measures

The data processor will implement appropriate technical and organizational measures including:
- Pseudonymisation and encryption of personal data
- Ongoing confidentiality, integrity, availability and resilience of processing systems and services
- Ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident
- Regular testing, assessment and evaluation of the effectiveness of technical and organizational measures

## Data Breach Notification

The data processor will notify the data controller without undue delay after becoming aware of a personal data breach.

## Duration

This Agreement applies from the effective date and continues until the data processing ceases.

## Governing Law

This Agreement shall be governed by and construed in accordance with the laws of the United States of America.

## Contact Information

For questions regarding this Agreement, please contact:
- Email: dpo@khamel.com
- Address: Khamel.com, USA
EOF
            ;;
        "incident_response")
            cat >> "$policy_file" << 'EOF'
## Incident Response Procedures

This document outlines the procedures for responding to security incidents and data breaches involving Atlas systems and data.

## Incident Classification

### Minor Incidents
- Low impact on systems or data
- No personal data compromised
- Minimal service disruption

### Major Incidents
- Significant impact on systems or data
- Potential personal data compromise
- Moderate service disruption

### Critical Incidents
- Severe impact on systems or data
- Confirmed personal data breach
- Major service disruption

## Incident Response Team

### Primary Team Members
- System Administrator
- Security Officer
- Legal Counsel
- Communications Lead

### Backup Team Members
- Development Lead
- Operations Manager

## Response Procedures

### 1. Incident Detection
- Monitor systems for unusual activity
- Review security logs and alerts
- Investigate potential incidents promptly

### 2. Incident Assessment
- Determine incident classification
- Assess impact on systems and data
- Identify affected systems and users

### 3. Containment
- Isolate affected systems
- Prevent further damage or data loss
- Preserve evidence for investigation

### 4. Eradication
- Remove threats and vulnerabilities
- Patch systems and applications
- Restore systems from clean backups

### 5. Recovery
- Restore services and data
- Verify system integrity
- Monitor for recurrence

### 6. Reporting
- Document incident details
- Notify affected parties if required
- Submit reports to management and authorities

### 7. Lessons Learned
- Conduct post-incident review
- Update procedures and policies
- Implement preventive measures

## Notification Requirements

### Internal Notification
- Notify incident response team within 1 hour
- Provide regular status updates
- Document all actions taken

### External Notification
- Data Protection Authority: Within 72 hours of becoming aware
- Affected Individuals: Without undue delay where high risk
- Regulatory Bodies: As required by applicable law

## Communication Plan

### Stakeholders
- Affected users
- Regulatory authorities
- Management team
- Media (if applicable)

### Communication Channels
- Email notifications
- Website announcements
- Press releases (if applicable)

## Record Keeping

All incident response activities must be documented including:
- Incident details and timeline
- Actions taken and by whom
- Resources used
- Cost of incident response
- Lessons learned and improvements

## Training and Awareness

Regular training must be provided to:
- Incident response team members
- System administrators
- All employees handling personal data

## Review and Updates

This procedure must be reviewed and updated:
- Annually
- After major incidents
- When regulatory requirements change
- When system architecture changes significantly

## Contact Information

For incident reporting, contact:
- 24/7 Security Hotline: +1-XXX-XXX-XXXX
- Email: security@khamel.com
- Alternative Contact: admin@khamel.com

Emergency Response:
- Outside Business Hours: +1-XXX-XXX-XXXX
- Critical Incidents: Immediately contact all team members
EOF
            ;;
        "security_policy")
            cat >> "$policy_file" << 'EOF'
## Security Policy

This Security Policy establishes the security requirements and procedures for protecting Atlas systems and data.

## Scope

This policy applies to all employees, contractors, consultants, temporaries, and other workers at Atlas who have access to company systems or data.

## Security Objectives

- Protect confidential and proprietary information
- Ensure system availability and reliability
- Comply with legal and regulatory requirements
- Minimize security risks and vulnerabilities
- Maintain business continuity

## Access Control

### User Access Management
- All users must be authenticated before accessing systems
- Access rights are granted based on job requirements
- Regular reviews of access rights must be conducted
- Access is revoked immediately upon termination

### Password Policy
- Minimum 12 characters with complexity requirements
- Regular password changes (every 90 days)
- Must not reuse previous 12 passwords
- Multi-factor authentication required for sensitive systems

### Physical Access Control
- Secure facilities with controlled access
- Visitor access logging and escorting
- Secure disposal of sensitive materials
- Asset inventory and tracking

## Data Protection

### Data Classification
- Public: Information that can be freely shared
- Internal: Information for internal use only
- Confidential: Sensitive information requiring protection
- Restricted: Highly sensitive information with strict access controls

### Data Handling
- Encrypt data in transit and at rest
- Apply appropriate access controls
- Implement data loss prevention measures
- Regular data backups and recovery testing

### Data Retention and Disposal
- Retain data according to legal requirements
- Securely dispose of data when no longer needed
- Document data disposal activities
- Verify complete data destruction

## System Security

### Network Security
- Firewalls and intrusion detection systems
- Regular vulnerability scanning
- Network segmentation
- Secure configuration of network devices

### Endpoint Security
- Antivirus and anti-malware protection
- Regular security updates and patches
- Device encryption
- Remote wipe capability for lost/stolen devices

### Application Security
- Secure coding practices
- Regular security testing
- Input validation and sanitization
- Error handling without information disclosure

## Incident Management

### Incident Response
- Established incident response procedures
- Trained incident response team
- Incident reporting and escalation procedures
- Post-incident analysis and improvement

### Business Continuity
- Disaster recovery plans
- Regular backup and restoration testing
- Business impact analysis
- Continuity testing and exercises

## Compliance and Monitoring

### Security Audits
- Regular internal security audits
- External security assessments
- Compliance monitoring
- Penetration testing

### Monitoring and Logging
- Comprehensive logging of system activities
- Regular log review and analysis
- Real-time security monitoring
- Alerting and notification procedures

## Training and Awareness

### Security Education
- Regular security awareness training
- Role-specific security training
- Phishing awareness programs
- Incident response training

### Policy Communication
- Clear communication of security policies
- Regular policy updates and reviews
- Acknowledgment of policy understanding
- Disciplinary actions for policy violations

## Enforcement

Violations of this Security Policy may result in disciplinary action, up to and including termination of employment or contract, and may also result in criminal prosecution.

## Review and Updates

This Security Policy will be reviewed annually and updated as necessary to reflect changes in technology, business requirements, and regulatory requirements.

## Contact Information

For questions regarding this Security Policy, please contact:
- Security Officer: security@khamel.com
- Management: admin@khamel.com
EOF
            ;;
        *)
            echo "## $policy_title" >> "$policy_file"
            echo "" >> "$policy_file"
            echo "This is a sample policy document for $policy_type." >> "$policy_file"
            echo "" >> "$policy_file"
            echo "Please customize this policy to meet your specific requirements." >> "$policy_file"
            echo "" >> "$policy_file"
            echo "Last Updated: $(date +%Y-%m-%d)" >> "$policy_file"
            ;;
    esac
    
    echo "✅ Compliance policy created: $policy_file"
    echo "📝 Policy Type: $policy_type"
    echo "📝 Policy Title: $policy_title"
    log_message "Compliance policy created: $policy_file"
    
    # Display summary
    echo ""
    echo "Policy Creation Summary:"
    echo "  Policy Type: $policy_type"
    echo "  Policy Title: $policy_title"
    echo "  File Created: $policy_file"
    echo "  Size: $(wc -c < "$policy_file") bytes"
}

# Function to clean old compliance reports
clean_old_reports() {
    log_message "Cleaning old compliance reports"
    
    echo ""
    echo "Cleaning Old Compliance Reports..."
    echo "=================================="
    
    # Remove compliance reports older than 365 days
    find "$COMPLIANCE_REPORT_DIR" -name "data_protection_*.txt" -mtime +365 -delete 2>/dev/null || true
    find "$COMPLIANCE_REPORT_DIR" -name "privacy_*.txt" -mtime +365 -delete 2>/dev/null || true
    find "$COMPLIANCE_REPORT_DIR" -name "security_*.txt" -mtime +365 -delete 2>/dev/null || true
    find "$COMPLIANCE_REPORT_DIR" -name "compliance_report_*.txt" -mtime +365 -delete 2>/dev/null || true
    
    # Remove old policy documents (but keep current versions)
    find "$POLICY_DIR" -name "*_*.md" -mtime +365 -delete 2>/dev/null || true
    
    echo "✅ Old compliance reports cleaned"
    log_message "Old compliance reports cleaned"
}

# Main legal compliance function
main() {
    log_message "=== Starting Atlas Legal Compliance ==="
    
    # Initialize configuration
    initialize_compliance_config
    
    # Start time
    local start_time=$(date)
    log_message "Legal compliance started at: $start_time"
    
    # Handle different compliance operations
    case $1 in
        "data")
            check_data_protection_compliance
            ;;
        "privacy")
            check_privacy_compliance
            ;;
        "security")
            check_security_compliance
            ;;
        "report")
            generate_compliance_report
            ;;
        "policy")
            if [ $# -lt 3 ]; then
                echo "❌ Usage: $0 policy <policy_type> <policy_title>"
                echo "Available policy types: privacy_policy, terms_of_service, data_processing_agreement, incident_response, security_policy"
                return 1
            fi
            create_compliance_policy "$2" "$3"
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive compliance check
            check_data_protection_compliance
            check_privacy_compliance
            check_security_compliance
            generate_compliance_report
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Legal compliance completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Legal Compliance Completed ==="
    
    echo ""
    echo "✅ Legal compliance operations completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $COMPLIANCE_REPORT_DIR"
    echo "📝 Log file: $COMPLIANCE_LOG"
}

# Run main function
main "$@"