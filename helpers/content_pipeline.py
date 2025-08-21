#!/usr/bin/env python3
"""
Unified Content Processing Pipeline

Consolidates all content processing stages into a configurable pipeline system.
Provides unified interface for classification, detection, processing, summarization,
clustering, and export operations.

Key Features:
- Configurable pipeline stages
- Unified content processing interface  
- Integration with existing processing components
- Flexible stage ordering and configuration
- Comprehensive metadata handling
- Performance monitoring and statistics
"""

import json
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Union, Callable

from helpers.utils import log_info, log_error


class ProcessingStage(Enum):
    """Available processing stages"""
    DETECT_TYPE = "detect_type"
    CLASSIFY_CONTENT = "classify_content" 
    PROCESS_DOCUMENT = "process_document"
    EXTRACT_METADATA = "extract_metadata"
    SUMMARIZE_CONTENT = "summarize_content"
    CLUSTER_TOPICS = "cluster_topics"
    EXPORT_CONTENT = "export_content"
    ANALYZE_QUALITY = "analyze_quality"
    GENERATE_INSIGHTS = "generate_insights"


@dataclass
class PipelineConfig:
    """Configuration for content pipeline"""
    enabled_stages: List[ProcessingStage]
    stage_options: Dict[str, Dict[str, Any]]
    default_options: Dict[str, Any]
    performance_tracking: bool = True
    stop_on_error: bool = False
    parallel_stages: List[str] = None
    
    def __post_init__(self):
        if self.parallel_stages is None:
            self.parallel_stages = []


@dataclass 
class ProcessingResult:
    """Result from a single processing stage"""
    stage: ProcessingStage
    success: bool
    data: Any = None
    error: str = None
    processing_time: float = 0.0
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class ContentResult:
    """Unified result container for content processing"""
    content: str
    title: str = None
    url: str = None
    content_type: str = None
    classification: Dict[str, Any] = None
    processed_content: str = None
    metadata: Dict[str, Any] = None
    summary: str = None
    topics: List[str] = None
    quality_score: float = 0.0
    insights: Dict[str, Any] = None
    exports: Dict[str, str] = None
    processing_stages: List[ProcessingResult] = None
    total_processing_time: float = 0.0
    pipeline_config: str = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
        if self.processing_stages is None:
            self.processing_stages = []
        if self.exports is None:
            self.exports = {}
        if self.insights is None:
            self.insights = {}


@dataclass
class PipelineStats:
    """Statistics for pipeline processing"""
    total_processed: int = 0
    total_successful: int = 0
    total_failed: int = 0
    stage_stats: Dict[str, Dict[str, int]] = None
    average_processing_time: float = 0.0
    processing_times: List[float] = None
    last_updated: str = None
    
    def __post_init__(self):
        if self.stage_stats is None:
            self.stage_stats = {}
        if self.processing_times is None:
            self.processing_times = []
        if self.last_updated is None:
            self.last_updated = datetime.now().isoformat()


class ContentPipeline:
    """
    Unified content processing pipeline with configurable stages.
    
    Orchestrates all content processing through a flexible, configurable pipeline
    that can handle various content types with different processing requirements.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize ContentPipeline with configuration."""
        self.config = config or {}
        self.pipeline_config = self._create_pipeline_config()
        
        # Statistics tracking
        self.stats_file = Path(self.config.get('stats_file', 'data/pipeline_stats.json'))
        self.stats_file.parent.mkdir(parents=True, exist_ok=True)
        self.stats = self._load_stats()
        
        # Initialize processing components (lazy loading)
        self._components = {}
        self._component_cache = {}
        
        log_info("", "ContentPipeline initialized with configurable processing stages")
    
    def _create_pipeline_config(self) -> PipelineConfig:
        """Create pipeline configuration from config dict."""
        # Default pipeline stages
        default_stages = [
            ProcessingStage.DETECT_TYPE,
            ProcessingStage.CLASSIFY_CONTENT,
            ProcessingStage.PROCESS_DOCUMENT,
            ProcessingStage.EXTRACT_METADATA
        ]
        
        # Optional stages based on config
        if self.config.get('enable_summarization', False):
            default_stages.append(ProcessingStage.SUMMARIZE_CONTENT)
            
        if self.config.get('enable_clustering', False):
            default_stages.append(ProcessingStage.CLUSTER_TOPICS)
            
        if self.config.get('enable_export', True):
            default_stages.append(ProcessingStage.EXPORT_CONTENT)
            
        if self.config.get('enable_quality_analysis', False):
            default_stages.append(ProcessingStage.ANALYZE_QUALITY)
        
        # Stage-specific options
        stage_options = {
            'detect_type': self.config.get('detection_config', {}),
            'classify_content': self.config.get('classification_config', {}),
            'process_document': self.config.get('processing_config', {}),
            'extract_metadata': self.config.get('metadata_config', {}),
            'summarize_content': self.config.get('summarization_config', {}),
            'cluster_topics': self.config.get('clustering_config', {}),
            'export_content': self.config.get('export_config', {}),
            'analyze_quality': self.config.get('quality_config', {}),
            'generate_insights': self.config.get('insights_config', {})
        }
        
        return PipelineConfig(
            enabled_stages=self.config.get('enabled_stages', default_stages),
            stage_options=stage_options,
            default_options=self.config.get('default_options', {}),
            performance_tracking=self.config.get('performance_tracking', True),
            stop_on_error=self.config.get('stop_on_error', False),
            parallel_stages=self.config.get('parallel_stages', ['extract_metadata'])
        )
    
    def _get_component(self, component_name: str):
        """Lazy load processing components."""
        if component_name not in self._components:
            try:
                if component_name == 'content_detector':
                    from helpers.content_detector import SmartContentDetector
                    self._components[component_name] = SmartContentDetector()
                    
                elif component_name == 'content_classifier':
                    from helpers.content_classifier import ContentClassifier
                    self._components[component_name] = ContentClassifier()
                    
                elif component_name == 'document_processor':
                    from helpers.document_processor import DocumentProcessor
                    self._components[component_name] = DocumentProcessor(self.config)
                    
                elif component_name == 'content_exporter':
                    from helpers.content_exporter import ContentExporter
                    self._components[component_name] = ContentExporter(self.config)
                    
                else:
                    log_error("", f"Unknown component: {component_name}")
                    return None
                    
            except ImportError as e:
                log_error("", f"Failed to import {component_name}: {e}")
                return None
                
        return self._components.get(component_name)
    
    def _load_stats(self) -> PipelineStats:
        """Load pipeline statistics from disk."""
        try:
            if self.stats_file.exists():
                with open(self.stats_file, 'r') as f:
                    data = json.load(f)
                    return PipelineStats(**data)
        except Exception as e:
            log_error("", f"Failed to load pipeline stats: {e}")
        
        return PipelineStats()
    
    def _save_stats(self):
        """Save pipeline statistics to disk."""
        try:
            self.stats.last_updated = datetime.now().isoformat()
            with open(self.stats_file, 'w') as f:
                json.dump(asdict(self.stats), f, indent=2)
        except Exception as e:
            log_error("", f"Failed to save pipeline stats: {e}")
    
    def _record_processing(self, success: bool, processing_time: float, stage_results: List[ProcessingResult]):
        """Record processing statistics."""
        self.stats.total_processed += 1
        
        if success:
            self.stats.total_successful += 1
        else:
            self.stats.total_failed += 1
        
        # Update processing times
        self.stats.processing_times.append(processing_time)
        if len(self.stats.processing_times) > 1000:
            self.stats.processing_times = self.stats.processing_times[-1000:]
        
        # Update average
        if self.stats.processing_times:
            self.stats.average_processing_time = sum(self.stats.processing_times) / len(self.stats.processing_times)
        
        # Record stage statistics
        for stage_result in stage_results:
            stage_name = stage_result.stage.value
            
            if stage_name not in self.stats.stage_stats:
                self.stats.stage_stats[stage_name] = {
                    'attempts': 0,
                    'successes': 0,
                    'failures': 0,
                    'avg_time': 0.0
                }
            
            stage_stats = self.stats.stage_stats[stage_name]
            stage_stats['attempts'] += 1
            
            if stage_result.success:
                stage_stats['successes'] += 1
            else:
                stage_stats['failures'] += 1
            
            # Update average time
            current_avg = stage_stats['avg_time']
            attempts = stage_stats['attempts']
            stage_stats['avg_time'] = ((current_avg * (attempts - 1)) + stage_result.processing_time) / attempts
    
    def process_content(self, 
                       content: str,
                       title: str = None,
                       url: str = None,
                       pipeline_options: Dict[str, Any] = None,
                       log_path: str = "") -> ContentResult:
        """
        Process content through configurable pipeline stages.
        
        Args:
            content: Content to process
            title: Optional title
            url: Optional source URL
            pipeline_options: Override default pipeline configuration
            log_path: Path for logging
            
        Returns:
            ContentResult with processing outcomes
        """
        start_time = time.time()
        
        log_info(log_path, f"Processing content through pipeline (length: {len(content)} chars)")
        
        # Initialize result container
        result = ContentResult(
            content=content,
            title=title,
            url=url,
            pipeline_config=json.dumps(asdict(self.pipeline_config), default=str)
        )
        
        # Determine stages to run
        stages_to_run = pipeline_options.get('stages', self.pipeline_config.enabled_stages) if pipeline_options else self.pipeline_config.enabled_stages
        
        # Process each stage
        stage_results = []
        
        for stage in stages_to_run:
            try:
                log_info(log_path, f"Running pipeline stage: {stage.value}")
                stage_result = self._run_stage(stage, result, pipeline_options or {}, log_path)
                stage_results.append(stage_result)
                
                if not stage_result.success:
                    log_error(log_path, f"Stage {stage.value} failed: {stage_result.error}")
                    if self.pipeline_config.stop_on_error:
                        break
                else:
                    log_info(log_path, f"Stage {stage.value} completed in {stage_result.processing_time:.2f}s")
                    
            except Exception as e:
                log_error(log_path, f"Exception in stage {stage.value}: {e}")
                stage_results.append(ProcessingResult(
                    stage=stage,
                    success=False,
                    error=str(e)
                ))
                
                if self.pipeline_config.stop_on_error:
                    break
        
        # Finalize result
        result.processing_stages = stage_results
        result.total_processing_time = time.time() - start_time
        
        # Determine overall success
        success = any(r.success for r in stage_results)
        
        # Record statistics
        if self.pipeline_config.performance_tracking:
            self._record_processing(success, result.total_processing_time, stage_results)
            self._save_stats()
        
        log_info(log_path, f"Content processing completed in {result.total_processing_time:.2f}s ({len(stage_results)} stages)")
        
        return result
    
    def _run_stage(self, 
                   stage: ProcessingStage, 
                   content_result: ContentResult,
                   options: Dict[str, Any],
                   log_path: str) -> ProcessingResult:
        """Run a single pipeline stage."""
        start_time = time.time()
        
        try:
            if stage == ProcessingStage.DETECT_TYPE:
                return self._run_detect_type_stage(content_result, options, log_path)
                
            elif stage == ProcessingStage.CLASSIFY_CONTENT:
                return self._run_classify_content_stage(content_result, options, log_path)
                
            elif stage == ProcessingStage.PROCESS_DOCUMENT:
                return self._run_process_document_stage(content_result, options, log_path)
                
            elif stage == ProcessingStage.EXTRACT_METADATA:
                return self._run_extract_metadata_stage(content_result, options, log_path)
                
            elif stage == ProcessingStage.SUMMARIZE_CONTENT:
                return self._run_summarize_content_stage(content_result, options, log_path)
                
            elif stage == ProcessingStage.CLUSTER_TOPICS:
                return self._run_cluster_topics_stage(content_result, options, log_path)
                
            elif stage == ProcessingStage.EXPORT_CONTENT:
                return self._run_export_content_stage(content_result, options, log_path)
                
            elif stage == ProcessingStage.ANALYZE_QUALITY:
                return self._run_analyze_quality_stage(content_result, options, log_path)
                
            elif stage == ProcessingStage.GENERATE_INSIGHTS:
                return self._run_generate_insights_stage(content_result, options, log_path)
                
            else:
                return ProcessingResult(
                    stage=stage,
                    success=False,
                    error=f"Unknown stage: {stage}",
                    processing_time=time.time() - start_time
                )
                
        except Exception as e:
            return ProcessingResult(
                stage=stage,
                success=False,
                error=str(e),
                processing_time=time.time() - start_time
            )
    
    def _run_detect_type_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run content type detection stage."""
        detector = self._get_component('content_detector')
        if not detector:
            return ProcessingResult(
                stage=ProcessingStage.DETECT_TYPE,
                success=False,
                error="Content detector not available"
            )
        
        try:
            # Use URL if available, otherwise analyze content
            if result.url:
                detection_result = detector.detect_from_url(result.url)
            else:
                detection_result = detector.detect_from_content(result.content)
            
            result.content_type = detection_result.content_type
            result.metadata.update(detection_result.metadata)
            
            return ProcessingResult(
                stage=ProcessingStage.DETECT_TYPE,
                success=True,
                data=detection_result,
                metadata={'confidence': detection_result.confidence}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.DETECT_TYPE,
                success=False,
                error=str(e)
            )
    
    def _run_classify_content_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run content classification stage."""
        classifier = self._get_component('content_classifier')
        if not classifier:
            return ProcessingResult(
                stage=ProcessingStage.CLASSIFY_CONTENT,
                success=False,
                error="Content classifier not available"
            )
        
        try:
            classification_result = classifier.classify_content(
                title=result.title or "",
                content=result.content,
                url=result.url
            )
            
            result.classification = {
                'category': classification_result.category,
                'confidence': classification_result.confidence,
                'subcategory': classification_result.subcategory,
                'tags': classification_result.tags,
                'reasoning': classification_result.reasoning
            }
            
            return ProcessingResult(
                stage=ProcessingStage.CLASSIFY_CONTENT,
                success=True,
                data=classification_result,
                metadata={'confidence': classification_result.confidence}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.CLASSIFY_CONTENT,
                success=False,
                error=str(e)
            )
    
    def _run_process_document_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run document processing stage."""
        processor = self._get_component('document_processor')
        if not processor:
            # Skip if document processor not available
            return ProcessingResult(
                stage=ProcessingStage.PROCESS_DOCUMENT,
                success=True,
                data="Document processor not available, using original content",
                metadata={'skipped': True}
            )
        
        try:
            # Process content based on detected type
            processed_content = result.content  # Default to original content
            
            # Basic content cleaning and processing
            from markdownify import markdownify
            from readability import Document
            
            if result.content_type == 'article' or 'html' in result.content.lower():
                # HTML article processing
                doc = Document(result.content)
                clean_html = doc.summary()
                processed_content = markdownify(clean_html)
                
            result.processed_content = processed_content
            
            return ProcessingResult(
                stage=ProcessingStage.PROCESS_DOCUMENT,
                success=True,
                data=processed_content,
                metadata={'content_length': len(processed_content)}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.PROCESS_DOCUMENT,
                success=False,
                error=str(e)
            )
    
    def _run_extract_metadata_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run metadata extraction stage."""
        try:
            # Extract basic metadata from content
            metadata = {}
            
            content_to_analyze = result.processed_content or result.content
            
            # Basic metadata extraction
            metadata['word_count'] = len(content_to_analyze.split())
            metadata['character_count'] = len(content_to_analyze)
            metadata['processing_timestamp'] = datetime.now().isoformat()
            
            if result.title:
                metadata['title_length'] = len(result.title)
            
            if result.url:
                from urllib.parse import urlparse
                parsed = urlparse(result.url)
                metadata['domain'] = parsed.netloc
                metadata['path'] = parsed.path
            
            # Update result metadata
            result.metadata.update(metadata)
            
            return ProcessingResult(
                stage=ProcessingStage.EXTRACT_METADATA,
                success=True,
                data=metadata,
                metadata={'extracted_fields': len(metadata)}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.EXTRACT_METADATA,
                success=False,
                error=str(e)
            )
    
    def _run_summarize_content_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run content summarization stage."""
        try:
            # Basic summarization (first few sentences)
            content_to_summarize = result.processed_content or result.content
            
            # Simple extractive summarization
            sentences = content_to_summarize.split('. ')
            if len(sentences) > 3:
                summary = '. '.join(sentences[:3]) + '.'
            else:
                summary = content_to_summarize[:500] + '...' if len(content_to_summarize) > 500 else content_to_summarize
            
            result.summary = summary
            
            return ProcessingResult(
                stage=ProcessingStage.SUMMARIZE_CONTENT,
                success=True,
                data=summary,
                metadata={'summary_length': len(summary)}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.SUMMARIZE_CONTENT,
                success=False,
                error=str(e)
            )
    
    def _run_cluster_topics_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run topic clustering stage.""" 
        try:
            # Basic keyword extraction for topics
            content_to_analyze = result.processed_content or result.content
            
            # Simple topic extraction (common words, excluding stop words)
            import re
            words = re.findall(r'\b[a-zA-Z]{4,}\b', content_to_analyze.lower())
            
            # Basic stop words
            stop_words = {'that', 'this', 'with', 'from', 'have', 'been', 'they', 'were', 'said', 'each', 'which', 'their', 'time', 'will', 'about', 'would', 'there', 'could', 'other'}
            
            word_freq = {}
            for word in words:
                if word not in stop_words and len(word) > 4:
                    word_freq[word] = word_freq.get(word, 0) + 1
            
            # Get top topics
            topics = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
            result.topics = [topic[0] for topic in topics]
            
            return ProcessingResult(
                stage=ProcessingStage.CLUSTER_TOPICS,
                success=True,
                data=result.topics,
                metadata={'topic_count': len(result.topics)}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.CLUSTER_TOPICS,
                success=False,
                error=str(e)
            )
    
    def _run_export_content_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run content export stage."""
        exporter = self._get_component('content_exporter')
        if not exporter:
            return ProcessingResult(
                stage=ProcessingStage.EXPORT_CONTENT,
                success=True,
                data="Content exporter not available",
                metadata={'skipped': True}
            )
        
        try:
            # Export in configured formats
            export_formats = options.get('export_formats', ['json', 'markdown'])
            exports = {}
            
            for format_type in export_formats:
                try:
                    if format_type == 'json':
                        exports['json'] = json.dumps(asdict(result), indent=2, default=str)
                    elif format_type == 'markdown':
                        exports['markdown'] = self._generate_markdown_export(result)
                except Exception as format_error:
                    log_error(log_path, f"Failed to export as {format_type}: {format_error}")
            
            result.exports = exports
            
            return ProcessingResult(
                stage=ProcessingStage.EXPORT_CONTENT,
                success=True,
                data=exports,
                metadata={'export_formats': list(exports.keys())}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.EXPORT_CONTENT,
                success=False,
                error=str(e)
            )
    
    def _run_analyze_quality_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run content quality analysis stage."""
        try:
            # Basic quality scoring
            quality_score = 0.0
            factors = []
            
            content_to_analyze = result.processed_content or result.content
            
            # Length factor
            word_count = len(content_to_analyze.split())
            if word_count > 100:
                quality_score += 0.3
                factors.append(f"Sufficient length ({word_count} words)")
            
            # Title factor  
            if result.title and len(result.title) > 10:
                quality_score += 0.2
                factors.append("Has meaningful title")
            
            # Classification confidence factor
            if result.classification and result.classification.get('confidence', 0) > 0.7:
                quality_score += 0.2
                factors.append(f"High classification confidence ({result.classification['confidence']:.2f})")
            
            # Metadata richness factor
            if len(result.metadata) > 5:
                quality_score += 0.15
                factors.append(f"Rich metadata ({len(result.metadata)} fields)")
            
            # Topic extraction success factor  
            if result.topics and len(result.topics) > 3:
                quality_score += 0.15
                factors.append(f"Clear topics identified ({len(result.topics)})")
            
            result.quality_score = min(quality_score, 1.0)
            
            return ProcessingResult(
                stage=ProcessingStage.ANALYZE_QUALITY,
                success=True,
                data={'score': result.quality_score, 'factors': factors},
                metadata={'quality_score': result.quality_score}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.ANALYZE_QUALITY,
                success=False,
                error=str(e)
            )
    
    def _run_generate_insights_stage(self, result: ContentResult, options: Dict, log_path: str) -> ProcessingResult:
        """Run insight generation stage."""
        try:
            insights = {}
            
            # Content insights
            content_to_analyze = result.processed_content or result.content
            insights['readability'] = {
                'word_count': len(content_to_analyze.split()),
                'sentence_count': len(content_to_analyze.split('. ')),
                'avg_words_per_sentence': len(content_to_analyze.split()) / max(len(content_to_analyze.split('. ')), 1)
            }
            
            # Classification insights
            if result.classification:
                insights['classification'] = {
                    'category': result.classification.get('category'),
                    'confidence': result.classification.get('confidence'),
                    'needs_review': result.classification.get('confidence', 0) < 0.7
                }
            
            # Processing insights
            insights['processing'] = {
                'total_time': result.total_processing_time,
                'stages_run': len(result.processing_stages),
                'stages_successful': sum(1 for s in result.processing_stages if s.success),
                'quality_score': result.quality_score
            }
            
            result.insights = insights
            
            return ProcessingResult(
                stage=ProcessingStage.GENERATE_INSIGHTS,
                success=True,
                data=insights,
                metadata={'insight_categories': len(insights)}
            )
            
        except Exception as e:
            return ProcessingResult(
                stage=ProcessingStage.GENERATE_INSIGHTS,
                success=False,
                error=str(e)
            )
    
    def _generate_markdown_export(self, result: ContentResult) -> str:
        """Generate markdown export of processing result."""
        markdown = []
        
        # Header
        if result.title:
            markdown.append(f"# {result.title}\n")
        
        if result.url:
            markdown.append(f"**Source:** {result.url}\n")
        
        # Metadata section
        if result.metadata:
            markdown.append("## Metadata\n")
            for key, value in result.metadata.items():
                markdown.append(f"- **{key}:** {value}")
            markdown.append("")
        
        # Classification
        if result.classification:
            markdown.append("## Classification\n")
            markdown.append(f"- **Category:** {result.classification.get('category', 'Unknown')}")
            markdown.append(f"- **Confidence:** {result.classification.get('confidence', 0):.2f}")
            if result.classification.get('tags'):
                markdown.append(f"- **Tags:** {', '.join(result.classification['tags'])}")
            markdown.append("")
        
        # Summary
        if result.summary:
            markdown.append("## Summary\n")
            markdown.append(result.summary)
            markdown.append("")
        
        # Topics
        if result.topics:
            markdown.append("## Topics\n")
            markdown.append(", ".join(result.topics))
            markdown.append("")
        
        # Content
        markdown.append("## Content\n")
        content_to_include = result.processed_content or result.content
        markdown.append(content_to_include)
        
        return "\n".join(markdown)
    
    def bulk_process_content(self, 
                           content_items: List[Dict[str, Any]], 
                           pipeline_options: Dict[str, Any] = None,
                           log_path: str = "") -> List[ContentResult]:
        """
        Process multiple content items through the pipeline.
        
        Args:
            content_items: List of dicts with 'content', optional 'title', 'url'
            pipeline_options: Pipeline configuration overrides
            log_path: Path for logging
            
        Returns:
            List of ContentResult objects
        """
        log_info(log_path, f"Bulk processing {len(content_items)} content items")
        
        results = []
        for i, item in enumerate(content_items):
            try:
                log_info(log_path, f"Processing item {i+1}/{len(content_items)}")
                
                result = self.process_content(
                    content=item['content'],
                    title=item.get('title'),
                    url=item.get('url'),
                    pipeline_options=pipeline_options,
                    log_path=log_path
                )
                results.append(result)
                
            except Exception as e:
                log_error(log_path, f"Failed to process item {i+1}: {e}")
                # Create error result
                error_result = ContentResult(
                    content=item.get('content', ''),
                    title=item.get('title'),
                    url=item.get('url')
                )
                error_result.processing_stages = [ProcessingResult(
                    stage=ProcessingStage.DETECT_TYPE,
                    success=False,
                    error=str(e)
                )]
                results.append(error_result)
        
        success_count = sum(1 for r in results if any(s.success for s in r.processing_stages))
        log_info(log_path, f"Bulk processing complete: {success_count}/{len(content_items)} successful")
        
        return results
    
    def get_pipeline_stats(self) -> Dict[str, Any]:
        """Get detailed pipeline processing statistics.""" 
        stats_dict = asdict(self.stats)
        
        # Calculate success rates
        if self.stats.total_processed > 0:
            stats_dict['overall_success_rate'] = self.stats.total_successful / self.stats.total_processed
        else:
            stats_dict['overall_success_rate'] = 0.0
        
        # Stage success rates
        stage_rates = {}
        for stage, data in self.stats.stage_stats.items():
            attempts = data.get('attempts', 0)
            if attempts > 0:
                stage_rates[stage] = {
                    'success_rate': data.get('successes', 0) / attempts,
                    'attempts': attempts,
                    'avg_time': data.get('avg_time', 0.0)
                }
        stats_dict['stage_success_rates'] = stage_rates
        
        return stats_dict
    
    def reset_stats(self):
        """Reset pipeline statistics."""
        self.stats = PipelineStats()
        self._save_stats()
        log_info("", "Pipeline statistics reset")
    
    def export_stats(self, filepath: str = None) -> str:
        """Export statistics to JSON file."""
        if not filepath:
            filepath = f"pipeline_stats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        stats_export = self.get_pipeline_stats()
        
        with open(filepath, 'w') as f:
            json.dump(stats_export, f, indent=2)
        
        log_info("", f"Pipeline statistics exported to {filepath}")
        return filepath


# Factory function
def create_content_pipeline(config: Dict[str, Any] = None) -> ContentPipeline:
    """Create ContentPipeline instance."""
    return ContentPipeline(config)


# Legacy compatibility
class ContentProcessor:
    """Legacy ContentProcessor interface for backward compatibility."""
    
    def __init__(self, config=None):
        import warnings
        warnings.warn(
            "ContentProcessor is deprecated, use ContentPipeline instead",
            DeprecationWarning,
            stacklevel=2
        )
        self.pipeline = ContentPipeline(config)
    
    def process(self, content: str, **kwargs):
        """Legacy process method."""
        result = self.pipeline.process_content(content, **kwargs)
        return result.processed_content or result.content


if __name__ == "__main__":
    # Example usage
    config = {
        'enable_summarization': True,
        'enable_clustering': True,
        'export_formats': ['json', 'markdown']
    }
    
    pipeline = ContentPipeline(config)
    
    # Test single content processing
    result = pipeline.process_content(
        content="This is a test article about machine learning and AI.",
        title="Test Article",
        url="https://example.com/test"
    )
    
    print(f"Processed content with {len(result.processing_stages)} stages")
    print(f"Quality score: {result.quality_score:.2f}")
    print(f"Topics: {result.topics}")
    
    # Test bulk processing
    content_items = [
        {'content': 'Article 1 content', 'title': 'Article 1'},
        {'content': 'Article 2 content', 'title': 'Article 2'}
    ]
    
    bulk_results = pipeline.bulk_process_content(content_items)
    print(f"Bulk processed {len(bulk_results)} items")
    
    # Show statistics
    stats = pipeline.get_pipeline_stats()
    print(f"Pipeline success rate: {stats['overall_success_rate']:.2%}")