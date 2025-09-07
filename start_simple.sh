#!/bin/bash
echo "Starting Simple Podcast System"

# Step 1: Import episodes once
python3 simple_rss_import.py

# Step 2: Start continuous processing in background
nohup python3 simple_processor.py --continuous > processor.log 2>&1 &
echo $! > processor.pid

echo "✅ Simple system started!"
echo "Check: tail -f processor.log"
echo "Test: sqlite3 data/atlas.db 'SELECT COUNT(*) FROM podcast_episodes;'"