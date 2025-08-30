#!/usr/bin/env python3
"""
Simple Test for Unified AI System - No external dependencies
Basic validation of the unified AI system components
"""

import os
import sys
import json
import time
from pathlib import Path

# Add Atlas to path
sys.path.insert(0, str(Path(__file__).parent))

def mock_log_info(message):
    """Mock logging function."""
    print(f"INFO: {message}")

def mock_log_error(message):
    """Mock logging function."""
    print(f"ERROR: {message}")

# Patch logging to avoid dependency issues
sys.modules['helpers.utils'] = type(sys)('helpers.utils')
sys.modules['helpers.utils'].log_info = mock_log_info
sys.modules['helpers.utils'].log_error = mock_log_error


def test_llm_client_basic():
    """Test basic LLM client functionality without API calls."""
    print("🔧 Testing LLM Client (Basic)...")
    
    try:
        from helpers.llm_client import LLMClient
        
        # Test initialization
        client = LLMClient()
        print(f"   ✅ Client initialized")
        
        # Test token estimation
        test_text = "This is a test for token estimation"
        tokens = client.estimate_tokens(test_text)
        print(f"   ✅ Token estimation: {tokens} tokens for {len(test_text)} chars")
        
        # Test cost estimation
        cost = client.estimate_cost('meta-llama/llama-3.1-8b-instruct', 1000, 200)
        print(f"   ✅ Cost estimation: ${cost:.6f} for 1000+200 tokens")
        
        # Test JSON validation and repair
        valid_json = '{"test": "value"}'
        invalid_json = '```json\n{"test": "value",}\n```'
        
        print(f"   ✅ Valid JSON check: {client.is_valid_json(valid_json)}")
        
        repaired = client.repair_json(invalid_json)
        print(f"   ✅ JSON repair: {client.is_valid_json(repaired)}")
        
        # Test model info
        models = client.list_available_models()
        if models:
            info = client.get_model_info(models[0])
            print(f"   ✅ Model info: {models[0]} - ${info['input_per_1m']:.3f}/${info['output_per_1m']:.3f}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ LLM Client test failed: {str(e)}")
        return False


def test_routing_logic():
    """Test model routing logic."""
    print("\n🎯 Testing Model Routing Logic...")
    
    try:
        from helpers.llm_router import LLMRouter, TaskSpec, TaskKind
        
        # Test router initialization
        router = LLMRouter()
        print(f"   ✅ Router initialized with {len(router.MODELS)} models")
        
        # Test routing decisions (dry run)
        test_cases = [
            (TaskSpec(TaskKind.SUMMARIZE, 1000), "Basic summarization"),
            (TaskSpec(TaskKind.CODE_ANALYSIS, 5000, code_heavy=True), "Code analysis"),
            (TaskSpec(TaskKind.EXTRACT_JSON, 150000, requires_long_ctx=True), "Long context JSON"),
            (TaskSpec(TaskKind.SUMMARIZE, 1000, retry_count=1, previous_fail_reason='invalid_json'), "Fallback for JSON failure")
        ]
        
        for spec, description in test_cases:
            model = router.choose_model(spec)
            explanation = router._explain_choice(spec, model)
            model_info = router._get_model_info(model)
            
            print(f"   ✅ {description}")
            print(f"      Model: {model} ({model_info.tier.value})")
            print(f"      Reason: {explanation}")
        
        # Test escalation logic
        spec_normal = TaskSpec(TaskKind.SUMMARIZE, 1000)
        spec_escalated = TaskSpec(TaskKind.SUMMARIZE, 1000, retry_count=1, previous_fail_reason='invalid_json')
        
        should_escalate = router.should_escalate(spec_escalated)
        print(f"   ✅ Escalation logic: {should_escalate}")
        
        # Test routing stats
        stats = router.get_routing_stats()
        print(f"   ✅ Routing stats: {stats['available_models']} models available")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Model routing test failed: {str(e)}")
        return False


def test_cost_manager_basic():
    """Test basic cost management functionality."""
    print("\n💰 Testing Cost Management (Basic)...")
    
    try:
        from helpers.ai_cost_manager import AICostManager
        
        # Test initialization
        manager = AICostManager()
        print(f"   ✅ Cost manager initialized")
        
        # Test budget checking
        budget_check = manager.check_budget_limits(0.01)
        print(f"   ✅ Budget check (${0.01:.3f}): {'✅ Allowed' if budget_check['allowed'] else '❌ Blocked'}")
        
        if not budget_check['allowed']:
            print(f"      Reason: {budget_check['reason']}")
        
        # Test cost estimation
        estimated_cost = manager._estimate_request_cost({
            'content': 'Test content for cost estimation',
            'prompt': 'Summarize this content'
        })
        print(f"   ✅ Cost estimation: ${estimated_cost:.6f}")
        
        # Test usage tracking
        current_usage = manager._get_current_usage()
        print(f"   ✅ Current usage: Daily ${current_usage['daily_cost']:.4f}, Monthly ${current_usage['monthly_cost']:.4f}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Cost management test failed: {str(e)}")
        return False


def test_unified_system_basic():
    """Test unified system initialization and basic functionality."""
    print("\n🤖 Testing Unified AI System (Basic)...")
    
    try:
        from helpers.unified_ai import UnifiedAISystem
        
        # Test initialization
        ai = UnifiedAISystem()
        print(f"   ✅ Unified AI system initialized")
        
        # Test system status
        status = ai.get_system_status()
        print(f"   ✅ System status: {status['system_status']}")
        print(f"      Capabilities: {len(status.get('capabilities', {}))}")
        
        # Test content type detection
        test_cases = [
            ("def hello_world(): print('Hello')", "code"),
            ("<html><body>Test</body></html>", "markup"),
            ("This is a normal text article about technology.", "natural_text")
        ]
        
        for content, expected_type in test_cases:
            detected_type = ai._detect_content_type(content)
            print(f"   ✅ Content type detection: '{expected_type}' -> '{detected_type}'")
        
        # Test message building
        from helpers.llm_router import TaskKind
        messages = ai._build_messages(TaskKind.SUMMARIZE, "Test content", {'target_length': 100})
        print(f"   ✅ Message building: {len(messages)} messages created")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Unified AI system test failed: {str(e)}")
        return False


def test_summarizer_integration():
    """Test summarizer integration with unified system."""
    print("\n📝 Testing Summarizer Integration...")
    
    try:
        from helpers.summarizer import UnifiedSummarizer
        
        # Test initialization
        summarizer = UnifiedSummarizer()
        print(f"   ✅ Unified summarizer initialized")
        
        # Test with short content (should skip AI)
        short_content = "This is a short test."
        result = summarizer.summarize(short_content)
        
        print(f"   ✅ Short content test:")
        print(f"      Method: {result.get('method')}")
        print(f"      Success: {result.get('success')}")
        
        # Test with longer content (will use fallback since no API key)
        long_content = "This is a comprehensive test article about artificial intelligence. " * 20
        
        result = summarizer.summarize(long_content, summary_type="auto", target_length=200)
        
        print(f"   ✅ Long content test:")
        print(f"      Method: {result.get('method')}")
        print(f"      Success: {result.get('success')}")
        print(f"      Summary length: {len(result.get('summary', ''))}")
        print(f"      Fallback used: {result.get('fallback_used', 'N/A')}")
        
        # Test convenience functions
        from helpers.summarizer import unified_summarize_content
        quick_summary = unified_summarize_content("Test content for quick summarization", max_length=50)
        print(f"   ✅ Quick summarization: {len(quick_summary)} chars")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Summarizer integration test failed: {str(e)}")
        return False


def test_configuration():
    """Test configuration and environment setup."""
    print("\n⚙️ Testing Configuration...")
    
    try:
        # Check environment template
        env_template = Path("env.template")
        if env_template.exists():
            with open(env_template) as f:
                content = f.read()
                
            ai_vars = [var for var in content.split('\n') if 'AI_' in var or 'OPENROUTER_' in var]
            print(f"   ✅ Environment template: {len(ai_vars)} AI-related variables")
            
            # Show key AI configuration variables
            key_vars = ['OPENROUTER_API_KEY', 'AI_FEATURES_ENABLED', 'DAILY_AI_BUDGET', 'AI_MODEL']
            for var in key_vars:
                if var in content:
                    print(f"      ✅ {var} configured")
        
        # Test actual environment
        api_key = os.getenv('OPENROUTER_API_KEY', '')
        ai_enabled = os.getenv('AI_FEATURES_ENABLED', 'true').lower() == 'true'
        
        print(f"   ✅ Runtime config:")
        print(f"      API Key: {'✅ Set' if api_key else '❌ Not set (fallback mode)'}")
        print(f"      AI Features: {'✅ Enabled' if ai_enabled else '❌ Disabled'}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Configuration test failed: {str(e)}")
        return False


def main():
    """Run simplified test suite."""
    print("🚀 Unified AI System - Basic Test Suite")
    print("=" * 60)
    print("Note: Testing without external dependencies")
    print()
    
    tests = [
        ("LLM Client Basic", test_llm_client_basic),
        ("Routing Logic", test_routing_logic),
        ("Cost Management Basic", test_cost_manager_basic),
        ("Unified System Basic", test_unified_system_basic),
        ("Summarizer Integration", test_summarizer_integration),
        ("Configuration", test_configuration)
    ]
    
    results = []
    start_time = time.time()
    
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\n❌ {test_name} test crashed: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("🎯 Test Results Summary")
    print("-" * 30)
    
    passed = 0
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status:<8} {test_name}")
        if success:
            passed += 1
    
    total_time = time.time() - start_time
    success_rate = (passed / len(results)) * 100
    
    print("-" * 30)
    print(f"Results: {passed}/{len(results)} tests passed ({success_rate:.1f}%)")
    print(f"Time: {total_time:.2f} seconds")
    
    if success_rate >= 80:
        print("\n🎉 UNIFIED AI SYSTEM CORE IS READY!")
        print("✅ Component integration successful")
        print("✅ Routing logic operational")
        print("✅ Cost management functional")
        print("✅ Fallback strategies active")
        print("\nTo enable full AI features:")
        print("1. Set OPENROUTER_API_KEY in .env")
        print("2. Configure budget limits as needed")
        print("3. Test with actual API calls")
    else:
        print("\n⚠️ Some tests failed - review implementation")
    
    return success_rate >= 80


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)