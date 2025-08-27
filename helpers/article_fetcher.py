import hashlib
import os
import re
from datetime import datetime
from pathlib import Path
from time import sleep

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth
from readability import Document

from helpers.article_strategies import ArticleFetcher
from helpers.metadata_manager import MetadataManager, ContentType, ProcessingStatus
from helpers.retry_queue import enqueue
from helpers.utils import (calculate_hash, generate_markdown_summary,
                           log_error, log_info)

# --- Constants ---
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
GOOGLEBOT_USER_AGENT = (
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
)
PAYWALL_PHRASES = [
    "subscribe to continue",
    "create a free account",
    "sign in to read",
    "unlock this story",
    "your free articles",
    "to continue reading",
    "subscribe now",
    "subscription required",
    "premium content",
    "members only",
    "register to continue",
    "paid subscribers only",
    "subscribe for full access",
    "subscribe for unlimited access",
    "login to read more",
    "create an account to continue",
    "please enable js",
    "please enable javascript",
    "disable any ad blocker",
    "javascript is disabled",
    "javascript required",
    "enable javascript",
    "this site requires javascript",
    "javascript must be enabled",
]
PAYWALL_ELEMENTS = [
    ".paywall",
    ".subscription-required",
    ".premium-content",
    ".register-wall",
    ".subscription-wall",
    ".paid-content",
    "#paywall",
    "#subscribe-overlay",
    "#subscription-overlay",
    "div[data-paywall]",
    "[data-require-auth]",
]
MIN_WORD_COUNT = 150
# Ratio of title length to content length that suggests truncation
TITLE_CONTENT_RATIO_THRESHOLD = 0.1

# NOTE: As of July 2025, all article fetching is now handled by ArticleFetcher (strategy orchestrator) from article_strategies.py.
# This module now delegates all content fetching to the unified strategy pattern for maintainability and testability.


def is_truncated(html_content: str, log_path: str) -> bool:
    """
    Checks if the content is likely truncated or behind a paywall using multiple heuristics:
    1. Presence of paywall-related phrases in the text
    2. Presence of paywall-related HTML elements
    3. Unusually short content (word count below threshold)
    4. Suspicious ratio between title length and content length
    5. Presence of login/subscription forms in prominent positions

    Returns True if content appears to be truncated or paywalled.
    """
    if not html_content:
        return False

    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text().lower()

    # 1. Check for paywall phrases
    for phrase in PAYWALL_PHRASES:
        if phrase in text:
            log_info(log_path, f"Paywall phrase '{phrase}' detected.")
            return True

    # 2. Check for paywall HTML elements
    for selector in PAYWALL_ELEMENTS:
        if soup.select(selector):
            log_info(log_path, f"Paywall element '{selector}' detected.")
            return True

    # 3. Extract title and check title-to-content ratio
    title_tag = soup.find("title")
    if title_tag and title_tag.text:
        title_length = len(title_tag.text.strip())
        content_length = len(text)

        if content_length > 0:
            ratio = title_length / content_length
            if ratio > TITLE_CONTENT_RATIO_THRESHOLD:
                log_info(
                    log_path,
                    f"Suspicious title-to-content ratio: {ratio:.2f}. Likely truncated.",
                )
                return True

    # 4. Check for login forms near the top of the page
    form_tags = soup.find_all("form")
    for form in form_tags[:3]:  # Check only the first few forms
        form_text = form.get_text().lower()
        if any(
            word in form_text for word in ["login", "sign in", "subscribe", "register"]
        ):
            log_info(
                log_path, "Login/subscription form detected near the top of the page."
            )
            return True

    # 5. Check word count from readability's summary
    try:
        summary_html = Document(html_content).summary()
        summary_text = BeautifulSoup(summary_html, "html.parser").get_text()
        word_count = len(summary_text.split())
        if word_count < MIN_WORD_COUNT:
            log_info(
                log_path,
                f"Content is very short ({word_count} words). Likely a teaser.",
            )
            return True
    except Exception:
        # If readability fails, we can fall back to the raw text word count
        word_count = len(text.split())
        if word_count < MIN_WORD_COUNT:
            log_info(
                log_path,
                f"Content is very short ({word_count} words, raw). Likely a teaser.",
            )
            return True

    return False


def _fetch_with_12ft(url: str, log_path: str) -> str:
    """
    Tries to fetch the content via 12ft.io proxy.
    """
    try:
        proxy_url = f"https://12ft.io/{url}"
        log_info(log_path, f"Attempting to fetch {url} via 12ft.io.")
        headers = {"User-Agent": USER_AGENT}
        response = requests.get(proxy_url, headers=headers, timeout=20)
        response.raise_for_status()
        log_info(log_path, f"Successfully fetched {url} via 12ft.io.")
        return response.text
    except requests.exceptions.RequestException as e:
        log_error(log_path, f"12ft.io fetch failed for {url}: {e}")
        return None


def fetch_and_save_articles(urls, output_dir):

    for url in urls:
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context()
                stealth(context)  # <- apply stealth to the context

                page = context.new_page()
                page.goto(url, timeout=60000)

                html = page.content()
                title = page.title()

                # Use readability to extract content
                doc = Document(html)
                content = doc.summary()
                text = markdownify(content)

                # Save to file (adjust as needed)
                filename = re.sub(r"[^a-zA-Z0-9]+", "-", title).strip("-")[:60] + ".md"
                filepath = Path(output_dir) / filename
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(text)

                page.close()
                context.close()
                browser.close()

        except Exception as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")


def _fetch_from_wayback_machine(url: str, log_path: str) -> str:
    """
    Tries to fetch the content from the Internet Archive's Wayback Machine.
    Uses the "Wayback Availability JSON API" as documented here:
    https://archive.org/help/wayback_api.php
    """
    try:
        log_info(log_path, f"Attempting to fetch {url} from the Wayback Machine.")
        # 1. Check if the URL is available on the Wayback Machine
        availability_api_url = f"http://archive.org/wayback/available?url={url}"
        response = requests.get(availability_api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data.get("archived_snapshots"):
            log_info(log_path, f"No snapshot found in Wayback Machine for {url}.")
            return None

        # 2. Get the URL of the most recent snapshot
        snapshot_url = data["archived_snapshots"]["closest"]["url"]
        log_info(log_path, f"Found snapshot: {snapshot_url}. Fetching raw content.")

        # 3. Fetch the raw content from the snapshot (append 'id_' to the timestamp)
        raw_content_url = snapshot_url.replace("/web/", "/web/id_/")

        headers = {"User-Agent": USER_AGENT}
        content_response = requests.get(raw_content_url, headers=headers, timeout=20)
        content_response.raise_for_status()

        log_info(log_path, f"Successfully fetched {url} from Wayback Machine.")
        return content_response.text

    except requests.exceptions.RequestException as e:
        log_error(log_path, f"Wayback Machine fetch failed for {url}: {e}")
        return None
    except Exception as e:
        log_error(
            log_path,
            f"An unexpected error occurred during Wayback Machine fetch for {url}: {e}",
        )
        return None


def _fetch_from_archive_today(url: str, log_path: str) -> str:
    """
    Tries to fetch the content from archive.today (also known as archive.is).
    First checks if the URL is already archived, and if not, tries to request a new archive.

    Args:
        url: The original URL to fetch from archive.today
        log_path: Path to the log file

    Returns:
        The HTML content from archive.today or None if unsuccessful
    """
    try:
        log_info(log_path, f"Attempting to fetch {url} from archive.today.")

        # First, check if the URL is already archived
        archive_check_url = f"https://archive.today/submit/?url={url}"
        headers = {"User-Agent": USER_AGENT}
        response = requests.get(archive_check_url, headers=headers, timeout=20)
        response.raise_for_status()

        # Parse the response to find existing archives
        soup = BeautifulSoup(response.text, "html.parser")

        # Look for existing archives in the results
        archive_links = soup.select("div.results-right a")
        if archive_links:
            # Use the most recent archive (first link)
            archive_url = archive_links[0].get("href")
            if not archive_url.startswith("http"):
                archive_url = f"https://archive.today{archive_url}"

            log_info(
                log_path, f"Found existing archive at {archive_url}. Fetching content."
            )

            # Fetch the archived content
            archive_response = requests.get(archive_url, headers=headers, timeout=30)
            archive_response.raise_for_status()

            log_info(log_path, f"Successfully fetched {url} from archive.today.")
            return archive_response.text
        else:
            # No existing archive found, try to create a new one
            log_info(log_path, "No existing archive found. Requesting a new archive.")

            # archive.today requires a specific submission format
            submit_url = "https://archive.today/submit/"
            data = {"url": url}

            submit_response = requests.post(
                submit_url, data=data, headers=headers, timeout=60
            )

            # Check if submission was successful (this is tricky as archive.today doesn't provide clear success indicators)
            # Usually redirects to the archived page if successful
            if (
                submit_response.status_code == 200
                and "Submitting" in submit_response.text
            ):
                log_info(
                    log_path, "Archive request submitted. Waiting for processing..."
                )

                # Extract the job ID if available
                job_match = re.search(
                    r'id="DIVALREADY".*?href="([^"]+)"', submit_response.text
                )
                if job_match:
                    archive_url = job_match.group(1)
                    if not archive_url.startswith("http"):
                        archive_url = f"https://archive.today{archive_url}"

                    # Give archive.today some time to process the request
                    sleep(10)

                    # Now fetch the archived content
                    archive_response = requests.get(
                        archive_url, headers=headers, timeout=30
                    )
                    archive_response.raise_for_status()

                    log_info(
                        log_path,
                        f"Successfully created and fetched new archive for {url}.",
                    )
                    return archive_response.text

            log_error(log_path, "Failed to create or find archive.")
            return None

    except requests.exceptions.RequestException as e:
        log_error(log_path, f"Archive.today fetch failed for {url}: {e}")
        return None
    except Exception as e:
        log_error(
            log_path,
            f"An unexpected error occurred during archive.today fetch for {url}: {e}",
        )
        return None


def sanitize_filename(url):
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def fetch_and_save_article(url: str, config: dict) -> bool:
    """
    Fetch and save a single article from a URL.

    Args:
        url: The URL to fetch
        config: The application configuration dictionary

    Returns:
        bool: True if successful, False otherwise
    """
    output_path = config["article_output_path"]
    html_save_dir = os.path.join(output_path, "html")
    meta_save_dir = os.path.join(output_path, "metadata")
    md_save_dir = os.path.join(output_path, "markdown")
    log_path = os.path.join(output_path, "ingest.log")

    os.makedirs(html_save_dir, exist_ok=True)
    os.makedirs(meta_save_dir, exist_ok=True)
    os.makedirs(md_save_dir, exist_ok=True)

    # Keep old meta dict for compatibility, convert to ContentMetadata at end
    meta = {
        "title": None,
        "source": url,
        "date": datetime.now().isoformat(),
        "tags": [],
        "notes": [],
        "status": "started",
        "error": None,
        "content_path": None,
        "fetch_method": "unknown",
        "fetch_details": {
            "attempts": [],
            "successful_method": None,
            "is_truncated": False,
            "total_attempts": 0,
            "fetch_time": None,
        },
    }
    
    # Initialize MetadataManager for proper saving
    metadata_manager = MetadataManager(config)
    
    def convert_meta_to_content_metadata(meta_dict, file_id):
        """Convert old meta dict to ContentMetadata format."""
        from helpers.metadata_manager import FetchDetails
        
        # Convert status string to ProcessingStatus enum
        status_map = {
            "started": ProcessingStatus.STARTED,
            "success": ProcessingStatus.SUCCESS,
            "error": ProcessingStatus.ERROR,
            "pending": ProcessingStatus.PENDING,
            "retry": ProcessingStatus.RETRY,
            "skipped": ProcessingStatus.SKIPPED
        }
        
        # Create FetchDetails from the old format
        fetch_details = FetchDetails(
            attempts=[],  # Could convert from attempts list if needed
            successful_method=meta_dict["fetch_details"].get("successful_method"),
            is_truncated=meta_dict["fetch_details"].get("is_truncated", False),
            total_attempts=meta_dict["fetch_details"].get("total_attempts", 0),
            fetch_time=meta_dict["fetch_details"].get("fetch_time")
        )
        
        # Create ContentMetadata
        metadata = metadata_manager.create_metadata(
            content_type=ContentType.ARTICLE,
            source=meta_dict["source"],
            title=meta_dict["title"] or "[no-title]"
        )
        
        # Set additional fields
        metadata.uid = file_id
        metadata.status = status_map.get(meta_dict["status"], ProcessingStatus.PENDING)
        metadata.error = meta_dict.get("error")
        metadata.content_path = meta_dict.get("content_path")
        metadata.tags = meta_dict.get("tags", [])
        metadata.notes = meta_dict.get("notes", [])
        metadata.fetch_method = meta_dict.get("fetch_method", "unknown")
        metadata.fetch_details = fetch_details
        metadata.date = meta_dict["date"]
        
        # Add any additional fields from meta to type_specific
        metadata.type_specific.update({
            "category_version": meta_dict.get("category_version"),
            "last_tagged_at": meta_dict.get("last_tagged_at"),
            "source_hash": meta_dict.get("source_hash"),
            "summary_text": meta_dict.get("summary_text"),
            "extract_error": meta_dict.get("extract_error")
        })
        
        return metadata

    from helpers.dedupe import link_uid

    file_id = link_uid(url)
    html_path = os.path.join(html_save_dir, f"{file_id}.html")
    meta_path = os.path.join(meta_save_dir, f"{file_id}.json")
    md_path = os.path.join(md_save_dir, f"{file_id}.md")

    # Check if metadata file already exists, if so, skip.
    if os.path.exists(meta_path):
        log_info(log_path, f"Article {file_id} ({url}) already processed. Skipping.")
        return True

    response_text = None

    # Replace all direct/fallback HTTP logic with:
    fetcher = ArticleFetcher()
    result = fetcher.fetch_with_fallbacks(url, log_path)
    if not result.success or not result.content:
        log_error(log_path, f"All fetch strategies failed for {url}: {result.error}")
        meta["status"] = "error"
        meta["error"] = result.error or "All fetch strategies failed"
        # Convert and save using MetadataManager
        content_metadata = convert_meta_to_content_metadata(meta, file_id)
        metadata_manager.save_metadata(content_metadata)
        # Add to retry queue

        enqueue(
            {
                "type": "article",
                "url": url,
                "file_id": file_id,
                "error": result.error or "All fetch strategies failed",
                "timestamp": datetime.now().isoformat(),
                "attempts": meta["fetch_details"]["total_attempts"],
            }
        )
        return False
    response_text = result.content
    meta["fetch_method"] = result.method
    meta["fetch_details"]["successful_method"] = result.method
    meta["fetch_details"]["is_truncated"] = getattr(result, "is_truncated", False)

    # Save the raw HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(response_text)

    # Parse with readability
    try:
        doc = Document(response_text)
        title = doc.title()
        meta["title"] = title
        content = doc.summary()

        # Convert HTML to Markdown
        from bs4 import BeautifulSoup

        BeautifulSoup(content, "html.parser")

        # Basic HTML to Markdown conversion
        from html2text import HTML2Text

        h2t = HTML2Text()
        h2t.ignore_links = False
        h2t.ignore_images = False
        h2t.ignore_tables = False
        markdown_content = h2t.handle(content)

        # Generate Markdown summary file
        md = generate_markdown_summary(
            title=title,
            source=url,
            date=meta["date"],
            tags=[],
            notes=[],
            content=markdown_content,
        )
        with open(md_path, "w", encoding="utf-8") as mdf:
            mdf.write(md)
        meta["content_path"] = md_path
        meta["status"] = "success"

        # Run evaluations
        try:
            from helpers.evaluation_utils import EvaluationFile
            from process.evaluate import (classify_content, extract_entities,
                                          summarize_text)

            eval_file = EvaluationFile(source_file_path=md_path, config=config)
            eval_file.add_evaluation(
                evaluator_id="ingestion_v1",
                eval_type="ingestion_check",
                result={"status": "success", "notes": "Article fetched and processed."},
            )

            # Run content classification
            classification_result = classify_content(markdown_content, config)
            if classification_result:
                eval_file.add_evaluation(
                    evaluator_id="openrouter_classifier_v1",
                    eval_type="content_classification",
                    result={
                        "classification": classification_result,
                        "model": config.get("llm_model"),
                    },
                )

                # Add tags to metadata
                tier_1_cats = classification_result.get("tier_1_categories", [])
                meta["tags"].extend(tier_1_cats)
                meta["tags"].extend(classification_result.get("tier_2_sub_tags", []))
                meta["category_version"] = "v1.0"
                meta["last_tagged_at"] = datetime.now().isoformat()
                meta["source_hash"] = calculate_hash(md_path)

            # Generate summary
            summary = summarize_text(markdown_content, config)
            if summary:
                eval_file.add_evaluation(
                    evaluator_id="openrouter_summary_v1",
                    eval_type="summary",
                    result={"summary_text": summary, "model": config.get("llm_model")},
                )

            # Extract entities
            entities = extract_entities(markdown_content, config)
            if entities:
                eval_file.add_evaluation(
                    evaluator_id="openrouter_entities_v1",
                    eval_type="entity_extraction",
                    result={"entities": entities, "model": config.get("llm_model")},
                )

            eval_file.save()
        except Exception as e:
            log_error(
                log_path,
                f"Failed to create or update evaluation file for {md_path}: {e}",
            )

    except Exception as e:
        log_error(log_path, f"Failed to parse or process content from {url}: {e}")
        meta["status"] = "error"
        meta["error"] = str(e)
        # Add to retry queue

        enqueue(
            {
                "type": "article_processing",
                "url": url,
                "file_id": file_id,
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
                "html_path": html_path,  # So we can retry processing without refetching
            }
        )

    # Convert and save using MetadataManager
    content_metadata = convert_meta_to_content_metadata(meta, file_id)
    metadata_manager.save_metadata(content_metadata)

    return meta["status"] == "success"
