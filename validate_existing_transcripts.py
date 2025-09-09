#!/usr/bin/env python3
"""
Validate Existing Transcripts in Database
Analyze quality of transcripts already in the Atlas database
"""

import json
from helpers.database_config import get_database_connection

def validate_transcript_quality(transcript: str, title: str) -> dict:
    """Validate transcript quality and completeness using character-per-minute heuristic"""
    length = len(transcript)
    word_count = len(transcript.split())
    sentences = transcript.count('.') + transcript.count('!') + transcript.count('?')
    
    # Character per minute heuristic (based on analysis of Lex Fridman episodes)
    # Conservative: ~1559 chars/minute for full transcripts
    
    # Check for obvious spam first (very specific patterns)
    spam_patterns = [
        "buy discount ozempic", "click this link now", "order cheap pills",
        "pharmacy discount", "viagra cialis", "weight loss pills"
    ]
    has_spam = any(pattern.lower() in transcript.lower() for pattern in spam_patterns)
    
    if has_spam:
        quality = "spam"
        reason = "Contains obvious spam content"
        score = 0
    elif length < 2000:
        quality = "very_poor"
        reason = "Too short - definitely not a full transcript"
        score = 1
    elif length < 15000:
        quality = "poor"
        reason = "Short - likely summary or excerpt (< 10 min episode)"
        score = 2
    elif length < 40000:
        quality = "medium"
        reason = "Medium - could be short episode (15-25 min)"
        score = 3
    elif length < 75000:
        quality = "good"
        reason = "Good length - likely 30-45 min episode"
        score = 4
    elif length < 110000:
        quality = "excellent"
        reason = "Very good - likely 45-70 min episode"
        score = 5
    else:
        quality = "excellent"
        reason = "Excellent - definitely full long-form episode (70+ min)"
        score = 5
        
    # Additional quality indicators
    chars_per_word = length / max(word_count, 1)
    estimated_duration_minutes = length / 1559  # Using our heuristic
    
    return {
        "quality": quality,
        "score": score,
        "reason": reason,
        "length": length,
        "word_count": word_count,
        "sentences": sentences,
        "chars_per_word": round(chars_per_word, 1),
        "estimated_minutes": round(estimated_duration_minutes, 1),
        "is_spam": has_spam
    }

def main():
    conn = get_database_connection()
    
    # Get all podcast transcripts
    cursor = conn.execute('''
        SELECT id, title, content, url, metadata
        FROM content 
        WHERE content_type = 'podcast_transcript'
        ORDER BY length(content) DESC
    ''')
    
    results = cursor.fetchall()
    
    print(f"📊 TRANSCRIPT QUALITY ANALYSIS")
    print(f"Total transcripts: {len(results)}")
    print("="*80)
    
    quality_counts = {"excellent": 0, "good": 0, "medium": 0, "poor": 0, "very_poor": 0, "spam": 0}
    low_quality_ids = []
    
    for content_id, title, content, url, metadata in results:
        metadata_obj = json.loads(metadata) if metadata else {}
        podcast_name = metadata_obj.get('podcast_name', 'Unknown')
        
        quality_info = validate_transcript_quality(content, title)
        quality_counts[quality_info['quality']] += 1
        
        if quality_info['score'] < 3:  # Mark low quality for potential removal
            low_quality_ids.append((content_id, title[:50], quality_info))
        
        print(f"{quality_info['quality'].upper():9} | {quality_info['length']:6d} chars | {quality_info['estimated_minutes']:4.0f} min | {quality_info['word_count']:5d} words | {podcast_name[:15]:<15} | {title[:35]}")
    
    print("\n" + "="*80)
    print("📈 QUALITY DISTRIBUTION:")
    for quality, count in quality_counts.items():
        if count > 0:
            print(f"  {quality.capitalize():12}: {count:2d} transcripts")
    
    if low_quality_ids:
        print(f"\n⚠️  LOW QUALITY TRANSCRIPTS ({len(low_quality_ids)} items):")
        for content_id, title, quality_info in low_quality_ids:
            print(f"  ID {content_id}: {quality_info['quality']} - {quality_info['reason']} ({quality_info['length']} chars)")
            print(f"    Title: {title}")
        
        print(f"\n🧹 CLEANUP RECOMMENDATION:")
        print(f"Consider removing {len(low_quality_ids)} low-quality transcripts")
    else:
        print(f"\n✅ All transcripts meet quality standards!")
    
    conn.close()

if __name__ == "__main__":
    main()