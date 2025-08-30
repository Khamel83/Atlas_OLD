#!/usr/bin/env python3
"""
Enhanced HTML Processor with Trafilatura

Reprocesses all content to:
1. Remove 10K character limit 
2. Use trafilatura for proper content extraction
3. Remove ads, navigation, social buttons
4. Handle email newsletter formatting
"""

import sqlite3
from pathlib import Path
import trafilatura
from datetime import datetime
import re

class EnhancedContentProcessor:
    """Enhanced content processor using trafilatura"""
    
    def __init__(self):
        self.db_path = "atlas.db"
        
    def extract_clean_content(self, html_file):
        """Extract clean content using trafilatura"""
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()
            
            # Use trafilatura to extract main content
            extracted = trafilatura.extract(
                html_content,
                include_comments=False,      # No comments
                include_tables=True,         # Keep tables (data)
                include_links=False,         # Remove navigation links
                deduplicate=True,           # Remove duplicated text
                output_format='txt'          # Plain text
            )
            
            if not extracted:
                print(f"⚠️  Trafilatura failed on {html_file.name}, falling back to basic extraction")
                return self.fallback_extraction(html_content, html_file)
            
            # Get metadata too
            metadata = trafilatura.extract_metadata(html_content)
            
            # Extract URL from filename
            url = self.extract_url_from_filename(html_file)
            
            # Get title from metadata or filename
            title = "Unknown"
            if metadata and metadata.title:
                title = metadata.title
            elif html_file.stem:
                title = html_file.stem.replace('_', ' ')[:100]
            
            # Clean up extracted content
            cleaned_content = self.clean_extracted_text(extracted)
            
            return {
                'title': title[:500],
                'content': cleaned_content,  # NO character limit!
                'url': url[:500] if url else f"file://{html_file.name}",
                'filename': html_file.name,
                'extraction_method': 'trafilatura',
                'author': metadata.author if metadata and metadata.author else None,
                'date': metadata.date if metadata and metadata.date else None
            }
            
        except Exception as e:
            print(f"❌ Error with trafilatura on {html_file.name}: {e}")
            return self.fallback_extraction(html_content, html_file)
    
    def fallback_extraction(self, html_content, html_file):
        """Fallback extraction for when trafilatura fails"""
        from bs4 import BeautifulSoup
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove unwanted elements
        unwanted_tags = ['script', 'style', 'nav', 'footer', 'header', 'aside']
        unwanted_classes = ['ad', 'advertisement', 'social', 'share', 'navigation', 
                          'sidebar', 'footer', 'header', 'menu', 'comments']
        
        for tag in unwanted_tags:
            for element in soup.find_all(tag):
                element.decompose()
        
        for class_name in unwanted_classes:
            for element in soup.find_all(attrs={'class': re.compile(class_name, re.I)}):
                element.decompose()
        
        # Try semantic selectors first
        main_selectors = [
            'main', 'article', '.content', '.post', '.entry',
            '#content', '#main', '.article-body', '.post-body'
        ]
        
        text_content = ""
        for selector in main_selectors:
            main_elem = soup.select_one(selector)
            if main_elem:
                text_content = main_elem.get_text(separator=' ', strip=True)
                break
        
        if not text_content or len(text_content) < 100:
            text_content = soup.get_text(separator=' ', strip=True)
        
        # Clean up text
        cleaned_content = self.clean_extracted_text(text_content)
        
        # Get title
        title_elem = soup.find('title')
        title = title_elem.get_text().strip() if title_elem else html_file.stem
        
        url = self.extract_url_from_filename(html_file)
        
        return {
            'title': title[:500],
            'content': cleaned_content,  # NO character limit!
            'url': url[:500] if url else f"file://{html_file.name}",
            'filename': html_file.name,
            'extraction_method': 'fallback'
        }
    
    def clean_extracted_text(self, text):
        """Clean extracted text of email/newsletter artifacts"""
        if not text:
            return ""
        
        # Remove email newsletter artifacts
        cleaned = re.sub(r'\xa0|\u200c|\u200b', ' ', text)  # Remove unicode spaces
        cleaned = re.sub(r'\s+', ' ', cleaned)  # Normalize whitespace
        
        # Remove common newsletter/web artifacts
        artifacts_to_remove = [
            r'View in browser',
            r'Unsubscribe',
            r'Share on Twitter', 
            r'Share on Facebook',
            r'Share via Email',
            r'Forward to a friend',
            r'Print this email',
            r'Follow us on',
            r'© \d{4}.*?All rights reserved',
            r'This email was sent to',
            r'Update your preferences',
            r'Privacy Policy',
            r'Terms of Service',
            r'Click here to.*?(?:\.|!|\?)',
            r'Subscribe to.*?(?:\.|!|\?)',
        ]
        
        for pattern in artifacts_to_remove:
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
        
        # Remove excessive newlines and spaces
        cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
        cleaned = cleaned.strip()
        
        return cleaned
    
    def extract_url_from_filename(self, html_file):
        """Extract URL from filename"""
        url = ""
        filename_parts = html_file.stem.split('_')
        for part in filename_parts:
            if 'http' in part or '.com' in part:
                url = part.replace('_', '/')
                break
        return url
    
    def get_truncated_content(self):
        """Find content that was truncated at 10K chars"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT url, title, LENGTH(content) 
            FROM content 
            WHERE LENGTH(content) >= 9900
            ORDER BY LENGTH(content) DESC
        """)
        
        truncated = cursor.fetchall()
        conn.close()
        
        return truncated
    
    def reprocess_truncated_content(self, max_files=None):
        """Reprocess all truncated content"""
        
        print("🔍 Finding truncated content...")
        truncated = self.get_truncated_content()
        
        print(f"📊 Found {len(truncated)} items likely truncated at 10K chars")
        
        if max_files:
            truncated = truncated[:max_files]
            print(f"🎯 Processing first {max_files} truncated items")
        
        # Map filenames back to HTML files
        html_dir = Path("inputs/PROCESSED/html/")
        filename_to_path = {}
        
        for html_file in html_dir.glob("*.html"):
            filename_to_path[html_file.name] = html_file
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        processed = 0
        errors = 0
        not_found = 0
        
        for url, title, content_length in truncated:
            try:
                # Try to find matching HTML file by URL or title
                html_file = None
                
                # Try to find by filename in URL
                if url.startswith("file://"):
                    filename = url.replace("file://", "")
                    if filename in filename_to_path:
                        html_file = filename_to_path[filename]
                
                # If not found, try to match by title similarity
                if not html_file:
                    for file_path in filename_to_path.values():
                        file_title = file_path.stem.replace('_', ' ')
                        if title[:30] in file_title or file_title[:30] in title:
                            html_file = file_path
                            break
                
                if html_file:
                    # Re-extract with enhanced method
                    extracted = self.extract_clean_content(html_file)
                    
                    if extracted and len(extracted['content']) > content_length:
                        # Update database with better content
                        cursor.execute("""
                            UPDATE content 
                            SET content = ?, title = ?, updated_at = ?
                            WHERE url = ?
                        """, (
                            extracted['content'],
                            extracted['title'], 
                            datetime.now().isoformat(),
                            url
                        ))
                        
                        processed += 1
                        new_length = len(extracted['content'])
                        improvement = new_length - content_length
                        
                        print(f"✅ Enhanced: {title[:50]}... ({content_length}→{new_length}, +{improvement} chars)")
                        
                        if processed % 50 == 0:
                            conn.commit()  # Periodic commits
                    else:
                        print(f"⚠️  No improvement for {title[:50]}...")
                else:
                    not_found += 1
                    if not_found < 5:  # Only show first few
                        print(f"❌ HTML file not found for: {title[:50]}...")
                
            except Exception as e:
                errors += 1
                if errors < 5:  # Only show first few errors
                    print(f"❌ Error reprocessing {title[:50]}...: {e}")
        
        conn.commit()
        conn.close()
        
        print(f"\n🎉 REPROCESSING COMPLETE!")
        print(f"✅ Enhanced: {processed}")
        print(f"❌ Errors: {errors}")
        print(f"📁 Files not found: {not_found}")
        print(f"📊 Success rate: {processed/(processed+errors+not_found)*100:.1f}%")
        
        return processed

def main():
    """Main reprocessing function"""
    
    print("🚀 Atlas Enhanced Content Reprocessor")
    print("=" * 50)
    print("🎯 Removing 10K limit & improving content extraction")
    print("=" * 50)
    
    processor = EnhancedContentProcessor()
    
    # Check current truncated content
    truncated = processor.get_truncated_content()
    print(f"📊 Found {len(truncated)} items likely truncated")
    
    if len(truncated) == 0:
        print("✅ No truncated content found!")
        return True
    
    # Show sample of what will be reprocessed
    print(f"\n📄 Sample truncated content:")
    for i, (url, title, length) in enumerate(truncated[:5], 1):
        print(f"  {i}. {title[:60]}... ({length} chars)")
    
    # Ask for batch size
    import sys
    batch_size = None
    if len(sys.argv) > 1:
        try:
            batch_size = int(sys.argv[1])
            print(f"🎯 Processing {batch_size} items as requested")
        except ValueError:
            print("Usage: python enhanced_html_processor.py [batch_size]")
    
    # Reprocess content
    processed = processor.reprocess_truncated_content(batch_size)
    
    if processed > 0:
        print(f"\n🎉 SUCCESS! Enhanced {processed} articles")
        print(f"🧠 Atlas now has better quality content")
        print(f"📊 Content extraction improved with trafilatura")
    else:
        print(f"\n❌ No content was enhanced")
    
    return processed > 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)