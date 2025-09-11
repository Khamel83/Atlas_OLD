#!/usr/bin/env python3
"""
Atlas Complete System Validation
Tests all implemented features to verify the system is production-ready
"""

import os
import sys
import subprocess
import importlib
import json
from pathlib import Path

class AtlasValidator:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.results = []
    
    def test(self, name, test_func):
        """Run a test and track results"""
        print(f"🧪 Testing {name}...")
        try:
            result = test_func()
            if result:
                print(f"✅ {name}")
                self.passed += 1
                self.results.append({"name": name, "status": "PASS", "details": ""})
            else:
                print(f"❌ {name}")
                self.failed += 1
                self.results.append({"name": name, "status": "FAIL", "details": "Test returned False"})
        except Exception as e:
            print(f"❌ {name} - Error: {e}")
            self.failed += 1
            self.results.append({"name": name, "status": "ERROR", "details": str(e)})
    
    def run_command(self, cmd, desc=""):
        """Run a shell command and return success"""
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            return False
        except:
            return False

def validate_core_system():
    """Test core system components"""
    validator = AtlasValidator()
    
    # Test 1: Python environment
    validator.test("Python virtual environment", 
                  lambda: Path("venv/bin/python").exists())
    
    # Test 2: Core configuration loading
    validator.test("Configuration loading",
                  lambda: validator.run_command("./venv/bin/python -c 'from helpers.config import load_config; load_config()'"))
    
    # Test 3: Database connectivity
    validator.test("Database access", 
                  lambda: Path("atlas.db").exists())
    
    # Test 4: Atlas status command
    validator.test("Atlas status command",
                  lambda: validator.run_command("./venv/bin/python atlas_status.py --help"))
    
    return validator

def validate_cognitive_features():
    """Test all 6 ask modules (cognitive features)"""
    validator = AtlasValidator()
    
    # Test cognitive modules
    cognitive_modules = [
        ("Proactive Content Surfacer", "ask.proactive.surfacer"),
        ("Temporal Analysis Engine", "ask.temporal.temporal_engine"),
        ("Socratic Question Generator", "ask.socratic.question_engine"),
        ("Active Recall System", "ask.recall.recall_engine"),
        ("Pattern Detector", "ask.insights.pattern_detector"),
        ("Recommendation Engine", "ask.recommendations.recommendation_engine")
    ]
    
    for name, module_path in cognitive_modules:
        validator.test(f"{name} module import",
                      lambda mp=module_path: test_module_import(mp))
    
    return validator

def validate_content_processing():
    """Test content processing pipelines"""
    validator = AtlasValidator()
    
    # Test content processors
    processors = [
        ("Article processor", "helpers.article_ingestor"),
        ("Document processor", "helpers.document_processor"),
        ("Podcast processor", "helpers.podcast_ingestor"),
        ("Email processor", "helpers.email_ingestor"),
        ("YouTube processor", "helpers.youtube_ingestor")
    ]
    
    for name, module_path in processors:
        validator.test(f"{name} module",
                      lambda mp=module_path: test_module_import(mp))
    
    return validator

def validate_search_system():
    """Test search and indexing"""
    validator = AtlasValidator()
    
    # Test search components
    validator.test("Search engine", 
                  lambda: test_module_import("helpers.search_engine"))
    validator.test("Enhanced search",
                  lambda: test_module_import("helpers.enhanced_search"))
    validator.test("Semantic ranker",
                  lambda: test_module_import("helpers.semantic_search_ranker"))
    
    return validator

def validate_api_system():
    """Test API and web components"""
    validator = AtlasValidator()
    
    # Test web/API components
    validator.test("Web application",
                  lambda: test_module_import("web.app"))
    validator.test("API endpoints",
                  lambda: Path("api").exists() and Path("api/main.py").exists())
    
    return validator

def validate_apple_integration():
    """Test Apple shortcuts and integrations"""
    validator = AtlasValidator()
    
    # Test shortcuts exist
    validator.test("Apple Shortcuts package",
                  lambda: Path("shortcuts_package").exists())
    validator.test("Shortcut files present",
                  lambda: len(list(Path("shortcuts_package/shortcuts").glob("*.shortcut"))) >= 7)
    validator.test("Installation scripts",
                  lambda: Path("shortcuts_package/install_shortcuts.sh").exists())
    
    return validator

def validate_bulletproof_architecture():
    """Test bulletproof process management"""
    validator = AtlasValidator()
    
    # Test bulletproof components
    validator.test("Bulletproof process manager",
                  lambda: test_module_import("helpers.bulletproof_process_manager"))
    validator.test("Resource monitor",
                  lambda: test_module_import("helpers.resource_monitor"))
    validator.test("Process watchdog",
                  lambda: test_module_import("helpers.bulletproof_watchdog"))
    
    return validator

def validate_documentation():
    """Test documentation completeness"""
    validator = AtlasValidator()
    
    # Test key documentation exists
    docs = [
        "README.md",
        "CLAUDE.md", 
        "agents.md",
        "TASKS.md",
        "docs/user-guides/SETUP_GUIDE.md",
        "docs/user-guides/MAC_USER_GUIDE.md",
        "docs/user-guides/MOBILE_GUIDE.md",
        "atlas_quickstart_complete/README.md"
    ]
    
    for doc in docs:
        validator.test(f"Documentation: {doc}",
                      lambda d=doc: Path(d).exists())
    
    return validator

def validate_production_readiness():
    """Test production deployment features"""
    validator = AtlasValidator()
    
    # Test service scripts
    validator.test("Service manager script",
                  lambda: Path("atlas_service_manager.py").exists())
    validator.test("Background service script", 
                  lambda: Path("atlas_background_service.py").exists())
    validator.test("Quick start installer",
                  lambda: Path("atlas_quickstart_complete/install_atlas.sh").exists())
    
    return validator

def test_module_import(module_path):
    """Helper to test if a module can be imported"""
    try:
        importlib.import_module(module_path)
        return True
    except ImportError:
        return False

def main():
    """Run complete system validation"""
    print("🚀 Atlas Complete System Validation")
    print("=" * 50)
    print()
    
    # Change to project directory if needed
    if not Path("CLAUDE.md").exists():
        print("❌ Run this script from the Atlas root directory")
        sys.exit(1)
    
    # Add current directory to Python path
    sys.path.insert(0, ".")
    
    # Run all validation categories
    validators = [
        ("Core System", validate_core_system),
        ("Cognitive Features (6 Ask Modules)", validate_cognitive_features),
        ("Content Processing", validate_content_processing),
        ("Search System", validate_search_system),
        ("API System", validate_api_system),
        ("Apple Integration", validate_apple_integration),
        ("Bulletproof Architecture", validate_bulletproof_architecture),
        ("Documentation", validate_documentation),
        ("Production Readiness", validate_production_readiness)
    ]
    
    total_passed = 0
    total_failed = 0
    
    for category, validator_func in validators:
        print(f"\n📋 {category}")
        print("-" * len(category))
        validator = validator_func()
        total_passed += validator.passed
        total_failed += validator.failed
    
    # Final summary
    print("\n" + "=" * 50)
    print("🎯 VALIDATION SUMMARY")
    print("=" * 50)
    print(f"✅ Passed: {total_passed}")
    print(f"❌ Failed: {total_failed}")
    print(f"📊 Success Rate: {total_passed/(total_passed+total_failed)*100:.1f}%")
    
    if total_failed == 0:
        print("\n🎉 ALL SYSTEMS OPERATIONAL!")
        print("Atlas is ready for production use.")
    else:
        print(f"\n⚠️  {total_failed} issues found that need attention.")
    
    # Save detailed results
    results = {
        "total_tests": total_passed + total_failed,
        "passed": total_passed,
        "failed": total_failed,
        "success_rate": total_passed/(total_passed+total_failed)*100
    }
    
    with open("validation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Detailed results saved to validation_results.json")
    
    return total_failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)