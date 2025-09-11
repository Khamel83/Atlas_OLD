#!/bin/bash
# Quick Atlas status check
echo "🚀 ATLAS STATUS"
echo "==============="

# API server status
if pgrep -f "uvicorn api.main:app" > /dev/null; then
    echo "✅ API Server: Running on port 7444"
else 
    echo "❌ API Server: Not running"
fi

# Reprocessing status
if pgrep -f "reprocess_limited_content.py" > /dev/null; then
    echo "✅ Reprocessing: Active"
    python3 check_reprocessing_progress.py | tail -4
else
    echo "❌ Reprocessing: Complete/Stopped"
fi

# Recent API activity
echo ""
echo "Recent API calls:"
tail -3 reprocess_log.txt 2>/dev/null | grep -E "(tags|summary)" | head -2 | sed 's/INFO:atlas_model_client:✅ /  ✅ /' || echo "  No recent activity"