#!/bin/bash
# Simple background service runner for Atlas
cd /home/ubuntu/dev/atlas
source venv/bin/activate

# Set API key from command line argument
export OPENROUTER_API_KEY="$1"

echo "Starting Atlas background services..."
echo "API key set: $(echo $OPENROUTER_API_KEY | cut -c1-10)..."

# Start scheduler in background
python3 scripts/atlas_scheduler.py --start &
SCHEDULER_PID=$!

# Start watchdog in background  
python3 helpers/process_watchdog.py --daemon --interval 3 &
WATCHDOG_PID=$!

echo "Started scheduler (PID: $SCHEDULER_PID) and watchdog (PID: $WATCHDOG_PID)"
echo "Background services are running. Press Ctrl+C to stop."

# Keep script running
trap "kill $SCHEDULER_PID $WATCHDOG_PID; exit" INT TERM
wait