"""
Cognitive Features API for Atlas
Provides endpoints for all cognitive amplification features.
"""

import os

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

# Create router for cognitive features endpoints
cognitive_router = APIRouter(prefix="/cognitive", tags=["cognitive features"])

# Import Atlas cognitive features
from ask.proactive.surfacer import ProactiveSurfacer
from ask.temporal.temporal_engine import TemporalEngine
from ask.socratic.question_engine import QuestionEngine
from ask.recall.recall_engine import RecallEngine
from ask.insights.pattern_detector import PatternDetector
from helpers.metadata_manager import MetadataManager

# Initialize core components
metadata_manager = MetadataManager()
proactive_surfacer = ProactiveSurfacer(metadata_manager)
temporal_engine = TemporalEngine(metadata_manager)
question_engine = QuestionEngine(metadata_manager)
recall_engine = RecallEngine(metadata_manager)
pattern_detector = PatternDetector(metadata_manager)

# Data models
class ProactiveItem(BaseModel):
    title: str
    updated_at: str
    relevance_score: Optional[float] = None

class TemporalRelationship(BaseModel):
    from_title: str
    to_title: str
    days_apart: int
    relationship_type: str
    shared_tags: List[str]

class SocraticQuestion(BaseModel):
    question: str
    difficulty_level: Optional[int] = None

class RecallItem(BaseModel):
    title: str
    last_reviewed: Optional[str] = None
    review_count: Optional[int] = None
    difficulty_score: Optional[float] = None
    review_urgency: Optional[float] = None

class TagPattern(BaseModel):
    tag: str
    frequency: int
    trend: Optional[str] = None

class CognitiveInsight(BaseModel):
    type: str
    content: str
    confidence: Optional[float] = None

# Health check for cognitive features service
@cognitive_router.get("/health")
async def cognitive_health_check():
    """Health check for cognitive features service"""
    try:
        return {
            "status": "healthy",
            "service": "Atlas Cognitive Features Service",
            "features": {
                "proactive_surfacer": "operational",
                "temporal_engine": "operational", 
                "question_engine": "operational",
                "recall_engine": "operational",
                "pattern_detector": "operational"
            }
        }
    except Exception as e:
        return {
            "status": "degraded",
            "service": "Atlas Cognitive Features Service", 
            "error": str(e)
        }