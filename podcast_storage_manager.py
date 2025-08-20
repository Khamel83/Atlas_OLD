#!/usr/bin/env python3
"""
Podcast Storage Hierarchy Manager
Manages audio files vs transcripts based on priority
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class PodcastStorageManager:
    """Manages podcast storage hierarchy and search"""
    
    def __init__(self, atlas_root: str = "/home/ubuntu/dev/atlas"):
        self.atlas_root = Path(atlas_root)
        self.podcasts_dir = self.atlas_root / "output" / "podcasts"
        self.audio_dir = self.podcasts_dir / "audio"
        self.markdown_dir = self.podcasts_dir / "markdown"
        self.metadata_dir = self.podcasts_dir / "metadata"
        
        # Storage priorities based on actual OPML content
        self.priorities = {
            "high": ["this american life", "tyler cowen", "conversations with tyler", "planet money", "lex fridman", "ezra klein"],
            "medium": ["acquired", "all-in", "the bill simmons", "freakonomics", "decoder", "stratechery", "hard fork"],
            "low": ["atp", "nvidia"]  # Everything else including mysterious bulk downloads
        }
    
    def analyze_storage(self) -> Dict:
        """Analyze current storage usage"""
        analysis = {
            "total_audio_files": 0,
            "total_audio_size_gb": 0,
            "total_transcripts": 0,
            "total_metadata": 0,
            "by_priority": {"high": [], "medium": [], "low": []}
        }
        
        # Count audio files and size
        if self.audio_dir.exists():
            audio_files = list(self.audio_dir.glob("*"))
            analysis["total_audio_files"] = len(audio_files)
            
            total_size = sum(f.stat().st_size for f in audio_files if f.is_file())
            analysis["total_audio_size_gb"] = round(total_size / (1024**3), 2)
        
        # Count transcripts
        if self.markdown_dir.exists():
            analysis["total_transcripts"] = len(list(self.markdown_dir.glob("*.md")))
        
        # Count metadata
        analysis["total_metadata"] = len(list(self.podcasts_dir.glob("*_rss_entry.json")))
        
        return analysis
    
    def get_podcast_priority(self, metadata_file: Path) -> str:
        """Determine priority based on podcast metadata"""
        try:
            with open(metadata_file) as f:
                data = json.load(f)
            
            # Check multiple fields for podcast identification
            podcast_title = data.get("podcast_title", "").lower()
            author = data.get("raw_data", {}).get("author", "").lower()
            source = data.get("source", "").lower()
            
            # Combine all identifiers
            identifiers = f"{podcast_title} {author} {source}".lower()
            
            # Check high priority
            for high_priority in self.priorities["high"]:
                if high_priority in identifiers:
                    return "high"
            
            # Check medium priority  
            for medium_priority in self.priorities["medium"]:
                if medium_priority in identifiers:
                    return "medium"
            
            return "low"
            
        except Exception as e:
            logger.warning(f"Could not determine priority for {metadata_file}: {e}")
            return "low"
    
    def create_archive_plan(self) -> Dict:
        """Create plan for archiving audio files by priority"""
        plan = {
            "keep_local": [],      # High priority - keep everything
            "archive_audio": [],   # Medium priority - move audio, keep transcripts
            "metadata_only": []    # Low priority - keep only metadata
        }
        
        # Analyze all podcast metadata
        for metadata_file in self.podcasts_dir.glob("*_rss_entry.json"):
            priority = self.get_podcast_priority(metadata_file)
            podcast_id = metadata_file.stem.replace("_rss_entry", "")
            
            # Find associated files
            audio_file = self.audio_dir / f"{podcast_id}.mp3"
            if not audio_file.exists():
                audio_file = self.audio_dir / f"{podcast_id}.m4a"
            
            transcript_file = self.markdown_dir / f"{podcast_id}.md"
            
            podcast_info = {
                "id": podcast_id,
                "priority": priority,
                "metadata_file": str(metadata_file),
                "audio_file": str(audio_file) if audio_file.exists() else None,
                "transcript_file": str(transcript_file) if transcript_file.exists() else None,
                "audio_size_mb": round(audio_file.stat().st_size / (1024**2), 2) if audio_file.exists() else 0
            }
            
            if priority == "high":
                plan["keep_local"].append(podcast_info)
            elif priority == "medium":
                plan["archive_audio"].append(podcast_info) 
            else:
                plan["metadata_only"].append(podcast_info)
        
        return plan
    
    def execute_archive_plan(self, local_archive_path: str, dry_run: bool = True) -> Dict:
        """Execute the archiving plan"""
        local_path = Path(local_archive_path)
        if not dry_run:
            local_path.mkdir(parents=True, exist_ok=True)
        
        plan = self.create_archive_plan()
        results = {
            "moved_to_local": 0,
            "deleted_audio": 0,
            "space_freed_gb": 0,
            "errors": []
        }
        
        # Archive medium priority (move audio to local)
        for podcast in plan["archive_audio"]:
            if podcast["audio_file"] and Path(podcast["audio_file"]).exists():
                try:
                    if not dry_run:
                        # Move to local storage
                        local_file = local_path / Path(podcast["audio_file"]).name
                        shutil.move(podcast["audio_file"], local_file)
                    
                    results["moved_to_local"] += 1
                    results["space_freed_gb"] += podcast["audio_size_mb"] / 1024
                    
                except Exception as e:
                    results["errors"].append(f"Failed to move {podcast['audio_file']}: {e}")
        
        # Delete low priority audio files
        for podcast in plan["metadata_only"]:
            if podcast["audio_file"] and Path(podcast["audio_file"]).exists():
                try:
                    if not dry_run:
                        os.remove(podcast["audio_file"])
                    
                    results["deleted_audio"] += 1
                    results["space_freed_gb"] += podcast["audio_size_mb"] / 1024
                    
                except Exception as e:
                    results["errors"].append(f"Failed to delete {podcast['audio_file']}: {e}")
        
        results["space_freed_gb"] = round(results["space_freed_gb"], 2)
        return results


class PodcastSearchEngine:
    """Search engine specifically for podcast transcripts"""
    
    def __init__(self, atlas_root: str = "/home/ubuntu/dev/atlas"):
        self.atlas_root = Path(atlas_root)
        self.podcasts_dir = self.atlas_root / "output" / "podcasts"
        self.markdown_dir = self.podcasts_dir / "markdown"
        
    def index_podcasts(self) -> int:
        """Index all podcast transcripts for search"""
        try:
            from search.enhanced_search import EnhancedSearchEngine
            
            search_engine = EnhancedSearchEngine()
            indexed_count = 0
            
            for transcript_file in self.markdown_dir.glob("*.md"):
                try:
                    with open(transcript_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Get metadata if available
                    podcast_id = transcript_file.stem
                    metadata_file = self.podcasts_dir / f"{podcast_id}_rss_entry.json"
                    
                    metadata = {}
                    if metadata_file.exists():
                        with open(metadata_file) as f:
                            metadata = json.load(f)
                    
                    search_engine.add_document(
                        doc_id=f"podcast_{podcast_id}",
                        content=content,
                        metadata={
                            "type": "podcast",
                            "title": metadata.get("title", "Unknown"),
                            "podcast_title": metadata.get("podcast_title", "Unknown"),
                            "author": metadata.get("author", "Unknown"),
                            "duration": metadata.get("duration", "Unknown"),
                            "file_path": str(transcript_file)
                        }
                    )
                    
                    indexed_count += 1
                    
                except Exception as e:
                    logger.warning(f"Failed to index {transcript_file}: {e}")
            
            return indexed_count
            
        except ImportError:
            logger.error("Search engine not available")
            return 0
    
    def search_podcasts(self, query: str, limit: int = 10) -> List[Dict]:
        """Search podcast transcripts"""
        try:
            from search.enhanced_search import EnhancedSearchEngine
            
            search_engine = EnhancedSearchEngine()
            results = search_engine.search(query, limit=limit)
            
            # Filter for podcasts only and enrich with metadata
            podcast_results = []
            for result in results:
                if result["doc_id"].startswith("podcast_"):
                    podcast_results.append(result)
            
            return podcast_results
            
        except ImportError:
            logger.error("Search engine not available")
            return []


def main():
    """Main function for CLI usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Manage podcast storage and search")
    parser.add_argument("--analyze", action="store_true", help="Analyze current storage")
    parser.add_argument("--plan", action="store_true", help="Show archive plan")
    parser.add_argument("--archive", type=str, help="Execute archive plan (provide local path)")
    parser.add_argument("--search", type=str, help="Search podcasts")
    parser.add_argument("--index", action="store_true", help="Index podcasts for search")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually move files")
    
    args = parser.parse_args()
    
    storage_manager = PodcastStorageManager()
    search_engine = PodcastSearchEngine()
    
    if args.analyze:
        analysis = storage_manager.analyze_storage()
        print("📊 Podcast Storage Analysis:")
        print(f"   Audio files: {analysis['total_audio_files']}")
        print(f"   Audio size: {analysis['total_audio_size_gb']} GB")
        print(f"   Transcripts: {analysis['total_transcripts']}")
        print(f"   Metadata files: {analysis['total_metadata']}")
    
    elif args.plan:
        plan = storage_manager.create_archive_plan()
        print("📋 Archive Plan:")
        print(f"   Keep local (high priority): {len(plan['keep_local'])} podcasts")
        print(f"   Archive audio (medium priority): {len(plan['archive_audio'])} podcasts")
        print(f"   Metadata only (low priority): {len(plan['metadata_only'])} podcasts")
        
        # Show space savings
        archive_size = sum(p["audio_size_mb"] for p in plan["archive_audio"]) / 1024
        delete_size = sum(p["audio_size_mb"] for p in plan["metadata_only"]) / 1024
        print(f"   Space to free: {archive_size + delete_size:.1f} GB")
    
    elif args.archive:
        results = storage_manager.execute_archive_plan(args.archive, dry_run=args.dry_run)
        action = "Would free" if args.dry_run else "Freed"
        print(f"✅ {action} {results['space_freed_gb']} GB")
        print(f"   Moved to local: {results['moved_to_local']} files")
        print(f"   Deleted: {results['deleted_audio']} files")
        if results["errors"]:
            print(f"   Errors: {len(results['errors'])}")
    
    elif args.index:
        count = search_engine.index_podcasts()
        print(f"📚 Indexed {count} podcast transcripts for search")
    
    elif args.search:
        results = search_engine.search_podcasts(args.search)
        print(f"🔍 Found {len(results)} podcast matches:")
        for i, result in enumerate(results[:5], 1):
            metadata = result.get("metadata", {})
            print(f"   {i}. {metadata.get('title', 'Unknown')} ({metadata.get('podcast_title', 'Unknown')})")
            print(f"      Score: {result.get('score', 0):.2f}")


if __name__ == "__main__":
    main()