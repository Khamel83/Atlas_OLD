"""
Skyvern-Enhanced Article Ingestor

This module provides an intelligent browser automation ingestor that can:
1. Enhance existing article scraping with AI-powered web interaction
2. Handle complex sites that traditional scrapers can't access
3. Provide fallback for failed API or standard scraping attempts
"""

import hashlib
import os
import tempfile
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

try:
    # Skyvern MCP client - would be installed separately
    from skyvern import SkyverhClient

    SKYVERN_AVAILABLE = True
except ImportError:
    SkyverhClient = None
    SKYVERN_AVAILABLE = False

from helpers.base_ingestor import BaseIngestor, IngestorResult
from helpers.metadata_manager import ContentMetadata, ContentType
from helpers.utils import convert_html_to_markdown, log_error, log_info


class SkyvernEnhancedIngestor(BaseIngestor):
    """Enhanced article ingestor with Skyvern AI browser automation."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.content_type = ContentType.ARTICLE
        self.module_name = "skyvern_enhanced_ingestor"
        self._post_init()

        # Skyvern configuration
        self.skyvern_enabled = (
            config.get("SKYVERN_ENABLED", False) and SKYVERN_AVAILABLE
        )
        if self.skyvern_enabled:
            self.skyvern_client = SkyverhClient(
                base_url=config.get("SKYVERN_BASE_URL", "https://api.skyvern.com"),
                api_key=config.get("SKYVERN_API_KEY"),
            )
        else:
            self.skyvern_client = None

        # Fallback strategies
        self.use_traditional_scraping = config.get("USE_TRADITIONAL_SCRAPING", True)
        self.max_retries = config.get("SKYVERN_MAX_RETRIES", 2)

        print(
            f"[{self.module_name}] Initialized - Skyvern {'enabled' if self.skyvern_enabled else 'disabled'}"
        )

    def get_content_type(self) -> ContentType:
        return ContentType.ARTICLE

    def get_module_name(self) -> str:
        return self.module_name

    def is_supported_source(self, source: str) -> bool:
        """Check if source is a valid URL."""
        parsed = urlparse(source)
        return parsed.scheme in ["http", "https"]

    def fetch_content(
        self, source: str, metadata: ContentMetadata
    ) -> Tuple[bool, Optional[str]]:
        """
        Intelligent content fetching with multiple strategies.

        Strategy priority:
        1. Traditional requests (fast, works for most sites)
        2. Skyvern AI automation (handles complex cases)
        3. Enhanced extraction prompts for specific sites
        """
        strategies = []

        # Always try traditional first (fastest)
        if self.use_traditional_scraping:
            strategies.append(("traditional", self._fetch_traditional))

        # Add Skyvern strategies based on URL patterns
        if self.skyvern_enabled:
            if self._is_complex_site(source):
                strategies.append(("skyvern_complex", self._fetch_with_skyvern))
            if self._is_paywall_site(source):
                strategies.append(("skyvern_paywall", self._fetch_paywall_content))

        # Try each strategy in order
        for strategy_name, strategy_func in strategies:
            try:
                print(
                    f"[{self.module_name}] Trying {strategy_name} strategy for {source}"
                )
                success, result = strategy_func(source, metadata)
                if success:
                    metadata.fetch_method = strategy_name
                    return True, result
                else:
                    print(f"[{self.module_name}] {strategy_name} failed: {result}")
            except Exception as e:
                print(f"[{self.module_name}] {strategy_name} error: {str(e)}")

        return False, "All fetching strategies failed"

    def _fetch_traditional(
        self, source: str, metadata: ContentMetadata
    ) -> Tuple[bool, Optional[str]]:
        """Traditional requests-based fetching."""
        try:
            import requests
            from readability import Document

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }

            response = requests.get(source, headers=headers, timeout=30)
            response.raise_for_status()

            # Use readability to extract main content
            doc = Document(response.text)
            content = doc.content()

            return True, content

        except Exception as e:
            return False, f"Traditional fetch failed: {str(e)}"

    def _fetch_with_skyvern(
        self, source: str, metadata: ContentMetadata
    ) -> Tuple[bool, Optional[str]]:
        """Use Skyvern AI to intelligently navigate and extract content."""
        if not self.skyvern_client:
            return False, "Skyvern client not available"

        try:
            # Create Skyvern task with intelligent prompts
            task_prompt = self._generate_extraction_prompt(source, metadata)

            # Execute Skyvern task
            task_result = self.skyvern_client.run_task(
                url=source, prompt=task_prompt, max_steps=10
            )

            if task_result.success:
                # Extract content from Skyvern result
                content = self._extract_content_from_skyvern_result(task_result)
                return True, content
            else:
                return False, f"Skyvern task failed: {task_result.error}"

        except Exception as e:
            return False, f"Skyvern execution error: {str(e)}"

    def _fetch_paywall_content(
        self, source: str, metadata: ContentMetadata
    ) -> Tuple[bool, Optional[str]]:
        """Handle paywall sites with intelligent navigation."""
        if not self.skyvern_client:
            return False, "Skyvern client not available"

        try:
            # Check if we have credentials for this site
            site_domain = urlparse(source).netloc
            credentials = self._get_site_credentials(site_domain)

            if not credentials:
                return False, f"No credentials configured for {site_domain}"

            # Create login and extraction task
            login_prompt = f"""
            1. Navigate to the login page for {site_domain}
            2. Fill in login credentials (username: {credentials['username']})
            3. Navigate to the article at {source}
            4. Wait for the full article content to load
            5. Extract the main article text, ignoring ads and navigation
            """

            task_result = self.skyvern_client.run_task(
                url=source, prompt=login_prompt, max_steps=15
            )

            if task_result.success:
                content = self._extract_content_from_skyvern_result(task_result)
                return True, content
            else:
                return False, f"Paywall bypass failed: {task_result.error}"

        except Exception as e:
            return False, f"Paywall handling error: {str(e)}"

    def _generate_extraction_prompt(self, url: str, metadata: ContentMetadata) -> str:
        """Generate intelligent extraction prompts based on site and content type."""
        domain = urlparse(url).netloc

        # Site-specific prompts
        site_prompts = {
            "medium.com": """
            1. Navigate to the article page
            2. If there's a paywall popup, try to close it or find a "continue reading" option
            3. Scroll down to load the full article content
            4. Extract the article title, subtitle, author, and full text content
            5. Ignore claps, comments, and recommended articles
            """,
            "nytimes.com": """
            1. Navigate to the article page
            2. Handle any cookie consent banners
            3. If there's a subscription popup, try to find ways to access the article
            4. Extract the headline, byline, date, and full article text
            5. Stop at the end of the main article content
            """,
            "reddit.com": """
            1. Navigate to the Reddit post
            2. Load all comments by clicking "load more" if present
            3. Extract the post title, content, and top-level comments
            4. Include comment scores and timestamps
            """,
        }

        # Use site-specific prompt or generic one
        if domain in site_prompts:
            return site_prompts[domain]
        else:
            return f"""
            1. Navigate to {url}
            2. Handle any popups, cookie banners, or overlays
            3. Scroll to ensure all content is loaded
            4. Identify and extract the main article content
            5. Include title, author, date, and full text
            6. Ignore navigation, ads, and sidebar content
            """

    def _extract_content_from_skyvern_result(self, task_result) -> str:
        """Extract clean content from Skyvern task result."""
        # This would depend on Skyvern's actual API response format
        # For now, assuming it returns HTML content
        if hasattr(task_result, "extracted_content"):
            return task_result.extracted_content
        elif hasattr(task_result, "page_content"):
            return task_result.page_content
        else:
            return str(task_result)

    def _is_complex_site(self, url: str) -> bool:
        """Detect if site likely needs AI automation."""
        complex_domains = [
            "medium.com",
            "substack.com",
            "notion.so",
            "github.com",
            "stackoverflow.com",
            "reddit.com",
        ]
        domain = urlparse(url).netloc
        return any(d in domain for d in complex_domains)

    def _is_paywall_site(self, url: str) -> bool:
        """Detect if site likely has paywall."""
        paywall_domains = [
            "nytimes.com",
            "wsj.com",
            "ft.com",
            "bloomberg.com",
            "economist.com",
            "washingtonpost.com",
        ]
        domain = urlparse(url).netloc
        return any(d in domain for d in paywall_domains)

    def _get_site_credentials(self, domain: str) -> Optional[Dict[str, str]]:
        """Get stored credentials for a specific site."""
        # This would load from secure credential storage
        credentials_map = {
            "nytimes.com": {
                "username": self.config.get("NYTIMES_USERNAME"),
                "password": self.config.get("NYTIMES_PASSWORD"),
            },
            # Add more sites as needed
        }

        if domain in credentials_map:
            creds = credentials_map[domain]
            if creds["username"] and creds["password"]:
                return creds
        return None

    def process_content(self, content: str, metadata: ContentMetadata) -> bool:
        """Process extracted content into markdown."""
        try:
            # Convert HTML to markdown
            markdown_content = convert_html_to_markdown(content, metadata.source)

            # Save to temporary file for metadata processing
            temp_file = tempfile.NamedTemporaryFile(
                mode="w", suffix=".md", delete=False
            )
            temp_file.write(markdown_content)
            temp_file.close()

            # Store content in metadata
            metadata.type_specific["content"] = markdown_content
            metadata.type_specific["content_length"] = len(markdown_content)
            metadata.type_specific["processing_method"] = metadata.fetch_method

            # Generate summary if content is substantial
            if len(markdown_content) > 500:
                try:
                    from process.evaluate import summarize_text

                    metadata.type_specific["summary"] = summarize_text(
                        markdown_content[:4000]
                    )
                except Exception as e:
                    print(f"[{self.module_name}] Summary generation failed: {e}")
                    metadata.type_specific["summary"] = markdown_content[:500] + "..."
            else:
                metadata.type_specific["summary"] = markdown_content

            # Clean up temp file
            os.unlink(temp_file.name)

            return True

        except Exception as e:
            print(f"[{self.module_name}] Content processing error: {e}")
            return False


class SkyvernInstapaperEnhancer:
    """Enhance Instapaper scraping with Skyvern intelligence."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.skyvern_enabled = (
            config.get("SKYVERN_ENABLED", False) and SKYVERN_AVAILABLE
        )
        if self.skyvern_enabled:
            self.skyvern_client = SkyverhClient(
                base_url=config.get("SKYVERN_BASE_URL", "https://api.skyvern.com"),
                api_key=config.get("SKYVERN_API_KEY"),
            )

    def scrape_instapaper_intelligently(
        self, login: str, password: str
    ) -> List[Dict[str, Any]]:
        """Use Skyvern to scrape Instapaper reading list intelligently."""
        if not self.skyvern_enabled:
            raise RuntimeError("Skyvern not available for Instapaper scraping")

        instapaper_prompt = f"""
        1. Navigate to https://www.instapaper.com/user/login
        2. Fill in the username field with: {login}
        3. Fill in the password field with: {password}
        4. Click the login button
        5. Wait for the main reading list page to load
        6. Scroll down to load all articles in the reading list
        7. For each article, extract:
           - Article title
           - Original URL
           - Date added (if visible)
           - Any tags or categories
        8. Continue scrolling until no new articles appear
        9. Return the complete list of articles with their metadata
        """

        try:
            task_result = self.skyvern_client.run_task(
                url="https://www.instapaper.com/user/login",
                prompt=instapaper_prompt,
                max_steps=20,
            )

            if task_result.success:
                return self._parse_instapaper_results(task_result)
            else:
                raise RuntimeError(f"Instapaper scraping failed: {task_result.error}")

        except Exception as e:
            raise RuntimeError(f"Skyvern Instapaper scraping error: {str(e)}")

    def _parse_instapaper_results(self, task_result) -> List[Dict[str, Any]]:
        """Parse Skyvern results into structured article data."""
        # This would depend on Skyvern's actual response format
        # For now, return mock structure
        articles = []

        # Parse the extracted data from Skyvern
        if hasattr(task_result, "extracted_data"):
            for item in task_result.extracted_data:
                article = {
                    "title": item.get("title", "Unknown Title"),
                    "url": item.get("url", ""),
                    "date_added": item.get("date", ""),
                    "tags": item.get("tags", []),
                    "bookmark_id": hashlib.sha1(
                        item.get("url", "").encode()
                    ).hexdigest()[:16],
                }
                articles.append(article)

        return articles


def create_skyvern_enhanced_ingestor(config: Dict[str, Any]) -> SkyvernEnhancedIngestor:
    """Create and return a SkyvernEnhancedIngestor instance."""
    return SkyvernEnhancedIngestor(config)
