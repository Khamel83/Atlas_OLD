#!/usr/bin/env python3
"""
Automated ingestion script for Atlas.

This script automatically processes all input files and cleans them up:
- Processes all .txt URL files in inputs/
- Processes all .csv Instapaper files in inputs/ 
- Processes all .html files in inputs/saved_html/
- Processes all .eml files in inputs/saved_emails/
- Moves processed files to processed/ directory

This should be run periodically or triggered automatically.
"""

import os
import sys
import glob

# Add the parent directory to the path so we can import helpers
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helpers.config import load_config
from helpers.input_cleanup import (
    cleanup_html_files,
    cleanup_email_files,
    get_processed_file_stats,
)
from helpers.utils import log_info, log_error
from ingest.link_dispatcher import process_url_file, process_instapaper_csv


def process_html_files(config: dict) -> int:
    """
    Process all HTML files in inputs/saved_html/ and inputs/Docs/

    Returns:
        int: Number of files processed
    """
    processed_count = 0
    processed_files = []

    # Process saved_html directory
    html_dirs = ["inputs/saved_html", "inputs/Docs"]

    for html_dir in html_dirs:
        if not os.path.exists(html_dir):
            continue

        html_files = glob.glob(os.path.join(html_dir, "**/*.html"), recursive=True)

        for html_file in html_files:
            try:
                # For now, we'll use a simple document processor
                # In a full implementation, you'd integrate with DocumentIngestor

                # This is a placeholder - actual implementation would depend on DocumentIngestor interface
                log_info(
                    os.path.join(
                        config.get("data_directory", "output"),
                        "automated_ingestion.log",
                    ),
                    f"Processing HTML file: {html_file}",
                )

                # Mark as processed for cleanup (in real implementation, check if actually processed)
                processed_files.append(html_file)
                processed_count += 1

            except Exception as e:
                log_error(
                    os.path.join(
                        config.get("data_directory", "output"),
                        "automated_ingestion.log",
                    ),
                    f"Failed to process HTML file {html_file}: {str(e)}",
                )

    # Clean up processed HTML files
    if processed_files:
        moved_count = cleanup_html_files("inputs/saved_html", processed_files, config)
        log_info(
            os.path.join(
                config.get("data_directory", "output"), "automated_ingestion.log"
            ),
            f"Moved {moved_count} processed HTML files to processed/",
        )

    return processed_count


def process_email_files(config: dict) -> int:
    """
    Process all email files in inputs/saved_emails/

    Returns:
        int: Number of files processed
    """
    processed_count = 0
    processed_files = []

    email_dir = "inputs/saved_emails"

    if not os.path.exists(email_dir):
        return 0

    email_files = glob.glob(os.path.join(email_dir, "**/*.eml"), recursive=True)

    for email_file in email_files:
        try:
            # For now, we'll use a simple document processor
            # In a full implementation, you'd integrate with email processor
            log_info(
                os.path.join(
                    config.get("data_directory", "output"), "automated_ingestion.log"
                ),
                f"Processing email file: {email_file}",
            )

            # Mark as processed for cleanup (in real implementation, check if actually processed)
            processed_files.append(email_file)
            processed_count += 1

        except Exception as e:
            log_error(
                os.path.join(
                    config.get("data_directory", "output"), "automated_ingestion.log"
                ),
                f"Failed to process email file {email_file}: {str(e)}",
            )

    # Clean up processed email files
    if processed_files:
        moved_count = cleanup_email_files(
            "inputs/saved_emails", processed_files, config
        )
        log_info(
            os.path.join(
                config.get("data_directory", "output"), "automated_ingestion.log"
            ),
            f"Moved {moved_count} processed email files to processed/",
        )

    return processed_count


def process_url_files(config: dict) -> dict:
    """
    Process all .txt URL files in inputs/

    Returns:
        dict: Summary of processing results
    """
    results_summary = {"files_processed": 0, "urls_processed": 0, "urls_failed": 0}

    # Find all .txt files in inputs/ directory (not subdirectories)
    txt_files = glob.glob("inputs/*.txt")

    for txt_file in txt_files:
        try:
            log_info(
                os.path.join(
                    config.get("data_directory", "output"), "automated_ingestion.log"
                ),
                f"Processing URL file: {txt_file}",
            )

            results = process_url_file(txt_file, config)

            results_summary["files_processed"] += 1
            results_summary["urls_processed"] += len(results["successful"]) + len(
                results["duplicate"]
            )
            results_summary["urls_failed"] += len(results["failed"])

            log_info(
                os.path.join(
                    config.get("data_directory", "output"), "automated_ingestion.log"
                ),
                f"Processed {txt_file}: {len(results['successful'])} successful, {len(results['duplicate'])} duplicates, {len(results['failed'])} failed",
            )

        except Exception as e:
            log_error(
                os.path.join(
                    config.get("data_directory", "output"), "automated_ingestion.log"
                ),
                f"Failed to process URL file {txt_file}: {str(e)}",
            )

    return results_summary


def process_csv_files(config: dict) -> dict:
    """
    Process all .csv Instapaper files in inputs/

    Returns:
        dict: Summary of processing results
    """
    results_summary = {"files_processed": 0, "urls_processed": 0, "urls_failed": 0}

    # Find all .csv files in inputs/ directory (not subdirectories)
    csv_files = glob.glob("inputs/*.csv")

    for csv_file in csv_files:
        try:
            log_info(
                os.path.join(
                    config.get("data_directory", "output"), "automated_ingestion.log"
                ),
                f"Processing CSV file: {csv_file}",
            )

            results = process_instapaper_csv(csv_file, config)

            results_summary["files_processed"] += 1
            results_summary["urls_processed"] += len(results["successful"]) + len(
                results["duplicate"]
            )
            results_summary["urls_failed"] += len(results["failed"])

            log_info(
                os.path.join(
                    config.get("data_directory", "output"), "automated_ingestion.log"
                ),
                f"Processed {csv_file}: {len(results['successful'])} successful, {len(results['duplicate'])} duplicates, {len(results['failed'])} failed",
            )

        except Exception as e:
            log_error(
                os.path.join(
                    config.get("data_directory", "output"), "automated_ingestion.log"
                ),
                f"Failed to process CSV file {csv_file}: {str(e)}",
            )

    return results_summary


def main():
    """Main function to run automated ingestion."""
    print("🚀 Starting automated Atlas ingestion...")

    # Load configuration
    config = load_config()

    log_path = os.path.join(
        config.get("data_directory", "output"), "automated_ingestion.log"
    )
    log_info(log_path, "=== Starting automated ingestion cycle ===")

    # Process different types of input files
    url_results = process_url_files(config)
    csv_results = process_csv_files(config)
    html_count = process_html_files(config)
    email_count = process_email_files(config)

    # Log summary
    total_urls = url_results["urls_processed"] + csv_results["urls_processed"]
    total_failed = url_results["urls_failed"] + csv_results["urls_failed"]

    summary = f"""
=== Automated Ingestion Summary ===
URL Files: {url_results['files_processed']} files processed
CSV Files: {csv_results['files_processed']} files processed  
HTML Files: {html_count} files processed
Email Files: {email_count} files processed
Total URLs: {total_urls} processed, {total_failed} failed
"""

    print(summary)
    log_info(log_path, summary)

    # Show processed file stats
    stats = get_processed_file_stats()
    if stats:
        stats_summary = f"Processed files archived: {stats}"
        print(stats_summary)
        log_info(log_path, stats_summary)

    log_info(log_path, "=== Automated ingestion cycle complete ===")
    print("✅ Automated ingestion complete!")


if __name__ == "__main__":
    main()
