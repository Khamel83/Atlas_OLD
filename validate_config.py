#!/usr/bin/env python3
"""
Configuration Validation Script
Ensures all user-configurable values are properly set and .env is complete.
Addresses feedback: Configuration Management & Validation
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Set, Any
import re

class ConfigValidator:
    def __init__(self):
        self.atlas_root = Path(__file__).parent
        self.env_template = self.atlas_root / "env.template"
        self.env_file = self.atlas_root / ".env"
        self.config_errors = []
        self.config_warnings = []
        
    def validate_all(self) -> Dict[str, Any]:
        """Comprehensive configuration validation"""
        results = {
            "status": "success",
            "errors": [],
            "warnings": [],
            "env_coverage": {},
            "hardcoded_values": [],
            "missing_configs": [],
            "recommendations": []
        }
        
        # 1. Check .env template vs actual .env
        env_coverage = self._validate_env_coverage()
        results["env_coverage"] = env_coverage
        
        # 2. Scan code for hardcoded values that should be in .env
        hardcoded = self._scan_hardcoded_values()
        results["hardcoded_values"] = hardcoded
        
        # 3. Validate critical paths exist
        missing_configs = self._validate_critical_configs()
        results["missing_configs"] = missing_configs
        
        # 4. Check for missing required environment variables
        required_vars = self._check_required_variables()
        results["missing_required"] = required_vars
        
        # 5. Generate recommendations
        recommendations = self._generate_recommendations(env_coverage, hardcoded, missing_configs)
        results["recommendations"] = recommendations
        
        # Set overall status
        if self.config_errors:
            results["status"] = "error"
            results["errors"] = self.config_errors
        elif self.config_warnings:
            results["status"] = "warning" 
            results["warnings"] = self.config_warnings
            
        return results
        
    def _validate_env_coverage(self) -> Dict[str, Any]:
        """Check if .env covers all variables in env.template"""
        template_vars = set()
        env_vars = set()
        
        # Parse template
        if self.env_template.exists():
            with open(self.env_template) as f:
                for line in f:
                    if '=' in line and not line.strip().startswith('#'):
                        var_name = line.split('=')[0].strip()
                        template_vars.add(var_name)
        
        # Parse actual .env
        if self.env_file.exists():
            with open(self.env_file) as f:
                for line in f:
                    if '=' in line and not line.strip().startswith('#'):
                        var_name = line.split('=')[0].strip()
                        env_vars.add(var_name)
        
        missing = template_vars - env_vars
        extra = env_vars - template_vars
        
        if missing:
            self.config_errors.append(f"Missing .env variables: {', '.join(missing)}")
            
        return {
            "template_vars": len(template_vars),
            "env_vars": len(env_vars),
            "missing": list(missing),
            "extra": list(extra),
            "coverage_percent": round((len(env_vars) / len(template_vars) * 100), 1) if template_vars else 100
        }
        
    def _scan_hardcoded_values(self) -> List[Dict[str, str]]:
        """Scan Python files for hardcoded values that should be configurable"""
        hardcoded_patterns = [
            (r'timeout\s*=\s*(\d+)', 'timeout'),
            (r'delay\s*=\s*(\d+)', 'delay'),  
            (r'limit\s*=\s*(\d+)', 'limit'),
            (r'batch_size\s*=\s*(\d+)', 'batch_size'),
            (r'max_retries\s*=\s*(\d+)', 'max_retries'),
            (r'rate_limit\s*=\s*(\d+)', 'rate_limit'),
            (r'api_key\s*=\s*["\']([^"\']+)["\']', 'api_key'),
            (r'/tmp/\w+', 'temp_path'),
            (r'/home/\w+', 'home_path')
        ]
        
        hardcoded_found = []
        python_files = list(self.atlas_root.rglob("*.py"))
        
        for file_path in python_files:
            if 'test' in str(file_path) or '__pycache__' in str(file_path):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                for pattern, config_type in hardcoded_patterns:
                    matches = re.finditer(pattern, content, re.IGNORECASE)
                    for match in matches:
                        hardcoded_found.append({
                            "file": str(file_path.relative_to(self.atlas_root)),
                            "line": content[:match.start()].count('\n') + 1,
                            "value": match.group(0),
                            "type": config_type,
                            "recommendation": f"Move to .env as {config_type.upper()}"
                        })
                        
            except Exception as e:
                continue
                
        return hardcoded_found[:20]  # Limit output
        
    def _validate_critical_configs(self) -> List[str]:
        """Check that critical configuration paths exist"""
        critical_paths = [
            "data/",
            "output/", 
            "inputs/",
            "logs/",
            "config/"
        ]
        
        missing = []
        for path_str in critical_paths:
            path = self.atlas_root / path_str
            if not path.exists():
                missing.append(path_str)
                self.config_warnings.append(f"Critical directory missing: {path_str}")
                
        return missing
        
    def _check_required_variables(self) -> List[str]:
        """Check for absolutely required environment variables"""
        required_vars = [
            "ATLAS_DATA_DIR",
            "ATLAS_LOG_LEVEL",
            "ATLAS_OUTPUT_DIR"
        ]
        
        missing = []
        for var in required_vars:
            if not os.getenv(var):
                missing.append(var)
                self.config_errors.append(f"Required environment variable missing: {var}")
                
        return missing
        
    def _generate_recommendations(self, env_coverage, hardcoded, missing_configs) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        if env_coverage["coverage_percent"] < 100:
            recommendations.append("Update .env file to include all template variables")
            
        if hardcoded:
            recommendations.append("Move hardcoded values to .env for better configuration management")
            
        if missing_configs:
            recommendations.append("Create missing critical directories")
            
        if env_coverage["coverage_percent"] > 95:
            recommendations.append("Configuration coverage is excellent!")
            
        return recommendations
        
    def fix_common_issues(self) -> Dict[str, Any]:
        """Auto-fix common configuration issues"""
        fixes = {
            "directories_created": [],
            "env_updated": False,
            "recommendations": []
        }
        
        # Create missing directories
        critical_paths = ["data", "output", "inputs", "logs", "config"]
        for path_str in critical_paths:
            path = self.atlas_root / path_str
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                fixes["directories_created"].append(str(path))
                
        return fixes

def main():
    """Run configuration validation"""
    validator = ConfigValidator()
    
    print("🔍 Atlas Configuration Validation")
    print("=" * 50)
    
    # Run validation
    results = validator.validate_all()
    
    # Display results
    print(f"\n📊 Status: {results['status'].upper()}")
    
    if results['env_coverage']:
        cov = results['env_coverage']
        print(f"\n📝 Environment Coverage: {cov['coverage_percent']}%")
        print(f"   Template variables: {cov['template_vars']}")
        print(f"   .env variables: {cov['env_vars']}")
        
        if cov['missing']:
            print(f"   ❌ Missing: {', '.join(cov['missing'])}")
            
    if results['hardcoded_values']:
        print(f"\n⚠️  Hardcoded Values Found: {len(results['hardcoded_values'])}")
        for hc in results['hardcoded_values'][:5]:  # Show first 5
            print(f"   {hc['file']}:{hc['line']} - {hc['type']}")
            
    if results['missing_configs']:
        print(f"\n📁 Missing Directories: {', '.join(results['missing_configs'])}")
        
    if results['recommendations']:
        print("\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"   • {rec}")
            
    # Auto-fix option
    if results['status'] in ['error', 'warning']:
        print("\n🔧 Auto-fixing common issues...")
        fixes = validator.fix_common_issues()
        
        if fixes['directories_created']:
            print(f"   ✅ Created directories: {len(fixes['directories_created'])}")
            
    print(f"\n{'✅' if results['status'] == 'success' else '⚠️'} Validation complete!")
    
    return results

if __name__ == "__main__":
    main()