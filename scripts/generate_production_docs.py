#!/usr/bin/env python3
"""
Atlas Production Documentation Generator

This script generates comprehensive documentation for the Atlas production environment,
including system architecture, operational procedures, monitoring guides, and troubleshooting
information.

Features:
- System architecture documentation
- Operational procedures
- Monitoring and alerting guides
- Troubleshooting documentation
- Backup and recovery procedures
- Security guidelines
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

class AtlasDocumentationGenerator:
    def __init__(self):
        self.docs_dir = "/home/ubuntu/dev/atlas/docs"
        self.output_dir = f"{self.docs_dir}/production"
        
        # Create directories if they don't exist
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        
        self.documentation = {
            'title': 'Atlas Production Documentation',
            'version': '1.0',
            'generated_date': datetime.now().isoformat(),
            'sections': {}
        }
    
    def generate_system_architecture(self):
        """Generate system architecture documentation"""
        architecture_docs = {
            'title': 'System Architecture',
            'description': 'Overview of the Atlas production system architecture',
            'components': {
                'main_application': {
                    'name': 'Atlas Main Application',
                    'description': 'Core content processing and management service',
                    'technology': 'Python 3, Flask',
                    'port': 5000,
                    'dependencies': ['PostgreSQL', 'Nginx']
                },
                'database': {
                    'name': 'PostgreSQL Database',
                    'description': 'Primary data storage for content and metadata',
                    'version': '12+',
                    'port': 5432
                },
                'web_server': {
                    'name': 'Nginx Web Server',
                    'description': 'Reverse proxy and SSL termination',
                    'port': 80,
                    'ssl_port': 443
                },
                'monitoring': {
                    'name': 'Monitoring Stack',
                    'description': 'Prometheus metrics collection and Grafana visualization',
                    'components': {
                        'prometheus': {
                            'name': 'Prometheus',
                            'port': 9090
                        },
                        'grafana': {
                            'name': 'Grafana',
                            'port': 3000
                        },
                        'node_exporter': {
                            'name': 'Node Exporter',
                            'port': 9100
                        }
                    }
                }
            },
            'diagram': '''
Atlas Production Architecture

┌─────────────────────────────────────────────────────────────┐
│                    Load Balancer (Optional)                 │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                        Nginx (443)                          │
│                   SSL Termination & Proxy                   │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                     Atlas Application (5000)                │
│               Content Processing & Management               │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                     PostgreSQL Database (5432)              │
│                 Content, Metadata, and State                │
└─────────────────────────────────────────────────────────────┘

┌───────────────────┐    ┌───────────────────┐    ┌───────────────────┐
│  Prometheus (9090)│    │  Grafana (3000)   │    │ Node Exporter (9100)│
│  Metrics Collection│    │   Visualization   │    │ System Metrics     │
└───────────────────┘    └───────────────────┘    └───────────────────┘
'''
        }
        
        self.documentation['sections']['architecture'] = architecture_docs
        return architecture_docs
    
    def generate_operational_procedures(self):
        """Generate operational procedures documentation"""
        operational_docs = {
            'title': 'Operational Procedures',
            'description': 'Standard operating procedures for managing Atlas production',
            'procedures': {
                'starting_services': {
                    'title': 'Starting Services',
                    'description': 'Procedure to start all Atlas services',
                    'steps': [
                        '1. Start PostgreSQL database: sudo systemctl start postgresql',
                        '2. Start Atlas main service: sudo systemctl start atlas',
                        '3. Start monitoring services: sudo systemctl start atlas-prometheus atlas-grafana',
                        '4. Start web server: sudo systemctl start nginx',
                        '5. Verify all services are running: sudo systemctl status atlas postgresql nginx'
                    ]
                },
                'stopping_services': {
                    'title': 'Stopping Services',
                    'description': 'Procedure to stop all Atlas services',
                    'steps': [
                        '1. Stop web server: sudo systemctl stop nginx',
                        '2. Stop monitoring services: sudo systemctl stop atlas-prometheus atlas-grafana',
                        '3. Stop Atlas main service: sudo systemctl stop atlas',
                        '4. Stop PostgreSQL database: sudo systemctl stop postgresql',
                        '5. Verify all services are stopped: sudo systemctl status atlas postgresql nginx'
                    ]
                },
                'restarting_services': {
                    'title': 'Restarting Services',
                    'description': 'Procedure to restart Atlas services',
                    'steps': [
                        '1. Restart all services: sudo systemctl restart atlas postgresql nginx atlas-prometheus atlas-grafana',
                        '2. Wait 30 seconds for services to initialize',
                        '3. Verify services are running: sudo systemctl status atlas postgresql nginx',
                        '4. Check application health: curl -f http://localhost:5000/health'
                    ]
                },
                'deploying_updates': {
                    'title': 'Deploying Updates',
                    'description': 'Procedure to deploy code updates to production',
                    'steps': [
                        '1. Create backup: /home/ubuntu/dev/atlas/scripts/production_backup.sh',
                        '2. Stop Atlas service: sudo systemctl stop atlas',
                        '3. Pull latest code: cd /home/ubuntu/dev/atlas && git pull',
                        '4. Update dependencies: source atlas_venv/bin/activate && pip install -r requirements.txt',
                        '5. Run migrations: python3 /home/ubuntu/dev/atlas/migrations/migrate.py',
                        '6. Start Atlas service: sudo systemctl start atlas',
                        '7. Verify deployment: curl -f http://localhost:5000/'
                    ]
                }
            }
        }
        
        self.documentation['sections']['operations'] = operational_docs
        return operational_docs
    
    def generate_monitoring_guides(self):
        """Generate monitoring and alerting documentation"""
        monitoring_docs = {
            'title': 'Monitoring and Alerting',
            'description': 'Guides for monitoring Atlas production environment',
            'tools': {
                'prometheus': {
                    'title': 'Prometheus Monitoring',
                    'description': 'Metrics collection and alerting system',
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
                'grafana': {
                    'title': 'Grafana Dashboards',
                    'description': 'Visualization of system and application metrics',
                    'access': 'http://your-server:3000',
                    'dashboards': [
                        'Atlas Overview Dashboard',
                        'System Health Dashboard',
                        'Content Processing Dashboard',
                        'Database Performance Dashboard'
                    ]
                }
            },
            'alerting': {
                'email_alerts': {
                    'title': 'Email Alerts',
                    'description': 'Configuration for email-based alerting',
                    'setup': 'Configured via /home/ubuntu/dev/atlas/monitoring/alert_manager.py',
                    'recipients': 'admin@khamel.com',
                    'alert_types': [
                        'Critical service down',
                        'Disk space warnings (80% and 90%)',
                        'Processing pipeline stopped',
                        'High error rates',
                        'Weekly summary reports'
                    ]
                }
            }
        }
        
        self.documentation['sections']['monitoring'] = monitoring_docs
        return monitoring_docs
    
    def generate_troubleshooting_guide(self):
        """Generate troubleshooting documentation"""
        troubleshooting_docs = {
            'title': 'Troubleshooting Guide',
            'description': 'Common issues and solutions for Atlas production environment',
            'common_issues': {
                'service_not_starting': {
                    'title': 'Service Not Starting',
                    'description': 'Atlas service fails to start',
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
                'database_connection_issues': {
                    'title': 'Database Connection Issues',
                    'description': 'Application cannot connect to database',
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
                'high_resource_usage': {
                    'title': 'High Resource Usage',
                    'description': 'System showing high CPU or memory usage',
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
                'ssl_certificate_issues': {
                    'title': 'SSL Certificate Issues',
                    'description': 'HTTPS access failing due to certificate problems',
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
            },
            'emergency_procedures': {
                'panic_button': {
                    'title': 'Emergency Restart',
                    'description': 'Quick restart of all services',
                    'procedure': [
                        'Run emergency restart script: /home/ubuntu/dev/atlas/devops/panic_button.py',
                        'Monitor service status: watch -n 5 systemctl status atlas postgresql nginx',
                        'Verify application health: curl -f http://localhost:5000/health'
                    ]
                },
                'backup_restore': {
                    'title': 'Backup Restore',
                    'description': 'Restoring system from backup',
                    'procedure': [
                        'Stop all services: sudo systemctl stop atlas postgresql nginx',
                        'Restore database from backup: /home/ubuntu/dev/atlas/backup/restore.py',
                        'Restart services: sudo systemctl start postgresql atlas nginx',
                        'Verify restore: Check application functionality and data integrity'
                    ]
                }
            }
        }
        
        self.documentation['sections']['troubleshooting'] = troubleshooting_docs
        return troubleshooting_docs
    
    def generate_backup_recovery(self):
        """Generate backup and recovery documentation"""
        backup_docs = {
            'title': 'Backup and Recovery',
            'description': 'Procedures for backing up and recovering Atlas production data',
            'backup_strategy': {
                'database_backups': {
                    'title': 'Database Backups',
                    'frequency': 'Daily at 2:00 AM',
                    'retention': '30 days',
                    'location': '/home/ubuntu/dev/atlas/backups/',
                    'script': '/home/ubuntu/dev/atlas/backup/database_backup.py',
                    'verification': 'Automated verification after each backup'
                },
                'configuration_backups': {
                    'title': 'Configuration Backups',
                    'frequency': 'Weekly',
                    'retention': '90 days',
                    'location': '/home/ubuntu/dev/atlas/backups/',
                    'components': ['.env file', 'config directory', 'systemd service files']
                },
                'cloud_backups': {
                    'title': 'Cloud Backups',
                    'frequency': 'Daily',
                    'retention': '90 days',
                    'destination': 'OCI Object Storage',
                    'script': '/home/ubuntu/dev/atlas/backup/oci_storage_backup.py'
                }
            },
            'recovery_procedures': {
                'full_recovery': {
                    'title': 'Full System Recovery',
                    'description': 'Complete recovery from backup',
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
                    'description': 'Recovery of specific components',
                    'scenarios': [
                        'Database only recovery',
                        'Configuration only recovery',
                        'Specific content recovery'
                    ]
                }
            }
        }
        
        self.documentation['sections']['backup_recovery'] = backup_docs
        return backup_docs
    
    def generate_security_guidelines(self):
        """Generate security guidelines documentation"""
        security_docs = {
            'title': 'Security Guidelines',
            'description': 'Security best practices and configurations for Atlas production',
            'authentication': {
                'web_interface': {
                    'title': 'Web Interface Authentication',
                    'method': 'Basic HTTP Authentication',
                    'configuration': '/etc/nginx/.htpasswd',
                    'management': 'Use htpasswd command to manage users'
                },
                'ssh_access': {
                    'title': 'SSH Access Security',
                    'key_based_auth': 'Enabled',
                    'password_auth': 'Disabled',
                    'allowed_users': ['ubuntu'],
                    'port': 22
                }
            },
            'ssl_configuration': {
                'title': 'SSL/TLS Configuration',
                'certificate_authority': 'Let's Encrypt',
                'renewal': 'Automatic via certbot',
                'configuration': '/etc/nginx/sites-available/atlas',
                'cipher_suite': 'Modern secure ciphers'
            },
            'firewall': {
                'title': 'Firewall Configuration',
                'tool': 'UFW (Uncomplicated Firewall)',
                'rules': {
                    'ssh': '22/tcp - Limited to specific IPs',
                    'http': '80/tcp - Open',
                    'https': '443/tcp - Open',
                    'postgres': '5432/tcp - Local only'
                }
            },
            'monitoring_security': {
                'title': 'Monitoring Security',
                'grafana_auth': 'Admin password protection',
                'prometheus_access': 'Local network only',
                'log_security': 'Log file permissions restricted'
            }
        }
        
        self.documentation['sections']['security'] = security_docs
        return security_docs
    
    def generate_deployment_checklist(self):
        """Generate deployment checklist documentation"""
        deployment_docs = {
            'title': 'Deployment Checklist',
            'description': 'Pre-flight checklist for deploying Atlas to production',
            'pre_deployment': {
                'code_review': 'All code changes reviewed and approved',
                'testing': 'Unit tests and integration tests passing',
                'security_scan': 'Security scan completed with no critical issues',
                'backup': 'Current production backup created and verified'
            },
            'deployment': {
                'maintenance_window': 'Scheduled during low-usage period',
                'communication': 'Users notified of maintenance window',
                'rollback_plan': 'Clear rollback procedure documented',
                'monitoring': 'Monitoring alerts temporarily disabled if needed'
            },
            'post_deployment': {
                'verification': 'Application functionality verified',
                'monitoring': 'Monitoring alerts re-enabled',
                'performance': 'Performance metrics checked',
                'notification': 'Users notified of service restoration'
            }
        }
        
        self.documentation['sections']['deployment'] = deployment_docs
        return deployment_docs
    
    def generate_all_documentation(self):
        """Generate all documentation sections"""
        print("Generating Atlas Production Documentation...")
        
        # Generate each section
        self.generate_system_architecture()
        self.generate_operational_procedures()
        self.generate_monitoring_guides()
        self.generate_troubleshooting_guide()
        self.generate_backup_recovery()
        self.generate_security_guidelines()
        self.generate_deployment_checklist()
        
        # Save as JSON
        json_file = f"{self.output_dir}/atlas_production_docs.json"
        with open(json_file, 'w') as f:
            json.dump(self.documentation, f, indent=2)
        
        # Generate Markdown documentation
        self.generate_markdown_docs()
        
        # Generate PDF documentation
        self.generate_pdf_docs()
        
        print(f"Documentation generated successfully!")
        print(f"JSON: {json_file}")
        print(f"Markdown: {self.output_dir}/atlas_production_docs.md")
        print(f"PDF: {self.output_dir}/atlas_production_docs.pdf")
        
        return self.documentation
    
    def generate_markdown_docs(self):
        """Generate Markdown version of documentation"""
        md_content = f"""# {self.documentation['title']}
*Version {self.documentation['version']} - Generated {self.documentation['generated_date']}*

## Table of Contents
1. [System Architecture](#system-architecture)
2. [Operational Procedures](#operational-procedures)
3. [Monitoring and Alerting](#monitoring-and-alerting)
4. [Troubleshooting Guide](#troubleshooting-guide)
5. [Backup and Recovery](#backup-and-recovery)
6. [Security Guidelines](#security-guidelines)
7. [Deployment Checklist](#deployment-checklist)

"""
        
        # Add each section
        sections = self.documentation['sections']
        
        # System Architecture
        arch = sections['architecture']
        md_content += f"## System Architecture\\n\\n{arch['description']}\\n\\n"
        md_content += "### Components\\n\\n"
        for comp_key, comp in arch['components'].items():
            md_content += f"#### {comp['name']}\\n"
            md_content += f"- **Description**: {comp['description']}\\n"
            if 'technology' in comp:
                md_content += f"- **Technology**: {comp['technology']}\\n"
            if 'port' in comp:
                md_content += f"- **Port**: {comp['port']}\\n"
            if 'dependencies' in comp:
                md_content += f"- **Dependencies**: {', '.join(comp['dependencies'])}\\n"
            md_content += "\\n"
        
        md_content += f"### Architecture Diagram\\n\\n```\\n{arch['diagram']}\\n```\\n\\n"
        
        # Operational Procedures
        ops = sections['operations']
        md_content += f"## Operational Procedures\\n\\n{ops['description']}\\n\\n"
        for proc_key, proc in ops['procedures'].items():
            md_content += f"### {proc['title']}\\n\\n{proc['description']}\\n\\n"
            md_content += "Steps:\\n"
            for step in proc['steps']:
                md_content += f"{step}\\n"
            md_content += "\\n"
        
        # Save Markdown file
        md_file = f"{self.output_dir}/atlas_production_docs.md"
        with open(md_file, 'w') as f:
            f.write(md_content)
    
    def generate_pdf_docs(self):
        """Generate PDF version of documentation (placeholder)"""
        # In a real implementation, this would use a library like ReportLab
        # or convert the Markdown to PDF using pandoc
        pdf_file = f"{self.output_dir}/atlas_production_docs.pdf"
        with open(pdf_file, 'w') as f:
            f.write(f"Atlas Production Documentation\\n")
            f.write(f"Version {self.documentation['version']}\\n")
            f.write(f"Generated {self.documentation['generated_date']}\\n\\n")
            f.write("PDF generation would be implemented here.\\n")
            f.write("For now, please refer to the Markdown version.\\n")

def main():
    """Main function"""
    print("Atlas Production Documentation Generator")
    print("=" * 45)
    
    # Create and generate documentation
    generator = AtlasDocumentationGenerator()
    docs = generator.generate_all_documentation()
    
    print("\\nDocumentation generation completed successfully!")
    print(f"Output directory: {generator.output_dir}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())