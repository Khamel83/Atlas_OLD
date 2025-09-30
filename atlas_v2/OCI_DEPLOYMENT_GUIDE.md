# OCI Always-Free Deployment Guide

**Complete step-by-step guide to deploy Atlas v2 on Oracle Cloud Infrastructure Always-Free tier.**

## 🎯 **What You'll Get**

- **Atlas v2 running at `atlas.khamel.com/v2`**
- **4 ARM cores, 24GB RAM, 200GB storage**
- **$0/month forever** (just login every 90 days)
- **All your content preserved and migrated**

## 📋 **Prerequisites**

- Oracle Cloud account ([sign up free](https://cloud.oracle.com/))
- SSH key pair
- Access to your DNS provider (for khamel.com)

## 🚀 **Step 1: Create OCI Instance**

### **1.1 Login to Oracle Cloud**
```
1. Go to https://cloud.oracle.com/
2. Click "Sign in to Cloud"
3. Enter your cloud account details
```

### **1.2 Create Compute Instance**
```
1. In OCI Console, click "Create a VM instance"
2. Configure:

   Name: atlas-v2-production

   Image:
   - Click "Change Image"
   - Select "Ubuntu"
   - Choose "Ubuntu 22.04" (Always Free Eligible)

   Shape:
   - Click "Change Shape"
   - Select "Ampere" (ARM-based)
   - Choose "VM.Standard.A1.Flex"
   - Set OCPUs: 4 (maximum for free tier)
   - Set Memory: 24 GB (maximum for free tier)

   Networking:
   - Leave defaults (creates new VCN)
   - Ensure "Assign a public IPv4 address" is checked

   SSH Keys:
   - Upload your public SSH key
   - Or generate new key pair (download private key)

   Boot Volume:
   - Size: 200 GB (maximum for free tier)

3. Click "Create"
```

### **1.3 Note Your Instance Details**
```
After creation, note:
- Public IP Address: (e.g., 123.456.789.012)
- Username: ubuntu
- SSH Command: ssh -i your-key.pem ubuntu@123.456.789.012
```

### **1.4 Configure Security Rules**
```
1. In OCI Console, go to your instance
2. Click "Virtual Cloud Network" link
3. Click "Security Lists" > "Default Security List"
4. Click "Add Ingress Rules"

Add these rules:
- Port 22 (SSH): Source 0.0.0.0/0
- Port 80 (HTTP): Source 0.0.0.0/0
- Port 443 (HTTPS): Source 0.0.0.0/0
- Port 8000 (Atlas): Source 0.0.0.0/0

5. Click "Add Ingress Rules"
```

## 🔧 **Step 2: Setup Server**

### **2.1 Connect to Instance**
```bash
# Replace with your key and IP
ssh -i ~/.ssh/your-oci-key.pem ubuntu@YOUR-OCI-IP

# First time connection will ask to verify fingerprint - type "yes"
```

### **2.2 Update System**
```bash
sudo apt update && sudo apt upgrade -y
```

### **2.3 Install Docker**
```bash
# Install Docker
sudo apt install -y docker.io docker-compose git curl

# Add ubuntu user to docker group
sudo usermod -aG docker ubuntu

# Apply group changes
newgrp docker

# Verify Docker works
docker --version
docker-compose --version
```

### **2.4 Install Additional Tools**
```bash
# Install useful tools
sudo apt install -y htop ncdu tree jq sqlite3

# Install Let's Encrypt for SSL
sudo apt install -y certbot python3-certbot-nginx
```

## 📦 **Step 3: Deploy Atlas v2**

### **3.1 Clone Atlas Repository**
```bash
# Clone your Atlas repository
git clone https://github.com/Khamel83/Atlas.git
cd Atlas/atlas_v2

# Verify files are there
ls -la
```

### **3.2 Configure Environment**
```bash
# Generate secure webhook token
WEBHOOK_TOKEN=$(openssl rand -hex 32)

# Create environment file
cat > .env << EOF
WEBHOOK_SECRET_TOKEN=${WEBHOOK_TOKEN}
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO
EOF

# Show webhook token (save this for Vejla later)
echo "Your webhook token: ${WEBHOOK_TOKEN}"
```

### **3.3 Build and Start Atlas v2**
```bash
# Build Docker containers
docker-compose build

# Start Atlas v2
docker-compose up -d

# Check if it's running
docker ps
docker logs atlas-v2
```

### **3.4 Verify Atlas v2 Works**
```bash
# Test health endpoint
curl http://localhost:8000/health

# Should return:
# {"status":"healthy","version":"2.0.0",...}

# Test from outside (replace YOUR-OCI-IP)
curl http://YOUR-OCI-IP:8000/health
```

## 🌐 **Step 4: Configure Domain**

### **4.1 Setup DNS**

**Option A: Subdomain (Recommended)**
```
In your DNS provider (where khamel.com is hosted):

Add A Record:
- Name: v2.atlas
- Value: YOUR-OCI-IP
- TTL: 300

Result: v2.atlas.khamel.com points to Atlas v2
```

**Option B: Path-based routing**
```
If atlas.khamel.com is on a different server, add reverse proxy:

# On atlas.khamel.com server (if using nginx):
sudo nano /etc/nginx/sites-available/atlas

# Add this location block:
location /v2/ {
    proxy_pass http://YOUR-OCI-IP:8000/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

# Test and reload nginx:
sudo nginx -t
sudo nginx -s reload
```

### **4.2 Setup SSL Certificate**
```bash
# On OCI instance, install nginx for SSL termination
sudo apt install -y nginx

# Create nginx config for Atlas v2
sudo tee /etc/nginx/sites-available/atlas-v2 << EOF
server {
    listen 80;
    server_name v2.atlas.khamel.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable site
sudo ln -s /etc/nginx/sites-available/atlas-v2 /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# Get SSL certificate
sudo certbot --nginx -d v2.atlas.khamel.com
```

### **4.3 Test Domain Access**
```bash
# Test your domain
curl https://v2.atlas.khamel.com/health

# Should return Atlas v2 health status
```

## 📊 **Step 5: Migrate Your Data**

### **5.1 Prepare Migration on Local Machine**
```bash
# On your local Atlas machine:
cd /home/ubuntu/dev/atlas

# Run migration export
python3 atlas_v2_migration.py

# This creates atlas_v2_migration/ directory with all your data
ls -la atlas_v2_migration/
```

### **5.2 Transfer Data to OCI**
```bash
# From local machine, transfer migration data:
scp -i ~/.ssh/your-oci-key.pem -r atlas_v2_migration/ ubuntu@YOUR-OCI-IP:/home/ubuntu/

# Verify transfer
ssh -i ~/.ssh/your-oci-key.pem ubuntu@YOUR-OCI-IP "ls -la /home/ubuntu/atlas_v2_migration/"
```

### **5.3 Import Data on OCI**
```bash
# SSH to OCI instance
ssh -i ~/.ssh/your-oci-key.pem ubuntu@YOUR-OCI-IP

# Go to Atlas v2 directory
cd Atlas/atlas_v2

# Run import script
python3 import_migration_data.py

# This will import all 25,831+ content items
```

### **5.4 Verify Migration**
```bash
# Check import results
curl https://v2.atlas.khamel.com/stats

# Should show your content counts:
# {"content_by_type":{"podcast_transcript":9454,"email":1997,"article":1754},...}
```

## 🔧 **Step 6: Configure Vejla**

### **6.1 Update Vejla Webhook URL**
```
In macOS Shortcuts app:

1. Open your "Send to Atlas v2" shortcut
2. Update webhook URL to: https://v2.atlas.khamel.com/webhook/vejla
3. Update Authorization header: Bearer YOUR-WEBHOOK-TOKEN
```

### **6.2 Test Vejla Integration**
```bash
# Test webhook manually:
curl -X POST https://v2.atlas.khamel.com/webhook/vejla \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR-WEBHOOK-TOKEN" \
  -d '{
    "type": "podcast",
    "url": "https://example.com/test",
    "source": "Test"
  }'

# Should return:
# {"status":"queued","content_id":"test-podcast-2025-09-30-test",...}
```

## 📊 **Step 7: Monitoring & Maintenance**

### **7.1 Setup Monitoring**
```bash
# Create monitoring script
sudo tee /home/ubuntu/monitor-atlas.sh << 'EOF'
#!/bin/bash
HEALTH=$(curl -s http://localhost:8000/health | jq -r '.status')
if [ "$HEALTH" != "healthy" ]; then
    echo "Atlas v2 is not healthy: $HEALTH"
    # Restart if needed
    cd /home/ubuntu/Atlas/atlas_v2
    docker-compose restart
fi
EOF

# Make executable
sudo chmod +x /home/ubuntu/monitor-atlas.sh

# Add to cron (check every 5 minutes)
(crontab -l 2>/dev/null; echo "*/5 * * * * /home/ubuntu/monitor-atlas.sh") | crontab -
```

### **7.2 Setup Log Rotation**
```bash
# Prevent logs from filling disk
sudo tee /etc/logrotate.d/atlas-v2 << EOF
/home/ubuntu/Atlas/atlas_v2/logs/*.log {
    daily
    rotate 30
    compress
    missingok
    notifempty
    create 644 ubuntu ubuntu
}
EOF
```

### **7.3 Check Resource Usage**
```bash
# Monitor Docker resource usage
docker stats atlas-v2

# Check disk usage
df -h

# Check memory usage
free -h

# Should stay well within OCI Always-Free limits
```

## 🎯 **Step 8: Verification Checklist**

### **Final Verification**
- [ ] OCI instance running and accessible
- [ ] Atlas v2 Docker container healthy
- [ ] Domain `v2.atlas.khamel.com` resolving
- [ ] SSL certificate working
- [ ] Health endpoint responding: `curl https://v2.atlas.khamel.com/health`
- [ ] Stats showing migrated content: `curl https://v2.atlas.khamel.com/stats`
- [ ] Webhook responding to test requests
- [ ] Vejla configured with new webhook URL
- [ ] End-to-end test: Vejla → Atlas v2 → Content processed

### **Content Verification**
```bash
# Verify your specific content migrated
curl -s https://v2.atlas.khamel.com/stats | jq

# Should show numbers like:
# content_by_type: {"podcast_transcript": 9454, "email": 1997, "article": 1754}
# queue_by_status: {"pending": 5163, "completed": 174}
```

## 🆘 **Troubleshooting**

### **Common Issues**

**Container won't start:**
```bash
# Check logs
docker logs atlas-v2

# Check available memory
free -h

# Restart if needed
docker-compose restart
```

**Domain not resolving:**
```bash
# Check DNS propagation
dig v2.atlas.khamel.com
nslookup v2.atlas.khamel.com 8.8.8.8
```

**Migration failed:**
```bash
# Check migration files exist
ls -la /home/ubuntu/atlas_v2_migration/

# Check import logs
cat Atlas/atlas_v2/logs/migration_import.log

# Re-run import if needed
cd Atlas/atlas_v2
python3 import_migration_data.py
```

**High resource usage:**
```bash
# Check resource limits
docker stats

# If using too much memory, restart container
docker-compose restart
```

## 💰 **Cost Verification**

### **Always-Free Resources Used**
- ✅ Compute: VM.Standard.A1.Flex (ARM) - 4 OCPU, 24GB RAM
- ✅ Storage: 200GB boot volume
- ✅ Network: Public IP + egress traffic
- ✅ **Total cost: $0.00/month**

### **Resource Monitoring**
```bash
# Check you're within limits
docker stats atlas-v2

# Should show:
# MEM USAGE: < 4GB (out of 24GB available)
# CPU %: < 20% average
```

## 🎉 **Success!**

If all steps completed successfully, you now have:

- **Atlas v2 running at `https://v2.atlas.khamel.com`**
- **All 25,831+ content items migrated and preserved**
- **Vejla integration for automatic URL processing**
- **Free hosting forever on OCI Always-Free**
- **Original Atlas v1 still running at `atlas.khamel.com`**

Your Atlas v2 is now ready to automatically process any URL you encounter through Vejla!