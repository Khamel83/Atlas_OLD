#!/bin/bash

# Atlas Production Status Check
# This script checks the status of all Atlas production services and components

set -e  # Exit on any error

echo "Checking Atlas production status..."

# Function to check service status
check_service() {
    local service=$1
    local name=$2
    
    if systemctl is-active --quiet $service; then
        echo "✅ $name: Running"
        return 0
    else
        echo "❌ $name: Not running"
        return 1
    fi
}

# Function to check port availability
check_port() {
    local port=$1
    local service=$2
    
    if nc -z localhost $port; then
        echo "✅ $service: Port $port is open"
        return 0
    else
        echo "❌ $service: Port $port is closed"
        return 1
    fi
}

# Check systemd services
echo "=== Systemd Services ==="
check_service "atlas" "Atlas Main Service"
check_service "atlas-prometheus" "Prometheus Monitoring"
check_service "atlas-grafana" "Grafana Dashboard"
check_service "postgresql" "PostgreSQL Database"
check_service "nginx" "Nginx Web Server"

# Check ports
echo -e "\n=== Port Availability ==="
check_port 5000 "Atlas API"
check_port 9090 "Prometheus"
check_port 3000 "Grafana"
check_port 80 "HTTP"
check_port 443 "HTTPS"
check_port 5432 "PostgreSQL"

# Check disk space
echo -e "\n=== System Resources ==="
df -h /

# Check memory usage
free -h

# Check system load
echo "Load average: $(uptime | awk -F'load average:' '{print $2}')"

# Check recent logs
echo -e "\n=== Recent Log Entries ==="
echo "Atlas service logs (last 10 lines):"
sudo tail -10 /home/ubuntu/dev/atlas/logs/atlas_background.log 2>/dev/null || echo "No Atlas logs found"

echo -e "\n=== Database Status ==="
# Check if database is accessible
if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
    echo "✅ Database: Accessible"
    
    # Check table counts
    echo "Database table counts:"
    sudo -u postgres psql -U atlas_user -d atlas -c "SELECT schemaname,tablename,row_count FROM (SELECT schemaname,tablename,(SELECT count(*) FROM pg_class WHERE relname = tablename) AS row_count FROM pg_tables WHERE schemaname = 'public') AS tableinfo ORDER BY row_count DESC;" 2>/dev/null || echo "Could not retrieve table counts"
else
    echo "❌ Database: Not accessible"
fi

# Check backup status
echo -e "\n=== Backup Status ==="
if [ -d "/home/ubuntu/dev/atlas/backups" ]; then
    backup_count=$(ls -1 /home/ubuntu/dev/atlas/backups/*.sql.gz.enc 2>/dev/null | wc -l)
    echo "✅ Backup directory exists with $backup_count backup files"
    
    if [ $backup_count -gt 0 ]; then
        latest_backup=$(ls -t /home/ubuntu/dev/atlas/backups/*.sql.gz.enc 2>/dev/null | head -1)
        echo "Latest backup: $(basename $latest_backup)"
    fi
else
    echo "❌ Backup directory not found"
fi

# Check SSL certificate status
echo -e "\n=== SSL Certificate Status ==="
if [ -f "/etc/letsencrypt/live/atlas.khamel.com/cert.pem" ]; then
    echo "✅ SSL certificate exists"
    openssl x509 -in /etc/letsencrypt/live/atlas.khamel.com/cert.pem -noout -dates
else
    echo "⚠️  SSL certificate not found (may be using default configuration)"
fi

echo -e "\n=== Health Summary ==="
echo "Status check completed. Please review any ❌ or ⚠️  indicators above."

# Provide quick status summary
running_services=$(systemctl list-units --type=service --state=active | grep -E "(atlas|prometheus|grafana|postgresql|nginx)" | wc -l)
echo "Active Atlas-related services: $running_services"

echo -e "\nFor detailed information, check:"
echo "  - Service logs: sudo journalctl -u atlas"
echo "  - Application logs: /home/ubuntu/dev/atlas/logs/"
echo "  - Database logs: /var/log/postgresql/"