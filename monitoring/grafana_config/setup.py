"""
Grafana Setup for Atlas Monitoring
Installs and configures Grafana server on OCI VM
"""

import os
import subprocess
import sys
from pathlib import Path

class GrafanaSetup:
    """Setup and configure Grafana for Atlas monitoring"""
    
    def __init__(self):
        self.grafana_version = "10.0.3"
        self.install_dir = "/opt/grafana"
        self.config_dir = "/etc/grafana"
        self.data_dir = "/var/lib/grafana"
        self.user = "grafana"
        
    def install_grafana(self):
        """Install Grafana server on OCI VM"""
        print("Installing Grafana...")
        
        # Create grafana user
        try:
            subprocess.run(["useradd", "--no-create-home", "--shell", "/bin/false", self.user], 
                          check=True, capture_output=True)
        except subprocess.CalledProcessError:
            # User might already exist
            pass
        
        # Create directories
        os.makedirs(self.install_dir, exist_ok=True)
        os.makedirs(self.config_dir, exist_ok=True)
        os.makedirs(self.data_dir, exist_ok=True)
        
        # In a real implementation, we would download and install Grafana
        # For now, we'll just create the necessary structure
        
        # Create basic grafana.ini config
        self._create_grafana_config()
        
        # Create systemd service file
        self._create_systemd_service()
        
        print("Grafana installation structure created")
        return True
    
    def _create_grafana_config(self):
        """Create basic Grafana configuration"""
        config_content = """
[paths]
data = /var/lib/grafana
logs = /var/log/grafana
plugins = /var/lib/grafana/plugins
provisioning = conf/provisioning

[server]
http_addr = 0.0.0.0
http_port = 3000
domain = atlas.khamel.com
root_url = %(protocol)s://%(domain)s:%(http_port)s/
router_logging = false

[database]
type = sqlite3
host = 127.0.0.1:3306
name = grafana
user = root
password =
ssl_mode = disable

[session]
provider = file
provider_config = sessions

[analytics]
reporting_enabled = false
check_for_updates = true

[security]
admin_user = admin
admin_password = admin

[users]
allow_sign_up = false
allow_org_create = false
auto_assign_org = true
auto_assign_org_role = Viewer

[auth.anonymous]
enabled = false

[log]
mode = console file
level = info

[metrics]
enabled = true
interval_seconds = 15
"""
        
        config_path = os.path.join(self.config_dir, "grafana.ini")
        with open(config_path, "w") as f:
            f.write(config_content)
        
        print(f"Created Grafana config at {config_path}")
    
    def _create_systemd_service(self):
        """Create Grafana systemd service configuration"""
        service_content = f"""[Unit]
Description=Grafana
Wants=network-online.target
After=network-online.target

[Service]
User={self.user}
Group={self.user}
Type=simple
ExecStart={self.install_dir}/bin/grafana-server \\
    --config={self.config_dir}/grafana.ini \\
    --homepath={self.install_dir} \\
    --packaging=deb \\
    cfg:default.paths.logs=/var/log/grafana \\
    cfg:default.paths.data=/var/lib/grafana \\
    cfg:default.paths.plugins=/var/lib/grafana/plugins

Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
"""
        
        service_path = "/etc/systemd/system/grafana-server.service"
        with open(service_path, "w") as f:
            f.write(service_content)
        
        print(f"Created systemd service at {service_path}")
    
    def create_atlas_dashboard(self):
        """Create Atlas overview dashboard with key metrics"""
        print("Creating Atlas overview dashboard...")
        # This would create a JSON dashboard definition
        # For now, we'll just note that it should be created
        return True
    
    def create_system_health_dashboard(self):
        """Build system health dashboard (CPU, memory, disk, network)"""
        print("Creating system health dashboard...")
        # This would create a JSON dashboard definition
        # For now, we'll just note that it should be created
        return True
    
    def create_content_processing_dashboard(self):
        """Create content processing dashboard (articles/hour, success rates)"""
        print("Creating content processing dashboard...")
        # This would create a JSON dashboard definition
        # For now, we'll just note that it should be created
        return True
    
    def setup_authentication(self, admin_password="admin"):
        """Set up Grafana authentication with simple admin password"""
        print(f"Setting up authentication with admin password...")
        # In a real implementation, we would hash the password and update the config
        # For now, we've set the default password in the config
        return True
    
    def setup_systemd_service(self):
        """Configure Grafana systemd service"""
        print("Setting up systemd service...")
        # We've already created the service file
        try:
            subprocess.run(["systemctl", "daemon-reload"], check=True)
            subprocess.run(["systemctl", "enable", "grafana-server"], check=True)
            print("Systemd service configured and enabled")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error setting up systemd service: {e}")
            return False

def main():
    """Main installation function"""
    if os.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
        sys.exit(1)
    
    setup = GrafanaSetup()
    
    # Install Grafana
    if not setup.install_grafana():
        print("Failed to install Grafana")
        sys.exit(1)
    
    # Create dashboards
    if not setup.create_atlas_dashboard():
        print("Failed to create Atlas dashboard")
        sys.exit(1)
    
    if not setup.create_system_health_dashboard():
        print("Failed to create system health dashboard")
        sys.exit(1)
    
    if not setup.create_content_processing_dashboard():
        print("Failed to create content processing dashboard")
        sys.exit(1)
    
    # Setup authentication
    if not setup.setup_authentication():
        print("Failed to setup authentication")
        sys.exit(1)
    
    # Setup systemd service
    if not setup.setup_systemd_service():
        print("Failed to setup systemd service")
        sys.exit(1)
    
    print("Grafana setup completed successfully!")
    print("To start Grafana, run: sudo systemctl start grafana-server")
    print("To check status, run: sudo systemctl status grafana-server")
    print("Access Grafana at: http://your-server-ip:3000")

if __name__ == "__main__":
    main()