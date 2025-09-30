"""
Configuration Management for Atlas v2

Loads and manages configuration from CSV/JSON files
"""

import csv
import json
import logging
from pathlib import Path
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class ConfigManager:
    """Manages all configuration for Atlas v2"""

    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.sources = {}
        self.extraction_patterns = {}
        self.rate_limits = {}
        self.load_all_config()

    def load_all_config(self):
        """Load all configuration files"""
        try:
            self.load_sources()
            self.load_extraction_patterns()
            self.load_rate_limits()
            logger.info("✅ Configuration loaded successfully")
        except Exception as e:
            logger.error(f"❌ Configuration loading failed: {e}")

    def load_sources(self):
        """Load sources from CSV"""
        sources_file = self.config_dir / "sources.csv"
        if sources_file.exists():
            with open(sources_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.sources[row['source_name']] = row
            logger.info(f"📊 Loaded {len(self.sources)} sources")

    def load_extraction_patterns(self):
        """Load extraction patterns from JSON"""
        patterns_file = self.config_dir / "extraction_patterns.json"
        if patterns_file.exists():
            with open(patterns_file, 'r') as f:
                self.extraction_patterns = json.load(f)
            logger.info(f"🎯 Loaded extraction patterns for {len(self.extraction_patterns)} domains")

    def load_rate_limits(self):
        """Load rate limits from JSON"""
        limits_file = self.config_dir / "rate_limits.json"
        if limits_file.exists():
            with open(limits_file, 'r') as f:
                self.rate_limits = json.load(f)
        else:
            # Default rate limits
            self.rate_limits = {
                "global_default": 3,
                "domains": {},
                "per_hour_limits": {"global_default": 100}
            }

    def get_source_config(self, source_name: str) -> Dict[str, Any]:
        """Get configuration for a specific source"""
        return self.sources.get(source_name, {})

    def get_extraction_pattern(self, domain: str) -> Dict[str, Any]:
        """Get extraction pattern for a domain"""
        return self.extraction_patterns.get(domain, {})