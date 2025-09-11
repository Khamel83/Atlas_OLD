#!/bin/bash
echo "Starting Simple Podcast System with Real Transcription"

# Step 1: Import episodes once
python3 simple_rss_import.py

# Step 2: Start continuous processing in background with virtual environment
source venv/bin/activate
nohup python3 simple_processor.py --continuous > processor.log 2>&1 &
echo $! > processor.pid

echo "✅ Simple system started with Whisper transcription!"
echo "Check: tail -f processor.log"
echo "Test: sqlite3 data/atlas.db 'SELECT COUNT(*) FROM content WHERE title LIKE \"%[PODCAST]%\";'"