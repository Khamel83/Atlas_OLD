#!/bin/bash
# Atlas Real-Time Health Score - Log-Stream Version
# Provides single KPI metric using new log-stream analytics

echo "🔍 Atlas Health Score - Log-Stream Analytics"
echo "=============================================="

# Check if analytics engine exists
if [ ! -f "atlas_analytics.py" ]; then
    echo "❌ Analytics engine not found"
    exit 1
fi

# Get health score from analytics engine
HEALTH_DATA=$(python3 -c "
from atlas_analytics import AtlasAnalytics
import json
try:
    analytics = AtlasAnalytics()
    health = analytics.get_health_score()
    print(json.dumps(health))
except Exception as e:
    print(json.dumps({'error': str(e)}))
")

# Check if we got valid data
if echo "$HEALTH_DATA" | grep -q "error"; then
    echo "❌ Error getting health data"
    echo "$HEALTH_DATA" | python3 -c "import sys, json; data=json.load(sys.stdin); print(f'   Error: {data.get(\"error\", \"unknown\")}')"
    exit 1
fi

# Extract health score and status
HEALTH_SCORE=$(echo "$HEALTH_DATA" | python3 -c "import sys, json; data=json.load(sys.stdin); print(int(data.get('health_score', 0)))")
HEALTH_STATUS=$(echo "$HEALTH_DATA" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('status', 'UNKNOWN'))")

# Color codes for status
if [ "$HEALTH_SCORE" -ge 80 ]; then
    COLOR="🟢"
elif [ "$HEALTH_SCORE" -ge 60 ]; then
    COLOR="🟡"
elif [ "$HEALTH_SCORE" -ge 40 ]; then
    COLOR="🟠"
elif [ "$HEALTH_SCORE" -ge 20 ]; then
    COLOR="🔴"
else
    COLOR="⚫"
fi

# Display health score
echo "Health Score: $COLOR $HEALTH_SCORE/100 ($HEALTH_STATUS)"

# Get additional metrics
METRICS=$(python3 -c "
from atlas_analytics import AtlasAnalytics
import json
try:
    analytics = AtlasAnalytics()
    metrics = analytics.get_real_time_metrics()
    print(json.dumps({
        'discovered': metrics['totals']['discovered'],
        'processed': metrics['totals']['processed'],
        'failed': metrics['totals']['failed'],
        'success_rate': metrics['totals']['success_rate'],
        'recent_activity': metrics['recent_activity']['current_hour_processed'],
        'sources': len(metrics['top_sources'])
    }))
except Exception as e:
    print(json.dumps({'error': str(e)}))
")

if ! echo "$METRICS" | grep -q "error"; then
    echo ""
    echo "📊 Additional Metrics:"
    echo "$METRICS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print(f'   Discovered: {data[\"discovered\"]} episodes')
print(f'   Processed: {data[\"processed\"]} episodes')
print(f'   Failed: {data[\"failed\"]} episodes')
print(f'   Success Rate: {data[\"success_rate\"]}%')
print(f'   Current Hour: {data[\"recent_activity\"]} processed')
print(f'   Active Sources: {data[\"sources\"]}')
"
fi

# Check log files
echo ""
echo "📋 System Status:"
LOG_FILE="atlas_operations.log"
if [ -f "$LOG_FILE" ]; then
    LOG_SIZE=$(du -h "$LOG_FILE" | cut -f1)
    LOG_LINES=$(wc -l < "$LOG_FILE")
    echo "   Log File: $LOG_FILE ($LOG_SIZE, $LOG_LINES lines)"
else
    echo "   Log File: Not found"
fi

# Check if Atlas manager is running
if pgrep -f "atlas_manager.py" > /dev/null; then
    echo "   Atlas Manager: ✅ Running"
else
    echo "   Atlas Manager: ❌ Not running"
fi

# Check if Universal URL processor is running
if pgrep -f "universal_url_processor.py" > /dev/null; then
    echo "   Universal URL Processor: ✅ Running"
else
    echo "   Universal URL Processor: ❌ Not running"
fi

# Quick performance test
echo ""
echo "⚡ Performance Test:"
START_TIME=$(date +%s.%N)
python3 -c "from atlas_analytics import AtlasAnalytics; analytics = AtlasAnalytics(); analytics.update_cache()" 2>/dev/null
END_TIME=$(date +%s.%N)
ANALYTICS_TIME=$(echo "$END_TIME - $START_TIME" | bc -l)

if (( $(echo "$ANALYTICS_TIME < 1.0" | bc -l) )); then
    echo "   Analytics Response: ⚡ ${ANALYTICS_TIME}s (fast)"
elif (( $(echo "$ANALYTICS_TIME < 3.0" | bc -l) )); then
    echo "   Analytics Response: 🐢 ${ANALYTICS_TIME}s (normal)"
else
    echo "   Analytics Response: 🐌 ${ANALYTICS_TIME}s (slow)"
fi

# Return health score for scripting
echo ""
echo "HEALTH_SCORE=$HEALTH_SCORE"
echo "HEALTH_STATUS=$HEALTH_STATUS"

# Exit with appropriate code
if [ "$HEALTH_SCORE" -ge 60 ]; then
    exit 0  # Good
elif [ "$HEALTH_SCORE" -ge 40 ]; then
    exit 1  # Warning
else
    exit 2  # Critical
fi