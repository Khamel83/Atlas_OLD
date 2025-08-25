#!/bin/bash
# Atlas Monitoring Installation Script

set -e

echo "🚀 Installing Atlas Monitoring System..."

# Create logs directory if it doesn't exist
mkdir -p logs

# Copy service files to systemd
if [ -w /etc/systemd/system ]; then
    echo "Installing systemd services..."
    sudo cp monitoring_setup/*.service /etc/systemd/system/
    sudo cp monitoring_setup/*.timer /etc/systemd/system/
    
    # Reload systemd
    sudo systemctl daemon-reload
    
    # Enable and start timers
    sudo systemctl enable atlas-health-check.timer
    sudo systemctl enable atlas-performance.timer
    sudo systemctl enable atlas-alerts.timer
    
    sudo systemctl start atlas-health-check.timer
    sudo systemctl start atlas-performance.timer
    sudo systemctl start atlas-alerts.timer
    
    echo "✅ Systemd timers installed and started"
else
    echo "⚠️  No systemd access - install services manually"
fi

# Install logrotate configuration
if [ -w /etc/logrotate.d ]; then
    sudo cp monitoring_setup/atlas-logrotate /etc/logrotate.d/
    echo "✅ Logrotate configuration installed"
fi

# Make scripts executable
chmod +x monitoring_setup/*.py

echo "🎉 Atlas Monitoring System installed successfully!"
echo ""
echo "Manual verification:"
echo "• Check health: python3 monitoring_setup/health_check.py"
echo "• Check performance: python3 monitoring_setup/performance_monitor.py"
echo "• Analyze logs: python3 monitoring_setup/log_analyzer.py"
echo "• Test alerts: python3 monitoring_setup/alert_manager.py"
echo ""
echo "Service status:"
echo "• sudo systemctl status atlas-health-check.timer"
echo "• sudo systemctl status atlas-performance.timer" 
echo "• sudo systemctl status atlas-alerts.timer"
