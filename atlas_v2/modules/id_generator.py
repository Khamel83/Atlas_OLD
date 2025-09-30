"""
Content ID Generation Module

Generates unique, immutable IDs for all content in Atlas v2.
Format: {source}-{type}-{date}-{slug}

Examples:
- hardfork-podcast-123-2025-09-29-ai-regulation
- stratechery-newsletter-2025-09-29-bundling-unbundling
- youtube-transcript-abc123xyz-2025-09-29-docker-tutorial
"""

import re
import hashlib
from datetime import datetime
from urllib.parse import urlparse
from typing import Dict, Any

def generate_content_id(source: str, content_type: str, url: str, metadata: Dict[str, Any]) -> str:
    """
    Generate unique ID for content

    Args:
        source: Content source name (e.g., "Hard Fork")
        content_type: Type of content (podcast, newsletter, article, youtube)
        url: Source URL
        metadata: Additional metadata with title, date, episode_number, etc.

    Returns:
        Unique content ID string
    """
    # Normalize source name
    source_slug = normalize_source_name(source)

    # Get date (prefer from metadata, fallback to current)
    date_str = get_date_string(metadata)

    # Extract slug from URL or title
    content_slug = extract_content_slug(url, metadata)

    # Include episode number if available (for podcasts)
    episode_number = metadata.get('episode_number')

    if episode_number:
        return f"{source_slug}-{content_type}-{episode_number}-{date_str}-{content_slug}"
    else:
        return f"{source_slug}-{content_type}-{date_str}-{content_slug}"

def normalize_source_name(source: str) -> str:
    """Convert source name to URL-friendly slug"""
    # Convert to lowercase, replace spaces and special chars with hyphens
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', source.lower())

    # Remove leading/trailing hyphens
    slug = slug.strip('-')

    # Handle special cases
    slug_mappings = {
        'hard-fork': 'hardfork',
        'acq2-by-acquired': 'acq2',
        'conversations-with-tyler': 'tyler',
        'the-new-york-times': 'nyt'
    }

    return slug_mappings.get(slug, slug)

def get_date_string(metadata: Dict[str, Any]) -> str:
    """Extract date string in YYYY-MM-DD format"""
    # Try various date fields in metadata
    date_fields = ['date', 'publish_date', 'pub_date', 'created_at', 'published']

    for field in date_fields:
        date_value = metadata.get(field)
        if date_value:
            try:
                # Parse various date formats
                if isinstance(date_value, str):
                    # Try ISO format first
                    if 'T' in date_value:
                        dt = datetime.fromisoformat(date_value.replace('Z', '+00:00'))
                    else:
                        # Try common date formats
                        for fmt in ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y', '%Y-%m-%d %H:%M:%S']:
                            try:
                                dt = datetime.strptime(date_value, fmt)
                                break
                            except ValueError:
                                continue
                        else:
                            continue

                    return dt.strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                continue

    # Fallback to current date
    return datetime.now().strftime('%Y-%m-%d')

def extract_content_slug(url: str, metadata: Dict[str, Any]) -> str:
    """Extract content slug from URL or title"""
    # Try to extract from URL path first
    url_slug = extract_url_slug(url)
    if url_slug and len(url_slug) > 3:
        return url_slug

    # Fallback to title-based slug
    title = metadata.get('title', '')
    if title:
        return title_to_slug(title)

    # Last resort: hash the URL
    return url_to_hash(url)

def extract_url_slug(url: str) -> str:
    """Extract meaningful slug from URL path"""
    try:
        parsed = urlparse(url)
        path = parsed.path.strip('/')

        # Split path and take meaningful parts
        path_parts = [p for p in path.split('/') if p and not p.isdigit()]

        if path_parts:
            # Take the last meaningful part (usually the article/episode slug)
            slug = path_parts[-1]

            # Clean up common URL artifacts
            slug = re.sub(r'\.(html?|php|aspx?)$', '', slug)
            slug = re.sub(r'^(episode|ep|post|article)-?', '', slug, flags=re.IGNORECASE)

            # Normalize
            slug = re.sub(r'[^a-zA-Z0-9-]', '-', slug)
            slug = re.sub(r'-+', '-', slug)  # Collapse multiple hyphens
            slug = slug.strip('-')

            if len(slug) > 3:
                return slug[:50]  # Limit length

    except Exception:
        pass

    return ""

def title_to_slug(title: str) -> str:
    """Convert title to URL-friendly slug"""
    # Remove common podcast prefixes
    title = re.sub(r'^(episode|ep\.?)\s*\d*:?\s*', '', title, flags=re.IGNORECASE)

    # Convert to slug
    slug = title.lower()
    slug = re.sub(r'[^a-zA-Z0-9\s-]', '', slug)  # Remove special chars
    slug = re.sub(r'\s+', '-', slug)  # Spaces to hyphens
    slug = re.sub(r'-+', '-', slug)   # Collapse hyphens
    slug = slug.strip('-')

    # Limit length and take meaningful words
    words = slug.split('-')
    meaningful_words = [w for w in words if len(w) > 2]  # Skip short words

    result = '-'.join(meaningful_words[:6])  # Max 6 meaningful words
    return result[:50] if result else 'untitled'  # Max 50 chars

def url_to_hash(url: str) -> str:
    """Generate short hash from URL as last resort"""
    hash_obj = hashlib.md5(url.encode())
    return hash_obj.hexdigest()[:12]  # 12-char hash

def validate_content_id(content_id: str) -> bool:
    """Validate that content ID follows expected format"""
    # Basic format check: source-type-date-slug or source-type-episode-date-slug
    parts = content_id.split('-')

    if len(parts) < 4:
        return False

    # Check if third part looks like a date (YYYY-MM-DD would create 3 parts)
    date_part_start = 2

    # If third part is numeric, it might be episode number
    if parts[2].isdigit():
        date_part_start = 3

    # Date should be in format YYYY-MM-DD (creating 3 parts when split by -)
    if len(parts) < date_part_start + 3:
        return False

    # Check year part (should be 4 digits starting with 20)
    year_part = parts[date_part_start]
    if not (year_part.isdigit() and len(year_part) == 4 and year_part.startswith('20')):
        return False

    return True

# Legacy migration support
def generate_id_from_legacy_url(url: str, source: str = None, metadata: Dict[str, Any] = None) -> str:
    """Generate ID for legacy content during migration"""
    if metadata is None:
        metadata = {}

    # Try to infer source from URL if not provided
    if not source:
        source = infer_source_from_url(url)

    # Try to infer content type
    content_type = infer_content_type_from_url(url, metadata)

    return generate_content_id(source, content_type, url, metadata)

def infer_source_from_url(url: str) -> str:
    """Infer source name from URL domain"""
    try:
        domain = urlparse(url).netloc.lower()

        domain_mappings = {
            'acquired.fm': 'Acquired',
            'conversationswithtyler.com': 'Conversations with Tyler',
            'stratechery.com': 'Stratechery',
            'nytimes.com': 'Hard Fork',
            'youtube.com': 'YouTube',
            'youtu.be': 'YouTube'
        }

        for domain_part, source_name in domain_mappings.items():
            if domain_part in domain:
                return source_name

        # Fallback: use domain name
        return domain.replace('www.', '').replace('.com', '').title()

    except Exception:
        return 'unknown'

def infer_content_type_from_url(url: str, metadata: Dict[str, Any]) -> str:
    """Infer content type from URL and metadata"""
    url_lower = url.lower()

    # Check URL patterns
    if 'youtube.com' in url_lower or 'youtu.be' in url_lower:
        return 'youtube'
    elif 'podcast' in url_lower or 'episode' in url_lower:
        return 'podcast'
    elif any(word in url_lower for word in ['newsletter', 'daily-update', 'weekly']):
        return 'newsletter'

    # Check metadata
    content_type = metadata.get('content_type', '').lower()
    if content_type:
        return content_type

    # Check title for clues
    title = metadata.get('title', '').lower()
    if any(word in title for word in ['episode', 'podcast', 'interview']):
        return 'podcast'
    elif any(word in title for word in ['newsletter', 'daily update', 'weekly']):
        return 'newsletter'

    # Default
    return 'article'