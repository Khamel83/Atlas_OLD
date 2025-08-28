#!/usr/bin/env python3
"""Process podcasts according to user's specific rules and preferences"""

import csv
import json
import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime
from helpers.bulletproof_process_manager import create_managed_process

class UserPodcastProcessor:
    """Process podcasts according to user's detailed preferences"""
    
    def __init__(self):
        self.prefs_file = Path("config/podcasts_prioritized.csv")
        self.podcast_rules = {}
        self.load_preferences()
        
    def load_preferences(self):
        """Load user's podcast preferences"""
        if not self.prefs_file.exists():
            print(f"❌ Preferences file not found: {self.prefs_file}")
            return
            
        with open(self.prefs_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                podcast_name = row['Podcast Name'].strip('"')
                self.podcast_rules[podcast_name] = {
                    'count': int(row['Count']),
                    'future': bool(int(row['Future'])),
                    'transcript_only': bool(int(row['Transcript_Only'])),
                    'exclude': bool(int(row['Exclude'])),
                    'category': row['Category']
                }
        
        print(f"✅ Loaded {len(self.podcast_rules)} podcast rules")
    
    def get_high_priority_podcasts(self):
        """Get podcasts that should be processed first"""
        high_priority = []
        
        for name, rules in self.podcast_rules.items():
            if rules['exclude']:
                continue
                
            priority_score = 0
            
            # High episode count = high priority
            if rules['count'] >= 1000:
                priority_score += 100
            elif rules['count'] >= 100:
                priority_score += 50
            elif rules['count'] >= 10:
                priority_score += 20
            
            # Special high-value podcasts
            if any(key in name.lower() for key in ['acquired', 'atp', 'stratechery', 'tyler', 'hard fork', 'lex fridman']):
                priority_score += 75
                
            high_priority.append((name, rules, priority_score))
        
        # Sort by priority score descending
        high_priority.sort(key=lambda x: x[2], reverse=True)
        return high_priority
    
    def process_podcast_by_rules(self, podcast_name, rules):
        """Process a single podcast according to its rules"""
        print(f"\n🎙️  Processing: {podcast_name}")
        print(f"   Target episodes: {rules['count']}")
        print(f"   Transcript only: {rules['transcript_only']}")
        print(f"   Category: {rules['category']}")
        
        if rules['exclude']:
            print(f"   ❌ SKIPPED: Marked as excluded")
            return True
            
        if rules['count'] == 0:
            print(f"   ❌ SKIPPED: Zero episodes requested")
            return True
        
        # Find matching RSS URL from config files
        rss_url = self.find_rss_url(podcast_name)
        if not rss_url:
            print(f"   ❌ ERROR: No RSS URL found")
            return False
        
        print(f"   📡 RSS: {rss_url[:60]}...")
        
        # Run podcast processing with specific rules
        try:
            # Use the podcast CLI with specific parameters
            cmd = [
                sys.executable, "-m", "modules.podcasts.cli", "process-single",
                "--name", podcast_name,
                "--rss", rss_url,
                "--max-episodes", str(min(rules['count'], 50)),  # Process in batches
                "--transcript-only" if rules['transcript_only'] else "--full-content"
            ]
            
            print(f"   🚀 Running: {' '.join(cmd[:6])}...")
            
            try:
            process = create_managed_process(cmd, f"process_podcast_{podcast_name}", timeout=600)
            stdout, stderr = process.communicate()
            
            if process.returncode == 0:
                print(f"   ✅ SUCCESS: Processed {podcast_name}")
                return True
            else:
                print(f"   ❌ ERROR: {stderr.decode('utf-8')[:100] if stderr else 'Unknown error'}")
                return False
        except Exception as e:
            print(f"   ❌ EXCEPTION: {e}")
            return False
    
    def find_rss_url(self, podcast_name):
        """Find RSS URL for podcast from config files"""
        config_files = [
            "config/podcasts_prioritized.csv",
            "config/podcasts_from_your_preferences.csv", 
            "config/podcasts.csv"
        ]
        
        for config_file in config_files:
            if not Path(config_file).exists():
                continue
                
            try:
                with open(config_file, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        row_name = row.get('Podcast Name', '').strip('"')
                        if podcast_name.lower() == row_name.lower():
                            return row.get('RSS URL', '')
            except Exception:
                continue
        
        return None
    
    def process_all_by_priority(self):
        """Process all podcasts by priority order"""
        print("🚀 PROCESSING PODCASTS BY USER PREFERENCES")
        print("=" * 60)
        
        high_priority = self.get_high_priority_podcasts()
        
        print(f"\n📋 Processing order (by priority):")
        for i, (name, rules, score) in enumerate(high_priority[:10]):
            print(f"   {i+1}. {name} (score: {score}, episodes: {rules['count']})")
        
        successful = 0
        failed = 0
        
        # Process top priority podcasts first
        for name, rules, score in high_priority[:20]:  # Top 20 podcasts
            if self.process_podcast_by_rules(name, rules):
                successful += 1
            else:
                failed += 1
            
            # Brief pause between podcasts
            time.sleep(2)
        
        print(f"\n📊 SUMMARY:")
        print(f"   Successful: {successful}")
        print(f"   Failed: {failed}")
        print(f"   Success rate: {(successful/(successful+failed))*100:.1f}%")
        
        return successful > 0

def main():
    """Main entry point"""
    processor = UserPodcastProcessor()
    
    if len(sys.argv) > 1 and sys.argv[1] == "high-priority":
        # Just process top 5 highest priority
        high_priority = processor.get_high_priority_podcasts()[:5]
        print("Processing TOP 5 PRIORITY podcasts:")
        for name, rules, score in high_priority:
            print(f"  - {name} ({rules['count']} episodes)")
            processor.process_podcast_by_rules(name, rules)
    else:
        processor.process_all_by_priority()

if __name__ == "__main__":
    main()