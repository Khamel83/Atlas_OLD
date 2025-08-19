#!/bin/bash
"""
SSL Setup for Atlas
Installs and configures Let's Encrypt SSL certificate
"""

# Exit on any error
set -e

# Configuration
DOMAIN="atlas.khamel.com"
EMAIL="your-email@example.com"
WEBROOT="/var/www/html"

echo "Starting SSL setup for $DOMAIN..."

# Update package list
echo "Updating package list..."
sudo apt update

# Install Certbot
echo "Installing Certbot..."
sudo apt install -y certbot python3-certbot-nginx

# Create webroot directory if it doesn't exist
echo "Creating webroot directory..."
sudo mkdir -p $WEBROOT

# Obtain SSL certificate
echo "Obtaining SSL certificate..."
sudo certbot certonly --webroot -w $WEBROOT -d $DOMAIN --email $EMAIL --agree-tos --non-interactive

# Check if certificate was obtained successfully
if [ ! -d "/etc/letsencrypt/live/$DOMAIN" ]; then
    echo "ERROR: Failed to obtain SSL certificate for $DOMAIN"
    exit 1
fi

echo "SSL certificate obtained successfully!"

# Set up automatic renewal
echo "Setting up automatic certificate renewal..."
# Add cron job for certificate renewal
(crontab -l 2>/dev/null; echo "0 2 * * 1 sudo certbot renew --quiet") | crontab -

# Configure nginx SSL termination
echo "Configuring nginx for SSL..."
sudo tee /etc/nginx/sites-available/atlas << EOF
server {
    listen 80;
    server_name $DOMAIN;
    
    # Redirect all HTTP requests to HTTPS
    return 301 https://\$server_name\$request_uri;
}

server {
    listen 443 ssl;
    server_name $DOMAIN;
    
    ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    
    # Add security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
    
    # Atlas application reverse proxy
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable the site
sudo ln -sf /etc/nginx/sites-available/atlas /etc/nginx/sites-enabled/

# Test nginx configuration
echo "Testing nginx configuration..."
sudo nginx -t

# Reload nginx
echo "Reloading nginx..."
sudo systemctl reload nginx

echo "SSL setup completed successfully!"
echo "Your site should now be accessible at https://$DOMAIN"
echo "Certificate will automatically renew 30 days before expiration"