"""
Production-Grade Error Handler for Atlas v2

Integrates enhanced queue management, dead letter queue, and intelligent
retry logic to eliminate queue pollution and handle high-volume inputs reliably.

Key Features:
- Circuit breaker pattern for cascading failure prevention
- Exponential backoff with jitter for retry timing
- Dead letter queue integration for non-processable URLs
- Comprehensive error classification and routing
- Production monitoring and alerting integration
"""

import asyncio
import logging
import random
import time
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass

from .enhanced_queue_manager import (
    EnhancedQueueManager,
    QueueStatus,
    QueueItem,
    get_queue_stats,
    update_item_status
)
from .dead_letter_queue import (
    quarantine_item,
    get_quarantine_stats,
    FailureType,
    QuarantineReason
)
from .url_classifier import classify_url, URLClassification

logger = logging.getLogger(__name__)

class ErrorSeverity(Enum):
    LOW = "low"           # Temporary issues, worth retrying
    MEDIUM = "medium"     # May succeed with different approach
    HIGH = "high"         # Unlikely to succeed, consider quarantining
    CRITICAL = "critical" # Will never succeed, immediate quarantine

@dataclass
class ErrorContext:
    """Context for error handling decisions"""
    content_id: str
    source_url: str
    source_name: str
    error_message: str
    retry_count: int
    processing_duration: float
    classification: URLClassification
    queue_item: QueueItem

class CircuitBreaker:
    """Circuit breaker to prevent cascading failures"""

    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN

    async def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
                logger.info("🔄 Circuit breaker moving to HALF_OPEN")
            else:
                raise Exception("Circuit breaker is OPEN")

        try:
            result = await func(*args, **kwargs)

            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
                logger.info("✅ Circuit breaker returning to CLOSED")

            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
                logger.error(f"🚨 Circuit breaker OPENED after {self.failure_count} failures")

            raise e

class ProductionErrorHandler:
    """Production-grade error handling with intelligent routing"""

    def __init__(self):
        self.queue_manager = EnhancedQueueManager()
        self.circuit_breakers = {}  # Per-domain circuit breakers
        self.error_patterns = self._initialize_error_patterns()

    def _initialize_error_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Initialize error classification patterns"""
        return {
            # Network errors
            'timeout': {
                'patterns': ['timeout', 'timed out', 'connection timeout'],
                'severity': ErrorSeverity.LOW,
                'base_delay_minutes': 2,
                'max_retries': 5
            },
            'connection_error': {
                'patterns': ['connection refused', 'connection failed', 'network unreachable'],
                'severity': ErrorSeverity.LOW,
                'base_delay_minutes': 1,
                'max_retries': 5
            },
            'dns_error': {
                'patterns': ['dns', 'name resolution', 'host not found'],
                'severity': ErrorSeverity.HIGH,
                'base_delay_minutes': 10,
                'max_retries': 3
            },

            # HTTP errors
            'rate_limit': {
                'patterns': ['rate limit', '429', 'too many requests'],
                'severity': ErrorSeverity.MEDIUM,
                'base_delay_minutes': 30,
                'max_retries': 3
            },
            'not_found': {
                'patterns': ['404', 'not found', 'no such resource'],
                'severity': ErrorSeverity.CRITICAL,
                'base_delay_minutes': 0,
                'max_retries': 0
            },
            'server_error': {
                'patterns': ['500', '502', '503', '504', 'internal server error'],
                'severity': ErrorSeverity.MEDIUM,
                'base_delay_minutes': 5,
                'max_retries': 4
            },

            # Content errors
            'paywall': {
                'patterns': ['paywall', 'subscription', 'premium content'],
                'severity': ErrorSeverity.HIGH,
                'base_delay_minutes': 0,
                'max_retries': 0
            },
            'blocked_content': {
                'patterns': ['blocked', 'forbidden', 'access denied'],
                'severity': ErrorSeverity.HIGH,
                'base_delay_minutes': 0,
                'max_retries': 1
            },

            # System errors
            'memory_error': {
                'patterns': ['memory', 'out of memory'],
                'severity': ErrorSeverity.MEDIUM,
                'base_delay_minutes': 5,
                'max_retries': 3
            },
            'disk_space': {
                'patterns': ['disk space', 'no space left'],
                'severity': ErrorSeverity.CRITICAL,
                'base_delay_minutes': 0,
                'max_retries': 0
            }
        }

    async def handle_processing_error(
        self,
        context: ErrorContext,
        processing_start_time: datetime
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Handle processing error with intelligent routing

        Returns:
            (action, metadata) where action is one of:
            - 'retry': Schedule for retry with backoff
            - 'quarantine': Move to dead letter queue
            - 'fail': Mark as permanently failed
        """
        processing_duration = (datetime.now() - processing_start_time).total_seconds()

        # Classify the error
        error_type, severity = self._classify_error(context.error_message)

        # Check if this URL is processable at all
        if not context.classification.is_processable:
            return await self._quarantine_immediately(
                context,
                f"Non-processable URL: {context.classification.failure_reason}"
            )

        # Check circuit breaker status
        domain = self._extract_domain(context.source_url)
        if await self._is_circuit_breaker_open(domain):
            return await self._schedule_circuit_breaker_retry(context)

        # Determine action based on error classification and retry count
        if severity == ErrorSeverity.CRITICAL:
            return await self._quarantine_immediately(context, f"Critical error: {error_type}")

        elif severity == ErrorSeverity.HIGH:
            if context.retry_count >= 2:
                return await self._quarantine_immediately(
                    context,
                    f"High severity error after {context.retry_count} retries: {error_type}"
                )
            else:
                return await self._schedule_retry(context, error_type, severity)

        elif severity == ErrorSeverity.MEDIUM:
            if context.retry_count >= self.error_patterns[error_type]['max_retries']:
                return await self._quarantine_immediately(
                    context,
                    f"Max retries exceeded for {error_type}"
                )
            else:
                return await self._schedule_retry(context, error_type, severity)

        else:  # LOW severity
            return await self._schedule_retry(context, error_type, severity)

    def _classify_error(self, error_message: str) -> Tuple[str, ErrorSeverity]:
        """Classify error type and severity"""
        error_lower = error_message.lower()

        for error_type, config in self.error_patterns.items():
            for pattern in config['patterns']:
                if pattern in error_lower:
                    return error_type, config['severity']

        # Default classification for unknown errors
        if any(keyword in error_lower for keyword in ['timeout', 'connection']):
            return 'unknown_network', ErrorSeverity.LOW
        elif any(keyword in error_lower for keyword in ['500', '502', '503']):
            return 'unknown_server', ErrorSeverity.MEDIUM
        else:
            return 'unknown', ErrorSeverity.MEDIUM

    async def _schedule_retry(
        self,
        context: ErrorContext,
        error_type: str,
        severity: ErrorSeverity
    ) -> Tuple[str, Dict[str, Any]]:
        """Schedule retry with exponential backoff and jitter"""
        config = self.error_patterns.get(error_type, {
            'base_delay_minutes': 5,
            'max_retries': 3
        })

        # Calculate delay with exponential backoff
        base_delay = config['base_delay_minutes']
        exponential_delay = base_delay * (2 ** context.retry_count)

        # Add jitter to prevent thundering herd
        jitter = random.uniform(0.5, 1.5)
        delay_minutes = int(exponential_delay * jitter)

        # Cap at reasonable maximum
        delay_minutes = min(delay_minutes, 60)  # Max 1 hour

        # Schedule retry
        retry_at = datetime.now() + timedelta(minutes=delay_minutes)
        await update_item_status(
            context.content_id,
            QueueStatus.RETRY,
            error_message=context.error_message,
            retry_delay_minutes=delay_minutes
        )

        logger.info(
            f"🔄 Scheduled retry for {context.content_id} in {delay_minutes} minutes "
            f"(attempt {context.retry_count + 1}, error: {error_type})"
        )

        return 'retry', {
            'retry_at': retry_at.isoformat(),
            'delay_minutes': delay_minutes,
            'error_type': error_type,
            'severity': severity.value
        }

    async def _quarantine_immediately(
        self,
        context: ErrorContext,
        reason: str
    ) -> Tuple[str, Dict[str, Any]]:
        """Immediately quarantine item in dead letter queue"""
        success = await quarantine_item(
            content_id=context.content_id,
            source_url=context.source_url,
            source_name=context.source_name,
            original_error=context.error_message,
            classification=context.classification,
            retry_count=context.retry_count,
            notes=reason
        )

        if success:
            # Remove from processing queue
            await update_item_status(
                context.content_id,
                QueueStatus.QUARANTINED,
                error_message=reason
            )

            # Update circuit breaker if this is a domain-specific issue
            domain = self._extract_domain(context.source_url)
            await self._update_circuit_breaker(domain, failure=True)

            logger.warning(f"🚫 Quarantined {context.content_id}: {reason}")

            return 'quarantine', {
                'quarantine_reason': reason,
                'error_type': self._classify_error(context.error_message)[0],
                'timestamp': datetime.now().isoformat()
            }
        else:
            logger.error(f"❌ Failed to quarantine {context.content_id}")
            return 'fail', {'error': 'Quarantine failed'}

    async def _schedule_circuit_breaker_retry(
        self,
        context: ErrorContext
    ) -> Tuple[str, Dict[str, Any]]:
        """Schedule retry when circuit breaker is open"""
        # Circuit breaker retries have longer delays
        delay_minutes = random.randint(30, 60)
        retry_at = datetime.now() + timedelta(minutes=delay_minutes)

        await update_item_status(
            context.content_id,
            QueueStatus.RETRY,
            error_message=f"Circuit breaker open for domain, retrying in {delay_minutes} minutes",
            retry_delay_minutes=delay_minutes
        )

        return 'retry', {
            'retry_at': retry_at.isoformat(),
            'delay_minutes': delay_minutes,
            'reason': 'circuit_breaker_open'
        }

    def _extract_domain(self, url: str) -> str:
        """Extract domain from URL for circuit breaker grouping"""
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            return parsed.netloc.lower() if parsed.netloc else 'unknown'
        except:
            return 'unknown'

    async def _is_circuit_breaker_open(self, domain: str) -> bool:
        """Check if circuit breaker is open for domain"""
        if domain not in self.circuit_breakers:
            self.circuit_breakers[domain] = CircuitBreaker()

        return self.circuit_breakers[domain].state == "OPEN"

    async def _update_circuit_breaker(self, domain: str, failure: bool):
        """Update circuit breaker state"""
        if domain not in self.circuit_breakers:
            self.circuit_breakers[domain] = CircuitBreaker()

        breaker = self.circuit_breakers[domain]

        if failure:
            breaker.failure_count += 1
            breaker.last_failure_time = time.time()

            if breaker.failure_count >= breaker.failure_threshold:
                breaker.state = "OPEN"
                logger.error(f"🚨 Circuit breaker OPENED for domain: {domain}")
        else:
            # Success - reset circuit breaker
            if breaker.state == "HALF_OPEN":
                breaker.state = "CLOSED"
                breaker.failure_count = 0
                logger.info(f"✅ Circuit breaker CLOSED for domain: {domain}")

    async def get_error_handling_stats(self) -> Dict[str, Any]:
        """Get comprehensive error handling statistics"""
        # Get queue stats
        queue_stats = await get_queue_stats()

        # Get quarantine stats
        quarantine_stats = await get_quarantine_stats(days_ago=7)

        # Get circuit breaker status
        circuit_breaker_status = {
            domain: {
                'state': breaker.state,
                'failure_count': breaker.failure_count,
                'last_failure': breaker.last_failure_time
            }
            for domain, breaker in self.circuit_breakers.items()
        }

        # Calculate error rates
        total_processed = queue_stats['status_counts'].get('completed', 0)
        total_failed = queue_stats['status_counts'].get('failed', 0)
        total_quarantined = quarantine_stats['total_quarantined']

        error_rate = 0
        if total_processed + total_failed + total_quarantined > 0:
            error_rate = ((total_failed + total_quarantined) /
                        (total_processed + total_failed + total_quarantined)) * 100

        return {
            'queue_health': queue_stats['queue_health'],
            'error_rate_percent': round(error_rate, 2),
            'pending_count': queue_stats['pending_count'],
            'processing_rate_per_hour': queue_stats['processing_rate_per_hour'],
            'quarantined_items': total_quarantined,
            'circuit_breakers': circuit_breaker_status,
            'backpressure_active': queue_stats['backpressure_active']
        }

# Global error handler instance
_error_handler = ProductionErrorHandler()

async def handle_processing_error(
    content_id: str,
    source_url: str,
    source_name: str,
    error_message: str,
    retry_count: int,
    processing_start_time: datetime,
    queue_item: QueueItem
) -> Tuple[str, Dict[str, Any]]:
    """Handle processing error with intelligent routing"""
    # Classify URL for context
    classification = classify_url(source_url)

    # Create error context
    context = ErrorContext(
        content_id=content_id,
        source_url=source_url,
        source_name=source_name,
        error_message=error_message,
        retry_count=retry_count,
        processing_duration=0,  # Will be calculated in handler
        classification=classification,
        queue_item=queue_item
    )

    return await _error_handler.handle_processing_error(context, processing_start_time)

async def update_circuit_breaker(domain: str, success: bool):
    """Update circuit breaker after processing attempt"""
    await _error_handler._update_circuit_breaker(domain, not success)

async def get_error_handling_stats() -> Dict[str, Any]:
    """Get error handling statistics"""
    return await _error_handler.get_error_handling_stats()