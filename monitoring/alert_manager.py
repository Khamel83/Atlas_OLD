#!/usr/bin/env python3
"""
Alert Manager for Atlas Monitoring System

This script sets up an alerting system for Atlas using email notifications
via Gmail SMTP. It monitors system and application metrics and sends
alerts based on predefined thresholds.

Features:
- Gmail SMTP configuration for email alerts
- Critical and warning alert definitions
- Weekly summary email generation
- Alert deduplication and state management
"""

import smtplib
import ssl
import os
import json
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import subprocess
import sys

# Alert configuration
ALERT_CONFIG = {
    "email": {
        "smtp_server": "smtp.gmail.com",
        "port": 587,
        "sender_email": "atlas.monitor@gmail.com",  # To be configured
        "sender_password": "app_password",  # To be configured
        "recipient_email": "admin@khamel.com"  # To be configured
    },
    "thresholds": {
        "disk_usage_critical": 90,
        "disk_usage_warning": 80,
        "service_down": True,
        "high_error_rate": 10  # errors per minute
    },
    "schedule": {
        "weekly_summary_day": 6,  # Sunday (0=Monday, 6=Sunday)
        "weekly_summary_hour": 9  # 9 AM
    }
}

class AlertManager:
    def __init__(self, config):
        self.config = config
        self.alert_state = {}  # Track alert states to prevent duplicates
        self.smtp_config = config["email"]
        
    def send_email(self, subject, body):
        """Send an email using Gmail SMTP"""
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.smtp_config["sender_email"]
            message["To"] = self.smtp_config["recipient_email"]
            
            # Create text part
            text_part = MIMEText(body, "plain")
            message.attach(text_part)
            
            # Create secure connection and send email
            context = ssl.create_default_context()
            with smtplib.SMTP(self.smtp_config["smtp_server"], self.smtp_config["port"]) as server:
                server.starttls(context=context)
                server.login(self.smtp_config["sender_email"], self.smtp_config["sender_password"])
                server.sendmail(
                    self.smtp_config["sender_email"], 
                    self.smtp_config["recipient_email"], 
                    message.as_string()
                )
            
            print(f"Email sent successfully: {subject}")
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False
    
    def check_disk_usage(self):
        """Check disk usage and send alerts if thresholds are exceeded"""
        try:
            # Get disk usage
            result = subprocess.run(["df", "/"], capture_output=True, text=True, check=True)
            lines = result.stdout.strip().split("\n")
            if len(lines) > 1:
                # Parse disk usage percentage
                usage_info = lines[1].split()
                usage_percent = int(usage_info[4].rstrip('%'))
                
                # Check thresholds
                if usage_percent >= self.config["thresholds"]["disk_usage_critical"]:
                    alert_key = "disk_critical"
                    if not self.alert_state.get(alert_key, False):
                        subject = f"CRITICAL ALERT: Disk Usage at {usage_percent}%"
                        body = f"""
CRITICAL ALERT: Disk usage has reached {usage_percent}%

Immediate action is required to prevent system failure.

Current disk usage: {usage_percent}%
Critical threshold: {self.config["thresholds"]["disk_usage_critical"]}%

Please free up disk space immediately.
"""
                        self.send_email(subject, body)
                        self.alert_state[alert_key] = True
                elif usage_percent >= self.config["thresholds"]["disk_usage_warning"]:
                    alert_key = "disk_warning"
                    if not self.alert_state.get(alert_key, False):
                        subject = f"WARNING: Disk Usage at {usage_percent}%"
                        body = f"""
WARNING: Disk usage has reached {usage_percent}%

Consider freeing up disk space to prevent critical issues.

Current disk usage: {usage_percent}%
Warning threshold: {self.config["thresholds"]["disk_usage_warning"]}%
Critical threshold: {self.config["thresholds"]["disk_usage_critical"]}%
"""
                        self.send_email(subject, body)
                        self.alert_state[alert_key] = True
                else:
                    # Reset alert states if below thresholds
                    self.alert_state["disk_critical"] = False
                    self.alert_state["disk_warning"] = False
                    
        except Exception as e:
            print(f"Error checking disk usage: {str(e)}")
    
    def check_service_status(self):
        """Check if critical services are running"""
        services = ["prometheus", "grafana-server", "node_exporter", "atlas_background"]
        
        for service in services:
            try:
                result = subprocess.run(["systemctl", "is-active", service], 
                                      capture_output=True, text=True)
                if result.stdout.strip() != "active":
                    alert_key = f"service_down_{service}"
                    if not self.alert_state.get(alert_key, False):
                        subject = f"CRITICAL ALERT: Service {service} is DOWN"
                        body = f"""
CRITICAL ALERT: Service {service} is not running

The {service} service is in {result.stdout.strip()} state.
This may affect system monitoring and functionality.

Please check and restart the service immediately.
"""
                        self.send_email(subject, body)
                        self.alert_state[alert_key] = True
                else:
                    # Reset alert state if service is running
                    self.alert_state[f"service_down_{service}"] = False
            except Exception as e:
                print(f"Error checking service {service}: {str(e)}")
    
    def generate_weekly_summary(self):
        """Generate and send weekly summary email"""
        try:
            # Get system information
            hostname = os.uname().nodename
            
            # Get uptime
            uptime_result = subprocess.run(["uptime"], capture_output=True, text=True)
            uptime = uptime_result.stdout.strip()
            
            # Get disk usage
            disk_result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
            disk_usage = disk_result.stdout.strip()
            
            # Get memory usage
            mem_result = subprocess.run(["free", "-h"], capture_output=True, text=True)
            memory_usage = mem_result.stdout.strip()
            
            # Get top processes
            top_result = subprocess.run(["top", "-bn1"], capture_output=True, text=True)
            top_processes = "\n".join(top_result.stdout.strip().split("\n")[:10])
            
            subject = f"Weekly Atlas System Summary - {hostname}"
            body = f"""
ATLAS WEEKLY SYSTEM SUMMARY
===========================

Report Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Hostname: {hostname}

SYSTEM STATUS
-------------
{uptime}

DISK USAGE
----------
{disk_usage}

MEMORY USAGE
------------
{memory_usage}

TOP PROCESSES
-------------
{top_processes}

---

This is an automated weekly summary from your Atlas monitoring system.
"""
            
            self.send_email(subject, body)
            print("Weekly summary email sent successfully")
        except Exception as e:
            print(f"Error generating weekly summary: {str(e)}")
    
    def run_cycle(self):
        """Run a complete monitoring cycle"""
        print(f"Running alert check cycle at {datetime.now()}")
        
        # Check system metrics
        self.check_disk_usage()
        self.check_service_status()
        
        # Check if it's time for weekly summary
        now = datetime.now()
        if (now.weekday() == self.config["schedule"]["weekly_summary_day"] and 
            now.hour == self.config["schedule"]["weekly_summary_hour"] and
            now.minute < 5):  # Send within first 5 minutes of scheduled hour
            # Use a key based on date to prevent duplicate sends
            summary_key = f"weekly_summary_{now.strftime('%Y-%m-%d')}"
            if not self.alert_state.get(summary_key, False):
                self.generate_weekly_summary()
                self.alert_state[summary_key] = True
        elif now.hour != self.config["schedule"]["weekly_summary_hour"]:
            # Reset weekly summary state when hour changes
            summary_date = now.strftime('%Y-%m-%d')
            self.alert_state[f"weekly_summary_{summary_date}"] = False

def main():
    """Main function to run the alert manager"""
    print("Starting Atlas Alert Manager...")
    
    # Initialize alert manager
    alert_manager = AlertManager(ALERT_CONFIG)
    
    # For production, this would run as a daemon
    # For now, we'll run a few check cycles
    print("Running initial alert checks...")
    alert_manager.run_cycle()
    
    print("\nAlert Manager setup completed!")
    print("The system will now monitor:")
    print("- Disk usage (critical >90%, warning >80%)")
    print("- Service status (Prometheus, Grafana, Node Exporter, Atlas)")
    print("- Weekly summary emails every Sunday at 9 AM")
    print("\nNote: Email configuration needs to be updated in the script with actual credentials.")

if __name__ == "__main__":
    main()