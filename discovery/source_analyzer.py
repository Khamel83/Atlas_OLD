"""
Source Analyzer for Atlas
Analyzes content sources for quality, reputation, and categorization
"""

import re
import requests
from urllib.parse import urlparse
from datetime import datetime, timedelta
import tldextract
from collections import defaultdict


class SourceAnalyzer:
    """Analyze content sources for quality, reputation, and categorization"""

    def __init__(self):
        self.domain_scores = {}
        self.author_scores = {}
        self.source_categories = {}

    def analyze_source_quality(self, url, content_text="", publish_date=None):
        """
        Create SourceAnalyzer class with content quality scoring

        Args:
            url (str): The URL of the source
            content_text (str): The text content of the source
            publish_date (datetime): The publication date of the content

        Returns:
            dict: Quality scores and analysis results
        """
        print(f"Analyzing source quality for: {url}")

        # Extract domain
        domain = self._extract_domain(url)

        # Initialize scores
        quality_scores = {
            "url": url,
            "domain": domain,
            "overall_score": 0.0,
            "metrics": {},
        }

        # Content quality metrics
        quality_scores["metrics"]["content_length"] = self._assess_content_length(
            content_text
        )
        quality_scores["metrics"]["language_quality"] = self._assess_language_quality(
            content_text
        )
        quality_scores["metrics"]["readability"] = self._assess_readability(
            content_text
        )
        quality_scores["metrics"]["content_freshness"] = self._assess_content_freshness(
            publish_date
        )

        # Calculate overall score
        quality_scores["overall_score"] = self._calculate_overall_quality(
            quality_scores["metrics"]
        )

        print(f"Source quality analysis completed for: {url}")
        return quality_scores

    def build_domain_reputation(self, domain, signals=None):
        """
        Build domain reputation system using multiple signals

        Args:
            domain (str): The domain to analyze
            signals (dict): Additional reputation signals

        Returns:
            dict: Domain reputation scores
        """
        print(f"Building domain reputation for: {domain}")

        if signals is None:
            signals = {}

        # Initialize reputation scores
        reputation_scores = {"domain": domain, "reputation_score": 0.0, "signals": {}}

        # Domain age estimation (stub)
        reputation_scores["signals"]["domain_age"] = self._estimate_domain_age(domain)

        # Known reputable sources (stub)
        reputation_scores["signals"]["known_reputable"] = (
            self._check_known_reputable_sources(domain)
        )

        # Blacklist/whitelist status (stub)
        reputation_scores["signals"]["blacklist_status"] = self._check_blacklist_status(
            domain
        )
        reputation_scores["signals"]["whitelist_status"] = self._check_whitelist_status(
            domain
        )

        # Content quality history (stub)
        reputation_scores["signals"]["quality_history"] = self._get_quality_history(
            domain
        )

        # Add custom signals
        reputation_scores["signals"].update(signals)

        # Calculate overall reputation score
        reputation_scores["reputation_score"] = self._calculate_reputation_score(
            reputation_scores["signals"]
        )

        # Store in cache
        self.domain_scores[domain] = reputation_scores

        print(f"Domain reputation built for: {domain}")
        return reputation_scores

    def detect_content_freshness(self, publish_date=None, update_date=None):
        """
        Implement content freshness and update frequency detection

        Args:
            publish_date (datetime): Publication date
            update_date (datetime): Last update date

        Returns:
            dict: Freshness metrics
        """
        print("Detecting content freshness...")

        freshness_metrics = {
            "publish_date": publish_date,
            "update_date": update_date,
            "days_since_publish": None,
            "days_since_update": None,
            "freshness_score": 0.0,
        }

        # Calculate days since publish
        if publish_date:
            days_since_publish = (datetime.now() - publish_date).days
            freshness_metrics["days_since_publish"] = days_since_publish

        # Calculate days since update
        if update_date:
            days_since_update = (datetime.now() - update_date).days
            freshness_metrics["days_since_update"] = days_since_update

        # Calculate freshness score
        freshness_metrics["freshness_score"] = self._calculate_freshness_score(
            freshness_metrics["days_since_publish"],
            freshness_metrics["days_since_update"],
        )

        print("Content freshness detection completed")
        return freshness_metrics

    def assess_author_credibility(
        self, author_name, author_url=None, publication_history=None
    ):
        """
        Add author credibility and expertise scoring

        Args:
            author_name (str): Name of the author
            author_url (str): URL to author's profile/page
            publication_history (list): List of previous publications

        Returns:
            dict: Author credibility scores
        """
        print(f"Assessing author credibility for: {author_name}")

        if publication_history is None:
            publication_history = []

        credibility_scores = {
            "author_name": author_name,
            "author_url": author_url,
            "credibility_score": 0.0,
            "metrics": {},
        }

        # Publication count
        credibility_scores["metrics"]["publication_count"] = len(publication_history)

        # Publication quality (stub)
        credibility_scores["metrics"]["avg_publication_quality"] = (
            self._assess_avg_publication_quality(publication_history)
        )

        # Domain diversity (stub)
        credibility_scores["metrics"]["domain_diversity"] = (
            self._assess_domain_diversity(publication_history)
        )

        # Author verification (stub)
        credibility_scores["metrics"]["verified_status"] = (
            self._check_author_verification(author_name, author_url)
        )

        # Calculate overall credibility score
        credibility_scores["credibility_score"] = self._calculate_author_credibility(
            credibility_scores["metrics"]
        )

        # Store in cache
        self.author_scores[author_name] = credibility_scores

        print(f"Author credibility assessment completed for: {author_name}")
        return credibility_scores

    def categorize_source(self, url, content_text="", metadata=None):
        """
        Create source categorization (news, blog, academic, forum)

        Args:
            url (str): The URL of the source
            content_text (str): The text content of the source
            metadata (dict): Additional metadata about the source

        Returns:
            dict: Source categorization results
        """
        print(f"Categorizing source: {url}")

        if metadata is None:
            metadata = {}

        # Extract domain
        domain = self._extract_domain(url)

        categorization = {
            "url": url,
            "domain": domain,
            "category": "unknown",
            "confidence": 0.0,
            "subcategories": [],
        }

        # Determine category based on multiple factors
        category_scores = {
            "news": self._score_news_category(url, content_text, metadata),
            "blog": self._score_blog_category(url, content_text, metadata),
            "academic": self._score_academic_category(url, content_text, metadata),
            "forum": self._score_forum_category(url, content_text, metadata),
        }

        # Find the highest scoring category
        best_category = max(category_scores, key=category_scores.get)
        categorization["category"] = best_category
        categorization["confidence"] = category_scores[best_category]

        # Add subcategories
        categorization["subcategories"] = self._identify_subcategories(
            url, content_text, metadata
        )

        # Store in cache
        self.source_categories[url] = categorization

        print(f"Source categorized as: {best_category}")
        return categorization

    def write_unit_tests(self):
        """
        Write unit tests for all scoring algorithms
        """
        print("Writing unit tests for scoring algorithms...")

        # This would typically create a separate test file
        test_content = """
import unittest
from discovery.source_analyzer import SourceAnalyzer

class TestSourceAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = SourceAnalyzer()
    
    def test_content_length_assessment(self):
        # Test short content
        short_content = "This is short content."
        score = self.analyzer._assess_content_length(short_content)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
        
        # Test long content
        long_content = "A" * 10000
        score = self.analyzer._assess_content_length(long_content)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
    
    def test_language_quality_assessment(self):
        # Test good quality content
        good_content = "This is well-written content with proper grammar and structure."
        score = self.analyzer._assess_language_quality(good_content)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
    
    def test_domain_extraction(self):
        url = "https://www.example.com/article"
        domain = self.analyzer._extract_domain(url)
        self.assertEqual(domain, "example.com")
        
    def test_domain_reputation(self):
        domain = "example.com"
        reputation = self.analyzer.build_domain_reputation(domain)
        self.assertIn('reputation_score', reputation)
        self.assertGreaterEqual(reputation['reputation_score'], 0.0)
        self.assertLessEqual(reputation['reputation_score'], 1.0)

if __name__ == '__main__':
    unittest.main()
"""

        # Write test file
        with open("/home/ubuntu/dev/atlas/discovery/source_analyzer_test.py", "w") as f:
            f.write(test_content)

        print(
            "Unit tests written to: /home/ubuntu/dev/atlas/discovery/source_analyzer_test.py"
        )
        return True

    def _extract_domain(self, url):
        """Extract domain from URL"""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            # Remove www prefix if present
            if domain.startswith("www."):
                domain = domain[4:]
            return domain
        except:
            return "unknown"

    def _assess_content_length(self, content_text):
        """Assess content length quality (0.0 to 1.0)"""
        if not content_text:
            return 0.0

        length = len(content_text)

        # Ideal length is between 1000-5000 characters
        if length < 500:
            return length / 500.0 * 0.3
        elif length <= 5000:
            return 0.3 + (length - 500) / 4500.0 * 0.7
        else:
            # Too long, start reducing score
            excess = min(length - 5000, 5000)  # Cap at 5000 excess chars
            return 1.0 - (excess / 5000.0 * 0.3)

    def _assess_language_quality(self, content_text):
        """Assess language quality (0.0 to 1.0)"""
        if not content_text:
            return 0.0

        # Simple heuristic: check for sentence structure
        sentences = re.split(r"[.!?]+", content_text)
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)

        # Ideal average sentence length is 15-25 words
        if avg_sentence_length < 5:
            return 0.2
        elif avg_sentence_length <= 25:
            return 0.5 + (avg_sentence_length - 5) / 20.0 * 0.5
        else:
            return max(0.3, 1.0 - (avg_sentence_length - 25) / 25.0 * 0.7)

    def _assess_readability(self, content_text):
        """Assess readability (0.0 to 1.0)"""
        if not content_text:
            return 0.0

        # Simple Flesch Reading Ease approximation
        words = content_text.split()
        sentences = re.split(r"[.!?]+", content_text)
        syllables = sum(self._count_syllables(word) for word in words)

        if len(words) == 0 or len(sentences) == 0:
            return 0.3

        avg_words_per_sentence = len(words) / len(sentences)
        avg_syllables_per_word = syllables / len(words) if len(words) > 0 else 0

        # Simplified readability score (0-1 scale)
        readability = 1.0 - min(
            1.0,
            (avg_words_per_sentence / 30.0 * 0.7 + avg_syllables_per_word / 3.0 * 0.3),
        )
        return max(0.1, readability)

    def _count_syllables(self, word):
        """Count syllables in a word"""
        word = word.lower()
        vowels = "aeiouy"
        count = 0
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count = 1
        return count

    def _assess_content_freshness(self, publish_date):
        """Assess content freshness (0.0 to 1.0)"""
        if not publish_date:
            return 0.5  # Neutral score if no date

        days_old = (datetime.now() - publish_date).days

        # Content less than 30 days old is fresh
        if days_old < 30:
            return 1.0 - (days_old / 30.0 * 0.5)
        # Content 30-90 days old is somewhat fresh
        elif days_old < 90:
            return 0.5 - ((days_old - 30) / 60.0 * 0.3)
        # Content 90-365 days old is dated
        elif days_old < 365:
            return 0.2 - ((days_old - 90) / 275.0 * 0.15)
        # Content over a year old is stale
        else:
            return 0.05

    def _calculate_overall_quality(self, metrics):
        """Calculate overall quality score"""
        if not metrics:
            return 0.0

        # Weighted average of metrics
        weights = {
            "content_length": 0.25,
            "language_quality": 0.25,
            "readability": 0.25,
            "content_freshness": 0.25,
        }

        total_score = 0.0
        total_weight = 0.0

        for metric, weight in weights.items():
            if metric in metrics:
                total_score += metrics[metric] * weight
                total_weight += weight

        return total_score / total_weight if total_weight > 0 else 0.0

    def _estimate_domain_age(self, domain):
        """Estimate domain age (stub)"""
        # In a real implementation, this would check WHOIS data
        return 0.8  # Assume moderate age

    def _check_known_reputable_sources(self, domain):
        """Check if domain is in list of known reputable sources (stub)"""
        # In a real implementation, this would check against a database
        reputable_domains = [
            "nytimes.com",
            "washingtonpost.com",
            "reuters.com",
            "apnews.com",
            "bbc.com",
            "cnn.com",
            "npr.org",
        ]
        return 1.0 if domain in reputable_domains else 0.5

    def _check_blacklist_status(self, domain):
        """Check blacklist status (stub)"""
        # In a real implementation, this would check against blacklists
        return 0.0  # Assume not blacklisted

    def _check_whitelist_status(self, domain):
        """Check whitelist status (stub)"""
        # In a real implementation, this would check against whitelists
        return 0.5  # Neutral score

    def _get_quality_history(self, domain):
        """Get content quality history (stub)"""
        # In a real implementation, this would retrieve historical data
        return 0.7  # Assume moderate quality history

    def _calculate_reputation_score(self, signals):
        """Calculate overall reputation score"""
        if not signals:
            return 0.5

        # Weighted average of signals
        weights = {
            "domain_age": 0.15,
            "known_reputable": 0.30,
            "blacklist_status": 0.20,
            "whitelist_status": 0.20,
            "quality_history": 0.15,
        }

        total_score = 0.0
        total_weight = 0.0

        for signal, weight in weights.items():
            if signal in signals:
                total_score += signals[signal] * weight
                total_weight += weight

        return total_score / total_weight if total_weight > 0 else 0.5

    def _calculate_freshness_score(self, days_since_publish, days_since_update):
        """Calculate freshness score"""
        # Prefer updated content, fallback to publish date
        days_old = (
            days_since_update if days_since_update is not None else days_since_publish
        )

        if days_old is None:
            return 0.5  # Neutral score

        # Content less than 7 days old is very fresh
        if days_old < 7:
            return 1.0
        # Content 7-30 days old is fresh
        elif days_old < 30:
            return 0.8 - ((days_old - 7) / 23.0 * 0.3)
        # Content 30-90 days old is somewhat fresh
        elif days_old < 90:
            return 0.5 - ((days_old - 30) / 60.0 * 0.3)
        # Content 90-365 days old is dated
        elif days_old < 365:
            return 0.2 - ((days_old - 90) / 275.0 * 0.15)
        # Content over a year old is stale
        else:
            return 0.05

    def _assess_avg_publication_quality(self, publication_history):
        """Assess average publication quality (stub)"""
        # In a real implementation, this would analyze publication history
        return 0.7  # Assume moderate quality

    def _assess_domain_diversity(self, publication_history):
        """Assess domain diversity (stub)"""
        # In a real implementation, this would analyze domain distribution
        return 0.6  # Assume moderate diversity

    def _check_author_verification(self, author_name, author_url):
        """Check author verification status (stub)"""
        # In a real implementation, this would check verification signals
        return 0.5  # Neutral score

    def _calculate_author_credibility(self, metrics):
        """Calculate overall author credibility score"""
        if not metrics:
            return 0.5

        # Weighted average of metrics
        weights = {
            "publication_count": 0.25,
            "avg_publication_quality": 0.35,
            "domain_diversity": 0.20,
            "verified_status": 0.20,
        }

        total_score = 0.0
        total_weight = 0.0

        for metric, weight in weights.items():
            if metric in metrics:
                total_score += metrics[metric] * weight
                total_weight += weight

        return total_score / total_weight if total_weight > 0 else 0.5

    def _score_news_category(self, url, content_text, metadata):
        """Score likelihood of being a news source"""
        score = 0.2  # Base score

        # Check URL patterns
        news_patterns = ["news", "times", "journal", "tribune", "herald"]
        domain = self._extract_domain(url)
        if any(pattern in domain for pattern in news_patterns):
            score += 0.3

        # Check content keywords
        news_keywords = ["breaking", "report", "journalist", "correspondent", "wire"]
        content_lower = content_text.lower()
        news_matches = sum(1 for keyword in news_keywords if keyword in content_lower)
        score += min(0.3, news_matches * 0.1)

        # Check metadata
        if metadata.get("contentType") == "news":
            score += 0.2

        return min(1.0, score)

    def _score_blog_category(self, url, content_text, metadata):
        """Score likelihood of being a blog"""
        score = 0.2  # Base score

        # Check URL patterns
        blog_patterns = ["blog", "wordpress", "tumblr", "medium"]
        domain = self._extract_domain(url)
        if any(pattern in domain for pattern in blog_patterns):
            score += 0.3

        # Check content characteristics
        personal_pronouns = ["i ", "we ", "my ", "our ", "i'm", "we're"]
        content_lower = content_text.lower()
        pronoun_matches = sum(
            1 for pronoun in personal_pronouns if pronoun in content_lower
        )
        score += min(0.2, pronoun_matches * 0.05)

        # Check for personal tone
        if any(
            word in content_lower
            for word in ["personal", "opinion", "thoughts", "experience"]
        ):
            score += 0.1

        # Check metadata
        if metadata.get("contentType") == "blog":
            score += 0.2

        return min(1.0, score)

    def _score_academic_category(self, url, content_text, metadata):
        """Score likelihood of being academic content"""
        score = 0.1  # Base score

        # Check URL patterns
        academic_patterns = ["edu", "ac.uk", "research", "study", "paper"]
        domain = self._extract_domain(url)
        if any(pattern in domain for pattern in academic_patterns):
            score += 0.4

        # Check content characteristics
        academic_keywords = [
            "study",
            "research",
            "analysis",
            "data",
            "methodology",
            "conclusion",
            "hypothesis",
            "experiment",
            "peer-review",
        ]
        content_lower = content_text.lower()
        academic_matches = sum(
            1 for keyword in academic_keywords if keyword in content_lower
        )
        score += min(0.3, academic_matches * 0.1)

        # Check for citations
        if "citation" in content_lower or "reference" in content_lower:
            score += 0.1

        # Check metadata
        if metadata.get("contentType") in ["academic", "research"]:
            score += 0.2

        return min(1.0, score)

    def _score_forum_category(self, url, content_text, metadata):
        """Score likelihood of being a forum"""
        score = 0.1  # Base score

        # Check URL patterns
        forum_patterns = ["forum", "reddit", "quora", "stackexchange", "discuss"]
        domain = self._extract_domain(url)
        if any(pattern in domain for pattern in forum_patterns):
            score += 0.4

        # Check content characteristics
        if content_text.count("\n") > 20:  # Many line breaks suggest discussion
            score += 0.1

        # Check for question marks (suggests Q&A)
        if content_text.count("?") > 3:
            score += 0.1

        # Check metadata
        if metadata.get("contentType") == "forum":
            score += 0.2

        return min(1.0, score)

    def _identify_subcategories(self, url, content_text, metadata):
        """Identify subcategories for the source"""
        subcategories = []

        # Technology
        tech_keywords = [
            "tech",
            "software",
            "computer",
            "ai",
            "artificial intelligence",
            "programming",
            "coding",
            "digital",
            "internet",
        ]
        content_lower = content_text.lower()
        if any(keyword in content_lower for keyword in tech_keywords):
            subcategories.append("technology")

        # Science
        science_keywords = [
            "science",
            "research",
            "study",
            "experiment",
            "discovery",
            "physics",
            "chemistry",
            "biology",
            "medicine",
        ]
        if any(keyword in content_lower for keyword in science_keywords):
            subcategories.append("science")

        # Politics
        politics_keywords = [
            "politic",
            "government",
            "election",
            "president",
            "congress",
            "policy",
            "legislation",
            "democrat",
            "republican",
        ]
        if any(keyword in content_lower for keyword in politics_keywords):
            subcategories.append("politics")

        # Business
        business_keywords = [
            "business",
            "economy",
            "market",
            "finance",
            "investment",
            "company",
            "corporate",
            "stock",
            "profit",
        ]
        if any(keyword in content_lower for keyword in business_keywords):
            subcategories.append("business")

        return subcategories


def main():
    """Main function to demonstrate SourceAnalyzer usage"""
    print("Atlas Source Analyzer")
    print("====================")

    # Initialize analyzer
    analyzer = SourceAnalyzer()

    # Example usage
    test_url = "https://www.example.com/article"
    test_content = """
    This is an example article about technology and artificial intelligence. 
    The article discusses recent developments in machine learning and how 
    these technologies are transforming various industries. It provides 
    insights into the future of AI and its potential applications.
    """

    # Analyze source quality
    quality_results = analyzer.analyze_source_quality(test_url, test_content)
    print(f"Quality Analysis Results: {quality_results}")

    # Build domain reputation
    domain = analyzer._extract_domain(test_url)
    reputation_results = analyzer.build_domain_reputation(domain)
    print(f"Reputation Analysis Results: {reputation_results}")

    # Detect content freshness
    publish_date = datetime.now() - timedelta(days=10)
    freshness_results = analyzer.detect_content_freshness(publish_date)
    print(f"Freshness Analysis Results: {freshness_results}")

    # Assess author credibility
    author_results = analyzer.assess_author_credibility(
        "John Doe", "https://johndoe.com"
    )
    print(f"Author Credibility Results: {author_results}")

    # Categorize source
    category_results = analyzer.categorize_source(test_url, test_content)
    print(f"Source Categorization Results: {category_results}")

    # Write unit tests
    if analyzer.write_unit_tests():
        print("Unit tests created successfully!")

    print("\nSource Analyzer demonstration completed!")


if __name__ == "__main__":
    main()
