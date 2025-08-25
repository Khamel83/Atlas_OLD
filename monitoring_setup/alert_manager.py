#!/usr/bin/env python3
import json
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

class AlertManager:
    def __init__(self):
        self.email_config = {
            'smtp_server': os.getenv('SMTP_SERVER', 'localhost'),
            'smtp_port': int(os.getenv('SMTP_PORT', '587')),
            'smtp_user': os.getenv('SMTP_USER', ''),
            'smtp_password': os.getenv('SMTP_PASSWORD', ''),
            'alert_email': os.getenv('ALERT_EMAIL', 'admin@localhost')
        }
    
    def send_email_alert(self, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['smtp_user']
            msg['To'] = self.email_config['alert_email']
            msg['Subject'] = f"[ATLAS ALERT] {subject}"
            
            msg.attach(MIMEText(message, 'plain'))
            
            if self.email_config['smtp_user']:
                server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
                server.starttls()
                server.login(self.email_config['smtp_user'], self.email_config['smtp_password'])
                server.send_message(msg)
                server.quit()
                return True
        except Exception as e:
            print(f"Failed to send email alert: {e}")
        return False
    
    def check_and_alert(self):
        alerts = []
        
        # Check health
        try:
            result = subprocess.run(['python3', 'monitoring_setup/health_check.py'], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode != 0:
                alerts.append("System health check failed")
        except Exception:
            alerts.append("Health check script failed to run")
        
        # Check performance
        try:
            with open('logs/performance_metrics.log', 'r') as f:
                lines = f.readlines()
                if lines:
                    latest_metrics = json.loads(lines[-1])
                    
                    if latest_metrics['system']['cpu_percent'] > 90:
                        alerts.append(f"High CPU usage: {latest_metrics['system']['cpu_percent']}%")
                    
                    if latest_metrics['system']['memory_percent'] > 90:
                        alerts.append(f"High memory usage: {latest_metrics['system']['memory_percent']}%")
                    
                    if latest_metrics['system']['disk_percent'] > 90:
                        alerts.append(f"High disk usage: {latest_metrics['system']['disk_percent']}%")
                    
                    if latest_metrics['atlas']['api_response_time_ms'] > 5000:
                        alerts.append(f"Slow API response: {latest_metrics['atlas']['api_response_time_ms']}ms")
        except Exception as e:
            alerts.append(f"Failed to check performance metrics: {e}")
        
        # Send alerts
        if alerts:
            subject = f"Atlas System Alert - {len(alerts)} issues detected"
            message = f"Atlas monitoring detected the following issues:\n\n"
            message += "\n".join([f"• {alert}" for alert in alerts])
            message += f"\n\nTime: {datetime.now().isoformat()}"
            message += f"\nServer: {os.uname().nodename}"
            
            self.send_email_alert(subject, message)
            print(f"Sent alert for {len(alerts)} issues")
        else:
            print("All systems normal")

def main():
    alert_manager = AlertManager()
    alert_manager.check_and_alert()

if __name__ == "__main__":
    main()
