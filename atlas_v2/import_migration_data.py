#!/usr/bin/env python3
"""
Atlas v2 Migration Data Import Script

Imports data exported from Atlas v1 into Atlas v2.
Run this on the OCI instance after transferring migration files.

Usage:
    python3 import_migration_data.py
"""

import asyncio
import json
import logging
from pathlib import Path
from datetime import datetime
import sqlite3

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/migration_import.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

async def import_migration_data():
    """Import all migration data from exported files"""

    migration_dir = Path("/home/ubuntu/atlas_v2_migration")
    if not migration_dir.exists():
        logger.error(f"Migration directory not found: {migration_dir}")
        logger.error("Please copy migration files from local machine first:")
        logger.error("scp -r atlas_v2_migration/ ubuntu@<OCI-IP>:/home/ubuntu/")
        return

    # Import database manager
    from modules.database import DatabaseManager
    from modules.id_generator import generate_id_from_legacy_url

    db_manager = DatabaseManager()
    await db_manager.initialize()

    # Import main content
    content_file = migration_dir / "main_content_export.json"
    if content_file.exists():
        logger.info("📥 Importing main content...")

        with open(content_file, 'r', encoding='utf-8') as f:
            content_data = json.load(f)

        imported_count = 0
        skipped_count = 0

        for item in content_data:
            try:
                # Generate new content ID
                new_content_id = generate_id_from_legacy_url(
                    url=item['url'],
                    source=item.get('source', 'unknown'),
                    metadata={
                        'title': item.get('title', ''),
                        'created_at': item.get('created_at'),
                        'content_type': item.get('content_type', 'unknown')
                    }
                )

                # Check if already exists
                if await db_manager.content_exists(new_content_id):
                    skipped_count += 1
                    continue

                # Save content file
                if item.get('content') and len(item['content']) > 1000:
                    content_dir = Path("content/processed")
                    content_dir.mkdir(parents=True, exist_ok=True)

                    # Save markdown file
                    markdown_path = content_dir / f"{new_content_id}.md"

                    # Create frontmatter
                    frontmatter = f"""---
id: {new_content_id}
title: {item.get('title', '').replace('"', '\\"')}
url: {item['url']}
content_type: {item.get('content_type', 'unknown')}
created_at: {item.get('created_at', datetime.now().isoformat())}
migrated_from: atlas_v1
---

"""
                    with open(markdown_path, 'w', encoding='utf-8') as f:
                        f.write(frontmatter + item['content'])

                    # Create metadata JSON
                    metadata_path = content_dir / f"{new_content_id}.json"
                    metadata = {
                        "content_id": new_content_id,
                        "migrated_from": "atlas_v1",
                        "legacy_id": item.get('id'),
                        "validation": {
                            "status": "migrated",
                            "word_count": len(item['content'].split()),
                            "character_count": len(item['content'])
                        },
                        "original_metadata": {k: v for k, v in item.items() if k != 'content'}
                    }

                    with open(metadata_path, 'w', encoding='utf-8') as f:
                        json.dump(metadata, f, indent=2, ensure_ascii=False)

                # Store in database
                now = datetime.now().isoformat()
                async with db_manager.db_path.open() as conn:
                    await conn.execute("""
                        INSERT OR IGNORE INTO content_metadata (
                            content_id, source_url, source_name, content_type,
                            title, validation_status, word_count,
                            metadata_json, created_at, updated_at
                        ) VALUES (?, ?, ?, ?, ?, 'migrated', ?, ?, ?, ?)
                    """, (
                        new_content_id,
                        item['url'],
                        item.get('source', 'unknown'),
                        item.get('content_type', 'unknown'),
                        item.get('title', ''),
                        len(item.get('content', '').split()),
                        json.dumps(metadata),
                        item.get('created_at', now),
                        now
                    ))

                imported_count += 1

                if imported_count % 100 == 0:
                    logger.info(f"Imported {imported_count} items...")

            except Exception as e:
                logger.error(f"Error importing {item.get('url', 'unknown')}: {e}")

        logger.info(f"✅ Content import complete: {imported_count} imported, {skipped_count} skipped")

    # Import episode queue
    queue_file = migration_dir / "episode_queue_export.json"
    if queue_file.exists():
        logger.info("📥 Importing episode queue...")

        with open(queue_file, 'r', encoding='utf-8') as f:
            queue_data = json.load(f)

        for item in queue_data:
            try:
                # Generate content ID
                new_content_id = generate_id_from_legacy_url(
                    url=item['episode_url'],
                    source=item['podcast_name'],
                    metadata=json.loads(item.get('metadata', '{}'))
                )

                # Add to queue
                await db_manager.enqueue_content(
                    content_id=new_content_id,
                    source_url=item['episode_url'],
                    source_name=item['podcast_name'],
                    content_type='podcast',
                    metadata=json.loads(item.get('metadata', '{}')),
                    priority='normal'
                )

            except Exception as e:
                logger.error(f"Error importing queue item {item.get('episode_url')}: {e}")

        logger.info(f"✅ Queue import complete: {len(queue_data)} items")

    # Generate import report
    stats = await db_manager.get_processing_stats()

    report = {
        "import_timestamp": datetime.now().isoformat(),
        "imported_stats": stats,
        "import_source": "atlas_v1_migration"
    }

    report_file = Path("logs/migration_import_report.json")
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)

    logger.info(f"📊 Import report saved: {report_file}")
    logger.info("🎉 Migration import complete!")

    # Display final stats
    print("\n" + "="*60)
    print("ATLAS V2 MIGRATION IMPORT COMPLETE")
    print("="*60)
    for content_type, count in stats.get('content_by_type', {}).items():
        print(f"{content_type}: {count:,} items")
    print(f"\nTotal queue items: {sum(stats.get('queue_by_status', {}).values()):,}")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(import_migration_data())