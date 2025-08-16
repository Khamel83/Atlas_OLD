#!/bin/bash
# Setup Atlas as a systemd service for persistent operation

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVICE_FILE="$SCRIPT_DIR/atlas.service"

echo "🔧 Setting up Atlas systemd service..."

# Copy service file to systemd
sudo cp "$SERVICE_FILE" /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable service to start on boot
sudo systemctl enable atlas.service

echo "✅ Atlas systemd service setup complete!"
echo ""
echo "Commands:"
echo "  sudo systemctl start atlas     # Start service"
echo "  sudo systemctl stop atlas      # Stop service"
echo "  sudo systemctl status atlas    # Check status"
echo "  sudo systemctl restart atlas   # Restart service"
echo "  journalctl -u atlas -f         # Follow logs"
echo ""
echo "💡 The service will automatically:"
echo "  - Start on system boot"
echo "  - Restart if it crashes"
echo "  - Log to /home/ubuntu/dev/atlas/logs/"