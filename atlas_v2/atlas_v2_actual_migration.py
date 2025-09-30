#!/usr/bin/env python3
"""
Atlas v1 to v2 Data Migration Script

Migrates all critical data from Atlas v1 to Atlas v2:
- Content metadata and extracted text
- Episode queue items
- Processing history
"""

import os
import sys
import sqlite3
import asyncio
import hashlib
import json
from datetime import datetime
from pathlib import Path

# Add atlas_v2 modules to path
sys.path.append('/home/ubuntu/dev/atlas/atlas_v2')

from modules.database import DatabaseManager
from modules.id_generator import IDGenerator

class AtlasMigrator:
    """Migrates data from Atlas v1 to Atlas v2"""

    def __init__(self):
        self.v1_db_path = "/home/ubuntu/dev/atlas/atlas.db"
        self.v2_db_manager = DatabaseManager(db_path="/home/ubuntu/dev/atlas/atlas_v2/data/atlas_v2.db")
        self.id_generator = IDGenerator()
        self.migrated_count = 0
        self.skipped_count = 0

    async def migrate_all_data(self):
        """Migrate all data from v1 to v2"""
        print("🚀 Starting Atlas v1 → v2 migration...")

        # Initialize v2 database
        await self.v2_db_manager.init_database()

        # Connect to v1 database
        v1_conn = sqlite3.connect(self.v1_db_path)
        v1_conn.row_factory = sqlite3.Row

        try:
            # Migrate content
            await self.migrate_content(v1_conn)

            # Migrate episode queue
            await self.migrate_episode_queue(v1_conn)

        finally:
            v1_conn.close()

        print(f"✅ Migration complete!")
        print(f"📊 Migrated: {self.migrated_count:,} items")
        print(f"⏭️ Skipped: {self.skipped_count:,} items")

    async def migrate_content(self, v1_conn):
        """Migrate content table to content_metadata"""
        print("📄 Migrating content table...")

        # Get content from v1
        cursor = v1_conn.execute("""
            SELECT
                url, title, content, content_type,
                source, created_at, metadata,
                summary, tags, reading_time
            FROM content
            WHERE content IS NOT NULL
            AND LENGTH(TRIM(content)) > 100
            ORDER BY created_at DESC
        """)

        batch_size = 100
        batch = []

        for row in cursor:
            # Generate unique content ID
            source = row['source'] or 'unknown'
            content_type = row['content_type'] or 'article'
            created_at = row['created_at'] or datetime.now().isoformat()

            # Parse date for ID generation
            try:
                dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                date_str = dt.strftime('%Y-%m-%d')
            except:
                date_str = datetime.now().strftime('%Y-%m-%d')

            # Create slug from title or URL
            title = row['title'] or ''
            url = row['url'] or ''
            slug = self.id_generator._create_slug(title or url)

            content_id = f"{source}-{content_type}-{date_str}-{slug}"

            # Prepare metadata
            try:
                metadata = json.loads(row['metadata']) if row['metadata'] else {}
            except:
                metadata = {}

            # Enhanced metadata
            metadata.update({
                'original_url': url,
                'migrated_from': 'atlas_v1',
                'migration_date': datetime.now().isoformat(),
                'original_created_at': created_at,
                'tags': row['tags'],
                'reading_time': row['reading_time'],
                'summary': row['summary']
            })

            batch.append({
                'content_id': content_id,
                'url': url,
                'title': title,
                'content': row['content'],
                'content_type': content_type,
                'source': source,
                'metadata': json.dumps(metadata),
                'created_at': created_at
            })

            if len(batch) >= batch_size:
                await self._insert_content_batch(batch)
                batch = []

        # Insert remaining batch
        if batch:
            await self._insert_content_batch(batch)

    async def _insert_content_batch(self, batch):
        """Insert a batch of content records"""
        for item in batch:
            try:
                # Check if already exists
                existing = await self.v2_db_manager.get_content_metadata(item['content_id'])
                if existing:
                    self.skipped_count += 1
                    continue

                # Insert new content
                await self.v2_db_manager.store_content_metadata(
                    content_id=item['content_id'],
                    url=item['url'],
                    title=item['title'],
                    content=item['content'],
                    content_type=item['content_type'],
                    source=item['source'],
                    metadata=json.loads(item['metadata'])
                )

                self.migrated_count += 1

                if self.migrated_count % 100 == 0:
                    print(f"  📊 Migrated {self.migrated_count:,} content items...")

            except Exception as e:
                print(f"  ❌ Error migrating {item['content_id']}: {e}")
                self.skipped_count += 1

    async def migrate_episode_queue(self, v1_conn):
        """Migrate episode_queue table to processing_queue"""
        print("📋 Migrating episode queue...")

        cursor = v1_conn.execute("""
            SELECT
                episode_url, episode_title, podcast_name,
                status, created_at, updated_at,
                episode_description, transcript_url
            FROM episode_queue
            ORDER BY created_at DESC
        """)

        for row in cursor:
            try:
                # Generate content ID for episode
                source = 'podcast'
                content_type = 'episode'

                try:
                    dt = datetime.fromisoformat(row['created_at'].replace('Z', '+00:00'))
                    date_str = dt.strftime('%Y-%m-%d')
                except:
                    date_str = datetime.now().strftime('%Y-%m-%d')

                slug = self.id_generator._create_slug(row['episode_title'] or row['episode_url'])
                content_id = f"{source}-{content_type}-{date_str}-{slug}"

                # Check if already in queue
                existing = await self.v2_db_manager.get_queue_item(content_id)
                if existing:
                    self.skipped_count += 1
                    continue

                # Add to processing queue
                await self.v2_db_manager.add_to_queue(
                    content_id=content_id,
                    url=row['episode_url'],
                    content_type='podcast',
                    metadata={
                        'title': row['episode_title'],
                        'podcast_name': row['podcast_name'],
                        'description': row['episode_description'],
                        'transcript_url': row['transcript_url'],
                        'original_status': row['status'],
                        'migrated_from': 'atlas_v1'
                    }
                )

                self.migrated_count += 1

                if self.migrated_count % 100 == 0:
                    print(f"  📊 Migrated {self.migrated_count:,} total items...")

            except Exception as e:
                print(f"  ❌ Error migrating episode {row['episode_url']}: {e}")
                self.skipped_count += 1

async def main():
    """Run the migration"""
    migrator = AtlasMigrator()
    await migrator.migrate_all_data()

if __name__ == "__main__":
    asyncio.run(main())