#!/usr/bin/env python3
"""
Simple Instapaper Backlog Processor
Uses existing Atlas infrastructure to process Instapaper backlog.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

sys.path.append(os.path.dirname(__file__))

from helpers.config import load_config
from helpers.instapaper_ingestor import InstapaperIngestor
from helpers.article_strategies import DirectFetchStrategy, PlaywrightStrategy, GooglebotStrategy
from helpers.retry_queue import enqueue
from helpers.utils import log_info, log_error


def main():
    """Run Instapaper processing using existing infrastructure"""
    
    print("🚀 Starting Instapaper Backlog Processing")
    print("=" * 60)
    
    config = load_config()
    
    # Create results directory
    output_dir = Path("testing/instapaper_results")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize logging
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = output_dir / f"instapaper_run_{timestamp}.log"
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "start_time": timestamp,
        "total_processed": 0,
        "successful": 0,
        "failed": 0,
        "methods_used": {},
        "errors": []
    }
    
    print(f"📊 Logs will be saved to: {log_file}")
    
    # Method 1: Try direct Instapaper scraping
    print("\n🔍 Method 1: Direct Instapaper scraping")
    try:
        ingestor = InstapaperIngestor(config)
        
        # Log the attempt
        log_info(str(log_file), "Starting Instapaper direct scraping")
        
        # Try to scrape Instapaper directly  
        print("🔗 Attempting to scrape Instapaper bookmarks...")
        
        # This will use the existing Instapaper scraping logic
        success = ingestor.scrape_instapaper()
        
        if success:
            print("✅ Instapaper direct scraping successful!")
            results["successful"] += 1
            results["methods_used"]["instapaper_direct"] = 1
            log_info(str(log_file), "Instapaper direct scraping completed successfully")
        else:
            print("⚠️  Instapaper direct scraping failed, trying fallbacks...")
            results["failed"] += 1
            results["errors"].append("Instapaper direct scraping failed")
            log_error(str(log_file), "Instapaper direct scraping failed")
            
    except Exception as e:
        print(f"❌ Error with Instapaper scraping: {str(e)}")
        results["errors"].append(f"Instapaper scraping error: {str(e)}")
        log_error(str(log_file), f"Instapaper scraping exception: {str(e)}")
    
    results["total_processed"] += 1
    
    # Method 2: Try Instapaper API export
    print("\n🔍 Method 2: Instapaper API export")
    try:
        print("🔗 Attempting Instapaper API export...")
        
        # Use the existing instapaper_data_dump.py
        result = os.system("source atlas_venv/bin/activate && python3 instapaper_data_dump.py")
        
        if result == 0:
            print("✅ Instapaper API export successful!")
            results["successful"] += 1
            results["methods_used"]["instapaper_api"] = results["methods_used"].get("instapaper_api", 0) + 1
            log_info(str(log_file), "Instapaper API export completed successfully")
        else:
            print("⚠️  Instapaper API export failed")
            results["failed"] += 1
            results["errors"].append("Instapaper API export failed")
            log_error(str(log_file), "Instapaper API export failed")
            
    except Exception as e:
        print(f"❌ Error with Instapaper API: {str(e)}")
        results["errors"].append(f"Instapaper API error: {str(e)}")
        log_error(str(log_file), f"Instapaper API exception: {str(e)}")
    
    results["total_processed"] += 1
    
    # Method 3: Process any existing CSV files
    print("\n🔍 Method 3: Process existing CSV files")
    try:
        # Look for any Instapaper CSV files
        csv_files = list(Path(".").glob("*.csv")) + list(Path("inputs/").glob("*.csv"))
        
        if csv_files:
            for csv_file in csv_files:
                print(f"📄 Found CSV file: {csv_file}")
                
                # Use the existing CSV processor
                result = os.system(f"source atlas_venv/bin/activate && python3 run.py --instapaper-csv {csv_file}")
                
                if result == 0:
                    print(f"✅ CSV file {csv_file} processed successfully!")
                    results["successful"] += 1
                    results["methods_used"]["csv_processing"] = results["methods_used"].get("csv_processing", 0) + 1
                    log_info(str(log_file), f"CSV file {csv_file} processed successfully")
                else:
                    print(f"⚠️  CSV file {csv_file} processing failed")
                    results["failed"] += 1
                    results["errors"].append(f"CSV processing failed: {csv_file}")
                    log_error(str(log_file), f"CSV file {csv_file} processing failed")
                    
                results["total_processed"] += 1
        else:
            print("📄 No CSV files found")
            log_info(str(log_file), "No CSV files found for processing")
            
    except Exception as e:
        print(f"❌ Error processing CSV files: {str(e)}")
        results["errors"].append(f"CSV processing error: {str(e)}")
        log_error(str(log_file), f"CSV processing exception: {str(e)}")
    
    # Save final results
    results_file = output_dir / f"results_{timestamp}.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print final summary
    print("\n" + "=" * 60)
    print("📊 FINAL PROCESSING SUMMARY")
    print("=" * 60)
    print(f"⏰ Timestamp: {results['timestamp']}")
    print(f"📁 Results saved to: {results_file}")
    print(f"📋 Log saved to: {log_file}")
    print(f"🔢 Total methods attempted: {results['total_processed']}")
    print(f"✅ Successful: {results['successful']}")
    print(f"❌ Failed: {results['failed']}")
    
    if results['successful'] > 0:
        success_rate = (results['successful'] / results['total_processed']) * 100
        print(f"📈 Success rate: {success_rate:.1f}%")
        
        print(f"\n🎯 Methods that worked:")
        for method, count in results['methods_used'].items():
            print(f"  • {method}: {count}")
    
    if results['errors']:
        print(f"\n⚠️  Errors encountered:")
        for error in results['errors'][:5]:  # Show first 5 errors
            print(f"  • {error}")
    
    print(f"\n🎉 Processing complete!")
    
    # Suggest next steps
    if results['successful'] > 0:
        print(f"\n💡 Next steps:")
        print(f"  • Check output directories for downloaded content")
        print(f"  • Review logs for any processing details: {log_file}")
        print(f"  • Use Atlas search to find your content")
    else:
        print(f"\n🔧 Troubleshooting:")
        print(f"  • Check Instapaper credentials in .env file")
        print(f"  • Verify network connectivity")
        print(f"  • Review error log: {log_file}")


if __name__ == "__main__":
    main()