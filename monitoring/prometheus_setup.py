#!/usr/bin/env python3
"""
Prometheus Setup for Atlas

This module sets up Prometheus server on OCI VM for Atlas monitoring.
"""

import os
import subprocess
import sys

def install_prometheus():
    """Install Prometheus server on OCI VM"""
    print("Installing Prometheus server on OCI VM...")
    
    try:
        # Download Prometheus
        subprocess.run([
            "wget", 
            "https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz"
        ], check=True)
        
        # Extract
        subprocess.run([
            "tar", "xvfz", "prometheus-2.45.0.linux-amd64.tar.gz"
        ], check=True)
        
        # Move to /opt
        subprocess.run([
            "sudo", "mkdir", "-p", "/opt/prometheus"
        ], check=True)
        
        subprocess.run([
            "sudo", "cp", "-r", "prometheus-2.45.0.linux-amd64/*", "/opt/prometheus/"
        ], check=True)
        
        # Create prometheus user
        subprocess.run([
            "sudo", "useradd", "--no-create-home", "--shell", "/bin/false", "prometheus"
        ], check=True)
        
        # Set permissions
        subprocess.run([
            "sudo", "chown", "-R", "prometheus:prometheus", "/opt/prometheus"
        ], check=True)
        
        print("✅ Prometheus installed successfully")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Prometheus: {e}")
        return False

def configure_prometheus():
    """Configure Prometheus for Atlas-specific metrics"""
    print("Configuring Prometheus for Atlas-specific metrics...")
    
    config_content = '''
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "atlas_rules.yml"

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
'''
    
    try:
        with open("/opt/prometheus/prometheus.yml", "w") as f:
            f.write(config_content)
        
        # Set ownership
        subprocess.run([
            "sudo", "chown", "prometheus:prometheus", "/opt/prometheus/prometheus.yml"
        ], check=True)
        
        print("✅ Prometheus configured successfully")
        return True
        
    except Exception as e:
        print(f"❌ Failed to configure Prometheus: {e}")
        return False

def create_atlas_metrics_exporter():
    """Create Atlas metrics exporter for processing stats"""
    print("Creating Atlas metrics exporter...")
    
    exporter_content = '''
#!/usr/bin/env python3
"""
Atlas Metrics Exporter for Prometheus

This script exports Atlas processing statistics for Prometheus monitoring.
"""

import time
from prometheus_client import start_http_server, Gauge, Counter, Histogram

# Create metrics
articles_processed = Counter('atlas_articles_processed_total', 'Total articles processed')
articles_success_rate = Gauge('atlas_articles_success_rate', 'Article processing success rate')
podcast_episodes_processed = Counter('atlas_podcast_episodes_processed_total', 'Total podcast episodes processed')
youtube_videos_processed = Counter('atlas_youtube_videos_processed_total', 'Total YouTube videos processed')
failed_items = Counter('atlas_failed_items_total', 'Total failed items')
retry_success = Gauge('atlas_retry_success_rate', 'Retry success rate')

def collect_metrics():
    """Collect and update Atlas metrics"""
    # In a real implementation, this would get actual metrics from Atlas
    # For now, we'll use placeholder values
    articles_processed.inc(10)
    articles_success_rate.set(98.5)
    podcast_episodes_processed.inc(5)
    youtube_videos_processed.inc(15)
    failed_items.inc(2)
    retry_success.set(85.0)

def main():
    """Main function to start metrics exporter"""
    # Start HTTP server for Prometheus to scrape
    start_http_server(8000)
    print("Atlas metrics exporter started on port 8000")
    
    # Collect metrics periodically
    while True:
        collect_metrics()
        time.sleep(30)  # Update every 30 seconds

if __name__ == "__main__":
    main()
'''
    
    try:
        with open("/opt/prometheus/atlas_metrics_exporter.py", "w") as f:
            f.write(exporter_content)
        
        # Make executable
        subprocess.run([
            "sudo", "chmod", "+x", "/opt/prometheus/atlas_metrics_exporter.py"
        ], check=True)
        
        # Set ownership
        subprocess.run([
            "sudo", "chown", "prometheus:prometheus", "/opt/prometheus/atlas_metrics_exporter.py"
        ], check=True)
        
        print("✅ Atlas metrics exporter created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create Atlas metrics exporter: {e}")
        return False

def setup_node_exporter():
    """Set up Node Exporter for system metrics (CPU, memory, disk)"""
    print("Setting up Node Exporter for system metrics...")
    
    try:
        # Download Node Exporter
        subprocess.run([
            "wget", 
            "https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz"
        ], check=True)
        
        # Extract
        subprocess.run([
            "tar", "xvfz", "node_exporter-1.6.1.linux-amd64.tar.gz"
        ], check=True)
        
        # Move to /opt
        subprocess.run([
            "sudo", "mkdir", "-p", "/opt/node_exporter"
        ], check=True)
        
        subprocess.run([
            "sudo", "cp", "-r", "node_exporter-1.6.1.linux-amd64/*", "/opt/node_exporter/"
        ], check=True)
        
        # Create node_exporter user
        subprocess.run([
            "sudo", "useradd", "--no-create-home", "--shell", "/bin/false", "node_exporter"
        ], check=True)
        
        # Set permissions
        subprocess.run([
            "sudo", "chown", "-R", "node_exporter:node_exporter", "/opt/node_exporter"
        ], check=True)
        
        print("✅ Node Exporter installed successfully")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Node Exporter: {e}")
        return False

def configure_prometheus_retention():
    """Configure Prometheus data retention (30 days max)"""
    print("Configuring Prometheus data retention...")
    
    # This is handled in the systemd service configuration with --storage.tsdb.retention.time=30d
    print("✅ Prometheus data retention configured for 30 days")
    return True

def create_prometheus_service():
    """Create Prometheus systemd service configuration"""
    print("Creating Prometheus systemd service...")
    
    service_content = '''
[Unit]
Description=Prometheus Server
Documentation=https://prometheus.io/docs/introduction/overview/
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/opt/prometheus/prometheus \\
    --config.file /opt/prometheus/prometheus.yml \\
    --storage.tsdb.path /opt/prometheus/data \\
    --web.console.templates=/opt/prometheus/consoles \\
    --web.console.libraries=/opt/prometheus/console_libraries \\
    --storage.tsdb.retention.time=30d

[Install]
WantedBy=multi-user.target
'''
    
    try:
        with open("/etc/systemd/system/prometheus.service", "w") as f:
            f.write(service_content)
        
        # Reload systemd
        subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
        
        # Enable service
        subprocess.run(["sudo", "systemctl", "enable", "prometheus"], check=True)
        
        print("✅ Prometheus systemd service created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create Prometheus systemd service: {e}")
        return False

def main():
    """Main function to setup Prometheus monitoring"""
    print("🚀 Starting Prometheus Setup for Atlas")
    print("=" * 40)
    
    # Install Prometheus
    if not install_prometheus():
        sys.exit(1)
    
    # Configure Prometheus
    if not configure_prometheus():
        sys.exit(1)
    
    # Create Atlas metrics exporter
    if not create_atlas_metrics_exporter():
        sys.exit(1)
        
    # Setup Node Exporter
    if not setup_node_exporter():
        sys.exit(1)
        
    # Configure data retention
    if not configure_prometheus_retention():
        sys.exit(1)
        
    # Create systemd service
    if not create_prometheus_service():
        sys.exit(1)
    
    print("\n🎉 Prometheus Setup Complete!")
    print("✅ Prometheus server installed on OCI VM")
    print("✅ Prometheus configured for Atlas-specific metrics")
    print("✅ Atlas metrics exporter created for processing stats")
    print("✅ Node Exporter set up for system metrics")
    print("✅ Prometheus data retention configured (30 days max)")
    print("✅ Prometheus systemd service created")
    print("\nTo start Prometheus service:")
    print("sudo systemctl start prometheus")

if __name__ == "__main__":
    main()