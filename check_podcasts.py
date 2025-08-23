#!/usr/bin/env python3
import json
import os

files = [f for f in os.listdir('output/podcasts') if f.endswith('.json')]
total_files = len(files)
with_transcripts = 0
substantial_transcripts = 0

for i, f in enumerate(files[:100]):  # Sample first 100
    try:
        data = json.load(open(f'output/podcasts/{f}'))
        transcript = data.get('transcript_text', '')
        if transcript:
            with_transcripts += 1
            if len(transcript) > 100:
                substantial_transcripts += 1
    except Exception as e:
        continue

print(f"📻 Podcast Transcript Status:")
print(f"  Total podcast files: {total_files:,}")
print(f"  Sample checked: 100")
print(f"  With transcripts: {with_transcripts}/100")
print(f"  With substantial transcripts: {substantial_transcripts}/100")
print(f"  Transcript rate: {(substantial_transcripts/100)*100:.1f}%")