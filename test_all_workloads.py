#!/usr/bin/env python3
"""Test all 5 Atlas workloads with the new single model system"""

import os
import time
from atlas_model_client import create_client

# Set API key
os.environ['OPENROUTER_API_KEY'] = "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"

def test_all_workloads():
    client = create_client()
    
    test_article = """Artificial intelligence has become increasingly important in business operations, transforming how companies analyze data, make predictions, and automate complex processes. Machine learning algorithms can now identify patterns in massive datasets that would be impossible for humans to process manually. This technological revolution is reshaping entire industries and creating new opportunities for innovation and growth. Companies are using AI for customer service automation, predictive maintenance, fraud detection, and personalized marketing campaigns."""
    
    test_title = "AI Business Transformation"
    
    print('🎯 COMPREHENSIVE WORKLOAD TEST - All 5 Atlas Features')
    print('=' * 60)
    
    workloads = ['tags', 'summary', 'socratic', 'patterns', 'recommendations']
    total_cost = 0
    total_tokens = 0
    results = {}
    
    for workload in workloads:
        print(f'\n📋 Testing {workload.upper()} workload...')
        start_time = time.time()
        
        try:
            result, metadata = client.process_workload(workload, test_article, test_title)
            duration = time.time() - start_time
            
            if metadata['status'] == 'success':
                total_cost += metadata['cost']
                total_tokens += metadata['tokens']
                print(f'  ✅ SUCCESS: {metadata["tokens"]} tokens, ${metadata["cost"]:.6f}, {duration:.2f}s')
                print(f'  📝 Result: {result[:150]}...')
                
                results[workload] = {
                    'status': 'success',
                    'result': result,
                    'tokens': metadata['tokens'],
                    'cost': metadata['cost'],
                    'duration': duration
                }
            else:
                print(f'  ❌ FAILED: {metadata.get("error", "Unknown error")}')
                results[workload] = {
                    'status': 'failed',
                    'error': metadata.get("error", "Unknown error")
                }
        except Exception as e:
            print(f'  💥 EXCEPTION: {str(e)}')
            results[workload] = {
                'status': 'exception',
                'error': str(e)
            }
    
    print(f'\n🏆 FINAL SUMMARY:')
    print(f'  Total Cost: ${total_cost:.6f}')
    print(f'  Total Tokens: {total_tokens}')
    print(f'  Average Cost per Workload: ${total_cost/len(workloads) if len(workloads) > 0 else 0:.6f}')
    print(f'  Success Rate: {sum(1 for r in results.values() if r["status"] == "success")}/{len(workloads)} ({100 * sum(1 for r in results.values() if r["status"] == "success")/len(workloads):.0f}%)')
    
    return results

if __name__ == "__main__":
    test_all_workloads()