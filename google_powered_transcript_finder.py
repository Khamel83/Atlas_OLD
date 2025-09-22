#!/usr/bin/env python3
"""
GOOGLE-POWERED TRANSCRIPT FINDER
Exhaustive Google Custom Search API implementation
Uses Google API until we hit limits - every possible query pattern
"""

import requests
import json
import time
import csv
import sqlite3
import os
from typing import List, Dict, Optional
from urllib.parse import urlparse

class GooglePoweredTranscriptFinder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        # Google API credentials
        self.google_api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
        self.google_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

        if not self.google_api_key or not self.google_engine_id:
            print("⚠️  Google API credentials not found in environment")
            print("   Set GOOGLE_SEARCH_API_KEY and GOOGLE_SEARCH_ENGINE_ID")

        self.db_path = "data/atlas.db"

        # Comprehensive list of transcript sites
        self.transcript_sites = [
            "fireflies.ai",
            "happyscribe.com",
            "otter.ai",
            "rev.com",
            "scribie.com",
            "sonix.ai",
            "trint.com",
            "podscripts.co",
            "podsights.com",
            "github.com",
            "medium.com",
            "substack.com",
            "archive.org",
            "youtube.com",
            "docs.google.com",
            "dropbox.com",
            "notion.so",
            "airtable.com",
            "pastebin.com",
            "gist.github.com",
            "reddit.com",
            "twitter.com",
            "transcript.com",
            "transcripts.com",
            "podtranscripts.com"
        ]

        # Comprehensive search terms
        self.search_terms = [
            "transcript",
            "full transcript",
            "episode transcript",
            "transcription",
            "full text",
            "episode text",
            "complete text",
            "read along",
            "show notes",
            "episode notes",
            "spoken word",
            "conversation text",
            "dialogue",
            "script",
            "written version",
            "text version"
        ]

        # Query patterns
        self.query_patterns = [
            '"{podcast}" {term}',
            '"{podcast}" "{term}"',
            '{podcast} {term}',
            '{podcast} episode {term}',
            '"{podcast}" complete {term}',
            '{podcast} {term} archive',
            '{podcast} {term} collection',
            'find {podcast} {term}',
            'where {podcast} {term}',
            '{podcast} {term} download',
            '{podcast} {term} pdf',
            '{podcast} {term} text file'
        ]

    def exhaustive_google_search(self, podcast_name: str) -> List[Dict]:
        """
        EXHAUSTIVE GOOGLE SEARCH using every possible combination
        """
        print(f"\n🔍 EXHAUSTIVE GOOGLE SEARCH: {podcast_name}")
        print("=" * 70)

        all_results = []
        query_count = 0

        # PHASE 1: Site-specific searches for each transcript site
        print("1️⃣ PHASE 1: Site-specific searches...")
        for site in self.transcript_sites:
            for term in self.search_terms:
                for pattern in self.query_patterns[:6]:  # Use first 6 patterns
                    query = pattern.format(podcast=podcast_name, term=term) + f" site:{site}"

                    print(f"   Query {query_count+1}: {query[:60]}...")
                    query_count += 1

                    results = self._execute_google_search(query)
                    for result in results:
                        transcript_data = self._test_url_for_transcript(result['link'])
                        if transcript_data:
                            all_results.append({
                                'url': result['link'],
                                'title': result['title'],
                                'domain': site,
                                'content': transcript_data,
                                'source': 'google_site_specific',
                                'query': query,
                                'content_length': len(transcript_data)
                            })
                            print(f"     ✅ FOUND: {len(transcript_data)} chars")

                    time.sleep(0.2)  # Rate limiting

                    # Break if we hit limits
                    if query_count >= 500:  # Google allows ~100 queries/day free
                        print(f"   ⚠️  Reached query limit: {query_count}")
                        break

                if query_count >= 500:
                    break
            if query_count >= 500:
                break

        # PHASE 2: General searches (no site restriction)
        if query_count < 500:
            print("2️⃣ PHASE 2: General searches...")
            for term in self.search_terms:
                for pattern in self.query_patterns:
                    query = pattern.format(podcast=podcast_name, term=term)

                    print(f"   Query {query_count+1}: {query[:60]}...")
                    query_count += 1

                    results = self._execute_google_search(query)
                    for result in results[:5]:  # Top 5 per query
                        transcript_data = self._test_url_for_transcript(result['link'])
                        if transcript_data:
                            all_results.append({
                                'url': result['link'],
                                'title': result['title'],
                                'domain': urlparse(result['link']).netloc,
                                'content': transcript_data,
                                'source': 'google_general',
                                'query': query,
                                'content_length': len(transcript_data)
                            })
                            print(f"     ✅ FOUND: {len(transcript_data)} chars")

                    time.sleep(0.2)

                    if query_count >= 500:
                        print(f"   ⚠️  Reached query limit: {query_count}")
                        break

                if query_count >= 500:
                    break

        # PHASE 3: Advanced search operators
        if query_count < 500:
            print("3️⃣ PHASE 3: Advanced search operators...")
            advanced_queries = [
                f'"{podcast_name}" filetype:pdf transcript',
                f'"{podcast_name}" filetype:txt transcript',
                f'"{podcast_name}" filetype:doc transcript',
                f'"{podcast_name}" intitle:transcript',
                f'"{podcast_name}" inurl:transcript',
                f'"{podcast_name}" "full episode" text',
                f'"{podcast_name}" transcript OR transcription OR "full text"',
                f'allintitle: {podcast_name} transcript',
                f'allinurl: {podcast_name} transcript',
                f'cache:{podcast_name} transcript',
                f'related:youtube.com {podcast_name} transcript'
            ]

            for query in advanced_queries:
                print(f"   Query {query_count+1}: {query[:60]}...")
                query_count += 1

                results = self._execute_google_search(query)
                for result in results:
                    transcript_data = self._test_url_for_transcript(result['link'])
                    if transcript_data:
                        all_results.append({
                            'url': result['link'],
                            'title': result['title'],
                            'domain': urlparse(result['link']).netloc,
                            'content': transcript_data,
                            'source': 'google_advanced',
                            'query': query,
                            'content_length': len(transcript_data)
                        })
                        print(f"     ✅ FOUND: {len(transcript_data)} chars")

                time.sleep(0.2)

                if query_count >= 500:
                    print(f"   ⚠️  Reached query limit: {query_count}")
                    break

        print(f"\n📊 GOOGLE SEARCH SUMMARY:")
        print(f"   Total queries executed: {query_count}")
        print(f"   Raw results found: {len(all_results)}")

        # Deduplicate and sort by quality
        unique_results = self._deduplicate_results(all_results)
        quality_results = self._filter_quality_transcripts(unique_results)

        print(f"   Unique results: {len(unique_results)}")
        print(f"   Quality transcripts: {len(quality_results)}")

        return quality_results

    def _execute_google_search(self, query: str, num_results: int = 10) -> List[Dict]:
        """Execute Google Custom Search API query"""
        if not self.google_api_key or not self.google_engine_id:
            return []

        try:
            url = "https://customsearch.googleapis.com/customsearch/v1"
            params = {
                'key': self.google_api_key,
                'cx': self.google_engine_id,
                'q': query,
                'num': num_results
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data.get('items', [])
            elif response.status_code == 429:
                print(f"     ⚠️  Rate limited - waiting 60 seconds...")
                time.sleep(60)
                return []
            else:
                print(f"     ❌ API error: {response.status_code}")
                return []

        except Exception as e:
            print(f"     ❌ Search error: {e}")
            return []

    def _test_url_for_transcript(self, url: str) -> Optional[str]:
        """Test if URL contains actual transcript content"""
        try:
            response = self.session.get(url, timeout=15)
            if response.status_code == 200:
                content = response.text

                # Quality checks for real transcripts
                if len(content) > 3000:  # Minimum length
                    transcript_indicators = [
                        "speaker:", "host:", "[music]", "welcome to",
                        "today we", "our guest", "transcript",
                        "speaker 1:", "speaker 2:", "[laughter]",
                        "interviewer:", "guest:", "[applause]",
                        "narrator:", "announcer:", "[sound effect]"
                    ]

                    indicators_found = sum(1 for indicator in transcript_indicators
                                         if indicator.lower() in content.lower())

                    # Must have multiple indicators for quality
                    if indicators_found >= 2:
                        return content

        except Exception:
            pass

        return None

    def _deduplicate_results(self, results: List[Dict]) -> List[Dict]:
        """Remove duplicate URLs and keep best quality"""
        url_map = {}

        for result in results:
            url = result['url']
            if url not in url_map or result['content_length'] > url_map[url]['content_length']:
                url_map[url] = result

        return list(url_map.values())

    def _filter_quality_transcripts(self, results: List[Dict]) -> List[Dict]:
        """Filter for high-quality transcripts only"""
        quality_results = []

        for result in results:
            content_length = result['content_length']
            if content_length > 20000:  # High quality: 20k+ chars
                result['quality'] = 'high'
                quality_results.append(result)
            elif content_length > 10000:  # Medium quality: 10k+ chars
                result['quality'] = 'medium'
                quality_results.append(result)
            elif content_length > 5000:   # Acceptable quality: 5k+ chars
                result['quality'] = 'acceptable'
                quality_results.append(result)

        # Sort by content length (quality)
        quality_results.sort(key=lambda x: x['content_length'], reverse=True)
        return quality_results

    def hunt_priority_podcasts_with_google(self):
        """Run Google-powered hunt on priority podcasts"""
        print("🚀 GOOGLE-POWERED TRANSCRIPT HUNT")
        print("Using Google Custom Search API until limits")
        print("=" * 70)

        # Priority podcasts
        priority_podcasts = [
            "Acquired",
            "Hard Fork",
            "EconTalk",
            "Conversations with Tyler",
            "Lex Fridman Podcast",
            "Practical AI",
            "Planet Money",
            "99% Invisible",
            "This American Life",
            "Radiolab",
            "The Tim Ferriss Show",
            "Joe Rogan Experience",
            "a16z Podcast",
            "The Vergecast",
            "Decoder with Nilay Patel"
        ]

        all_findings = {}
        total_transcripts = 0

        for i, podcast_name in enumerate(priority_podcasts):
            print(f"\n[{i+1}/{len(priority_podcasts)}] GOOGLE HUNTING: {podcast_name}")

            findings = self.exhaustive_google_search(podcast_name)

            if findings:
                all_findings[podcast_name] = findings
                total_transcripts += len(findings)
                print(f"🎯 SUCCESS: {len(findings)} quality transcripts found!")

                # Store in database
                self._store_findings(podcast_name, findings)

                # Show best finding
                best_finding = max(findings, key=lambda x: x['content_length'])
                print(f"   Best: {best_finding['domain']} ({best_finding['content_length']:,} chars)")
            else:
                print(f"❌ NO TRANSCRIPTS: Google search exhausted")

            # Rate limiting between podcasts
            time.sleep(5)

        # Save comprehensive results
        output_file = "config/google_hunt_results.json"
        with open(output_file, 'w') as f:
            json.dump(all_findings, f, indent=2)

        print(f"\n🎉 GOOGLE HUNT COMPLETE!")
        print(f"📊 Results saved to: {output_file}")
        print(f"🏆 Successful podcasts: {len(all_findings)}")
        print(f"📝 Total transcripts found: {total_transcripts}")

        return all_findings

    def _store_findings(self, podcast_name: str, findings: List[Dict]):
        """Store findings in database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            for finding in findings:
                cursor.execute('''
                    INSERT OR REPLACE INTO content (title, content, content_type, url, created_at)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    f"{podcast_name} - Google Found Transcript",
                    finding['content'],
                    'podcast_transcript',
                    finding['url'],
                    time.strftime('%Y-%m-%d %H:%M:%S')
                ))

            conn.commit()
            conn.close()
            print(f"   💾 Stored {len(findings)} Google transcripts in database")

        except Exception as e:
            print(f"   ❌ Database error: {e}")

if __name__ == "__main__":
    finder = GooglePoweredTranscriptFinder()
    finder.hunt_priority_podcasts_with_google()