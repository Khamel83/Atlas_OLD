#!/usr/bin/env python3
"""
Check what podcast sources we actually have content from
"""

import asyncio
import sys
import aiosqlite
from pathlib import Path

async def check_podcast_sources():
    print("🎙️ Checking REAL podcast content by source...")

    # Connect to database
    async with aiosqlite.connect("atlas_v2/data/atlas_v2.db") as db:

        # Check processed content table for podcast indicators
        cursor = await db.execute("""
            SELECT
                content_id,
                content_type,
                json_extract(metadata_json, '$.source_url') as source_url,
                json_extract(metadata_json, '$.title') as title,
                LENGTH(content) as content_length,
                substr(content, 1, 300) as preview
            FROM processed_content
            WHERE (
                json_extract(metadata_json, '$.source_url') LIKE '%lexfridman.com%' OR
                json_extract(metadata_json, '$.source_url') LIKE '%acquired.fm%' OR
                json_extract(metadata_json, '$.source_url') LIKE '%tim.blog%' OR
                json_extract(metadata_json, '$.source_url') LIKE '%spotify.com%' OR
                json_extract(metadata_json, '$.source_url') LIKE '%apple.com%' OR
                json_extract(metadata_json, '$.source_url') LIKE '%youtube.com%' OR
                LOWER(content) LIKE '%lex fridman%' OR
                LOWER(content) LIKE '%acquired%' OR
                LOWER(content) LIKE '%tim ferriss%' OR
                content_type = 'podcast'
            )
            ORDER BY content_length DESC
        """)
        potential_podcasts = await cursor.fetchall()

        print(f"\n🎧 Potential Podcast Content Found: {len(potential_podcasts)} items")

        # Group by source
        sources = {}
        for content_id, content_type, source_url, title, length, preview in potential_podcasts:
            if source_url:
                if 'lexfridman.com' in source_url:
                    source = 'Lex Fridman'
                elif 'acquired.fm' in source_url:
                    source = 'Acquired'
                elif 'tim.blog' in source_url:
                    source = 'Tim Ferriss'
                else:
                    source = 'Other Podcast'
            else:
                source = 'Unknown Source'

            if source not in sources:
                sources[source] = []
            sources[source].append({
                'content_id': content_id,
                'content_type': content_type,
                'source_url': source_url,
                'title': title,
                'length': length,
                'preview': preview
            })

        print(f"\n📊 Podcast Content by Source:")
        for source, items in sources.items():
            print(f"\n{source}: {len(items)} items")
            for item in items[:3]:  # Show first 3
                print(f"  - {item['content_id']} ({item['content_type']})")
                print(f"    Length: {item['length']:,} chars")
                print(f"    Title: {item['title']}")
                if item['source_url']:
                    print(f"    URL: {item['source_url']}")
                print(f"    Preview: {item['preview'][:150]}...")
                print()

        # Now check the main content table for v1 migrated content
        cursor = await db.execute("""
            SELECT
                content_id,
                source_url,
                source_name,
                content_type,
                LENGTH(content) as content_length,
                substr(content, 1, 200) as preview
            FROM content
            WHERE (
                source_url LIKE '%lexfridman.com%' OR
                source_url LIKE '%acquired.fm%' OR
                source_url LIKE '%tim.blog%' OR
                source_name LIKE '%lex fridman%' OR
                source_name LIKE '%acquired%' OR
                source_name LIKE '%tim ferriss%' OR
                content_type = 'podcast_episode'
            )
            ORDER BY content_length DESC
            LIMIT 20
        """)
        v1_podcasts = await cursor.fetchall()

        print(f"\n📚 V1 Migrated Podcast Content: {len(v1_podcasts)} items")

        v1_sources = {}
        for content_id, source_url, source_name, content_type, length, preview in v1_podcasts:
            if source_url:
                if 'lexfridman.com' in source_url:
                    source = 'Lex Fridman'
                elif 'acquired.fm' in source_url:
                    source = 'Acquired'
                elif 'tim.blog' in source_url:
                    source = 'Tim Ferriss'
                else:
                    source = 'Other Podcast'
            elif source_name:
                if 'lex fridman' in source_name.lower():
                    source = 'Lex Fridman'
                elif 'acquired' in source_name.lower():
                    source = 'Acquired'
                elif 'tim ferriss' in source_name.lower():
                    source = 'Tim Ferriss'
                else:
                    source = source_name
            else:
                source = 'Unknown'

            if source not in v1_sources:
                v1_sources[source] = []
            v1_sources[source].append({
                'content_id': content_id,
                'content_type': content_type,
                'source_url': source_url,
                'source_name': source_name,
                'length': length,
                'preview': preview
            })

        print(f"\n📊 V1 Content by Source:")
        for source, items in v1_sources.items():
            print(f"\n{source}: {len(items)} items")
            total_chars = sum(item['length'] for item in items)
            print(f"  Total characters: {total_chars:,}")
            for item in items[:2]:  # Show first 2
                print(f"  - {item['content_id']} ({item['content_type']})")
                print(f"    Length: {item['length']:,} chars")
                if item['source_url']:
                    print(f"    URL: {item['source_url']}")
                print(f"    Preview: {item['preview'][:150]}...")
                print()

if __name__ == "__main__":
    asyncio.run(check_podcast_sources())