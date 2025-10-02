"""
Intelligent Monitoring and Auto-Fix System for Atlas

Features:
- Real-time health monitoring with AI-powered auto-fix
- Harmonized alerting - only alerts for critical failures
- Automatic recovery using OpenRouter API
- Self-healing capabilities for common issues
- Minimal noise - only when system truly fails
"""

import asyncio
import logging
import os
import json
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import aiohttp
import subprocess
from pathlib import Path

from .database import DatabaseManager
from .config_manager import ConfigManager

logger = logging.getLogger(__name__)

class IntelligentMonitor:
    """
    AI-powered monitoring system with auto-fix capabilities
    Only alerts when system is truly stopped and cannot recover
    """

    def __init__(self, db_manager: DatabaseManager, config_manager: ConfigManager):
        self.db_manager = db_manager
        self.config_manager = config_manager
        self.openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

        # Monitoring configuration
        self.health_check_interval = 60  # seconds
        self.auto_fix_attempts = 3
        self.critical_failure_threshold = 3  # consecutive failures

        # State tracking
        self.consecutive_failures = 0
        self.last_successful_check = None
        self.last_auto_fix = None
        self.is_auto_fixing = False

        # Performance metrics
        self.metrics = {
            'total_checks': 0,
            'successful_checks': 0,
            'auto_fixes_attempted': 0,
            'auto_fixes_successful': 0,
            'alerts_sent': 0,
            'start_time': datetime.now()
        }

    async def initialize(self):
        """Initialize the intelligent monitor"""
        logger.info("🤖 Initializing Intelligent Monitor with AI auto-fix...")

        if not self.openrouter_api_key:
            logger.warning("⚠️ OPENROUTER_API_KEY not found - auto-fix disabled")
            return

        logger.info("✅ Intelligent Monitor initialized with AI auto-fix capabilities")

    async def health_check_with_auto_fix(self) -> Dict[str, Any]:
        """
        Comprehensive health check with automatic recovery
        Only alerts when system is truly stopped and cannot recover
        """
        self.metrics['total_checks'] += 1

        try:
            # Check database health
            db_healthy = await self.db_manager.health_check()

            # Check processing activity
            processing_active = await self._check_processing_activity()

            # Check queue health
            queue_healthy = await self._check_queue_health()

            # Check service processes
            services_running = await self._check_service_processes()

            # Overall health determination
            overall_healthy = db_healthy and processing_active and queue_healthy and services_running

            if overall_healthy:
                self.consecutive_failures = 0
                self.last_successful_check = datetime.now()
                self.metrics['successful_checks'] += 1

                return {
                    "status": "healthy",
                    "message": "All systems operational",
                    "timestamp": datetime.now().isoformat(),
                    "auto_fix_enabled": bool(self.openrouter_api_key)
                }
            else:
                self.consecutive_failures += 1
                logger.warning(f"⚠️ Health check failed ({self.consecutive_failures}/{self.critical_failure_threshold})")

                # Attempt auto-fix if we have AI capabilities and threshold reached
                if (self.openrouter_api_key and
                    self.consecutive_failures >= self.critical_failure_threshold and
                    not self.is_auto_fixing):

                    return await self._attempt_auto_fix({
                        "database_healthy": db_healthy,
                        "processing_active": processing_active,
                        "queue_healthy": queue_healthy,
                        "services_running": services_running
                    })

                # If no auto-fix or still in progress, return degraded status
                return {
                    "status": "degraded" if self.consecutive_failures < self.critical_failure_threshold else "critical",
                    "message": f"System issues detected (consecutive failures: {self.consecutive_failures})",
                    "timestamp": datetime.now().isoformat(),
                    "auto_fix_enabled": bool(self.openrouter_api_key),
                    "auto_fix_in_progress": self.is_auto_fixing
                }

        except Exception as e:
            self.consecutive_failures += 1
            logger.error(f"❌ Health check error: {e}")

            # Attempt auto-fix for critical errors
            if (self.openrouter_api_key and
                self.consecutive_failures >= self.critical_failure_threshold and
                not self.is_auto_fixing):

                return await self._attempt_auto_fix({
                    "error": str(e),
                    "error_type": "health_check_exception"
                })

            return {
                "status": "critical",
                "message": f"Health check failed: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "auto_fix_enabled": bool(self.openrouter_api_key)
            }

    async def _check_processing_activity(self) -> bool:
        """Check if processing is actively happening"""
        try:
            # Get recent processing activity
            recent_activity = await self.db_manager.get_processing_stats(hours=1)

            # Check if there's been any successful processing in the last hour
            if recent_activity.get('successful_processing', 0) > 0:
                return True

            # Check if there are items in queue that should be processed
            queue_size = await self.db_manager.get_queue_size()
            if queue_size > 0:
                # Queue has items but no recent processing - potential issue
                logger.warning(f"⚠️ Queue has {queue_size} items but no recent processing activity")
                return False

            return True  # No queue items is considered healthy

        except Exception as e:
            logger.error(f"❌ Processing activity check failed: {e}")
            return False

    async def _check_queue_health(self) -> bool:
        """Check processing queue health"""
        try:
            stats = await self.db_manager.get_queue_stats()

            # Check for queue congestion
            if stats.get('queue_size', 0) > 1000:
                logger.warning(f"⚠️ Large queue size: {stats['queue_size']}")

            # Check for high failure rate
            failure_rate = stats.get('failure_rate', 0)
            if failure_rate > 50:  # More than 50% failure rate
                logger.warning(f"⚠️ High failure rate: {failure_rate}%")
                return False

            return True

        except Exception as e:
            logger.error(f"❌ Queue health check failed: {e}")
            return False

    async def _check_service_processes(self) -> bool:
        """Check if required service processes are running"""
        try:
            # Check if main Atlas process is running
            result = subprocess.run(['pgrep', '-f', 'python.*main.py'],
                                  capture_output=True, text=True)
            atlas_running = bool(result.stdout.strip())

            if not atlas_running:
                logger.warning("⚠️ Atlas main process not found running")

            return atlas_running

        except Exception as e:
            logger.error(f"❌ Service process check failed: {e}")
            return False

    async def _attempt_auto_fix(self, diagnostic_data: Dict[str, Any]) -> Dict[str, Any]:
        """Attempt to fix issues using AI-powered auto-fix"""
        if self.is_auto_fixing:
            return {
                "status": "critical",
                "message": "Auto-fix already in progress",
                "timestamp": datetime.now().isoformat()
            }

        self.is_auto_fixing = True
        self.metrics['auto_fixes_attempted'] += 1
        self.last_auto_fix = datetime.now()

        try:
            logger.warning("🤖 Starting AI-powered auto-fix...")

            # Create AI prompt for diagnosis and fix
            prompt = self._create_auto_fix_prompt(diagnostic_data)

            # Get AI recommendations
            fix_recommendations = await self._get_ai_fix_recommendations(prompt)

            # Execute the recommended fixes
            fix_results = await self._execute_fix_recommendations(fix_recommendations)

            if fix_results['success']:
                self.consecutive_failures = 0  # Reset on successful fix
                self.metrics['auto_fixes_successful'] += 1

                logger.info("✅ AI-powered auto-fix successful!")

                return {
                    "status": "recovered",
                    "message": "AI auto-fix successfully resolved issues",
                    "fix_applied": fix_results['fixes_applied'],
                    "timestamp": datetime.now().isoformat(),
                    "auto_fix_duration": (datetime.now() - self.last_auto_fix).total_seconds()
                }
            else:
                logger.error(f"❌ AI auto-fix failed: {fix_results['error']}")

                # Send critical alert if auto-fix fails
                await self._send_critical_alert(f"Auto-fix failed: {fix_results['error']}")

                return {
                    "status": "critical",
                    "message": f"Auto-fix failed: {fix_results['error']}",
                    "fix_attempted": fix_results['fixes_attempted'],
                    "timestamp": datetime.now().isoformat()
                }

        except Exception as e:
            logger.error(f"❌ Auto-fix attempt failed: {e}")
            await self._send_critical_alert(f"Auto-fix system error: {str(e)}")

            return {
                "status": "critical",
                "message": f"Auto-fix system error: {str(e)}",
                "timestamp": datetime.now().isoformat()
            }
        finally:
            self.is_auto_fixing = False

    def _create_auto_fix_prompt(self, diagnostic_data: Dict[str, Any]) -> str:
        """Create prompt for AI auto-fix recommendations"""
        system_info = {
            "timestamp": datetime.now().isoformat(),
            "consecutive_failures": self.consecutive_failures,
            "last_successful_check": self.last_successful_check.isoformat() if self.last_successful_check else None,
            "auto_fix_attempts": self.metrics['auto_fixes_attempted'],
            "diagnostic_data": diagnostic_data
        }

        return f"""
You are an expert system administrator for Atlas, an event-driven content pipeline.

CURRENT SYSTEM STATUS:
{json.dumps(system_info, indent=2)}

YOUR TASK:
1. Analyze the diagnostic data to identify the root cause
2. Recommend specific, executable fixes to resolve the issues
3. Provide the exact shell commands or actions needed
4. Focus on the most likely and impactful fixes first

RESPONSE FORMAT:
Return a JSON object with:
{{
    "analysis": "Brief analysis of the root cause",
    "fixes": [
        {{
            "description": "What this fix does",
            "command": "Exact shell command to execute",
            "priority": "high|medium|low",
            "risk": "low|medium|high"
        }}
    ],
    "verification": "How to verify the fix worked"
}}

IMPORTANT:
- Only recommend fixes that are safe to execute automatically
- Prioritize fixes that restore system functionality
- Include service restarts, process cleanup, queue management
- Be conservative - prefer minimal interventions
"""

    async def _get_ai_fix_recommendations(self, prompt: str) -> Dict[str, Any]:
        """Get AI recommendations for fixing system issues"""
        if not self.openrouter_api_key:
            raise Exception("OpenRouter API key not available")

        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.openrouter_api_key}",
                    "HTTP-Referer": "https://atlas-system.com",
                    "X-Title": "Atlas Auto-Fix System"
                }

                payload = {
                    "model": "anthropic/claude-3.5-sonnet",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "response_format": {"type": "json_object"}
                }

                async with session.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:

                    if response.status == 200:
                        data = await response.json()
                        content = data['choices'][0]['message']['content']
                        return json.loads(content)
                    else:
                        error_text = await response.text()
                        raise Exception(f"OpenRouter API error: {response.status} - {error_text}")

        except Exception as e:
            logger.error(f"❌ AI fix recommendation failed: {e}")
            raise

    async def _execute_fix_recommendations(self, recommendations: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the AI-recommended fixes"""
        fixes_applied = []
        fixes_attempted = []

        try:
            # Sort fixes by priority
            fixes = sorted(recommendations.get('fixes', []),
                         key=lambda x: {'high': 0, 'medium': 1, 'low': 2}[x.get('priority', 'medium')])

            for fix in fixes:
                if fix.get('risk', 'medium') == 'high':
                    logger.warning(f"⚠️ Skipping high-risk fix: {fix['description']}")
                    continue

                logger.info(f"🔧 Applying fix: {fix['description']}")
                fixes_attempted.append(fix['description'])

                try:
                    # Execute the fix command
                    result = subprocess.run(
                        fix['command'],
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=300
                    )

                    if result.returncode == 0:
                        fixes_applied.append(fix['description'])
                        logger.info(f"✅ Fix applied successfully: {fix['description']}")
                    else:
                        logger.error(f"❌ Fix failed: {fix['description']} - {result.stderr}")

                except subprocess.TimeoutExpired:
                    logger.error(f"❌ Fix timeout: {fix['description']}")
                except Exception as e:
                    logger.error(f"❌ Fix execution error: {fix['description']} - {e}")

            # Verify the fixes worked
            verification_result = await self._verify_fixes(recommendations.get('verification', ''))

            return {
                "success": verification_result and len(fixes_applied) > 0,
                "fixes_applied": fixes_applied,
                "fixes_attempted": fixes_attempted,
                "verification_result": verification_result
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "fixes_attempted": fixes_attempted
            }

    async def _verify_fixes(self, verification_method: str) -> bool:
        """Verify that the applied fixes worked"""
        try:
            # Simple verification - run a quick health check
            db_healthy = await self.db_manager.health_check()
            processing_active = await self._check_processing_activity()

            return db_healthy and processing_active

        except Exception as e:
            logger.error(f"❌ Fix verification failed: {e}")
            return False

    async def _send_critical_alert(self, message: str):
        """Send critical alert when system cannot recover"""
        self.metrics['alerts_sent'] += 1

        logger.critical(f"🚨 CRITICAL ALERT: {message}")

        # Here you could integrate with your preferred alerting system
        # (email, Slack, Telegram, etc.)

        # For now, log to file for external monitoring
        alert_file = Path("logs/critical_alerts.log")
        alert_file.parent.mkdir(exist_ok=True)

        with open(alert_file, 'a') as f:
            f.write(f"{datetime.now().isoformat()} - CRITICAL: {message}\n")

    def get_monitoring_stats(self) -> Dict[str, Any]:
        """Get comprehensive monitoring statistics"""
        uptime = (datetime.now() - self.metrics['start_time']).total_seconds()
        uptime_hours = uptime / 3600

        success_rate = (self.metrics['successful_checks'] /
                       max(self.metrics['total_checks'], 1)) * 100

        auto_fix_success_rate = (self.metrics['auto_fixes_successful'] /
                               max(self.metrics['auto_fixes_attempted'], 1)) * 100

        return {
            "uptime_hours": round(uptime_hours, 1),
            "total_health_checks": self.metrics['total_checks'],
            "successful_health_checks": self.metrics['successful_checks'],
            "health_check_success_rate": round(success_rate, 2),
            "auto_fixes_attempted": self.metrics['auto_fixes_attempted'],
            "auto_fixes_successful": self.metrics['auto_fixes_successful'],
            "auto_fix_success_rate": round(auto_fix_success_rate, 2),
            "alerts_sent": self.metrics['alerts_sent'],
            "consecutive_failures": self.consecutive_failures,
            "last_successful_check": self.last_successful_check.isoformat() if self.last_successful_check else None,
            "last_auto_fix": self.last_auto_fix.isoformat() if self.last_auto_fix else None,
            "auto_fix_in_progress": self.is_auto_fixing,
            "auto_fix_enabled": bool(self.openrouter_api_key)
        }

# Global monitor instance
_monitor = None

async def get_intelligent_monitor(
    db_manager: DatabaseManager,
    config_manager: ConfigManager
) -> IntelligentMonitor:
    """Get or create intelligent monitor instance"""
    global _monitor
    if _monitor is None:
        _monitor = IntelligentMonitor(db_manager, config_manager)
        await _monitor.initialize()
    return _monitor