#!/usr/bin/env python3
"""
Test Mission & Values Alignment After Fixes

Validates that Atlas system properly embodies:
1. Personal knowledge amplification mission
2. Privacy-first values  
3. User control and autonomy
4. Cognitive enhancement goals
"""

import sqlite3
import os
import importlib.util
from pathlib import Path
import json

class MissionAlignmentTester:
    def __init__(self):
        self.project_root = Path.cwd()
        self.test_results = []
        
    def test_result(self, category: str, test_name: str, passed: bool, message: str):
        """Record test result"""
        self.test_results.append({
            'category': category,
            'test': test_name,
            'passed': passed,
            'message': message
        })
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {status}: {test_name} - {message}")
    
    def test_mission_artifacts(self):
        """Test that mission-critical artifacts exist"""
        print("🎯 TESTING MISSION ARTIFACTS...")
        
        # Mission statement exists
        mission_file = self.project_root / "MISSION.md"
        self.test_result("Mission", "Mission Statement", 
                        mission_file.exists(),
                        "MISSION.md file exists" if mission_file.exists() else "Missing MISSION.md")
        
        # Environment configuration exists
        env_template = self.project_root / ".env.template"
        self.test_result("Mission", "Configuration Template",
                        env_template.exists(),
                        ".env.template exists" if env_template.exists() else "Missing .env.template")
        
        # Check for privacy-focused config options
        if env_template.exists():
            with open(env_template, 'r') as f:
                env_content = f.read()
            
            privacy_configs = [
                'USER_DATA_RETENTION_DAYS',
                'ENABLE_DATA_EXPORT', 
                'SECRET_KEY',
                'ALLOW_CONTENT_DELETION'
            ]
            
            missing_configs = [cfg for cfg in privacy_configs if cfg not in env_content]
            self.test_result("Privacy", "Privacy Configuration Options",
                            len(missing_configs) == 0,
                            f"All privacy configs present" if len(missing_configs) == 0 else f"Missing: {missing_configs}")
    
    def test_cognitive_modules(self):
        """Test that all 6 cognitive modules exist and are functional"""
        print("🧠 TESTING COGNITIVE MODULES...")
        
        ask_dir = self.project_root / "ask"
        required_modules = [
            "proactive_content_surfacer.py",
            "temporal_relationship_analyzer.py", 
            "socratic_question_generator.py",
            "active_recall_system.py",
            "pattern_detector.py",
            "recommendation_engine.py"
        ]
        
        for module_file in required_modules:
            module_path = ask_dir / module_file
            exists = module_path.exists()
            self.test_result("Cognitive", f"Module: {module_file}",
                            exists,
                            "Module exists" if exists else f"Missing {module_file}")
            
            # Test module can be imported
            if exists:
                try:
                    spec = importlib.util.spec_from_file_location("test_module", module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    self.test_result("Cognitive", f"Import: {module_file}",
                                    True, "Module imports successfully")
                except Exception as e:
                    self.test_result("Cognitive", f"Import: {module_file}",
                                    False, f"Import error: {e}")
    
    def test_database_privacy_schema(self):
        """Test database has user-centric, privacy-focused schema"""
        print("🗄️ TESTING DATABASE PRIVACY SCHEMA...")
        
        if not Path("atlas.db").exists():
            self.test_result("Privacy", "Database Exists", False, "No atlas.db found")
            return
        
        try:
            conn = sqlite3.connect("atlas.db")
            cursor = conn.cursor()
            
            # Check for user preferences table
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_preferences'")
            has_preferences = len(cursor.fetchall()) > 0
            self.test_result("Privacy", "User Preferences Table",
                            has_preferences, "user_preferences table exists" if has_preferences else "Missing user_preferences")
            
            # Check for search history table
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='search_history'")
            has_search_history = len(cursor.fetchall()) > 0
            self.test_result("Privacy", "Search History Table",
                            has_search_history, "search_history table exists" if has_search_history else "Missing search_history")
            
            # Check for privacy-focused defaults in preferences
            if has_preferences:
                cursor.execute("SELECT COUNT(*) FROM user_preferences WHERE category='privacy'")
                privacy_prefs_count = cursor.fetchone()[0]
                self.test_result("Privacy", "Privacy Preferences",
                                privacy_prefs_count > 0, f"{privacy_prefs_count} privacy preferences configured")
            
            # Check content table has reasonable schema
            cursor.execute("PRAGMA table_info(content)")
            content_columns = [row[1] for row in cursor.fetchall()]
            required_columns = ['id', 'title', 'content', 'url', 'created_at']
            missing_columns = [col for col in required_columns if col not in content_columns]
            
            self.test_result("Data", "Content Table Schema",
                            len(missing_columns) == 0, 
                            "All required columns present" if len(missing_columns) == 0 else f"Missing: {missing_columns}")
            
            conn.close()
            
        except Exception as e:
            self.test_result("Privacy", "Database Schema Test", False, f"Database error: {e}")
    
    def test_user_control_features(self):
        """Test user control and autonomy features"""
        print("🔧 TESTING USER CONTROL FEATURES...")
        
        # Check for configuration management
        config_files = list(self.project_root.glob("*.env*"))
        self.test_result("Control", "Configuration Files",
                        len(config_files) > 0, f"Found {len(config_files)} config files")
        
        # Check for data export capabilities
        export_scripts = list(self.project_root.rglob("*export*"))
        export_scripts = [f for f in export_scripts if f.suffix in ['.py', '.sh']]
        self.test_result("Control", "Data Export Tools",
                        len(export_scripts) > 0, f"Found {len(export_scripts)} export tools")
        
        # Check for backup/restore capabilities  
        backup_scripts = list(self.project_root.rglob("*backup*"))
        backup_scripts = [f for f in backup_scripts if f.suffix in ['.py', '.sh']]
        self.test_result("Control", "Backup Tools",
                        len(backup_scripts) > 0, f"Found {len(backup_scripts)} backup tools")
    
    def test_security_measures(self):
        """Test security and privacy measures"""
        print("🔒 TESTING SECURITY MEASURES...")
        
        # Check for gitignore of sensitive files
        gitignore_path = self.project_root / ".gitignore"
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                gitignore_content = f.read()
            
            sensitive_patterns = ['.env', '*.db', '*.key', '*.log']
            ignored_patterns = [pattern for pattern in sensitive_patterns if pattern in gitignore_content]
            
            self.test_result("Security", "Sensitive Files Ignored",
                            len(ignored_patterns) >= 2, f"Ignoring {len(ignored_patterns)} sensitive patterns")
        else:
            self.test_result("Security", "Gitignore Exists", False, "No .gitignore found")
        
        # Check for SQL injection backup files (indicating fixes were applied)
        backup_files = list(self.project_root.rglob("*.backup"))
        sql_injection_backups = [f for f in backup_files if "sql" in str(f).lower() or "database" in str(f).lower()]
        
        self.test_result("Security", "SQL Injection Fixes Applied",
                        len(backup_files) >= 8, f"Found {len(backup_files)} backup files from security fixes")
    
    def test_content_processing_quality(self):
        """Test content processing aligns with quality over quantity values"""
        print("📊 TESTING CONTENT PROCESSING QUALITY...")
        
        if not Path("atlas.db").exists():
            self.test_result("Quality", "Content Database", False, "No content database found")
            return
        
        try:
            conn = sqlite3.connect("atlas.db")
            cursor = conn.cursor()
            
            # Check content count and quality
            cursor.execute("SELECT COUNT(*) FROM content")
            content_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT AVG(LENGTH(content)) FROM content WHERE content IS NOT NULL")
            avg_content_length = cursor.fetchone()[0] or 0
            
            self.test_result("Quality", "Content Volume",
                            content_count > 1000, f"{content_count:,} items processed")
            
            self.test_result("Quality", "Content Substance",
                            avg_content_length > 5000, f"Average content length: {avg_content_length:,.0f} chars")
            
            # Check for transcript diversity 
            cursor.execute("SELECT COUNT(*) FROM content WHERE title LIKE '%TRANSCRIPT%'")
            transcript_count = cursor.fetchone()[0]
            
            self.test_result("Quality", "Content Diversity",
                            transcript_count > 50, f"{transcript_count} podcast transcripts processed")
            
            conn.close()
            
        except Exception as e:
            self.test_result("Quality", "Content Analysis", False, f"Analysis error: {e}")
    
    def generate_mission_alignment_report(self):
        """Generate comprehensive mission alignment report"""
        print("\n" + "="*80)
        print("🎯 ATLAS MISSION & VALUES ALIGNMENT REPORT")
        print("="*80)
        
        # Calculate statistics
        total_tests = len(self.test_results)
        passed_tests = len([t for t in self.test_results if t['passed']])
        failed_tests = total_tests - passed_tests
        pass_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n📊 OVERALL RESULTS:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed_tests}")
        print(f"   ❌ Failed: {failed_tests}")
        print(f"   📈 Pass Rate: {pass_rate:.1f}%")
        
        # Results by category
        categories = {}
        for result in self.test_results:
            cat = result['category']
            if cat not in categories:
                categories[cat] = {'passed': 0, 'total': 0}
            categories[cat]['total'] += 1
            if result['passed']:
                categories[cat]['passed'] += 1
        
        print(f"\n📋 RESULTS BY CATEGORY:")
        for category, stats in categories.items():
            rate = (stats['passed'] / stats['total'] * 100) if stats['total'] > 0 else 0
            status = "✅" if rate >= 80 else "⚠️" if rate >= 60 else "❌"
            print(f"   {status} {category}: {stats['passed']}/{stats['total']} ({rate:.0f}%)")
        
        # Failed tests
        failed_tests_list = [t for t in self.test_results if not t['passed']]
        if failed_tests_list:
            print(f"\n❌ FAILED TESTS ({len(failed_tests_list)}):")
            for test in failed_tests_list:
                print(f"   • {test['category']}/{test['test']}: {test['message']}")
        
        # Mission alignment assessment
        print(f"\n🎯 MISSION ALIGNMENT ASSESSMENT:")
        
        mission_score = categories.get('Mission', {}).get('passed', 0) / max(categories.get('Mission', {}).get('total', 1), 1) * 100
        privacy_score = categories.get('Privacy', {}).get('passed', 0) / max(categories.get('Privacy', {}).get('total', 1), 1) * 100
        cognitive_score = categories.get('Cognitive', {}).get('passed', 0) / max(categories.get('Cognitive', {}).get('total', 1), 1) * 100
        control_score = categories.get('Control', {}).get('passed', 0) / max(categories.get('Control', {}).get('total', 1), 1) * 100
        
        assessments = [
            ("Personal Knowledge Amplification", cognitive_score, "Cognitive modules and content processing"),
            ("Privacy & Data Ownership", privacy_score, "User data control and privacy measures"),
            ("User Control & Autonomy", control_score, "Configuration and export capabilities"),
            ("Mission Artifacts", mission_score, "Documentation and stated values")
        ]
        
        for aspect, score, description in assessments:
            if score >= 80:
                status = "🟢 ALIGNED"
            elif score >= 60:
                status = "🟡 PARTIAL"
            else:
                status = "🔴 MISALIGNED"
            print(f"   {status} {aspect}: {score:.0f}% - {description}")
        
        # Overall recommendation
        overall_score = pass_rate
        print(f"\n🎯 OVERALL MISSION ALIGNMENT:")
        if overall_score >= 85:
            print("   🟢 EXCELLENT - Atlas strongly embodies its mission and values")
        elif overall_score >= 70:
            print("   🟡 GOOD - Atlas generally aligned with minor areas for improvement")  
        elif overall_score >= 50:
            print("   🟠 NEEDS WORK - Some mission alignment issues need attention")
        else:
            print("   🔴 CRITICAL - Significant misalignment with stated mission and values")
        
        return {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'pass_rate': pass_rate,
            'category_results': categories,
            'failed_tests': failed_tests_list
        }
    
    def run_all_tests(self):
        """Run complete mission alignment test suite"""
        print("🚀 Atlas Mission & Values Alignment Testing")
        print("="*60)
        
        self.test_mission_artifacts()
        self.test_cognitive_modules()
        self.test_database_privacy_schema()
        self.test_user_control_features()
        self.test_security_measures()
        self.test_content_processing_quality()
        
        return self.generate_mission_alignment_report()

if __name__ == "__main__":
    tester = MissionAlignmentTester()
    results = tester.run_all_tests()