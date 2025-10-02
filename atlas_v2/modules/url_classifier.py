"""
URL Classification and Routing System for Atlas v2

Intelligently classifies URLs for appropriate processing strategies,
eliminating queue pollution and enabling reliable high-volume ingestion.

Key Features:
- URL scheme detection (http://, https://, file://, etc.)
- Content type identification from URL patterns
- Processing strategy assignment
- Dead letter queue routing for non-processable URLs
- Duplicate detection through URL normalization
"""

import re
import hashlib
import urllib.parse
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class URLScheme(Enum):
    HTTP = "http"
    HTTPS = "https"
    FILE = "file"
    UNKNOWN = "unknown"

class ProcessingStrategy(Enum):
    HTTP_CONTENT = "http_content"  # Standard HTTP content extraction
    FILE_LOCAL = "file_local"      # Local file processing (disabled for now)
    UNSUPPORTED = "unsupported"    # Unsupported content types
    DEAD_LETTER = "dead_letter"    # Permanently failed items

@dataclass
class URLClassification:
    """URL classification result"""
    original_url: str
    normalized_url: str
    scheme: URLScheme
    domain: Optional[str]
    processing_strategy: ProcessingStrategy
    is_processable: bool
    content_type_hint: Optional[str]
    failure_reason: Optional[str]
    confidence_score: float  # 0.0 to 1.0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            'original_url': self.original_url,
            'normalized_url': self.normalized_url,
            'scheme': self.scheme.value,
            'domain': self.domain,
            'processing_strategy': self.processing_strategy.value,
            'is_processable': self.is_processable,
            'content_type_hint': self.content_type_hint,
            'failure_reason': self.failure_reason,
            'confidence_score': self.confidence_score
        }

class URLClassifier:
    """Intelligent URL classification and routing"""

    def __init__(self):
        # URL pattern matching
        self.url_patterns = {
            # HTTP/HTTPS patterns (processable)
            'http_processable': re.compile(r'^https?://', re.IGNORECASE),

            # File patterns (non-processable in current system)
            'file_local': re.compile(r'^file://', re.IGNORECASE),

            # Invalid schemes
            'invalid_scheme': re.compile(r'^(?!https?://)(?!file://)'),

            # Unsupported file extensions
            'unsupported_extensions': re.compile(
                r'\.(zip|tar|gz|rar|7z|exe|dmg|pkg|deb|rpm|pdf|psd|ai|eps)$',
                re.IGNORECASE
            ),

            # Social media platforms
            'social_media': re.compile(
                r'(facebook\.com|twitter\.com|x\.com|instagram\.com|linkedin\.com|tiktok\.com)',
                re.IGNORECASE
            ),

            # Video platforms
            'video_platforms': re.compile(
                r'(youtube\.com|youtu\.be|vimeo\.com|twitch\.tv|dailymotion\.com)',
                re.IGNORECASE
            ),

            # Podcast platforms
            'podcast_platforms': re.compile(
                r'(spotify\.com|apple\.com/podcasts|google\.com/podcasts|stitcher\.com|overcast\.fm)',
                re.IGNORECASE
            ),

            # News domains
            'news_domains': re.compile(
                r'(nytimes\.com|washingtonpost\.com|wsj\.com|theguardian\.com|bbc\.com|cnn\.com|reuters\.com|ap\.org)',
                re.IGNORECASE
            ),

            # Documentation/Tech sites
            'tech_domains': re.compile(
                r'(github\.com|stackoverflow\.com|medium\.com|dev\.to|hashnode\.com|substack\.com)',
                re.IGNORECASE
            ),
        }

        # Processing strategy rules
        self.strategy_rules = {
            # Processable HTTP content
            'http_content': {
                'conditions': [
                    lambda url: self.url_patterns['http_processable'].match(url) is not None,
                    lambda url: not self._is_unsupported_content(url),
                ],
                'strategy': ProcessingStrategy.HTTP_CONTENT,
                'processable': True,
            },

            # Local files (disabled for security)
            'file_local': {
                'conditions': [
                    lambda url: self.url_patterns['file_local'].match(url) is not None,
                ],
                'strategy': ProcessingStrategy.FILE_LOCAL,
                'processable': False,
                'reason': 'Local file processing not supported in production environment'
            },

            # Invalid schemes
            'invalid_scheme': {
                'conditions': [
                    lambda url: self.url_patterns['invalid_scheme'].match(url) is not None,
                ],
                'strategy': ProcessingStrategy.UNSUPPORTED,
                'processable': False,
                'reason': 'Unsupported URL scheme - only HTTP/HTTPS URLs are supported'
            },
        }

    def classify_url(self, url: str) -> URLClassification:
        """
        Classify a URL for appropriate processing strategy

        Args:
            url: The URL to classify

        Returns:
            URLClassification with processing strategy and metadata
        """
        try:
            # Parse URL
            parsed = urllib.parse.urlparse(url)
            normalized = self._normalize_url(url)

            # Determine scheme
            scheme = self._classify_scheme(parsed.scheme)

            # Extract domain for HTTP URLs
            domain = parsed.netloc.lower() if scheme in [URLScheme.HTTP, URLScheme.HTTPS] else None

            # Determine content type hints
            content_type_hint = self._get_content_type_hint(url, domain)

            # Apply processing strategy rules
            classification = self._apply_strategy_rules(url, normalized, scheme, domain, content_type_hint)

            logger.debug(f"URL classified: {url[:100]}... -> {classification.processing_strategy.value}")
            return classification

        except Exception as e:
            logger.error(f"Error classifying URL {url[:100]}...: {e}")
            return URLClassification(
                original_url=url,
                normalized_url=url,
                scheme=URLScheme.UNKNOWN,
                domain=None,
                processing_strategy=ProcessingStrategy.UNSUPPORTED,
                is_processable=False,
                content_type_hint=None,
                failure_reason=f"Classification error: {str(e)}",
                confidence_score=0.0
            )

    def _normalize_url(self, url: str) -> str:
        """
        Normalize URL for deduplication purposes

        Removes tracking parameters, normalizes scheme, handles redirects
        """
        try:
            parsed = urllib.parse.urlparse(url)

            # Normalize scheme (always prefer https)
            if parsed.scheme == 'http':
                # Check if https version exists (but don't make external calls here)
                normalized_scheme = 'https'
            else:
                normalized_scheme = parsed.scheme

            # Remove tracking parameters
            query_params = urllib.parse.parse_qs(parsed.query)

            # Common tracking parameters to remove
            tracking_params = {
                'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
                'fbclid', 'gclid', 'msclkid', 'twclid', 'igshid', 'ref', 'source',
                '_ga', '_gid', 'mc_eid', 'mc_cid', 'c', 'i'
            }

            # Filter out tracking parameters
            cleaned_params = {
                k: v for k, v in query_params.items()
                if k.lower() not in tracking_params
            }

            # Rebuild query string
            clean_query = urllib.parse.urlencode(cleaned_params, doseq=True)

            # Normalize path (remove trailing slash unless it's just "/")
            path = parsed.path.rstrip('/') if parsed.path != '/' else parsed.path

            # Rebuild URL
            normalized = urllib.parse.urlunparse((
                normalized_scheme,
                parsed.netloc.lower(),  # Normalize domain to lowercase
                path,
                parsed.params,
                clean_query,
                parsed.fragment  # Keep fragment for now
            ))

            return normalized

        except Exception as e:
            logger.warning(f"Error normalizing URL {url[:100]}...: {e}")
            return url

    def _classify_scheme(self, scheme: str) -> URLScheme:
        """Classify URL scheme"""
        scheme_lower = scheme.lower()
        if scheme_lower == 'http':
            return URLScheme.HTTP
        elif scheme_lower == 'https':
            return URLScheme.HTTPS
        elif scheme_lower == 'file':
            return URLScheme.FILE
        else:
            return URLScheme.UNKNOWN

    def _get_content_type_hint(self, url: str, domain: Optional[str]) -> Optional[str]:
        """Get content type hint from URL patterns"""
        url_lower = url.lower()

        # Check for podcast patterns
        if self.url_patterns['podcast_platforms'].search(url_lower):
            return 'podcast'

        # Check for video platforms
        if self.url_patterns['video_platforms'].search(url_lower):
            return 'video'

        # Check for social media
        if self.url_patterns['social_media'].search(url_lower):
            return 'social'

        # Check for news domains
        if domain and self.url_patterns['news_domains'].search(domain):
            return 'article'

        # Check for tech domains
        if domain and self.url_patterns['tech_domains'].search(domain):
            return 'tech'

        # Check file extensions
        if any(ext in url_lower for ext in ['.mp3', '.wav', '.m4a', '.aac']):
            return 'audio'
        if any(ext in url_lower for ext in ['.mp4', '.mov', '.avi', '.mkv']):
            return 'video'
        if any(ext in url_lower for ext in ['.pdf', '.epub', '.mobi']):
            return 'document'

        # Default to generic web content
        return 'web'

    def _apply_strategy_rules(
        self,
        url: str,
        normalized: str,
        scheme: URLScheme,
        domain: Optional[str],
        content_type_hint: Optional[str]
    ) -> URLClassification:
        """Apply processing strategy rules to determine classification"""

        # Check each strategy rule
        for rule_name, rule_config in self.strategy_rules.items():
            if all(condition(url) for condition in rule_config['conditions']):
                return URLClassification(
                    original_url=url,
                    normalized_url=normalized,
                    scheme=scheme,
                    domain=domain,
                    processing_strategy=rule_config['strategy'],
                    is_processable=rule_config['processable'],
                    content_type_hint=content_type_hint,
                    failure_reason=rule_config.get('reason'),
                    confidence_score=self._calculate_confidence(url, scheme, domain, content_type_hint)
                )

        # Default to unsupported if no rules match
        return URLClassification(
            original_url=url,
            normalized_url=normalized,
            scheme=scheme,
            domain=domain,
            processing_strategy=ProcessingStrategy.UNSUPPORTED,
            is_processable=False,
            content_type_hint=content_type_hint,
            failure_reason="No processing strategy matched",
            confidence_score=0.1
        )

    def _is_unsupported_content(self, url: str) -> bool:
        """Check if URL points to unsupported content types"""
        url_lower = url.lower()
        return self.url_patterns['unsupported_extensions'].search(url_lower) is not None

    def _calculate_confidence(
        self,
        url: str,
        scheme: URLScheme,
        domain: Optional[str],
        content_type_hint: Optional[str]
    ) -> float:
        """Calculate confidence score for classification"""
        confidence = 0.5  # Base confidence

        # Higher confidence for standard HTTP/HTTPS URLs
        if scheme in [URLScheme.HTTP, URLScheme.HTTPS]:
            confidence += 0.3

        # Lower confidence for unknown schemes
        if scheme == URLScheme.UNKNOWN:
            confidence -= 0.4

        # Higher confidence for known domains
        if domain:
            confidence += 0.1

        # Higher confidence for identifiable content types
        if content_type_hint and content_type_hint != 'web':
            confidence += 0.1

        # Penalize very long URLs (often tracking links)
        if len(url) > 200:
            confidence -= 0.1

        return max(0.0, min(1.0, confidence))

    def generate_content_id(self, url: str, source_name: str = None) -> str:
        """
        Generate deterministic content ID from URL

        Used for deduplication - same URL always generates same ID
        """
        try:
            # Normalize URL first
            normalized = self._normalize_url(url)

            # Create hash from normalized URL + source
            hash_input = f"{normalized}|{source_name or 'unknown'}"
            hash_bytes = hashlib.sha256(hash_input.encode('utf-8')).digest()

            # Convert to base36 for shorter IDs
            content_id = int.from_bytes(hash_bytes[:12], 'big')
            return f"atlas_{content_id:015x}"

        except Exception as e:
            logger.error(f"Error generating content ID for {url[:100]}...: {e}")
            # Fallback to simple hash
            return f"atlas_{hash(url) % 10**15:015x}"

# Global classifier instance
_classifier = URLClassifier()

def classify_url(url: str) -> URLClassification:
    """Convenience function to classify a URL"""
    return _classifier.classify_url(url)

def generate_content_id(url: str, source_name: str = None) -> str:
    """Convenience function to generate content ID from URL"""
    return _classifier.generate_content_id(url, source_name)

def is_processable_url(url: str) -> bool:
    """Quick check if URL is processable"""
    classification = classify_url(url)
    return classification.is_processable

def get_processing_strategy(url: str) -> ProcessingStrategy:
    """Get processing strategy for URL"""
    classification = classify_url(url)
    return classification.processing_strategy