#!/usr/bin/env python3
"""
Send Content to Atlas - Easy Entry Point
Simple interface to send URLs, files, or text to Atlas for processing.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

sys.path.append(os.path.dirname(__file__))

from helpers.config import load_config
from ingest.capture.bulletproof_capture import capture_url, capture_file, capture_text
from ingest.link_dispatcher import detect_url_type
from helpers.retry_queue import enqueue


class AtlasSubmitter:
    """Easy interface to submit content to Atlas"""
    
    def __init__(self):
        self.config = load_config()
        
    def submit_url(self, url: str, metadata: dict = None) -> dict:
        """Submit a single URL to Atlas"""
        
        # Detect content type
        content_type = detect_url_type(url)
        
        print(f"🔍 Detected content type: {content_type}")
        print(f"📎 Submitting: {url}")
        
        # Use bulletproof capture to ensure we never lose the URL
        result = capture_url(url, metadata or {})
        
        if result.success:
            print(f"✅ Successfully captured with ID: {result.capture_id}")
            
            # Also add to processing queue for immediate processing
            enqueue({
                "url": url,
                "type": content_type,
                "metadata": metadata or {},
                "timestamp": datetime.now().isoformat(),
                "capture_id": result.capture_id
            })
            
            return {
                "success": True,
                "capture_id": result.capture_id,
                "content_type": content_type
            }
        else:
            print(f"❌ Failed to capture: {result.error}")
            return {
                "success": False,
                "error": result.error
            }
    
    def submit_file(self, file_path: str, metadata: dict = None) -> dict:
        """Submit a file to Atlas"""
        
        file_path = Path(file_path)
        if not file_path.exists():
            return {"success": False, "error": f"File not found: {file_path}"}
        
        print(f"📄 Submitting file: {file_path}")
        
        # Use bulletproof capture for files
        result = capture_file(str(file_path), metadata or {})
        
        if result.success:
            print(f"✅ Successfully captured file with ID: {result.capture_id}")
            return {
                "success": True,
                "capture_id": result.capture_id,
                "file_type": file_path.suffix
            }
        else:
            print(f"❌ Failed to capture file: {result.error}")
            return {
                "success": False,
                "error": result.error
            }
    
    def submit_text(self, text: str, title: str = None, metadata: dict = None) -> dict:
        """Submit raw text to Atlas"""
        
        print(f"📝 Submitting text content: {title or 'Untitled'}")
        
        # Create text metadata
        text_metadata = {
            "title": title or "Direct Text Submission",
            "content": text,
            "submission_time": datetime.now().isoformat(),
            **(metadata or {})
        }
        
        # Use bulletproof capture for text
        result = capture_text(text, title or "Direct Text Submission", text_metadata)
        
        if result.success:
            print(f"✅ Successfully captured text with ID: {result.capture_id}")
            return {
                "success": True,
                "capture_id": result.capture_id,
                "content_length": len(text)
            }
        else:
            print(f"❌ Failed to capture text: {result.error}")
            return {
                "success": False,
                "error": result.error
            }
    
    def submit_url_list(self, url_file: str) -> dict:
        """Submit a file containing multiple URLs"""
        
        url_file = Path(url_file)
        if not url_file.exists():
            return {"success": False, "error": f"URL file not found: {url_file}"}
        
        print(f"📋 Processing URL list: {url_file}")
        
        urls = []
        with open(url_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    urls.append(line)
        
        print(f"📊 Found {len(urls)} URLs to process")
        
        results = []
        for i, url in enumerate(urls, 1):
            print(f"\n🔄 Processing {i}/{len(urls)}: {url}")
            result = self.submit_url(url)
            results.append({"url": url, **result})
        
        successful = sum(1 for r in results if r["success"])
        
        print(f"\n📈 Summary: {successful}/{len(urls)} URLs successfully submitted")
        
        return {
            "success": True,
            "total_urls": len(urls),
            "successful": successful,
            "failed": len(urls) - successful,
            "results": results
        }


def main():
    """Main CLI interface"""
    
    parser = argparse.ArgumentParser(description="Send content to Atlas for processing")
    
    # Content type options
    parser.add_argument("--url", help="Submit a single URL")
    parser.add_argument("--file", help="Submit a local file")
    parser.add_argument("--text", help="Submit raw text content")
    parser.add_argument("--url-list", help="Submit a file containing multiple URLs")
    
    # Metadata options
    parser.add_argument("--title", help="Title for the content")
    parser.add_argument("--tags", help="Comma-separated tags")
    parser.add_argument("--source", help="Source attribution")
    parser.add_argument("--priority", type=int, help="Processing priority (1-10)")
    
    # Processing options
    parser.add_argument("--immediate", action="store_true", 
                       help="Process immediately (default: queue for later)")
    parser.add_argument("--format", choices=["json", "simple"], default="simple",
                       help="Output format")
    
    args = parser.parse_args()
    
    # Build metadata
    metadata = {}
    if args.title:
        metadata["title"] = args.title
    if args.tags:
        metadata["tags"] = [tag.strip() for tag in args.tags.split(",")]
    if args.source:
        metadata["source"] = args.source
    if args.priority:
        metadata["priority"] = args.priority
    if args.immediate:
        metadata["immediate_processing"] = True
    
    # Initialize submitter
    submitter = AtlasSubmitter()
    
    # Process based on content type
    result = None
    
    if args.url:
        result = submitter.submit_url(args.url, metadata)
    elif args.file:
        result = submitter.submit_file(args.file, metadata)
    elif args.text:
        result = submitter.submit_text(args.text, args.title, metadata)
    elif args.url_list:
        result = submitter.submit_url_list(args.url_list)
    else:
        parser.print_help()
        print("\n❌ Please specify content to submit (--url, --file, --text, or --url-list)")
        return
    
    # Output results
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        if result["success"]:
            print(f"\n🎉 Content successfully submitted to Atlas!")
            if "capture_id" in result:
                print(f"📋 Tracking ID: {result['capture_id']}")
        else:
            print(f"\n💥 Submission failed: {result.get('error', 'Unknown error')}")


if __name__ == "__main__":
    main()