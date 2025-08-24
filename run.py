# run.py

import argparse
import logging
import os
from pathlib import Path


from helpers.article_fetcher import fetch_and_save_articles
from helpers.config import load_config
from helpers.podcast_ingestor import ingest_podcasts
from helpers.safety_monitor import check_pre_run_safety
from helpers.utils import setup_logging
from helpers.youtube_ingestor import ingest_youtube_history
from ingest.link_dispatcher import process_instapaper_csv, process_url_file
from process.recategorize import recategorize_all_content


def main():
    """
    Main function to run the Atlas pipeline.
    """
    # Load environment and configuration
    config = load_config()

    # Safety and compliance check
    if not check_pre_run_safety(config):
        print("❌ Safety check failed. Exiting.")
        return

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run the Atlas pipeline")
    parser.add_argument("--articles", action="store_true", help="Run article ingestion")
    parser.add_argument("--podcasts", action="store_true", help="Run podcast ingestion")
    parser.add_argument("--transcripts", action="store_true", help="Run transcript discovery and polling")
    parser.add_argument("--youtube", action="store_true", help="Run YouTube ingestion")
    parser.add_argument(
        "--instapaper-csv",
        type=str,
        help="Path to a clean Instapaper CSV file to ingest",
    )
    parser.add_argument(
        "--recategorize", action="store_true", help="Run recategorization"
    )
    parser.add_argument("--all", action="store_true", help="Run all ingestion types")
    parser.add_argument(
        "--urls", type=str, help="Path to a file containing URLs to ingest"
    )
    args = parser.parse_args()

    # If no arguments are provided, show help
    if not any(vars(args).values()):
        parser.print_help()
        return

    # Setup logging
    log_file_path = os.path.join(config.get("data_directory"), "Full_Pipeline.log")
    setup_logging(log_file_path)
    logging.info("-------------------")
    logging.info("Atlas Pipeline Start")
    logging.info("-------------------")

    # Check for legacy retries.json and migrate if needed
    retries_json_path = Path("retries.json")
    if retries_json_path.exists():
        logging.info("Found legacy retries.json file. Migrating to new retry queue...")
        from scripts.migrate_retry_queue import migrate_retry_queue

        migrate_success = migrate_retry_queue(config)
        if migrate_success:
            logging.info("Migration completed successfully.")
        else:
            logging.error("Migration failed. Check the logs for details.")
            # Continue with the pipeline anyway

    # Run the requested ingestion types
    if args.all or args.articles:
        logging.info("Starting article ingestion...")
        
        # AUTOMATICALLY process ALL sources - no manual intervention required
        all_urls = []
        
        # 1. Get articles from inputs/articles.txt
        articles_file = "inputs/articles.txt"
        if os.path.exists(articles_file):
            with open(articles_file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
                all_urls.extend(urls)
                logging.info(f"Loaded {len(urls)} URLs from articles.txt")
        
        # 2. AUTOMATICALLY process Instapaper CSV
        instapaper_csv = "inputs/instapaper_export.csv"
        if os.path.exists(instapaper_csv):
            import csv
            csv_urls = []
            with open(instapaper_csv, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    url = row.get('URL', '').strip()
                    if (url.startswith(('http://', 'https://')) and 
                        not url.startswith('instapaper-private://') and
                        url not in all_urls):
                        csv_urls.append(url)
            all_urls.extend(csv_urls)
            logging.info(f"Auto-loaded {len(csv_urls)} URLs from instapaper_export.csv")
        
        # 3. Process all URLs with full recovery
        if all_urls:
            logging.info(f"Processing {len(all_urls)} total URLs with full recovery strategies")
            fetch_and_save_articles(all_urls, config.get('output_dir', 'output'))
        else:
            logging.warning("No URLs found to process")
            
        logging.info("Article ingestion complete.")

    # 4. AUTOMATICALLY process ALL uploaded files - no manual intervention
    if args.all or args.articles:
        logging.info("Starting automatic processing of uploaded files...")
        
        # Process saved HTML files
        saved_html_dir = Path("inputs/saved_html")
        if saved_html_dir.exists():
            html_files = list(saved_html_dir.glob("*.html"))
            if html_files:
                logging.info(f"Auto-processing {len(html_files)} uploaded HTML files")
                from helpers.document_ingestor import DocumentIngestor
                doc_ingestor = DocumentIngestor(config)
                for html_file in html_files:
                    try:
                        doc_ingestor.ingest_document(str(html_file))
                    except Exception as e:
                        logging.error(f"Failed to process {html_file.name}: {e}")
        
        # Process Docs files  
        docs_dir = Path("inputs/Docs")
        if docs_dir.exists():
            doc_files = list(docs_dir.glob("*.html")) + list(docs_dir.glob("*.pdf"))
            if doc_files:
                logging.info(f"Auto-processing {len(doc_files)} uploaded document files")
                from helpers.document_ingestor import DocumentIngestor
                doc_ingestor = DocumentIngestor(config)
                for doc_file in doc_files:
                    try:
                        doc_ingestor.ingest_document(str(doc_file))
                    except Exception as e:
                        logging.error(f"Failed to process {doc_file.name}: {e}")
        
        # Process saved emails
        saved_emails_dir = Path("inputs/saved_emails")
        if saved_emails_dir.exists():
            email_files = list(saved_emails_dir.glob("*"))
            if email_files:
                logging.info(f"Auto-processing {len(email_files)} uploaded email files")
                from helpers.email_ingestor import EmailIngestor
                email_ingestor = EmailIngestor(config)
                for email_file in email_files:
                    try:
                        email_ingestor.ingest_email(str(email_file))
                    except Exception as e:
                        logging.error(f"Failed to process {email_file.name}: {e}")
        
        logging.info("Uploaded file processing complete.")

    if args.all or args.podcasts:
        logging.info("Starting podcast ingestion...")
        ingest_podcasts(config)
        logging.info("Podcast ingestion complete.")

    if args.all or args.youtube:
        logging.info("Starting YouTube ingestion...")
        ingest_youtube_history(config)
        logging.info("YouTube ingestion complete.")

    if args.all or args.transcripts:
        logging.info("Starting transcript discovery and polling...")
        try:
            # Use existing TranscriptManager directly - no separate script needed
            import sys
            sys.modules['helpers.utils'] = type(sys)('helpers.utils') 
            sys.modules['helpers.utils'].log_info = lambda msg: logging.info(msg)
            sys.modules['helpers.utils'].log_error = lambda msg: logging.error(msg)
            
            from helpers.transcript_manager import TranscriptManager
            tm = TranscriptManager()
            
            # Discover and process transcripts
            transcripts = tm.discover_transcripts('auto', limit=50)
            processed = 0
            for transcript in transcripts:
                result = tm.fetch_transcript(transcript)
                if result:
                    processed += 1
                    
            logging.info(f"Transcript processing complete: {processed} new transcripts processed")
        except Exception as e:
            logging.error(f"Error in transcript processing: {e}")
            # Don't fail the whole pipeline for transcript errors

    if args.instapaper_csv:
        logging.info(f"Processing Instapaper CSV from {args.instapaper_csv}...")
        results = process_instapaper_csv(args.instapaper_csv, config)
        logging.info(
            f"Instapaper CSV processing complete. Processed {len(results['successful'])} URLs successfully."
        )
        logging.info(f"Skipped {len(results['duplicate'])} duplicate URLs.")
        logging.info(f"Failed to process {len(results['failed'])} URLs.")
        logging.info(f"Unsupported URL types: {len(results['unknown'])}")

    if args.urls:
        logging.info(f"Processing URLs from {args.urls}...")
        results = process_url_file(args.urls, config)
        logging.info(
            f"URL processing complete. Processed {len(results['successful'])} URLs successfully."
        )
        logging.info(f"Skipped {len(results['duplicate'])} duplicate URLs.")
        logging.info(f"Failed to process {len(results['failed'])} URLs.")
        logging.info(f"Unsupported URL types: {len(results['unknown'])}")

    if args.recategorize:
        logging.info("Starting recategorization...")
        recategorize_all_content(config)
        logging.info("Recategorization complete.")

    logging.info("-----------------")
    logging.info("Atlas Pipeline End")
    logging.info("-----------------")


if __name__ == "__main__":
    main()
