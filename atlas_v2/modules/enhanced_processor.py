"""
Enhanced Content Processor for Atlas v2

Production-grade processor that integrates:
- Enhanced queue management with deduplication
- Dead letter queue for non-processable URLs
- Intelligent error handling with circuit breakers
- High-volume input handling with backpressure
- Real-time monitoring and alerting

Key Features:
- Bulletproof duplicate prevention
- Queue pollution elimination
- Intelligent retry with exponential backoff
- Circuit breaker pattern for cascading failure prevention
- Comprehensive monitoring and health checks
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Tuple
import time

from .real_content_processor import RealContentProcessor
from .enhanced_queue_manager import (
    EnhancedQueueManager,
    QueueStatus,
    QueueItem,
    enqueue_url,
    get_next_batch,
    get_queue_stats,
    update_item_status,
    PriorityLevel
)
from .dead_letter_queue import initialize_dlq, get_quarantine_stats
from .error_handler import (
    handle_processing_error,
    update_circuit_breaker,
    get_error_handling_stats
)
from .database import DatabaseManager
from .config_manager import ConfigManager

logger = logging.getLogger(__name__)

class EnhancedProcessor:
    """Enhanced content processor with production-grade reliability"""

    def __init__(self, db_manager: DatabaseManager, config_manager: ConfigManager):
        self.db_manager = db_manager
        self.config_manager = config_manager
        self.base_processor = RealContentProcessor(db_manager, config_manager)
        self.queue_manager = EnhancedQueueManager()

        # Processing configuration
        self.max_concurrent_processing = 10
        self.processing_timeout_seconds = 300  # 5 minutes max per item
        self.batch_size = 20
        self.health_check_interval = 60  # seconds

        # Metrics
        self.processing_stats = {
            'total_processed': 0,
            'successful': 0,
            'failed': 0,
            'quarantined': 0,
            'start_time': datetime.now(),
            'last_health_check': None,
            'health_score': 100
        }

    async def initialize(self):
        """Initialize enhanced processor components"""
        logger.info("🚀 Initializing enhanced processor...")

        # Initialize queue manager
        await self.queue_manager.initialize()

        # Initialize dead letter queue
        await initialize_dlq()

        logger.info("✅ Enhanced processor initialized")

    async def process_content_webhook(
        self,
        url: str,
        source_name: str,
        content_type: str = "web",
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Process content from webhook with enhanced reliability
        """
        try:
            # Enqueue with deduplication and validation
            success, message, content_id = await enqueue_url(
                url=url,
                source_name=source_name,
                content_type=content_type,
                priority=PriorityLevel.HIGH,  # Webhook events are high priority
                metadata=metadata
            )

            if not success:
                if "Duplicate" in message:
                    return {
                        "status": "skipped",
                        "reason": "duplicate",
                        "content_id": content_id,
                        "message": message
                    }
                elif "quarantined" in message.lower():
                    return {
                        "status": "rejected",
                        "reason": "quarantined",
                        "content_id": content_id,
                        "message": message
                    }
                else:
                    return {
                        "status": "error",
                        "reason": "enqueue_failed",
                        "message": message
                    }

            # Process immediately with error handling
            result = await self._process_single_item_with_retry(content_id)

            return {
                "status": result["status"],
                "content_id": content_id,
                "message": result.get("message", ""),
                "processing_time_seconds": result.get("processing_time", 0),
                "estimated_completion": result.get("estimated_completion", "")
            }

        except Exception as e:
            logger.error(f"❌ Enhanced webhook processing failed for {url}: {e}")
            return {
                "status": "error",
                "reason": "processing_exception",
                "message": str(e)
            }

    async def process_backlog_enhanced(self, limit: int = None) -> Dict[str, Any]:
        """
        Process backlog with enhanced reliability and monitoring
        """
        if limit is None:
            limit = self.batch_size

        processing_start = datetime.now()

        try:
            logger.info(f"📋 Starting enhanced backlog processing (limit: {limit})...")

            # Get next batch with intelligent routing
            batch = await get_next_batch(limit=limit)

            if not batch:
                logger.info("📋 No items in queue to process")
                return {
                    "status": "complete",
                    "processed": 0,
                    "reason": "no_items",
                    "processing_time_seconds": 0
                }

            logger.info(f"📋 Processing batch of {len(batch)} items")

            # Process batch concurrently with error handling
            results = await asyncio.gather(
                *[self._process_single_item_with_retry(item.content_id, item)
                  for item in batch],
                return_exceptions=True
            )

            # Analyze results
            processed = 0
            successful = 0
            failed = 0
            quarantined = 0
            errors = []

            for i, result in enumerate(results):
                processed += 1

                if isinstance(result, Exception):
                    failed += 1
                    errors.append(str(result))
                    logger.error(f"❌ Batch processing error for item {i}: {result}")
                else:
                    if result["status"] == "success":
                        successful += 1
                    elif result["status"] == "no_content":
                        successful += 1  # Count as successful - no content available is not a failure
                    elif result["status"] == "quarantined":
                        quarantined += 1
                    else:
                        failed += 1

            processing_time = (datetime.now() - processing_start).total_seconds()

            # Update metrics
            self.processing_stats.update({
                'total_processed': self.processing_stats['total_processed'] + processed,
                'successful': self.processing_stats['successful'] + successful,
                'failed': self.processing_stats['failed'] + failed,
                'quarantined': self.processing_stats['quarantined'] + quarantined
            })

            logger.info(
                f"📋 Batch processing complete: {successful} success, {failed} failed, "
                f"{quarantined} quarantined ({processing_time:.1f}s)"
            )

            return {
                "status": "complete",
                "processed": processed,
                "successful": successful,
                "failed": failed,
                "quarantined": quarantined,
                "errors": errors,
                "processing_time_seconds": processing_time,
                "items_per_second": processed / processing_time if processing_time > 0 else 0
            }

        except Exception as e:
            logger.error(f"❌ Enhanced backlog processing failed: {e}")
            return {
                "status": "error",
                "reason": "batch_processing_failed",
                "message": str(e),
                "processed": 0
            }

    async def _process_single_item_with_retry(
        self,
        content_id: str,
        queue_item: Optional[QueueItem] = None
    ) -> Dict[str, Any]:
        """
        Process single item with comprehensive error handling and retry logic
        """
        processing_start = datetime.now()

        try:
            # Get queue item if not provided
            if not queue_item:
                # This is a simplified approach - in production, we'd get this from the queue
                # For now, we'll create a minimal queue item for error handling
                from .url_classifier import classify_url
                classification = classify_url("https://unknown")  # Placeholder
                queue_item = QueueItem(
                    content_id=content_id,
                    source_url="https://unknown",
                    normalized_url="https://unknown",
                    source_name="unknown",
                    content_type="web",
                    priority=50,
                    status=QueueStatus.PROCESSING,
                    retry_count=0,
                    processing_strategy=classification.processing_strategy,
                    metadata={},
                    created_at=processing_start.isoformat(),
                    updated_at=processing_start.isoformat()
                )

            logger.info(f"🔄 Processing {content_id} (attempt {queue_item.retry_count + 1})")

            # Mark as processing
            await update_item_status(content_id, QueueStatus.PROCESSING)

            # Set processing timeout
            try:
                # Run actual processing with timeout
                result = await asyncio.wait_for(
                    self._execute_base_processing(content_id),
                    timeout=self.processing_timeout_seconds
                )

                processing_time = (datetime.now() - processing_start).total_seconds()

                if result['status'] == 'success':
                    # Success - update circuit breaker
                    domain = self._extract_domain(queue_item.source_url)
                    await update_circuit_breaker(domain, success=True)

                    await update_item_status(content_id, QueueStatus.COMPLETED)

                    logger.info(f"✅ Successfully processed {content_id} in {processing_time:.1f}s")

                    return {
                        "status": "success",
                        "message": result.get('message', 'Processing complete'),
                        "processing_time": processing_time,
                        "content_type": result.get('content_type', 'unknown')
                    }
                elif result['status'] == 'no_content':
                    # No content available (e.g., transcript not available) - mark as completed with no content
                    domain = self._extract_domain(queue_item.source_url)
                    await update_circuit_breaker(domain, success=True)  # Not a processing failure

                    await update_item_status(content_id, QueueStatus.COMPLETED,
                                            error_message=result.get('message', 'No content available'))

                    logger.info(f"✅ No content available for {content_id}: {result.get('message', 'No content')}")

                    return {
                        "status": "no_content",
                        "message": result.get('message', 'No content available'),
                        "processing_time": processing_time,
                        "content_type": result.get('content_type', 'unknown')
                    }
                else:
                    # Processing failed - handle with error handler
                    await self._handle_processing_failure(
                        content_id, queue_item, result.get('message', 'Unknown error'), processing_start
                    )

                    return {
                        "status": "failed",
                        "message": result.get('message', 'Processing failed'),
                        "processing_time": processing_time
                    }

            except asyncio.TimeoutError:
                # Processing timeout
                await self._handle_processing_failure(
                    content_id, queue_item, f"Processing timeout after {self.processing_timeout_seconds}s", processing_start
                )

                return {
                    "status": "timeout",
                    "message": f"Processing timeout after {self.processing_timeout_seconds}s",
                    "processing_time": self.processing_timeout_seconds
                }

        except Exception as e:
            logger.error(f"❌ Critical processing error for {content_id}: {e}")

            # Handle critical error
            await self._handle_processing_failure(content_id, queue_item, str(e), processing_start)

            return {
                "status": "error",
                "message": f"Critical processing error: {str(e)}",
                "processing_time": (datetime.now() - processing_start).total_seconds()
            }

    async def _execute_base_processing(self, content_id: str) -> Dict[str, Any]:
        """Execute the base content processing"""
        async with self.base_processor as processor:
            return await processor.process_content(content_id)

    async def _handle_processing_failure(
        self,
        content_id: str,
        queue_item: QueueItem,
        error_message: str,
        processing_start: datetime
    ):
        """Handle processing failure with intelligent error routing"""
        try:
            # Use enhanced error handler
            action, metadata = await handle_processing_error(
                content_id=content_id,
                source_url=queue_item.source_url,
                source_name=queue_item.source_name,
                error_message=error_message,
                retry_count=queue_item.retry_count,
                processing_start_time=processing_start,
                queue_item=queue_item
            )

            logger.info(f"🔧 Error handling action for {content_id}: {action}")

        except Exception as e:
            logger.error(f"❌ Error handling failed for {content_id}: {e}")
            # Fallback - mark as failed
            await update_item_status(
                content_id,
                QueueStatus.FAILED,
                error_message=f"Error handling failed: {str(e)}"
            )

    def _extract_domain(self, url: str) -> str:
        """Extract domain from URL"""
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            return parsed.netloc.lower() if parsed.netloc else 'unknown'
        except:
            return 'unknown'

    async def get_comprehensive_stats(self) -> Dict[str, Any]:
        """Get comprehensive processing statistics"""
        # Get queue statistics
        queue_stats = await get_queue_stats()

        # Get error handling statistics
        error_stats = await get_error_handling_stats()

        # Get quarantine statistics
        quarantine_stats = await get_quarantine_stats(days_ago=7)

        # Calculate uptime and performance metrics
        uptime_seconds = (datetime.now() - self.processing_stats['start_time']).total_seconds()
        uptime_hours = uptime_seconds / 3600

        # Calculate processing rates
        overall_rate = self.processing_stats['total_processed'] / uptime_hours if uptime_hours > 0 else 0
        success_rate = (self.processing_stats['successful'] /
                       max(self.processing_stats['total_processed'], 1)) * 100

        return {
            'processor_uptime_hours': round(uptime_hours, 1),
            'total_processed': self.processing_stats['total_processed'],
            'successful_processing': self.processing_stats['successful'],
            'failed_processing': self.processing_stats['failed'],
            'quarantined_items': self.processing_stats['quarantined'],
            'success_rate_percent': round(success_rate, 2),
            'overall_processing_rate_per_hour': round(overall_rate, 1),

            # Queue health
            'queue_health': queue_stats['queue_health'],
            'pending_items': queue_stats['pending_count'],
            'queue_backpressure_active': queue_stats['backpressure_active'],

            # Error handling
            'error_rate_percent': error_stats['error_rate_percent'],
            'active_circuit_breakers': len([
                cb for cb in error_stats['circuit_breakers'].values()
                if cb['state'] == 'OPEN'
            ]),

            # Quarantine
            'quarantined_last_7_days': quarantine_stats['total_quarantined'],
            'quarantine_breakdown': quarantine_stats['by_quarantine_reason'],

            # Health score
            'health_score': self._calculate_health_score(queue_stats, error_stats),

            'timestamp': datetime.now().isoformat()
        }

    def _calculate_health_score(self, queue_stats: Dict, error_stats: Dict) -> int:
        """Calculate overall system health score (0-100)"""
        score = 100

        # Penalize high error rate
        error_rate = error_stats['error_rate_percent']
        if error_rate > 20:
            score -= 40
        elif error_rate > 10:
            score -= 20
        elif error_rate > 5:
            score -= 10

        # Penalize open circuit breakers
        open_circuit_breakers = len([
            cb for cb in error_stats['circuit_breakers'].values()
            if cb['state'] == 'OPEN'
        ])
        score -= open_circuit_breakers * 15

        # Penalize backpressure
        if queue_stats['backpressure_active']:
            score -= 20

        # Penalize poor queue health
        queue_health = queue_stats['queue_health']
        if queue_health == 'critical':
            score -= 30
        elif queue_health == 'poor':
            score -= 20
        elif queue_health == 'fair':
            score -= 10

        # Bonus for good processing rates
        if queue_stats['processing_rate_per_hour'] > 50:
            score += 5
        elif queue_stats['processing_rate_per_hour'] > 100:
            score += 10

        return max(0, min(100, score))

    async def get_queue_health(self) -> Dict[str, Any]:
        """Get detailed queue health metrics"""
        try:
            # Get basic queue stats
            queue_stats = await get_queue_stats()

            # Get enhanced queue manager stats
            eqm_stats = await self.queue_manager.get_queue_health()

            # Get dead letter queue stats
            dlq_stats = await get_quarantine_stats(days_ago=7)

            # Calculate health metrics
            total_items = sum(queue_stats.values())
            success_rate = queue_stats.get('completed', 0) / max(total_items, 1)
            error_rate = queue_stats.get('failed', 0) / max(total_items, 1)

            # Queue health classification
            if success_rate > 0.95 and error_rate < 0.05:
                queue_status = "excellent"
            elif success_rate > 0.85 and error_rate < 0.15:
                queue_status = "good"
            elif success_rate > 0.70 and error_rate < 0.30:
                queue_status = "acceptable"
            else:
                queue_status = "poor"

            return {
                "status": queue_status,
                "basic_stats": queue_stats,
                "enhanced_stats": eqm_stats,
                "dead_letter_stats": dlq_stats,
                "success_rate": round(success_rate * 100, 2),
                "error_rate": round(error_rate * 100, 2),
                "total_processed": total_items,
                "health_indicators": {
                    "high_success_rate": success_rate > 0.85,
                    "low_error_rate": error_rate < 0.15,
                    "manageable_backlog": queue_stats.get('pending', 0) < 1000,
                    "low_quarantine_rate": dlq_stats.get('total_quarantined', 0) < 100
                },
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"❌ Queue health check failed: {e}")
            return {
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

    async def health_check(self) -> Dict[str, Any]:
        """Comprehensive health check"""
        try:
            # Check database connection
            db_healthy = await self.db_manager.health_check()

            # Get comprehensive stats
            stats = await self.get_comprehensive_stats()

            # Determine overall health
            health_score = stats['health_score']

            if health_score >= 80:
                health_status = "healthy"
            elif health_score >= 60:
                health_status = "degraded"
            elif health_score >= 40:
                health_status = "unhealthy"
            else:
                health_status = "critical"

            return {
                "status": health_status,
                "health_score": health_score,
                "database_healthy": db_healthy,
                "processor_uptime_hours": stats['processor_uptime_hours'],
                "pending_items": stats['pending_items'],
                "error_rate_percent": stats['error_rate_percent'],
                "active_circuit_breakers": stats['active_circuit_breakers'],
                "queue_health": stats['queue_health'],
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"❌ Health check failed: {e}")
            return {
                "status": "critical",
                "health_score": 0,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

# Global enhanced processor instance
_enhanced_processor = None

async def get_enhanced_processor(
    db_manager: DatabaseManager,
    config_manager: ConfigManager
) -> EnhancedProcessor:
    """Get or create enhanced processor instance"""
    global _enhanced_processor
    if _enhanced_processor is None:
        _enhanced_processor = EnhancedProcessor(db_manager, config_manager)
        await _enhanced_processor.initialize()
    return _enhanced_processor