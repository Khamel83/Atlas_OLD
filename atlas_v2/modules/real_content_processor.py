"""
REAL Content Processing Module for Atlas v2

Actually extracts content from the internet:
- Fetches podcast transcripts from websites
- Processes articles and extracts content
- Validates and stores real content
No more placeholders!
"""

import asyncio
import aiohttp
import logging
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup
import re
from datetime import datetime
import json

logger = logging.getLogger(__name__)

class RealContentProcessor:
    """Real content processing pipeline that actually extracts information"""

    def __init__(self, db_manager, config_manager):
        self.db_manager = db_manager
        self.config_manager = config_manager
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            headers={'User-Agent': 'Mozilla/5.0 (compatible; Atlas-Content-Processor/1.0)'}
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def process_content(self, content_id: str) -> Dict[str, Any]:
        """
        Process a single content item with REAL extraction

        Returns:
            {"status": "success"|"failure"|"retry", "message": str, "content": str}
        """
        try:
            logger.info(f"🔄 REAL processing for {content_id}")

            # Get content details from database
            content_info = await self.db_manager.get_content_details(content_id)
            if not content_info:
                # Try getting from processing_queue directly
                import aiosqlite
                async with aiosqlite.connect("atlas_v2/data/atlas_v2.db") as conn:
                    cursor = await conn.execute("""
                        SELECT content_id, source_url, source_name, content_type
                        FROM processing_queue
                        WHERE content_id = ?
                    """, (content_id,))

                    row = await cursor.fetchone()

                if not row:
                    return {"status": "failure", "message": "Content not found"}

                content_info = {
                    'content_id': row[0],
                    'source_url': row[1],
                    'source_name': row[2],
                    'content_type': row[3],
                    'title': row[2],
                    'metadata': {}
                }

            source_url = content_info.get('source_url')
            content_type = content_info.get('content_type')

            if not source_url:
                return {"status": "failure", "message": "No source URL found"}

            # Extract based on content type
            if content_type in ['podcast_episode', 'podcast']:
                result = await self.extract_podcast_transcript(source_url, content_id)
            elif content_type == 'article':
                result = await self.extract_article_content(source_url, content_id)
            elif content_type == 'url_processing':
                result = await self.extract_generic_content(source_url, content_id)
            else:
                result = await self.extract_generic_content(source_url, content_id)

            # If we got content, store it
            if result['status'] == 'success' and result.get('content'):
                await self.store_extracted_content(content_id, result, content_info)

            return result

        except Exception as e:
            logger.error(f"❌ Processing failed for {content_id}: {e}")
            await self.db_manager.log_operation(
                content_id, 'process', 'failure', str(e)
            )
            return {"status": "failure", "message": str(e)}

    async def extract_podcast_transcript(self, url: str, content_id: str) -> Dict[str, Any]:
        """Extract transcript from podcast website"""
        try:
            if not self.session:
                return {"status": "failure", "message": "No HTTP session"}

            logger.info(f"🎙️ Extracting podcast transcript from: {url}")

            async with self.session.get(url) as response:
                if response.status != 200:
                    return {"status": "retry", "message": f"HTTP {response.status}"}

                html = await response.text()

            soup = BeautifulSoup(html, 'html.parser')

            # Look for transcript content in common patterns
            transcript_content = None
            title = self.extract_title(soup)

            # Method 1: Look for transcript sections
            transcript_selectors = [
                '.transcript', '#transcript', '.episode-transcript',
                '[class*="transcript"]', '[id*="transcript"]',
                '.transcript-content', '.episode-content'
            ]

            for selector in transcript_selectors:
                element = soup.select_one(selector)
                if element:
                    transcript_content = self.clean_text(element.get_text())
                    break

            # Method 2: Look for large text blocks that might be transcripts
            if not transcript_content:
                # Find large text blocks (likely transcripts)
                text_blocks = []
                for p in soup.find_all(['p', 'div']):
                    text = self.clean_text(p.get_text())
                    if len(text) > 500:  # Substantial content
                        text_blocks.append(text)

                if text_blocks:
                    transcript_content = '\n\n'.join(text_blocks)

            # Method 3: Look for common podcast transcript patterns
            if not transcript_content:
                # Search for common transcript indicators
                page_text = self.clean_text(soup.get_text())
                if self.looks_like_transcript(page_text):
                    transcript_content = page_text

            if transcript_content and len(transcript_content) > 1000:
                logger.info(f"✅ Found transcript: {len(transcript_content)} characters")
                return {
                    "status": "success",
                    "message": f"Extracted {len(transcript_content)} characters",
                    "content": transcript_content,
                    "title": title,
                    "source_url": url
                }
            else:
                return {"status": "failure", "message": "No substantial transcript found"}

        except Exception as e:
            logger.error(f"❌ Transcript extraction failed: {e}")
            return {"status": "retry", "message": f"Extraction error: {str(e)}"}

    async def extract_article_content(self, url: str, content_id: str) -> Dict[str, Any]:
        """Extract content from article"""
        try:
            if not self.session:
                return {"status": "failure", "message": "No HTTP session"}

            logger.info(f"📰 Extracting article from: {url}")

            async with self.session.get(url) as response:
                if response.status != 200:
                    return {"status": "retry", "message": f"HTTP {response.status}"}

                html = await response.text()

            soup = BeautifulSoup(html, 'html.parser')

            # Extract title
            title = self.extract_title(soup)

            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                element.decompose()

            # Try to find main article content
            article_content = None

            # Common article selectors
            article_selectors = [
                'article', '.article-content', '.post-content', '.entry-content',
                '.content', 'main', '.story-content', '.article-body'
            ]

            for selector in article_selectors:
                element = soup.select_one(selector)
                if element:
                    article_content = self.clean_text(element.get_text())
                    break

            # Fallback: use largest text block
            if not article_content:
                paragraphs = soup.find_all('p')
                if paragraphs:
                    article_content = '\n\n'.join([p.get_text().strip() for p in paragraphs if len(p.get_text().strip()) > 50])

            if article_content and len(article_content) > 500:
                logger.info(f"✅ Found article: {len(article_content)} characters")
                return {
                    "status": "success",
                    "message": f"Extracted {len(article_content)} characters",
                    "content": article_content,
                    "title": title,
                    "source_url": url
                }
            else:
                return {"status": "failure", "message": "No substantial article content found"}

        except Exception as e:
            logger.error(f"❌ Article extraction failed: {e}")
            return {"status": "retry", "message": f"Extraction error: {str(e)}"}

    async def extract_generic_content(self, url: str, content_id: str) -> Dict[str, Any]:
        """Generic content extraction fallback"""
        try:
            if not self.session:
                return {"status": "failure", "message": "No HTTP session"}

            logger.info(f"🌐 Extracting generic content from: {url}")

            async with self.session.get(url) as response:
                if response.status != 200:
                    return {"status": "retry", "message": f"HTTP {response.status}"}

                html = await response.text()

            soup = BeautifulSoup(html, 'html.parser')

            # Extract title
            title = self.extract_title(soup)

            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                element.decompose()

            # Extract all text content
            content = self.clean_text(soup.get_text())

            if content and len(content) > 300:
                logger.info(f"✅ Found content: {len(content)} characters")
                return {
                    "status": "success",
                    "message": f"Extracted {len(content)} characters",
                    "content": content,
                    "title": title,
                    "source_url": url
                }
            else:
                return {"status": "failure", "message": "No substantial content found"}

        except Exception as e:
            logger.error(f"❌ Generic extraction failed: {e}")
            return {"status": "retry", "message": f"Extraction error: {str(e)}"}

    def extract_title(self, soup) -> str:
        """Extract title from page"""
        # Try common title selectors
        title_selectors = [
            'h1', 'title', '.title', '.headline',
            '[property="og:title"]', '[name="twitter:title"]'
        ]

        for selector in title_selectors:
            element = soup.select_one(selector)
            if element:
                title = element.get_text().strip()
                if selector.startswith('['):  # Meta tag
                    title = element.get('content', '').strip()
                if title and len(title) > 5:
                    return title

        return "Untitled Content"

    def clean_text(self, text: str) -> str:
        """Clean extracted text"""
        if not text:
            return ""

        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove common junk
        text = re.sub(r'\[.*?\]', '', text)  # Remove bracketed content
        text = re.sub(r'\(.*?\)', '', text)  # Remove parenthetical content

        return text.strip()

    def looks_like_transcript(self, text: str) -> bool:
        """Check if text looks like a transcript"""
        # Transcript indicators
        transcript_indicators = [
            r'\bhost:\b', r'\bguest:\b', r'\binterviewer:\b',
            r'\bspeaker \d+\b', r'\bepisode \d+\b',
            r'\bpodcast\b', r'\btranscript\b'
        ]

        for pattern in transcript_indicators:
            if re.search(pattern, text, re.IGNORECASE):
                return True

        return False

    async def store_extracted_content(self, content_id: str, result: Dict[str, Any], content_info: Dict[str, Any]):
        """Store the extracted content"""
        try:
            # Create markdown file
            content_dir = f"atlas_v2/content/transcripts"
            import os
            os.makedirs(content_dir, exist_ok=True)

            # Generate filename
            title = result.get('title', 'Untitled')[:50]
            safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
            if not safe_title:
                safe_title = content_id
            filename = f"{safe_title.replace(' ', '_')}.md"
            filepath = f"{content_dir}/{filename}"

            # Write markdown file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {result.get('title', 'Untitled')}\n\n")
                f.write(f"**Source**: {result.get('source_url')}\n")
                f.write(f"**Extracted**: {datetime.now().isoformat()}\n")
                f.write(f"**Content ID**: {content_id}\n\n")
                f.write("---\n\n")
                f.write(result['content'])

            # Update database
            await self.db_manager.update_content_status(content_id, 'completed', {
                'file_path': filepath,
                'content_length': len(result['content']),
                'title': result.get('title'),
                'extraction_method': 'real_processor'
            })

            logger.info(f"💾 Stored content: {filepath}")

        except Exception as e:
            logger.error(f"❌ Failed to store content: {e}")