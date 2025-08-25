#!/usr/bin/env python3
"""
Proactive Content Surfacer

Intelligently surfaces relevant content from Atlas based on context,
recent activity, and user patterns.
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# Add Atlas to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from helpers.metadata_manager import MetadataManager
    from helpers.config import load_config
except ImportError:
    # Fallback for testing
    MetadataManager = None
    load_config = lambda: {}


@dataclass
class SurfacedContent:
    """Container for surfaced content with relevance scoring."""
    uid: str
    title: str
    source: str
    content_type: str
    relevance_score: float
    surface_reason: str
    metadata: Dict[str, Any]
    updated_at: str
    
    def __post_init__(self):
        if self.updated_at is None:
            self.updated_at = datetime.now().isoformat()


@dataclass
class SurfacingContext:
    """Context for content surfacing."""
    current_topic: Optional[str] = None
    recent_queries: List[str] = None
    time_context: str = "any"  # morning, afternoon, evening, weekend
    content_types: List[str] = None
    max_results: int = 10
    
    def __post_init__(self):
        if self.recent_queries is None:
            self.recent_queries = []
        if self.content_types is None:
            self.content_types = ["article", "podcast", "video"]


class ProactiveSurfacer:
    """
    Proactive content surfacing engine.
    
    Intelligently surfaces relevant content from Atlas based on:
    - Current context and recent activity
    - Time-based relevance (recent vs. historical)
    - Content relationships and patterns
    - User interaction patterns
    """
    
    def __init__(self, metadata_manager: MetadataManager):
        """Initialize ProactiveSurfacer."""
        self.metadata_manager = metadata_manager
        
        # Surfacing configuration
        self.relevance_threshold = self.metadata_manager.config.get('relevance_threshold', 0.3)
        self.max_age_days = self.metadata_manager.config.get('max_content_age_days', 365)
        self.boost_recent = self.metadata_manager.config.get('boost_recent_content', True)
        
    def surface_content(self, 
                       context: SurfacingContext,
                       log_path: str = "") -> List[SurfacedContent]:
        """
        Surface relevant content based on context.
        
        Args:
            context: Surfacing context with topics, queries, preferences
            log_path: Path for logging
            
        Returns:
            List of SurfacedContent objects ordered by relevance
        """
        if not self.metadata_manager:
            return self._mock_surface_content(context)
        
        try:
            # Get all content items
            all_content = self._get_all_content()
            
            # Filter by content types
            filtered_content = [
                item for item in all_content 
                if item.get('content_type', 'unknown') in context.content_types
            ]
            
            # Filter by age
            recent_content = self._filter_by_age(filtered_content)
            
            # Score content for relevance
            scored_content = []
            for item in all_content:
                score = self._calculate_relevance_score(item.to_dict(), context)
                if score >= self.relevance_threshold:
                    reason = self._determine_surface_reason(item.to_dict(), context, score)
                    
                    surfaced = SurfacedContent(
                        uid=item.uid,
                        title=item.title,
                        source=item.source,
                        content_type=item.content_type.value,
                        relevance_score=score,
                        surface_reason=reason,
                        metadata=item.to_dict(),
                        updated_at=datetime.now().isoformat()
                    )
                    scored_content.append(surfaced)
            
            # Sort by relevance score and return top results
            scored_content.sort(key=lambda x: x.relevance_score, reverse=True)
            return scored_content[:context.max_results]
            
        except Exception as e:
            print(f"Error surfacing content: {e}")
            return self._mock_surface_content(context)
    
    def surface_by_topic(self, 
                        topic: str, 
                        max_results: int = 5) -> List[SurfacedContent]:
        """Surface content related to a specific topic."""
        context = SurfacingContext(
            current_topic=topic,
            max_results=max_results
        )
        return self.surface_content(context)
    
    def surface_recent(self, 
                      days: int = 7, 
                      max_results: int = 10) -> List[SurfacedContent]:
        """Surface recently added content."""
        context = SurfacingContext(
            time_context="recent",
            max_results=max_results
        )
        
        # Override age filter for this specific call
        original_max_age = self.max_age_days
        self.max_age_days = days
        
        try:
            results = self.surface_content(context)
            return results
        finally:
            self.max_age_days = original_max_age
    
    def surface_by_content_type(self, 
                              content_type: str, 
                              max_results: int = 10) -> List[SurfacedContent]:
        """Surface content of a specific type."""
        context = SurfacingContext(
            content_types=[content_type],
            max_results=max_results
        )
        return self.surface_content(context)
    
    def surface_diverse_content(self, 
                               max_results: int = 10) -> List[SurfacedContent]:
        """Surface a diverse selection of content across types and topics."""
        if not self.metadata_manager:
            return self._mock_surface_content(SurfacingContext(max_results=max_results))
        
        try:
            # Get all content items
            all_content = self._get_all_content()
            
            # Group by content type
            content_by_type = defaultdict(list)
            for item in all_content:
                content_type = item.get('content_type', 'unknown')
                content_by_type[content_type].append(item)
            
            # Sample from each type to ensure diversity
            surfaced_content = []
            types = list(content_by_type.keys())
            
            items_per_type = max(1, max_results // len(types)) if types else max_results
            
            for content_type in types:
                type_items = content_by_type[content_type]
                # Sort by recency for each type
                type_items.sort(key=lambda x: x.get('created_at', ''), reverse=True)
                # Take a sample
                sampled_items = type_items[:items_per_type]
                
                for item in sampled_items:
                    surfaced = SurfacedContent(
                        uid=item.uid,
                        title=item.title,
                        source=item.source,
                        content_type=item.content_type.value,
                        relevance_score=0.5,  # Base score for diversity
                        surface_reason=f"Diverse selection from {content_type} content",
                        metadata=item.to_dict(),
                        updated_at=datetime.now().isoformat()
                    )
                    surfaced_content.append(surfaced)
            
            # Sort by relevance and return top results
            surfaced_content.sort(key=lambda x: x.relevance_score, reverse=True)
            return surfaced_content[:max_results]
            
        except Exception as e:
            print(f"Error surfacing diverse content: {e}")
            return self._mock_surface_content(SurfacingContext(max_results=max_results))
    
    def _get_all_content(self) -> List[Dict[str, Any]]:
        """Get all content items from metadata manager."""
        try:
            return self.metadata_manager.get_all_metadata()
        except Exception:
            return []
    
    def _filter_by_age(self, content_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter content by maximum age.""" 
        if self.max_age_days <= 0:
            return content_items
            
        cutoff_date = datetime.now() - timedelta(days=self.max_age_days)
        
        filtered = []
        for item in content_items:
            try:
                created_at = item.created_at
                if created_at:
                    content_date = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    if content_date >= cutoff_date:
                        filtered.append(item)
                else:
                    # Include items without dates (assume recent)
                    filtered.append(item)
            except Exception:
                # Include items with unparseable dates
                filtered.append(item)
                
        return filtered
    
    def _calculate_relevance_score(self, 
                                  item: Dict[str, Any], 
                                  context: SurfacingContext) -> float:
        """Calculate relevance score for content item."""
        score = 0.0
        
        # Base score for content type preference
        if item.content_type.value in context.content_types:
            score += 0.2
        
        # Topic/title matching
        if context.current_topic:
            title = item.title.lower()
            topic_lower = context.current_topic.lower()
            
            if topic_lower in title:
                score += 0.4
            elif any(word in title for word in topic_lower.split()):
                score += 0.2
        
        # Recent query matching
        if context.recent_queries:
            title = item.title.lower()
            content = item.content.lower()
            
            for query in context.recent_queries:
                query_lower = query.lower()
                if query_lower in title:
                    score += 0.3
                elif query_lower in content:
                    score += 0.1
        
        # Recency boost
        if self.boost_recent:
            try:
                created_at = item.created_at
                if created_at:
                    content_date = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    days_ago = (datetime.now() - content_date).days
                    
                    if days_ago <= 7:
                        score += 0.2  # Recent content boost
                    elif days_ago <= 30:
                        score += 0.1  # Somewhat recent boost
            except Exception:
                pass
        
        return min(score, 1.0)  # Cap at 1.0
    
    def _determine_surface_reason(self, 
                                 item: Dict[str, Any], 
                                 context: SurfacingContext, 
                                 score: float) -> str:
        """Determine why content was surfaced."""
        reasons = []
        
        if context.current_topic:
            title = item.title.lower()
            if context.current_topic.lower() in title:
                reasons.append(f"matches topic '{context.current_topic}'")
        
        if context.recent_queries:
            for query in context.recent_queries:
                if query.lower() in item.title.lower():
                    reasons.append(f"matches recent query '{query}'")
                    break
        
        try:
            created_at = item.created_at
            if created_at:
                content_date = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                days_ago = (datetime.now() - content_date).days
                
                if days_ago <= 7:
                    reasons.append("recently added")
        except Exception:
            pass
        
        if score > 0.7:
            reasons.append("high relevance score")
        
        if not reasons:
            return "general relevance"
        
        return ", ".join(reasons)
    
    def _mock_surface_content(self, context: SurfacingContext) -> List[SurfacedContent]:
        """Mock content surfacing for when metadata manager unavailable."""
        mock_content = [
            SurfacedContent(
                uid="mock_1",
                title="Understanding Machine Learning Fundamentals",
                source="https://example.com/ml-fundamentals",
                content_type="article",
                relevance_score=0.85,
                surface_reason="matches current topic",
                metadata={"tags": ["machine learning", "AI", "fundamentals"]},
                updated_at=datetime.now().isoformat()
            ),
            SurfacedContent(
                uid="mock_2", 
                title="Recent Advances in Neural Networks",
                source="https://example.com/neural-networks",
                content_type="article",
                relevance_score=0.72,
                surface_reason="recently added, high relevance",
                metadata={"tags": ["neural networks", "deep learning"]},
                updated_at=datetime.now().isoformat()
            ),
            SurfacedContent(
                uid="mock_3",
                title="AI Ethics and Society Podcast",
                source="https://example.com/ai-ethics-podcast",
                content_type="podcast",
                relevance_score=0.68,
                surface_reason="related to current interests",
                metadata={"tags": ["AI", "ethics", "society"]},
                updated_at=datetime.now().isoformat()
            )
        ]
        
        # Filter by context preferences
        filtered = [
            item for item in mock_content
            if item.content_type in context.content_types
        ]
        
        # Apply topic filtering if specified
        if context.current_topic:
            topic_lower = context.current_topic.lower()
            filtered = [
                item for item in filtered
                if topic_lower in item.title.lower() or 
                   any(topic_lower in tag.lower() for tag in item.metadata.get('tags', []))
            ]
        
        return filtered[:context.max_results]


if __name__ == "__main__":
    # Example usage
    surfacer = ProactiveSurfacer()
    
    # Test topic-based surfacing
    context = SurfacingContext(
        current_topic="machine learning",
        max_results=5
    )
    
    results = surfacer.surface_content(context)
    
    print("Proactive Content Surfacing Results:")
    print("=" * 40)
    
    for result in results:
        print(f"\nTitle: {result.title}")
        print(f"Type: {result.content_type}")
        print(f"Relevance: {result.relevance_score:.2f}")
        print(f"Reason: {result.surface_reason}")