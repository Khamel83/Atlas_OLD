#!/usr/bin/env python3
"""
SSL Setup Script for Atlas

This script automates the setup of Let's Encrypt SSL certificates for Atlas
running on an OCI VM. It configures nginx for SSL termination and HTTPS redirect.

Features:
- Installs Certbot for Let's Encrypt certificate management
- Generates SSL certificates for specified domain
- Configures nginx for SSL termination
- Sets up automatic certificate renewal
- Implements HTTPS redirect for all HTTP traffic
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, description=""):
    """Run a shell command with error handling"""
    try:
        print(f"Executing: {description}")
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"Success: {description}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {description}")
        print(f"Error: {e.stderr}")
        sys.exit(1)

def install_certbot():
    """Install Certbot for Let's Encrypt"""
    print("Installing Certbot...")
    
    # Update package list
    run_command("sudo apt-get update", "Updating package list")
    
    # Install Certbot
    run_command("sudo apt-get install -y certbot python3-certbot-nginx", "Installing Certbot")
    
    print("Certbot installed successfully")

def configure_nginx():
    """Configure nginx for Atlas"""
    print("Configuring nginx...")
    
    # Get domain from environment variable
    domain = os.environ.get('ATLAS_DOMAIN', 'atlas.khamel.com')
    
    # Create nginx configuration for Atlas
    nginx_config = f"""
server {{
    listen 80;
    server_name {domain};
    
    location /.well-known/acme-challenge/ {{
        root /var/www/certbot;
    }}
    
    location / {{
        return 301 https://$host$request_uri;
    }}
}}

server {{
    listen 443 ssl;
    server_name {domain};
    
    ssl_certificate /etc/letsencrypt/live/{domain}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{domain}/privkey.pem;
    
    # SSL configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    
    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
    
    location / {{
        proxy_pass http://localhost:5000;  # Assuming Atlas runs on port 5000
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}
}}
"""
    
    # Write nginx config
    with open("/tmp/atlas_nginx.conf", "w") as f:
        f.write(nginx_config)
    
    # Install configuration
    run_command("sudo cp /tmp/atlas_nginx.conf /etc/nginx/sites-available/atlas", "Installing nginx configuration")
    run_command("sudo ln -sf /etc/nginx/sites-available/atlas /etc/nginx/sites-enabled/", "Enabling nginx configuration")
    run_command("sudo mkdir -p /var/www/certbot", "Creating certbot directory")
    run_command("sudo nginx -t", "Testing nginx configuration")
    run_command("sudo systemctl reload nginx", "Reloading nginx")
    
    print("nginx configured successfully")

def obtain_certificate(domain, email):
    """Obtain Let's Encrypt certificate"""
    print(f"Obtaining certificate for {domain}...")
    
    # Run certbot to obtain certificate
    cmd = f"sudo certbot --nginx -d {domain} --non-interactive --agree-tos --email {email}"
    run_command(cmd, "Obtaining SSL certificate")
    
    print("Certificate obtained successfully")

def setup_auto_renewal():
    """Setup automatic certificate renewal"""
    print("Setting up automatic certificate renewal...")
    
    # Create cron job for certificate renewal
    cron_job = "0 12 * * * /usr/bin/certbot renew --quiet"
    
    # Add to crontab
    current_crontab = run_command("crontab -l", "Getting current crontab").strip()
    new_crontab = current_crontab + "\n" + cron_job if current_crontab else cron_job
    
    with open("/tmp/new_crontab", "w") as f:
        f.write(new_crontab + "\n")
    
    run_command("crontab /tmp/new_crontab", "Installing new crontab")
    
    # Test renewal process
    run_command("sudo certbot renew --dry-run", "Testing certificate renewal")
    
    print("Automatic certificate renewal setup successfully")

def test_ssl_configuration():
    """Test SSL configuration"""
    print("Testing SSL configuration...")
    
    # Get domain from environment variable
    domain = os.environ.get('ATLAS_DOMAIN', 'atlas.khamel.com')
    
    # Check if certificate files exist
    cert_path = f"/etc/letsencrypt/live/{domain}/fullchain.pem"
    key_path = f"/etc/letsencrypt/live/{domain}/privkey.pem"
    
    if os.path.exists(cert_path) and os.path.exists(key_path):
        print("SSL certificate files found")
    else:
        print("Warning: SSL certificate files not found")
    
    # Test nginx configuration
    run_command("sudo nginx -t", "Testing nginx configuration")
    
    print("SSL configuration test completed")

def main():
    """Main SSL setup function"""
    print("Starting SSL setup for Atlas...")
    
    # Get configuration from environment variables
    domain = os.environ.get('ATLAS_DOMAIN')
    email = os.environ.get('ATLAS_ADMIN_EMAIL')
    
    # Validate required environment variables
    if not domain:
        print("Error: ATLAS_DOMAIN environment variable is not set")
        sys.exit(1)
    
    if not email:
        print("Error: ATLAS_ADMIN_EMAIL environment variable is not set")
        sys.exit(1)
    
    print(f"Configuring SSL for domain: {domain}")
    print(f"Using admin email: {email}")
    
    # Install Certbot
    install_certbot()
    
    # Configure nginx
    configure_nginx()
    
    # Obtain certificate
    obtain_certificate(domain, email)
    
    # Setup auto-renewal
    setup_auto_renewal()
    
    # Test configuration
    test_ssl_configuration()
    
    print("\nSSL setup completed successfully!")
    print("Your Atlas instance is now secured with:")
    print(f"- SSL certificate for {domain}")
    print("- Automatic certificate renewal")
    print("- HTTPS redirect for all HTTP traffic")
    print("- Security headers for protection against common attacks")
    
    print("\nNext steps:")
    print("1. Verify DNS is pointing to your OCI VM")
    print(f"2. Test access to https://{domain}")
    print("3. Update any Atlas configuration to use HTTPS")

if __name__ == "__main__":
    main()