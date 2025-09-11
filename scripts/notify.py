#!/usr/bin/env python3
"""
Atlas Notification System
Sends alerts via Telegram and optional Uptime Kuma webhook.
"""

import os
import sys
import argparse
import requests
import json
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


class AtlasNotificationSystem:
    """Send notifications via multiple channels"""
    
    def __init__(self):
        self.telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.uptime_kuma_url = os.getenv('UPTIME_KUMA_URL')
        
    def send_telegram_message(self, message: str) -> bool:
        """Send message via Telegram"""
        if not self.telegram_bot_token or not self.telegram_chat_id:
            print("❌ Telegram credentials not configured")
            return False
            
        try:
            url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
            payload = {
                'chat_id': self.telegram_chat_id,
                'text': message,
                'parse_mode': 'Markdown'
            }
            
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            
            print("✅ Telegram message sent")
            return True
            
        except Exception as e:
            print(f"❌ Telegram send failed: {e}")
            return False
    
    def send_uptime_kuma_alert(self, status: str, message: str) -> bool:
        """Send alert to Uptime Kuma webhook"""
        if not self.uptime_kuma_url:
            print("⏭️  Uptime Kuma not configured, skipping")
            return True
            
        try:
            payload = {
                'status': status,
                'message': message,
                'timestamp': datetime.now().isoformat()
            }
            
            response = requests.post(self.uptime_kuma_url, json=payload, timeout=10)
            response.raise_for_status()
            
            print("✅ Uptime Kuma alert sent")
            return True
            
        except Exception as e:
            print(f"❌ Uptime Kuma send failed: {e}")
            return False
    
    def send_alert(self, title: str, message: str, alert_type: str = "warning") -> bool:
        """Send alert via all configured channels"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format for Telegram (Markdown)
        telegram_message = f"🚨 *Atlas Alert*\n\n*{title}*\n\n{message}\n\n📅 {timestamp}"
        
        # Send via Telegram
        telegram_success = self.send_telegram_message(telegram_message)
        
        # Send via Uptime Kuma
        uptime_success = self.send_uptime_kuma_alert(alert_type, f"{title}: {message}")
        
        return telegram_success or uptime_success
    
    def send_recovery_alert(self, title: str, message: str) -> bool:
        """Send recovery (green) alert"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format for Telegram (Markdown)
        telegram_message = f"✅ *Atlas Recovery*\n\n*{title}*\n\n{message}\n\n📅 {timestamp}"
        
        # Send via Telegram
        telegram_success = self.send_telegram_message(telegram_message)
        
        # Send via Uptime Kuma
        uptime_success = self.send_uptime_kuma_alert("up", f"{title}: {message}")
        
        return telegram_success or uptime_success


def send_notification(message: str, title: str = "Atlas Alert", priority: str = "warning") -> bool:
    """Convenience function for sending notifications."""
    notifier = AtlasNotificationSystem()
    
    if priority == "critical" or priority == "error":
        return notifier.send_alert(title, message, "error")
    elif priority == "info" or priority == "recovery":
        return notifier.send_recovery_alert(title, message)
    else:
        return notifier.send_alert(title, message, "warning")


def main():
    """CLI interface for notifications"""
    parser = argparse.ArgumentParser(description='Atlas Notification System')
    parser.add_argument('--msg', required=True, help='Message to send')
    parser.add_argument('--title', default='Atlas Alert', help='Alert title')
    parser.add_argument('--type', choices=['warning', 'error', 'recovery'], default='warning', help='Alert type')
    parser.add_argument('--test', action='store_true', help='Send test message')
    
    args = parser.parse_args()
    
    notifier = AtlasNotificationSystem()
    
    if args.test:
        success = notifier.send_alert(
            "Test Alert",
            "This is a test notification from Atlas monitoring system.",
            "warning"
        )
    elif args.type == 'recovery':
        success = notifier.send_recovery_alert(args.title, args.msg)
    else:
        success = notifier.send_alert(args.title, args.msg, args.type)
    
    if success:
        print("📤 Notification sent successfully")
        sys.exit(0)
    else:
        print("💥 Notification failed")
        sys.exit(1)


if __name__ == "__main__":
    main()