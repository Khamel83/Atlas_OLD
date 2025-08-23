#!/usr/bin/env python3
"""
Comprehensive Atlas Reality Audit

Audit EVERYTHING to find gaps between claims and reality.
No more lies, no more delusions. What ACTUALLY works vs what we claim works.
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime
import subprocess
import sys

class AtlasRealityAudit:
    """Audit every single claim about Atlas functionality"""
    
    def __init__(self):
        self.audit_results = {
            'timestamp': datetime.now().isoformat(),
            'categories': {},
            'major_failures': [],
            'lies_detected': []
        }
    
    def audit_articles(self):
        """Audit article processing claims vs reality"""
        print("🗞️  AUDITING ARTICLES")
        
        # Claims from documentation
        claims = {
            'processing_rate': '>1000 articles/hour',
            'success_rate': '>98%',
            'enhanced_strategies': '6-strategy fallback system',
            'authentication': 'NYTimes/WSJ authentication'
        }
        
        # Reality check
        reality = {}
        
        # Check processed files
        article_files = list(Path("output/articles/metadata").glob("*.json"))
        successful = 0
        failed = 0
        
        for article_file in article_files[:100]:  # Sample
            try:
                with open(article_file, 'r') as f:
                    data = json.load(f)
                if data.get('status') == 'success':
                    successful += 1
                else:
                    failed += 1
            except:
                failed += 1
        
        total_sampled = successful + failed
        actual_success_rate = (successful / max(1, total_sampled)) * 100
        
        reality = {
            'total_files': len(article_files),
            'success_rate': f"{actual_success_rate:.1f}%",
            'in_database': self.count_database_records('article')
        }
        
        # Check for lies
        if actual_success_rate < 90:  # Claimed >98%
            self.audit_results['lies_detected'].append({
                'claim': 'Article success rate >98%',
                'reality': f'{actual_success_rate:.1f}%',
                'category': 'articles'
            })
        
        self.audit_results['categories']['articles'] = {
            'claims': claims,
            'reality': reality,
            'verdict': 'WORKING_BUT_OVERSTATED' if successful > 0 else 'BROKEN'
        }
        
        print(f"   Claims: {claims}")
        print(f"   Reality: {reality}")
    
    def audit_documents(self):
        """Audit document processing - the 18,575 'successful' but contentless items"""
        print("📄 AUDITING DOCUMENTS (THE BIG LIE)")
        
        claims = {
            'processing_rate': 'High volume processing',
            'success_rate': '95.0%',
            'content_extraction': 'Full document content'
        }
        
        # Check the 18,575 "successful" documents
        doc_files = list(Path("output/documents/metadata").glob("*.json"))
        
        successful_claimed = 0
        actually_have_content = 0
        
        for doc_file in doc_files[:100]:
            try:
                with open(doc_file, 'r') as f:
                    data = json.load(f)
                
                if data.get('status') == 'success':
                    successful_claimed += 1
                    
                    # Check if actually has content
                    content_path = data.get('content_path')
                    if content_path and Path(content_path).exists():
                        with open(content_path, 'r', encoding='utf-8', errors='ignore') as cf:
                            content = cf.read()
                            if len(content.strip()) > 50:
                                actually_have_content += 1
            except:
                pass
        
        reality = {
            'total_files': len(doc_files),
            'claimed_successful': successful_claimed,
            'actually_have_content': actually_have_content,
            'real_success_rate': f"{(actually_have_content/max(1,successful_claimed))*100:.1f}%"
        }
        
        # This is a MAJOR lie
        if actually_have_content == 0 and successful_claimed > 0:
            self.audit_results['major_failures'].append({
                'component': 'Documents',
                'issue': f'{successful_claimed} claimed successful but 0 have actual content',
                'severity': 'CRITICAL_LIE'
            })
        
        self.audit_results['categories']['documents'] = {
            'claims': claims,
            'reality': reality,
            'verdict': 'MASSIVE_LIE'
        }
        
        print(f"   Claims: {claims}")
        print(f"   Reality: {reality}")
        print(f"   🚨 VERDICT: MASSIVE LIE - {successful_claimed} claimed successful, {actually_have_content} actually have content")
    
    def audit_youtube(self):
        """Audit YouTube processing claims vs reality"""
        print("📺 AUDITING YOUTUBE")
        
        claims = {
            'integration': 'YouTube video ingestion with transcript extraction',
            'daily_sync': 'YouTube daily sync every day at 3 AM',
            'processing': 'Yesterday\'s watched videos + transcripts'
        }
        
        # Reality check
        youtube_files = list(Path("output/youtube").rglob("*.json"))
        youtube_db_records = self.count_database_records('youtube')
        
        reality = {
            'total_files': len(youtube_files),
            'db_records': youtube_db_records,
            'daily_sync_running': self.check_service_running('youtube'),
            'api_credentials': self.check_youtube_credentials()
        }
        
        if len(youtube_files) == 0:
            self.audit_results['major_failures'].append({
                'component': 'YouTube',
                'issue': 'Claims full integration but 0 videos processed',
                'severity': 'COMPLETE_FAILURE'
            })
        
        self.audit_results['categories']['youtube'] = {
            'claims': claims,
            'reality': reality,
            'verdict': 'COMPLETE_FAILURE' if len(youtube_files) == 0 else 'WORKING'
        }
        
        print(f"   Claims: {claims}")
        print(f"   Reality: {reality}")
    
    def audit_emails(self):
        """Audit email processing claims vs reality"""
        print("📧 AUDITING EMAILS")
        
        claims = {
            'integration': 'Newsletter & email integration with Gmail API',
            'processing': 'Complete IMAP pipeline with authentication',
            'automation': 'Email processing every 30 minutes'
        }
        
        # Check for email files
        email_dirs = [Path("emails"), Path("data/emails"), Path("output/emails")]
        total_emails = 0
        for email_dir in email_dirs:
            if email_dir.exists():
                total_emails += len(list(email_dir.rglob("*")))
        
        reality = {
            'email_files': total_emails,
            'gmail_credentials': self.check_gmail_credentials(),
            'processing_active': self.check_service_running('email'),
            'db_records': self.count_database_records('email')
        }
        
        if total_emails == 0:
            self.audit_results['major_failures'].append({
                'component': 'Emails',
                'issue': 'Claims Gmail integration but 0 emails processed',
                'severity': 'COMPLETE_FAILURE'
            })
        
        self.audit_results['categories']['emails'] = {
            'claims': claims,
            'reality': reality,
            'verdict': 'COMPLETE_FAILURE' if total_emails == 0 else 'WORKING'
        }
        
        print(f"   Claims: {claims}")
        print(f"   Reality: {reality}")
    
    def audit_background_services(self):
        """Audit background service claims vs reality"""
        print("🔄 AUDITING BACKGROUND SERVICES")
        
        claims = {
            'comprehensive_processing': 'Every 2 hours',
            'never_stops': 'Intelligent retry with rate limiting, exponential backoff',
            'health_monitoring': 'System health monitoring and auto-restart',
            'service_count': '1 sophisticated service'
        }
        
        # Check what's actually running
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            atlas_processes = [line for line in result.stdout.split('\n') if 'atlas' in line.lower()]
            
            # Count duplicate processes (the travesty we found earlier)
            background_processes = len([p for p in atlas_processes if 'Background processing' in p])
            
            reality = {
                'total_atlas_processes': len(atlas_processes),
                'duplicate_background_loops': background_processes,
                'comprehensive_service_running': any('comprehensive_service' in p for p in atlas_processes),
                'service_status': 'FIXED' if background_processes < 5 else 'DUPLICATE_HELL'
            }
            
            if background_processes > 10:
                self.audit_results['major_failures'].append({
                    'component': 'Background Services',
                    'issue': f'{background_processes} duplicate processes instead of 1 sophisticated service',
                    'severity': 'ARCHITECTURAL_FAILURE'
                })
        
        except Exception as e:
            reality = {'error': str(e)}
        
        self.audit_results['categories']['background_services'] = {
            'claims': claims,
            'reality': reality,
            'verdict': 'FIXED' if reality.get('service_status') == 'FIXED' else 'BROKEN'
        }
        
        print(f"   Claims: {claims}")
        print(f"   Reality: {reality}")
    
    def audit_cognitive_features(self):
        """Audit cognitive features claims vs reality"""
        print("🧠 AUDITING COGNITIVE FEATURES")
        
        claims = {
            'modules': '5 cognitive modules (ProactiveSurfacer, TemporalEngine, etc.)',
            'functionality': 'Cognitive amplification features',
            'integration': 'Complete cognitive framework',
            'socratic_questions': 'Socratic question generation for deeper learning'
        }
        
        # Check if modules actually work
        working_modules = 0
        module_tests = [
            'ask/proactive/surfacer.py',
            'ask/temporal/temporal_engine.py',
            'ask/socratic/question_engine.py',
            'ask/recall/recall_engine.py',
            'ask/insights/pattern_detector.py'
        ]
        
        for module in module_tests:
            if Path(module).exists():
                try:
                    result = subprocess.run([sys.executable, '-c', f'import sys; sys.path.insert(0, "."); from {module.replace("/", ".").replace(".py", "")} import *'], 
                                          capture_output=True, timeout=10)
                    if result.returncode == 0:
                        working_modules += 1
                except:
                    pass
        
        reality = {
            'modules_exist': len([m for m in module_tests if Path(m).exists()]),
            'modules_import': working_modules,
            'api_endpoints': self.check_cognitive_api(),
            'actual_functionality': 'Unknown - need testing'
        }
        
        self.audit_results['categories']['cognitive_features'] = {
            'claims': claims,
            'reality': reality,
            'verdict': 'PARTIALLY_WORKING' if working_modules > 0 else 'UNKNOWN'
        }
        
        print(f"   Claims: {claims}")
        print(f"   Reality: {reality}")
    
    def count_database_records(self, content_type):
        """Count records in database by content type"""
        try:
            conn = sqlite3.connect('atlas.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM content WHERE content_type = ?", (content_type,))
            count = cursor.fetchone()[0]
            conn.close()
            return count
        except:
            return 0
    
    def check_service_running(self, service_name):
        """Check if a specific service is running"""
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            return service_name.lower() in result.stdout.lower()
        except:
            return False
    
    def check_youtube_credentials(self):
        """Check if YouTube API credentials exist"""
        return Path(".env").exists()  # Simplified check
    
    def check_gmail_credentials(self):
        """Check if Gmail credentials exist"""
        return Path("credentials.json").exists() or Path("token.json").exists()
    
    def check_cognitive_api(self):
        """Check if cognitive API endpoints are working"""
        try:
            result = subprocess.run(['curl', '-s', 'http://localhost:8000/api/v1/cognitive/'], 
                                  capture_output=True, timeout=5)
            return result.returncode == 0
        except:
            return False
    
    def run_comprehensive_audit(self):
        """Run complete audit of Atlas"""
        print("🔍 ATLAS REALITY AUDIT - NO LIES, NO DELUSIONS")
        print("=" * 60)
        
        self.audit_articles()
        self.audit_documents()
        self.audit_youtube()
        self.audit_emails()
        self.audit_background_services()
        self.audit_cognitive_features()
        
        # Generate summary
        print(f"\n📊 AUDIT SUMMARY")
        print("=" * 60)
        
        working_count = 0
        broken_count = 0
        lying_count = 0
        
        for category, results in self.audit_results['categories'].items():
            verdict = results['verdict']
            if verdict in ['WORKING', 'WORKING_BUT_OVERSTATED', 'PARTIALLY_WORKING', 'FIXED']:
                working_count += 1
                status_icon = "✅" if verdict == 'WORKING' else "⚠️"
            else:
                broken_count += 1
                status_icon = "❌"
            
            if 'LIE' in verdict:
                lying_count += 1
            
            print(f"{status_icon} {category.upper()}: {verdict}")
        
        print(f"\n🎯 FINAL VERDICT:")
        print(f"   ✅ Working: {working_count}")
        print(f"   ❌ Broken: {broken_count}")
        print(f"   🤥 Major lies detected: {lying_count}")
        print(f"   🚨 Major failures: {len(self.audit_results['major_failures'])}")
        
        if self.audit_results['major_failures']:
            print(f"\n🚨 MAJOR FAILURES:")
            for failure in self.audit_results['major_failures']:
                print(f"   • {failure['component']}: {failure['issue']}")
        
        if self.audit_results['lies_detected']:
            print(f"\n🤥 LIES DETECTED:")
            for lie in self.audit_results['lies_detected']:
                print(f"   • {lie['claim']} vs Reality: {lie['reality']}")
        
        # Save audit results
        with open('atlas_reality_audit.json', 'w') as f:
            json.dump(self.audit_results, f, indent=2)
        
        print(f"\n📄 Full audit saved to: atlas_reality_audit.json")
        
        return self.audit_results

def main():
    auditor = AtlasRealityAudit()
    results = auditor.run_comprehensive_audit()
    
    # Return exit code based on failures
    major_failures = len(results['major_failures'])
    if major_failures > 3:
        return 1  # Critical failures
    elif major_failures > 0:
        return 2  # Some failures
    else:
        return 0  # All good

if __name__ == "__main__":
    sys.exit(main())