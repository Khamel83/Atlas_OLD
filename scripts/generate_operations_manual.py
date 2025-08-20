#!/usr/bin/env python3
"""
Atlas Production Operations Manual Generator

This script generates a comprehensive operations manual for the Atlas production environment,
including system administration procedures, monitoring guides, troubleshooting documentation,
and best practices.

Features:
- System administration procedures
- Monitoring and alerting guides
- Troubleshooting documentation
- Best practices and recommendations
- Emergency procedures
"""

import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/ubuntu/dev/atlas/logs/operations_manual.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('AtlasOperationsManual')

class AtlasOperationsManual:
    def __init__(self):
        self.manual = {
            'title': 'Atlas Production Operations Manual',
            'version': '1.0',
            'generated_date': datetime.now().isoformat(),
            'last_updated': datetime.now().isoformat(),
            'sections': {}
        }
        
        # Create logs directory if it doesn't exist
        Path('/home/ubuntu/dev/atlas/logs').mkdir(parents=True, exist_ok=True)
    
    def generate_system_overview(self):
        \"\"\"Generate system overview section\"\"\"
        overview = {
            'title': 'System Overview',
            'description': 'High-level overview of the Atlas production environment',
            'architecture': {
                'components': [
                    {
                        'name': 'Atlas Main Application',
                        'description': 'Core content processing and management service',
                        'technology': 'Python 3, Flask',
                        'port': 5000
                    },
                    {
                        'name': 'PostgreSQL Database',
                        'description': 'Primary data storage for content and metadata',
                        'version': '12+',
                        'port': 5432
                    },
                    {
                        'name': 'Nginx Web Server',
                        'description': 'Reverse proxy and SSL termination',
                        'port': 80,
                        'ssl_port': 443
                    },
                    {
                        'name': 'Prometheus Monitoring',
                        'description': 'Metrics collection and alerting system',
                        'port': 9090
                    },
                    {
                        'name': 'Grafana Dashboard',
                        'description': 'Visualization of system and application metrics',
                        'port': 3000
                    }
                ]
            },
            'system_specifications': {
                'operating_system': 'Ubuntu 20.04 LTS',
                'python_version': '3.9+',
                'database_version': 'PostgreSQL 12+',
                'web_server': 'Nginx 1.18+',
                'monitoring_stack': 'Prometheus 2.30+, Grafana 8.0+'
            }
        }
        
        self.manual['sections']['system_overview'] = overview
        return overview
    
    def generate_administration_procedures(self):
        \"\"\"Generate system administration procedures\"\"\"
        admin_procedures = {
            'title': 'System Administration Procedures',
            'description': 'Standard procedures for administering the Atlas production environment',
            'service_management': {
                'starting_services': {
                    'title': 'Starting Services',
                    'procedure': [
                        '1. Start PostgreSQL database: sudo systemctl start postgresql',
                        '2. Start Atlas main service: sudo systemctl start atlas',
                        '3. Start monitoring services: sudo systemctl start atlas-prometheus atlas-grafana',
                        '4. Start web server: sudo systemctl start nginx',
                        '5. Verify all services are running: sudo systemctl status atlas postgresql nginx'
                    ]
                },
                'stopping_services': {
                    'title': 'Stopping Services',
                    'procedure': [
                        '1. Stop web server: sudo systemctl stop nginx',
                        '2. Stop monitoring services: sudo systemctl stop atlas-prometheus atlas-grafana',
                        '3. Stop Atlas main service: sudo systemctl stop atlas',
                        '4. Stop PostgreSQL database: sudo systemctl stop postgresql',
                        '5. Verify all services are stopped: sudo systemctl status atlas postgresql nginx'
                    ]
                },
                'restarting_services': {
                    'title': 'Restarting Services',
                    'procedure': [
                        '1. Restart all services: sudo systemctl restart atlas postgresql nginx atlas-prometheus atlas-grafana',
                        '2. Wait 30 seconds for services to initialize',
                        '3. Verify services are running: sudo systemctl status atlas postgresql nginx',
                        '4. Check application health: curl -f http://localhost:5000/health'
                    ]
                }
            },
            'user_management': {
                'adding_users': {
                    'title': 'Adding Users',
                    'procedure': [
                        '1. Add system user: sudo adduser newuser',
                        '2. Add to sudo group if needed: sudo usermod -aG sudo newuser',
                        '3. Configure SSH access: sudo nano /home/newuser/.ssh/authorized_keys',
                        '4. Set proper permissions: sudo chmod 700 /home/newuser/.ssh && sudo chmod 600 /home/newuser/.ssh/authorized_keys'
                    ]
                },
                'removing_users': {
                    'title': 'Removing Users',
                    'procedure': [
                        '1. Lock user account: sudo passwd -l username',
                        '2. Remove user: sudo deluser username',
                        '3. Remove home directory: sudo rm -rf /home/username',
                        '4. Remove from groups: sudo gpasswd -d username groupname'
                    ]
                }
            },
            'software_updates': {
                'title': 'Software Updates',
                'procedure': [
                        '1. Update package list: sudo apt update',
                        '2. Check for security updates: sudo unattended-upgrade -d',
                        '3. Upgrade specific packages: sudo apt upgrade packagename',
                        '4. Install new packages: sudo apt install packagename',
                        '5. Verify updates: sudo systemctl status servicename'
                    ]
            }
        }
        
        self.manual['sections']['administration_procedures'] = admin_procedures
        return admin_procedures
    
    def generate_monitoring_guides(self):
        \"\"\"Generate monitoring and alerting guides\"\"\"
        monitoring_guides = {
            'title': 'Monitoring and Alerting Guides',
            'description': 'Guides for monitoring and responding to alerts in the Atlas production environment',
            'prometheus_monitoring': {
                'title': 'Prometheus Monitoring',
                'access': 'http://your-server:9090',
                'key_metrics': [
                    'atlas_articles_processed_total',
                    'atlas_podcasts_downloaded_total',
                    'atlas_youtube_videos_processed_total',
                    'system_cpu_usage',
                    'system_memory_usage',
                    'system_disk_usage'
                ],
                'alert_rules': [
                    'High CPU usage > 90%',
                    'Low disk space < 10%',
                    'Service down detection',
                    'High error rates in processing'
                ]
            },
            'grafana_dashboards': {
                'title': 'Grafana Dashboards',
                'access': 'http://your-server:3000',
                'dashboards': [
                    'Atlas Overview Dashboard',
                    'System Health Dashboard',
                    'Content Processing Dashboard',
                    'Database Performance Dashboard'
                ]
            },
            'alert_response': {
                'title': 'Alert Response Procedures',
                'critical_alerts': [
                    {
                        'alert': 'Service Down',
                        'response': [
                            '1. Verify service status: systemctl status servicename',
                            '2. Check service logs: journalctl -u servicename',
                            '3. Attempt restart: systemctl restart servicename',
                            '4. If restart fails, check dependencies and system resources',
                            '5. Document issue and resolution'
                        ]
                    },
                    {
                        'alert': 'High Disk Usage',
                        'response': [
                            '1. Check disk usage: df -h',
                            '2. Identify large files: sudo find / -type f -size +100M -exec ls -lh {} \\; | head -10',
                            '3. Clean up old logs: sudo find /var/log -name \"*.log\" -mtime +30 -delete',
                            '4. Clean up temp files: sudo find /tmp -type f -mtime +7 -delete',
                            '5. If needed, expand disk space or archive data'
                        ]
                    }
                ]
            }
        }
        
        self.manual['sections']['monitoring_guides'] = monitoring_guides
        return monitoring_guides
    
    def generate_troubleshooting_guide(self):
        \"\"\"Generate troubleshooting documentation\"\"\"
        troubleshooting = {
            'title': 'Troubleshooting Guide',
            'description': 'Common issues and solutions for the Atlas production environment',
            'common_issues': [
                {
                    'issue': 'Service Not Starting',
                    'diagnosis': [
                        'Check service logs: sudo journalctl -u atlas',
                        'Verify database connectivity: sudo -u postgres pg_isready',
                        'Check configuration files: /home/ubuntu/dev/atlas/.env'
                    ],
                    'solutions': [
                        'Restart service: sudo systemctl restart atlas',
                        'Check for port conflicts: sudo netstat -tlnp | grep 5000',
                        'Verify database credentials in .env file'
                    ]
                },
                {
                    'issue': 'Database Connection Issues',
                    'diagnosis': [
                        'Check database status: sudo systemctl status postgresql',
                        'Verify database is accepting connections: sudo -u postgres pg_isready',
                        'Check database logs: /var/log/postgresql/'
                    ],
                    'solutions': [
                        'Restart database: sudo systemctl restart postgresql',
                        'Verify database credentials in application config',
                        'Check firewall rules for port 5432'
                    ]
                },
                {
                    'issue': 'High Resource Usage',
                    'diagnosis': [
                        'Check system resources: top, htop',
                        'Check Atlas logs for processing issues',
                        'Monitor with Prometheus/Grafana dashboards'
                    ],
                    'solutions': [
                        'Restart Atlas service to clear memory leaks',
                        'Check for stuck processing jobs',
                        'Scale up system resources if consistently high usage'
                    ]
                },
                {
                    'issue': 'SSL Certificate Issues',
                    'diagnosis': [
                        'Check certificate validity: openssl x509 -in /etc/letsencrypt/live/atlas.khamel.com/cert.pem -noout -dates',
                        'Check Nginx configuration: sudo nginx -t',
                        'Check certificate renewal logs: /var/log/letsencrypt/'
                    ],
                    'solutions': [
                        'Renew certificate: sudo certbot renew',
                        'Restart Nginx: sudo systemctl restart nginx',
                        'Check domain DNS settings'
                    ]
                }
            ]
        }
        
        self.manual['sections']['troubleshooting'] = troubleshooting
        return troubleshooting
    
    def generate_backup_recovery(self):
        \"\"\"Generate backup and recovery procedures\"\"\"
        backup_recovery = {
            'title': 'Backup and Recovery Procedures',
            'description': 'Procedures for backing up and recovering the Atlas production environment',
            'backup_procedures': {
                'daily_backups': {
                    'title': 'Daily Database Backups',
                    'frequency': 'Daily at 2:00 AM',
                    'script': '/home/ubuntu/dev/atlas/scripts/production_backup.sh',
                    'verification': 'Automated verification after each backup',
                    'retention': '30 days'
                },
                'configuration_backups': {
                    'title': 'Configuration Backups',
                    'frequency': 'Weekly',
                    'components': ['.env file', 'config directory', 'systemd service files'],
                    'retention': '90 days'
                }
            },
            'recovery_procedures': {
                'full_recovery': {
                    'title': 'Full System Recovery',
                    'steps': [
                        '1. Provision new server instance',
                        '2. Install required packages and dependencies',
                        '3. Restore database from backup: /home/ubuntu/dev/atlas/backup/restore.py',
                        '4. Restore configuration files',
                        '5. Recreate systemd service files',
                        '6. Start all services',
                        '7. Verify system functionality'
                    ]
                },
                'partial_recovery': {
                    'title': 'Partial Recovery',
                    'scenarios': [
                        'Database only recovery',
                        'Configuration only recovery',
                        'Specific content recovery'
                    ]
                }
            }
        }
        
        self.manual['sections']['backup_recovery'] = backup_recovery
        return backup_recovery
    
    def generate_security_procedures(self):
        \"\"\"Generate security procedures and best practices\"\"\"
        security = {
            'title': 'Security Procedures',
            'description': 'Security best practices and procedures for the Atlas production environment',
            'authentication': {
                'web_interface': {
                    'method': 'Basic HTTP Authentication',
                    'configuration': '/etc/nginx/.htpasswd',
                    'management': 'Use htpasswd command to manage users'
                },
                'ssh_access': {
                    'key_based_auth': 'Enabled',
                    'password_auth': 'Disabled',
                    'allowed_users': ['ubuntu'],
                    'port': 22
                }
            },
            'ssl_configuration': {
                'certificate_authority': 'Let\\'s Encrypt',
                'renewal': 'Automatic via certbot',
                'configuration': '/etc/nginx/sites-available/atlas'
            },
            'firewall': {
                'tool': 'UFW (Uncomplicated Firewall)',
                'rules': {
                    'ssh': '22/tcp - Limited to specific IPs',
                    'http': '80/tcp - Open',
                    'https': '443/tcp - Open',
                    'postgres': '5432/tcp - Local only'
                }
            },
            'regular_audits': {
                'frequency': 'Monthly',
                'procedures': [
                    'Review firewall rules',
                    'Check authentication logs',
                    'Verify file permissions',
                    'Update security patches',
                    'Review access controls'
                ]
            }
        }
        
        self.manual['sections']['security'] = security
        return security
    
    def generate_emergency_procedures(self):
        \"\"\"Generate emergency procedures\"\"\"
        emergency = {
            'title': 'Emergency Procedures',
            'description': 'Procedures for handling emergency situations in the Atlas production environment',
            'panic_button': {
                'title': 'Emergency Restart',
                'script': '/home/ubuntu/dev/atlas/devops/panic_button.py',
                'procedure': [
                    '1. Run emergency restart script: /home/ubuntu/dev/atlas/devops/panic_button.py',
                    '2. Monitor service status: watch -n 5 systemctl status atlas postgresql nginx',
                    '3. Verify application health: curl -f http://localhost:5000/health'
                ]
            },
            'service_outage': {
                'title': 'Service Outage Response',
                'procedure': [
                    '1. Identify affected services',
                    '2. Check system resources and logs',
                    '3. Attempt service restart',
                    '4. If restart fails, check dependencies',
                    '5. Escalate to system administrator if needed',
                    '6. Document incident and resolution'
                ]
            },
            'security_breach': {
                'title': 'Security Breach Response',
                'procedure': [
                    '1. Isolate affected systems',
                    '2. Change all passwords and credentials',
                    '3. Revoke and regenerate SSL certificates',
                    '4. Audit all logs for suspicious activity',
                    '5. Restore from clean backups',
                    '6. Implement additional security measures',
                    '7. Document incident and notify stakeholders'
                ]
            }
        }
        
        self.manual['sections']['emergency'] = emergency
        return emergency
    
    def generate_best_practices(self):
        \"\"\"Generate best practices and recommendations\"\"\"
        best_practices = {
            'title': 'Best Practices and Recommendations',
            'description': 'Recommended best practices for maintaining the Atlas production environment',
            'system_maintenance': {
                'title': 'System Maintenance',
                'recommendations': [
                    'Regularly update system packages and security patches',
                    'Monitor system resources and performance metrics',
                    'Review and rotate log files to prevent disk space issues',
                    'Conduct regular backup verification tests',
                    'Document all system changes and updates'
                ]
            },
            'performance_optimization': {
                'title': 'Performance Optimization',
                'recommendations': [
                    'Monitor and tune database performance regularly',
                    'Optimize application code for efficiency',
                    'Use caching mechanisms where appropriate',
                    'Scale resources based on usage patterns',
                    'Implement efficient data storage and retrieval'
                ]
            },
            'monitoring_improvement': {
                'title': 'Monitoring Improvement',
                'recommendations': [
                    'Add more detailed metrics for application performance',
                    'Implement custom alerting rules for business-critical metrics',
                    'Regularly review and update dashboard visualizations',
                    'Set up automated reporting for key metrics',
                    'Conduct periodic monitoring system reviews'
                ]
            }
        }
        
        self.manual['sections']['best_practices'] = best_practices
        return best_practices
    
    def generate_all_sections(self):
        \"\"\"Generate all sections of the operations manual\"\"\"
        print(\"Generating Atlas Production Operations Manual...\")
        
        # Generate each section
        self.generate_system_overview()
        self.generate_administration_procedures()
        self.generate_monitoring_guides()
        self.generate_troubleshooting_guide()
        self.generate_backup_recovery()
        self.generate_security_procedures()
        self.generate_emergency_procedures()
        self.generate_best_practices()
        
        # Save as JSON
        json_file = \"/home/ubuntu/dev/atlas/docs/operations_manual.json\"
        with open(json_file, 'w') as f:
            json.dump(self.manual, f, indent=2)
        
        # Generate Markdown documentation
        self.generate_markdown_manual()
        
        # Generate PDF documentation
        self.generate_pdf_manual()
        
        print(f\"Operations manual generated successfully!\")
        print(f\"JSON: {json_file}\")
        print(f\"Markdown: /home/ubuntu/dev/atlas/docs/operations_manual.md\")
        print(f\"PDF: /home/ubuntu/dev/atlas/docs/operations_manual.pdf\")
        
        return self.manual
    
    def generate_markdown_manual(self):
        \"\"\"Generate Markdown version of the operations manual\"\"\"
        md_content = f\"\"\"# {self.manual['title']}
*Version {self.manual['version']} - Generated {self.manual['generated_date']}*

## Table of Contents
1. [System Overview](#system-overview)
2. [System Administration Procedures](#system-administration-procedures)
3. [Monitoring and Alerting Guides](#monitoring-and-alerting-guides)
4. [Troubleshooting Guide](#troubleshooting-guide)
5. [Backup and Recovery Procedures](#backup-and-recovery-procedures)
6. [Security Procedures](#security-procedures)
7. [Emergency Procedures](#emergency-procedures)
8. [Best Practices and Recommendations](#best-practices-and-recommendations)

\"\"\"
        
        # Add each section
        sections = self.manual['sections']
        
        # System Overview
        overview = sections['system_overview']
        md_content += f\"## System Overview\\n\\n{overview['description']}\\n\\n\"
        
        md_content += \"### System Components\\n\\n\"
        for component in overview['architecture']['components']:
            md_content += f\"#### {component['name']}\\n\"
            md_content += f\"- **Description**: {component['description']}\\n\"
            md_content += f\"- **Technology**: {component['technology']}\\n\"
            if 'port' in component:
                md_content += f\"- **Port**: {component['port']}\\n\"
            md_content += \"\\n\"
        
        md_content += \"### System Specifications\\n\\n\"
        for spec, value in overview['system_specifications'].items():
            md_content += f\"- **{spec.replace('_', ' ').title()}**: {value}\\n\"
        md_content += \"\\n\"
        
        # Administration Procedures
        admin = sections['administration_procedures']
        md_content += f\"## System Administration Procedures\\n\\n{admin['description']}\\n\\n\"
        
        for category_key, category in admin['service_management'].items():
            md_content += f\"### {category['title']}\\n\\n\"
            for step in category['procedure']:
                md_content += f\"{step}\\n\"
            md_content += \"\\n\"
        
        # Monitoring Guides
        monitoring = sections['monitoring_guides']
        md_content += f\"## Monitoring and Alerting Guides\\n\\n{monitoring['description']}\\n\\n\"
        
        md_content += f\"### {monitoring['prometheus_monitoring']['title']}\\n\\n\"
        md_content += f\"**Access**: {monitoring['prometheus_monitoring']['access']}\\n\\n\"
        md_content += \"**Key Metrics**:\\n\"
        for metric in monitoring['prometheus_monitoring']['key_metrics']:
            md_content += f\"- {metric}\\n\"
        md_content += \"\\n**Alert Rules**:\\n\"
        for rule in monitoring['prometheus_monitoring']['alert_rules']:
            md_content += f\"- {rule}\\n\"
        md_content += \"\\n\"
        
        # Troubleshooting Guide
        troubleshooting = sections['troubleshooting']
        md_content += f\"## Troubleshooting Guide\\n\\n{troubleshooting['description']}\\n\\n\"
        
        for issue in troubleshooting['common_issues']:
            md_content += f\"### {issue['issue']}\\n\\n\"
            md_content += \"**Diagnosis**:\\n\"
            for step in issue['diagnosis']:
                md_content += f\"- {step}\\n\"
            md_content += \"\\n**Solutions**:\\n\"
            for step in issue['solutions']:
                md_content += f\"- {step}\\n\"
            md_content += \"\\n\"
        
        # Save Markdown file
        md_file = \"/home/ubuntu/dev/atlas/docs/operations_manual.md\"
        with open(md_file, 'w') as f:
            f.write(md_content)
    
    def generate_pdf_manual(self):
        \"\"\"Generate PDF version of the operations manual (placeholder)\"\"\"
        # In a real implementation, this would use a library like ReportLab
        # or convert the Markdown to PDF using pandoc
        pdf_file = \"/home/ubuntu/dev/atlas/docs/operations_manual.pdf\"
        with open(pdf_file, 'w') as f:
            f.write(f\"Atlas Production Operations Manual\\n\")
            f.write(f\"Version {self.manual['version']}\\n\")
            f.write(f\"Generated {self.manual['generated_date']}\\n\\n\")
            f.write(\"PDF generation would be implemented here.\\n\")
            f.write(\"For now, please refer to the Markdown version.\\n\")

def main():
    \"\"\"Main function\"\"\"
    print(\"Atlas Production Operations Manual Generator\")
    print(\"=\" * 45)
    
    # Create and generate operations manual
    manual = AtlasOperationsManual()
    ops_manual = manual.generate_all_sections()
    
    print(\"\\nOperations manual generation completed successfully!\")
    print(\"Manual includes:\")
    for section_name in ops_manual['sections'].keys():
        print(f\"  - {section_name.replace('_', ' ').title()}\")
    
    return 0

if __name__ == \"__main__\":
    sys.exit(main())