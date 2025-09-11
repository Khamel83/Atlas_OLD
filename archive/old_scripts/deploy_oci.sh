#!/bin/bash
# Atlas OCI Production Deployment Script
# Optimized for comprehensive metadata capture + whisper_tiny transcription

set -e

echo "🚀 ATLAS OCI DEPLOYMENT"
echo "======================="

# Check if running on OCI (Oracle Cloud)
if [ ! -f /etc/oracle-cloud-agent/oracle-cloud-agent.conf ]; then
    echo "⚠️  Warning: Not detected as OCI instance"
    read -p "Continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Create production environment
echo "📦 Setting up production environment..."

# Install system dependencies
sudo apt-get update
sudo apt-get install -y python3-venv python3-pip ffmpeg git

# Create production directory
ATLAS_HOME="/opt/atlas"
sudo mkdir -p $ATLAS_HOME
sudo chown $USER:$USER $ATLAS_HOME
cd $ATLAS_HOME

# Clone/copy Atlas if not present
if [ ! -d "atlas" ]; then
    echo "📥 Cloning Atlas repository..."
    git clone https://github.com/yourusername/atlas.git
    cd atlas
else
    echo "📁 Using existing Atlas directory..."
    cd atlas
    git pull origin main
fi

# Set up Python environment
echo "🐍 Creating Python virtual environment..."
python3 -m venv atlas_venv
source atlas_venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Whisper for transcription
echo "🎵 Installing Whisper for transcription..."
pip install openai-whisper

# Create production configuration
echo "⚙️  Creating production configuration..."
cat > .env << 'EOF'
# Atlas Production Configuration for OCI
DATA_DIRECTORY=output
TRANSCRIBE_ENABLED=true
TRANSCRIBE_BACKEND=local
WHISPER_MODEL=tiny

# Directory setup
TEMP_DIRECTORY=/tmp/atlas
CACHE_DIRECTORY=/opt/atlas/cache

# Logging
LOG_LEVEL=INFO
LOG_FILE=atlas_production.log

# Performance optimizations for OCI
MAX_CONCURRENT_JOBS=2
BATCH_SIZE=5
MEMORY_LIMIT_MB=2048

# API Keys (set these manually)
# OPENROUTER_API_KEY=your_key_here
# OPENAI_API_KEY=your_key_here
EOF

# Create required directories
echo "📁 Creating production directories..."
mkdir -p output/{articles,podcasts,youtube,documents,logs}
mkdir -p inputs
mkdir -p cache
mkdir -p /tmp/atlas

# Set up systemd service for production
echo "🔧 Creating systemd service..."
sudo tee /etc/systemd/system/atlas-ingestion.service > /dev/null << EOF
[Unit]
Description=Atlas Content Ingestion Service
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$ATLAS_HOME/atlas
Environment=PATH=$ATLAS_HOME/atlas/atlas_venv/bin:/usr/local/bin:/usr/bin:/bin
ExecStart=$ATLAS_HOME/atlas/atlas_venv/bin/python run.py --all
Restart=always
RestartSec=30
StandardOutput=journal
StandardError=journal
SyslogIdentifier=atlas-ingestion

[Install]
WantedBy=multi-user.target
EOF

# Create daily processing cron job
echo "⏰ Setting up daily processing..."
(crontab -l 2>/dev/null; echo "0 2 * * * cd $ATLAS_HOME/atlas && source atlas_venv/bin/activate && python run.py --all >> logs/daily_processing.log 2>&1") | crontab -

# Create monitoring script
cat > monitor_atlas.sh << 'EOF'
#!/bin/bash
# Atlas Production Monitoring Script

echo "📊 ATLAS PRODUCTION STATUS"
echo "========================="

# Check service status
echo "🔧 Service Status:"
systemctl is-active atlas-ingestion

# Check recent processing
echo "📈 Recent Activity:"
echo "Articles processed today: $(find output/articles/metadata -name "*.json" -mtime -1 | wc -l)"
echo "Podcasts processed today: $(find output/podcasts -name "*.json" -mtime -1 | wc -l)"
echo "YouTube videos processed today: $(find output/youtube -name "*.json" -mtime -1 | wc -l)"

# Check disk usage
echo "💾 Disk Usage:"
df -h output/

# Check recent errors
echo "⚠️  Recent Errors:"
journalctl -u atlas-ingestion --since "1 hour ago" --grep ERROR | tail -5

# Check memory usage
echo "🧠 Memory Usage:"
ps aux | grep python | grep atlas | awk '{print $4"%", $11}' | head -5
EOF

chmod +x monitor_atlas.sh

# Test basic functionality
echo "🧪 Testing basic functionality..."
source atlas_venv/bin/activate

# Test configuration loading
python3 -c "
from helpers.config import load_config
config = load_config()
print('✅ Configuration loads successfully')
print(f'Data directory: {config.get(\"data_directory\")}')
print(f'Transcription enabled: {config.get(\"run_transcription\")}')
"

# Test whisper installation
python3 -c "
import whisper
model = whisper.load_model('tiny')
print('✅ Whisper tiny model loads successfully')
print(f'Model size: {len(model.decoder.token_embedding.weight)} tokens')
"

echo ""
echo "✅ ATLAS OCI DEPLOYMENT COMPLETE!"
echo "=================================="
echo ""
echo "🚀 Production Ready Features:"
echo "   ✅ Comprehensive metadata capture (ALL ingestors)"
echo "   ✅ Whisper tiny transcription (optimized for speed)"
echo "   ✅ Raw data preservation (never lose anything)"
echo "   ✅ Systemd service for continuous operation"
echo "   ✅ Daily automated processing"
echo "   ✅ Production monitoring tools"
echo ""
echo "📋 Next Steps:"
echo "   1. Configure API keys in .env if needed"
echo "   2. Add your content URLs to inputs/ directory"
echo "   3. Start service: sudo systemctl start atlas-ingestion"
echo "   4. Monitor with: ./monitor_atlas.sh"
echo ""
echo "📊 Current Status:"
find output -name "*.json" -mtime -7 | wc -l | xargs echo "   Files processed this week:"
du -sh output/ | awk '{print "   Total data size: " $1}'
echo ""
echo "🎯 Your Atlas instance is ready for production!"
EOF