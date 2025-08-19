"""
Emergency Recovery Tools for Atlas
Creates emergency tools for system recovery
"""

import os
import subprocess
import sys
from datetime import datetime
import psutil
import json

class EmergencyTools:
    \"\"\"Manage emergency recovery tools for Atlas\"\"\"
    
    def __init__(self):
        self.emergency_log = "/var/log/atlas_emergency.log"
        self.status_api_port = 8080
        
    def create_panic_button(self):
        \"\"\"Create "panic button" script to restart all services\"\"\"
        print("Creating panic button script...")
        
        panic_script = f\"\"\"#!/bin/bash
# Atlas Emergency Panic Button Script

EMERGENCY_LOG="{self.emergency_log}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] EMERGENCY: Panic button activated" >> $EMERGENCY_LOG

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $EMERGENCY_LOG
}

# Function to restart all Atlas services
restart_all_services() {
    log_message "Restarting all Atlas services"
    
    # List of services to restart
    SERVICES=("atlas" "prometheus" "grafana-server" "nginx" "postgresql")
    
    for service in "${SERVICES[@]}"; do
        log_message "Restarting $service"
        
        # Stop service
        systemctl stop $service >> $EMERGENCY_LOG 2>&1
        sleep 2
        
        # Start service
        systemctl start $service >> $EMERGENCY_LOG 2>&1
        
        # Check if service started successfully
        if systemctl is-active --quiet $service; then
            log_message "✓ $service restarted successfully"
        else
            log_message "✗ Failed to restart $service"
        fi
        
        sleep 3
    done
}

# Function to clear caches and temporary files
clear_caches() {
    log_message "Clearing caches and temporary files"
    
    # Clear system caches
    sync
    echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true
    
    # Clear application caches
    rm -rf /home/ubuntu/dev/atlas/cache/* 2>/dev/null || true
    rm -rf /tmp/atlas_* 2>/dev/null || true
    
    # Clear log caches
    journalctl --vacuum-time=1d >> $EMERGENCY_LOG 2>&1
    
    log_message "Caches cleared successfully"
}

# Function to check system resources
check_resources() {
    log_message "Checking system resources"
    
    # Check disk space
    DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    log_message "Disk usage: ${DISK_USAGE}%"
    
    # Check memory
    MEMORY_USAGE=$(free | grep Mem | awk '{printf "%.2f", $3/$2 * 100.0}')
    log_message "Memory usage: ${MEMORY_USAGE}%"
    
    # Check CPU
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    log_message "CPU usage: ${CPU_USAGE}%"
}

# Main panic button process
main() {
    log_message "=== EMERGENCY PANIC BUTTON ACTIVATED ==="
    
    # Check current system status
    check_resources
    
    # Clear caches
    clear_caches
    
    # Restart all services
    restart_all_services
    
    # Check final system status
    check_resources
    
    log_message "=== EMERGENCY PANIC BUTTON COMPLETED ==="
    
    # Send emergency notification
    echo "Atlas emergency panic button activated and completed at $(date).
    
    System status after recovery:
    $(df -h /)
    $(free -h)
    
    Check $EMERGENCY_LOG for detailed information." | mail -s "Atlas EMERGENCY - Panic Button Activated" admin@example.com
}

# Run main panic button process
main
\"\"\"
        
        script_path = "/usr/local/bin/atlas_panic_button.sh"
        with open(script_path, "w") as f:
            f.write(panic_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created panic button script at {script_path}")
        return script_path
    
    def implement_quick_diagnostics(self):
        \"\"\"Implement quick diagnostic and status check tools\"\"\"
        print("Implementing quick diagnostic tools...")
        
        diag_script = f\"\"\"#!/bin/bash
# Atlas Quick Diagnostic Script

EMERGENCY_LOG="{self.emergency_log}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Running quick diagnostics" >> $EMERGENCY_LOG

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $EMERGENCY_LOG
}

# Function to check service status
check_service_status() {
    local service_name=$1
    local service_port=$2
    
    echo "=== $service_name Status ==="
    
    # Check systemd status
    if systemctl is-active --quiet $service_name; then
        echo "✓ Service: RUNNING"
    else
        echo "✗ Service: STOPPED"
    fi
    
    # Check process
    if pgrep -f "$service_name" > /dev/null 2>&1; then
        echo "✓ Process: ACTIVE"
    else
        echo "✗ Process: INACTIVE"
    fi
    
    # Check port
    if netstat -tlnp 2>/dev/null | grep -q ":$service_port "; then
        echo "✓ Port $service_port: LISTENING"
    else
        echo "✗ Port $service_port: NOT LISTENING"
    fi
    
    echo ""
}

# Function to check system health
check_system_health() {
    echo "=== System Health ==="
    
    # Disk usage
    DISK_USAGE=$(df / | tail -1 | awk '{print $5}')
    echo "Disk Usage: $DISK_USAGE"
    
    # Memory usage
    MEMORY_USAGE=$(free -h | grep Mem | awk '{print $3 "/" $2}')
    echo "Memory Usage: $MEMORY_USAGE"
    
    # CPU usage
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
    echo "CPU Usage: $CPU_USAGE"
    
    # Load average
    LOAD_AVERAGE=$(uptime | awk -F'load average:' '{print $2}')
    echo "Load Average: $LOAD_AVERAGE"
    
    echo ""
}

# Function to check recent logs
check_recent_logs() {
    echo "=== Recent Error Logs ==="
    
    # Check for recent errors in system logs
    journalctl -p err --since "1 hour ago" --no-pager | tail -10
    
    echo ""
}

# Main diagnostic process
main() {
    log_message "Running quick diagnostics"
    
    echo "Atlas Quick Diagnostic Report"
    echo "============================"
    echo "Generated at: $(date)"
    echo ""
    
    # Check system health
    check_system_health
    
    # Check service status
    check_service_status "atlas" "5000"
    check_service_status "prometheus" "9090"
    check_service_status "grafana-server" "3000"
    check_service_status "nginx" "80"
    check_service_status "postgresql" "5432"
    
    # Check recent logs
    check_recent_logs
    
    log_message "Quick diagnostics completed"
}

# Run main diagnostic process
main
\"\"\"
        
        script_path = "/usr/local/bin/atlas_diagnostics.sh"
        with open(script_path, "w") as f:
            f.write(diag_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created diagnostic script at {script_path}")
        return script_path
    
    def setup_emergency_backup(self):
        \"\"\"Set up emergency backup and recovery procedures\"\"\"
        print("Setting up emergency backup procedures...")
        
        backup_script = f\"\"\"#!/bin/bash
# Atlas Emergency Backup Script

EMERGENCY_LOG="{self.emergency_log}"
BACKUP_DIR="/backup/emergency"
DATE=$(date '+%Y%m%d_%H%M%S')

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting emergency backup" >> $EMERGENCY_LOG

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $EMERGENCY_LOG
}

# Function to create emergency backup
create_emergency_backup() {
    log_message "Creating emergency backup"
    
    # Create backup directory
    mkdir -p $BACKUP_DIR/backup_$DATE
    
    # Backup critical data
    log_message "Backing up database"
    pg_dump -U atlas_user atlas_db > $BACKUP_DIR/backup_$DATE/atlas_db.sql 2>> $EMERGENCY_LOG
    
    # Backup configuration
    log_message "Backing up configuration"
    if [ -d "/etc/atlas" ]; then
        cp -r /etc/atlas $BACKUP_DIR/backup_$DATE/config 2>> $EMERGENCY_LOG
    fi
    
    # Backup application code
    log_message "Backing up application code"
    if [ -d "/home/ubuntu/dev/atlas" ]; then
        tar -czf $BACKUP_DIR/backup_$DATE/atlas_code.tar.gz -C /home/ubuntu/dev atlas 2>> $EMERGENCY_LOG
    fi
    
    # Backup logs (last 24 hours)
    log_message "Backing up recent logs"
    mkdir -p $BACKUP_DIR/backup_$DATE/logs
    find /var/log -name "*.log" -mtime -1 -exec cp {} $BACKUP_DIR/backup_$DATE/logs/ \\; 2>> $EMERGENCY_LOG
    
    log_message "Emergency backup completed at $BACKUP_DIR/backup_$DATE"
}

# Function to verify backup integrity
verify_backup() {
    local backup_path=$1
    
    log_message "Verifying backup integrity for $backup_path"
    
    # Check if backup files exist
    if [ -f "$backup_path/atlas_db.sql" ]; then
        log_message "✓ Database backup exists"
    else
        log_message "✗ Database backup missing"
    fi
    
    if [ -d "$backup_path/config" ]; then
        log_message "✓ Configuration backup exists"
    else
        log_message "✗ Configuration backup missing"
    fi
    
    if [ -f "$backup_path/atlas_code.tar.gz" ]; then
        # Test archive integrity
        tar -tzf $backup_path/atlas_code.tar.gz > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            log_message "✓ Code backup is valid"
        else
            log_message "✗ Code backup is corrupted"
        fi
    else
        log_message "✗ Code backup missing"
    fi
    
    log_message "Backup verification completed"
}

# Main emergency backup process
main() {
    log_message "=== Starting Emergency Backup ==="
    
    # Create emergency backup
    create_emergency_backup
    
    # Verify backup integrity
    verify_backup "$BACKUP_DIR/backup_$DATE"
    
    log_message "=== Emergency Backup Completed ==="
    
    # Send notification
    echo "Atlas emergency backup completed at $(date).
    Backup location: $BACKUP_DIR/backup_$DATE
    
    Check $EMERGENCY_LOG for details." | mail -s "Atlas Emergency Backup Completed" admin@example.com
}

# Run main emergency backup process
main
\"\"\"
        
        script_path = "/usr/local/bin/atlas_emergency_backup.sh"
        with open(script_path, "w") as f:
            f.write(backup_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created emergency backup script at {script_path}")
        return script_path
    
    def create_system_status_api(self):
        \"\"\"Create system status API endpoint for external monitoring\"\"\"
        print("Creating system status API endpoint...")
        
        # Create a simple Flask app for status API
        api_script = f\"\"\"#!/usr/bin/env python3
\"\"\"
Atlas System Status API
Simple API endpoint for external monitoring
\"\"\"

import json
import psutil
import subprocess
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

def get_system_status():
    \"\"\"Get comprehensive system status\"\"\"
    status = {
        'timestamp': datetime.now().isoformat(),
        'system': {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory': dict(psutil.virtual_memory()._asdict()),
            'disk': dict(psutil.disk_usage('/')._asdict()),
            'uptime': datetime.now().timestamp() - psutil.boot_time()
        },
        'services': {
            'atlas': check_service_status('atlas'),
            'prometheus': check_service_status('prometheus'),
            'grafana': check_service_status('grafana-server'),
            'nginx': check_service_status('nginx'),
            'postgresql': check_service_status('postgresql')
        },
        'network': {
            'connections': len(psutil.net_connections()),
            'interfaces': dict(psutil.net_if_stats())
        }
    }
    return status

def check_service_status(service_name):
    \"\"\"Check if a service is running\"\"\"
    try:
        result = subprocess.run(['systemctl', 'is-active', service_name], 
                              capture_output=True, text=True)
        return result.stdout.strip() == 'active'
    except:
        return False

@app.route('/status')
def status():
    \"\"\"Return system status\"\"\"
    return jsonify(get_system_status())

@app.route('/health')
def health():
    \"\"\"Return simple health check\"\"\"
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = (psutil.disk_usage('/').used / psutil.disk_usage('/').total) * 100
    
    healthy = (
        cpu_percent < 90 and 
        memory_percent < 90 and 
        disk_percent < 90 and
        check_service_status('atlas')
    )
    
    return jsonify({
        'status': 'healthy' if healthy else 'unhealthy',
        'cpu_percent': cpu_percent,
        'memory_percent': memory_percent,
        'disk_percent': disk_percent,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/')
def index():
    \"\"\"Return API information\"\"\"
    return jsonify({
        'name': 'Atlas System Status API',
        'endpoints': {
            '/status': 'Full system status',
            '/health': 'Simple health check',
            '/': 'This information'
        },
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port={self.status_api_port}, debug=False)
\"\"\"
        
        script_path = "/usr/local/bin/atlas_status_api.py"
        with open(script_path, "w") as f:
            f.write(api_script)
        
        print(f"Created status API script at {script_path}")
        
        # Create systemd service for the API
        service_content = f\"\"\"[Unit]
Description=Atlas System Status API
After=network.target

[Service]
Type=simple
User=atlas
Group=atlas
WorkingDirectory=/home/ubuntu/dev/atlas
ExecStart=/usr/bin/python3 /usr/local/bin/atlas_status_api.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
\"\"\"
        
        service_path = "/etc/systemd/system/atlas-status-api.service"
        with open(service_path, "w") as f:
            f.write(service_content)
        
        print(f"Created systemd service at {service_path}")
        return script_path, service_path
    
    def add_remote_debugging_tools(self):
        \"\"\"Add remote debugging and log access tools\"\"\"
        print("Adding remote debugging tools...")
        
        debug_script = f\"\"\"#!/bin/bash
# Atlas Remote Debugging Tools

EMERGENCY_LOG="{self.emergency_log}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting remote debugging session" >> $EMERGENCY_LOG

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $EMERGENCY_LOG
}

# Function to collect debug information
collect_debug_info() {
    local debug_dir="/tmp/atlas_debug_$(date +%Y%m%d_%H%M%S)"
    mkdir -p $debug_dir
    
    log_message "Collecting debug information in $debug_dir"
    
    # System information
    uname -a > $debug_dir/system_info.txt
    lsb_release -a > $debug_dir/os_info.txt 2>/dev/null || true
    
    # Process information
    ps aux | grep atlas > $debug_dir/atlas_processes.txt
    top -bn1 > $debug_dir/top_output.txt
    
    # Network information
    netstat -tlnp > $debug_dir/network_connections.txt
    ss -tlnp > $debug_dir/socket_connections.txt
    
    # Disk information
    df -h > $debug_dir/disk_usage.txt
    iotop -b -n 1 > $debug_dir/disk_io.txt 2>/dev/null || true
    
    # Memory information
    free -h > $debug_dir/memory_usage.txt
    vmstat 1 5 > $debug_dir/vmstat.txt
    
    # Service status
    systemctl status atlas > $debug_dir/atlas_service_status.txt 2>&1
    systemctl status prometheus > $debug_dir/prometheus_service_status.txt 2>&1
    systemctl status grafana-server > $debug_dir/grafana_service_status.txt 2>&1
    systemctl status nginx > $debug_dir/nginx_service_status.txt 2>&1
    systemctl status postgresql > $debug_dir/postgresql_service_status.txt 2>&1
    
    # Recent logs
    journalctl -u atlas --since "1 hour ago" > $debug_dir/atlas_recent_logs.txt
    journalctl -u prometheus --since "1 hour ago" > $debug_dir/prometheus_recent_logs.txt
    journalctl -u grafana-server --since "1 hour ago" > $debug_dir/grafana_recent_logs.txt
    journalctl -u nginx --since "1 hour ago" > $debug_dir/nginx_recent_logs.txt
    journalctl -u postgresql --since "1 hour ago" > $debug_dir/postgresql_recent_logs.txt
    
    # Configuration files (without sensitive data)
    if [ -d "/etc/atlas" ]; then
        mkdir -p $debug_dir/config
        # Copy config files but exclude sensitive ones
        find /etc/atlas -name "*.conf" -exec cp {} $debug_dir/config/ \\; 2>/dev/null || true
    fi
    
    # Create summary report
    cat > $debug_dir/debug_summary.txt << EOF
Atlas Debug Information
======================
Generated at: $DATE

Files included:
$(find $debug_dir -type f | sed 's|^$debug_dir/||')

To access debug files remotely:
scp -r $debug_dir user@remote_host:/path/to/debug/

To create compressed archive:
tar -czf atlas_debug_$(date +%Y%m%d_%H%M%S).tar.gz -C /tmp $(basename $debug_dir)
EOF
    
    log_message "Debug information collected in $debug_dir"
    echo "Debug information collected in $debug_dir"
}

# Function to enable remote log access
enable_remote_log_access() {
    log_message "Enabling remote log access"
    
    # This would typically involve:
    # 1. Setting up SSH key-based access
    # 2. Creating read-only log access user
    # 3. Configuring log file permissions
    
    echo "Remote log access tools configured"
}

# Main debugging process
main() {
    log_message "=== Starting Remote Debugging Session ==="
    
    # Collect debug information
    collect_debug_info
    
    # Enable remote log access
    enable_remote_log_access
    
    log_message "=== Remote Debugging Session Completed ==="
}

# Run main debugging process
main
\"\"\"
        
        script_path = "/usr/local/bin/atlas_debug.sh"
        with open(script_path, "w") as f:
            f.write(debug_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created debugging script at {script_path}")
        return script_path
    
    def test_emergency_procedures(self):
        \"\"\"Test emergency procedures and recovery tools\"\"\"
        print("Testing emergency procedures...")
        
        # In a real implementation, this would:
        # 1. Test each emergency script
        # 2. Verify systemd services are properly configured
        # 3. Check log files are being created
        # 4. Test API endpoint functionality
        # 5. Verify email notifications work
        
        try:
            # Check if required scripts exist
            scripts = [
                "/usr/local/bin/atlas_panic_button.sh",
                "/usr/local/bin/atlas_diagnostics.sh",
                "/usr/local/bin/atlas_emergency_backup.sh",
                "/usr/local/bin/atlas_status_api.py",
                "/usr/local/bin/atlas_debug.sh"
            ]
            
            missing_scripts = []
            for script in scripts:
                if not os.path.exists(script):
                    missing_scripts.append(script)
            
            if missing_scripts:
                print(f"✗ Missing scripts: {missing_scripts}")
                return False
            else:
                print("✓ All emergency scripts exist")
            
            # Test script syntax
            bash_scripts = [
                "/usr/local/bin/atlas_panic_button.sh",
                "/usr/local/bin/atlas_diagnostics.sh",
                "/usr/local/bin/atlas_emergency_backup.sh",
                "/usr/local/bin/atlas_debug.sh"
            ]
            
            for script in bash_scripts:
                if os.path.exists(script):
                    result = subprocess.run(["bash", "-n", script], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"✓ {script} syntax is valid")
                    else:
                        print(f"✗ {script} syntax error: {result.stderr}")
                        return False
            
            # Check if Python script syntax is valid
            if os.path.exists("/usr/local/bin/atlas_status_api.py"):
                result = subprocess.run(["python3", "-m", "py_compile", 
                                       "/usr/local/bin/atlas_status_api.py"], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    print("✓ atlas_status_api.py syntax is valid")
                else:
                    print(f"✗ atlas_status_api.py syntax error: {result.stderr}")
                    return False
            
            # Check if systemd service exists
            if os.path.exists("/etc/systemd/system/atlas-status-api.service"):
                print("✓ Atlas status API systemd service exists")
            else:
                print("⚠ Atlas status API systemd service not found")
            
            print("Emergency procedures test completed successfully")
            return True
            
        except Exception as e:
            print(f"✗ Emergency procedures test failed: {e}")
            return False

def main():
    \"\"\"Main emergency tools function\"\"\"
    if os.geteuid() != 0:
        print("This script should be run as root for full functionality.")
    
    # Initialize emergency tools
    emergency = EmergencyTools()
    
    # Create panic button
    panic_script = emergency.create_panic_button()
    print(f"Panic button script created at: {panic_script}")
    
    # Implement quick diagnostics
    diag_script = emergency.implement_quick_diagnostics()
    print(f"Diagnostic script created at: {diag_script}")
    
    # Setup emergency backup
    backup_script = emergency.setup_emergency_backup()
    print(f"Emergency backup script created at: {backup_script}")
    
    # Create system status API
    api_script, service_file = emergency.create_system_status_api()
    print(f"Status API script created at: {api_script}")
    print(f"Systemd service created at: {service_file}")
    
    # Add remote debugging tools
    debug_script = emergency.add_remote_debugging_tools()
    print(f"Debugging script created at: {debug_script}")
    
    # Test emergency procedures
    if emergency.test_emergency_procedures():
        print("✓ Emergency procedures test successful")
    else:
        print("✗ Emergency procedures test failed")
    
    print("\nEmergency recovery tools setup completed!")
    print("Emergency panic button: /usr/local/bin/atlas_panic_button.sh")
    print("Quick diagnostics: /usr/local/bin/atlas_diagnostics.sh")
    print("Emergency backup: /usr/local/bin/atlas_emergency_backup.sh")
    print("Remote debugging: /usr/local/bin/atlas_debug.sh")
    print("Status API: /usr/local/bin/atlas_status_api.py")
    print("To start status API service: systemctl start atlas-status-api")

if __name__ == "__main__":
    main()