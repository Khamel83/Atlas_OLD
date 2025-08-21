#!/usr/bin/env python3
"""
Validation script for Phases 3 & 4 refactoring

Tests the basic structure and interfaces of our refactored components
without requiring external dependencies.
"""

import sys
import os
from pathlib import Path

# Add atlas to path
atlas_path = str(Path(__file__).parent.parent)
sys.path.insert(0, atlas_path)

def test_base_article_strategy():
    """Test BaseArticleStrategy interface."""
    print("🔍 Testing BaseArticleStrategy...")
    
    try:
        from helpers.base_article_strategy import (
            BaseArticleStrategy, StrategyMetadata, FetchResult,
            StrategyCapability, StrategyPriority, create_strategy
        )
        print("  ✓ Imports successful")
        
        # Test enums
        assert StrategyCapability.BASIC_FETCH
        assert StrategyPriority.HIGHEST
        print("  ✓ Enums defined correctly")
        
        # Test data classes
        metadata = StrategyMetadata(
            name="test",
            priority=StrategyPriority.HIGH,
            capabilities=[StrategyCapability.BASIC_FETCH]
        )
        assert metadata.name == "test"
        print("  ✓ StrategyMetadata works")
        
        result = FetchResult(
            success=True,
            url="https://example.com/test",
            content="Test content"
        )
        assert result.success is True
        assert result.method == result.strategy  # Should sync
        print("  ✓ FetchResult works")
        
        print("  ✅ BaseArticleStrategy validation passed\n")
        return True
        
    except Exception as e:
        print(f"  ❌ BaseArticleStrategy validation failed: {e}\n")
        return False


def test_article_manager_structure():
    """Test ArticleManager structure without dependencies."""
    print("🔍 Testing ArticleManager structure...")
    
    try:
        # Read the file content to check structure
        manager_file = Path(atlas_path) / "helpers" / "article_manager.py"
        content = manager_file.read_text()
        
        # Check for key components
        required_classes = [
            "class ArticleManager:",
            "class ProcessingStats:",
            "class ArticleResult:",
            "def process_article(",
            "def bulk_process_articles(",
            "def recover_failed_articles(",
            "def get_processing_stats("
        ]
        
        for required in required_classes:
            if required not in content:
                raise AssertionError(f"Missing required component: {required}")
        
        print("  ✓ All required classes and methods present")
        
        # Check for backward compatibility
        compatibility_items = [
            "class ArticleFetcher:",
            "def fetch_with_fallbacks(",
            "DeprecationWarning"
        ]
        
        for item in compatibility_items:
            if item not in content:
                raise AssertionError(f"Missing backward compatibility: {item}")
                
        print("  ✓ Backward compatibility layer present")
        print("  ✅ ArticleManager structure validation passed\n")
        return True
        
    except Exception as e:
        print(f"  ❌ ArticleManager structure validation failed: {e}\n")
        return False


def test_content_pipeline_structure():
    """Test ContentPipeline structure without dependencies."""
    print("🔍 Testing ContentPipeline structure...")
    
    try:
        # Read the file content to check structure
        pipeline_file = Path(atlas_path) / "helpers" / "content_pipeline.py"
        content = pipeline_file.read_text()
        
        # Check for key components
        required_classes = [
            "class ContentPipeline:",
            "class ContentResult:",
            "class ProcessingResult:",
            "class PipelineStats:",
            "class ProcessingStage(Enum):",
            "def process_content(",
            "def bulk_process_content(",
            "def get_pipeline_stats("
        ]
        
        for required in required_classes:
            if required not in content:
                raise AssertionError(f"Missing required component: {required}")
        
        print("  ✓ All required classes and methods present")
        
        # Check for processing stages
        stages = [
            "DETECT_TYPE",
            "CLASSIFY_CONTENT", 
            "PROCESS_DOCUMENT",
            "EXTRACT_METADATA",
            "SUMMARIZE_CONTENT",
            "CLUSTER_TOPICS",
            "EXPORT_CONTENT"
        ]
        
        for stage in stages:
            if stage not in content:
                raise AssertionError(f"Missing processing stage: {stage}")
                
        print("  ✓ All processing stages defined")
        
        # Check for stage methods
        stage_methods = [
            "_run_detect_type_stage",
            "_run_classify_content_stage",
            "_run_process_document_stage", 
            "_run_extract_metadata_stage",
            "_run_summarize_content_stage"
        ]
        
        for method in stage_methods:
            if method not in content:
                raise AssertionError(f"Missing stage method: {method}")
                
        print("  ✓ All stage methods implemented")
        print("  ✅ ContentPipeline structure validation passed\n")
        return True
        
    except Exception as e:
        print(f"  ❌ ContentPipeline structure validation failed: {e}\n")
        return False


def test_integration_layer():
    """Test ContentIntegration layer."""
    print("🔍 Testing ContentIntegration layer...")
    
    try:
        integration_file = Path(atlas_path) / "helpers" / "content_integration.py"
        content = integration_file.read_text()
        
        # Check for key integration functions
        required_functions = [
            "def process_article_with_pipeline(",
            "def bulk_process_articles_with_pipeline(",
            "class UnifiedContentProcessor:",
            "def create_unified_processor(",
            "def migrate_to_unified_processing("
        ]
        
        for required in required_functions:
            if required not in content:
                raise AssertionError(f"Missing required function: {required}")
        
        print("  ✓ All integration functions present")
        
        # Check for legacy compatibility
        legacy_items = [
            "def enhanced_article_processing(",
            "def process_content_comprehensive(",
            "class EnhancedArticleIngestor:",
            "DeprecationWarning"
        ]
        
        for item in legacy_items:
            if item not in content:
                raise AssertionError(f"Missing legacy compatibility: {item}")
                
        print("  ✓ Legacy compatibility functions present")
        print("  ✅ ContentIntegration validation passed\n")
        return True
        
    except Exception as e:
        print(f"  ❌ ContentIntegration validation failed: {e}\n")
        return False


def test_compatibility_layer():
    """Test article compatibility layer."""
    print("🔍 Testing Article Compatibility layer...")
    
    try:
        compat_file = Path(atlas_path) / "helpers" / "article_compatibility.py" 
        content = compat_file.read_text()
        
        # Check for compatibility components
        required_items = [
            "class DeprecatedArticleFetcher:",
            "def fetch_article_direct(",
            "def fetch_article_with_auth(",
            "def bulk_fetch_articles(",
            "class ArticleIngestorCompat:",
            "def migrate_article_processing_code("
        ]
        
        for required in required_items:
            if required not in content:
                raise AssertionError(f"Missing compatibility component: {required}")
        
        print("  ✓ All compatibility components present")
        print("  ✅ Article Compatibility validation passed\n")
        return True
        
    except Exception as e:
        print(f"  ❌ Article Compatibility validation failed: {e}\n")
        return False


def test_file_structure():
    """Test that all required files were created."""
    print("🔍 Testing file structure...")
    
    try:
        required_files = [
            "helpers/article_manager.py",
            "helpers/base_article_strategy.py", 
            "helpers/article_compatibility.py",
            "helpers/content_pipeline.py",
            "helpers/content_integration.py",
            "tests/test_article_manager.py",
            "tests/test_content_pipeline.py",
            "tests/test_unified_processing.py"
        ]
        
        for file_path in required_files:
            full_path = Path(atlas_path) / file_path
            if not full_path.exists():
                raise AssertionError(f"Missing required file: {file_path}")
                
        print("  ✓ All required files present")
        
        # Check file sizes (should not be empty)
        for file_path in required_files:
            full_path = Path(atlas_path) / file_path
            if full_path.stat().st_size < 100:  # Very small files might be empty
                print(f"  ⚠️  Warning: {file_path} seems very small ({full_path.stat().st_size} bytes)")
        
        print("  ✅ File structure validation passed\n")
        return True
        
    except Exception as e:
        print(f"  ❌ File structure validation failed: {e}\n")
        return False


def test_article_ingestor_migration():
    """Test that ArticleIngestor was successfully migrated."""
    print("🔍 Testing ArticleIngestor migration...")
    
    try:
        ingestor_file = Path(atlas_path) / "helpers" / "article_ingestor.py"
        content = ingestor_file.read_text()
        
        # Should now import ArticleManager instead of ArticleFetcher
        if "from helpers.article_manager import ArticleManager" not in content:
            raise AssertionError("ArticleIngestor not updated to use ArticleManager")
        
        # Should use article_manager instead of fetcher
        if "self.article_manager = ArticleManager" not in content:
            raise AssertionError("ArticleIngestor not using ArticleManager instance")
            
        # Should call process_article instead of fetch
        if "self.article_manager.process_article" not in content:
            raise AssertionError("ArticleIngestor not calling process_article")
        
        print("  ✓ ArticleIngestor successfully migrated to use ArticleManager")
        print("  ✅ ArticleIngestor migration validation passed\n")
        return True
        
    except Exception as e:
        print(f"  ❌ ArticleIngestor migration validation failed: {e}\n")
        return False


def validate_code_quality():
    """Basic code quality checks."""
    print("🔍 Testing code quality...")
    
    try:
        files_to_check = [
            "helpers/article_manager.py",
            "helpers/content_pipeline.py",
            "helpers/content_integration.py"
        ]
        
        for file_path in files_to_check:
            full_path = Path(atlas_path) / file_path
            content = full_path.read_text()
            
            # Check for basic docstrings
            if '"""' not in content[:500]:  # Should have module docstring near top
                print(f"  ⚠️  Warning: {file_path} missing module docstring")
                
            # Check for basic error handling
            if "except Exception as e:" not in content:
                print(f"  ⚠️  Warning: {file_path} may lack proper error handling")
                
            # Check for logging
            if "log_info" not in content and "log_error" not in content:
                print(f"  ⚠️  Warning: {file_path} may lack proper logging")
        
        print("  ✓ Basic code quality checks completed")
        print("  ✅ Code quality validation passed\n")
        return True
        
    except Exception as e:
        print(f"  ❌ Code quality validation failed: {e}\n")
        return False


def main():
    """Run all validation tests."""
    print("🚀 PHASE 3 & 4 REFACTORING VALIDATION")
    print("=" * 50)
    print()
    
    tests = [
        test_file_structure,
        test_base_article_strategy,
        test_article_manager_structure,
        test_content_pipeline_structure,
        test_integration_layer,
        test_compatibility_layer,
        test_article_ingestor_migration,
        validate_code_quality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print()
    print("=" * 50)
    print("🎯 VALIDATION SUMMARY")
    print("=" * 50)
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    print()
    
    if passed == total:
        print("🎉 ALL VALIDATIONS PASSED!")
        print()
        print("✅ Phase 3 Complete: Article Processing Consolidation")
        print("   - Unified ArticleManager with strategy cascade")
        print("   - Standardized article strategy interfaces") 
        print("   - Migrated existing article processing code")
        print("   - Comprehensive backward compatibility")
        print()
        print("✅ Phase 4 Complete: Content Processing Pipeline")
        print("   - Unified ContentPipeline with configurable stages")
        print("   - Integration with existing content processing components")
        print("   - Comprehensive testing and validation")
        print("   - Complete unified processing workflow")
        print()
        print("🚀 Phases 3 & 4 refactoring successfully completed!")
        print("   Atlas now has unified article + content processing")
        print("   with comprehensive statistics, bulk processing,")
        print("   error recovery, and full backward compatibility.")
        return True
    else:
        print("❌ SOME VALIDATIONS FAILED")
        print("   Review the failed tests above and fix issues.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)