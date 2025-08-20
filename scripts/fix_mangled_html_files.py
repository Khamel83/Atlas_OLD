#!/usr/bin/env python3
"""
Fix Mangled HTML Filenames and Process Content

This script handles the mangled UTF-8 encoded filenames in inputs/saved_html/
and processes the content through Atlas.

The filenames are MIME-encoded UTF-8 like:
- =UTF-8bV2hhdCBJ4oCZbSBIZWFyaW5nOiBBIE1vdmllIENyaXNpcywgRWxsaXNvbg===
- =UTF-8qWhat_I=E2=80=99m_Hearing_Netflix=E2=80=99s_Curtain_Call...

This script:
1. Decodes the mangled filenames 
2. Renames files to clean names
3. Processes them through Atlas document processor
4. Moves processed files to avoid reprocessing
"""

import os
import sys
import glob
import base64
import urllib.parse
import hashlib
import shutil
from typing import List, Tuple, Optional
from pathlib import Path

# Add the parent directory to the path so we can import helpers
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from helpers.config import load_config
    from helpers.document_processor import AtlasDocumentProcessor
    from helpers.utils import log_info, log_error
except ImportError as e:
    print(f"Error importing Atlas modules: {e}")
    print("Make sure you're running from the Atlas root directory")
    sys.exit(1)


def decode_utf8_filename(mangled_name: str) -> Optional[str]:
    """
    Decode mangled UTF-8 MIME-encoded filename.

    Handles patterns like:
    - =UTF-8bV2hhdCBJ4oCZbSBIZWFyaW5nOiBBIE1vdmllIENyaXNpcywgRWxsaXNvbg===
    - =UTF-8qWhat_I=E2=80=99m_Hearing_Netflix=E2=80=99s_Curtain_Call...
    """
    try:
        if mangled_name.startswith("=UTF-8b"):
            # Base64 encoded UTF-8
            base64_part = mangled_name[7:]  # Remove '=UTF-8b'
            # Extract just the base64 part before any additional encoding
            base64_clean = base64_part.split("_")[0].split("=")[0] + "=="  # Add padding
            decoded_bytes = base64.b64decode(base64_clean)
            return decoded_bytes.decode("utf-8", errors="ignore")

        elif mangled_name.startswith("=UTF-8q"):
            # Quoted-printable encoded UTF-8
            import quopri

            quoted_part = mangled_name[7:]  # Remove '=UTF-8q'
            # Extract everything before the timestamp
            quoted_clean = (
                quoted_part.split("_Tue,")[0].split("_Wed,")[0].split("_Fri,")[0]
            )
            # Decode quoted-printable
            decoded_bytes = quopri.decodestring(quoted_clean.encode())
            return decoded_bytes.decode("utf-8", errors="ignore")

        elif mangled_name.startswith("=utf-8b"):
            # Lowercase variant
            base64_part = mangled_name[7:]
            base64_clean = base64_part.split("_")[0].split("=")[0] + "=="
            decoded_bytes = base64.b64decode(base64_clean)
            return decoded_bytes.decode("utf-8", errors="ignore")

    except Exception as e:
        print(f"Failed to decode filename {mangled_name}: {e}")
        return None

    return mangled_name  # Return as-is if no pattern matches


def clean_filename(decoded_name: str) -> str:
    """Convert decoded filename to a clean, filesystem-safe name."""
    # Remove or replace problematic characters
    cleaned = decoded_name.replace("/", "_").replace("\\", "_")
    cleaned = cleaned.replace(":", "_").replace("*", "_")
    cleaned = cleaned.replace("?", "_").replace('"', "_")
    cleaned = cleaned.replace("<", "_").replace(">", "_")
    cleaned = cleaned.replace("|", "_").replace("\n", "_")

    # Limit length and add hash for uniqueness
    if len(cleaned) > 100:
        hash_suffix = hashlib.md5(decoded_name.encode()).hexdigest()[:8]
        cleaned = cleaned[:90] + "_" + hash_suffix

    return cleaned


def process_mangled_html_files(
    input_dir: str = "inputs", max_files: int = 100
) -> Tuple[int, int]:
    """
    Process mangled HTML files in the input directory.

    Returns:
        Tuple[int, int]: (successful_count, failed_count)
    """
    print(f"🔄 Processing mangled HTML files in {input_dir}...")

    # Load Atlas configuration
    config = load_config()

    # Initialize document processor
    doc_processor = AtlasDocumentProcessor(config)

    # Find all HTML files recursively
    html_files = glob.glob(os.path.join(input_dir, "**/*.html"), recursive=True)

    if not html_files:
        print(f"❌ No HTML files found in {input_dir}")
        return 0, 0

    print(f"📁 Found {len(html_files)} HTML files to process")

    # Create processed directory to avoid reprocessing
    processed_dir = os.path.join(input_dir, "processed")
    os.makedirs(processed_dir, exist_ok=True)

    successful_count = 0
    failed_count = 0

    for i, html_file in enumerate(html_files[:max_files]):
        print(
            f"\n📄 Processing file {i+1}/{min(len(html_files), max_files)}: {os.path.basename(html_file)}"
        )

        try:
            # Decode the mangled filename
            original_name = os.path.basename(html_file)
            decoded_name = decode_utf8_filename(original_name)

            if decoded_name and decoded_name != original_name:
                print(f"   🔤 Decoded filename: {decoded_name[:100]}...")

            # Clean the filename for processing
            clean_name = clean_filename(decoded_name or original_name)
            temp_file = os.path.join(input_dir, f"temp_{clean_name}.html")

            # Copy to temporary clean filename
            shutil.copy2(html_file, temp_file)

            try:
                # Process through Atlas document processor
                result = doc_processor.process_document(temp_file)

                if result and result.get("processing_status") == "success":
                    print(
                        f"   ✅ Successfully processed: {result.get('uid', 'unknown')}"
                    )

                    # Move original file to processed directory
                    processed_file = os.path.join(processed_dir, original_name)
                    shutil.move(html_file, processed_file)
                    successful_count += 1

                else:
                    print(
                        f"   ❌ Processing failed: {result.get('error', 'Unknown error') if result else 'No result'}"
                    )
                    failed_count += 1

            finally:
                # Clean up temporary file
                if os.path.exists(temp_file):
                    os.remove(temp_file)

        except Exception as e:
            print(f"   💥 Exception processing {html_file}: {str(e)}")
            failed_count += 1

    print(f"\n🎯 Processing complete:")
    print(f"   ✅ Successful: {successful_count}")
    print(f"   ❌ Failed: {failed_count}")
    print(f"   📁 Remaining: {len(html_files) - successful_count - failed_count}")

    return successful_count, failed_count


def main():
    """Main function to run the HTML file processor."""
    import argparse

    parser = argparse.ArgumentParser(description="Fix and process mangled HTML files")
    parser.add_argument(
        "--input-dir", default="inputs", help="Directory containing mangled HTML files"
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=100,
        help="Maximum number of files to process in one run",
    )
    parser.add_argument(
        "--test-decode",
        action="store_true",
        help="Just test filename decoding without processing",
    )

    args = parser.parse_args()

    if args.test_decode:
        # Test filename decoding
        html_files = glob.glob(os.path.join(args.input_dir, "*.html"))
        print(f"Testing filename decoding for {len(html_files)} files:")

        for html_file in html_files[:10]:  # Test first 10
            original = os.path.basename(html_file)
            decoded = decode_utf8_filename(original)
            cleaned = clean_filename(decoded or original)

            print(f"\nOriginal: {original}")
            print(f"Decoded:  {decoded}")
            print(f"Cleaned:  {cleaned}")

    else:
        # Process the files
        successful, failed = process_mangled_html_files(args.input_dir, args.max_files)

        if successful > 0:
            print(f"\n🚀 Success! Processed {successful} HTML files into Atlas.")
            print("   Run the script again to process more files.")
        else:
            print(f"\n😞 No files were successfully processed. Check the errors above.")


if __name__ == "__main__":
    main()
