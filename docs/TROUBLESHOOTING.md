# 🔧 Atlas Bulletproof Troubleshooting Guide

## Common Issues and Solutions

### Memory Leaks Detected
**Symptoms**: Memory usage continuously grows
**Solution**:
1. Check logs: `tail -f logs/bulletproof_process_manager.log`
2. Review memory reports: `ls -la logs/memory_leak_*.json`
3. Restart services: `sudo systemctl restart atlas.service`

### Circuit Breaker Open
**Symptoms**: Operations failing with "Circuit breaker is OPEN"
**Solution**:
1. Check what's failing: `./venv/bin/python atlas_status.py --detailed`
2. Fix underlying issue (disk space, permissions, etc.)
3. Wait for automatic reset or restart service

### Service Won't Start
**Symptoms**: `systemctl start atlas.service` fails
**Solution**:
1. Check system health: `./venv/bin/python helpers/resource_monitor.py`
2. Check logs: `journalctl -u atlas.service -f`
3. Verify Python environment: `./venv/bin/python --version`

### High Resource Usage
**Symptoms**: High CPU/memory alerts
**Solution**:
1. Check process status: `./venv/bin/python atlas_status.py`
2. Kill runaway processes: `sudo systemctl stop atlas.service`
3. Clean up: `pkill -f atlas_`

## Emergency Commands
```bash
# Emergency stop everything
sudo systemctl stop atlas.service
pkill -f "atlas_"

# Clean up large log files
find logs/ -name "*.log" -size +100M -exec mv {} {}.old \;

# Reset circuit breakers
sudo systemctl restart atlas.service
```
