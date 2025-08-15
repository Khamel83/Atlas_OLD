#!/usr/bin/env python3
"""Run Tyler Cowen accuracy test with known parameters"""

from tyler_cowen_accuracy_test import TylerCowenAccuracyTester
import json
from pathlib import Path
from datetime import datetime

def main():
    audio_url = "https://traffic.libsyn.com/secure/cowenconvos/CWT-265-NateSilver-Audio-Finalwav.mp3?dest-id=850607"
    ref_path = "testing/podcast_tests/nate_silver_reference_partial.txt"
    
    print("Starting Tyler Cowen accuracy test...")
    print(f"Audio URL: {audio_url}")
    print(f"Reference transcript: {ref_path}")
    
    tester = TylerCowenAccuracyTester()
    results = tester.test_episode_accuracy(audio_url, ref_path)
    
    # Save results
    results_file = Path("testing/podcast_tests") / f"tyler_cowen_accuracy_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print results
    print("\n" + "="*60)
    print("TYLER COWEN ACCURACY TEST RESULTS")
    print("="*60)
    
    if results.get("error"):
        print(f"❌ Test failed: {results['error']}")
        return
    
    if results.get("download_success"):
        print(f"✅ Audio downloaded: {results.get('file_size_mb', 0):.1f}MB")
    
    if results.get("transcription_success"):
        tiny_results = results.get("whisper_tiny_results", {})
        print(f"✅ Transcription completed in {tiny_results.get('processing_time_seconds', 0):.1f}s")
        print(f"   Words generated: {tiny_results.get('word_count', 0)}")
        print(f"   Processing speed: {tiny_results.get('realtime_factor', 0):.1f}x realtime")
        
        accuracy = results.get("accuracy_metrics", {})
        if accuracy:
            print("\n📊 Accuracy Metrics:")
            print(f"   Word accuracy: {accuracy.get('word_accuracy', 0):.2%}")
            print(f"   Precision: {accuracy.get('precision', 0):.2%}")
            print(f"   Recall: {accuracy.get('recall', 0):.2%}")
            print(f"   F1 Score: {accuracy.get('f1_score', 0):.2%}")
            print(f"   Character similarity: {accuracy.get('character_similarity', 0):.2%}")
            print(f"   Length ratio (AI/Human): {accuracy.get('length_ratio', 0):.2f}")
            
            print("\n📏 Length Comparison:")
            print(f"   Reference: {accuracy.get('reference_word_count', 0)} words")
            print(f"   AI Generated: {accuracy.get('ai_word_count', 0)} words")
            print(f"   Matched words: {accuracy.get('matched_words', 0)}")
    
    print(f"\nFull results saved to: {results_file}")

if __name__ == "__main__":
    main()