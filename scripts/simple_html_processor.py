#!/usr/bin/env python3
"""
Simple HTML File Processor for Atlas

Processes the 4,331 mangled HTML files by treating them as articles
and running them through the existing article ingestion system.
"""

import os
import sys
import glob
import shutil
import hashlib
from datetime import datetime
from pathlib import Path

# Add the parent directory to the path so we can import helpers
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from helpers.config import load_config
    from helpers.document_ingestor import DocumentIngestor
    from helpers.utils import log_info, log_error
except ImportError as e:
    print(f"Error importing Atlas modules: {e}")
    sys.exit(1)


def process_html_files_as_articles(max_files: int = 100):
    """
    Process HTML files by treating them as articles.
    This bypasses the complex filename issues by processing content directly.
    """
    print(f"🔄 Processing HTML files as articles (max {max_files})...")

    # Load Atlas configuration
    config = load_config()

    # Initialize document ingestor
    document_ingestor = DocumentIngestor(config)

    # Find all HTML files
    html_files = glob.glob("inputs/**/*.html", recursive=True)

    if not html_files:
        print("❌ No HTML files found")
        return 0, 0

    print(f"📁 Found {len(html_files)} HTML files")

    # Create processed directory
    processed_dir = "inputs/processed_html"
    os.makedirs(processed_dir, exist_ok=True)

    successful_count = 0
    failed_count = 0

    for i, html_file in enumerate(html_files[:max_files]):
        print(f"\n📄 Processing file {i+1}/{min(len(html_files), max_files)}")

        try:
            # Read the HTML content
            with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
                html_content = f.read()

            if len(html_content) < 100:
                print(f"   ⚠️  Skipping tiny file ({len(html_content)} chars)")
                continue

            # Generate a simple filename for processing
            file_hash = hashlib.md5(html_content.encode()).hexdigest()[:12]
            simple_name = f"article_{file_hash}.html"
            temp_file = f"temp_{simple_name}"

            # Write to temporary file with simple name
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write(html_content)

            try:
                # Create metadata for historical record including original filename
                original_filename = os.path.basename(html_file)
                metadata = {
                    "original_filename": original_filename,
                    "original_path": html_file,
                    "content_source": "mangled_html_file",
                    "processing_date": datetime.now().isoformat(),
                    "file_size": len(html_content),
                }

                # Process as document using existing system
                result = document_ingestor.ingest_content(temp_file)

                if result and result.success:
                    uid = getattr(
                        result, "uid", getattr(result, "content_id", "processed")
                    )
                    print(f"   ✅ Success: {uid}")

                    # Move original file to processed with metadata preserved
                    target_file = os.path.join(
                        processed_dir, f"{file_hash}_{simple_name}"
                    )
                    if not os.path.exists(target_file):
                        shutil.move(html_file, target_file)

                    successful_count += 1
                else:
                    print(
                        f"   ❌ Failed: {result.error if result else 'Unknown error'}"
                    )
                    failed_count += 1

            finally:
                # Clean up temp file
                if os.path.exists(temp_file):
                    os.remove(temp_file)

        except Exception as e:
            print(f"   💥 Exception: {str(e)}")
            failed_count += 1

    print(f"\n🎯 Results:")
    print(f"   ✅ Successful: {successful_count}")
    print(f"   ❌ Failed: {failed_count}")
    print(f"   📁 Remaining: {len(html_files) - successful_count - failed_count}")

    return successful_count, failed_count


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Simple HTML file processor")
    parser.add_argument(
        "--max-files", type=int, default=50, help="Maximum number of files to process"
    )

    args = parser.parse_args()

    successful, failed = process_html_files_as_articles(args.max_files)

    if successful > 0:
        print(f"\n🚀 Success! Processed {successful} HTML files.")
        print("   Run again to process more files.")
    else:
        print("\n😞 No files were successfully processed.")


if __name__ == "__main__":
    main()
