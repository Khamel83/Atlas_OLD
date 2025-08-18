#!/usr/bin/env python3
"""
Atlas Content Export CLI
Command-line interface for exporting Atlas content in multiple formats
"""

import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import json

# Add Atlas helpers to path
sys.path.append(str(Path(__file__).parent.parent))

from helpers.content_exporter import ContentExporter
from helpers.config import load_config

def parse_date_range(date_str):
    """Parse date range string into datetime objects"""
    if not date_str:
        return None
        
    if date_str.lower() == "today":
        return datetime.now().strftime("%Y-%m-%d")
    elif date_str.lower() == "yesterday":
        return (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    elif date_str.lower() == "week":
        return (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    elif date_str.lower() == "month":
        return (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    else:
        # Assume it's a date string
        return date_str

def progress_callback(current, total, message):
    """Progress callback for batch exports"""
    percent = (current / total) * 100 if total > 0 else 0
    print(f"\r[{percent:5.1f}%] {message}...", end="", flush=True)
    if current == total - 1:
        print()  # New line when complete

def main():
    parser = argparse.ArgumentParser(description="Export Atlas content in multiple formats")
    
    # Output format
    parser.add_argument("--format", "-f", 
                       choices=["markdown", "json", "csv", "obsidian", "notion", "anki"],
                       default="markdown",
                       help="Export format")
    
    # Output location
    parser.add_argument("--output", "-o",
                       help="Output directory or file path")
    
    # Content filters
    parser.add_argument("--speaker", 
                       help="Filter by speaker name (partial match)")
    
    parser.add_argument("--podcast",
                       help="Filter by podcast name (partial match)")
    
    parser.add_argument("--topic",
                       help="Filter by topic/subject (partial match)")
    
    parser.add_argument("--content-type",
                       choices=["article", "podcast", "transcript", "document"],
                       help="Filter by content type")
    
    parser.add_argument("--date-from",
                       help="Start date (YYYY-MM-DD, 'today', 'yesterday', 'week', 'month')")
    
    parser.add_argument("--date-to", 
                       help="End date (YYYY-MM-DD)")
    
    parser.add_argument("--limit", type=int,
                       help="Maximum number of items to export")
    
    # Specific content IDs
    parser.add_argument("--ids",
                       help="Specific content IDs to export (comma-separated)")
    
    # Template and customization
    parser.add_argument("--template",
                       help="Custom template name for formatting")
    
    # Batch operations
    parser.add_argument("--batch-config",
                       help="JSON file with batch export configurations")
    
    # Preview mode
    parser.add_argument("--preview", action="store_true",
                       help="Preview what would be exported without writing files")
    
    # Verbose output
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")
    
    args = parser.parse_args()
    
    # Load configuration and set database path
    try:
        config = load_config()
        # Try multiple potential database locations
        possible_db_paths = [
            config.get("database", {}).get("path", "data/atlas.db"),
            "data/podcasts/atlas_podcasts.db",
            "data/atlas.db"
        ]
        
        db_path = None
        for path in possible_db_paths:
            if Path(path).exists():
                db_path = path
                break
                
        if not db_path:
            db_path = "data/podcasts/atlas_podcasts.db"  # Default to podcast DB
            
    except Exception as e:
        print(f"Error loading config: {e}")
        db_path = "data/podcasts/atlas_podcasts.db"
    
    # Initialize exporter
    exporter = ContentExporter(db_path)
    
    if args.batch_config:
        # Batch export mode
        return run_batch_export(exporter, args)
    else:
        # Single export mode
        return run_single_export(exporter, args)

def run_single_export(exporter, args):
    """Run a single export operation"""
    
    # Build filters
    filters = {}
    if args.speaker:
        filters["speaker"] = args.speaker
    if args.podcast:
        filters["podcast"] = args.podcast
    if args.topic:
        filters["topic"] = args.topic
    if args.content_type:
        filters["content_type"] = args.content_type
    if args.date_from:
        filters["date_from"] = parse_date_range(args.date_from)
    if args.date_to:
        filters["date_to"] = parse_date_range(args.date_to)
    if args.limit:
        filters["limit"] = args.limit
    
    # Handle specific IDs
    content_ids = None
    if args.ids:
        content_ids = [id.strip() for id in args.ids.split(",")]
    
    # Set default output path if not provided
    output_path = args.output
    if not output_path and not args.preview:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"exports/atlas_export_{args.format}_{timestamp}"
    
    if args.verbose:
        print("Export configuration:")
        print(f"  Format: {args.format}")
        print(f"  Output: {output_path or 'preview mode'}")
        print(f"  Filters: {filters}")
        if content_ids:
            print(f"  Content IDs: {content_ids}")
        print()
    
    try:
        # Perform export
        result = exporter.export_content(
            content_ids=content_ids,
            format_type=args.format,
            filters=filters,
            output_path=output_path if not args.preview else None,
            template=args.template
        )
        
        if result["status"] == "success":
            print("✅ Export successful!")
            print(f"   Content items: {result['content_count']}")
            print(f"   Format: {result['format']}")
            
            if args.preview:
                print("   Preview mode - no files written")
                if args.verbose and "data" in result:
                    if isinstance(result["data"], list):
                        print(f"   Would create {len(result['data'])} files")
                        for item in result["data"][:3]:  # Show first 3
                            if isinstance(item, dict) and "filename" in item:
                                print(f"     - {item['filename']}")
                        if len(result["data"]) > 3:
                            print(f"     ... and {len(result['data']) - 3} more files")
            else:
                print(f"   Files created: {len(result.get('files', []))}")
                if args.verbose:
                    for file_path in result.get("files", []):
                        print(f"     - {file_path}")
        else:
            print(f"❌ Export failed: {result.get('message', 'Unknown error')}")
            return 1
            
    except Exception as e:
        print(f"❌ Export error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1
    
    return 0

def run_batch_export(exporter, args):
    """Run batch export from configuration file"""
    
    try:
        with open(args.batch_config, 'r') as f:
            batch_configs = json.load(f)
    except Exception as e:
        print(f"❌ Error loading batch config: {e}")
        return 1
    
    if not isinstance(batch_configs, list):
        print("❌ Batch config must be a list of export configurations")
        return 1
    
    print(f"🚀 Starting batch export with {len(batch_configs)} configurations...")
    
    try:
        result = exporter.batch_export(
            batch_configs, 
            progress_callback=progress_callback if args.verbose else None
        )
        
        print("✅ Batch export completed!")
        print(f"   Total exports: {result['total_exports']}")
        print(f"   Successful: {result['successful']}")
        print(f"   Failed: {result['total_exports'] - result['successful']}")
        
        if args.verbose:
            for i, export_result in enumerate(result["results"]):
                status_icon = "✅" if export_result["status"] == "success" else "❌"
                config = batch_configs[i]
                print(f"   {status_icon} {config.get('format_type', 'unknown')} export: {export_result.get('content_count', 0)} items")
        
        return 0 if result["successful"] == result["total_exports"] else 1
        
    except Exception as e:
        print(f"❌ Batch export error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())