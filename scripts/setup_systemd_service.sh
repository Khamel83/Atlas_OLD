#!/bin/bash

# Atlas systemd service setup script
# This script creates systemd service files for Atlas components

set -e  # Exit on any error

echo "Setting up Atlas systemd services..."

# Create systemd service directory if it doesn't exist
sudo mkdir -p /etc/systemd/system

# Create main Atlas service
sudo tee /etc/systemd/system/atlas.service > /dev/null <<EOF
[Unit]
Description=Atlas Content Processing Service
After=network.target postgresql.service
Requires=postgresql.service

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/dev/atlas
ExecStart=/home/ubuntu/dev/atlas/scripts/atlas_background_service.py
Restart=always
RestartSec=10
Environment=PYTHONPATH=/home/ubuntu/dev/atlas

[Install]
WantedBy=multi-user.target
EOF

# Create Prometheus service
sudo tee /etc/systemd/system/atlas-prometheus.service > /dev/null <<EOF
[Unit]
Description=Atlas Prometheus Monitoring
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/dev/atlas
ExecStart=/home/ubuntu/dev/atlas/monitoring/prometheus_setup.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Create Grafana service
sudo tee /etc/systemd/system/atlas-grafana.service > /dev/null <<EOF
[Unit]
Description=Atlas Grafana Dashboard
After=network.target atlas-prometheus.service
Requires=atlas-prometheus.service

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/dev/atlas
ExecStart=/home/ubuntu/dev/atlas/monitoring/grafana_config/setup.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Create backup service
sudo tee /etc/systemd/system/atlas-backup.service > /dev/null <<EOF
[Unit]
Description=Atlas Backup Service
After=network.target

[Service]
Type=oneshot
User=ubuntu
WorkingDirectory=/home/ubuntu/dev/atlas
ExecStart=/home/ubuntu/dev/atlas/backup/database_backup.py
EOF

# Create backup timer (runs daily at 2 AM)
sudo tee /etc/systemd/system/atlas-backup.timer > /dev/null <<EOF
[Unit]
Description=Atlas Daily Backup Timer

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
EOF

# Create maintenance service
sudo tee /etc/systemd/system/atlas-maintenance.service > /dev/null <<EOF
[Unit]
Description=Atlas Maintenance Service
After=network.target

[Service]
Type=oneshot
User=ubuntu
WorkingDirectory=/home/ubuntu/dev/atlas
ExecStart=/home/ubuntu/dev/atlas/maintenance/atlas_maintenance.py
EOF

# Create maintenance timer (runs daily at 3 AM)
sudo tee /etc/systemd/system/atlas-maintenance.timer > /dev/null <<EOF
[Unit]
Description=Atlas Daily Maintenance Timer

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
EOF

# Reload systemd configuration
sudo systemctl daemon-reload

# Enable services
sudo systemctl enable atlas.service
sudo systemctl enable atlas-prometheus.service
sudo systemctl enable atlas-grafana.service
sudo systemctl enable atlas-backup.timer
sudo systemctl enable atlas-maintenance.timer

echo "Atlas systemd services created successfully!"
echo ""
echo "To start the services, run:"
echo "  sudo systemctl start atlas"
echo "  sudo systemctl start atlas-prometheus"
echo "  sudo systemctl start atlas-grafana"
echo "  sudo systemctl start atlas-backup.timer"
echo "  sudo systemctl start atlas-maintenance.timer"
echo ""
echo "To check service status, run:"
echo "  sudo systemctl status atlas"