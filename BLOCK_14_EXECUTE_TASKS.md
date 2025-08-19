# 🤖 Block 14 Execute-Tasks Format for Agent OS

## 🎯 Mission: Transform Atlas into Production-Ready Personal Platform

You are implementing Atlas Block 14: Personal Production Hardening. Your goal is to create a self-maintaining, monitored, backed-up production system that runs on OCI free tier and requires zero manual intervention.

**Domain**: atlas.khamel.com  
**Platform**: OCI free tier  
**Cost Target**: $0/month  
**Maintenance**: Fully automated

---

## 🚀 STARTUP PROTOCOL FOR BLOCK 14

### **Environment Setup**
```bash
cd /home/ubuntu/dev/atlas
source atlas_venv/bin/activate
source load_secrets.sh

# Verify domain configuration
nslookup atlas.khamel.com
ping atlas.khamel.com
```

### **Read Context**
- **PRIMARY**: Study `docs/specs/BLOCK_14_IMPLEMENTATION.md` 
- **INTEGRATION**: Review existing `scripts/atlas_background_service.py`
- **ARCHITECTURE**: Understand current nginx/systemd setup

---

## 📋 EXECUTE-TASKS: BLOCK 14.1 - MONITORING SYSTEM

### **TASK 14.1.1: Install Prometheus**
```bash
# Install Prometheus
sudo apt update
sudo apt install prometheus prometheus-node-exporter -y

# Configure Prometheus
sudo nano /etc/prometheus/prometheus.yml
# Add Atlas metrics endpoints

# Start services
sudo systemctl enable prometheus prometheus-node-exporter
sudo systemctl start prometheus prometheus-node-exporter
```

**Create**: `monitoring/prometheus_setup.py`
**Verify**: `curl http://localhost:9090/metrics`

### **TASK 14.1.2: Install Grafana**
```bash
# Install Grafana
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update && sudo apt install grafana -y

# Configure and start
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

**Create**: `monitoring/grafana_config/atlas_dashboard.json`
**Verify**: Navigate to `http://your-ip:3000`

### **TASK 14.1.3: Atlas Metrics Exporter**
**Create**: `monitoring/atlas_metrics_exporter.py`
```python
from prometheus_client import start_http_server, Gauge, Counter
import time
import psycopg2
from helpers.config import load_config

# Atlas-specific metrics
articles_processed = Counter('atlas_articles_processed_total')
processing_queue_size = Gauge('atlas_processing_queue_size')
service_uptime = Gauge('atlas_service_uptime_seconds')

def collect_atlas_metrics():
    # Implementation here
    pass

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        collect_atlas_metrics()
        time.sleep(15)
```

**Integrate**: Add to `scripts/atlas_background_service.py`
**Verify**: `curl http://localhost:8000/metrics`

### **TASK 14.1.4: Email Alert System**
**Create**: `monitoring/alert_manager.py`
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AlertManager:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        
    def send_alert(self, subject, message):
        # Email alert implementation
        pass
        
    def check_system_health(self):
        # Health check implementation
        pass
```

**Configure**: Gmail SMTP credentials in `.env.secure`
**Test**: Send test alert email

---

## 📋 EXECUTE-TASKS: BLOCK 14.2 - SSL + AUTHENTICATION

### **TASK 14.2.1: Domain Configuration**
```bash
# Verify atlas.khamel.com points to your OCI IP
nslookup atlas.khamel.com

# If not configured, add A record in Squarespace:
# atlas.khamel.com -> your.oci.ip.address
```

**Verify**: Domain resolves to OCI VM
**Document**: DNS configuration steps

### **TASK 14.2.2: Let's Encrypt SSL**
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Stop nginx temporarily
sudo systemctl stop nginx

# Get certificate
sudo certbot certonly --standalone -d atlas.khamel.com

# Set up auto-renewal
sudo crontab -e
# Add: 0 3 * * * certbot renew --quiet && systemctl reload nginx
```

**Create**: `ssl/ssl_setup.sh`
**Verify**: Certificate exists in `/etc/letsencrypt/live/atlas.khamel.com/`

### **TASK 14.2.3: nginx SSL Configuration**
**Create**: `/etc/nginx/sites-available/atlas-ssl`
```nginx
server {
    listen 80;
    server_name atlas.khamel.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name atlas.khamel.com;
    
    ssl_certificate /etc/letsencrypt/live/atlas.khamel.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/atlas.khamel.com/privkey.pem;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Frame-Options DENY always;
    add_header X-Content-Type-Options nosniff always;
    
    # Basic auth
    auth_basic "Atlas Access";
    auth_basic_user_file /etc/nginx/.htpasswd;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**Execute**: 
```bash
sudo ln -s /etc/nginx/sites-available/atlas-ssl /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

### **TASK 14.2.4: Basic Authentication**
```bash
# Create htpasswd file
sudo htpasswd -c /etc/nginx/.htpasswd atlas_user

# Set secure permissions
sudo chmod 640 /etc/nginx/.htpasswd
sudo chown root:nginx /etc/nginx/.htpasswd
```

**Test**: `curl -u atlas_user:password https://atlas.khamel.com`
**Verify**: Authentication required for access

---

## 📋 EXECUTE-TASKS: BLOCK 14.3 - BACKUP SYSTEM

### **TASK 14.3.1: Database Backup Script**
**Create**: `backup/database_backup.py`
```python
#!/usr/bin/env python3
import subprocess
import datetime
import os
import gzip
from pathlib import Path

def backup_database():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = Path('/home/ubuntu/backups/database')
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    backup_file = backup_dir / f'atlas_backup_{timestamp}.sql'
    compressed_file = backup_dir / f'atlas_backup_{timestamp}.sql.gz'
    
    # pg_dump command
    cmd = [
        'pg_dump',
        '-h', 'localhost',
        '-U', 'atlas_user', 
        '-d', 'atlas',
        '-f', str(backup_file)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Compress backup
        with open(backup_file, 'rb') as f_in:
            with gzip.open(compressed_file, 'wb') as f_out:
                f_out.writelines(f_in)
        
        os.remove(backup_file)
        print(f"Backup successful: {compressed_file}")
        return compressed_file
    else:
        print(f"Backup failed: {result.stderr}")
        return None

if __name__ == '__main__':
    backup_database()
```

**Configure**: Database credentials in `.env.secure`
**Test**: Run backup manually

### **TASK 14.3.2: OCI Object Storage Setup**
```bash
# Install OCI CLI
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

# Configure OCI CLI
oci setup config

# Create Object Storage bucket
oci os bucket create --name atlas-backups --compartment-id your-compartment-id
```

**Create**: `backup/oci_storage_backup.py`
```python
import subprocess
from pathlib import Path

def upload_to_oci(local_file):
    cmd = [
        'oci', 'os', 'object', 'put',
        '--bucket-name', 'atlas-backups',
        '--file', str(local_file),
        '--name', local_file.name
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0
```

**Test**: Upload test file to OCI Object Storage

### **TASK 14.3.3: Local Machine Backup Sync**
**Create**: `backup/local_sync_backup.py`
```python
import subprocess
from pathlib import Path

def sync_to_local_machine():
    local_machine_ip = "your.local.machine.ip"
    local_backup_path = "/path/to/local/backups/"
    
    cmd = [
        'rsync', '-avz', '--delete',
        '/home/ubuntu/backups/',
        f'user@{local_machine_ip}:{local_backup_path}'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0
```

**Setup**: SSH key authentication to personal machine
**Test**: Sync backup files to local machine

### **TASK 14.3.4: Automated Backup Scheduling**
```bash
# Add to crontab
crontab -e

# Daily database backup at 2 AM
0 2 * * * /home/ubuntu/dev/atlas/backup/run_daily_backup.sh

# Weekly local sync on Sundays at 3 AM  
0 3 * * 0 /home/ubuntu/dev/atlas/backup/run_weekly_sync.sh
```

**Create**: `backup/run_daily_backup.sh`
**Create**: `backup/run_weekly_sync.sh`
**Test**: All backup automation

### **TASK 14.3.5: One-Command Restore**
**Create**: `backup/restore_system.py`
```python
#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

def list_backups():
    backup_dir = Path('/home/ubuntu/backups/database')
    backups = sorted(backup_dir.glob('*.sql.gz'))
    return backups

def restore_from_backup(backup_file):
    # Stop Atlas services
    subprocess.run(['sudo', 'systemctl', 'stop', 'atlas-background'])
    
    # Restore database
    cmd = f"gunzip -c {backup_file} | psql -h localhost -U atlas_user -d atlas"
    result = subprocess.run(cmd, shell=True)
    
    # Restart services
    subprocess.run(['sudo', 'systemctl', 'start', 'atlas-background'])
    
    return result.returncode == 0

if __name__ == '__main__':
    if len(sys.argv) > 1:
        backup_file = sys.argv[1]
        restore_from_backup(backup_file)
    else:
        backups = list_backups()
        for i, backup in enumerate(backups[-10:]):  # Show last 10
            print(f"{i}: {backup.name}")
```

**Test**: Full restore from backup

---

## 📋 EXECUTE-TASKS: BLOCK 14.4 - MAINTENANCE AUTOMATION

### **TASK 14.4.1: Auto-Updates Configuration**
```bash
# Configure unattended-upgrades
sudo apt install unattended-upgrades -y

# Configure automatic updates
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
# Enable security updates

# Configure update schedule
sudo nano /etc/apt/apt.conf.d/20auto-upgrades
# Set automatic update frequency
```

**Create**: `maintenance/system_updates.py`
**Schedule**: Updates at 4 AM PST daily
**Test**: Automatic update process

### **TASK 14.4.2: Atlas Service Maintenance**
**Create**: `maintenance/atlas_maintenance.py`
```python
import subprocess
import psycopg2
from pathlib import Path

class AtlasMaintenance:
    def __init__(self):
        self.config = load_config()
        
    def retry_failed_articles(self):
        # Retry failed articles from last 24 hours
        pass
        
    def optimize_database(self):
        # Run VACUUM and ANALYZE on Atlas database
        pass
        
    def cleanup_logs(self):
        # Remove logs older than 30 days
        pass
        
    def restart_if_needed(self):
        # Check if Atlas services need restart
        pass

if __name__ == '__main__':
    maintenance = AtlasMaintenance()
    maintenance.retry_failed_articles()
    maintenance.optimize_database()
    maintenance.cleanup_logs()
    maintenance.restart_if_needed()
```

**Schedule**: Daily maintenance at 3 AM PST
**Test**: All maintenance tasks

### **TASK 14.4.3: Service Health Monitor**
**Create**: `maintenance/service_monitor.py`
```python
import subprocess
import time
import requests

class ServiceMonitor:
    def __init__(self):
        self.services = [
            'atlas-background',
            'nginx', 
            'postgresql',
            'prometheus',
            'grafana-server'
        ]
        
    def check_service_health(self, service):
        result = subprocess.run(
            ['systemctl', 'is-active', service],
            capture_output=True, text=True
        )
        return result.stdout.strip() == 'active'
        
    def restart_service(self, service):
        subprocess.run(['sudo', 'systemctl', 'restart', service])
        
    def monitor_loop(self):
        while True:
            for service in self.services:
                if not self.check_service_health(service):
                    self.restart_service(service)
                    # Send alert
            time.sleep(30)

if __name__ == '__main__':
    monitor = ServiceMonitor()
    monitor.monitor_loop()
```

**Configure**: As systemd service
**Test**: Service restart automation

---

## 📋 EXECUTE-TASKS: BLOCK 14.5 - DEVOPS TOOLS

### **TASK 14.5.1: Git-Based Deployment**
**Create**: `devops/git_deploy.py`
```python
#!/usr/bin/env python3
import subprocess
import datetime
from pathlib import Path

def backup_before_deploy():
    # Create backup before deployment
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_cmd = f"/home/ubuntu/dev/atlas/backup/database_backup.py"
    subprocess.run([backup_cmd])
    
def deploy_atlas():
    # Git pull latest changes
    subprocess.run(['git', 'pull', 'origin', 'main'])
    
    # Install/update dependencies
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    
    # Run database migrations if any
    # subprocess.run(['python', 'migrate.py'])
    
    # Restart Atlas services
    subprocess.run(['sudo', 'systemctl', 'restart', 'atlas-background'])
    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'])
    
    print("Deployment complete!")

if __name__ == '__main__':
    backup_before_deploy()
    deploy_atlas()
```

**Setup**: Git hooks for automatic deployment
**Test**: Push-to-deploy functionality

### **TASK 14.5.2: Emergency Recovery Tools**
**Create**: `devops/emergency_tools.py`
```python
#!/usr/bin/env python3
import subprocess

def panic_button():
    """Restart all Atlas services"""
    services = [
        'atlas-background',
        'nginx',
        'postgresql', 
        'prometheus',
        'grafana-server'
    ]
    
    for service in services:
        print(f"Restarting {service}...")
        subprocess.run(['sudo', 'systemctl', 'restart', service])
    
    print("All services restarted!")

def status_check():
    """Quick system status check"""
    services = [
        'atlas-background',
        'nginx',
        'postgresql'
    ]
    
    for service in services:
        result = subprocess.run(
            ['systemctl', 'is-active', service],
            capture_output=True, text=True
        )
        status = result.stdout.strip()
        print(f"{service}: {status}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'panic':
        panic_button()
    else:
        status_check()
```

**Create**: Simple status API endpoint
**Test**: Emergency procedures

---

## 📋 EXECUTE-TASKS: BLOCK 14.6 - OCI OPTIMIZATIONS

### **TASK 14.6.1: OCI Free Tier Monitoring**
**Create**: `oci/free_tier_monitor.py`
```python
import subprocess
import json

class OCIFreeTierMonitor:
    def __init__(self):
        self.compute_limit = 2  # 2 VMs max
        self.storage_limit = 200  # 200GB max
        self.object_storage_limit = 10  # 10GB max
        
    def check_compute_usage(self):
        cmd = ['oci', 'compute', 'instance', 'list', '--output', 'json']
        result = subprocess.run(cmd, capture_output=True, text=True)
        instances = json.loads(result.stdout)
        return len(instances['data'])
        
    def check_storage_usage(self):
        # Check block volume usage
        cmd = ['oci', 'bv', 'volume', 'list', '--output', 'json']
        result = subprocess.run(cmd, capture_output=True, text=True)
        volumes = json.loads(result.stdout)
        total_storage = sum(vol['size-in-gbs'] for vol in volumes['data'])
        return total_storage
        
    def check_object_storage_usage(self):
        cmd = ['oci', 'os', 'object', 'list', '--bucket-name', 'atlas-backups', '--output', 'json']
        result = subprocess.run(cmd, capture_output=True, text=True)
        objects = json.loads(result.stdout)
        total_size = sum(obj['size'] for obj in objects['data']) / (1024**3)  # Convert to GB
        return total_size
        
    def generate_usage_report(self):
        compute_usage = self.check_compute_usage()
        storage_usage = self.check_storage_usage()
        object_usage = self.check_object_storage_usage()
        
        report = f"""
        OCI Free Tier Usage Report:
        Compute: {compute_usage}/{self.compute_limit} instances
        Block Storage: {storage_usage}/{self.storage_limit} GB
        Object Storage: {object_usage:.2f}/{self.object_storage_limit} GB
        """
        
        return report

if __name__ == '__main__':
    monitor = OCIFreeTierMonitor()
    print(monitor.generate_usage_report())
```

**Schedule**: Weekly usage report
**Alert**: If approaching limits

### **TASK 14.6.2: OCI Security Configuration**
```bash
# Configure OCI Security Lists
oci network security-list update --security-list-id your-security-list-id \
    --ingress-security-rules '[
        {
            "source": "0.0.0.0/0",
            "protocol": "6",
            "tcpOptions": {
                "destinationPortRange": {
                    "min": 443,
                    "max": 443
                }
            }
        }
    ]'
```

**Configure**: Firewall rules for Atlas
**Test**: Security configuration

---

## 📋 EXECUTE-TASKS: BLOCK 14.7 - LAZY PERSON FEATURES

### **TASK 14.7.1: Mobile Dashboard**
**Create**: `lazy/mobile_dashboard.py`
```python
from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/status')
def simple_status():
    # Simple status page for mobile
    services = check_all_services()
    stats = get_atlas_stats()
    
    return render_template('mobile_status.html', 
                         services=services, 
                         stats=stats)

@app.route('/api/health')
def health_check():
    """Simple API endpoint for external monitoring"""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

def check_all_services():
    # Check all critical services
    pass

def get_atlas_stats():
    # Get Atlas processing statistics
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

**Create**: `templates/mobile_status.html` (mobile-responsive)
**Test**: Mobile access and functionality

### **TASK 14.7.2: Weekly Status Email**
**Create**: `lazy/weekly_status.py`
```python
import datetime
from monitoring.alert_manager import AlertManager

class WeeklyStatusReporter:
    def __init__(self):
        self.alert_manager = AlertManager()
        
    def generate_weekly_report(self):
        # Generate comprehensive weekly status
        report = f"""
        Atlas Weekly Status Report - {datetime.date.today()}
        
        SYSTEM HEALTH:
        - Uptime: {self.get_uptime()}
        - Services: {self.get_service_status()}
        - Storage: {self.get_storage_usage()}
        
        PROCESSING STATS:
        - Articles processed: {self.get_articles_count()}
        - Success rate: {self.get_success_rate()}%
        - Queue status: {self.get_queue_status()}
        
        ISSUES:
        {self.get_issues_summary()}
        """
        
        return report
        
    def send_weekly_email(self):
        report = self.generate_weekly_report()
        self.alert_manager.send_alert(
            "Atlas Weekly Status", 
            report
        )

if __name__ == '__main__':
    reporter = WeeklyStatusReporter()
    reporter.send_weekly_email()
```

**Schedule**: Every Sunday at 9 AM PST
**Test**: Weekly email delivery

### **TASK 14.7.3: Ultimate Convenience**
**Create**: `lazy/convenience_features.py`
```python
#!/usr/bin/env python3

def auto_heal_common_issues():
    """Automatically fix common Atlas issues"""
    issues_fixed = []
    
    # Check disk space
    if get_disk_usage() > 90:
        cleanup_old_files()
        issues_fixed.append("Cleaned up disk space")
    
    # Check service health
    for service in ['atlas-background', 'nginx', 'postgresql']:
        if not is_service_running(service):
            restart_service(service)
            issues_fixed.append(f"Restarted {service}")
    
    # Check Atlas processing
    if get_hours_since_last_processing() > 2:
        restart_atlas_processing()
        issues_fixed.append("Restarted Atlas processing")
    
    return issues_fixed

def create_convenience_cron_jobs():
    """Set up auto-healing cron jobs"""
    cron_jobs = [
        "*/15 * * * * /home/ubuntu/dev/atlas/lazy/auto_heal.py",  # Every 15 minutes
        "0 */6 * * * /home/ubuntu/dev/atlas/lazy/deep_clean.py"   # Every 6 hours
    ]
    
    for job in cron_jobs:
        add_cron_job(job)

if __name__ == '__main__':
    fixed = auto_heal_common_issues()
    if fixed:
        print(f"Auto-healed: {', '.join(fixed)}")
```

**Configure**: Auto-healing automation
**Test**: All convenience features

---

## 🔄 FINAL INTEGRATION AND TESTING

### **TASK 14.8.1: Full System Integration Test**
```bash
# Run complete system test
python devops/full_system_test.py

# Test backup and restore
./backup/test_backup_restore.sh

# Test monitoring and alerts
python monitoring/test_alerts.py

# Test SSL and authentication
curl -k https://atlas.khamel.com/status
```

### **TASK 14.8.2: 24-Hour Burn-In Test**
- Let system run for 24+ hours
- Monitor all services and alerts
- Verify backup automation
- Test emergency procedures
- Validate mobile access

### **TASK 14.8.3: Documentation and Handoff**
**Create**: `PRODUCTION_OPERATIONS_MANUAL.md`
**Update**: `CLAUDE.md` with production status
**Create**: Emergency contact procedures
**Test**: All documented procedures

---

## ✅ SUCCESS CRITERIA - BLOCK 14 COMPLETE

**When these all work, Block 14 is complete:**

1. ✅ **atlas.khamel.com** loads with HTTPS and authentication
2. ✅ **Monitoring dashboard** shows all Atlas and system metrics
3. ✅ **Daily backups** complete automatically and upload to OCI
4. ✅ **Weekly backups** sync to personal machine automatically
5. ✅ **Email alerts** notify of any system issues within 5 minutes
6. ✅ **Auto-updates** install at 4 AM PST without breaking Atlas
7. ✅ **Service monitoring** restarts failed services automatically
8. ✅ **Mobile dashboard** works perfectly on phone
9. ✅ **Weekly status email** delivers every Sunday
10. ✅ **Emergency tools** fix common issues in under 30 seconds
11. ✅ **Git deployment** works with `git push production`
12. ✅ **OCI costs** remain $0/month
13. ✅ **System runs 24+ hours** without manual intervention

**When all criteria pass: Atlas is production-ready! 🚀**