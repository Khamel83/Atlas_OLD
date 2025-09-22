#!/usr/bin/env python3
"""
Token Optimization System

Optimizes context for token efficiency using compression and other techniques.
"""

import asyncio
import json
import logging
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import re
from pathlib import Path

@dataclass
class OptimizationResult:
    """Result of token optimization"""
    original_tokens: int
    optimized_tokens: int
    reduction_percentage: float
    techniques_used: List[str]
    compressed_content: Dict[str, Any]

class TokenOptimizer:
    """Handles token optimization through various techniques"""

    def __init__(self):
        self.logger = logging.getLogger("token_optimizer")

    async def estimate_context_tokens(self, context: Dict[str, Any]) -> int:
        """Estimate token count for a context object"""
        # Simple estimation: ~4 chars per token on average
        context_json = json.dumps(context, indent=2)
        return len(context_json) // 4

    async def optimize_for_budget(self, context: Dict[str, Any], target_tokens: int) -> Tuple[Dict[str, Any], OptimizationResult]:
        """Optimize context to fit within token budget"""
        original_tokens = await self.estimate_context_tokens(context)

        if original_tokens <= target_tokens:
            # No optimization needed
            return context, OptimizationResult(
                original_tokens=original_tokens,
                optimized_tokens=original_tokens,
                reduction_percentage=0.0,
                techniques_used=[],
                compressed_content=context
            )

        optimized_context = context.copy()
        techniques_used = []

        # Technique 1: Remove redundant whitespace and formatting
        optimized_context = self._compress_json_structure(optimized_context)
        techniques_used.append("json_compression")

        current_tokens = await self.estimate_context_tokens(optimized_context)

        # Technique 2: Remove less important fields if still over budget
        if current_tokens > target_tokens:
            optimized_context = self._remove_less_important_fields(optimized_context, target_tokens)
            techniques_used.append("field_pruning")

        current_tokens = await self.estimate_context_tokens(optimized_context)

        # Technique 3: Summarize long text content
        if current_tokens > target_tokens:
            optimized_context = self._summarize_long_content(optimized_context, target_tokens)
            techniques_used.append("content_summarization")

        current_tokens = await self.estimate_context_tokens(optimized_context)

        # Calculate final results
        optimized_tokens = current_tokens
        reduction_percentage = ((original_tokens - optimized_tokens) / original_tokens) * 100

        return optimized_context, OptimizationResult(
            original_tokens=original_tokens,
            optimized_tokens=optimized_tokens,
            reduction_percentage=reduction_percentage,
            techniques_used=techniques_used,
            compressed_content=optimized_context
        )

    def _compress_json_structure(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Compress JSON by removing whitespace and optimizing structure"""
        # Convert to compact JSON and back to remove whitespace
        json_str = json.dumps(context, separators=(',', ':'))
        return json.loads(json_str)

    def _remove_less_important_fields(self, context: Dict[str, Any], target_tokens: int) -> Dict[str, Any]:
        """Remove fields that are less important for the context"""
        # Define field priority (lower number = higher priority)
        field_priority = {
            # High priority - keep these
            'user_request': 1,
            'intent': 1,
            'key_entities': 2,
            'problems': 2,

            # Medium priority - might remove if needed
            'suggested_actions': 3,
            'metadata': 4,
            'timestamp': 5,

            # Low priority - remove first
            'debug_info': 10,
            'logs': 10,
            'verbose_output': 10
        }

        def prioritize_items(obj, current_tokens):
            """Recursively prioritize items to keep"""
            if isinstance(obj, dict):
                # Sort items by priority
                items = list(obj.items())
                items.sort(key=lambda x: field_priority.get(x[0], 5))

                # Keep high priority items first
                result = {}
                for key, value in items:
                    result[key] = prioritize_items(value, current_tokens)
                    # Simple token check - could be more sophisticated
                    if len(json.dumps(result)) // 4 > target_tokens * 0.8:  # 80% of target
                        break
                return result
            elif isinstance(obj, list):
                # Keep first few items of lists
                keep_count = max(1, len(obj) // 2)  # Keep at least half
                return [prioritize_items(item, current_tokens) for item in obj[:keep_count]]
            else:
                return obj

        return prioritize_items(context, target_tokens)

    def _summarize_long_content(self, context: Dict[str, Any], target_tokens: int) -> Dict[str, Any]:
        """Summarize long text content to reduce tokens"""
        def summarize_text(text: str, max_length: int = 500) -> str:
            """Simple text summarization"""
            if len(text) <= max_length:
                return text

            # Truncate with ellipsis
            return text[:max_length-3] + "..."

        def summarize_object(obj):
            """Recursively summarize text content"""
            if isinstance(obj, dict):
                return {k: summarize_object(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [summarize_object(item) for item in obj]
            elif isinstance(obj, str):
                return summarize_text(obj)
            else:
                return obj

        return summarize_object(context)

    async def analyze_context_usage(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze how context is being used"""
        analysis = {
            'total_tokens': await self.estimate_context_tokens(context),
            'structure_size': len(json.dumps(context, indent=2)),
            'compressed_size': len(json.dumps(context, separators=(',', ':'))),
            'key_fields': list(context.keys()) if isinstance(context, dict) else [],
            'optimization_opportunities': []
        }

        # Check for optimization opportunities
        if analysis['total_tokens'] > 3000:
            analysis['optimization_opportunities'].append("High token count - consider compression")

        if analysis['structure_size'] > analysis['compressed_size'] * 2:
            analysis['optimization_opportunities'].append("JSON formatting overhead - can be compressed")

        # Look for repetitive content
        context_str = json.dumps(context, separators=(',', ':'))
        if len(context_str) > 1000:
            # Simple repetition check
            words = context_str.split()
            word_counts = {}
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

            repetitive_words = [word for word, count in word_counts.items() if count > 5]
            if repetitive_words:
                analysis['optimization_opportunities'].append(f"Repetitive content: {', '.join(repetitive_words[:3])}")

        return analysis

async def optimize_for_budget(context: Dict[str, Any], target_tokens: int) -> Tuple[Dict[str, Any], OptimizationResult]:
    """Optimize context for token budget (async wrapper)"""
    optimizer = TokenOptimizer()
    return await optimizer.optimize_for_budget(context, target_tokens)

async def estimate_context_tokens(context: Dict[str, Any]) -> int:
    """Estimate token count for context (async wrapper)"""
    optimizer = TokenOptimizer()
    return await optimizer.estimate_context_tokens(context)