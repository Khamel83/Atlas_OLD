#!/usr/bin/env python3
"""
Alert Manager for Atlas - Phase 3.2
Handles alert notifications and escalation for production monitoring
"""

import json
import smtplib
import os
import sys
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from typing import Dict, List, Optional
import subprocess
import logging
from dataclasses import dataclass

@dataclass
class AlertConfig:
    """Alert configuration for different notification methods"""
    email_enabled: bool = False
    email_smtp_server: str = "smtp.gmail.com"
    email_smtp_port: int = 587
    email_from: str = ""
    email_to: List[str] = None
    email_password: str = ""
    
    webhook_enabled: bool = False
    webhook_url: str = ""
    
    local_notification_enabled: bool = True
    log_alerts: bool = True
    
    def __post_init__(self):
        if self.email_to is None:
            self.email_to = []

class AtlasAlertManager:
    """Manages alerts, notifications, and escalation for Atlas monitoring"""
    
    def __init__(self, base_path="/home/ubuntu/dev/atlas"):
        self.base_path = Path(base_path)
        self.config_file = self.base_path / "config" / "alert_config.json"
        self.alert_log = self.base_path / "logs" / "alerts.log"
        self.state_file = self.base_path / "data" / "alert_state.json"
        
        # Ensure directories exist
        self.config_file.parent.mkdir(exist_ok=True)
        self.alert_log.parent.mkdir(exist_ok=True)
        self.state_file.parent.mkdir(exist_ok=True)
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - AlertManager - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.alert_log),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Load configuration
        self.config = self._load_config()
        
        # Alert state tracking
        self.alert_state = self._load_alert_state()
        
    def _load_config(self) -> AlertConfig:
        """Load alert configuration from file or environment"""
        config = AlertConfig()
        
        try:
            # Try to load from config file first
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    config_data = json.load(f)
                    
                    config.email_enabled = config_data.get('email_enabled', False)
                    config.email_from = config_data.get('email_from', '')
                    config.email_to = config_data.get('email_to', [])
                    config.email_password = config_data.get('email_password', '')
                    config.webhook_enabled = config_data.get('webhook_enabled', False)
                    config.webhook_url = config_data.get('webhook_url', '')
            
            # Override with environment variables if available
            if os.getenv('ATLAS_ALERT_EMAIL'):
                config.email_enabled = True
                config.email_to = [os.getenv('ATLAS_ALERT_EMAIL')]
                
            if os.getenv('ATLAS_ALERT_WEBHOOK'):
                config.webhook_enabled = True
                config.webhook_url = os.getenv('ATLAS_ALERT_WEBHOOK')
                
        except Exception as e:
            self.logger.error(f"Failed to load alert config: {e}")
            
        return config
    
    def _load_alert_state(self) -> Dict:
        """Load persistent alert state"""
        try:
            if self.state_file.exists():
                with open(self.state_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load alert state: {e}")
        
        return {
            'last_alerts': {},
            'alert_counts': {},
            'suppressed_until': {}
        }
    
    def _save_alert_state(self):
        """Save persistent alert state"""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(self.alert_state, f, indent=2)
        except Exception as e:
            self.logger.error(f"Failed to save alert state: {e}")
    
    def process_alert(self, alert: Dict) -> bool:
        """Process a single alert with deduplication and rate limiting"""
        try:
            alert_key = f"{alert['metric_name']}_{alert['severity']}"
            current_time = datetime.now()
            
            # Check if alert is suppressed
            if alert_key in self.alert_state.get('suppressed_until', {}):
                suppress_until = datetime.fromisoformat(self.alert_state['suppressed_until'][alert_key])
                if current_time < suppress_until:
                    self.logger.debug(f"Alert {alert_key} suppressed until {suppress_until}")
                    return False
            
            # Check for recent identical alert (deduplication)
            last_alerts = self.alert_state.get('last_alerts', {})
            if alert_key in last_alerts:
                last_alert_time = datetime.fromisoformat(last_alerts[alert_key])
                if current_time - last_alert_time < timedelta(minutes=5):
                    self.logger.debug(f"Alert {alert_key} deduplicated (too recent)")
                    return False
            
            # Update alert state
            if 'last_alerts' not in self.alert_state:
                self.alert_state['last_alerts'] = {}
            if 'alert_counts' not in self.alert_state:
                self.alert_state['alert_counts'] = {}
                
            self.alert_state['last_alerts'][alert_key] = current_time.isoformat()
            self.alert_state['alert_counts'][alert_key] = self.alert_state['alert_counts'].get(alert_key, 0) + 1
            
            # Send notifications
            self._send_notifications(alert)
            
            # Set suppression period based on severity
            suppression_minutes = 15 if alert['severity'] == 'CRITICAL' else 30
            suppress_until = current_time + timedelta(minutes=suppression_minutes)
            
            if 'suppressed_until' not in self.alert_state:
                self.alert_state['suppressed_until'] = {}
            self.alert_state['suppressed_until'][alert_key] = suppress_until.isoformat()
            
            # Save state
            self._save_alert_state()
            
            self.logger.info(f"Processed alert: {alert['message']}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to process alert: {e}")
            return False
    
    def _send_notifications(self, alert: Dict):
        """Send alert notifications through configured channels"""
        try:
            # Always log the alert
            if self.config.log_alerts:
                self.logger.warning(f"ALERT [{alert['severity']}]: {alert['message']}")
            
            # Local system notification (for desktop environments)
            if self.config.local_notification_enabled:
                self._send_local_notification(alert)
            
            # Email notification
            if self.config.email_enabled and self.config.email_to:
                self._send_email_notification(alert)
            
            # Webhook notification
            if self.config.webhook_enabled and self.config.webhook_url:
                self._send_webhook_notification(alert)
                
        except Exception as e:
            self.logger.error(f"Failed to send notifications: {e}")
    
    def _send_local_notification(self, alert: Dict):
        """Send local system notification"""
        try:
            # Try different notification methods
            notification_commands = [
                ['notify-send', f"Atlas Alert [{alert['severity']}]", alert['message']],
                ['wall', f"Atlas Alert: {alert['message']}"],  # Fallback for server environments
            ]
            
            for cmd in notification_commands:
                try:
                    subprocess.run(cmd, check=False, capture_output=True, timeout=5)
                    break  # Success, stop trying other methods
                except (subprocess.SubprocessError, FileNotFoundError):
                    continue  # Try next method
                    
        except Exception as e:
            self.logger.debug(f"Local notification failed: {e}")
    
    def _send_email_notification(self, alert: Dict):
        """Send email alert notification"""
        try:
            if not self.config.email_from or not self.config.email_to:
                return
            
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = self.config.email_from
            msg['To'] = ', '.join(self.config.email_to)
            msg['Subject'] = f"Atlas Alert [{alert['severity']}]: {alert['metric_name']}"
            
            # Email body
            body = self._format_alert_email(alert)
            msg.attach(MIMEText(body, 'html'))
            
            # Send email
            with smtplib.SMTP(self.config.email_smtp_server, self.config.email_smtp_port) as server:
                server.starttls()
                server.login(self.config.email_from, self.config.email_password)
                server.send_message(msg)
            
            self.logger.info(f"Email alert sent to {len(self.config.email_to)} recipients")
            
        except Exception as e:
            self.logger.error(f"Failed to send email notification: {e}")
    
    def _send_webhook_notification(self, alert: Dict):
        """Send webhook alert notification"""
        try:
            import requests
            
            # Prepare webhook payload
            payload = {
                'timestamp': alert['timestamp'],
                'severity': alert['severity'],
                'metric_name': alert['metric_name'],
                'value': alert['value'],
                'threshold': alert['threshold'],
                'message': alert['message'],
                'source': 'atlas_monitoring'
            }
            
            # Send webhook
            response = requests.post(
                self.config.webhook_url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 200:
                self.logger.info("Webhook alert sent successfully")
            else:
                self.logger.warning(f"Webhook returned status {response.status_code}")
                
        except Exception as e:
            self.logger.error(f"Failed to send webhook notification: {e}")
    
    def _format_alert_email(self, alert: Dict) -> str:
        """Format alert as HTML email"""
        severity_colors = {
            'CRITICAL': '#dc3545',  # Red
            'WARNING': '#ffc107',   # Yellow
            'INFO': '#17a2b8'       # Blue
        }
        
        color = severity_colors.get(alert['severity'], '#6c757d')
        
        html = f"""
        <html>
        <body>
            <h2 style="color: {color};">Atlas Alert - {alert['severity']}</h2>
            
            <table style="border-collapse: collapse; width: 100%;">
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">Metric</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">{alert['metric_name']}</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">Current Value</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">{alert['value']:.2f}</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">Threshold</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">{alert['threshold']:.2f}</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">Time</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">{alert['timestamp']}</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">Message</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">{alert['message']}</td>
                </tr>
            </table>
            
            <p><strong>Atlas Monitoring System</strong><br>
            This alert was automatically generated by the Atlas monitoring system.</p>
        </body>
        </html>
        """
        
        return html
    
    def process_multiple_alerts(self, alerts: List[Dict]) -> int:
        """Process multiple alerts with batching and prioritization"""
        if not alerts:
            return 0
        
        # Sort by severity (CRITICAL first)
        severity_priority = {'CRITICAL': 0, 'WARNING': 1, 'INFO': 2}
        sorted_alerts = sorted(alerts, key=lambda a: severity_priority.get(a['severity'], 3))
        
        processed_count = 0
        for alert in sorted_alerts:
            if self.process_alert(alert):
                processed_count += 1
        
        return processed_count
    
    def get_alert_status(self) -> Dict:
        """Get current alert manager status"""
        try:
            current_time = datetime.now()
            
            # Count active suppressions
            active_suppressions = 0
            if 'suppressed_until' in self.alert_state:
                for suppress_until_str in self.alert_state['suppressed_until'].values():
                    suppress_until = datetime.fromisoformat(suppress_until_str)
                    if current_time < suppress_until:
                        active_suppressions += 1
            
            return {
                'timestamp': current_time.isoformat(),
                'configuration': {
                    'email_enabled': self.config.email_enabled,
                    'webhook_enabled': self.config.webhook_enabled,
                    'local_notification_enabled': self.config.local_notification_enabled,
                    'email_recipients': len(self.config.email_to) if self.config.email_to else 0
                },
                'state': {
                    'total_alerts_sent': sum(self.alert_state.get('alert_counts', {}).values()),
                    'unique_alert_types': len(self.alert_state.get('alert_counts', {})),
                    'active_suppressions': active_suppressions
                }
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def clear_alert_state(self):
        """Clear all alert state (for testing or reset)"""
        try:
            self.alert_state = {
                'last_alerts': {},
                'alert_counts': {},
                'suppressed_until': {}
            }
            self._save_alert_state()
            self.logger.info("Alert state cleared")
            
        except Exception as e:
            self.logger.error(f"Failed to clear alert state: {e}")
    
    def create_sample_config(self):
        """Create a sample configuration file"""
        try:
            sample_config = {
                "email_enabled": False,
                "email_from": "atlas@yourdomain.com",
                "email_to": ["admin@yourdomain.com"],
                "email_password": "your-email-password-here",
                "webhook_enabled": False,
                "webhook_url": "https://hooks.slack.com/your-webhook-url"
            }
            
            with open(self.config_file, 'w') as f:
                json.dump(sample_config, f, indent=2)
            
            self.logger.info(f"Sample config created at {self.config_file}")
            print(f"📝 Sample alert config created: {self.config_file}")
            print("Edit this file to configure email/webhook alerts")
            
        except Exception as e:
            self.logger.error(f"Failed to create sample config: {e}")

def main():
    """Test alert manager functionality"""
    alert_manager = AtlasAlertManager()
    
    print("🚨 Atlas Alert Manager - Phase 3.2")
    print("=" * 50)
    
    # Check if config exists, create sample if not
    if not alert_manager.config_file.exists():
        print("📝 Creating sample configuration...")
        alert_manager.create_sample_config()
    
    # Get status
    status = alert_manager.get_alert_status()
    print("📊 Alert Manager Status:")
    print(f"  Email enabled: {status['configuration']['email_enabled']}")
    print(f"  Webhook enabled: {status['configuration']['webhook_enabled']}")
    print(f"  Local notifications: {status['configuration']['local_notification_enabled']}")
    print(f"  Total alerts sent: {status['state']['total_alerts_sent']}")
    
    # Test with a sample alert
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        print("\n🧪 Testing alert system...")
        
        test_alert = {
            'timestamp': datetime.now().isoformat(),
            'metric_name': 'test_metric',
            'value': 95.0,
            'threshold': 90.0,
            'severity': 'WARNING',
            'message': 'Test alert - Atlas monitoring system is working'
        }
        
        result = alert_manager.process_alert(test_alert)
        print(f"Test alert processed: {result}")

if __name__ == "__main__":
    main()