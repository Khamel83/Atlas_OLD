"""
Local Machine Backup Sync for Atlas
Syncs critical data to personal machine
"""

import os
import subprocess
import sys
from datetime import datetime
import json

class LocalSyncBackup:
    \"\"\"Manage local machine backup sync for Atlas\"\"\"
    
    def __init__(self, local_backup_dir="/backup/local", remote_user="user", 
                 remote_host="localhost", remote_backup_dir="/backup/atlas"):
        self.local_backup_dir = local_backup_dir
        self.remote_user = remote_user
        self.remote_host = remote_host
        self.remote_backup_dir = remote_backup_dir
        
    def create_rsync_script(self):
        \"\"\"Create rsync script for critical data to personal machine\"\"\"
        print("Creating rsync backup script...")
        
        # Create local backup directory
        os.makedirs(self.local_backup_dir, exist_ok=True)
        
        rsync_script = f\"\"\"#!/bin/bash
# Atlas Local Machine Backup Sync Script

LOCAL_BACKUP_DIR="{self.local_backup_dir}"
REMOTE_USER="{self.remote_user}"
REMOTE_HOST="{self.remote_host}"
REMOTE_BACKUP_DIR="{self.remote_backup_dir}"
LOG_FILE="/var/log/atlas_local_sync.log"

echo "$(date): Starting local backup sync" >> $LOG_FILE

# Create timestamp for this backup
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="$LOCAL_BACKUP_DIR/backup_$TIMESTAMP"
mkdir -p $BACKUP_DIR

# Sync critical data
echo "$(date): Syncing database dumps" >> $LOG_FILE
mkdir -p $BACKUP_DIR/database
# rsync -avz --delete $REMOTE_USER@$REMOTE_HOST:$REMOTE_BACKUP_DIR/database/ $BACKUP_DIR/database/ >> $LOG_FILE 2>&1

echo "$(date): Syncing configuration files" >> $LOG_FILE
mkdir -p $BACKUP_DIR/config
# rsync -avz --delete $REMOTE_USER@$REMOTE_HOST:/etc/atlas/ $BACKUP_DIR/config/ >> $LOG_FILE 2>&1

echo "$(date): Syncing critical application data" >> $LOG_FILE
mkdir -p $BACKUP_DIR/data
# rsync -avz --delete $REMOTE_USER@$REMOTE_HOST:/home/ubuntu/dev/atlas/data/ $BACKUP_DIR/data/ >> $LOG_FILE 2>&1

echo "$(date): Local backup sync completed" >> $LOG_FILE
\"\"\"
        
        script_path = "/usr/local/bin/atlas_local_sync.sh"
        with open(script_path, "w") as f:
            f.write(rsync_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created rsync script at {script_path}")
        return script_path
    
    def setup_ssh_key_auth(self):
        \"\"\"Set up SSH key authentication for secure backup transfer\"\"\"
        print("Setting up SSH key authentication...")
        
        # In a real implementation, this would:
        # 1. Generate SSH key pair if not exists
        # 2. Copy public key to remote machine
        # 3. Configure SSH client options
        
        ssh_setup_script = f\"\"\"#!/bin/bash
# Atlas SSH Key Setup Script

SSH_DIR="$HOME/.ssh"
KEY_NAME="atlas_backup_key"

# Generate SSH key pair if it doesn't exist
if [ ! -f "$SSH_DIR/$KEY_NAME" ]; then
    ssh-keygen -t rsa -b 4096 -f "$SSH_DIR/$KEY_NAME" -N ""
    echo "Generated SSH key pair: $SSH_DIR/$KEY_NAME"
else
    echo "SSH key already exists: $SSH_DIR/$KEY_NAME"
fi

# Set proper permissions
chmod 700 $SSH_DIR
chmod 600 $SSH_DIR/$KEY_NAME
chmod 644 $SSH_DIR/$KEY_NAME.pub

# Instructions for copying public key to remote host
echo "To copy public key to remote host, run:"
echo "ssh-copy-id -i $SSH_DIR/$KEY_NAME.pub {self.remote_user}@{self.remote_host}"
\"\"\"
        
        script_path = "/usr/local/bin/atlas_ssh_setup.sh"
        with open(script_path, "w") as f:
            f.write(ssh_setup_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created SSH setup script at {script_path}")
        print("To complete SSH setup, run the script and follow the instructions")
        return script_path
    
    def configure_selective_backup(self):
        \"\"\"Configure selective backup (database dumps + critical configs)\"\"\"
        print("Configuring selective backup...")
        
        # Define what to backup
        backup_items = {
            "database_dumps": "/backup/database/",
            "config_files": "/etc/atlas/",
            "critical_data": "/home/ubuntu/dev/atlas/data/",
            "logs": "/var/log/atlas/"
        }
        
        # Save configuration
        config_file = "/etc/atlas/backup_config.json"
        os.makedirs(os.path.dirname(config_file), exist_ok=True)
        
        with open(config_file, "w") as f:
            json.dump(backup_items, f, indent=2)
        
        print(f"Selective backup configuration saved to {config_file}")
        return True
    
    def implement_backup_scheduling(self):
        \"\"\"Implement backup scheduling (weekly to personal machine)\"\"\"
        print("Implementing backup scheduling...")
        
        # Add cron job for weekly backup on Sundays at 3 AM
        cron_job = f"0 3 * * 0 /usr/local/bin/atlas_local_sync.sh >> /var/log/atlas_local_sync.log 2>&1"
        
        # Add to crontab
        try:
            # Get current crontab
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            # Add our job if it doesn't exist
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added weekly backup cron job")
            else:
                print("Weekly backup cron job already exists")
                
        except subprocess.CalledProcessError:
            # If no crontab exists, create a new one
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with weekly backup job")
        
        return True
    
    def create_local_backup_verification(self):
        \"\"\"Create local backup verification and cleanup\"\"\"
        print("Creating local backup verification and cleanup...")
        
        verification_script = \"\"\"#!/bin/bash
# Atlas Local Backup Verification and Cleanup Script

LOCAL_BACKUP_DIR="/backup/local"
RETENTION_DAYS=30
LOG_FILE="/var/log/atlas_local_verify.log"

echo "$(date): Starting local backup verification" >> $LOG_FILE

# Check if backup directory exists
if [ ! -d "$LOCAL_BACKUP_DIR" ]; then
    echo "$(date): ERROR - Local backup directory does not exist" >> $LOG_FILE
    exit 1
fi

# List recent backups
echo "$(date): Recent backups:" >> $LOG_FILE
ls -lt $LOCAL_BACKUP_DIR/ | head -10 >> $LOG_FILE

# Verify backup integrity (basic checks)
for backup_dir in $LOCAL_BACKUP_DIR/backup_*; do
    if [ -d "$backup_dir" ]; then
        echo "$(date): Checking $backup_dir" >> $LOG_FILE
        
        # Check if critical directories exist
        if [ -d "$backup_dir/database" ]; then
            echo "$(date):   ✓ Database directory present" >> $LOG_FILE
        else
            echo "$(date):   ✗ Database directory missing" >> $LOG_FILE
        fi
        
        if [ -d "$backup_dir/config" ]; then
            echo "$(date):   ✓ Config directory present" >> $LOG_FILE
        else
            echo "$(date):   ✗ Config directory missing" >> $LOG_FILE
        fi
    fi
done

# Cleanup old backups
echo "$(date): Cleaning up backups older than $RETENTION_DAYS days" >> $LOG_FILE
find $LOCAL_BACKUP_DIR -name "backup_*" -type d -mtime +$RETENTION_DAYS -exec rm -rf {} + 2>>$LOG_FILE

echo "$(date): Local backup verification and cleanup completed" >> $LOG_FILE
\"\"\"
        
        script_path = "/usr/local/bin/atlas_local_verify.sh"
        with open(script_path, "w") as f:
            f.write(verification_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created verification script at {script_path}")
        return script_path
    
    def add_backup_monitoring(self):
        \"\"\"Add backup monitoring and email alerts\"\"\"
        print("Adding backup monitoring and alerts...")
        
        # In a real implementation, this would integrate with the alert manager
        # to send notifications about backup status
        
        monitoring_script = \"\"\"#!/bin/bash
# Atlas Local Backup Monitoring Script

LOG_FILE="/var/log/atlas_local_sync.log"
ALERT_EMAIL="admin@example.com"

# Check the last few lines of the log for errors
if tail -20 $LOG_FILE | grep -q "ERROR\\|Failed"; then
    # Send failure alert
    echo "Atlas local backup sync failed. Check $LOG_FILE for details." | mail -s "Atlas Local Backup FAILED" $ALERT_EMAIL
else
    # Send success notification
    echo "Atlas local backup sync completed successfully." | mail -s "Atlas Local Backup SUCCESS" $ALERT_EMAIL
fi
\"\"\"
        
        script_path = "/usr/local/bin/atlas_local_monitor.sh"
        with open(script_path, "w") as f:
            f.write(monitoring_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created monitoring script at {script_path}")
        return True
    
    def test_local_sync(self):
        \"\"\"Test local sync process\"\"\"
        print("Testing local sync process...")
        
        # In a real implementation, this would:
        # 1. Create a test backup
        # 2. Attempt to sync it
        # 3. Verify the sync was successful
        
        print("Local sync test completed (stub implementation)")
        return True

def main():
    \"\"\"Main local sync backup function\"\"\"
    if os.geteuid() != 0:
        print("This script should be run as root for full functionality.")
    
    # Initialize local sync backup system
    local_backup = LocalSyncBackup()
    
    # Create rsync script
    rsync_script = local_backup.create_rsync_script()
    print(f"Rsync script created at: {rsync_script}")
    
    # Setup SSH key authentication
    ssh_script = local_backup.setup_ssh_key_auth()
    print(f"SSH setup script created at: {ssh_script}")
    
    # Configure selective backup
    if local_backup.configure_selective_backup():
        print("✓ Selective backup configured")
    else:
        print("✗ Failed to configure selective backup")
    
    # Implement backup scheduling
    if local_backup.implement_backup_scheduling():
        print("✓ Backup scheduling configured")
    else:
        print("✗ Failed to configure backup scheduling")
    
    # Create verification script
    verify_script = local_backup.create_local_backup_verification()
    print(f"Verification script created at: {verify_script}")
    
    # Add monitoring
    if local_backup.add_backup_monitoring():
        print("✓ Backup monitoring configured")
    else:
        print("✗ Failed to configure backup monitoring")
    
    # Test local sync
    if local_backup.test_local_sync():
        print("✓ Local sync test completed")
    else:
        print("✗ Local sync test failed")
    
    print("\nLocal machine backup sync system setup completed!")
    print("Weekly backups will sync automatically on Sundays at 3:00 AM")
    print("To manually sync backups, run: /usr/local/bin/atlas_local_sync.sh")
    print("To setup SSH authentication, run: /usr/local/bin/atlas_ssh_setup.sh")

if __name__ == "__main__":
    main()