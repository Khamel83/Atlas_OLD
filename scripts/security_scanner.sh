#!/bin/bash

# Atlas Production Security Scanner
# This script performs security scanning and vulnerability assessment of the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Security Scanner..."

# Configuration
SECURITY_LOG="/home/ubuntu/dev/atlas/logs/security_scan.log"
SECURITY_REPORT_DIR="/home/ubuntu/dev/atlas/security/reports"
SECURITY_TOOLS_DIR="/home/ubuntu/dev/atlas/security/tools"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $SECURITY_LOG)"
mkdir -p "$SECURITY_REPORT_DIR"
mkdir -p "$SECURITY_TOOLS_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $SECURITY_LOG
    echo "$1"
}

# Function to check for required security tools
check_security_tools() {
    log_message "Checking for required security tools"
    
    echo "Checking Security Tools..."
    echo "========================"
    
    local missing_tools=()
    
    # Check for nmap
    if ! command -v nmap &> /dev/null; then
        missing_tools+=("nmap")
    fi
    
    # Check for nikto
    if ! command -v nikto &> /dev/null; then
        missing_tools+=("nikto")
    fi
    
    # Check for lynis
    if ! command -v lynis &> /dev/null; then
        missing_tools+=("lynis")
    fi
    
    # Check for clamav
    if ! command -v clamscan &> /dev/null; then
        missing_tools+=("clamav")
    fi
    
    # Report missing tools
    if [ ${#missing_tools[@]} -gt 0 ]; then
        echo "⚠️ Missing security tools: ${missing_tools[*]}"
        echo "🔧 Install with: sudo apt install ${missing_tools[*]}"
        log_message "Missing security tools: ${missing_tools[*]}"
    else
        echo "✅ All required security tools are installed"
        log_message "All required security tools are installed"
    fi
}

# Function to scan open ports
scan_open_ports() {
    log_message "Scanning open ports"
    
    echo ""
    echo "Scanning Open Ports..."
    echo "===================="
    
    local port_scan_report="$SECURITY_REPORT_DIR/port_scan_$(date +%Y%m%d_%H%M%S).txt"
    
    # Perform port scan
    if command -v nmap &> /dev/null; then
        echo "🔍 Scanning localhost ports..."
        sudo nmap -sT -p- localhost > "$port_scan_report" 2>/dev/null || true
        
        # Extract open ports
        local open_ports=$(grep "open" "$port_scan_report" | awk '{print $1}')
        if [ ! -z "$open_ports" ]; then
            echo "🔓 Open ports found:"
            echo "$open_ports"
        else
            echo "✅ No unexpected open ports found"
        fi
        
        echo "📋 Port scan report saved to: $port_scan_report"
        log_message "Port scan completed: $port_scan_report"
    else
        echo "❌ nmap not installed, skipping port scan"
        log_message "nmap not installed, skipping port scan"
    fi
}

# Function to scan web application vulnerabilities
scan_web_vulnerabilities() {
    log_message "Scanning web application vulnerabilities"
    
    echo ""
    echo "Scanning Web Application Vulnerabilities..."
    echo "========================================"
    
    local web_scan_report="$SECURITY_REPORT_DIR/web_scan_$(date +%Y%m%d_%H%M%S).txt"
    
    # Check if web server is running
    if ! curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        echo "❌ Web application not accessible, skipping web scan"
        log_message "Web application not accessible, skipping web scan"
        return 1
    fi
    
    # Perform web vulnerability scan
    if command -v nikto &> /dev/null; then
        echo "🔍 Scanning web application for vulnerabilities..."
        nikto -h http://localhost:5000 -o "$web_scan_report" > /dev/null 2>&1 || true
        
        # Check for critical vulnerabilities
        local critical_vulns=$(grep "CRITICAL" "$web_scan_report" 2>/dev/null | wc -l)
        if [ $critical_vulns -gt 0 ]; then
            echo "🚨 Critical vulnerabilities found: $critical_vulns"
        else
            echo "✅ No critical web vulnerabilities found"
        fi
        
        echo "📋 Web vulnerability report saved to: $web_scan_report"
        log_message "Web vulnerability scan completed: $web_scan_report"
    else
        echo "❌ nikto not installed, skipping web vulnerability scan"
        log_message "nikto not installed, skipping web vulnerability scan"
    fi
}

# Function to perform system security audit
audit_system_security() {
    log_message "Performing system security audit"
    
    echo ""
    echo "Performing System Security Audit..."
    echo "================================"
    
    local system_audit_report="$SECURITY_REPORT_DIR/system_audit_$(date +%Y%m%d_%H%M%S).txt"
    
    # Perform system audit with lynis
    if command -v lynis &> /dev/null; then
        echo "🔍 Performing system security audit..."
        sudo lynis audit system --quick > "$system_audit_report" 2>/dev/null || true
        
        # Extract warnings and suggestions
        local warnings=$(grep "Warning" "$system_audit_report" 2>/dev/null | wc -l)
        local suggestions=$(grep "Suggestion" "$system_audit_report" 2>/dev/null | wc -l)
        
        echo "⚠️ System audit warnings: $warnings"
        echo "💡 System audit suggestions: $suggestions"
        
        echo "📋 System audit report saved to: $system_audit_report"
        log_message "System audit completed: $system_audit_report"
    else
        echo "❌ lynis not installed, skipping system audit"
        log_message "lynis not installed, skipping system audit"
    fi
}

# Function to scan for malware
scan_for_malware() {
    log_message "Scanning for malware"
    
    echo ""
    echo "Scanning for Malware..."
    echo "===================="
    
    local malware_scan_report="$SECURITY_REPORT_DIR/malware_scan_$(date +%Y%m%d_%H%M%S).txt"
    
    # Perform malware scan with ClamAV
    if command -v clamscan &> /dev/null; then
        echo "🔍 Scanning system for malware..."
        clamscan -r /home/ubuntu/dev/atlas > "$malware_scan_report" 2>/dev/null || true
        
        # Check for infected files
        local infected_files=$(grep "Infected files:" "$malware_scan_report" 2>/dev/null | awk '{print $3}')
        if [ "$infected_files" != "0" ] && [ ! -z "$infected_files" ]; then
            echo "🚨 Malware detected in $infected_files files"
            log_message "MALWARE DETECTED: $infected_files files infected"
        else
            echo "✅ No malware detected"
        fi
        
        echo "📋 Malware scan report saved to: $malware_scan_report"
        log_message "Malware scan completed: $malware_scan_report"
    else
        echo "❌ clamav not installed, skipping malware scan"
        log_message "clamav not installed, skipping malware scan"
    fi
}

# Function to check file permissions
check_file_permissions() {
    log_message "Checking file permissions"
    
    echo ""
    echo "Checking File Permissions..."
    echo "========================="
    
    local permission_report="$SECURITY_REPORT_DIR/permission_check_$(date +%Y%m%d_%H%M%S).txt"
    
    # Check sensitive file permissions
    local sensitive_files=(
        "/home/ubuntu/dev/atlas/.env"
        "/etc/nginx/.htpasswd"
        "/home/ubuntu/dev/atlas/backups"
        "/etc/ssl/private"
    )
    
    echo "🔍 Checking permissions for sensitive files..." > "$permission_report"
    
    local issues_found=0
    for file in "${sensitive_files[@]}"; do
        if [ -e "$file" ]; then
            local permissions=$(stat -c "%a" "$file" 2>/dev/null || echo "N/A")
            echo "$file: $permissions" >> "$permission_report"
            
            # Check if permissions are too permissive
            if [ "$permissions" = "777" ] || [ "$permissions" = "666" ]; then
                echo "⚠️ Overly permissive permissions for $file: $permissions" >> "$permission_report"
                issues_found=$((issues_found + 1))
            fi
        else
            echo "$file: Not found" >> "$permission_report"
        fi
    done
    
    if [ $issues_found -gt 0 ]; then
        echo "⚠️ File permission issues found: $issues_found"
    else
        echo "✅ All file permissions are secure"
    fi
    
    echo "📋 Permission check report saved to: $permission_report"
    log_message "File permission check completed: $permission_report"
}

# Function to check for security updates
check_security_updates() {
    log_message "Checking for security updates"
    
    echo ""
    echo "Checking for Security Updates..."
    echo "============================="
    
    local update_report="$SECURITY_REPORT_DIR/security_updates_$(date +%Y%m%d_%H%M%S).txt"
    
    # Update package list
    echo "🔄 Updating package list..." > "$update_report"
    sudo apt update > /dev/null 2>&1
    
    # Check for security updates
    echo "🔍 Checking for security updates..." >> "$update_report"
    local security_updates=$(apt list --upgradable 2>/dev/null | grep security | wc -l)
    
    if [ $security_updates -gt 0 ]; then
        echo "⚠️ Security updates available: $security_updates" >> "$update_report"
        echo "🔧 Run 'sudo unattended-upgrade' to install security updates"
        echo "⚠️ Security updates available: $security_updates"
        log_message "SECURITY UPDATES AVAILABLE: $security_updates"
    else
        echo "✅ No security updates available" >> "$update_report"
        echo "✅ No security updates available"
    fi
    
    echo "📋 Security update report saved to: $update_report"
    log_message "Security update check completed: $update_report"
}

# Function to generate security summary report
generate_security_summary() {
    log_message "Generating security summary report"
    
    echo ""
    echo "Generating Security Summary Report..."
    echo "=================================="
    
    local summary_report="$SECURITY_REPORT_DIR/security_summary_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create summary header
    echo "Atlas Production Security Summary Report" > "$summary_report"
    echo "Generated: $(date)" >> "$summary_report"
    echo "=====================================" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add system information
    echo "System Information:" >> "$summary_report"
    echo "------------------" >> "$summary_report"
    echo "Hostname: $(hostname)" >> "$summary_report"
    echo "OS: $(lsb_release -d | cut -f2)" >> "$summary_report"
    echo "Kernel: $(uname -r)" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add security scan results
    echo "Security Scan Results:" >> "$summary_report"
    echo "---------------------" >> "$summary_report"
    
    # Count recent security issues
    local port_scan_issues=$(ls -t $SECURITY_REPORT_DIR/port_scan_*.txt 2>/dev/null | head -1 | xargs grep -c "open" 2>/dev/null || echo "0")
    local web_vulns=$(ls -t $SECURITY_REPORT_DIR/web_scan_*.txt 2>/dev/null | head -1 | xargs grep -c "CRITICAL" 2>/dev/null || echo "0")
    local malware_issues=$(ls -t $SECURITY_REPORT_DIR/malware_scan_*.txt 2>/dev/null | head -1 | xargs grep -c "Infected files: [1-9]" 2>/dev/null || echo "0")
    local permission_issues=$(ls -t $SECURITY_REPORT_DIR/permission_check_*.txt 2>/dev/null | head -1 | xargs grep -c "Overly permissive" 2>/dev/null || echo "0")
    local security_updates=$(ls -t $SECURITY_REPORT_DIR/security_updates_*.txt 2>/dev/null | head -1 | xargs grep -c "Security updates available" 2>/dev/null || echo "0")
    
    echo "Open Ports Issues: $port_scan_issues" >> "$summary_report"
    echo "Web Vulnerabilities: $web_vulns" >> "$summary_report"
    echo "Malware Issues: $malware_issues" >> "$summary_report"
    echo "Permission Issues: $permission_issues" >> "$summary_report"
    echo "Security Updates: $security_updates" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add recommendations
    echo "Security Recommendations:" >> "$summary_report"
    echo "-----------------------" >> "$summary_report"
    if [ $security_updates -gt 0 ]; then
        echo "• Install available security updates" >> "$summary_report"
    fi
    if [ $permission_issues -gt 0 ]; then
        echo "• Review and fix file permissions" >> "$summary_report"
    fi
    if [ $web_vulns -gt 0 ]; then
        echo "• Address critical web vulnerabilities" >> "$summary_report"
    fi
    echo "• Run security scans regularly" >> "$summary_report"
    echo "• Monitor system logs for suspicious activity" >> "$summary_report"
    echo "• Keep security tools updated" >> "$summary_report"
    
    echo "✅ Security summary report generated: $summary_report"
    log_message "Security summary report generated: $summary_report"
    
    # Display summary
    echo ""
    echo "Security Summary:"
    echo "  Open Port Issues: $port_scan_issues"
    echo "  Web Vulnerabilities: $web_vulns"
    echo "  Malware Issues: $malware_issues"
    echo "  Permission Issues: $permission_issues"
    echo "  Security Updates: $security_updates"
    echo "Report saved to: $summary_report"
}

# Function to clean old security reports
clean_old_reports() {
    log_message "Cleaning old security reports"
    
    echo ""
    echo "Cleaning Old Security Reports..."
    echo "============================="
    
    # Remove security reports older than 30 days
    find "$SECURITY_REPORT_DIR" -name "port_scan_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$SECURITY_REPORT_DIR" -name "web_scan_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$SECURITY_REPORT_DIR" -name "system_audit_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$SECURITY_REPORT_DIR" -name "malware_scan_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$SECURITY_REPORT_DIR" -name "permission_check_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$SECURITY_REPORT_DIR" -name "security_updates_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$SECURITY_REPORT_DIR" -name "security_summary_*.txt" -mtime +30 -delete 2>/dev/null || true
    
    echo "✅ Old security reports cleaned"
    log_message "Old security reports cleaned"
}

# Main security scanner function
main() {
    log_message "=== Starting Atlas Security Scanner ==="
    
    # Start time
    local start_time=$(date)
    log_message "Security scan started at: $start_time"
    
    # Handle different security operations
    case $1 in
        "tools")
            check_security_tools
            ;;
        "ports")
            scan_open_ports
            ;;
        "web")
            scan_web_vulnerabilities
            ;;
        "system")
            audit_system_security
            ;;
        "malware")
            scan_for_malware
            ;;
        "permissions")
            check_file_permissions
            ;;
        "updates")
            check_security_updates
            ;;
        "summary")
            generate_security_summary
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive security scan
            check_security_tools
            scan_open_ports
            scan_web_vulnerabilities
            audit_system_security
            scan_for_malware
            check_file_permissions
            check_security_updates
            generate_security_summary
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Security scan completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Security Scanner Completed ==="
    
    echo ""
    echo "✅ Security scan complete!"
    echo "📋 Reports saved to: $SECURITY_REPORT_DIR"
    echo "📝 Log file: $SECURITY_LOG"
}

# Run main function
main "$@"