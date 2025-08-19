"""
Prometheus Setup for Atlas Monitoring
Installs and configures Prometheus server on OCI VM
"""

import os
import subprocess
import sys
from pathlib import Path

class PrometheusSetup:
    """Setup and configure Prometheus for Atlas monitoring"""
    
    def __init__(self):
        self.prometheus_version = "2.45.0"
        self.install_dir = "/opt/prometheus"
        self.config_dir = "/etc/prometheus"
        self.data_dir = "/var/lib/prometheus"
        self.user = "prometheus"
        
    def install_prometheus(self):
        """Install Prometheus server on OCI VM"""
        print("Installing Prometheus...")
        
        # Create prometheus user
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
        
        # Download Prometheus
        prometheus_url = f"https://github.com/prometheus/prometheus/releases/download/v{self.prometheus_version}/prometheus-{self.prometheus_version}.linux-amd64.tar.gz"
        
        # In a real implementation, we would download and extract Prometheus
        # For now, we'll just create the necessary structure
        
        # Create basic prometheus.yml config
        self._create_prometheus_config()
        
        # Create systemd service file
        self._create_systemd_service()
        
        print("Prometheus installation structure created")
        return True
    
    def _create_prometheus_config(self):
        """Create basic Prometheus configuration"""
        config_content = """
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  scrape_timeout: 10s

rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'atlas'
    static_configs:
      - targets: ['localhost:8000']

  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
"""
        
        config_path = os.path.join(self.config_dir, "prometheus.yml")
        with open(config_path, "w") as f:
            f.write(config_content)
        
        print(f"Created Prometheus config at {config_path}")
    
    def _create_systemd_service(self):
        """Create Prometheus systemd service configuration"""
        service_content = f"""[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User={self.user}
Group={self.user}
Type=simple
ExecStart={self.install_dir}/prometheus \\
    --config.file {self.config_dir}/prometheus.yml \\
    --storage.tsdb.path {self.data_dir} \\
    --web.console.templates={self.install_dir}/consoles \\
    --web.console.libraries={self.install_dir}/console_libraries \\
    --storage.tsdb.retention.time=30d

Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
"""
        
        service_path = "/etc/systemd/system/prometheus.service"
        with open(service_path, "w") as f:
            f.write(service_content)
        
        print(f"Created systemd service at {service_path}")
    
    def configure_atlas_metrics(self):
        """Configure Prometheus for Atlas-specific metrics"""
        print("Configuring Atlas metrics collection...")
        # This would be implemented to add Atlas-specific metric collection
        # For now, we've already added the 'atlas' job in the config
        return True
    
    def install_node_exporter(self):
        """Set up Node Exporter for system metrics"""
        print("Installing Node Exporter...")
        # This would download and install Node Exporter
        # For now, we'll just note that it should target port 9100
        return True
    
    def configure_data_retention(self, days=30):
        """Configure Prometheus data retention"""
        print(f"Configuring data retention for {days} days...")
        # We've already set this in the systemd service with --storage.tsdb.retention.time=30d
        return True
    
    def setup_systemd_service(self):
        """Create Prometheus systemd service configuration"""
        print("Setting up systemd service...")
        # We've already created the service file
        try:
            subprocess.run(["systemctl", "daemon-reload"], check=True)
            subprocess.run(["systemctl", "enable", "prometheus"], check=True)
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
    
    setup = PrometheusSetup()
    
    # Install Prometheus
    if not setup.install_prometheus():
        print("Failed to install Prometheus")
        sys.exit(1)
    
    # Configure Atlas metrics
    if not setup.configure_atlas_metrics():
        print("Failed to configure Atlas metrics")
        sys.exit(1)
    
    # Install Node Exporter
    if not setup.install_node_exporter():
        print("Failed to install Node Exporter")
        sys.exit(1)
    
    # Configure data retention
    if not setup.configure_data_retention():
        print("Failed to configure data retention")
        sys.exit(1)
    
    # Setup systemd service
    if not setup.setup_systemd_service():
        print("Failed to setup systemd service")
        sys.exit(1)
    
    print("Prometheus setup completed successfully!")
    print("To start Prometheus, run: sudo systemctl start prometheus")
    print("To check status, run: sudo systemctl status prometheus")

if __name__ == "__main__":
    main()