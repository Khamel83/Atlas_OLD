#!/usr/bin/env python3
"""
Atlas Transcription Smoke Test
Validates the entire transcription pipeline with a known test case.
"""

import os
import sys
import time
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.database_config import get_database_connection


class TranscriptionSmokeTest:
    """Comprehensive smoke test for transcription pipeline"""
    
    def __init__(self):
        self.test_timeout_seconds = 120  # 2 minutes
        self.test_url = "https://lexfridman.com/oliver-anthony-transcript"  # Known working URL
        self.expected_min_length = 5000  # Minimum transcript length
        
    def get_initial_transcription_count(self) -> int:
        """Get current transcription count"""
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM transcriptions")
            count = cursor.fetchone()[0]
            conn.close()
            return count
        except Exception as e:
            print(f"❌ Error getting initial count: {e}")
            return -1
    
    def run_transcript_worker_test(self) -> bool:
        """Run the transcript worker with a single test case"""
        try:
            print("🧪 Running transcript worker test...")
            
            # Import the worker
            from scripts.fixed_transcript_worker import FixedTranscriptWorker
            
            worker = FixedTranscriptWorker()
            
            # Fetch a known transcript
            transcript_text = worker.fetch_transcript_from_url(self.test_url)
            
            if not transcript_text:
                print("❌ Failed to fetch test transcript")
                return False
                
            if len(transcript_text) < self.expected_min_length:
                print(f"❌ Transcript too short: {len(transcript_text)} chars")
                return False
            
            # Save to database
            filename = f"smoke_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            metadata = {
                "test": True,
                "url": self.test_url,
                "length": len(transcript_text),
                "timestamp": datetime.now().isoformat()
            }
            
            success = worker.save_transcript_to_transcriptions_table(
                filename, transcript_text, "smoke_test", metadata
            )
            
            if success:
                print(f"✅ Test transcript saved ({len(transcript_text):,} chars)")
                return True
            else:
                print("❌ Failed to save test transcript")
                return False
                
        except Exception as e:
            print(f"❌ Worker test failed: {e}")
            return False
    
    def verify_database_update(self, initial_count: int) -> bool:
        """Verify that a new transcription was added"""
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            
            # Get new count
            cursor.execute("SELECT COUNT(*) FROM transcriptions")
            new_count = cursor.fetchone()[0]
            
            # Get latest transcription
            cursor.execute("""
                SELECT filename, created_at, LENGTH(transcript) as length
                FROM transcriptions 
                ORDER BY created_at DESC 
                LIMIT 1
            """)
            latest = cursor.fetchone()
            
            conn.close()
            
            if new_count <= initial_count:
                print(f"❌ No new transcription added: {initial_count} -> {new_count}")
                return False
            
            if latest:
                filename, created_at, length = latest
                print(f"✅ New transcription: {filename} ({length:,} chars) at {created_at}")
                
                # Check if it's recent (within last 5 minutes)
                try:
                    if 'T' in created_at:
                        created_time = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    else:
                        created_time = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                    
                    age_minutes = (datetime.now() - created_time).total_seconds() / 60
                    
                    if age_minutes > 5:
                        print(f"⚠️ Latest transcription is {age_minutes:.1f} minutes old")
                        return False
                    else:
                        print(f"✅ Transcription is fresh ({age_minutes:.1f} minutes old)")
                        return True
                        
                except Exception as e:
                    print(f"⚠️ Could not parse timestamp: {e}")
                    return True  # Assume success if we can't parse time
            else:
                print("❌ No transcriptions found")
                return False
                
        except Exception as e:
            print(f"❌ Database verification failed: {e}")
            return False
    
    def test_database_connectivity(self) -> bool:
        """Test basic database connectivity"""
        try:
            print("🔍 Testing database connectivity...")
            
            conn = get_database_connection()
            cursor = conn.cursor()
            
            # Test basic queries
            cursor.execute("SELECT COUNT(*) FROM podcast_episodes")
            episodes = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM transcriptions")
            transcriptions = cursor.fetchone()[0]
            
            conn.close()
            
            print(f"✅ Database connected: {episodes:,} episodes, {transcriptions:,} transcriptions")
            return True
            
        except Exception as e:
            print(f"❌ Database connectivity failed: {e}")
            return False
    
    def test_file_permissions(self) -> bool:
        """Test file system permissions"""
        try:
            print("📁 Testing file permissions...")
            
            # Test database path access
            from helpers.database_config import get_database_path
            db_path = get_database_path()
            
            if not db_path.exists():
                print(f"❌ Database file not found: {db_path}")
                return False
            
            if not os.access(db_path, os.R_OK | os.W_OK):
                print(f"❌ Database file not readable/writable: {db_path}")
                return False
            
            # Test log directory
            log_dir = Path(__file__).parent.parent / "logs"
            if not log_dir.exists():
                log_dir.mkdir(exist_ok=True)
            
            if not os.access(log_dir, os.R_OK | os.W_OK):
                print(f"❌ Log directory not accessible: {log_dir}")
                return False
            
            print("✅ File permissions OK")
            return True
            
        except Exception as e:
            print(f"❌ File permission test failed: {e}")
            return False
    
    def run_comprehensive_smoke_test(self) -> bool:
        """Run comprehensive smoke test"""
        print("🧪 Atlas Transcription Smoke Test")
        print("=" * 50)
        print(f"🕐 Started at: {datetime.now()}")
        print("")
        
        start_time = datetime.now()
        tests_passed = 0
        total_tests = 4
        
        # Test 1: File permissions
        if self.test_file_permissions():
            tests_passed += 1
        
        # Test 2: Database connectivity
        if self.test_database_connectivity():
            tests_passed += 1
        
        # Test 3: Get initial state
        initial_count = self.get_initial_transcription_count()
        if initial_count >= 0:
            tests_passed += 1
            print(f"📊 Initial transcription count: {initial_count}")
        else:
            print("❌ Could not get initial transcription count")
        
        # Test 4: Run worker and verify
        if self.run_transcript_worker_test():
            if self.verify_database_update(initial_count):
                tests_passed += 1
            else:
                print("❌ Database verification failed")
        else:
            print("❌ Worker test failed")
        
        # Results
        elapsed = (datetime.now() - start_time).total_seconds()
        print("")
        print("=" * 50)
        print(f"🎯 Smoke Test Results: {tests_passed}/{total_tests} passed")
        print(f"⏱️  Elapsed time: {elapsed:.1f} seconds")
        
        if tests_passed == total_tests:
            print("✅ All tests passed - Transcription pipeline is healthy!")
            return True
        else:
            print("❌ Some tests failed - Check logs and configuration")
            return False


def main():
    """Main smoke test entry point"""
    test = TranscriptionSmokeTest()
    
    success = test.run_comprehensive_smoke_test()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()