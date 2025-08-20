#!/usr/bin/env python3
"""
Analytics Engine for Atlas

This module implements content analysis capabilities for Atlas.
"""

import re
from typing import Dict, List, Any, Optional
from collections import defaultdict, Counter
import math

class AnalyticsEngine:
    """Content analysis engine for Atlas"""
    
    def __init__(self):
        """Initialize the analytics engine"""
        self.content_stats = {}
        self.user_stats = {}
        self.processing_stats = {}
    
    def analyze_content(self, content: str, metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Analyze content and extract statistics
        
        Args:
            content (str): Content to analyze
            metadata (Dict[str, Any], optional): Content metadata
            
        Returns:
            Dict[str, Any]: Content analysis results
        """
        # Basic text statistics
        word_count = len(re.findall(r'\b\w+\b', content))
        char_count = len(content)
        sentence_count = len(re.split(r'[.!?]+', content))
        paragraph_count = len(content.split('\n\n'))
        
        # Readability metrics
        readability_score = self._calculate_readability(content)
        
        # Keyword extraction
        keywords = self._extract_keywords(content)
        
        # Content categorization
        categories = self._categorize_content(content, metadata)
        
        # Sentiment analysis (simplified)
        sentiment = self._analyze_sentiment(content)
        
        # Content quality score
        quality_score = self._calculate_quality_score(content, word_count, sentence_count)
        
        return {
            'word_count': word_count,
            'char_count': char_count,
            'sentence_count': sentence_count,
            'paragraph_count': paragraph_count,
            'readability_score': readability_score,
            'keywords': keywords,
            'categories': categories,
            'sentiment': sentiment,
            'quality_score': quality_score,
            'analysis_timestamp': '2023-05-01T12:00:00Z'  # In a real implementation, this would be current time
        }
    
    def _calculate_readability(self, content: str) -> float:
        """
        Calculate content readability score
        
        Args:
            content (str): Content to analyze
            
        Returns:
            float: Readability score (0-100)
        """
        # Simplified readability calculation using word and sentence length
        words = re.findall(r'\b\w+\b', content)
        sentences = re.split(r'[.!?]+', content)
        
        if not words or not sentences:
            return 50.0  # Neutral score
        
        avg_word_length = sum(len(word) for word in words) / len(words)
        avg_sentence_length = len(words) / len(sentences) if sentences else 0
        
        # Simple formula: shorter words and sentences = higher readability
        readability = 100 - (avg_word_length * 2 + avg_sentence_length / 2)
        
        # Clamp to 0-100 range
        return max(0, min(100, readability))
    
    def _extract_keywords(self, content: str) -> List[str]:
        """
        Extract keywords from content
        
        Args:
            content (str): Content to analyze
            
        Returns:
            List[str]: Extracted keywords
        """
        # Simple keyword extraction based on word frequency
        words = re.findall(r'\b\w+\b', content.lower())
        
        # Remove stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
            'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
            'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those'
        }
        
        filtered_words = [word for word in words if word not in stop_words and len(word) > 3]
        
        # Get most common words
        word_freq = Counter(filtered_words)
        keywords = [word for word, freq in word_freq.most_common(10)]
        
        return keywords
    
    def _categorize_content(self, content: str, metadata: Dict[str, Any] = None) -> List[str]:
        """
        Categorize content based on keywords and metadata
        
        Args:
            content (str): Content to categorize
            metadata (Dict[str, Any], optional): Content metadata
            
        Returns:
            List[str]: Content categories
        """
        categories = []
        
        # Use metadata if available
        if metadata and 'categories' in metadata:
            categories.extend(metadata['categories'])
        
        # Extract categories from content
        content_lower = content.lower()
        
        # Technology categories
        if any(word in content_lower for word in ['python', 'programming', 'code', 'software']):
            categories.append('technology')
        
        if any(word in content_lower for word in ['machine learning', 'ai', 'artificial intelligence']):
            categories.append('ai')
        
        if any(word in content_lower for word in ['data science', 'analytics', 'big data']):
            categories.append('data-science')
        
        # Business categories
        if any(word in content_lower for word in ['business', 'management', 'strategy']):
            categories.append('business')
        
        if any(word in content_lower for word in ['finance', 'investment', 'money']):
            categories.append('finance')
        
        # Health categories
        if any(word in content_lower for word in ['health', 'medical', 'wellness']):
            categories.append('health')
        
        # Education categories
        if any(word in content_lower for word in ['education', 'learning', 'study']):
            categories.append('education')
        
        # Default category if none found
        if not categories:
            categories.append('general')
        
        return list(set(categories))  # Remove duplicates
    
    def _analyze_sentiment(self, content: str) -> Dict[str, float]:
        """
        Analyze content sentiment (simplified)
        
        Args:
            content (str): Content to analyze
            
        Returns:
            Dict[str, float]: Sentiment scores
        """
        # Simple sentiment analysis based on positive/negative words
        positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'awesome', 'brilliant',
            'outstanding', 'superb', 'terrific', 'marvelous', 'splendid', 'fabulous', 'incredible',
            'remarkable', 'extraordinary', 'exceptional', 'magnificent', 'spectacular', 'phenomenal'
        }
        
        negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'dreadful', 'atrocious', 'abysmal', 'dismal',
            'poor', 'mediocre', 'inferior', 'substandard', 'unsatisfactory', 'disappointing',
            'frustrating', 'annoying', 'irritating', 'exasperating', 'infuriating', 'enraging'
        }
        
        words = re.findall(r'\b\w+\b', content.lower())
        
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)
        
        total_emotional_words = positive_count + negative_count
        
        if total_emotional_words > 0:
            positivity = positive_count / total_emotional_words
            negativity = negative_count / total_emotional_words
        else:
            positivity = 0.5  # Neutral
            negativity = 0.5  # Neutral
        
        return {
            'positivity': positivity,
            'negativity': negativity,
            'overall': 'positive' if positivity > negativity else 'negative' if negativity > positivity else 'neutral'
        }
    
    def _calculate_quality_score(self, content: str, word_count: int, sentence_count: int) -> float:
        """
        Calculate content quality score
        
        Args:
            content (str): Content to analyze
            word_count (int): Number of words
            sentence_count (int): Number of sentences
            
        Returns:
            float: Quality score (0-100)
        """
        # Factors affecting quality score:
        # 1. Adequate length (not too short)
        length_score = min(100, word_count / 100 * 20)  # Up to 20 points for length
        
        # 2. Good sentence structure
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
        sentence_score = 20 if 10 <= avg_sentence_length <= 30 else 10  # Up to 20 points
        
        # 3. Vocabulary diversity
        words = re.findall(r'\b\w+\b', content.lower())
        unique_words = len(set(words))
        vocabulary_score = min(20, unique_words / word_count * 100) if word_count > 0 else 0  # Up to 20 points
        
        # 4. Proper formatting (paragraphs)
        paragraphs = content.split('\n\n')
        paragraph_count = len([p for p in paragraphs if p.strip()])
        format_score = min(20, paragraph_count * 2)  # Up to 20 points
        
        # 5. Keyword density (not too repetitive)
        keyword_density = len(self._extract_keywords(content)) / max(1, word_count / 100)
        keyword_score = min(20, 20 / max(1, abs(keyword_density - 1)))  # Up to 20 points
        
        # Total score
        total_score = length_score + sentence_score + vocabulary_score + format_score + keyword_score
        
        return min(100, total_score)
    
    def track_user_engagement(self, user_id: str, content_id: str, 
                            engagement_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Track user engagement with content
        
        Args:
            user_id (str): User identifier
            content_id (str): Content identifier
            engagement_data (Dict[str, Any]): Engagement data
            
        Returns:
            Dict[str, Any]: Updated user statistics
        """
        if user_id not in self.user_stats:
            self.user_stats[user_id] = {
                'user_id': user_id,
                'total_content_viewed': 0,
                'total_reading_time': 0,
                'favorite_categories': defaultdict(int),
                'reading_speed': 0,
                'completion_rate': 0.0
            }
        
        user_stat = self.user_stats[user_id]
        
        # Update content viewed count
        user_stat['total_content_viewed'] += 1
        
        # Update reading time
        if 'reading_time' in engagement_data:
            user_stat['total_reading_time'] += engagement_data['reading_time']
        
        # Update favorite categories
        if 'categories' in engagement_data:
            for category in engagement_data['categories']:
                user_stat['favorite_categories'][category] += 1
        
        # Update reading speed
        if 'word_count' in engagement_data and 'reading_time' in engagement_data:
            words_per_minute = engagement_data['word_count'] / (engagement_data['reading_time'] / 60)
            # Update average reading speed
            if user_stat['reading_speed'] == 0:
                user_stat['reading_speed'] = words_per_minute
            else:
                # Moving average
                user_stat['reading_speed'] = (user_stat['reading_speed'] + words_per_minute) / 2
        
        # Update completion rate
        if 'completed' in engagement_data:
            if engagement_data['completed']:
                user_stat['completion_rate'] = (
                    user_stat['completion_rate'] * (user_stat['total_content_viewed'] - 1) + 1
                ) / user_stat['total_content_viewed']
            else:
                user_stat['completion_rate'] = (
                    user_stat['completion_rate'] * (user_stat['total_content_viewed'] - 1)
                ) / user_stat['total_content_viewed']
        
        return user_stat
    
    def get_user_analytics(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Get analytics for a specific user
        
        Args:
            user_id (str): User identifier
            
        Returns:
            Optional[Dict[str, Any]]: User analytics or None if user not found
        """
        return self.user_stats.get(user_id)
    
    def get_content_analytics(self, content_id: str) -> Optional[Dict[str, Any]]:
        """
        Get analytics for specific content
        
        Args:
            content_id (str): Content identifier
            
        Returns:
            Optional[Dict[str, Any]]: Content analytics or None if content not found
        """
        return self.content_stats.get(content_id)
    
    def generate_report(self) -> Dict[str, Any]:
        """
        Generate analytics report
        
        Returns:
            Dict[str, Any]: Analytics report
        """
        # Calculate overall statistics
        total_users = len(self.user_stats)
        total_content = len(self.content_stats)
        
        # Calculate average user metrics
        avg_content_viewed = sum(stat['total_content_viewed'] for stat in self.user_stats.values()) / max(1, total_users)
        avg_reading_time = sum(stat['total_reading_time'] for stat in self.user_stats.values()) / max(1, total_users)
        avg_reading_speed = sum(stat['reading_speed'] for stat in self.user_stats.values()) / max(1, total_users)
        avg_completion_rate = sum(stat['completion_rate'] for stat in self.user_stats.values()) / max(1, total_users)
        
        # Calculate popular categories
        category_counts = defaultdict(int)
        for stat in self.user_stats.values():
            for category, count in stat['favorite_categories'].items():
                category_counts[category] += count
        
        popular_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        return {
            'report_generated': '2023-05-01T12:00:00Z',  # In a real implementation, this would be current time
            'user_statistics': {
                'total_users': total_users,
                'avg_content_viewed': avg_content_viewed,
                'avg_reading_time': avg_reading_time,
                'avg_reading_speed': avg_reading_speed,
                'avg_completion_rate': avg_completion_rate,
                'popular_categories': popular_categories
            },
            'content_statistics': {
                'total_content': total_content
            },
            'processing_statistics': self.processing_stats
        }

def main():
    """Example usage of AnalyticsEngine"""
    # Create analytics engine
    engine = AnalyticsEngine()
    
    # Sample content
    content = """
    Python is a high-level programming language with dynamic semantics. It is used for web development, 
    data science, and automation. Python has a simple syntax similar to English, making it easy to learn. 
    The language supports multiple programming paradigms, including procedural, object-oriented, and functional programming. 
    Python has a large standard library and a vibrant community that contributes to thousands of third-party modules and packages. 
    Popular frameworks like Django and Flask make web development with Python straightforward. 
    For data science, libraries like NumPy, Pandas, and Matplotlib provide powerful tools for analysis and visualization. 
    Machine learning practitioners use Python with libraries like TensorFlow, PyTorch, and Scikit-learn. 
    Python is also popular for automation tasks, scripting, and rapid prototyping. 
    The language continues to evolve with regular updates and improvements to performance and features.
    """
    
    # Sample metadata
    metadata = {
        'title': 'Introduction to Python Programming',
        'author': 'John Doe',
        'categories': ['programming', 'technology'],
        'tags': ['python', 'beginner', 'tutorial'],
        'publication_date': '2023-05-01T10:00:00Z'
    }
    
    # Analyze content
    print("Analyzing content...")
    analysis = engine.analyze_content(content, metadata)
    
    print(f"Word count: {analysis['word_count']}")
    print(f"Character count: {analysis['char_count']}")
    print(f"Sentence count: {analysis['sentence_count']}")
    print(f"Paragraph count: {analysis['paragraph_count']}")
    print(f"Readability score: {analysis['readability_score']:.2f}")
    print(f"Keywords: {', '.join(analysis['keywords'])}")
    print(f"Categories: {', '.join(analysis['categories'])}")
    print(f"Sentiment: {analysis['sentiment']['overall']} (pos: {analysis['sentiment']['positivity']:.2f}, neg: {analysis['sentiment']['negativity']:.2f})")
    print(f"Quality score: {analysis['quality_score']:.2f}")
    
    # Track user engagement
    print("\nTracking user engagement...")
    user_engagement = engine.track_user_engagement(
        'user123',
        'content456',
        {
            'reading_time': 15,  # minutes
            'word_count': analysis['word_count'],
            'categories': analysis['categories'],
            'completed': True
        }
    )
    
    print(f"User statistics updated: {user_engagement}")
    
    # Get user analytics
    user_stats = engine.get_user_analytics('user123')
    print(f"User analytics: {user_stats}")
    
    # Generate report
    print("\nGenerating analytics report...")
    report = engine.generate_report()
    print(f"Report generated: {report['report_generated']}")
    print(f"Total users: {report['user_statistics']['total_users']}")
    print(f"Average content viewed: {report['user_statistics']['avg_content_viewed']:.2f}")
    print(f"Average reading time: {report['user_statistics']['avg_reading_time']:.2f} minutes")
    print(f"Average reading speed: {report['user_statistics']['avg_reading_speed']:.2f} wpm")
    print(f"Average completion rate: {report['user_statistics']['avg_completion_rate']:.2f}")
    print(f"Popular categories: {report['user_statistics']['popular_categories']}")

if __name__ == "__main__":
    main()