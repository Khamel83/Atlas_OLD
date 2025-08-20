#!/usr/bin/env python3
"""
Atlas Production Security Audit Report Generator

This script performs a comprehensive security audit of the Atlas production environment
and generates a detailed report with findings and recommendations.

Features:
- System security checks
- Network security analysis
- Application security assessment
- Data protection evaluation
- Compliance verification
- Vulnerability scanning
"""

import os
import sys
import subprocess
import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/ubuntu/dev/atlas/logs/security_audit.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('AtlasSecurityAudit')

class AtlasSecurityAudit:
    def __init__(self):
        self.audit_report = {
            'timestamp': datetime.now().isoformat(),
            'system_info': {},
            'findings': [],
            'recommendations': [],
            'overall_score': 0,
            'risk_level': 'UNKNOWN'
        }
        
        # Create logs directory if it doesn't exist
        Path('/home/ubuntu/dev/atlas/logs').mkdir(parents=True, exist_ok=True)
    
    def check_system_security(self):
        """Check system-level security configuration"""
        logger.info("Checking system security...")
        
        findings = []
        
        # Check if firewall is active
        try:
            result = subprocess.run(['sudo', 'ufw', 'status'], capture_output=True, text=True)
            if 'Status: active' in result.stdout:
                findings.append({
                    'category': 'system',
                    'type': 'firewall',
                    'status': 'PASS',
                    'description': 'Firewall is active',
                    'severity': 'INFO'
                })
            else:
                findings.append({
                    'category': 'system',
                    'type': 'firewall',
                    'status': 'FAIL',
                    'description': 'Firewall is not active',
                    'severity': 'HIGH',
                    'recommendation': 'Enable UFW firewall: sudo ufw enable'
                })
        except Exception as e:
            findings.append({
                'category': 'system',
                'type': 'firewall',
                'status': 'ERROR',
                'description': f'Error checking firewall: {str(e)}',
                'severity': 'MEDIUM'
            })
        
        # Check SSH configuration
        ssh_config_path = '/etc/ssh/sshd_config'
        if os.path.exists(ssh_config_path):
            try:
                with open(ssh_config_path, 'r') as f:
                    ssh_config = f.read()
                
                # Check if password authentication is disabled
                if 'PasswordAuthentication no' in ssh_config or '#PasswordAuthentication yes' not in ssh_config:
                    findings.append({
                        'category': 'system',
                        'type': 'ssh',
                        'status': 'PASS',
                        'description': 'SSH password authentication is disabled',
                        'severity': 'INFO'
                    })
                else:
                    findings.append({
                        'category': 'system',
                        'type': 'ssh',
                        'status': 'FAIL',
                        'description': 'SSH password authentication is enabled',
                        'severity': 'HIGH',
                        'recommendation': 'Disable password auth in /etc/ssh/sshd_config: PasswordAuthentication no'
                    })
                
                # Check if root login is disabled
                if 'PermitRootLogin no' in ssh_config:
                    findings.append({
                        'category': 'system',
                        'type': 'ssh',
                        'status': 'PASS',
                        'description': 'SSH root login is disabled',
                        'severity': 'INFO'
                    })
                else:
                    findings.append({
                        'category': 'system',
                        'type': 'ssh',
                        'status': 'WARN',
                        'description': 'SSH root login is not explicitly disabled',
                        'severity': 'MEDIUM',
                        'recommendation': 'Disable root login in /etc/ssh/sshd_config: PermitRootLogin no'
                    })
            except Exception as e:
                findings.append({
                    'category': 'system',
                    'type': 'ssh',
                    'status': 'ERROR',
                    'description': f'Error reading SSH config: {str(e)}',
                    'severity': 'MEDIUM'
                })
        else:
            findings.append({
                'category': 'system',
                'type': 'ssh',
                'status': 'FAIL',
                'description': 'SSH configuration file not found',
                'severity': 'HIGH'
            })
        
        # Check for unnecessary services
        try:
            result = subprocess.run(['systemctl', 'list-units', '--type=service', '--state=running'], 
                                  capture_output=True, text=True)
            running_services = result.stdout
            
            # Check for potentially insecure services
            insecure_services = ['telnet', 'ftp', 'rsh']
            for service in insecure_services:
                if service in running_services:
                    findings.append({
                        'category': 'system',
                        'type': 'services',
                        'status': 'FAIL',
                        'description': f'Insecure service running: {service}',
                        'severity': 'HIGH',
                        'recommendation': f'Stop and disable {service} service'
                    })
        except Exception as e:
            findings.append({
                'category': 'system',
                'type': 'services',
                'status': 'ERROR',
                'description': f'Error checking running services: {str(e)}',
                'severity': 'MEDIUM'
            })
        
        self.audit_report['findings'].extend(findings)
        logger.info("System security check completed")
    
    def check_network_security(self):
        """Check network-level security configuration"""
        logger.info("Checking network security...")
        
        findings = []
        
        # Check open ports
        try:
            result = subprocess.run(['ss', '-tuln'], capture_output=True, text=True)
            open_ports = result.stdout
            
            # Check for critical ports that should not be open
            critical_ports = [23, 21, 111, 139, 445]  # telnet, ftp, rpc, netbios
            for port in critical_ports:
                if f':{port}' in open_ports:
                    findings.append({
                        'category': 'network',
                        'type': 'ports',
                        'status': 'FAIL',
                        'description': f'Critical port {port} is open',
                        'severity': 'HIGH',
                        'recommendation': f'Close port {port} using firewall rules'
                    })
            
            # Check for expected ports
            expected_ports = [22, 80, 443, 5432, 9090, 3000]
            for port in expected_ports:
                if f':{port}' in open_ports:
                    findings.append({
                        'category': 'network',
                        'type': 'ports',
                        'status': 'PASS',
                        'description': f'Expected port {port} is open',
                        'severity': 'INFO'
                    })
        except Exception as e:
            findings.append({
                'category': 'network',
                'type': 'ports',
                'status': 'ERROR',
                'description': f'Error checking open ports: {str(e)}',
                'severity': 'MEDIUM'
            })
        
        # Check firewall rules
        try:
            result = subprocess.run(['sudo', 'ufw', 'status', 'numbered'], capture_output=True, text=True)
            firewall_rules = result.stdout
            
            # Check if SSH is restricted
            if '22' in firewall_rules and 'Anywhere' in firewall_rules.split('22')[1].split('\n')[0]:
                findings.append({
                    'category': 'network',
                    'type': 'firewall',
                    'status': 'WARN',
                    'description': 'SSH access is not restricted to specific IPs',
                    'severity': 'MEDIUM',
                    'recommendation': 'Restrict SSH access to trusted IP ranges'
                })
        except Exception as e:
            findings.append({
                'category': 'network',
                'type': 'firewall',
                'status': 'ERROR',
                'description': f'Error checking firewall rules: {str(e)}',
                'severity': 'MEDIUM'
            })
        
        self.audit_report['findings'].extend(findings)
        logger.info("Network security check completed")
    
    def check_application_security(self):
        """Check application-level security configuration"""
        logger.info("Checking application security...")
        
        findings = []
        
        # Check web server security
        nginx_config_path = '/etc/nginx/sites-available/atlas'
        if os.path.exists(nginx_config_path):
            try:
                with open(nginx_config_path, 'r') as f:
                    nginx_config = f.read()
                
                # Check if security headers are configured
                security_headers = [
                    'X-Frame-Options',
                    'X-Content-Type-Options',
                    'X-XSS-Protection',
                    'Referrer-Policy',
                    'Content-Security-Policy'
                ]
                
                missing_headers = []
                for header in security_headers:
                    if header not in nginx_config:
                        missing_headers.append(header)
                
                if not missing_headers:
                    findings.append({
                        'category': 'application',
                        'type': 'web_server',
                        'status': 'PASS',
                        'description': 'Web server security headers are configured',
                        'severity': 'INFO'
                    })
                else:
                    findings.append({
                        'category': 'application',
                        'type': 'web_server',
                        'status': 'FAIL',
                        'description': f'Missing security headers: {", ".join(missing_headers)}',
                        'severity': 'MEDIUM',
                        'recommendation': f'Add missing security headers to nginx config: {", ".join(missing_headers)}'
                    })
                
                # Check if SSL is enforced
                if 'ssl' in nginx_config and 'return 301 https' in nginx_config:
                    findings.append({
                        'category': 'application',
                        'type': 'web_server',
                        'status': 'PASS',
                        'description': 'SSL is enforced for web interface',
                        'severity': 'INFO'
                    })
                else:
                    findings.append({
                        'category': 'application',
                        'type': 'web_server',
                        'status': 'FAIL',
                        'description': 'SSL is not enforced for web interface',
                        'severity': 'HIGH',
                        'recommendation': 'Configure SSL enforcement in nginx config'
                    })
            except Exception as e:
                findings.append({
                    'category': 'application',
                    'type': 'web_server',
                    'status': 'ERROR',
                    'description': f'Error reading nginx config: {str(e)}',
                    'severity': 'MEDIUM'
                })
        else:
            findings.append({
                'category': 'application',
                'type': 'web_server',
                'status': 'FAIL',
                'description': 'Nginx configuration file not found',
                'severity': 'HIGH'
            })
        
        # Check authentication configuration
        htpasswd_path = '/etc/nginx/.htpasswd'
        if os.path.exists(htpasswd_path):
            findings.append({
                'category': 'application',
                'type': 'authentication',
                'status': 'PASS',
                'description': 'Web authentication is configured',
                'severity': 'INFO'
            })
        else:
            findings.append({
                'category': 'application',
                'type': 'authentication',
                'status': 'FAIL',
                'description': 'Web authentication is not configured',
                'severity': 'HIGH',
                'recommendation': 'Configure basic authentication for web interface'
            })
        
        self.audit_report['findings'].extend(findings)
        logger.info("Application security check completed")
    
    def check_data_protection(self):
        """Check data protection and encryption"""
        logger.info("Checking data protection...")
        
        findings = []
        
        # Check SSL certificate
        ssl_cert_path = '/etc/letsencrypt/live/atlas.khamel.com/cert.pem'
        if os.path.exists(ssl_cert_path):
            try:
                # Check certificate expiration
                result = subprocess.run([
                    'openssl', 'x509', '-in', ssl_cert_path, '-noout', '-enddate'
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    expiry_info = result.stdout.strip().split('=')[1]
                    findings.append({
                        'category': 'data',
                        'type': 'ssl_certificate',
                        'status': 'PASS',
                        'description': f'SSL certificate exists and expires on {expiry_info}',
                        'severity': 'INFO'
                    })
                else:
                    findings.append({
                        'category': 'data',
                        'type': 'ssl_certificate',
                        'status': 'FAIL',
                        'description': 'SSL certificate exists but cannot read expiration',
                        'severity': 'MEDIUM'
                    })
            except Exception as e:
                findings.append({
                    'category': 'data',
                    'type': 'ssl_certificate',
                    'status': 'ERROR',
                    'description': f'Error checking SSL certificate: {str(e)}',
                    'severity': 'MEDIUM'
                })
        else:
            findings.append({
                'category': 'data',
                'type': 'ssl_certificate',
                'status': 'FAIL',
                'description': 'SSL certificate not found',
                'severity': 'HIGH',
                'recommendation': 'Install SSL certificate using Let's Encrypt'
            })
        
        # Check database encryption
        try:
            # Check if PostgreSQL has SSL enabled
            result = subprocess.run([
                'sudo', '-u', 'postgres', 'psql', '-c', 'SHOW ssl;'
            ], capture_output=True, text=True)
            
            if 'on' in result.stdout:
                findings.append({
                    'category': 'data',
                    'type': 'database',
                    'status': 'PASS',
                    'description': 'Database SSL is enabled',
                    'severity': 'INFO'
                })
            else:
                findings.append({
                    'category': 'data',
                    'type': 'database',
                    'status': 'WARN',
                    'description': 'Database SSL is not enabled',
                    'severity': 'MEDIUM',
                    'recommendation': 'Enable SSL for database connections'
                })
        except Exception as e:
            findings.append({
                'category': 'data',
                'type': 'database',
                'status': 'ERROR',
                'description': f'Error checking database SSL: {str(e)}',
                'severity': 'MEDIUM'
            })
        
        # Check file permissions
        sensitive_files = [
            ('/home/ubuntu/dev/atlas/.env', 'environment file'),
            ('/etc/nginx/.htpasswd', 'authentication file'),
            ('/home/ubuntu/dev/atlas/backups', 'backup directory')
        ]
        
        for file_path, description in sensitive_files:
            if os.path.exists(file_path):
                try:
                    # Check permissions
                    result = subprocess.run(['stat', '-c', '%a', file_path], capture_output=True, text=True)
                    permissions = result.stdout.strip()
                    
                    # Check if permissions are too permissive
                    if permissions in ['600', '640', '700']:
                        findings.append({
                            'category': 'data',
                            'type': 'file_permissions',
                            'status': 'PASS',
                            'description': f'{description} has secure permissions ({permissions})',
                            'severity': 'INFO'
                        })
                    else:
                        findings.append({
                            'category': 'data',
                            'type': 'file_permissions',
                            'status': 'FAIL',
                            'description': f'{description} has insecure permissions ({permissions})',
                            'severity': 'HIGH',
                            'recommendation': f'Set secure permissions for {file_path}: chmod 600 {file_path}'
                        })
                except Exception as e:
                    findings.append({
                        'category': 'data',
                        'type': 'file_permissions',
                        'status': 'ERROR',
                        'description': f'Error checking permissions for {file_path}: {str(e)}',
                        'severity': 'MEDIUM'
                    })
        
        self.audit_report['findings'].extend(findings)
        logger.info("Data protection check completed")
    
    def check_compliance(self):
        """Check compliance with security best practices"""
        logger.info("Checking compliance...")
        
        findings = []
        
        # Check if regular security updates are configured
        try:
            result = subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True)
            if 'security' in result.stdout:
                findings.append({
                    'category': 'compliance',
                    'type': 'updates',
                    'status': 'WARN',
                    'description': 'Security updates are available but not installed',
                    'severity': 'MEDIUM',
                    'recommendation': 'Install security updates or configure unattended-upgrades'
                })
            else:
                findings.append({
                    'category': 'compliance',
                    'type': 'updates',
                    'status': 'PASS',
                    'description': 'No security updates pending',
                    'severity': 'INFO'
                })
        except Exception as e:
            findings.append({
                'category': 'compliance',
                'type': 'updates',
                'status': 'ERROR',
                'description': f'Error checking for updates: {str(e)}',
                'severity': 'MEDIUM'
            })
        
        # Check if log monitoring is configured
        log_files = [
            '/var/log/auth.log',
            '/var/log/nginx/error.log',
            '/home/ubuntu/dev/atlas/logs/atlas_background.log'
        ]
        
        monitored_logs = 0
        for log_file in log_files:
            if os.path.exists(log_file):
                monitored_logs += 1
        
        if monitored_logs >= 2:
            findings.append({
                'category': 'compliance',
                'type': 'logging',
                'status': 'PASS',
                'description': f'{monitored_logs} log files are being monitored',
                'severity': 'INFO'
            })
        else:
            findings.append({
                'category': 'compliance',
                'type': 'logging',
                'status': 'WARN',
                'description': f'Only {monitored_logs} log files are being monitored',
                'severity': 'MEDIUM',
                'recommendation': 'Configure monitoring for all critical log files'
            })
        
        self.audit_report['findings'].extend(findings)
        logger.info("Compliance check completed")
    
    def generate_recommendations(self):
        """Generate recommendations based on findings"""
        logger.info("Generating recommendations...")
        
        recommendations = []
        findings = self.audit_report['findings']
        
        # Categorize findings by severity
        high_severity = [f for f in findings if f.get('severity') == 'HIGH']
        medium_severity = [f for f in findings if f.get('severity') == 'MEDIUM']
        
        if high_severity:
            recommendations.append({
                'priority': 'HIGH',
                'description': f'Address {len(high_severity)} high-severity security issues immediately',
                'actions': [f.get('recommendation', f.get('description')) for f in high_severity if f.get('recommendation')]
            })
        
        if medium_severity:
            recommendations.append({
                'priority': 'MEDIUM',
                'description': f'Review and address {len(medium_severity)} medium-severity security issues',
                'actions': [f.get('recommendation', f.get('description')) for f in medium_severity if f.get('recommendation')]
            })
        
        # General recommendations
        recommendations.append({
            'priority': 'LOW',
            'description': 'Implement additional security measures',
            'actions': [
                'Regularly review and update firewall rules',
                'Implement intrusion detection system',
                'Set up security monitoring and alerting',
                'Conduct periodic security audits',
                'Keep all software components up to date'
            ]
        })
        
        self.audit_report['recommendations'] = recommendations
        logger.info("Recommendations generated")
    
    def calculate_risk_score(self):
        """Calculate overall risk score and level"""
        logger.info("Calculating risk score...")
        
        findings = self.audit_report['findings']
        
        # Score calculation (0-100, where 100 is worst)
        score = 0
        max_score = len(findings) * 3  # Max 3 points per finding
        
        for finding in findings:
            severity = finding.get('severity', 'INFO')
            status = finding.get('status', 'UNKNOWN')
            
            if status == 'FAIL':
                if severity == 'HIGH':
                    score += 3
                elif severity == 'MEDIUM':
                    score += 2
                elif severity == 'LOW':
                    score += 1
            elif status == 'WARN':
                if severity == 'HIGH':
                    score += 2
                elif severity == 'MEDIUM':
                    score += 1
                elif severity == 'LOW':
                    score += 0.5
            elif status == 'ERROR':
                score += 1  # Errors indicate potential issues
        
        # Normalize score to 0-100
        if max_score > 0:
            normalized_score = (score / max_score) * 100
        else:
            normalized_score = 0
        
        self.audit_report['overall_score'] = round(normalized_score, 2)
        
        # Determine risk level
        if normalized_score < 20:
            risk_level = 'LOW'
        elif normalized_score < 50:
            risk_level = 'MEDIUM'
        elif normalized_score < 80:
            risk_level = 'HIGH'
        else:
            risk_level = 'CRITICAL'
        
        self.audit_report['risk_level'] = risk_level
        logger.info(f"Risk score calculated: {normalized_score:.2f} ({risk_level})")
    
    def generate_report(self):
        """Generate the complete security audit report"""
        logger.info("Generating security audit report...")
        
        # Run all checks
        self.check_system_security()
        self.check_network_security()
        self.check_application_security()
        self.check_data_protection()
        self.check_compliance()
        self.generate_recommendations()
        self.calculate_risk_score()
        
        # Save report to file
        report_file = f"/home/ubuntu/dev/atlas/logs/security_audit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(self.audit_report, f, indent=2)
        
        logger.info(f"Security audit report saved to {report_file}")
        return self.audit_report
    
    def print_summary(self):
        """Print a human-readable summary of the audit"""
        print("\n" + "="*60)
        print("ATLAS PRODUCTION SECURITY AUDIT REPORT")
        print("="*60)
        print(f"Generated: {self.audit_report['timestamp']}")
        print(f"Overall Risk Score: {self.audit_report['overall_score']}/100")
        print(f"Risk Level: {self.audit_report['risk_level']}")
        
        # Summary of findings
        findings = self.audit_report['findings']
        total_findings = len(findings)
        
        # Categorize findings
        passed = len([f for f in findings if f.get('status') == 'PASS'])
        failed = len([f for f in findings if f.get('status') == 'FAIL'])
        warnings = len([f for f in findings if f.get('status') == 'WARN'])
        errors = len([f for f in findings if f.get('status') == 'ERROR'])
        
        print(f"\nFindings Summary:")
        print(f"  Total Checks: {total_findings}")
        print(f"  Passed: {passed}")
        print(f"  Failed: {failed}")
        print(f"  Warnings: {warnings}")
        print(f"  Errors: {errors}")
        
        # Breakdown by severity
        high_severity = len([f for f in findings if f.get('severity') == 'HIGH'])
        medium_severity = len([f for f in findings if f.get('severity') == 'MEDIUM'])
        low_severity = len([f for f in findings if f.get('severity') == 'LOW'])
        
        print(f"\nSeverity Breakdown:")
        print(f"  High: {high_severity}")
        print(f"  Medium: {medium_severity}")
        print(f"  Low: {low_severity}")
        print(f"  Info: {len(findings) - high_severity - medium_severity - low_severity}")
        
        # Detailed findings
        print(f"\nDetailed Findings:")
        for i, finding in enumerate(findings, 1):
            status_icon = {
                'PASS': '✅',
                'FAIL': '❌',
                'WARN': '⚠️',
                'ERROR': '💥'
            }.get(finding.get('status', 'UNKNOWN'), '❓')
            
            print(f"  {i}. {status_icon} [{finding.get('severity', 'INFO')}] {finding.get('description', 'No description')}")
            if finding.get('status') in ['FAIL', 'WARN', 'ERROR'] and finding.get('recommendation'):
                print(f"      🔧 Recommendation: {finding.get('recommendation')}")
        
        # Recommendations
        print(f"\nRecommendations:")
        recommendations = self.audit_report['recommendations']
        for i, rec in enumerate(recommendations, 1):
            priority_icon = {
                'HIGH': '🔴',
                'MEDIUM': '🟡',
                'LOW': '🟢'
            }.get(rec.get('priority', 'LOW'), '🔵')
            
            print(f"  {i}. {priority_icon} {rec.get('description', 'No description')}")
            if rec.get('actions'):
                for action in rec.get('actions', []):
                    print(f"      • {action}")
        
        print("\n" + "="*60)
        
        # Final assessment
        risk_level = self.audit_report['risk_level']
        if risk_level == 'LOW':
            print("✅ SECURITY ASSESSMENT: GOOD")
            print("   The system has a low security risk profile.")
        elif risk_level == 'MEDIUM':
            print("⚠️ SECURITY ASSESSMENT: MODERATE")
            print("   The system has a moderate security risk profile. Review recommendations.")
        elif risk_level == 'HIGH':
            print("❌ SECURITY ASSESSMENT: HIGH RISK")
            print("   The system has a high security risk profile. Address critical issues immediately.")
        else:
            print("💥 SECURITY ASSESSMENT: CRITICAL")
            print("   The system has a critical security risk profile. Take immediate action.")

def main():
    """Main function"""
    print("Atlas Production Security Audit")
    print("=" * 35)
    
    # Create and run audit
    auditor = AtlasSecurityAudit()
    report = auditor.generate_report()
    auditor.print_summary()
    
    # Return appropriate exit code based on risk level
    risk_level = report['risk_level']
    if risk_level == 'LOW':
        return 0
    elif risk_level == 'MEDIUM':
        return 1
    elif risk_level == 'HIGH':
        return 2
    else:
        return 3

if __name__ == "__main__":
    sys.exit(main())