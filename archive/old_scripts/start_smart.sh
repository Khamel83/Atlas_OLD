#!/bin/bash
echo "Starting Smart Transcript-First Podcast System"

# Step 1: Import episodes once
python3 simple_rss_import.py

# Step 2: Start smart transcript processor
python3 smart_transcript_processor.py --continuous > smart_processor.log 2>&1 &
echo $! > smart_processor.pid

echo "✅ Smart transcript-first system started!"
echo "This system finds existing transcripts online instead of downloading MP3s"
echo "Much faster and more efficient approach"
echo ""
echo "Check progress: tail -f smart_processor.log"
echo "Test transcripts: sqlite3 data/atlas.db 'SELECT COUNT(*) FROM content WHERE content_type = \"podcast_transcript\";'"
echo "Test pending: sqlite3 data/atlas.db 'SELECT COUNT(*) FROM content WHERE content_type = \"podcast_placeholder\";'"