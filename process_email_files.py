#!/usr/bin/env python3
"""
Process email files from inputs/PROCESSED/emails/
"""

import sqlite3
import os
import email
import re
from datetime import datetime
from pathlib import Path
from email.header import decode_header

def decode_email_header(header):
    """Decode email header properly"""
    if not header:
        return ""
    
    decoded = decode_header(header)
    parts = []
    for part, encoding in decoded:
        if isinstance(part, bytes):
            parts.append(part.decode(encoding or 'utf-8', errors='ignore'))
        else:
            parts.append(str(part))
    return ''.join(parts)

def extract_email_content(email_path):
    """Extract content from email file"""
    try:
        with open(email_path, 'rb') as f:
            msg = email.message_from_bytes(f.read())
        
        # Get subject
        subject = decode_email_header(msg.get('Subject', ''))
        
        # Get content
        content_parts = []
        
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    payload = part.get_payload(decode=True)
                    if payload:
                        content_parts.append(payload.decode('utf-8', errors='ignore'))
                elif part.get_content_type() == 'text/html':
                    payload = part.get_payload(decode=True)
                    if payload:
                        # Simple HTML stripping
                        html_content = payload.decode('utf-8', errors='ignore')
                        # Remove HTML tags
                        clean_text = re.sub(r'<[^>]+>', ' ', html_content)
                        content_parts.append(clean_text)
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                content_parts.append(payload.decode('utf-8', errors='ignore'))
        
        content = '\n'.join(content_parts).strip()
        
        # Clean up content
        content = re.sub(r'\s+', ' ', content)
        
        return {
            'title': subject,
            'content': content,
            'url': str(email_path)
        }
        
    except Exception as e:
        print(f"❌ Error processing {email_path}: {e}")
        return None

def process_email_files():
    """Process all email files"""
    
    print("📧 PROCESSING EMAIL FILES")
    print("=" * 30)
    
    email_dir = Path("inputs/PROCESSED/emails/")
    if not email_dir.exists():
        print(f"❌ Directory not found: {email_dir}")
        return 0
    
    email_files = list(email_dir.glob("*.eml"))
    print(f"📊 Found {len(email_files)} email files")
    
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    processed = 0
    errors = 0
    
    for i, email_file in enumerate(email_files, 1):
        email_data = extract_email_content(email_file)
        
        if email_data and email_data['content'] and len(email_data['content']) > 200:
            try:
                cursor.execute("""
                    INSERT OR IGNORE INTO content 
                    (url, title, content, created_at)
                    VALUES (?, ?, ?, ?)
                """, (
                    email_data['url'],
                    email_data['title'][:500],
                    email_data['content'],
                    datetime.now().isoformat()
                ))
                
                if cursor.rowcount > 0:
                    processed += 1
                    print(f"  {i:3}. ✅ {email_data['title'][:50]}...")
                else:
                    print(f"  {i:3}. ➖ Duplicate: {email_data['title'][:40]}...")
                    
            except Exception as e:
                errors += 1
                print(f"  {i:3}. ❌ Save error: {e}")
        else:
            errors += 1
            
        if i % 100 == 0:
            conn.commit()
            print(f"      💾 Committed batch at {i}")
    
    conn.commit()
    conn.close()
    
    print(f"\n📊 EMAIL PROCESSING COMPLETE!")
    print(f"✅ Files processed: {processed}")
    print(f"❌ Errors: {errors}")
    
    return processed

if __name__ == "__main__":
    process_email_files()