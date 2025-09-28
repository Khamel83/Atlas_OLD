#!/bin/bash
# Start Atlas monitoring service

echo "🚀 Starting Atlas monitoring service..."

# Stop any existing monitoring
pkill -f monitor_atlas.sh || true
pkill -f atlas_manager.py || true

# Start monitoring in background
nohup ./monitor_atlas.sh > logs/monitoring.log 2>&1 &
MONITOR_PID=$!

echo "✅ Monitoring service started (PID: $MONITOR_PID)"
echo "📋 To stop: pkill -f monitor_atlas.sh"
echo "📋 To view logs: tail -f logs/monitoring.log"
echo "📋 To check status: ps aux | grep monitor_atlas"