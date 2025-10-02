#!/usr/bin/env python3
"""
Analyze what's actually in the processed_content table
Break down by content type and source
"""

import asyncio
import sys
import aiosqlite
import json
from pathlib import Path

sys.path.append('.')

async def analyze_content():
    print("🔍 Analyzing actual processed content...")

    # Connect to database - try different paths
    db_paths = [
        "atlas_v2/data/atlas_v2.db",
        "atlas_v2/atlas.db",
        "data/atlas_v2.db",
        "atlas.db"
    ]

    db = None
    for path in db_paths:
        if Path(path).exists():
            print(f"📂 Using database: {path}")
            db = aiosqlite.connect(path)
            break

    if not db:
        print("❌ No database file found!")
        return

    async with db:

        # Check if processed_content table exists
        cursor = await db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='processed_content'")
        table_exists = await cursor.fetchone()

        if not table_exists:
            print("❌ processed_content table does not exist!")
            return

        # Get total count
        cursor = await db.execute("SELECT COUNT(*) FROM processed_content")
        total_count = (await cursor.fetchone())[0]
        print(f"📊 Total items in processed_content: {total_count}")

        # Break down by content type
        cursor = await db.execute("""
            SELECT content_type, COUNT(*) as count,
                   AVG(LENGTH(content)) as avg_length,
                   MIN(LENGTH(content)) as min_length,
                   MAX(LENGTH(content)) as max_length
            FROM processed_content
            GROUP BY content_type
            ORDER BY count DESC
        """)
        content_types = await cursor.fetchall()

        print(f"\n📋 Content Type Breakdown:")
        for content_type, count, avg_len, min_len, max_len in content_types:
            print(f"  - {content_type}: {count} items")
            print(f"    Avg length: {int(avg_len):,} chars")
            print(f"    Min/Max: {int(min_len):,} / {int(max_len):,} chars")

        # Look at source URLs to identify actual podcasts
        cursor = await db.execute("""
            SELECT
                CASE
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%lexfridman.com%' THEN 'Lex Fridman'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%acquired.fm%' THEN 'Acquired'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%tim.blog%' THEN 'Tim Ferriss'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%spotify.com%' THEN 'Spotify'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%apple.com%' THEN 'Apple Podcasts'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%youtube.com%' THEN 'YouTube'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%anchor.fm%' THEN 'Anchor'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%buzzsprout.com%' THEN 'Buzzsprout'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%simplecast.com%' THEN 'Simplecast'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%transistor.fm%' THEN 'Transistor'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%libsyn.com%' THEN 'Libsyn'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%soundcloud.com%' THEN 'SoundCloud'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%stitcher.com%' THEN 'Stitcher'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%overcast.fm%' THEN 'Overcast'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%pocketcasts.com%' THEN 'Pocket Casts'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%castro.fm%' THEN 'Castro'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%breaker.audio%' THEN 'Breaker'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%podcastaddict.com%' THEN 'Podcast Addict'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%podbean.com%' THEN 'Podbean'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%megaphone.fm%' THEN 'Megaphone'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%art19.com%' THEN 'Art19'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%wondery.com%' THEN 'Wondery'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%gimlet.com%' THEN 'Gimlet'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%parcast.com%' THEN 'Parcast'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%cadence13.com%' THEN 'Cadence13'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%westwoodone.com%' THEN 'Westwood One'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%iheart.com%' THEN 'iHeartRadio'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%tunein.com%' THEN 'TuneIn'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%deezer.com%' THEN 'Deezer'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%pandora.com%' THEN 'Pandora'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%last.fm%' THEN 'Last.fm'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%mixcloud.com%' THEN 'Mixcloud'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%bandcamp.com%' THEN 'Bandcamp'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%reverb.fm%' THEN 'ReverbFM'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%fireside.fm%' THEN 'Fireside'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%transistor.fm%' THEN 'Transistor'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%anchor.fm%' THEN 'Anchor'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%buzzsprout.com%' THEN 'Buzzsprout'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%simplecast.com%' THEN 'Simplecast'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%libsyn.com%' THEN 'Libsyn'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%soundcloud.com%' THEN 'SoundCloud'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%stitcher.com%' THEN 'Stitcher'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%overcast.fm%' THEN 'Overcast'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%pocketcasts.com%' THEN 'Pocket Casts'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%castro.fm%' THEN 'Castro'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%breaker.audio%' THEN 'Breaker'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%podcastaddict.com%' THEN 'Podcast Addict'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%podbean.com%' THEN 'Podbean'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%megaphone.fm%' THEN 'Megaphone'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%art19.com%' THEN 'Art19'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%wondery.com%' THEN 'Wondery'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%gimlet.com%' THEN 'Gimlet'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%parcast.com%' THEN 'Parcast'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%cadence13.com%' THEN 'Cadence13'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%westwoodone.com%' THEN 'Westwood One'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%iheart.com%' THEN 'iHeartRadio'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%tunein.com%' THEN 'TuneIn'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%deezer.com%' THEN 'Deezer'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%pandora.com%' THEN 'Pandora'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%last.fm%' THEN 'Last.fm'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%mixcloud.com%' THEN 'Mixcloud'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%bandcamp.com%' THEN 'Bandcamp'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%reverb.fm%' THEN 'ReverbFM'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%fireside.fm%' THEN 'Fireside'
                    WHEN json_extract(metadata_json, '$.source_url') LIKE '%transistor.fm%' THEN 'Transistor'
                    ELSE 'Other/Unknown'
                END as source,
                COUNT(*) as count,
                AVG(LENGTH(content)) as avg_length
            FROM processed_content
            WHERE json_extract(metadata_json, '$.source_url') IS NOT NULL
            GROUP BY source
            ORDER BY count DESC
        """)
        sources = await cursor.fetchall()

        print(f"\n🎧 Source Breakdown:")
        for source, count, avg_len in sources:
            if count > 5:  # Only show sources with more than 5 items
                print(f"  - {source}: {count} items, avg {int(avg_len):,} chars")

        # Look for actual podcast transcripts (check for transcript indicators)
        cursor = await db.execute("""
            SELECT COUNT(*) as potential_transcripts
            FROM processed_content
            WHERE (
                LOWER(content) LIKE '%host:%' OR
                LOWER(content) LIKE '%guest:%' OR
                LOWER(content) LIKE '%interviewer:%' OR
                LOWER(content) LIKE '%speaker %' OR
                LOWER(content) LIKE '%episode %' OR
                LOWER(content) LIKE '%podcast%' OR
                LOWER(content) LIKE '%transcript%'
            )
        """)
        potential_transcripts = (await cursor.fetchone())[0]

        print(f"\n🎙️ Potential Podcast Transcripts (based on content analysis): {potential_transcripts}")

        # Show some actual examples of what we have
        cursor = await db.execute("""
            SELECT
                content_id,
                json_extract(metadata_json, '$.source_url') as source_url,
                json_extract(metadata_json, '$.title') as title,
                LENGTH(content) as content_length,
                content_type,
                substr(content, 1, 200) as preview
            FROM processed_content
            ORDER BY content_length DESC
            LIMIT 10
        """)
        top_items = await cursor.fetchall()

        print(f"\n🔝 Top 10 items by content length:")
        for i, (content_id, source_url, title, length, content_type, preview) in enumerate(top_items, 1):
            print(f"\n{i}. {content_id} ({content_type})")
            print(f"   Source: {source_url}")
            print(f"   Title: {title}")
            print(f"   Length: {length:,} chars")
            print(f"   Preview: {preview}...")

if __name__ == "__main__":
    asyncio.run(analyze_content())