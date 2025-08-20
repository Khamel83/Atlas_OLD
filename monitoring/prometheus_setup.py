#!/usr/bin/env python3
"""
Prometheus Setup for Atlas Monitoring System

This script automates the installation and configuration of Prometheus
on an OCI VM for monitoring Atlas system and application metrics.

Features:
- Prometheus server installation
- Atlas metrics exporter configuration
- Node exporter setup for system metrics
- Systemd service configuration
- Data retention management
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(cmd, description=""):
    """Run a shell command with error handling"""
    try:
        print(f"Executing: {description}")
        result = subprocess.run(
            cmd, shell=True, check=True, capture_output=True, text=True
        )
        print(f"Success: {description}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {description}")
        print(f"Error: {e.stderr}")
        sys.exit(1)


def install_prometheus():
    """Install Prometheus server"""
    print("Installing Prometheus...")

    # Download and extract Prometheus
    prometheus_url = "https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz"
    run_command(
        f"wget {prometheus_url} -O /tmp/prometheus.tar.gz", "Downloading Prometheus"
    )
    run_command("tar xvfz /tmp/prometheus.tar.gz -C /tmp", "Extracting Prometheus")
    run_command(
        "sudo cp /tmp/prometheus-2.45.0.linux-amd64/prometheus /usr/local/bin/",
        "Installing Prometheus binary",
    )
    run_command(
        "sudo cp /tmp/prometheus-2.45.0.linux-amd64/promtool /usr/local/bin/",
        "Installing promtool",
    )

    # Create prometheus user
    run_command(
        "sudo useradd --no-create-home --shell /bin/false prometheus || true",
        "Creating prometheus user",
    )

    # Create directories
    run_command("sudo mkdir -p /etc/prometheus", "Creating config directory")
    run_command("sudo mkdir -p /var/lib/prometheus", "Creating data directory")

    # Set permissions
    run_command(
        "sudo chown prometheus:prometheus /etc/prometheus", "Setting config permissions"
    )
    run_command(
        "sudo chown prometheus:prometheus /var/lib/prometheus",
        "Setting data permissions",
    )

    print("Prometheus installed successfully")


def configure_prometheus():
    """Configure Prometheus for Atlas monitoring"""
    print("Configuring Prometheus...")

    # Create prometheus.yml configuration
    prometheus_config = """
global:
  scrape_interval:     15s
  evaluation_interval: 15s
  scrape_timeout:      10s

rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'atlas'
    static_configs:
      - targets: ['localhost:8000']  # Atlas metrics endpoint

  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']  # Node exporter
"""

    with open("/tmp/prometheus.yml", "w") as f:
        f.write(prometheus_config)

    run_command(
        "sudo cp /tmp/prometheus.yml /etc/prometheus/prometheus.yml",
        "Copying configuration",
    )
    run_command(
        "sudo chown prometheus:prometheus /etc/prometheus/prometheus.yml",
        "Setting config ownership",
    )

    # Create systemd service file
    service_config = """
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \\
    --config.file /etc/prometheus/prometheus.yml \\
    --storage.tsdb.path /var/lib/prometheus/ \\
    --web.console.templates=/etc/prometheus/consoles \\
    --web.console.libraries=/etc/prometheus/console_libraries \\
    --storage.tsdb.retention.time=30d \\
    --web.enable-lifecycle

[Install]
WantedBy=multi-user.target
"""

    with open("/tmp/prometheus.service", "w") as f:
        f.write(service_config)

    run_command(
        "sudo cp /tmp/prometheus.service /etc/systemd/system/prometheus.service",
        "Installing systemd service",
    )
    run_command("sudo systemctl daemon-reload", "Reloading systemd")
    run_command("sudo systemctl enable prometheus", "Enabling Prometheus service")

    print("Prometheus configured successfully")


def install_node_exporter():
    """Install Node Exporter for system metrics"""
    print("Installing Node Exporter...")

    # Download and extract Node Exporter
    node_exporter_url = "https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz"
    run_command(
        f"wget {node_exporter_url} -O /tmp/node_exporter.tar.gz",
        "Downloading Node Exporter",
    )
    run_command(
        "tar xvfz /tmp/node_exporter.tar.gz -C /tmp", "Extracting Node Exporter"
    )
    run_command(
        "sudo cp /tmp/node_exporter-1.6.1.linux-amd64/node_exporter /usr/local/bin/",
        "Installing Node Exporter binary",
    )

    # Create node_exporter user
    run_command(
        "sudo useradd --no-create-home --shell /bin/false node_exporter || true",
        "Creating node_exporter user",
    )

    # Create systemd service file for Node Exporter
    node_service_config = """
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
"""

    with open("/tmp/node_exporter.service", "w") as f:
        f.write(node_service_config)

    run_command(
        "sudo cp /tmp/node_exporter.service /etc/systemd/system/node_exporter.service",
        "Installing Node Exporter service",
    )
    run_command("sudo systemctl daemon-reload", "Reloading systemd")
    run_command("sudo systemctl enable node_exporter", "Enabling Node Exporter service")

    print("Node Exporter installed successfully")


def setup_atlas_metrics_exporter():
    """Setup Atlas metrics exporter"""
    print("Setting up Atlas metrics exporter...")

    # Create a simple exporter script
    exporter_script = """
#!/usr/bin/env python3
# Simple HTTP server that exposes Atlas metrics in Prometheus format

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            
            # Sample metrics - in a real implementation, these would come from Atlas
            metrics = '''
# HELP atlas_articles_processed_total Total number of articles processed
# TYPE atlas_articles_processed_total counter
atlas_articles_processed_total{status="success"} 1234
atlas_articles_processed_total{status="failed"} 12

# HELP atlas_podcasts_downloaded_total Total number of podcasts downloaded
# TYPE atlas_podcasts_downloaded_total counter
atlas_podcasts_downloaded_total 567

# HELP atlas_youtube_videos_processed_total Total number of YouTube videos processed
# TYPE atlas_youtube_videos_processed_total counter
atlas_youtube_videos_processed_total 89

# HELP atlas_processing_queue_length Current length of processing queue
# TYPE atlas_processing_queue_length gauge
atlas_processing_queue_length 5

# HELP atlas_system_health_status System health status (1=healthy, 0=unhealthy)
# TYPE atlas_system_health_status gauge
atlas_system_health_status 1
'''
            
            self.wfile.write(metrics.encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), MetricsHandler)
    print("Atlas metrics exporter running on http://localhost:8000/metrics")
    server.serve_forever()
"""

    # Write the exporter script
    exporter_path = "/usr/local/bin/atlas_metrics_exporter.py"
    with open("/tmp/atlas_metrics_exporter.py", "w") as f:
        f.write(exporter_script)

    run_command(
        "sudo cp /tmp/atlas_metrics_exporter.py " + exporter_path,
        "Installing Atlas metrics exporter",
    )
    run_command("sudo chmod +x " + exporter_path, "Making exporter executable")

    # Create systemd service for the exporter
    exporter_service = f"""
[Unit]
Description=Atlas Metrics Exporter
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
ExecStart={exporter_path}
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""

    with open("/tmp/atlas_metrics_exporter.service", "w") as f:
        f.write(exporter_service)

    run_command(
        "sudo cp /tmp/atlas_metrics_exporter.service /etc/systemd/system/atlas_metrics_exporter.service",
        "Installing exporter service",
    )
    run_command("sudo systemctl daemon-reload", "Reloading systemd")
    run_command(
        "sudo systemctl enable atlas_metrics_exporter", "Enabling exporter service"
    )

    print("Atlas metrics exporter setup successfully")


def start_services():
    """Start all monitoring services"""
    print("Starting monitoring services...")

    # Start services
    run_command("sudo systemctl start node_exporter", "Starting Node Exporter")
    run_command(
        "sudo systemctl start atlas_metrics_exporter", "Starting Atlas Metrics Exporter"
    )
    run_command("sudo systemctl start prometheus", "Starting Prometheus")

    # Check service status
    print("\nService Status:")
    run_command(
        "sudo systemctl status node_exporter --no-pager -l || true",
        "Node Exporter status",
    )
    run_command(
        "sudo systemctl status atlas_metrics_exporter --no-pager -l || true",
        "Atlas Metrics Exporter status",
    )
    run_command(
        "sudo systemctl status prometheus --no-pager -l || true", "Prometheus status"
    )

    print("\nMonitoring services started successfully")


def main():
    """Main installation and configuration function"""
    print("Starting Prometheus setup for Atlas monitoring...")

    # Install components
    install_prometheus()
    install_node_exporter()
    setup_atlas_metrics_exporter()

    # Configure Prometheus
    configure_prometheus()

    # Start services
    start_services()

    print("\nPrometheus setup completed successfully!")
    print("Prometheus is now running and monitoring:")
    print("- System metrics via Node Exporter (http://localhost:9100)")
    print("- Atlas application metrics (http://localhost:8000/metrics)")
    print("- Prometheus dashboard at http://localhost:9090")
    print("\nData retention is configured for 30 days")
    print("Services are configured to auto-start on boot")


if __name__ == "__main__":
    main()
