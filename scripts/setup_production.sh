#!/bin/bash

# Atlas Production Setup Script
# This script sets up Atlas for production use with all necessary services and configurations

set -e  # Exit on any error

echo "Setting up Atlas for production..."

# Update system packages
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install required packages
echo "Installing required packages..."
sudo apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    postgresql \
    postgresql-contrib \
    nginx \
    certbot \
    python3-certbot-nginx \
    prometheus \
    grafana \
    node-exporter \
    unattended-upgrades \
    logrotate \
    rsync \
    openssh-client \
    git

# Create Atlas user if it doesn't exist
if ! id "atlas" &>/dev/null; then
    echo "Creating atlas user..."
    sudo useradd -m -s /bin/bash atlas
fi

# Set up Python virtual environment
echo "Setting up Python virtual environment..."
cd /home/ubuntu/dev/atlas
python3 -m venv atlas_venv
source atlas_venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
echo "Creating directories..."
mkdir -p /home/ubuntu/dev/atlas/logs
mkdir -p /home/ubuntu/dev/atlas/backups
mkdir -p /home/ubuntu/dev/atlas/config

# Set up PostgreSQL database
echo "Setting up PostgreSQL database..."
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql -c "CREATE USER atlas_user WITH PASSWORD 'atlas_password';" || true
sudo -u postgres psql -c "CREATE DATABASE atlas OWNER atlas_user;" || true
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE atlas TO atlas_user;" || true

# Set up systemd services
echo "Setting up systemd services..."
sudo /home/ubuntu/dev/atlas/scripts/setup_systemd_service.sh

# Set up monitoring
echo "Setting up monitoring..."
python3 /home/ubuntu/dev/atlas/monitoring/prometheus_setup.py
python3 /home/ubuntu/dev/atlas/monitoring/grafana_config/setup.py

# Set up backup system
echo "Setting up backup system..."
python3 /home/ubuntu/dev/atlas/backup/database_backup.py

# Set up maintenance
echo "Setting up maintenance system..."
python3 /home/ubuntu/dev/atlas/maintenance/system_updates.py
python3 /home/ubuntu/dev/atlas/maintenance/atlas_maintenance.py

# Set up authentication and SSL
echo "Setting up authentication and SSL..."
# Note: This requires manual configuration of domain and email
# python3 /home/ubuntu/dev/atlas/ssl/ssl_setup.sh
# python3 /home/ubuntu/dev/atlas/auth/nginx_auth_setup.py

# Set up log rotation
echo "Setting up log rotation..."
sudo tee /etc/logrotate.d/atlas > /dev/null <<EOF
/home/ubuntu/dev/atlas/logs/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 ubuntu ubuntu
    sharedscripts
    postrotate
        systemctl reload atlas > /dev/null 2>&1 || true
    endscript
}
EOF

# Set up firewall
echo "Setting up firewall..."
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw --force enable

# Start services
echo "Starting services..."
sudo systemctl daemon-reload
sudo systemctl start atlas
sudo systemctl start atlas-prometheus
sudo systemctl start atlas-grafana
sudo systemctl start atlas-backup.timer
sudo systemctl start atlas-maintenance.timer

# Enable services to start on boot
sudo systemctl enable atlas
sudo systemctl enable atlas-prometheus
sudo systemctl enable atlas-grafana
sudo systemctl enable atlas-backup.timer
sudo systemctl enable atlas-maintenance.timer

echo "Atlas production setup completed!"
echo ""
echo "Next steps:"
echo "1. Configure domain and SSL certificates:"
echo "   - Update /home/ubuntu/dev/atlas/ssl/ssl_setup.sh with your domain"
echo "   - Run: python3 /home/ubuntu/dev/atlas/ssl/ssl_setup.sh"
echo ""
echo "2. Configure authentication:"
echo "   - Update /home/ubuntu/dev/atlas/auth/nginx_auth_setup.py with your credentials"
echo "   - Run: python3 /home/ubuntu/dev/atlas/auth/nginx_auth_setup.py"
echo ""
echo "3. Verify services are running:"
echo "   - sudo systemctl status atlas"
echo "   - sudo systemctl status atlas-prometheus"
echo "   - sudo systemctl status atlas-grafana"
echo ""
echo "4. Access the services:"
echo "   - Web interface: http://your-server-ip"
echo "   - Grafana dashboard: http://your-server-ip:3000"
echo "   - Prometheus: http://your-server-ip:9090"