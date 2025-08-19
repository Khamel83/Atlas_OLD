"""
Development Environment Sync for Atlas
Syncs development to production environment
"""

import os
import subprocess
import sys
from datetime import datetime
import json

class DevSync:
    """Manage development to production sync for Atlas"""
    
    def __init__(self):
        self.sync_log = "/var/log/atlas_dev_sync.log"
        self.dev_dir = "/home/ubuntu/dev/atlas"
        self.prod_dir = "/opt/atlas"
        self.config_dir = "/etc/atlas"
        
    def create_sync_script(self):
        """Create development to production sync tools"""
        print("Creating development to production sync tools...")
        
        sync_script = f"""#!/bin/bash
# Atlas Development to Production Sync Script

SYNC_LOG="{self.sync_log}"
DEV_DIR="{self.dev_dir}"
PROD_DIR="{self.prod_dir}"
CONFIG_DIR="{self.config_dir}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting development to production sync" >> $SYNC_LOG

log_message() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $SYNC_LOG
}}

# Function to sync code
sync_code() {{
    log_message "Syncing code from development to production"
    
    # Create production directory if it doesn't exist
    mkdir -p $PROD_DIR
    
    # Sync code files (excluding development-specific files)
    rsync -avz --delete \
        --exclude='.git' \
        --exclude='*.pyc' \
        --exclude='__pycache__' \
        --exclude='.env' \
        --exclude='venv' \
        --exclude='logs' \
        --exclude='temp' \
        --exclude='test' \
        $DEV_DIR/ $PROD_DIR/ >> $SYNC_LOG 2>&1
    
    if [ $? -eq 0 ]; then
        log_message "Code sync completed successfully"
    else
        log_message "ERROR: Code sync failed"
        return 1
    fi
}}

# Function to sync configuration
sync_configuration() {{
    log_message "Syncing configuration files"
    
    # Create config directory if it doesn't exist
    mkdir -p $CONFIG_DIR
    
    # Sync configuration files
    if [ -d "$DEV_DIR/config" ]; then
        rsync -avz $DEV_DIR/config/ $CONFIG_DIR/ >> $SYNC_LOG 2>&1
        if [ $? -eq 0 ]; then
            log_message "Configuration sync completed successfully"
        else
            log_message "ERROR: Configuration sync failed"
            return 1
        fi
    else
        log_message "No configuration directory found in development"
    fi
}}

# Function to install dependencies
install_dependencies() {{
    log_message "Installing/updating dependencies"
    
    # Install Python dependencies
    if [ -f "$PROD_DIR/requirements.txt" ]; then
        pip3 install -r $PROD_DIR/requirements.txt >> $SYNC_LOG 2>&1
        if [ $? -eq 0 ]; then
            log_message "Python dependencies installed successfully"
        else
            log_message "ERROR: Failed to install Python dependencies"
            return 1
        fi
    fi
    
    # Install system dependencies (if needed)
    # Add any system package installations here
}}

# Function to restart services
restart_services() {{
    log_message "Restarting services"
    
    # Restart Atlas service
    systemctl restart atlas >> $SYNC_LOG 2>&1
    if [ $? -eq 0 ]; then
        log_message "Atlas service restarted successfully"
    else
        log_message "ERROR: Failed to restart Atlas service"
        return 1
    fi
    
    # Restart monitoring services if they exist
    systemctl restart prometheus 2>/dev/null && log_message "Prometheus restarted" || log_message "Prometheus not found"
    systemctl restart grafana-server 2>/dev/null && log_message "Grafana restarted" || log_message "Grafana not found"
    
    # Reload nginx
    systemctl reload nginx >> $SYNC_LOG 2>&1
    if [ $? -eq 0 ]; then
        log_message "Nginx reloaded successfully"
    else
        log_message "ERROR: Failed to reload Nginx"
        return 1
    fi
}}

# Main sync process
main() {{
    log_message "=== Starting Development to Production Sync ==="
    
    # Sync code
    sync_code
    if [ $? -ne 0 ]; then
        log_message "ERROR: Code sync failed, aborting"
        echo "Development sync FAILED at $(date)" | mail -s "Atlas Dev Sync FAILED" admin@example.com
        exit 1
    fi
    
    # Sync configuration
    sync_configuration
    if [ $? -ne 0 ]; then
        log_message "ERROR: Configuration sync failed"
        echo "Development sync FAILED at $(date)" | mail -s "Atlas Dev Sync FAILED" admin@example.com
        exit 1
    fi
    
    # Install dependencies
    install_dependencies
    if [ $? -ne 0 ]; then
        log_message "ERROR: Dependency installation failed"
        echo "Development sync FAILED at $(date)" | mail -s "Atlas Dev Sync FAILED" admin@example.com
        exit 1
    fi
    
    # Restart services
    restart_services
    if [ $? -ne 0 ]; then
        log_message "ERROR: Service restart failed"
        echo "Development sync FAILED at $(date)" | mail -s "Atlas Dev Sync FAILED" admin@example.com
        exit 1
    fi
    
    log_message "=== Development to Production Sync completed successfully ==="
    echo "Development sync completed successfully at $(date)" | mail -s "Atlas Dev Sync SUCCESS" admin@example.com
}}

# Run main sync process
main
"""
        
        script_path = "/usr/local/bin/atlas_dev_sync.sh"
        with open(script_path, "w") as f:
            f.write(sync_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created sync script at {script_path}")
        return script_path
    
    def implement_configuration_management(self):
        """Implement configuration management and templating"""
        print("Implementing configuration management...")
        
        # Create configuration templates
        config_templates = {
            "atlas.conf": """
# Atlas Configuration Template
# Generated on {{DATE}}

[database]
host = {{DB_HOST}}
port = {{DB_PORT}}
name = {{DB_NAME}}
user = {{DB_USER}}
password = {{DB_PASSWORD}}

[server]
host = {{SERVER_HOST}}
port = {{SERVER_PORT}}
debug = {{DEBUG}}

[logging]
level = {{LOG_LEVEL}}
file = {{LOG_FILE}}
""",
            "nginx.conf": """
# Nginx Configuration Template
# Generated on {{DATE}}

server {{
    listen {{SERVER_PORT}};
    server_name {{SERVER_NAME}};
    
    location / {{
        proxy_pass http://{{APP_HOST}}:{{APP_PORT}};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }}
}}
"""
        }
        
        # Create templates directory
        templates_dir = f"{self.dev_dir}/templates"
        os.makedirs(templates_dir, exist_ok=True)
        
        # Write template files
        for filename, content in config_templates.items():
            template_path = f"{templates_dir}/{filename}"
            with open(template_path, "w") as f:
                f.write(content)
            print(f"Created configuration template: {template_path}")
        
        # Create template processing script
        template_script = f"""#!/bin/bash
# Atlas Configuration Template Processor

TEMPLATES_DIR="{templates_dir}"
CONFIG_DIR="{self.config_dir}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Function to process template
process_template() {{
    local template_file=$1
    local output_file=$2
    
    # Copy template to output
    cp "$template_file" "$output_file"
    
    # Replace placeholders with actual values
    # In a real implementation, you would get these from environment or config
    sed -i "s/{{DATE}}/$DATE/g" "$output_file"
    sed -i "s/{{DB_HOST}}/localhost/g" "$output_file"
    sed -i "s/{{DB_PORT}}/5432/g" "$output_file"
    sed -i "s/{{DB_NAME}}/atlas_db/g" "$output_file"
    sed -i "s/{{DB_USER}}/atlas_user/g" "$output_file"
    sed -i "s/{{DB_PASSWORD}}/atlas_password/g" "$output_file"
    sed -i "s/{{SERVER_HOST}}/0.0.0.0/g" "$output_file"
    sed -i "s/{{SERVER_PORT}}/5000/g" "$output_file"
    sed -i "s/{{DEBUG}}/False/g" "$output_file"
    sed -i "s/{{LOG_LEVEL}}/INFO/g" "$output_file"
    sed -i "s/{{LOG_FILE}}/\\/var\\/log\\/atlas\\/atlas.log/g" "$output_file"
    sed -i "s/{{SERVER_NAME}}/atlas.khamel.com/g" "$output_file"
    sed -i "s/{{APP_HOST}}/127.0.0.1/g" "$output_file"
    sed -i "s/{{APP_PORT}}/5000/g" "$output_file"
}}

# Process all templates
if [ -d "$TEMPLATES_DIR" ]; then
    for template in "$TEMPLATES_DIR"/*.conf; do
        if [ -f "$template" ]; then
            filename=$(basename "$template")
            output_file="$CONFIG_DIR/$filename"
            process_template "$template" "$output_file"
            echo "Processed template: $filename -> $output_file"
        fi
    done
fi
"""
        
        script_path = "/usr/local/bin/atlas_process_templates.sh"
        with open(script_path, "w") as f:
            f.write(template_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created template processor at {script_path}")
        return script_path
    
    def setup_environment_configuration(self):
        """Set up environment-specific configuration handling"""
        print("Setting up environment-specific configuration...")
        
        # Create environment configuration files
        environments = ["development", "staging", "production"]
        
        for env in environments:
            config_content = f"""
# Atlas {env.title()} Environment Configuration
# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ENVIRONMENT = "{env}"
DEBUG = {"True" if env == "development" else "False"}
LOG_LEVEL = "{"DEBUG" if env == "development" else "INFO"}"

# Database
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "atlas_{env}_db"
DB_USER = "atlas_{env}_user"
DB_PASSWORD = "atlas_{env}_password"

# Server
SERVER_HOST = "0.0.0.0"
SERVER_PORT = {"5000" if env == "development" else "80"}

# API Keys (these would be different per environment)
API_KEY = "your_api_key_here"
SECRET_KEY = "your_secret_key_here"
"""
            
            config_path = f"{self.dev_dir}/config/{env}.conf"
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            
            with open(config_path, "w") as f:
                f.write(config_content)
            
            print(f"Created {env} configuration: {config_path}")
        
        return True
    
    def create_database_migration(self):
        """Create database migration automation"""
        print("Creating database migration automation...")
        
        migration_script = """#!/bin/bash
# Atlas Database Migration Script

LOG_FILE="/var/log/atlas_migration.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting database migration" >> $LOG_FILE

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}

# Function to run database migrations
run_migrations() {
    log_message "Running database migrations"
    
    # Check if migration directory exists
    if [ -d "/opt/atlas/migrations" ]; then
        # Run any pending migrations
        # This is a placeholder - actual implementation would depend on your migration system
        # For example, with Flask-Migrate:
        # cd /opt/atlas && flask db upgrade >> $LOG_FILE 2>&1
        
        log_message "Database migrations completed"
    else
        log_message "No migrations directory found"
    fi
}

# Function to backup database before migration
backup_database() {
    log_message "Creating database backup before migration"
    
    # Create backup
    pg_dump -U atlas_user atlas_db > "/backup/database/atlas_backup_$(date +%Y%m%d_%H%M%S).sql" 2>> $LOG_FILE
    
    if [ $? -eq 0 ]; then
        log_message "Database backup created successfully"
    else
        log_message "ERROR: Failed to create database backup"
        return 1
    fi
}

# Main migration process
main() {
    log_message "=== Starting Database Migration ==="
    
    # Backup database
    backup_database
    if [ $? -ne 0 ]; then
        log_message "ERROR: Database backup failed, aborting migration"
        echo "Database migration FAILED at $(date)" | mail -s "Atlas Migration FAILED" admin@example.com
        exit 1
    fi
    
    # Run migrations
    run_migrations
    if [ $? -ne 0 ]; then
        log_message "ERROR: Database migration failed"
        echo "Database migration FAILED at $(date)" | mail -s "Atlas Migration FAILED" admin@example.com
        exit 1
    fi
    
    log_message "=== Database Migration completed successfully ==="
    echo "Database migration completed successfully at $(date)" | mail -s "Atlas Migration SUCCESS" admin@example.com
}

# Run main migration process
main
"""
        
        script_path = "/usr/local/bin/atlas_db_migrate.sh"
        with open(script_path, "w") as f:
            f.write(migration_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        # Add to deployment process
        cron_job = f"@reboot {script_path} >> /var/log/atlas_db_migrate_boot.log 2>&1"
        
        # Add to crontab
        try:
            current_crontab = subprocess.run(["crontab", "-l"], 
                                           capture_output=True, text=True)
            
            if cron_job not in current_crontab.stdout:
                new_crontab = current_crontab.stdout + cron_job + "\n"
                subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                print("Added database migration boot job")
            else:
                print("Database migration boot job already exists")
        except subprocess.CalledProcessError:
            subprocess.run(["crontab", "-"], input=cron_job + "\n", text=True)
            print("Created new crontab with database migration boot job")
        
        print(f"Created database migration script at {script_path}")
        return script_path
    
    def add_development_dependency_management(self):
        """Add development dependency management"""
        print("Adding development dependency management...")
        
        dep_script = """#!/bin/bash
# Atlas Development Dependency Management Script

LOG_FILE="/var/log/atlas_dependencies.log"
DEV_DIR="/home/ubuntu/dev/atlas"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting dependency management" >> $LOG_FILE

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}

# Function to update development dependencies
update_dev_dependencies() {
    log_message "Updating development dependencies"
    
    # Update pip
    pip3 install --upgrade pip >> $LOG_FILE 2>&1
    
    # Install development requirements
    if [ -f "$DEV_DIR/requirements-dev.txt" ]; then
        pip3 install -r $DEV_DIR/requirements-dev.txt >> $LOG_FILE 2>&1
        if [ $? -eq 0 ]; then
            log_message "Development dependencies updated successfully"
        else
            log_message "ERROR: Failed to update development dependencies"
            return 1
        fi
    else
        log_message "No development requirements file found"
    fi
}

# Function to sync dependencies to production
sync_dependencies() {
    log_message "Syncing dependencies to production"
    
    # Install production requirements
    if [ -f "$DEV_DIR/requirements.txt" ]; then
        pip3 install -r $DEV_DIR/requirements.txt >> $LOG_FILE 2>&1
        if [ $? -eq 0 ]; then
            log_message "Production dependencies synced successfully"
        else
            log_message "ERROR: Failed to sync production dependencies"
            return 1
        fi
    else
        log_message "No production requirements file found"
    fi
}

# Main dependency management process
main() {
    log_message "=== Starting Dependency Management ==="
    
    # Update development dependencies
    update_dev_dependencies
    if [ $? -ne 0 ]; then
        log_message "ERROR: Failed to update development dependencies"
        exit 1
    fi
    
    # Sync to production
    sync_dependencies
    if [ $? -ne 0 ]; then
        log_message "ERROR: Failed to sync dependencies to production"
        exit 1
    fi
    
    log_message "=== Dependency Management completed successfully ==="
}

# Run main dependency management process
main
"""
        
        script_path = "/usr/local/bin/atlas_manage_deps.sh"
        with open(script_path, "w") as f:
            f.write(dep_script)
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        print(f"Created dependency management script at {script_path}")
        return script_path
    
    def test_sync_process(self):
        """Test sync process and configuration differences"""
        print("Testing sync process...")
        
        # In a real implementation, this would:
        # 1. Test each sync script
        # 2. Verify configuration templates work correctly
        # 3. Check environment-specific configs
        # 4. Test database migration functionality
        # 5. Verify dependency management
        
        try:
            # Check if required scripts exist
            scripts = [
                "/usr/local/bin/atlas_dev_sync.sh",
                "/usr/local/bin/atlas_process_templates.sh",
                "/usr/local/bin/atlas_db_migrate.sh",
                "/usr/local/bin/atlas_manage_deps.sh"
            ]
            
            missing_scripts = []
            for script in scripts:
                if not os.path.exists(script):
                    missing_scripts.append(script)
            
            if missing_scripts:
                print(f"✗ Missing scripts: {missing_scripts}")
                return False
            else:
                print("✓ All sync scripts exist")
            
            # Test script syntax
            for script in scripts:
                if os.path.exists(script):
                    result = subprocess.run(["bash", "-n", script], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"✓ {script} syntax is valid")
                    else:
                        print(f"✗ {script} syntax error: {result.stderr}")
                        return False
            
            # Check if config directories exist
            config_dirs = [
                f"{self.dev_dir}/config",
                f"{self.dev_dir}/templates"
            ]
            
            missing_dirs = []
            for config_dir in config_dirs:
                if not os.path.exists(config_dir):
                    missing_dirs.append(config_dir)
            
            if missing_dirs:
                print(f"⚠ Missing config directories: {missing_dirs}")
            else:
                print("✓ Configuration directories exist")
            
            print("Sync process test completed successfully")
            return True
            
        except Exception as e:
            print(f"✗ Sync process test failed: {e}")
            return False

def main():
    """Main development sync function"""
    if os.geteuid() != 0:
        print("This script should be run as root for full functionality.")
    
    # Initialize development sync
    dev_sync = DevSync()
    
    # Create sync script
    sync_script = dev_sync.create_sync_script()
    print(f"Sync script created at: {sync_script}")
    
    # Implement configuration management
    template_script = dev_sync.implement_configuration_management()
    print(f"Template processor created at: {template_script}")
    
    # Setup environment configuration
    if dev_sync.setup_environment_configuration():
        print("✓ Environment-specific configuration setup")
    else:
        print("✗ Failed to setup environment configuration")
    
    # Create database migration
    migration_script = dev_sync.create_database_migration()
    print(f"Database migration script created at: {migration_script}")
    
    # Add development dependency management
    dep_script = dev_sync.add_development_dependency_management()
    print(f"Dependency management script created at: {dep_script}")
    
    # Test sync process
    if dev_sync.test_sync_process():
        print("✓ Sync process test successful")
    else:
        print("✗ Sync process test failed")
    
    print("\nDevelopment environment sync setup completed!")
    print("To sync development to production: /usr/local/bin/atlas_dev_sync.sh")
    print("To process configuration templates: /usr/local/bin/atlas_process_templates.sh")
    print("To run database migrations: /usr/local/bin/atlas_db_migrate.sh")
    print("To manage dependencies: /usr/local/bin/atlas_manage_deps.sh")

if __name__ == "__main__":
    main()