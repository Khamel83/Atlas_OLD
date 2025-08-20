#!/usr/bin/env python3
"""
Smart Content Recommendations for Atlas

This module implements smart content recommendation capabilities for Atlas.
"""

import random
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import math

class ContentRecommender:
    """Smart content recommender system"""
    
    def __init__(self):
        """Initialize the content recommender"""
        self.user_profiles = {}
        self.content_metadata = {}
        self.interaction_history = defaultdict(list)
        self.content_similarity_matrix = {}
        self.recommendation_cache = {}
    
    def add_user_profile(self, user_id: str, profile_data: Dict[str, Any]):
        """
        Add or update user profile
        
        Args:
            user_id (str): User identifier
            profile_data (Dict[str, Any]): User profile data
        """
        self.user_profiles[user_id] = {
            'id': user_id,
            'preferences': profile_data.get('preferences', {}),
            'interests': profile_data.get('interests', []),
            'reading_history': profile_data.get('reading_history', []),
            'skills': profile_data.get('skills', []),
            'goals': profile_data.get('goals', []),
            'created_at': profile_data.get('created_at', datetime.now().isoformat()),
            'updated_at': datetime.now().isoformat()
        }
        
        print(f"User profile added/updated for {user_id}")
    
    def add_content_metadata(self, content_id: str, metadata: Dict[str, Any]):
        """
        Add content metadata
        
        Args:
            content_id (str): Content identifier
            metadata (Dict[str, Any]): Content metadata
        """
        self.content_metadata[content_id] = {
            'id': content_id,
            'title': metadata.get('title', 'Untitled'),
            'type': metadata.get('type', 'unknown'),
            'categories': metadata.get('categories', []),
            'tags': metadata.get('tags', []),
            'authors': metadata.get('authors', []),
            'publication_date': metadata.get('publication_date'),
            'difficulty': metadata.get('difficulty', 'intermediate'),
            'estimated_reading_time': metadata.get('estimated_reading_time', 0),
            'language': metadata.get('language', 'en'),
            'keywords': metadata.get('keywords', []),
            'summary': metadata.get('summary', ''),
            'created_at': metadata.get('created_at', datetime.now().isoformat()),
            'updated_at': datetime.now().isoformat()
        }
        
        print(f"Content metadata added for {content_id}")
    
    def record_interaction(self, user_id: str, content_id: str, 
                         interaction_type: str, interaction_data: Dict[str, Any] = None):
        """
        Record user interaction with content
        
        Args:
            user_id (str): User identifier
            content_id (str): Content identifier
            interaction_type (str): Type of interaction (view, read, like, share, etc.)
            interaction_data (Dict[str, Any], optional): Additional interaction data
        """
        interaction = {
            'user_id': user_id,
            'content_id': content_id,
            'type': interaction_type,
            'data': interaction_data or {},
            'timestamp': datetime.now().isoformat()
        }
        
        self.interaction_history[user_id].append(interaction)
        
        # Update user profile with reading history
        if user_id in self.user_profiles:
            user_profile = self.user_profiles[user_id]
            if content_id not in user_profile['reading_history']:
                user_profile['reading_history'].append(content_id)
                user_profile['updated_at'] = datetime.now().isoformat()
        
        print(f"Recorded {interaction_type} interaction for user {user_id} with content {content_id}")
    
    def generate_recommendations(self, user_id: str, 
                               num_recommendations: int = 10,
                               recommendation_types: List[str] = None) -> List[Dict[str, Any]]:
        """
        Generate content recommendations for a user
        
        Args:
            user_id (str): User identifier
            num_recommendations (int): Number of recommendations to generate
            recommendation_types (List[str], optional): Types of recommendations
            
        Returns:
            List[Dict[str, Any]]: List of recommendations
        """
        if recommendation_types is None:
            recommendation_types = [
                'collaborative_filtering',
                'content_based',
                'hybrid',
                'trending',
                'personalized_trending'
            ]
        
        # Check cache first
        cache_key = f"{user_id}_{num_recommendations}_{'_'.join(recommendation_types)}"
        if cache_key in self.recommendation_cache:
            cached_result = self.recommendation_cache[cache_key]
            # Check if cache is still valid (1 hour)
            if datetime.now().timestamp() - cached_result['timestamp'] < 3600:
                print("Returning cached recommendations")
                return cached_result['recommendations'][:num_recommendations]
        
        print(f"Generating recommendations for user {user_id}...")
        
        all_recommendations = []
        
        # Generate different types of recommendations
        for rec_type in recommendation_types:
            if rec_type == 'collaborative_filtering':
                recs = self._collaborative_filtering_recommendations(user_id, num_recommendations)
            elif rec_type == 'content_based':
                recs = self._content_based_recommendations(user_id, num_recommendations)
            elif rec_type == 'hybrid':
                recs = self._hybrid_recommendations(user_id, num_recommendations)
            elif rec_type == 'trending':
                recs = self._trending_recommendations(num_recommendations)
            elif rec_type == 'personalized_trending':
                recs = self._personalized_trending_recommendations(user_id, num_recommendations)
            else:
                recs = []
            
            all_recommendations.extend(recs)
        
        # Remove duplicates and rank
        unique_recommendations = self._rank_and_deduplicate_recommendations(all_recommendations)
        
        # Cache results
        self.recommendation_cache[cache_key] = {
            'recommendations': unique_recommendations,
            'timestamp': datetime.now().timestamp()
        }
        
        return unique_recommendations[:num_recommendations]
    
    def _collaborative_filtering_recommendations(self, user_id: str, 
                                               num_recommendations: int) -> List[Dict[str, Any]]:
        """
        Generate collaborative filtering recommendations
        
        Args:
            user_id (str): User identifier
            num_recommendations (int): Number of recommendations to generate
            
        Returns:
            List[Dict[str, Any]]: Collaborative filtering recommendations
        """
        recommendations = []
        
        # Find similar users
        similar_users = self._find_similar_users(user_id)
        
        # Get content liked by similar users
        for similar_user_id, similarity_score in similar_users:
            user_interactions = self.interaction_history[similar_user_id]
            
            # Look for positive interactions (likes, shares, completions)
            positive_interactions = [
                interaction for interaction in user_interactions 
                if interaction['type'] in ['like', 'share', 'complete', 'read']
            ]
            
            for interaction in positive_interactions:
                content_id = interaction['content_id']
                
                # Don't recommend content the user has already interacted with
                if not self._has_user_interacted_with_content(user_id, content_id):
                    # Calculate recommendation score
                    score = similarity_score * self._calculate_content_popularity(content_id)
                    
                    recommendations.append({
                        'content_id': content_id,
                        'score': score,
                        'reason': f'Liked by similar user (similarity: {similarity_score:.2f})',
                        'type': 'collaborative_filtering'
                    })
        
        return recommendations
    
    def _content_based_recommendations(self, user_id: str, 
                                     num_recommendations: int) -> List[Dict[str, Any]]:
        """
        Generate content-based recommendations
        
        Args:
            user_id (str): User identifier
            num_recommendations (int): Number of recommendations to generate
            
        Returns:
            List[Dict[str, Any]]: Content-based recommendations
        """
        recommendations = []
        
        # Get user's reading history
        if user_id not in self.user_profiles:
            return []
        
        user_profile = self.user_profiles[user_id]
        reading_history = user_profile['reading_history']
        
        if not reading_history:
            return []
        
        # Analyze user's interests based on reading history
        user_interests = self._analyze_user_interests(user_id)
        
        # Find content matching user interests
        for content_id, content_meta in self.content_metadata.items():
            # Skip content user has already read
            if content_id in reading_history:
                continue
            
            # Calculate content relevance score
            relevance_score = self._calculate_content_relevance(content_meta, user_interests)
            
            if relevance_score > 0.1:  # Minimum relevance threshold
                recommendations.append({
                    'content_id': content_id,
                    'score': relevance_score,
                    'reason': f'Matches your interests (relevance: {relevance_score:.2f})',
                    'type': 'content_based'
                })
        
        return recommendations
    
    def _hybrid_recommendations(self, user_id: str, 
                              num_recommendations: int) -> List[Dict[str, Any]]:
        """
        Generate hybrid recommendations combining multiple approaches
        
        Args:
            user_id (str): User identifier
            num_recommendations (int): Number of recommendations to generate
            
        Returns:
            List[Dict[str, Any]]: Hybrid recommendations
        """
        # Get recommendations from different methods
        cf_recs = self._collaborative_filtering_recommendations(user_id, num_recommendations)
        cb_recs = self._content_based_recommendations(user_id, num_recommendations)
        
        # Combine and weight recommendations
        combined_scores = defaultdict(float)
        recommendation_details = {}
        
        # Weight collaborative filtering (40%)
        for rec in cf_recs:
            content_id = rec['content_id']
            combined_scores[content_id] += rec['score'] * 0.4
            if content_id not in recommendation_details:
                recommendation_details[content_id] = rec
        
        # Weight content-based (60%)
        for rec in cb_recs:
            content_id = rec['content_id']
            combined_scores[content_id] += rec['score'] * 0.6
            if content_id not in recommendation_details:
                recommendation_details[content_id] = rec
        
        # Create final recommendations
        hybrid_recommendations = []
        for content_id, score in combined_scores.items():
            rec_detail = recommendation_details[content_id]
            hybrid_recommendations.append({
                'content_id': content_id,
                'score': score,
                'reason': f'Hybrid recommendation (combined score: {score:.2f})',
                'type': 'hybrid'
            })
        
        return hybrid_recommendations
    
    def _trending_recommendations(self, num_recommendations: int) -> List[Dict[str, Any]]:
        """
        Generate trending content recommendations
        
        Args:
            num_recommendations (int): Number of recommendations to generate
            
        Returns:
            List[Dict[str, Any]]: Trending recommendations
        """
        recommendations = []
        
        # Calculate content popularity based on recent interactions
        content_popularity = defaultdict(int)
        
        # Look at interactions from the last week
        one_week_ago = datetime.now() - timedelta(days=7)
        
        for user_interactions in self.interaction_history.values():
            for interaction in user_interactions:
                # Parse timestamp
                try:
                    # Handle both naive and timezone-aware timestamps
                    interaction_timestamp = interaction['timestamp']
                    if interaction_timestamp.endswith('Z'):
                        # UTC timestamp
                        interaction_time = datetime.fromisoformat(interaction_timestamp[:-1]).replace(tzinfo=None)
                    else:
                        interaction_time = datetime.fromisoformat(interaction_timestamp).replace(tzinfo=None)
                except ValueError:
                    continue
                
                # Only consider recent interactions
                if interaction_time > one_week_ago.replace(tzinfo=None):
                    content_id = interaction['content_id']
                    content_popularity[content_id] += 1
        
        # Sort by popularity
        sorted_content = sorted(
            content_popularity.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        # Generate recommendations
        for content_id, popularity_score in sorted_content[:num_recommendations * 2]:
            # Calculate trending score (boost recent content)
            trending_score = self._calculate_trending_score(content_id, popularity_score)
            
            recommendations.append({
                'content_id': content_id,
                'score': trending_score,
                'reason': f'Trending content (popularity: {popularity_score})',
                'type': 'trending'
            })
        
        return recommendations
    
    def _personalized_trending_recommendations(self, user_id: str, 
                                              num_recommendations: int) -> List[Dict[str, Any]]:
        """
        Generate personalized trending recommendations
        
        Args:
            user_id (str): User identifier
            num_recommendations (int): Number of recommendations to generate
            
        Returns:
            List[Dict[str, Any]]: Personalized trending recommendations
        """
        # Get trending content
        trending_recs = self._trending_recommendations(num_recommendations * 2)
        
        # Get user interests
        user_interests = self._analyze_user_interests(user_id)
        
        # Personalize trending recommendations
        personalized_recommendations = []
        
        for rec in trending_recs:
            content_id = rec['content_id']
            
            if content_id in self.content_metadata:
                content_meta = self.content_metadata[content_id]
                
                # Calculate personal relevance
                personal_relevance = self._calculate_content_relevance(content_meta, user_interests)
                
                # Combine trending score with personal relevance
                personalized_score = rec['score'] * 0.7 + personal_relevance * 0.3
                
                personalized_recommendations.append({
                    'content_id': content_id,
                    'score': personalized_score,
                    'reason': f'Personalized trending (relevance: {personal_relevance:.2f})',
                    'type': 'personalized_trending'
                })
        
        return personalized_recommendations
    
    def _find_similar_users(self, user_id: str) -> List[Tuple[str, float]]:
        """
        Find users similar to the given user
        
        Args:
            user_id (str): User identifier
            
        Returns:
            List[Tuple[str, float]]: List of (user_id, similarity_score) tuples
        """
        if user_id not in self.user_profiles:
            return []
        
        target_user_profile = self.user_profiles[user_id]
        target_reading_history = set(target_user_profile['reading_history'])
        
        similar_users = []
        
        for other_user_id, other_user_profile in self.user_profiles.items():
            if other_user_id == user_id:
                continue
            
            other_reading_history = set(other_user_profile['reading_history'])
            
            # Calculate Jaccard similarity based on reading history
            intersection = len(target_reading_history.intersection(other_reading_history))
            union = len(target_reading_history.union(other_reading_history))
            
            if union > 0:
                similarity = intersection / union
                if similarity > 0.1:  # Minimum similarity threshold
                    similar_users.append((other_user_id, similarity))
        
        # Sort by similarity (descending)
        similar_users.sort(key=lambda x: x[1], reverse=True)
        
        return similar_users
    
    def _analyze_user_interests(self, user_id: str) -> Dict[str, float]:
        """
        Analyze user interests based on reading history
        
        Args:
            user_id (str): User identifier
            
        Returns:
            Dict[str, float]: Interest scores by category/tag
        """
        if user_id not in self.user_profiles:
            return {}
        
        user_profile = self.user_profiles[user_id]
        reading_history = user_profile['reading_history']
        
        # Collect all categories, tags, and keywords from user's reading history
        interest_scores = defaultdict(float)
        
        for content_id in reading_history:
            if content_id in self.content_metadata:
                content_meta = self.content_metadata[content_id]
                
                # Weight recent content more heavily
                recency_weight = self._calculate_recency_weight(content_id, reading_history)
                
                # Add category scores
                for category in content_meta['categories']:
                    interest_scores[f'category:{category}'] += 1.0 * recency_weight
                
                # Add tag scores
                for tag in content_meta['tags']:
                    interest_scores[f'tag:{tag}'] += 0.8 * recency_weight
                
                # Add keyword scores
                for keyword in content_meta['keywords']:
                    interest_scores[f'keyword:{keyword}'] += 0.5 * recency_weight
        
        return dict(interest_scores)
    
    def _calculate_content_relevance(self, content_meta: Dict[str, Any], 
                                   user_interests: Dict[str, float]) -> float:
        """
        Calculate content relevance to user interests
        
        Args:
            content_meta (Dict[str, Any]): Content metadata
            user_interests (Dict[str, float]): User interest scores
            
        Returns:
            float: Content relevance score (0-1)
        """
        relevance_score = 0.0
        total_weight = 0.0
        
        # Check category relevance
        for category in content_meta['categories']:
            interest_key = f'category:{category}'
            if interest_key in user_interests:
                relevance_score += user_interests[interest_key] * 1.0
                total_weight += 1.0
        
        # Check tag relevance
        for tag in content_meta['tags']:
            interest_key = f'tag:{tag}'
            if interest_key in user_interests:
                relevance_score += user_interests[interest_key] * 0.8
                total_weight += 0.8
        
        # Check keyword relevance
        for keyword in content_meta['keywords']:
            interest_key = f'keyword:{keyword}'
            if interest_key in user_interests:
                relevance_score += user_interests[interest_key] * 0.5
                total_weight += 0.5
        
        if total_weight > 0:
            return min(1.0, relevance_score / total_weight)
        
        return 0.0
    
    def _calculate_content_popularity(self, content_id: str) -> float:
        """
        Calculate content popularity score
        
        Args:
            content_id (str): Content identifier
            
        Returns:
            float: Popularity score
        """
        popularity_count = 0
        
        for user_interactions in self.interaction_history.values():
            for interaction in user_interactions:
                if interaction['content_id'] == content_id:
                    popularity_count += 1
        
        # Normalize popularity (simple approach)
        return min(1.0, popularity_count / 100.0)  # Cap at 100 interactions
    
    def _calculate_trending_score(self, content_id: str, popularity_score: int) -> float:
        """
        Calculate trending score for content
        
        Args:
            content_id (str): Content identifier
            popularity_score (int): Raw popularity score
            
        Returns:
            float: Trending score
        """
        # Get content publication date
        if content_id in self.content_metadata:
            content_meta = self.content_metadata[content_id]
            pub_date_str = content_meta.get('publication_date')
            
            if pub_date_str:
                try:
                    pub_date = datetime.fromisoformat(pub_date_str)
                    # Make both datetimes naive (without timezone info)
                    now_naive = datetime.now().replace(tzinfo=None)
                    pub_date_naive = pub_date.replace(tzinfo=None) if pub_date.tzinfo else pub_date
                    days_since_pub = (now_naive - pub_date_naive).days
                    
                    # Boost score for recently published content
                    recency_boost = max(0.1, 1.0 - (days_since_pub / 30.0))
                    return popularity_score * recency_boost
                except ValueError:
                    pass
        
        return float(popularity_score)
    
    def _calculate_recency_weight(self, content_id: str, reading_history: List[str]) -> float:
        """
        Calculate recency weight for content
        
        Args:
            content_id (str): Content identifier
            reading_history (List[str]): User's reading history
            
        Returns:
            float: Recency weight (0.5-1.5)
        """
        try:
            # Find position in reading history (most recent = highest weight)
            position = len(reading_history) - reading_history.index(content_id) - 1
            max_position = len(reading_history) - 1
            
            if max_position > 0:
                # Linear interpolation between 0.5 and 1.5
                return 0.5 + (position / max_position) * 1.0
            else:
                return 1.0
        except ValueError:
            # Content not in reading history
            return 1.0
    
    def _has_user_interacted_with_content(self, user_id: str, content_id: str) -> bool:
        """
        Check if user has interacted with content
        
        Args:
            user_id (str): User identifier
            content_id (str): Content identifier
            
        Returns:
            bool: True if user has interacted with content
        """
        if user_id in self.interaction_history:
            for interaction in self.interaction_history[user_id]:
                if interaction['content_id'] == content_id:
                    return True
        
        return False
    
    def _rank_and_deduplicate_recommendations(self, 
                                             recommendations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Rank and remove duplicate recommendations
        
        Args:
            recommendations (List[Dict[str, Any]]): List of recommendations
            
        Returns:
            List[Dict[str, Any]]: Ranked and deduplicated recommendations
        """
        # Group by content ID
        content_recommendations = defaultdict(list)
        
        for rec in recommendations:
            content_recommendations[rec['content_id']].append(rec)
        
        # For each content, keep the highest scoring recommendation
        unique_recommendations = []
        
        for content_id, recs in content_recommendations.items():
            # Sort by score descending
            recs.sort(key=lambda x: x['score'], reverse=True)
            # Keep the highest scoring recommendation
            unique_recommendations.append(recs[0])
        
        # Sort all recommendations by score descending
        unique_recommendations.sort(key=lambda x: x['score'], reverse=True)
        
        return unique_recommendations
    
    def get_user_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Get user profile
        
        Args:
            user_id (str): User identifier
            
        Returns:
            Optional[Dict[str, Any]]: User profile or None if not found
        """
        return self.user_profiles.get(user_id)
    
    def get_content_metadata(self, content_id: str) -> Optional[Dict[str, Any]]:
        """
        Get content metadata
        
        Args:
            content_id (str): Content identifier
            
        Returns:
            Optional[Dict[str, Any]]: Content metadata or None if not found
        """
        return self.content_metadata.get(content_id)
    
    def get_user_interactions(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Get user interactions
        
        Args:
            user_id (str): User identifier
            
        Returns:
            List[Dict[str, Any]]: List of user interactions
        """
        return self.interaction_history.get(user_id, [])

def main():
    """Example usage of ContentRecommender"""
    # Create recommender
    recommender = ContentRecommender()
    
    # Sample user profiles
    users = [
        {
            'id': 'user1',
            'preferences': {'reading_time': 'evening', 'device': 'desktop'},
            'interests': ['python', 'data-science', 'machine-learning'],
            'skills': ['intermediate'],
            'goals': ['learn-ml', 'career-change'],
            'reading_history': []
        },
        {
            'id': 'user2',
            'preferences': {'reading_time': 'morning', 'device': 'mobile'},
            'interests': ['web-development', 'javascript', 'react'],
            'skills': ['beginner'],
            'goals': ['build-portfolio', 'learn-js'],
            'reading_history': []
        }
    ]
    
    # Add user profiles
    for user in users:
        recommender.add_user_profile(user['id'], user)
    
    # Sample content metadata
    content_items = [
        {
            'id': 'content1',
            'title': 'Introduction to Python Programming',
            'type': 'article',
            'categories': ['programming'],
            'tags': ['python', 'beginner'],
            'authors': ['John Doe'],
            'publication_date': '2023-05-01T10:00:00Z',
            'difficulty': 'beginner',
            'estimated_reading_time': 15,
            'language': 'en',
            'keywords': ['python', 'programming', 'tutorial'],
            'summary': 'Learn Python programming basics in this comprehensive tutorial.'
        },
        {
            'id': 'content2',
            'title': 'Machine Learning with Python',
            'type': 'article',
            'categories': ['data-science', 'machine-learning'],
            'tags': ['python', 'ml', 'scikit-learn'],
            'authors': ['Jane Smith'],
            'publication_date': '2023-05-02T14:30:00Z',
            'difficulty': 'intermediate',
            'estimated_reading_time': 25,
            'language': 'en',
            'keywords': ['machine-learning', 'python', 'data-science'],
            'summary': 'Explore machine learning concepts and implementation with Python.'
        },
        {
            'id': 'content3',
            'title': 'React Fundamentals',
            'type': 'article',
            'categories': ['web-development', 'javascript'],
            'tags': ['react', 'javascript', 'frontend'],
            'authors': ['Bob Johnson'],
            'publication_date': '2023-05-03T09:15:00Z',
            'difficulty': 'beginner',
            'estimated_reading_time': 20,
            'language': 'en',
            'keywords': ['react', 'javascript', 'components'],
            'summary': 'Master React fundamentals including components, props, and state.'
        }
    ]
    
    # Add content metadata
    for content in content_items:
        recommender.add_content_metadata(content['id'], content)
    
    # Record sample interactions
    interactions = [
        ('user1', 'content1', 'read', {'duration': 18}),
        ('user1', 'content2', 'like', {}),
        ('user1', 'content2', 'share', {'platform': 'twitter'}),
        ('user2', 'content3', 'read', {'duration': 22}),
        ('user2', 'content1', 'like', {}),
        ('user2', 'content3', 'complete', {'quiz_score': 95})
    ]
    
    # Record interactions
    for user_id, content_id, interaction_type, data in interactions:
        recommender.record_interaction(user_id, content_id, interaction_type, data)
    
    # Generate recommendations
    print("Generating content recommendations...")
    
    # For user1
    user1_recs = recommender.generate_recommendations('user1', num_recommendations=5)
    print(f"\nRecommendations for user1:")
    for i, rec in enumerate(user1_recs, 1):
        content_meta = recommender.get_content_metadata(rec['content_id'])
        title = content_meta['title'] if content_meta else rec['content_id']
        print(f"  {i}. {title} (Score: {rec['score']:.2f})")
        print(f"     Reason: {rec['reason']}")
    
    # For user2
    user2_recs = recommender.generate_recommendations('user2', num_recommendations=5)
    print(f"\nRecommendations for user2:")
    for i, rec in enumerate(user2_recs, 1):
        content_meta = recommender.get_content_metadata(rec['content_id'])
        title = content_meta['title'] if content_meta else rec['content_id']
        print(f"  {i}. {title} (Score: {rec['score']:.2f})")
        print(f"     Reason: {rec['reason']}")
    
    # Get user profiles
    print(f"\nUser Profiles:")
    for user_id in ['user1', 'user2']:
        profile = recommender.get_user_profile(user_id)
        if profile:
            print(f"  {user_id}:")
            print(f"    Interests: {', '.join(profile['interests'])}")
            print(f"    Reading History: {', '.join(profile['reading_history'])}")

if __name__ == "__main__":
    main()