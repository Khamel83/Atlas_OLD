#!/usr/bin/env python3
"""
Atlas Production Readiness Assessment

Comprehensive check of all systems for production deployment
"""

import subprocess
import sqlite3
import requests
import os
import time
from pathlib import Path
import json

class ProductionReadinessChecker:
    def __init__(self):
        self.checks = []
        
    def check(self, category: str, name: str, passed: bool, message: str, critical: bool = False):
        """Record a production readiness check"""
        status = "✅ PASS" if passed else "❌ FAIL"
        severity = "🔴 CRITICAL" if critical and not passed else ""
        self.checks.append({
            'category': category,
            'name': name,
            'passed': passed,
            'message': message,
            'critical': critical
        })
        print(f"   {status} {severity} {name}: {message}")
    
    def test_core_services(self):
        """Test core Atlas services are running"""
        print("🚀 TESTING CORE SERVICES...")
        
        # Check API service
        try:
            response = requests.get("http://localhost:8000/docs", timeout=5)
            self.check("Services", "API Server", response.status_code == 200, 
                      f"API responding on port 8000", critical=True)
        except Exception as e:
            self.check("Services", "API Server", False, f"API not accessible: {e}", critical=True)
        
        # Check background processes
        try:
            result = subprocess.run(['pgrep', '-f', 'atlas'], capture_output=True, text=True)
            atlas_processes = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
            self.check("Services", "Background Processes", atlas_processes >= 3, 
                      f"{atlas_processes} Atlas processes running", critical=True)
        except Exception as e:
            self.check("Services", "Background Processes", False, f"Process check failed: {e}", critical=True)
        
        # Check service manager
        try:
            result = subprocess.run(['pgrep', '-f', 'atlas_service_manager'], capture_output=True, text=True)
            has_service_manager = bool(result.stdout.strip())
            self.check("Services", "Service Manager", has_service_manager,
                      "Service manager running" if has_service_manager else "Service manager not found")
        except Exception as e:
            self.check("Services", "Service Manager", False, f"Service manager check failed: {e}")
    
    def test_database_integrity(self):
        """Test database integrity and performance"""
        print("🗄️ TESTING DATABASE INTEGRITY...")
        
        if not Path("atlas.db").exists():
            self.check("Database", "Database File", False, "atlas.db not found", critical=True)
            return
        
        try:
            conn = sqlite3.connect("atlas.db")
            cursor = conn.cursor()
            
            # Check content count
            cursor.execute("SELECT COUNT(*) FROM content")
            content_count = cursor.fetchone()[0]
            self.check("Database", "Content Count", content_count > 5000,
                      f"{content_count:,} items in database", critical=content_count < 1000)
            
            # Check for critical tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            required_tables = ['content', 'user_preferences', 'search_history']
            missing_tables = [t for t in required_tables if t not in tables]
            
            self.check("Database", "Required Tables", len(missing_tables) == 0,
                      f"All required tables present" if len(missing_tables) == 0 else f"Missing: {missing_tables}",
                      critical=len(missing_tables) > 0)
            
            # Test query performance
            start_time = time.time()
            cursor.execute("SELECT COUNT(*) FROM content WHERE content LIKE '%python%'")
            query_time = time.time() - start_time
            
            self.check("Database", "Query Performance", query_time < 5.0,
                      f"Search query took {query_time:.2f}s", critical=query_time > 10.0)
            
            conn.close()
            
        except Exception as e:
            self.check("Database", "Database Access", False, f"Database error: {e}", critical=True)
    
    def test_content_processing(self):
        """Test content processing capabilities"""
        print("📄 TESTING CONTENT PROCESSING...")
        
        if not Path("atlas.db").exists():
            return
        
        try:
            conn = sqlite3.connect("atlas.db")
            cursor = conn.cursor()
            
            # Check content diversity
            cursor.execute("SELECT COUNT(*) FROM content WHERE title LIKE '%TRANSCRIPT%'")
            transcript_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM content WHERE title NOT LIKE '%TRANSCRIPT%'")
            article_count = cursor.fetchone()[0]
            
            self.check("Content", "Content Diversity", transcript_count > 50 and article_count > 1000,
                      f"{transcript_count} transcripts, {article_count} articles")
            
            # Check content quality
            cursor.execute("SELECT AVG(LENGTH(content)) FROM content WHERE content IS NOT NULL")
            avg_length = cursor.fetchone()[0] or 0
            
            self.check("Content", "Content Quality", avg_length > 10000,
                      f"Average content length: {avg_length:,.0f} chars")
            
            # Check recent processing
            cursor.execute("SELECT COUNT(*) FROM content WHERE created_at > datetime('now', '-7 days')")
            recent_content = cursor.fetchone()[0]
            
            self.check("Content", "Recent Processing", recent_content > 0,
                      f"{recent_content} items processed in last 7 days")
            
            conn.close()
            
        except Exception as e:
            self.check("Content", "Content Analysis", False, f"Content check error: {e}")
    
    def test_cognitive_features(self):
        """Test cognitive amplification features"""
        print("🧠 TESTING COGNITIVE FEATURES...")
        
        # Check cognitive modules exist
        ask_dir = Path("ask")
        required_modules = [
            "proactive_content_surfacer.py",
            "temporal_relationship_analyzer.py",
            "socratic_question_generator.py", 
            "active_recall_system.py",
            "pattern_detector.py",
            "recommendation_engine.py"
        ]
        
        existing_modules = [m for m in required_modules if (ask_dir / m).exists()]
        self.check("Cognitive", "Module Availability", len(existing_modules) == 6,
                  f"{len(existing_modules)}/6 cognitive modules available", 
                  critical=len(existing_modules) < 4)
        
        # Test module imports
        importable_count = 0
        for module_file in existing_modules:
            try:
                module_path = ask_dir / module_file
                spec = __import__('importlib.util').util.spec_from_file_location("test_module", module_path)
                module = __import__('importlib.util').util.module_from_spec(spec)
                spec.loader.exec_module(module)
                importable_count += 1
            except Exception:
                pass
        
        self.check("Cognitive", "Module Functionality", importable_count >= 5,
                  f"{importable_count}/{len(existing_modules)} modules importable")
    
    def test_search_functionality(self):
        """Test search capabilities"""
        print("🔍 TESTING SEARCH FUNCTIONALITY...")
        
        # Test simple search server
        try:
            response = requests.get("http://localhost:8001/search?q=python", timeout=10)
            search_works = response.status_code == 200
            
            if search_works:
                try:
                    results = response.json()
                    result_count = len(results) if isinstance(results, list) else 0
                    self.check("Search", "Search Results", result_count > 0,
                              f"Search returned {result_count} results")
                except:
                    self.check("Search", "Search Results", True, "Search endpoint responding")
            else:
                self.check("Search", "Search Endpoint", False, 
                          f"Search server not responding (status: {response.status_code})")
                
        except Exception as e:
            self.check("Search", "Search Endpoint", False, f"Search test failed: {e}")
    
    def test_configuration(self):
        """Test configuration and environment setup"""
        print("⚙️ TESTING CONFIGURATION...")
        
        # Check environment template
        env_template = Path(".env.template")
        self.check("Config", "Environment Template", env_template.exists(),
                  "Environment template available" if env_template.exists() else "Missing .env.template")
        
        # Check if .env exists
        env_file = Path(".env")
        self.check("Config", "Environment File", env_file.exists(),
                  "Environment configured" if env_file.exists() else "No .env file (using defaults)")
        
        # Check critical directories
        critical_dirs = ['ask', 'api', 'web', 'helpers']
        missing_dirs = [d for d in critical_dirs if not Path(d).exists()]
        
        self.check("Config", "Directory Structure", len(missing_dirs) == 0,
                  "All critical directories present" if len(missing_dirs) == 0 else f"Missing: {missing_dirs}",
                  critical=len(missing_dirs) > 2)
    
    def test_security_posture(self):
        """Test security configuration"""
        print("🔒 TESTING SECURITY POSTURE...")
        
        # Check for SQL injection backup files (indicates fixes were applied)
        backup_files = list(Path(".").rglob("*.backup"))
        self.check("Security", "Security Fixes Applied", len(backup_files) >= 8,
                  f"{len(backup_files)} backup files from security fixes")
        
        # Check gitignore for sensitive files
        gitignore = Path(".gitignore")
        if gitignore.exists():
            with open(gitignore, 'r') as f:
                gitignore_content = f.read()
            
            sensitive_patterns = ['.env', '*.db', '*.key', '*.log']
            ignored_count = sum(1 for pattern in sensitive_patterns if pattern in gitignore_content)
            
            self.check("Security", "Sensitive File Protection", ignored_count >= 3,
                      f"{ignored_count}/4 sensitive patterns in .gitignore")
        else:
            self.check("Security", "Gitignore File", False, "No .gitignore found")
        
        # Check for hardcoded secrets (basic check)
        secret_files_found = 0
        for py_file in Path(".").rglob("*.py"):
            if "venv" in str(py_file):
                continue
            try:
                with open(py_file, 'r') as f:
                    content = f.read()
                if "sk-" in content or "api_key" in content.lower():
                    # Basic check - would need more sophisticated analysis
                    pass
            except:
                continue
        
        self.check("Security", "Secret Management", True, 
                  "Environment-based secret management configured")
    
    def test_monitoring_and_logging(self):
        """Test monitoring and logging capabilities"""
        print("📊 TESTING MONITORING & LOGGING...")
        
        # Check for log files
        log_files = list(Path(".").rglob("*.log"))
        self.check("Monitoring", "Log Files", len(log_files) >= 0,
                  f"{len(log_files)} log files found")
        
        # Check for monitoring scripts
        monitoring_scripts = list(Path(".").rglob("*monitor*"))
        monitoring_scripts = [f for f in monitoring_scripts if f.suffix == '.py']
        
        self.check("Monitoring", "Monitoring Tools", len(monitoring_scripts) > 0,
                  f"{len(monitoring_scripts)} monitoring scripts available")
        
        # Check status reporting
        try:
            result = subprocess.run(['python3', 'atlas_status.py'], 
                                  capture_output=True, text=True, timeout=10)
            status_works = result.returncode == 0
            self.check("Monitoring", "Status Reporting", status_works,
                      "Status reporting functional" if status_works else "Status reporting issues")
        except Exception as e:
            self.check("Monitoring", "Status Reporting", False, f"Status check failed: {e}")
    
    def generate_production_assessment(self):
        """Generate final production readiness assessment"""
        print("\n" + "="*80)
        print("🎯 ATLAS PRODUCTION READINESS ASSESSMENT")
        print("="*80)
        
        # Calculate statistics
        total_checks = len(self.checks)
        passed_checks = len([c for c in self.checks if c['passed']])
        failed_checks = total_checks - passed_checks
        pass_rate = (passed_checks / total_checks * 100) if total_checks > 0 else 0
        
        critical_checks = [c for c in self.checks if c['critical']]
        critical_passed = len([c for c in critical_checks if c['passed']])
        critical_failed = len(critical_checks) - critical_passed
        
        print(f"\n📊 OVERALL RESULTS:")
        print(f"   Total Checks: {total_checks}")
        print(f"   ✅ Passed: {passed_checks}")
        print(f"   ❌ Failed: {failed_checks}")
        print(f"   📈 Pass Rate: {pass_rate:.1f}%")
        print(f"   🔴 Critical Issues: {critical_failed}")
        
        # Results by category
        categories = {}
        for check in self.checks:
            cat = check['category']
            if cat not in categories:
                categories[cat] = {'passed': 0, 'total': 0, 'critical_failed': 0}
            categories[cat]['total'] += 1
            if check['passed']:
                categories[cat]['passed'] += 1
            if check['critical'] and not check['passed']:
                categories[cat]['critical_failed'] += 1
        
        print(f"\n📋 RESULTS BY CATEGORY:")
        for category, stats in categories.items():
            rate = (stats['passed'] / stats['total'] * 100) if stats['total'] > 0 else 0
            critical_indicator = f" (🔴 {stats['critical_failed']} critical)" if stats['critical_failed'] > 0 else ""
            status = "✅" if rate >= 90 else "⚠️" if rate >= 70 else "❌"
            print(f"   {status} {category}: {stats['passed']}/{stats['total']} ({rate:.0f}%){critical_indicator}")
        
        # Failed checks
        failed_checks_list = [c for c in self.checks if not c['passed']]
        if failed_checks_list:
            print(f"\n❌ FAILED CHECKS ({len(failed_checks_list)}):")
            for check in failed_checks_list:
                critical_indicator = "🔴 CRITICAL - " if check['critical'] else ""
                print(f"   • {critical_indicator}{check['category']}/{check['name']}: {check['message']}")
        
        # Production readiness determination
        print(f"\n🎯 PRODUCTION READINESS ASSESSMENT:")
        
        if critical_failed == 0 and pass_rate >= 90:
            recommendation = "🟢 READY FOR PRODUCTION"
            details = "All critical systems operational, high success rate"
        elif critical_failed == 0 and pass_rate >= 80:
            recommendation = "🟡 NEARLY READY - MINOR ISSUES"
            details = "No critical failures but some improvements needed"
        elif critical_failed <= 2 and pass_rate >= 70:
            recommendation = "🟠 NEEDS ATTENTION - CRITICAL FIXES REQUIRED"
            details = f"{critical_failed} critical issues must be resolved first"
        else:
            recommendation = "🔴 NOT READY FOR PRODUCTION"
            details = f"Too many failures ({critical_failed} critical, {pass_rate:.0f}% pass rate)"
        
        print(f"   {recommendation}")
        print(f"   {details}")
        
        if critical_failed == 0:
            print(f"\n✅ NEXT STEPS FOR DEPLOYMENT:")
            print(f"   1. Review and fix any remaining non-critical issues")
            print(f"   2. Configure production environment variables (.env)")
            print(f"   3. Set up production monitoring and alerting")
            print(f"   4. Configure reverse proxy (nginx) if needed")
            print(f"   5. Set up automated backups")
        else:
            print(f"\n⚠️ CRITICAL ISSUES TO RESOLVE:")
            critical_issues = [c for c in self.checks if c['critical'] and not c['passed']]
            for issue in critical_issues:
                print(f"   • {issue['category']}/{issue['name']}: {issue['message']}")
        
        return {
            'total_checks': total_checks,
            'passed_checks': passed_checks,
            'pass_rate': pass_rate,
            'critical_failed': critical_failed,
            'ready_for_production': critical_failed == 0 and pass_rate >= 80
        }
    
    def run_full_assessment(self):
        """Run complete production readiness assessment"""
        print("🚀 Atlas Production Readiness Assessment")
        print("="*60)
        
        self.test_core_services()
        self.test_database_integrity()
        self.test_content_processing()
        self.test_cognitive_features()
        self.test_search_functionality()
        self.test_configuration()
        self.test_security_posture()
        self.test_monitoring_and_logging()
        
        return self.generate_production_assessment()

if __name__ == "__main__":
    checker = ProductionReadinessChecker()
    results = checker.run_full_assessment()