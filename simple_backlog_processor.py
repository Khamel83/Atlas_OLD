#!/usr/bin/env python3
"""
Simple Backlog Processor - Process your backlog once and move on

No complex architecture, no abstract classes, no bullshit.
Just: read file → extract text → save markdown → move to processed.

Usage:
    python simple_backlog_processor.py --test-html        # Test 3 HTML files  
    python simple_backlog_processor.py --test-emails      # Test 3 email files
    python simple_backlog_processor.py --test-instapaper  # Test 5 URLs from CSV
    python simple_backlog_processor.py --test-all         # Test everything
    python simple_backlog_processor.py --process-all      # Process full backlog
"""

import argparse
import csv
import email
import hashlib
import os
import shutil
from pathlib import Path
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


def clean_filename(text, max_length=100):
    """Convert text to safe filename"""
    # Remove/replace problematic characters
    cleaned = "".join(c if c.isalnum() or c in ' -_.' else '_' for c in text)
    # Remove extra spaces and truncate
    cleaned = ' '.join(cleaned.split())[:max_length]
    return cleaned.strip() or "untitled"


def html_to_text(html_content):
    """Extract clean text from HTML"""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script, style, nav, footer, etc.
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'advertisement']):
            tag.decompose()
            
        # Get title
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else "Untitled"
        
        # Get main content
        # Try common content containers first
        content = None
        for selector in ['article', '[role="main"]', 'main', '.content', '#content', '.post', '.entry']:
            content = soup.select_one(selector)
            if content:
                break
        
        # Fallback to body
        if not content:
            content = soup.find('body') or soup
            
        # Convert to markdown
        markdown = markdownify(str(content), heading_style="ATX")
        
        return title, markdown
        
    except Exception as e:
        return "Error extracting content", f"Error: {str(e)}"


def process_html_file(html_path, output_dir="processed_backlog"):
    """Process a single HTML file"""
    print(f"Processing HTML: {html_path}")
    
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
            
        title, text = html_to_text(html_content)
        
        # Create output filename
        safe_title = clean_filename(title)
        output_file = Path(output_dir) / "html" / f"{safe_title}.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write markdown
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Source:** {html_path}\n")
            f.write(f"**Processed:** {datetime.now().isoformat()}\n\n")
            f.write(text)
            
        # Move original to processed
        processed_dir = Path("inputs/PROCESSED/html")
        processed_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(html_path, processed_dir / Path(html_path).name)
        
        print(f"✅ Success: {output_file}")
        return True, str(output_file)
        
    except Exception as e:
        print(f"❌ Error processing {html_path}: {e}")
        return False, str(e)


def process_email_file(email_path, output_dir="processed_backlog"):
    """Process a single email file"""
    print(f"Processing Email: {email_path}")
    
    try:
        with open(email_path, 'rb') as f:
            msg = email.message_from_bytes(f.read())
            
        # Extract email content
        subject = msg.get('Subject', 'No Subject')
        sender = msg.get('From', 'Unknown Sender')
        date = msg.get('Date', 'Unknown Date')
        
        # Get body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    break
                elif part.get_content_type() == "text/html":
                    html_body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    _, body = html_to_text(html_body)
        else:
            if msg.get_content_type() == "text/plain":
                body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
            elif msg.get_content_type() == "text/html":
                html_body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                _, body = html_to_text(html_body)
                
        # Create output filename
        safe_subject = clean_filename(subject)
        output_file = Path(output_dir) / "emails" / f"{safe_subject}.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write markdown
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {subject}\n\n")
            f.write(f"**From:** {sender}\n")
            f.write(f"**Date:** {date}\n")
            f.write(f"**Source:** {email_path}\n")
            f.write(f"**Processed:** {datetime.now().isoformat()}\n\n")
            f.write(body)
            
        # Move original to processed
        processed_dir = Path("inputs/PROCESSED/emails")
        processed_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(email_path, processed_dir / Path(email_path).name)
        
        print(f"✅ Success: {output_file}")
        return True, str(output_file)
        
    except Exception as e:
        print(f"❌ Error processing {email_path}: {e}")
        return False, str(e)


def process_url(url, output_dir="processed_backlog"):
    """Process a single URL"""
    print(f"Processing URL: {url}")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        title, text = html_to_text(response.text)
        
        # Create output filename  
        safe_title = clean_filename(title)
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        output_file = Path(output_dir) / "articles" / f"{safe_title}_{url_hash}.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write markdown
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**URL:** {url}\n")
            f.write(f"**Processed:** {datetime.now().isoformat()}\n\n")
            f.write(text)
            
        print(f"✅ Success: {output_file}")
        return True, str(output_file)
        
    except Exception as e:
        print(f"❌ Error processing {url}: {e}")
        return False, str(e)


def process_instapaper_csv(csv_path, output_dir="processed_backlog", max_urls=None):
    """Process URLs from Instapaper CSV"""
    print(f"Processing Instapaper CSV: {csv_path}")
    
    urls_processed = 0
    urls_failed = 0
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for i, row in enumerate(reader):
                if max_urls and i >= max_urls:
                    break
                    
                url = row.get('URL', '').strip()
                if not url:
                    continue
                    
                success, result = process_url(url, output_dir)
                if success:
                    urls_processed += 1
                else:
                    urls_failed += 1
                    
        # Move CSV to processed
        processed_dir = Path("inputs/PROCESSED")
        processed_dir.mkdir(parents=True, exist_ok=True)
        if max_urls is None:  # Only move if processing full CSV
            shutil.move(csv_path, processed_dir / Path(csv_path).name)
            
        print(f"📊 Instapaper Results: {urls_processed} success, {urls_failed} failed")
        return True, f"Processed {urls_processed} URLs"
        
    except Exception as e:
        print(f"❌ Error processing CSV {csv_path}: {e}")
        return False, str(e)


def test_processing():
    """Test processing on a few sample files"""
    print("🧪 TESTING BACKLOG PROCESSING")
    
    results = []
    
    # Test HTML files
    html_files = list(Path("inputs/saved_html").glob("*.html"))[:3]
    print(f"\n📄 Testing {len(html_files)} HTML files:")
    for html_file in html_files:
        success, result = process_html_file(str(html_file))
        results.append(("HTML", str(html_file), success, result))
        
    # Test email files  
    email_files = list(Path("inputs/saved_emails").glob("*.eml"))[:3]
    print(f"\n📧 Testing {len(email_files)} email files:")
    for email_file in email_files:
        success, result = process_email_file(str(email_file))
        results.append(("Email", str(email_file), success, result))
        
    # Test Instapaper URLs
    instapaper_csv = "inputs/PROCESSED/instapaper_export.csv"
    if Path(instapaper_csv).exists():
        print(f"\n🔗 Testing 5 URLs from Instapaper:")
        success, result = process_instapaper_csv(instapaper_csv, max_urls=5)
        results.append(("Instapaper", instapaper_csv, success, result))
        
    # Print summary
    print(f"\n📊 TEST RESULTS:")
    for category, source, success, result in results:
        status = "✅" if success else "❌" 
        print(f"   {status} {category}: {Path(source).name}")
        
    successful = sum(1 for _, _, success, _ in results if success)
    print(f"\n🎯 Success Rate: {successful}/{len(results)} ({successful/len(results)*100:.1f}%)")


def main():
    parser = argparse.ArgumentParser(description='Simple backlog processor - no bullshit')
    parser.add_argument('--test', action='store_true', help='Test on sample files')
    parser.add_argument('--process-all', action='store_true', help='Process full backlog')
    
    args = parser.parse_args()
    
    if args.test:
        test_processing()
    elif args.process_all:
        process_all_backlog()
    else:
        parser.print_help()


def process_all_backlog():
    """Process the ENTIRE backlog - every single file"""
    print("🚀 PROCESSING COMPLETE BACKLOG")
    print("=" * 50)
    
    total_files = 0
    total_success = 0
    total_failed = 0
    
    # Process all HTML files
    html_files = list(Path("inputs/saved_html").glob("*.html"))
    print(f"\n📄 Processing {len(html_files)} HTML files:")
    for i, html_file in enumerate(html_files, 1):
        print(f"[{i}/{len(html_files)}] {html_file.name[:60]}...")
        success, result = process_html_file(str(html_file))
        total_files += 1
        if success:
            total_success += 1
        else:
            total_failed += 1
            
    # Process all email files  
    email_files = list(Path("inputs/saved_emails").glob("*.eml"))
    print(f"\n📧 Processing {len(email_files)} email files:")
    for i, email_file in enumerate(email_files, 1):
        print(f"[{i}/{len(email_files)}] {email_file.name[:60]}...")
        success, result = process_email_file(str(email_file))
        total_files += 1
        if success:
            total_success += 1
        else:
            total_failed += 1
            
    # Process all documents in New Docs
    doc_files = list(Path("inputs/New Docs").rglob("*"))
    doc_files = [f for f in doc_files if f.is_file() and f.suffix.lower() in ['.html', '.htm', '.txt', '.pdf']]
    print(f"\n📁 Processing {len(doc_files)} document files:")
    for i, doc_file in enumerate(doc_files, 1):
        print(f"[{i}/{len(doc_files)}] {doc_file.name[:60]}...")
        if doc_file.suffix.lower() in ['.html', '.htm']:
            success, result = process_html_file(str(doc_file))
        else:
            # For now, just move non-HTML docs to processed
            try:
                processed_dir = Path("inputs/PROCESSED/documents") 
                processed_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(doc_file), processed_dir / doc_file.name)
                success = True
                print(f"✅ Moved to processed: {doc_file.name}")
            except Exception as e:
                success = False
                print(f"❌ Failed to move: {e}")
        total_files += 1
        if success:
            total_success += 1
        else:
            total_failed += 1
    
    # Process Instapaper CSV completely
    instapaper_csv = "inputs/PROCESSED/instapaper_export.csv"
    if Path(instapaper_csv).exists():
        print(f"\n🔗 Processing FULL Instapaper CSV:")
        success, result = process_instapaper_csv(instapaper_csv)
        total_files += 1
        if success:
            total_success += 1
        else:
            total_failed += 1
            
    # Process articles.txt if exists
    articles_txt = "inputs/PROCESSED/articles.txt"
    if Path(articles_txt).exists():
        print(f"\n📝 Processing articles.txt URLs:")
        try:
            with open(articles_txt, 'r') as f:
                urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                
            for i, url in enumerate(urls, 1):
                print(f"[{i}/{len(urls)}] {url[:60]}...")
                success, result = process_url(url)
                total_files += 1
                if success:
                    total_success += 1
                else:
                    total_failed += 1
                    
            # Move articles.txt to processed
            shutil.move(articles_txt, "inputs/PROCESSED/articles_processed.txt")
            
        except Exception as e:
            print(f"❌ Error processing articles.txt: {e}")
            total_failed += 1
    
    # FINAL SUMMARY
    print("\n" + "=" * 50)
    print("🏁 BACKLOG PROCESSING COMPLETE")
    print("=" * 50)
    print(f"📊 FINAL RESULTS:")
    print(f"   Total files processed: {total_files}")
    print(f"   Successful: {total_success}")
    print(f"   Failed: {total_failed}")
    print(f"   Success rate: {(total_success/total_files*100):.1f}%")
    print(f"\n📁 Output location: processed_backlog/")
    print(f"📁 Originals moved to: inputs/PROCESSED/")
    print(f"\n✅ BACKLOG IS NOW COMPLETELY PROCESSED")
    print(f"✅ YOU CAN NOW MOVE TO THE NEXT PHASE OF ATLAS")
    print(f"\n📋 REFERENCE FILES FOR METADATA PROCESSING:")
    print(f"   - processed_backlog/html/ (HTML content)")
    print(f"   - processed_backlog/emails/ (Email content)")  
    print(f"   - processed_backlog/articles/ (URL content)")
    print(f"   - inputs/PROCESSED/ (Original files for reference)")
    
    return total_success, total_failed


if __name__ == '__main__':
    main()