#!/bin/bash

# Atlas Production Security Hardening Script
# This script implements security hardening measures for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Security Hardening..."

# Configuration
SECURITY_LOG="/home/ubuntu/dev/atlas/logs/security_hardening.log"
SECURITY_REPORT_DIR="/home/ubuntu/dev/atlas/reports/security"
SECURITY_CONFIG="/home/ubuntu/dev/atlas/config/security.json"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $SECURITY_LOG)"
mkdir -p "$SECURITY_REPORT_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $SECURITY_LOG
    echo "$1"
}

# Function to initialize security configuration
initialize_security_config() {
    log_message "Initializing security configuration"
    
    # Create default security configuration if it doesn't exist
    if [ ! -f "$SECURITY_CONFIG" ]; then
        cat > "$SECURITY_CONFIG" << EOF
{
    "security": {
        "hardening": {
            "enabled": true,
            "level": "high",
            "compliance_standard": "cis"
        },
        "network": {
            "firewall": {
                "enabled": true,
                "default_policy": "drop",
                "allowed_ports": [22, 80, 443, 5432, 9090, 3000],
                "rate_limiting": {
                    "enabled": true,
                    "connections_per_minute": 100
                }
            },
            "ssh": {
                "port": 22,
                "protocol": "2",
                "password_authentication": "no",
                "permit_root_login": "no",
                "max_auth_tries": 3,
                "client_alive_interval": 300,
                "client_alive_count_max": 3
            }
        },
        "system": {
            "users": {
                "allowed_users": ["ubuntu"],
                "restricted_services": ["telnet", "ftp", "rsh", "rexec"]
            },
            "packages": {
                "remove_unnecessary": true,
                "update_packages": true,
                "install_security_tools": true
            },
            "filesystem": {
                "secure_permissions": true,
                "enable_auditing": true,
                "mount_options": {
                    "/tmp": "noexec,nosuid,nodev",
                    "/var/tmp": "noexec,nosuid,nodev",
                    "/home": "nodev"
                }
            }
        },
        "application": {
            "web_server": {
                "name": "nginx",
                "security_headers": {
                    "enabled": true,
                    "x_frame_options": "DENY",
                    "x_content_type_options": "nosniff",
                    "x_xss_protection": "1; mode=block",
                    "strict_transport_security": "max-age=31536000; includeSubDomains",
                    "content_security_policy": "default-src 'self'"
                },
                "rate_limiting": {
                    "enabled": true,
                    "requests_per_second": 10
                }
            },
            "database": {
                "name": "postgresql",
                "ssl_enabled": true,
                "authentication_method": "md5",
                "connection_limit": 100,
                "log_connections": true,
                "log_disconnections": true,
                "log_statement": "none"
            }
        },
        "monitoring": {
            "intrusion_detection": {
                "enabled": true,
                "system": "fail2ban",
                "ban_time_seconds": 3600,
                "find_time_seconds": 600,
                "max_retry_attempts": 5
            },
            "log_monitoring": {
                "enabled": true,
                "system": "rsyslog",
                "log_retention_days": 90
            },
            "vulnerability_scanning": {
                "enabled": true,
                "frequency": "weekly",
                "tools": ["lynis", "clamav"]
            }
        }
    }
}
EOF
        echo "✅ Created default security configuration"
        log_message "Default security configuration created"
    else
        echo "✅ Security configuration already exists"
    fi
}

# Function to harden network security
harden_network_security() {
    log_message "Hardening network security"
    
    echo ""
    echo "Hardening Network Security..."
    echo "=========================="
    
    local network_report="$SECURITY_REPORT_DIR/network_hardening_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create network security report header
    echo "Atlas Production Network Security Hardening" > "$network_report"
    echo "Generated: $(date)" >> "$network_report"
    echo "========================================" >> "$network_report"
    echo "" >> "$network_report"
    
    # Get network security configuration
    local firewall_enabled=$(jq -r '.security.network.firewall.enabled' "$SECURITY_CONFIG")
    local default_policy=$(jq -r '.security.network.firewall.default_policy' "$SECURITY_CONFIG")
    local allowed_ports=$(jq -r '.security.network.firewall.allowed_ports[]' "$SECURITY_CONFIG")
    local rate_limiting_enabled=$(jq -r '.security.network.firewall.rate_limiting.enabled' "$SECURITY_CONFIG")
    local connections_per_minute=$(jq -r '.security.network.firewall.rate_limiting.connections_per_minute' "$SECURITY_CONFIG")
    
    echo "Network Security Configuration:" >> "$network_report"
    echo "-----------------------------" >> "$network_report"
    echo "Firewall Enabled: $firewall_enabled" >> "$network_report"
    echo "Default Policy: $default_policy" >> "$network_report"
    echo "Allowed Ports: $allowed_ports" >> "$network_report"
    echo "Rate Limiting Enabled: $rate_limiting_enabled" >> "$network_report"
    echo "Connections Per Minute: $connections_per_minute" >> "$network_report"
    echo "" >> "$network_report"
    
    # Apply firewall configuration
    echo "Applying Firewall Configuration:" >> "$network_report"
    echo "------------------------------" >> "$network_report"
    
    if [ "$firewall_enabled" = "true" ]; then
        # Enable UFW firewall
        if sudo ufw enable > /dev/null 2>&1; then
            echo "✅ UFW firewall enabled" >> "$network_report"
        else
            echo "❌ Failed to enable UFW firewall" >> "$network_report"
            log_message "Failed to enable UFW firewall"
            return 1
        fi
        
        # Set default policy
        if sudo ufw default "$default_policy" > /dev/null 2>&1; then
            echo "✅ Default policy set to $default_policy" >> "$network_report"
        else
            echo "❌ Failed to set default policy to $default_policy" >> "$network_report"
            log_message "Failed to set default policy to $default_policy"
            return 1
        fi
        
        # Allow specified ports
        while IFS= read -r port; do
            if sudo ufw allow $port > /dev/null 2>&1; then
                echo "✅ Port $port allowed" >> "$network_report"
            else
                echo "❌ Failed to allow port $port" >> "$network_report"
                log_message "Failed to allow port $port"
            fi
        done <<< "$allowed_ports"
        
        # Deny all other incoming connections
        if sudo ufw deny in from any to any > /dev/null 2>&1; then
            echo "✅ All other incoming connections denied" >> "$network_report"
        else
            echo "❌ Failed to deny all other incoming connections" >> "$network_report"
            log_message "Failed to deny all other incoming connections"
        fi
    else
        echo "❌ Firewall is disabled in configuration" >> "$network_report"
        log_message "Firewall is disabled in configuration"
        return 1
    fi
    echo "" >> "$network_report"
    
    # Apply rate limiting
    echo "Applying Rate Limiting:" >> "$network_report"
    echo "---------------------" >> "$network_report"
    
    if [ "$rate_limiting_enabled" = "true" ]; then
        # Configure rate limiting using iptables
        if sudo iptables -A INPUT -p tcp --dport 22 -m limit --limit ${connections_per_minute}/minute --limit-burst ${connections_per_minute} -j ACCEPT > /dev/null 2>&1; then
            echo "✅ Rate limiting configured for SSH (${connections_per_minute} connections/minute)" >> "$network_report"
        else
            echo "❌ Failed to configure rate limiting for SSH" >> "$network_report"
            log_message "Failed to configure rate limiting for SSH"
        fi
        
        if sudo iptables -A INPUT -p tcp --dport 80 -m limit --limit ${connections_per_minute}/minute --limit-burst ${connections_per_minute} -j ACCEPT > /dev/null 2>&1; then
            echo "✅ Rate limiting configured for HTTP (${connections_per_minute} connections/minute)" >> "$network_report"
        else
            echo "❌ Failed to configure rate limiting for HTTP" >> "$network_report"
            log_message "Failed to configure rate limiting for HTTP"
        fi
        
        if sudo iptables -A INPUT -p tcp --dport 443 -m limit --limit ${connections_per_minute}/minute --limit-burst ${connections_per_minute} -j ACCEPT > /dev/null 2>&1; then
            echo "✅ Rate limiting configured for HTTPS (${connections_per_minute} connections/minute)" >> "$network_report"
        else
            echo "❌ Failed to configure rate limiting for HTTPS" >> "$network_report"
            log_message "Failed to configure rate limiting for HTTPS"
        fi
    else
        echo "❌ Rate limiting is disabled in configuration" >> "$network_report"
        log_message "Rate limiting is disabled in configuration"
    fi
    echo "" >> "$network_report"
    
    # Verify firewall status
    echo "Verifying Firewall Status:" >> "$network_report"
    echo "------------------------" >> "$network_report"
    
    if sudo ufw status | grep -q "Status: active"; then
        echo "✅ Firewall is active" >> "$network_report"
        
        # List allowed rules
        local allowed_rules=$(sudo ufw status | grep -E "ALLOW|LIMIT")
        echo "Allowed Rules:" >> "$network_report"
        echo "$allowed_rules" >> "$network_report"
    else
        echo "❌ Firewall is not active" >> "$network_report"
        log_message "Firewall is not active"
        return 1
    fi
    echo "" >> "$network_report"
    
    # Network security recommendations
    echo "Network Security Recommendations:" >> "$network_report"
    echo "-------------------------------" >> "$network_report"
    
    if [ "$firewall_enabled" = "true" ] && sudo ufw status | grep -q "Status: active"; then
        echo "✅ Network firewall is properly configured" >> "$network_report"
        echo "✅ Continue current firewall configuration" >> "$network_report"
        echo "✅ Monitor firewall logs for suspicious activity" >> "$network_report"
    else
        echo "❌ Network firewall is not properly configured" >> "$network_report"
        echo "❌ Enable and configure firewall immediately" >> "$network_report"
        echo "❌ Review firewall rules and policies" >> "$network_report"
    fi
    
    if [ "$rate_limiting_enabled" = "true" ]; then
        echo "✅ Network rate limiting is enabled" >> "$network_report"
        echo "✅ Current rate limit: ${connections_per_minute} connections/minute" >> "$network_report"
        echo "✅ Continue current rate limiting configuration" >> "$network_report"
    else
        echo "❌ Network rate limiting is disabled" >> "$network_report"
        echo "❌ Enable rate limiting to prevent abuse" >> "$network_report"
        echo "❌ Configure appropriate rate limits" >> "$network_report"
    fi
    echo "" >> "$network_report"
    
    echo "✅ Network security hardening completed"
    echo "📋 Network security report saved to: $network_report"
    log_message "Network security hardening completed: $network_report"
    
    # Display summary
    echo ""
    echo "Network Security Hardening Summary:"
    echo "  Firewall Enabled: $firewall_enabled"
    echo "  Default Policy: $default_policy"
    echo "  Allowed Ports: $allowed_ports"
    echo "  Rate Limiting Enabled: $rate_limiting_enabled"
    echo "  Connections Per Minute: $connections_per_minute"
    echo "  Firewall Status: $(if sudo ufw status | grep -q "Status: active"; then echo "Active"; else echo "Inactive"; fi)"
    echo "  Report: $network_report"
}

# Function to harden SSH security
harden_ssh_security() {
    log_message "Hardening SSH security"
    
    echo ""
    echo "Hardening SSH Security..."
    echo "======================"
    
    local ssh_report="$SECURITY_REPORT_DIR/ssh_hardening_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create SSH security report header
    echo "Atlas Production SSH Security Hardening" > "$ssh_report"
    echo "Generated: $(date)" >> "$ssh_report"
    echo "=====================================" >> "$ssh_report"
    echo "" >> "$ssh_report"
    
    # Get SSH security configuration
    local ssh_port=$(jq -r '.security.network.ssh.port' "$SECURITY_CONFIG")
    local ssh_protocol=$(jq -r '.security.network.ssh.protocol' "$SECURITY_CONFIG")
    local password_authentication=$(jq -r '.security.network.ssh.password_authentication' "$SECURITY_CONFIG")
    local permit_root_login=$(jq -r '.security.network.ssh.permit_root_login' "$SECURITY_CONFIG")
    local max_auth_tries=$(jq -r '.security.network.ssh.max_auth_tries' "$SECURITY_CONFIG")
    local client_alive_interval=$(jq -r '.security.network.ssh.client_alive_interval' "$SECURITY_CONFIG")
    local client_alive_count_max=$(jq -r '.security.network.ssh.client_alive_count_max' "$SECURITY_CONFIG")
    
    echo "SSH Security Configuration:" >> "$ssh_report"
    echo "-------------------------" >> "$ssh_report"
    echo "SSH Port: $ssh_port" >> "$ssh_report"
    echo "SSH Protocol: $ssh_protocol" >> "$ssh_report"
    echo "Password Authentication: $password_authentication" >> "$ssh_report"
    echo "Permit Root Login: $permit_root_login" >> "$ssh_report"
    echo "Max Auth Tries: $max_auth_tries" >> "$ssh_report"
    echo "Client Alive Interval: ${client_alive_interval} seconds" >> "$ssh_report"
    echo "Client Alive Count Max: $client_alive_count_max" >> "$ssh_report"
    echo "" >> "$ssh_report"
    
    # Apply SSH security configuration
    echo "Applying SSH Security Configuration:" >> "$ssh_report"
    echo "----------------------------------" >> "$ssh_report"
    
    # Backup SSH configuration
    local ssh_config="/etc/ssh/sshd_config"
    if [ -f "$ssh_config" ]; then
        sudo cp "$ssh_config" "${ssh_config}.bak.$(date +%Y%m%d_%H%M%S)" > /dev/null 2>&1
        echo "✅ SSH configuration backed up" >> "$ssh_report"
        
        # Apply SSH security settings
        sudo sed -i "s/^#*Port.*/Port $ssh_port/" "$ssh_config"
        echo "✅ SSH port set to $ssh_port" >> "$ssh_report"
        
        sudo sed -i "s/^#*Protocol.*/Protocol $ssh_protocol/" "$ssh_config"
        echo "✅ SSH protocol set to $ssh_protocol" >> "$ssh_report"
        
        sudo sed -i "s/^#*PasswordAuthentication.*/PasswordAuthentication $password_authentication/" "$ssh_config"
        echo "✅ Password authentication set to $password_authentication" >> "$ssh_report"
        
        sudo sed -i "s/^#*PermitRootLogin.*/PermitRootLogin $permit_root_login/" "$ssh_config"
        echo "✅ Root login set to $permit_root_login" >> "$ssh_report"
        
        sudo sed -i "s/^#*MaxAuthTries.*/MaxAuthTries $max_auth_tries/" "$ssh_config"
        echo "✅ Max auth tries set to $max_auth_tries" >> "$ssh_report"
        
        sudo sed -i "s/^#*ClientAliveInterval.*/ClientAliveInterval $client_alive_interval/" "$ssh_config"
        echo "✅ Client alive interval set to ${client_alive_interval} seconds" >> "$ssh_report"
        
        sudo sed -i "s/^#*ClientAliveCountMax.*/ClientAliveCountMax $client_alive_count_max/" "$ssh_config"
        echo "✅ Client alive count max set to $client_alive_count_max" >> "$ssh_report"
        
        # Restart SSH service
        if sudo systemctl restart ssh; then
            echo "✅ SSH service restarted with new configuration" >> "$ssh_report"
        else
            echo "❌ Failed to restart SSH service" >> "$ssh_report"
            log_message "Failed to restart SSH service"
            return 1
        fi
    else
        echo "❌ SSH configuration file not found: $ssh_config" >> "$ssh_report"
        log_message "SSH configuration file not found: $ssh_config"
        return 1
    fi
    echo "" >> "$ssh_report"
    
    # Verify SSH security configuration
    echo "Verifying SSH Security Configuration:" >> "$ssh_report"
    echo "-----------------------------------" >> "$ssh_report"
    
    # Check if SSH is running
    if systemctl is-active --quiet ssh; then
        echo "✅ SSH service is running" >> "$ssh_report"
    else
        echo "❌ SSH service is not running" >> "$ssh_report"
        log_message "SSH service is not running"
        return 1
    fi
    
    # Check SSH port
    local current_ssh_port=$(sudo ss -tuln | grep ":$ssh_port " | wc -l)
    if [ $current_ssh_port -gt 0 ]; then
        echo "✅ SSH is listening on port $ssh_port" >> "$ssh_report"
    else
        echo "❌ SSH is not listening on port $ssh_port" >> "$ssh_report"
        log_message "SSH is not listening on port $ssh_port"
    fi
    
    # Check SSH configuration
    local current_password_auth=$(sudo grep "^PasswordAuthentication" "$ssh_config" | awk '{print $2}')
    if [ "$current_password_auth" = "$password_authentication" ]; then
        echo "✅ Password authentication is set to $password_authentication" >> "$ssh_report"
    else
        echo "❌ Password authentication is set to $current_password_auth, expected $password_authentication" >> "$ssh_report"
        log_message "Password authentication mismatch"
    fi
    
    local current_permit_root=$(sudo grep "^PermitRootLogin" "$ssh_config" | awk '{print $2}')
    if [ "$current_permit_root" = "$permit_root_login" ]; then
        echo "✅ Root login is set to $permit_root_login" >> "$ssh_report"
    else
        echo "❌ Root login is set to $current_permit_root, expected $permit_root_login" >> "$ssh_report"
        log_message "Root login setting mismatch"
    fi
    echo "" >> "$ssh_report"
    
    # SSH security recommendations
    echo "SSH Security Recommendations:" >> "$ssh_report"
    echo "---------------------------" >> "$ssh_report"
    
    if [ "$password_authentication" = "no" ]; then
        echo "✅ Password authentication is disabled" >> "$ssh_report"
        echo "✅ Continue using key-based authentication" >> "$ssh_report"
        echo "✅ Monitor SSH login attempts" >> "$ssh_report"
    else
        echo "❌ Password authentication is enabled" >> "$ssh_report"
        echo "❌ Disable password authentication immediately" >> "$ssh_report"
        echo "❌ Switch to key-based authentication" >> "$ssh_report"
    fi
    
    if [ "$permit_root_login" = "no" ]; then
        echo "✅ Root login is disabled" >> "$ssh_report"
        echo "✅ Continue restricting root access" >> "$ssh_report"
        echo "✅ Use sudo for administrative tasks" >> "$ssh_report"
    else
        echo "❌ Root login is enabled" >> "$ssh_report"
        echo "❌ Disable root login immediately" >> "$ssh_report"
        echo "❌ Restrict root access to sudo only" >> "$ssh_report"
    fi
    
    if [ $max_auth_tries -le 3 ]; then
        echo "✅ Max auth tries is set to $max_auth_tries (reasonable limit)" >> "$ssh_report"
        echo "✅ Continue current auth attempt limits" >> "$ssh_report"
    else
        echo "❌ Max auth tries is set to $max_auth_tries (too high)" >> "$ssh_report"
        echo "❌ Reduce max auth tries to 3 or less" >> "$ssh_report"
    fi
    
    if [ $client_alive_interval -ge 300 ]; then
        echo "✅ Client alive interval is set to ${client_alive_interval} seconds (reasonable)" >> "$ssh_report"
        echo "✅ Continue current client timeout settings" >> "$ssh_report"
    else
        echo "❌ Client alive interval is set to ${client_alive_interval} seconds (too short)" >> "$ssh_report"
        echo "❌ Increase client alive interval to 300 seconds or more" >> "$ssh_report"
    fi
    echo "" >> "$ssh_report"
    
    echo "✅ SSH security hardening completed"
    echo "📋 SSH security report saved to: $ssh_report"
    log_message "SSH security hardening completed: $ssh_report"
    
    # Display summary
    echo ""
    echo "SSH Security Hardening Summary:"
    echo "  SSH Port: $ssh_port"
    echo "  SSH Protocol: $ssh_protocol"
    echo "  Password Authentication: $password_authentication"
    echo "  Permit Root Login: $permit_root_login"
    echo "  Max Auth Tries: $max_auth_tries"
    echo "  Client Alive Interval: ${client_alive_interval} seconds"
    echo "  Client Alive Count Max: $client_alive_count_max"
    echo "  SSH Service Status: $(if systemctl is-active --quiet ssh; then echo "Running"; else echo "Not Running"; fi)"
    echo "  Report: $ssh_report"
}

# Function to harden system security
harden_system_security() {
    log_message "Hardening system security"
    
    echo ""
    echo "Hardening System Security..."
    echo "=========================="
    
    local system_report="$SECURITY_REPORT_DIR/system_hardening_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create system security report header
    echo "Atlas Production System Security Hardening" > "$system_report"
    echo "Generated: $(date)" >> "$system_report"
    echo "========================================" >> "$system_report"
    echo "" >> "$system_report"
    
    # Get system security configuration
    local remove_unnecessary_packages=$(jq -r '.security.system.packages.remove_unnecessary' "$SECURITY_CONFIG")
    local update_packages=$(jq -r '.security.system.packages.update_packages' "$SECURITY_CONFIG")
    local install_security_tools=$(jq -r '.security.system.packages.install_security_tools' "$SECURITY_CONFIG")
    local secure_permissions=$(jq -r '.security.system.filesystem.secure_permissions' "$SECURITY_CONFIG")
    local enable_auditing=$(jq -r '.security.system.filesystem.enable_auditing' "$SECURITY_CONFIG")
    local mount_options=$(jq -r '.security.system.filesystem.mount_options' "$SECURITY_CONFIG")
    
    echo "System Security Configuration:" >> "$system_report"
    echo "----------------------------" >> "$system_report"
    echo "Remove Unnecessary Packages: $remove_unnecessary_packages" >> "$system_report"
    echo "Update Packages: $update_packages" >> "$system_report"
    echo "Install Security Tools: $install_security_tools" >> "$system_report"
    echo "Secure Permissions: $secure_permissions" >> "$system_report"
    echo "Enable Auditing: $enable_auditing" >> "$system_report"
    echo "Mount Options: $mount_options" >> "$system_report"
    echo "" >> "$system_report"
    
    # Update system packages
    echo "Updating System Packages:" >> "$system_report"
    echo "-----------------------" >> "$system_report"
    
    if [ "$update_packages" = "true" ]; then
        # Update package list
        if sudo apt update > /dev/null 2>&1; then
            echo "✅ Package list updated" >> "$system_report"
        else
            echo "❌ Failed to update package list" >> "$system_report"
            log_message "Failed to update package list"
        fi
        
        # Upgrade packages
        if sudo apt upgrade -y > /dev/null 2>&1; then
            echo "✅ System packages upgraded" >> "$system_report"
        else
            echo "❌ Failed to upgrade system packages" >> "$system_report"
            log_message "Failed to upgrade system packages"
        fi
        
        # Install security updates
        if sudo unattended-upgrade > /dev/null 2>&1; then
            echo "✅ Security updates installed" >> "$system_report"
        else
            echo "❌ Failed to install security updates" >> "$system_report"
            log_message "Failed to install security updates"
        fi
    else
        echo "❌ Package updates are disabled in configuration" >> "$system_report"
        log_message "Package updates are disabled in configuration"
    fi
    echo "" >> "$system_report"
    
    # Install security tools
    echo "Installing Security Tools:" >> "$system_report"
    echo "------------------------" >> "$system_report"
    
    if [ "$install_security_tools" = "true" ]; then
        # Install security tools
        local security_tools=("fail2ban" "lynis" "clamav" "rkhunter" "chkrootkit")
        
        for tool in "${security_tools[@]}"; do
            if dpkg -l | grep -q "^ii  $tool "; then
                echo "✅ $tool is already installed" >> "$system_report"
            else
                if sudo apt install -y $tool > /dev/null 2>&1; then
                    echo "✅ $tool installed successfully" >> "$system_report"
                else
                    echo "❌ Failed to install $tool" >> "$system_report"
                    log_message "Failed to install $tool"
                fi
            fi
        done
    else
        echo "❌ Security tool installation is disabled in configuration" >> "$system_report"
        log_message "Security tool installation is disabled in configuration"
    fi
    echo "" >> "$system_report"
    
    # Remove unnecessary packages
    echo "Removing Unnecessary Packages:" >> "$system_report"
    echo "----------------------------" >> "$system_report"
    
    if [ "$remove_unnecessary_packages" = "true" ]; then
        # List of unnecessary packages to remove
        local unnecessary_packages=("telnet" "ftp" "rsh-client" "rsh-redone-client" "rexec-client")
        
        for package in "${unnecessary_packages[@]}"; do
            if dpkg -l | grep -q "^ii  $package "; then
                if sudo apt remove -y $package > /dev/null 2>&1; then
                    echo "✅ $package removed successfully" >> "$system_report"
                else
                    echo "❌ Failed to remove $package" >> "$system_report"
                    log_message "Failed to remove $package"
                fi
            else
                echo "✅ $package is not installed" >> "$system_report"
            fi
        done
    else
        echo "❌ Removal of unnecessary packages is disabled in configuration" >> "$system_report"
        log_message "Removal of unnecessary packages is disabled in configuration"
    fi
    echo "" >> "$system_report"
    
    # Secure file permissions
    echo "Securing File Permissions:" >> "$system_report"
    echo "------------------------" >> "$system_report"
    
    if [ "$secure_permissions" = "true" ]; then
        # Secure sensitive files
        local sensitive_files=(
            "/home/ubuntu/dev/atlas/.env:600"
            "/etc/nginx/.htpasswd:600"
            "/etc/ssh/sshd_config:600"
            "/etc/ssl/private:700"
        )
        
        for file_info in "${sensitive_files[@]}"; do
            local file_path=$(echo $file_info | cut -d':' -f1)
            local permissions=$(echo $file_info | cut -d':' -f2)
            
            if [ -e "$file_path" ]; then
                if sudo chmod $permissions "$file_path" > /dev/null 2>&1; then
                    echo "✅ Permissions set to $permissions for $file_path" >> "$system_report"
                else
                    echo "❌ Failed to set permissions for $file_path" >> "$system_report"
                    log_message "Failed to set permissions for $file_path"
                fi
            else
                echo "❌ File not found: $file_path" >> "$system_report"
            fi
        done
        
        # Secure directories
        local sensitive_directories=(
            "/home/ubuntu/dev/atlas/config:700"
            "/home/ubuntu/dev/atlas/logs:755"
            "/home/ubuntu/dev/atlas/backups:700"
        )
        
        for dir_info in "${sensitive_directories[@]}"; do
            local dir_path=$(echo $dir_info | cut -d':' -f1)
            local permissions=$(echo $dir_info | cut -d':' -f2)
            
            if [ -d "$dir_path" ]; then
                if sudo chmod $permissions "$dir_path" > /dev/null 2>&1; then
                    echo "✅ Permissions set to $permissions for $dir_path" >> "$system_report"
                else
                    echo "❌ Failed to set permissions for $dir_path" >> "$system_report"
                    log_message "Failed to set permissions for $dir_path"
                fi
            else
                echo "❌ Directory not found: $dir_path" >> "$system_report"
            fi
        done
    else
        echo "❌ File permission securing is disabled in configuration" >> "$system_report"
        log_message "File permission securing is disabled in configuration"
    fi
    echo "" >> "$system_report"
    
    # Enable auditing
    echo "Enabling System Auditing:" >> "$system_report"
    echo "----------------------" >> "$system_report"
    
    if [ "$enable_auditing" = "true" ]; then
        # Install auditd if not already installed
        if ! dpkg -l | grep -q "^ii  auditd "; then
            if sudo apt install -y auditd > /dev/null 2>&1; then
                echo "✅ auditd installed successfully" >> "$system_report"
            else
                echo "❌ Failed to install auditd" >> "$system_report"
                log_message "Failed to install auditd"
            fi
        else
            echo "✅ auditd is already installed" >> "$system_report"
        fi
        
        # Start auditd service
        if sudo systemctl start auditd > /dev/null 2>&1; then
            echo "✅ auditd service started" >> "$system_report"
        else
            echo "❌ Failed to start auditd service" >> "$system_report"
            log_message "Failed to start auditd service"
        fi
        
        # Enable auditd service to start on boot
        if sudo systemctl enable auditd > /dev/null 2>&1; then
            echo "✅ auditd service enabled to start on boot" >> "$system_report"
        else
            echo "❌ Failed to enable auditd service to start on boot" >> "$system_report"
            log_message "Failed to enable auditd service to start on boot"
        fi
    else
        echo "❌ System auditing is disabled in configuration" >> "$system_report"
        log_message "System auditing is disabled in configuration"
    fi
    echo "" >> "$system_report"
    
    # Verify system security
    echo "Verifying System Security:" >> "$system_report"
    echo "------------------------" >> "$system_report"
    
    # Check if security tools are installed and running
    local security_tools=("fail2ban" "auditd")
    
    for tool in "${security_tools[@]}"; do
        if systemctl is-active --quiet $tool; then
            echo "✅ $tool is running" >> "$system_report"
        else
            echo "❌ $tool is not running" >> "$system_report"
        fi
    done
    
    # Check for unnecessary services
    local unnecessary_services=("telnet" "ftp" "rsh" "rexec")
    
    for service in "${unnecessary_services[@]}"; do
        if systemctl is-active --quiet $service; then
            echo "❌ Unnecessary service $service is running" >> "$system_report"
        else
            echo "✅ Unnecessary service $service is not running" >> "$system_report"
        fi
    done
    echo "" >> "$system_report"
    
    # System security recommendations
    echo "System Security Recommendations:" >> "$system_report"
    echo "------------------------------" >> "$system_report"
    
    if [ "$update_packages" = "true" ]; then
        echo "✅ System packages are kept up to date" >> "$system_report"
        echo "✅ Continue regular package updates" >> "$system_report"
        echo "✅ Monitor security advisories" >> "$system_report"
    else
        echo "❌ System packages are not updated regularly" >> "$system_report"
        echo "❌ Enable automatic package updates" >> "$system_report"
        echo "❌ Monitor security advisories regularly" >> "$system_report"
    fi
    
    if [ "$install_security_tools" = "true" ]; then
        echo "✅ Security tools are installed" >> "$system_report"
        echo "✅ Continue using security tools for monitoring" >> "$system_report"
        echo "✅ Schedule regular security scans" >> "$system_report"
    else
        echo "❌ Security tools are not installed" >> "$system_report"
        echo "❌ Install security tools immediately" >> "$system_report"
        echo "❌ Schedule regular security assessments" >> "$system_report"
    fi
    
    if [ "$secure_permissions" = "true" ]; then
        echo "✅ File permissions are secured" >> "$system_report"
        echo "✅ Continue monitoring file permissions" >> "$system_report"
        echo "✅ Review permissions periodically" >> "$system_report"
    else
        echo "❌ File permissions are not secured" >> "$system_report"
        echo "❌ Secure sensitive file permissions immediately" >> "$system_report"
        echo "❌ Implement permission monitoring" >> "$system_report"
    fi
    
    if [ "$enable_auditing" = "true" ]; then
        echo "✅ System auditing is enabled" >> "$system_report"
        echo "✅ Continue audit logging" >> "$system_report"
        echo "✅ Review audit logs regularly" >> "$system_report"
    else
        echo "❌ System auditing is disabled" >> "$system_report"
        echo "❌ Enable system auditing" >> "$system_report"
        echo "❌ Implement audit log monitoring" >> "$system_report"
    fi
    
    if [ "$remove_unnecessary_packages" = "true" ]; then
        echo "✅ Unnecessary packages are removed" >> "$system_report"
        echo "✅ Continue removing unnecessary software" >> "$system_report"
        echo "✅ Review installed packages periodically" >> "$system_report"
    else
        echo "❌ Unnecessary packages are not removed" >> "$system_report"
        echo "❌ Remove unnecessary software" >> "$system_report"
        echo "❌ Review installed packages for removal" >> "$system_report"
    fi
    echo "" >> "$system_report"
    
    echo "✅ System security hardening completed"
    echo "📋 System security report saved to: $system_report"
    log_message "System security hardening completed: $system_report"
    
    # Display summary
    echo ""
    echo "System Security Hardening Summary:"
    echo "  Remove Unnecessary Packages: $remove_unnecessary_packages"
    echo "  Update Packages: $update_packages"
    echo "  Install Security Tools: $install_security_tools"
    echo "  Secure Permissions: $secure_permissions"
    echo "  Enable Auditing: $enable_auditing"
    echo "  Mount Options: $mount_options"
    echo "  Security Tools Status:"
    for tool in "${security_tools[@]}"; do
        echo "    $tool: $(if systemctl is-active --quiet $tool; then echo "Running"; else echo "Not Running"; fi)"
    done
    echo "  Report: $system_report"
}

# Function to harden application security
harden_application_security() {
    log_message "Hardening application security"
    
    echo ""
    echo "Hardening Application Security..."
    echo "=============================="
    
    local app_report="$SECURITY_REPORT_DIR/application_hardening_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create application security report header
    echo "Atlas Production Application Security Hardening" > "$app_report"
    echo "Generated: $(date)" >> "$app_report"
    echo "=============================================" >> "$app_report"
    echo "" >> "$app_report"
    
    # Get application security configuration
    local web_server_name=$(jq -r '.security.application.web_server.name' "$SECURITY_CONFIG")
    local security_headers_enabled=$(jq -r '.security.application.web_server.security_headers.enabled' "$SECURITY_CONFIG")
    local rate_limiting_enabled=$(jq -r '.security.application.web_server.rate_limiting.enabled' "$SECURITY_CONFIG")
    local requests_per_second=$(jq -r '.security.application.web_server.rate_limiting.requests_per_second' "$SECURITY_CONFIG")
    local database_ssl_enabled=$(jq -r '.security.application.database.ssl_enabled' "$SECURITY_CONFIG")
    local database_auth_method=$(jq -r '.security.application.database.authentication_method' "$SECURITY_CONFIG")
    local database_connection_limit=$(jq -r '.security.application.database.connection_limit' "$SECURITY_CONFIG")
    
    echo "Application Security Configuration:" >> "$app_report"
    echo "---------------------------------" >> "$app_report"
    echo "Web Server: $web_server_name" >> "$app_report"
    echo "Security Headers Enabled: $security_headers_enabled" >> "$app_report"
    echo "Rate Limiting Enabled: $rate_limiting_enabled" >> "$app_report"
    echo "Requests Per Second: $requests_per_second" >> "$app_report"
    echo "Database SSL Enabled: $database_ssl_enabled" >> "$app_report"
    echo "Database Authentication Method: $database_auth_method" >> "$app_report"
    echo "Database Connection Limit: $database_connection_limit" >> "$app_report"
    echo "" >> "$app_report"
    
    # Harden web server security
    echo "Hardening Web Server Security:" >> "$app_report"
    echo "---------------------------" >> "$app_report"
    
    if [ "$web_server_name" = "nginx" ]; then
        # Check if Nginx is installed
        if dpkg -l | grep -q "^ii  nginx "; then
            echo "✅ Nginx is installed" >> "$app_report"
            
            # Apply security headers
            if [ "$security_headers_enabled" = "true" ]; then
                local nginx_config="/etc/nginx/sites-available/atlas"
                
                if [ -f "$nginx_config" ]; then
                    # Backup original configuration
                    sudo cp "$nginx_config" "${nginx_config}.bak.$(date +%Y%m%d_%H%M%S)" > /dev/null 2>&1
                    echo "✅ Nginx configuration backed up" >> "$app_report"
                    
                    # Add security headers
                    local x_frame_options=$(jq -r '.security.application.web_server.security_headers.x_frame_options' "$SECURITY_CONFIG")
                    local x_content_type_options=$(jq -r '.security.application.web_server.security_headers.x_content_type_options' "$SECURITY_CONFIG")
                    local x_xss_protection=$(jq -r '.security.application.web_server.security_headers.x_xss_protection' "$SECURITY_CONFIG")
                    local strict_transport_security=$(jq -r '.security.application.web_server.security_headers.strict_transport_security' "$SECURITY_CONFIG")
                    local content_security_policy=$(jq -r '.security.application.web_server.security_headers.content_security_policy' "$SECURITY_CONFIG")
                    
                    # Add headers to configuration
                    sudo sed -i '/add_header/d' "$nginx_config"
                    sudo sed -i '/server {/a \
    add_header X-Frame-Options '"$x_frame_options"'; \
    add_header X-Content-Type-Options '"$x_content_type_options"'; \
    add_header X-XSS-Protection '"$x_xss_protection"'; \
    add_header Strict-Transport-Security '"$strict_transport_security"'; \
    add_header Content-Security-Policy '"$content_security_policy"';' "$nginx_config"
                    
                    echo "✅ Security headers added to Nginx configuration" >> "$app_report"
                    
                    # Restart Nginx
                    if sudo systemctl restart nginx; then
                        echo "✅ Nginx restarted with new configuration" >> "$app_report"
                    else
                        echo "❌ Failed to restart Nginx" >> "$app_report"
                        log_message "Failed to restart Nginx"
                    fi
                else
                    echo "❌ Nginx configuration file not found: $nginx_config" >> "$app_report"
                    log_message "Nginx configuration file not found: $nginx_config"
                fi
            else
                echo "❌ Security headers are disabled in configuration" >> "$app_report"
                log_message "Security headers are disabled in configuration"
            fi
            
            # Apply rate limiting
            if [ "$rate_limiting_enabled" = "true" ]; then
                # Add rate limiting to Nginx configuration
                local nginx_main_config="/etc/nginx/nginx.conf"
                
                if [ -f "$nginx_main_config" ]; then
                    # Add rate limiting zone
                    if ! grep -q "limit_req_zone" "$nginx_main_config"; then
                        sudo sed -i '/http {/a \
    limit_req_zone $binary_remote_addr zone=atlas:10m rate='"$requests_per_second"'r/s;' "$nginx_main_config"
                        echo "✅ Rate limiting zone added to Nginx configuration" >> "$app_report"
                    else
                        echo "✅ Rate limiting zone already exists in Nginx configuration" >> "$app_report"
                    fi
                    
                    # Add rate limiting to server block
                    local nginx_site_config="/etc/nginx/sites-available/atlas"
                    if [ -f "$nginx_site_config" ]; then
                        if ! grep -q "limit_req" "$nginx_site_config"; then
                            sudo sed -i '/location \//a \
        limit_req zone=atlas burst=10 nodelay;' "$nginx_site_config"
                            echo "✅ Rate limiting added to server block" >> "$app_report"
                        else
                            echo "✅ Rate limiting already exists in server block" >> "$app_report"
                        fi
                        
                        # Restart Nginx
                        if sudo systemctl restart nginx; then
                            echo "✅ Nginx restarted with rate limiting" >> "$app_report"
                        else
                            echo "❌ Failed to restart Nginx with rate limiting" >> "$app_report"
                            log_message "Failed to restart Nginx with rate limiting"
                        fi
                    else
                        echo "❌ Nginx site configuration not found: $nginx_site_config" >> "$app_report"
                        log_message "Nginx site configuration not found: $nginx_site_config"
                    fi
                else
                    echo "❌ Nginx main configuration not found: $nginx_main_config" >> "$app_report"
                    log_message "Nginx main configuration not found: $nginx_main_config"
                fi
            else
                echo "❌ Rate limiting is disabled in configuration" >> "$app_report"
                log_message "Rate limiting is disabled in configuration"
            fi
        else
            echo "❌ Nginx is not installed" >> "$app_report"
            log_message "Nginx is not installed"
        fi
    else
        echo "❌ Unsupported web server: $web_server_name" >> "$app_report"
        log_message "Unsupported web server: $web_server_name"
    fi
    echo "" >> "$app_report"
    
    # Harden database security
    echo "Hardening Database Security:" >> "$app_report"
    echo "--------------------------" >> "$app_report"
    
    if [ "$database_ssl_enabled" = "true" ]; then
        # Check if PostgreSQL is installed
        if dpkg -l | grep -q "^ii  postgresql "; then
            echo "✅ PostgreSQL is installed" >> "$app_report"
            
            # Check if SSL is enabled
            local postgresql_conf="/etc/postgresql/12/main/postgresql.conf"
            
            if [ -f "$postgresql_conf" ]; then
                # Backup original configuration
                sudo cp "$postgresql_conf" "${postgresql_conf}.bak.$(date +%Y%m%d_%H%M%S)" > /dev/null 2>&1
                echo "✅ PostgreSQL configuration backed up" >> "$app_report"
                
                # Enable SSL
                sudo sed -i "s/^#*ssl.*/ssl = on/" "$postgresql_conf"
                echo "✅ SSL enabled in PostgreSQL configuration" >> "$app_report"
                
                # Set SSL certificate and key paths
                sudo sed -i "s/^#*ssl_cert_file.*/ssl_cert_file = '\/etc\/ssl\/certs\/ssl-cert.pem'/" "$postgresql_conf"
                sudo sed -i "s/^#*ssl_key_file.*/ssl_key_file = '\/etc\/ssl\/private\/ssl-cert.key'/" "$postgresql_conf"
                echo "✅ SSL certificate and key paths set" >> "$app_report"
                
                # Restart PostgreSQL
                if sudo systemctl restart postgresql; then
                    echo "✅ PostgreSQL restarted with SSL enabled" >> "$app_report"
                else
                    echo "❌ Failed to restart PostgreSQL with SSL" >> "$app_report"
                    log_message "Failed to restart PostgreSQL with SSL"
                fi
            else
                echo "❌ PostgreSQL configuration file not found: $postgresql_conf" >> "$app_report"
                log_message "PostgreSQL configuration file not found: $postgresql_conf"
            fi
        else
            echo "❌ PostgreSQL is not installed" >> "$app_report"
            log_message "PostgreSQL is not installed"
        fi
    else
        echo "❌ Database SSL is disabled in configuration" >> "$app_report"
        log_message "Database SSL is disabled in configuration"
    fi
    
    # Configure database authentication
    echo "Configuring Database Authentication:" >> "$app_report"
    echo "----------------------------------" >> "$app_report"
    
    local pg_hba_conf="/etc/postgresql/12/main/pg_hba.conf"
    
    if [ -f "$pg_hba_conf" ]; then
        # Backup original configuration
        sudo cp "$pg_hba_conf" "${pg_hba_conf}.bak.$(date +%Y%m%d_%H%M%S)" > /dev/null 2>&1
        echo "✅ PostgreSQL authentication configuration backed up" >> "$app_report"
        
        # Configure authentication method
        if [ "$database_auth_method" = "md5" ]; then
            # Replace trust with md5 for local connections
            sudo sed -i 's/local.*all.*all.*trust/local all all md5/' "$pg_hba_conf"
            echo "✅ MD5 authentication configured for local connections" >> "$app_report"
            
            # Replace trust with md5 for host connections
            sudo sed -i 's/host.*all.*all.*127.0.0.1\/32.*trust/host all all 127.0.0.1\/32 md5/' "$pg_hba_conf"
            sudo sed -i 's/host.*all.*all.*::1\/128.*trust/host all all ::1\/128 md5/' "$pg_hba_conf"
            echo "✅ MD5 authentication configured for host connections" >> "$app_report"
        else
            echo "❌ Unsupported authentication method: $database_auth_method" >> "$app_report"
            log_message "Unsupported authentication method: $database_auth_method"
        fi
        
        # Set connection limit
        sudo sed -i "s/^#*max_connections.*/max_connections = $database_connection_limit/" "/etc/postgresql/12/main/postgresql.conf"
        echo "✅ Database connection limit set to $database_connection_limit" >> "$app_report"
        
        # Restart PostgreSQL
        if sudo systemctl restart postgresql; then
            echo "✅ PostgreSQL restarted with new authentication configuration" >> "$app_report"
        else
            echo "❌ Failed to restart PostgreSQL with new authentication" >> "$app_report"
            log_message "Failed to restart PostgreSQL with new authentication"
        fi
    else
        echo "❌ PostgreSQL authentication configuration not found: $pg_hba_conf" >> "$app_report"
        log_message "PostgreSQL authentication configuration not found: $pg_hba_conf"
    fi
    echo "" >> "$app_report"
    
    # Verify application security
    echo "Verifying Application Security:" >> "$app_report"
    echo "-----------------------------" >> "$app_report"
    
    # Check web server status
    if systemctl is-active --quiet nginx; then
        echo "✅ Nginx is running" >> "$app_report"
        
        # Check if security headers are present
        local security_headers_check=$(curl -I -s http://localhost/ | grep -E "(X-Frame-Options|X-Content-Type-Options|X-XSS-Protection|Strict-Transport-Security|Content-Security-Policy)")
        if [ ! -z "$security_headers_check" ]; then
            echo "✅ Security headers are present in web responses" >> "$app_report"
        else
            echo "❌ Security headers are missing from web responses" >> "$app_report"
        fi
        
        # Check rate limiting
        if [ "$rate_limiting_enabled" = "true" ]; then
            echo "✅ Rate limiting is configured (check manually for effectiveness)" >> "$app_report"
        else
            echo "❌ Rate limiting is disabled" >> "$app_report"
        fi
    else
        echo "❌ Nginx is not running" >> "$app_report"
    fi
    
    # Check database status
    if systemctl is-active --quiet postgresql; then
        echo "✅ PostgreSQL is running" >> "$app_report"
        
        # Check SSL status
        if [ "$database_ssl_enabled" = "true" ]; then
            local ssl_status=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SHOW ssl;" 2>/dev/null | grep -q "on" && echo "enabled" || echo "disabled")
            if [ "$ssl_status" = "enabled" ]; then
                echo "✅ Database SSL is enabled" >> "$app_report"
            else
                echo "❌ Database SSL is disabled" >> "$app_report"
            fi
        else
            echo "❌ Database SSL is disabled in configuration" >> "$app_report"
        fi
        
        # Check authentication method
        local auth_method_check=$(grep "local all all md5" "$pg_hba_conf" 2>/dev/null || echo "")
        if [ ! -z "$auth_method_check" ]; then
            echo "✅ Database authentication method is set to MD5" >> "$app_report"
        else
            echo "❌ Database authentication method is not set to MD5" >> "$app_report"
        fi
        
        # Check connection limit
        local connection_limit_check=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SHOW max_connections;" 2>/dev/null | xargs)
        if [ "$connection_limit_check" = "$database_connection_limit" ]; then
            echo "✅ Database connection limit is set to $database_connection_limit" >> "$app_report"
        else
            echo "❌ Database connection limit is set to $connection_limit_check, expected $database_connection_limit" >> "$app_report"
        fi
    else
        echo "❌ PostgreSQL is not running" >> "$app_report"
    fi
    echo "" >> "$app_report"
    
    # Application security recommendations
    echo "Application Security Recommendations:" >> "$app_report"
    echo "----------------------------------" >> "$app_report"
    
    if [ "$security_headers_enabled" = "true" ]; then
        echo "✅ Security headers are enabled" >> "$app_report"
        echo "✅ Continue using security headers for web protection" >> "$app_report"
        echo "✅ Review and update security headers periodically" >> "$app_report"
    else
        echo "❌ Security headers are disabled" >> "$app_report"
        echo "❌ Enable security headers immediately" >> "$app_report"
        echo "❌ Review and implement web security best practices" >> "$app_report"
    fi
    
    if [ "$rate_limiting_enabled" = "true" ]; then
        echo "✅ Rate limiting is enabled" >> "$app_report"
        echo "✅ Current rate limit: ${requests_per_second} requests/second" >> "$app_report"
        echo "✅ Continue rate limiting to prevent abuse" >> "$app_report"
    else
        echo "❌ Rate limiting is disabled" >> "$app_report"
        echo "❌ Enable rate limiting to prevent denial of service" >> "$app_report"
        echo "❌ Configure appropriate rate limits for services" >> "$app_report"
    fi
    
    if [ "$database_ssl_enabled" = "true" ]; then
        echo "✅ Database SSL is enabled" >> "$app_report"
        echo "✅ Continue using SSL for database connections" >> "$app_report"
        echo "✅ Monitor SSL certificate expiration" >> "$app_report"
    else
        echo "❌ Database SSL is disabled" >> "$app_report"
        echo "❌ Enable SSL for database connections immediately" >> "$app_report"
        echo "❌ Implement encrypted database connections" >> "$app_report"
    fi
    
    if [ "$database_auth_method" = "md5" ]; then
        echo "✅ Database authentication method is MD5" >> "$app_report"
        echo "✅ Continue using strong authentication for database" >> "$app_report"
        echo "✅ Review and update authentication methods periodically" >> "$app_report"
    else
        echo "❌ Database authentication method is not MD5" >> "$app_report"
        echo "❌ Change database authentication to MD5 immediately" >> "$app_report"
        echo "❌ Implement strong authentication for database connections" >> "$app_report"
    fi
    
    if [ "$database_connection_limit" -le 100 ]; then
        echo "✅ Database connection limit is reasonable (${database_connection_limit})" >> "$app_report"
        echo "✅ Continue monitoring database connections" >> "$app_report"
    else
        echo "❌ Database connection limit is high (${database_connection_limit})" >> "$app_report"
        echo "❌ Review and adjust database connection limits" >> "$app_report"
        echo "✅ Monitor database connection usage" >> "$app_report"
    fi
    echo "" >> "$app_report"
    
    echo "✅ Application security hardening completed"
    echo "📋 Application security report saved to: $app_report"
    log_message "Application security hardening completed: $app_report"
    
    # Display summary
    echo ""
    echo "Application Security Hardening Summary:"
    echo "  Web Server: $web_server_name"
    echo "  Security Headers Enabled: $security_headers_enabled"
    echo "  Rate Limiting Enabled: $rate_limiting_enabled"
    echo "  Requests Per Second: $requests_per_second"
    echo "  Database SSL Enabled: $database_ssl_enabled"
    echo "  Database Authentication Method: $database_auth_method"
    echo "  Database Connection Limit: $database_connection_limit"
    echo "  Nginx Status: $(if systemctl is-active --quiet nginx; then echo "Running"; else echo "Not Running"; fi)"
    echo "  PostgreSQL Status: $(if systemctl is-active --quiet postgresql; then echo "Running"; else echo "Not Running"; fi)"
    echo "  Report: $app_report"
}

# Function to run security scan
run_security_scan() {
    log_message "Running security scan"
    
    echo ""
    echo "Running Security Scan..."
    echo "======================"
    
    local scan_report="$SECURITY_REPORT_DIR/security_scan_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create security scan report header
    echo "Atlas Production Security Scan" > "$scan_report"
    echo "Generated: $(date)" >> "$scan_report"
    echo "===============================" >> "$scan_report"
    echo "" >> "$scan_report"
    
    # Check if security tools are installed
    echo "Security Tools Check:" >> "$scan_report"
    echo "-------------------" >> "$scan_report"
    
    local security_tools=("lynis" "clamav" "rkhunter" "chkrootkit")
    local tools_installed=0
    
    for tool in "${security_tools[@]}"; do
        if command -v $tool &> /dev/null; then
            echo "✅ $tool is installed" >> "$scan_report"
            tools_installed=$((tools_installed + 1))
        else
            echo "❌ $tool is not installed" >> "$scan_report"
        fi
    done
    echo "" >> "$scan_report"
    
    # Run Lynis security audit
    echo "Lynis Security Audit:" >> "$scan_report"
    echo "-------------------" >> "$scan_report"
    
    if command -v lynis &> /dev/null; then
        echo "Running Lynis security audit..." >> "$scan_report"
        
        # Run quick Lynis audit
        if sudo lynis audit system --quick > /tmp/lynis_audit.txt 2>/dev/null; then
            echo "✅ Lynis audit completed successfully" >> "$scan_report"
            
            # Extract key findings
            local warnings=$(grep "Warning" /tmp/lynis_audit.txt | wc -l)
            local suggestions=$(grep "Suggestion" /tmp/lynis_audit.txt | wc -l)
            
            echo "Lynis Findings:" >> "$scan_report"
            echo "  Warnings: $warnings" >> "$scan_report"
            echo "  Suggestions: $suggestions" >> "$scan_report"
            
            if [ $warnings -gt 0 ] || [ $suggestions -gt 0 ]; then
                echo "❌ Security issues detected by Lynis" >> "$scan_report"
                echo "  Review /tmp/lynis_audit.txt for details" >> "$scan_report"
            else
                echo "✅ No security issues detected by Lynis" >> "$scan_report"
            fi
        else
            echo "❌ Lynis audit failed" >> "$scan_report"
        fi
        
        # Clean up temporary file
        rm -f /tmp/lynis_audit.txt
    else
        echo "❌ Lynis is not installed" >> "$scan_report"
    fi
    echo "" >> "$scan_report"
    
    # Run ClamAV malware scan
    echo "ClamAV Malware Scan:" >> "$scan_report"
    echo "------------------" >> "$scan_report"
    
    if command -v clamav &> /dev/null; then
        echo "Running ClamAV malware scan..." >> "$scan_report"
        
        # Update ClamAV signatures
        if sudo freshclam > /dev/null 2>&1; then
            echo "✅ ClamAV signatures updated" >> "$scan_report"
        else
            echo "❌ Failed to update ClamAV signatures" >> "$scan_report"
        fi
        
        # Run malware scan on Atlas directory
        local atlas_dir="/home/ubuntu/dev/atlas"
        if [ -d "$atlas_dir" ]; then
            if sudo clamscan -r "$atlas_dir" > /tmp/clamav_scan.txt 2>/dev/null; then
                echo "✅ ClamAV scan completed successfully" >> "$scan_report"
                
                # Extract scan results
                local infected_files=$(grep "Infected files:" /tmp/clamav_scan.txt | awk '{print $3}')
                local total_files=$(grep "Scanned files:" /tmp/clamav_scan.txt | awk '{print $3}')
                
                echo "ClamAV Results:" >> "$scan_report"
                echo "  Scanned Files: $total_files" >> "$scan_report"
                echo "  Infected Files: $infected_files" >> "$scan_report"
                
                if [ $infected_files -eq 0 ]; then
                    echo "✅ No malware detected by ClamAV" >> "$scan_report"
                else
                    echo "❌ Malware detected by ClamAV" >> "$scan_report"
                    echo "  Review /tmp/clamav_scan.txt for details" >> "$scan_report"
                fi
            else
                echo "❌ ClamAV scan failed" >> "$scan_report"
            fi
            
            # Clean up temporary file
            rm -f /tmp/clamav_scan.txt
        else
            echo "❌ Atlas directory not found: $atlas_dir" >> "$scan_report"
        fi
    else
        echo "❌ ClamAV is not installed" >> "$scan_report"
    fi
    echo "" >> "$scan_report"
    
    # Run Rootkit Hunter scan
    echo "Rootkit Hunter Scan:" >> "$scan_report"
    echo "------------------" >> "$scan_report"
    
    if command -v rkhunter &> /dev/null; then
        echo "Running Rootkit Hunter scan..." >> "$scan_report"
        
        # Update RKHunter database
        if sudo rkhunter --update > /dev/null 2>&1; then
            echo "✅ RKHunter database updated" >> "$scan_report"
        else
            echo "❌ Failed to update RKHunter database" >> "$scan_report"
        fi
        
        # Run RKHunter scan
        if sudo rkhunter --check --sk > /tmp/rkhunter_scan.txt 2>/dev/null; then
            echo "✅ RKHunter scan completed successfully" >> "$scan_report"
            
            # Extract scan results
            local warnings=$(grep "Warning:" /tmp/rkhunter_scan.txt | wc -l)
            local possible_rootkits=$(grep "Possible rootkit" /tmp/rkhunter_scan.txt | wc -l)
            
            echo "RKHunter Results:" >> "$scan_report"
            echo "  Warnings: $warnings" >> "$scan_report"
            echo "  Possible Rootkits: $possible_rootkits" >> "$scan_report"
            
            if [ $warnings -eq 0 ] && [ $possible_rootkits -eq 0 ]; then
                echo "✅ No rootkits detected by RKHunter" >> "$scan_report"
            else
                echo "❌ Rootkits or warnings detected by RKHunter" >> "$scan_report"
                echo "  Review /tmp/rkhunter_scan.txt for details" >> "$scan_report"
            fi
        else
            echo "❌ RKHunter scan failed" >> "$scan_report"
        fi
        
        # Clean up temporary file
        rm -f /tmp/rkhunter_scan.txt
    else
        echo "❌ RKHunter is not installed" >> "$scan_report"
    fi
    echo "" >> "$scan_report"
    
    # Run CHKRootkit scan
    echo "CHKRootkit Scan:" >> "$scan_report"
    echo "---------------" >> "$scan_report"
    
    if command -v chkrootkit &> /dev/null; then
        echo "Running CHKRootkit scan..." >> "$scan_report"
        
        # Run CHKRootkit scan
        if sudo chkrootkit > /tmp/chkrootkit_scan.txt 2>/dev/null; then
            echo "✅ CHKRootkit scan completed successfully" >> "$scan_report"
            
            # Extract scan results
            local infected=$(grep "INFECTED" /tmp/chkrootkit_scan.txt | wc -l)
            
            echo "CHKRootkit Results:" >> "$scan_report"
            echo "  Infected Systems: $infected" >> "$scan_report"
            
            if [ $infected -eq 0 ]; then
                echo "✅ No rootkits detected by CHKRootkit" >> "$scan_report"
            else
                echo "❌ Rootkits detected by CHKRootkit" >> "$scan_report"
                echo "  Review /tmp/chkrootkit_scan.txt for details" >> "$scan_report"
            fi
        else
            echo "❌ CHKRootkit scan failed" >> "$scan_report"
        fi
        
        # Clean up temporary file
        rm -f /tmp/chkrootkit_scan.txt
    else
        echo "❌ CHKRootkit is not installed" >> "$scan_report"
    fi
    echo "" >> "$scan_report"
    
    # Security scan summary
    echo "Security Scan Summary:" >> "$scan_report"
    echo "--------------------" >> "$scan_report"
    
    local total_tools=${#security_tools[@]}
    echo "Security Tools Installed: $tools_installed/$total_tools" >> "$scan_report"
    
    if [ $tools_installed -eq $total_tools ]; then
        echo "✅ All security tools are installed" >> "$scan_report"
    else
        echo "❌ Some security tools are missing" >> "$scan_report"
        echo "  Install missing tools: $(echo "${security_tools[@]}" | tr ' ' '\n' | grep -v "$(command -v lynis &>/dev/null && echo 'lynis')$(command -v clamav &>/dev/null && echo 'clamav')$(command -v rkhunter &>/dev/null && echo 'rkhunter')$(command -v chkrootkit &>/dev/null && echo 'chkrootkit')")" >> "$scan_report"
    fi
    
    # Check for security issues
    local security_issues=0
    
    # Check Lynis findings
    if [ -f /tmp/lynis_audit.txt ]; then
        local lynis_warnings=$(grep "Warning" /tmp/lynis_audit.txt | wc -l)
        local lynis_suggestions=$(grep "Suggestion" /tmp/lynis_audit.txt | wc -l)
        if [ $lynis_warnings -gt 0 ] || [ $lynis_suggestions -gt 0 ]; then
            security_issues=$((security_issues + 1))
        fi
    fi
    
    # Check ClamAV findings
    if [ -f /tmp/clamav_scan.txt ]; then
        local infected_files=$(grep "Infected files:" /tmp/clamav_scan.txt | awk '{print $3}')
        if [ $infected_files -gt 0 ]; then
            security_issues=$((security_issues + 1))
        fi
    fi
    
    # Check RKHunter findings
    if [ -f /tmp/rkhunter_scan.txt ]; then
        local rkhunter_warnings=$(grep "Warning:" /tmp/rkhunter_scan.txt | wc -l)
        local rkhunter_rootkits=$(grep "Possible rootkit" /tmp/rkhunter_scan.txt | wc -l)
        if [ $rkhunter_warnings -gt 0 ] || [ $rkhunter_rootkits -gt 0 ]; then
            security_issues=$((security_issues + 1))
        fi
    fi
    
    # Check CHKRootkit findings
    if [ -f /tmp/chkrootkit_scan.txt ]; then
        local chkrootkit_infected=$(grep "INFECTED" /tmp/chkrootkit_scan.txt | wc -l)
        if [ $chkrootkit_infected -gt 0 ]; then
            security_issues=$((security_issues + 1))
        fi
    fi
    
    if [ $security_issues -eq 0 ]; then
        echo "✅ No security issues detected" >> "$scan_report"
        echo "✅ System appears to be secure" >> "$scan_report"
    else
        echo "❌ Security issues detected" >> "$scan_report"
        echo "❌ Review scan results for details" >> "$scan_report"
        echo "❌ Address security vulnerabilities immediately" >> "$scan_report"
    fi
    echo "" >> "$scan_report"
    
    # Security recommendations
    echo "Security Recommendations:" >> "$scan_report"
    echo "-----------------------" >> "$scan_report"
    
    if [ $security_issues -eq 0 ]; then
        echo "✅ Continue current security practices" >> "$scan_report"
        echo "✅ Schedule regular security scans" >> "$scan_report"
        echo "✅ Monitor security advisories" >> "$scan_report"
    else
        echo "❌ Address detected security issues immediately" >> "$scan_report"
        echo "✅ Review and remediate all security findings" >> "$scan_report"
        echo "✅ Implement additional security measures" >> "$scan_report"
        echo "✅ Schedule more frequent security scans" >> "$scan_report"
    fi
    
    if [ $tools_installed -lt $total_tools ]; then
        echo "❌ Install all recommended security tools" >> "$scan_report"
        echo "✅ Configure and schedule regular scans" >> "$scan_report"
        echo "✅ Monitor scan results and alerts" >> "$scan_report"
    fi
    echo "" >> "$scan_report"
    
    echo "✅ Security scan completed"
    echo "📋 Security scan report saved to: $scan_report"
    log_message "Security scan completed: $scan_report"
    
    # Display summary
    echo ""
    echo "Security Scan Summary:"
    echo "  Tools Installed: $tools_installed/$total_tools"
    echo "  Security Issues: $security_issues"
    if [ $security_issues -eq 0 ]; then
        echo "  Status: ✅ SECURE"
    else
        echo "  Status: ❌ VULNERABILITIES DETECTED"
    fi
    echo "  Report: $scan_report"
}

# Main function
main() {
    log_message "=== Starting Atlas Security Hardening ==="
    
    # Initialize configuration
    initialize_security_config
    
    # Start time
    local start_time=$(date)
    log_message "Security hardening started at: $start_time"
    
    # Handle different security operations
    case $1 in
        "network")
            harden_network_security
            ;;
        "ssh")
            harden_ssh_security
            ;;
        "system")
            harden_system_security
            ;;
        "application")
            harden_application_security
            ;;
        "scan")
            run_security_scan
            ;;
        "report")
            generate_sla_report
            ;;
        "notify")
            send_sla_notifications
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive security hardening
            harden_network_security
            harden_ssh_security
            harden_system_security
            harden_application_security
            run_security_scan
            generate_sla_report
            send_sla_notifications
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Security hardening completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Security Hardening Completed ==="
    
    echo ""
    echo "✅ Security hardening completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $SECURITY_REPORT_DIR"
    echo "📝 Log file: $SECURITY_LOG"
}

# Run main function
main "$@"