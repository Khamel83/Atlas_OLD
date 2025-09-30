"""
Content Validation Module for Atlas v2

Quality checks and validation for extracted content
"""

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class ContentValidator:
    """Validates extracted content quality"""

    def validate_content(self, content: str, content_type: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate content based on type and metadata

        Returns:
            {"status": "valid"|"invalid"|"needs_review", "score": float, "checks": dict}
        """
        if content_type == 'podcast':
            return self.validate_podcast_transcript(content, metadata)
        elif content_type == 'article':
            return self.validate_article(content, metadata)
        elif content_type == 'newsletter':
            return self.validate_newsletter(content, metadata)
        else:
            return self.validate_generic_content(content, metadata)

    def validate_podcast_transcript(self, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Validate podcast transcript"""
        duration_min = metadata.get('duration_minutes', 60)
        words_per_min = 80

        expected_low = duration_min * words_per_min * 0.5
        expected_high = duration_min * words_per_min * 1.5

        actual_words = len(content.split())

        checks = {
            "word_count_in_range": expected_low <= actual_words <= expected_high,
            "min_length": actual_words >= 1000,
            "has_conversation_markers": any(marker in content.lower()
                                          for marker in [': ', 'speaker', 'host', 'guest'])
        }

        score = sum(checks.values()) / len(checks)

        if score >= 0.8:
            status = "valid"
        elif score >= 0.6:
            status = "needs_review"
        else:
            status = "invalid"

        return {
            "status": status,
            "score": score,
            "checks": checks,
            "actual_words": actual_words,
            "expected_range": [expected_low, expected_high]
        }

    def validate_article(self, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Validate article content"""
        actual_words = len(content.split())

        checks = {
            "min_length": actual_words >= 500,
            "has_paragraphs": content.count('\n\n') >= 2,
            "has_sentences": '.' in content or '!' in content
        }

        score = sum(checks.values()) / len(checks)
        status = "valid" if score >= 0.7 else "needs_review" if score >= 0.5 else "invalid"

        return {"status": status, "score": score, "checks": checks}

    def validate_newsletter(self, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Validate newsletter content"""
        return self.validate_article(content, metadata)  # Same as article for now

    def validate_generic_content(self, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Validate generic content"""
        actual_words = len(content.split())

        checks = {
            "has_content": actual_words > 100,
            "reasonable_length": actual_words < 50000
        }

        score = sum(checks.values()) / len(checks)
        status = "valid" if score >= 0.8 else "needs_review"

        return {"status": status, "score": score, "checks": checks}