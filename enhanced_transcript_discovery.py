#!/usr/bin/env python3
"""
Enhanced Transcript Discovery Service
Integrates all advanced transcript resolvers into Atlas background processing.
"""

import sys
import logging
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

# Add modules path
sys.path.append(str(Path(__file__).parent))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/enhanced_transcript_discovery.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EnhancedTranscriptDiscoveryService:
    """Service that runs enhanced transcript discovery using all resolvers."""
    
    def __init__(self):
        self.start_time = datetime.utcnow()
        self.stats = {
            'podcasts_discovered': 0,
            'transcripts_found': 0,
            'transcripts_fetched': 0,
            'errors': 0,
            'youtube_transcripts': 0,
            'network_transcripts': 0,
            'processing_time': 0
        }
        
    def log_stats(self):
        """Log current statistics."""
        elapsed = (datetime.utcnow() - self.start_time).total_seconds()
        self.stats['processing_time'] = elapsed
        
        logger.info("🎯 Enhanced Transcript Discovery Statistics:")
        logger.info(f"   📡 Podcasts discovered: {self.stats['podcasts_discovered']}")
        logger.info(f"   📄 Total transcripts found: {self.stats['transcripts_found']}")
        logger.info(f"   ✅ Transcripts fetched: {self.stats['transcripts_fetched']}")
        logger.info(f"   🎥 YouTube transcripts: {self.stats['youtube_transcripts']}")
        logger.info(f"   🏢 Network transcripts: {self.stats['network_transcripts']}")
        logger.info(f"   ❌ Errors: {self.stats['errors']}")
        logger.info(f"   ⏱️  Processing time: {elapsed:.1f}s")
        
    def run_enhanced_discovery(self) -> Dict[str, Any]:
        """Run the enhanced podcast transcript discovery."""
        logger.info("🚀 Starting Enhanced Transcript Discovery")
        logger.info("=" * 60)
        
        try:
            logger.info("📡 Phase 1: Enhanced Discovery (using CLI)")
            
            # Run discovery using CLI interface
            discovery_start = time.time()
            
            # Use subprocess to run CLI with enhanced resolvers
            import subprocess
            
            discovery_result = subprocess.run([
                sys.executable, '-m', 'modules.podcasts.cli', 'discover', '--all'
            ], capture_output=True, text=True, timeout=600)
            
            discovery_time = time.time() - discovery_start
            
            if discovery_result.returncode == 0:
                logger.info(f"✅ Enhanced discovery completed in {discovery_time:.1f}s")
                
                # Parse output for statistics
                output_lines = discovery_result.stdout.split('\n')
                for line in output_lines:
                    if 'episodes,' in line and 'transcripts found' in line:
                        # Parse: "✅ Discovery complete: 31353 episodes, 221 transcripts found"
                        try:
                            parts = line.split(':')[1].strip().split(',')
                            episodes_part = parts[0].strip().split()[0]
                            transcripts_part = parts[1].strip().split()[0]
                            self.stats['transcripts_found'] = int(transcripts_part)
                        except:
                            pass
            else:
                logger.error(f"❌ Enhanced discovery failed: {discovery_result.stderr}")
                self.stats['errors'] += 1
            
            logger.info("📥 Phase 2: Enhanced Transcript Fetching")
            
            # Run transcript fetching using CLI
            fetch_start = time.time()
            
            try:
                fetch_result = subprocess.run([
                    sys.executable, '-m', 'modules.podcasts.cli', 'fetch-transcripts', '--all'
                ], capture_output=True, text=True, timeout=900)
                
                fetch_time = time.time() - fetch_start
                
                if fetch_result.returncode == 0:
                    logger.info(f"✅ Enhanced transcript fetching completed in {fetch_time:.1f}s")
                    
                    # Parse output for fetch statistics
                    output_lines = fetch_result.stdout.split('\n')
                    for line in output_lines:
                        if 'fetched,' in line:
                            # Parse fetch results
                            try:
                                parts = line.split(':')[1].strip().split(',')
                                fetched_part = parts[0].strip().split()[0]
                                self.stats['transcripts_fetched'] = int(fetched_part)
                            except:
                                pass
                else:
                    logger.error(f"❌ Enhanced transcript fetching failed: {fetch_result.stderr}")
                    self.stats['errors'] += 1
                    
            except subprocess.TimeoutExpired:
                logger.error("❌ Transcript fetching timed out after 900s")
                self.stats['errors'] += 1
            except Exception as e:
                logger.error(f"❌ Transcript fetching failed: {e}")
                self.stats['errors'] += 1
                
            logger.info("🔄 Phase 3: Atlas Integration")
            
            # Run the existing podcast processing to integrate with Atlas
            integration_start = time.time()
            try:
                import subprocess
                result = subprocess.run([
                    sys.executable, 'process_podcasts.py'
                ], capture_output=True, text=True, timeout=300)
                
                integration_time = time.time() - integration_start
                
                if result.returncode == 0:
                    logger.info(f"✅ Atlas integration completed in {integration_time:.1f}s")
                else:
                    logger.warning(f"⚠️ Atlas integration had issues: {result.stderr[:200]}")
                    
            except subprocess.TimeoutExpired:
                logger.error("❌ Atlas integration timed out after 300s")
                self.stats['errors'] += 1
            except Exception as e:
                logger.error(f"❌ Atlas integration failed: {e}")
                self.stats['errors'] += 1
                
            # Log final statistics
            self.log_stats()
            
            logger.info("🎉 Enhanced Transcript Discovery Complete!")
            logger.info("=" * 60)
            
            return self.stats
            
        except ImportError as e:
            logger.error(f"❌ Failed to import podcast modules: {e}")
            logger.error("   Make sure enhanced resolvers are properly installed")
            self.stats['errors'] += 1
            return self.stats
            
        except Exception as e:
            logger.error(f"❌ Enhanced transcript discovery failed: {e}")
            self.stats['errors'] += 1
            return self.stats
            
    def run_fallback_discovery(self):
        """Run fallback discovery using existing Atlas methods."""
        logger.warning("🔄 Running fallback transcript discovery...")
        
        try:
            # Try existing transcript polling methods
            import subprocess
            
            scripts_to_try = [
                'helpers/universal_transcript_discoverer.py',
                'helpers/atp_enhanced_transcript.py', 
                'helpers/network_transcript_scrapers.py'
            ]
            
            for script in scripts_to_try:
                if Path(script).exists():
                    logger.info(f"   Trying: {script}")
                    try:
                        result = subprocess.run([
                            sys.executable, script, '--all'
                        ], capture_output=True, text=True, timeout=180)
                        
                        if result.returncode == 0:
                            logger.info(f"   ✅ {script} completed successfully")
                        else:
                            logger.warning(f"   ⚠️ {script} had issues: {result.stderr[:100]}")
                            
                    except subprocess.TimeoutExpired:
                        logger.warning(f"   ⏱️ {script} timed out")
                    except Exception as e:
                        logger.warning(f"   ❌ {script} failed: {e}")
                        
        except Exception as e:
            logger.error(f"❌ Fallback discovery failed: {e}")

def main():
    """Main entry point for enhanced transcript discovery."""
    
    # Ensure logs directory exists
    Path('logs').mkdir(exist_ok=True)
    
    logger.info("🎯 Atlas Enhanced Transcript Discovery Service")
    logger.info("=" * 60)
    
    service = EnhancedTranscriptDiscoveryService()
    
    # Try enhanced discovery first
    stats = service.run_enhanced_discovery()
    
    # If enhanced discovery had significant issues, try fallback
    if stats['errors'] > 0 and stats['transcripts_found'] == 0:
        logger.warning("🔄 Enhanced discovery had issues, trying fallback methods...")
        service.run_fallback_discovery()
        
    # Final status
    if stats['transcripts_found'] > 0 or stats['transcripts_fetched'] > 0:
        logger.info("🎉 SUCCESS: Enhanced transcript discovery found new content")
        return 0
    else:
        logger.warning("⚠️ WARNING: No new transcripts discovered")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)