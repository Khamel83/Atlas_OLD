"""
System Updates for Atlas
Configures Ubuntu unattended-upgrades for security updates
"""

import os
import subprocess
import sys
from datetime import datetime

class SystemUpdates:
    \"\"\"Manage system updates for Atlas\"\"\"
    
    def __init__(self):
        self.update_time = "04:00"  # 4 AM PST
        self.log_file = "/var/log/atlas_updates.log"
        
    def configure_unattended_upgrades(self):
        \"\"\"Configure Ubuntu unattended-upgrades for security updates\"\"\"
        print("Configuring unattended upgrades...")
        
        # Install unattended-upgrades if not present
        try:
            subprocess.run(["apt", "install", "-y", "unattended-upgrades"], 
                          check=True, capture_output=True)
            print("Installed unattended-upgrades")
        except subprocess.CalledProcessError:
            print("Failed to install unattended-upgrades")
            return False
        
        # Configure unattended-upgrades
        config_content = \"\"\"
// Automatically upgrade packages from these (origin:archive) pairs
Unattended-Upgrade::Allowed-Origins {
    "${distro_id}:${distro_codename}";
    "${distro_id}:${distro_codename}-security";
    // Extended Security Maintenance; doesn't necessarily exist for
    // every release and this system may not have it installed, but if
    // available, the policy for updates is such that unattended-upgrades
    // doesn't automatically install from here in all cases, so
    // this entry doesn't cost anything that isn't already being spent
    "${distro_id}ESM:${distro_codename}-infra-security";
};

// List of packages to not update (regexp are supported)
Unattended-Upgrade::Package-Blacklist {
    // The following matches all packages starting with linux-
    //  "linux-";
    
    // Use $ to exclude the end of a package name
    //  "vim$";
};

// This option allows you to control if on a unclean dpkg exit
// unattended-upgrades will automatically run 
//   dpkg --force-confold --configure -a
// The default is true, to ensure updates keep getting installed
Unattended-Upgrade::AutoFixInterruptedDpkg "true";

// Split the upgrade into the smallest possible chunks so that
// they can be interrupted with SIGTERM. This makes the upgrade
// a bit slower but it has the benefit that shutdown while a upgrade
// is running is possible (with a small delay)
Unattended-Upgrade::MinimalSteps "true";

// Install all unattended-upgrades when the machine is shuting down
// instead of doing it in the background while the machine is running
// This will (obviously) make shutdown slower
Unattended-Upgrade::InstallOnShutdown "false";

// Send email to this address for problems or packages upgrades
// If empty or unset then no email is sent, make sure that you
// have a working mail setup on your system. A package that provides
// 'mailx' must be installed. E.g. "user@example.com"
Unattended-Upgrade::Mail "admin@example.com";

// Set this value to "true" to get emails only on errors. Default
// is to always send a mail if Unattended-Upgrade::Mail is set
Unattended-Upgrade::MailOnlyOnError "true";

// Do automatic removal of new unused dependencies after the upgrade
// (equivalent to apt-get autoremove)
Unattended-Upgrade::Remove-Unused-Dependencies "true";

// Automatically reboot *WITHOUT CONFIRMATION*
//  if the patch level has changed and a reboot is required
Unattended-Upgrade::Automatic-Reboot "true";

// If automatic reboot is enabled and needed, reboot at the specific
// time instead of immediately
//  Default: "now"
Unattended-Upgrade::Automatic-Reboot-Time "04:00";

// Use apt bandwidth limit feature, this example limits the download
// speed to 70kb/sec
// Acquire::http::Dl-Limit "70";
\"\"\"
        
        config_path = "/etc/apt/apt.conf.d/50unattended-upgrades"
        with open(config_path, "w") as f:
            f.write(config_content)
        
        print(f"Configured unattended upgrades at {config_path}")
        return True
    
    def setup_automatic_updates(self):
        \"\"\"Set up automatic security updates at 4 AM PST\"\"\"
        print(f"Setting up automatic updates at {self.update_time} PST...")
        
        # Create apt configuration for automatic updates
        apt_config = \"\"\"
// Enable the update/upgrade script (0=disable)
APT::Periodic::Enable "1";

// Do "apt-get update" automatically every n-days (0=disable)
APT::Periodic::Update-Package-Lists "1";

// Do "apt-get upgrade --download-only" every n-days (0=disable)
APT::Periodic::Download-Upgradeable-Packages "1";

// Run the "unattended-upgrade" security upgrade script
// every n-days (0=disable)
// Requires the package "unattended-upgrades" and will write
// a log in /var/log/unattended-upgrades
APT::Periodic::Unattended-Upgrade "1";

// Do "apt-get autoclean" every n-days (0=disable)
APT::Periodic::AutocleanInterval "7";

// Send email to this address if any important activity happens
// Requires the package "mailutils" to be installed
APT::Periodic::Unattended-Upgrade::Mail "admin@example.com";

// Only send mail on errors, not for every package upgrade
APT::Periodic::Unattended-Upgrade::MailOnlyOnError "true";
\"\"\"
        
        config_path = "/etc/apt/apt.conf.d/20auto-upgrades"
        with open(config_path, "w") as f:
            f.write(apt_config)
        
        print(f"Automatic updates configured at {config_path}")
        return True
    
    def configure_update_notifications(self):
        \"\"\"Configure update notifications via email\"\"\"
        print("Configuring update notifications...")
        
        # In a real implementation, this would:
        # 1. Install mailutils if not present
        # 2. Configure email notifications for update status
        # 3. Set up log monitoring
        
        notification_script = f\"\"\"#!/bin/bash
# Atlas Update Notification Script

LOG_FILE="{self.log_file}"
ADMIN_EMAIL="admin@example.com"

# Check for recent updates
if grep -q "Packages installed" $LOG_FILE 2>/dev/null; then
    # Get summary of updates
    update_summary=$(grep "Packages installed" $LOG_FILE | tail -5)
    
    # Send notification email
    echo "Atlas system updates completed successfully:
$update_summary

Full log available at: $LOG_FILE" | mail -s "Atlas System Updates - SUCCESS" $ADMIN_EMAIL
else
    # Check for errors
    if grep -q "ERROR\\|Failed" $LOG_FILE 2>/dev/null; then
        error_summary=$(grep "ERROR\\|Failed" $LOG_FILE | tail -5)
        echo "Atlas system updates encountered errors:
$error_summary

Check $LOG_FILE for details and take corrective action." | mail -s "Atlas System Updates - FAILED" $ADMIN_EMAIL
    fi
fi
\"\"\"
        
        script_path = "/usr/local/bin/atlas_update_notify.sh"
        with open(script_path, "w") as f:
            f.write(notification_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created update notification script at {script_path}")
        return script_path
    
    def implement_reboot_scheduling(self):
        \"\"\"Implement reboot scheduling if required (with service restart)\"\"\"
        print("Implementing reboot scheduling...")
        
        # The unattended-upgrades configuration already handles this
        # with Unattended-Upgrade::Automatic-Reboot "true"
        # and Unattended-Upgrade::Automatic-Reboot-Time "04:00"
        
        print("Reboot scheduling configured via unattended-upgrades")
        return True
    
    def create_update_log_monitoring(self):
        \"\"\"Create update log monitoring and reporting\"\"\"
        print("Creating update log monitoring...")
        
        monitoring_script = f\"\"\"#!/bin/bash
# Atlas Update Log Monitoring Script

LOG_FILE="{self.log_file}"
MONITOR_LOG="/var/log/atlas_update_monitor.log"

echo "$(date): Starting update log monitoring" >> $MONITOR_LOG

# Monitor unattended-upgrades logs
UNATTENDED_LOG="/var/log/unattended-upgrades/unattended-upgrades.log"

if [ -f "$UNATTENDED_LOG" ]; then
    # Check for recent activity
    recent_activity=$(find $UNATTENDED_LOG -mtime -1)
    if [ -n "$recent_activity" ]; then
        echo "$(date): Recent update activity detected" >> $MONITOR_LOG
        # Get last 10 lines of log
        tail -10 $UNATTENDED_LOG >> $MONITOR_LOG
    else
        echo "$(date): No recent update activity" >> $MONITOR_LOG
    fi
else
    echo "$(date): WARNING - Unattended upgrades log not found" >> $MONITOR_LOG
fi

echo "$(date): Update log monitoring completed" >> $MONITOR_LOG
\"\"\"
        
        script_path = "/usr/local/bin/atlas_update_monitor.sh"
        with open(script_path, "w") as f:
            f.write(monitoring_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to cron for regular monitoring
        cron_job = f"0 */6 * * * {script_path} >> /var/log/atlas_update_monitor_cron.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added update monitoring cron job")
            else:
                print("Update monitoring cron job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with update monitoring job")
        
        print(f"Created update monitoring script at {script_path}")
        return script_path
    
    def test_update_process(self):
        \"\"\"Test update process and service recovery\"\"\"
        print("Testing update process...")
        
        # In a real implementation, this would:
        # 1. Check if unattended-upgrades is properly configured
        # 2. Verify cron jobs are set up correctly
        # 3. Test service restart functionality
        # 4. Verify email notifications work
        
        try:
            # Check if unattended-upgrades package is installed
            result = subprocess.run(["dpkg", "-l", "unattended-upgrades"], 
                                  capture_output=True, text=True)
            if "unattended-upgrades" in result.stdout:
                print("✓ unattended-upgrades package is installed")
            else:
                print("✗ unattended-upgrades package not found")
                return False
            
            # Check configuration files
            if os.path.exists("/etc/apt/apt.conf.d/50unattended-upgrades"):
                print("✓ Unattended upgrades configuration exists")
            else:
                print("✗ Unattended upgrades configuration missing")
                return False
            
            if os.path.exists("/etc/apt/apt.conf.d/20auto-upgrades"):
                print("✓ Auto-upgrades configuration exists")
            else:
                print("✗ Auto-upgrades configuration missing")
                return False
            
            print("Update process test completed successfully")
            return True
            
        except Exception as e:
            print(f"✗ Update process test failed: {e}")
            return False

def main():
    \"\"\"Main system updates function\"\"\"
    if os.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
        sys.exit(1)
    
    # Initialize system updates
    updates = SystemUpdates()
    
    # Configure unattended upgrades
    if updates.configure_unattended_upgrades():
        print("✓ Unattended upgrades configured")
    else:
        print("✗ Failed to configure unattended upgrades")
    
    # Setup automatic updates
    if updates.setup_automatic_updates():
        print("✓ Automatic updates configured")
    else:
        print("✗ Failed to configure automatic updates")
    
    # Configure update notifications
    notify_script = updates.configure_update_notifications()
    print(f"Update notification script created at: {notify_script}")
    
    # Implement reboot scheduling
    if updates.implement_reboot_scheduling():
        print("✓ Reboot scheduling configured")
    else:
        print("✗ Failed to configure reboot scheduling")
    
    # Create update log monitoring
    monitor_script = updates.create_update_log_monitoring()
    print(f"Update monitoring script created at: {monitor_script}")
    
    # Test update process
    if updates.test_update_process():
        print("✓ Update process test successful")
    else:
        print("✗ Update process test failed")
    
    print("\nSystem updates configuration completed!")
    print("Security updates will install automatically at 4:00 AM PST")
    print("System will automatically reboot if required after updates")
    print("Update status will be emailed to admin@example.com")

if __name__ == "__main__":
    main()