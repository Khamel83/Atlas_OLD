#!/bin/bash
# Mac Mini Software Installation Script
# Run this script ON THE MAC MINI to install all required software

set -e

echo "🚀 Installing Atlas Mac Mini Processing Software..."

# Check if we're on macOS
if [[ "$(uname)" != "Darwin" ]]; then
    echo "❌ This script must be run on macOS (Mac Mini)"
    exit 1
fi

# Install Homebrew if not present
if ! command -v brew &> /dev/null; then
    echo "📦 Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✅ Homebrew already installed"
fi

# Install Python 3.11+ if not present
echo "🐍 Installing Python 3.11..."
if ! python3.11 --version &> /dev/null; then
    brew install python@3.11
else
    echo "✅ Python 3.11 already installed"
fi

# Install FFmpeg
echo "🎵 Installing FFmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    brew install ffmpeg
else
    echo "✅ FFmpeg already installed"
fi

# Create Atlas worker directory
echo "📁 Creating Atlas worker directory..."
mkdir -p ~/atlas_worker
cd ~/atlas_worker

# Create virtual environment
echo "🏗️ Creating Python virtual environment..."
python3.11 -m venv venv
source venv/bin/activate

# Install Python packages
echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install openai-whisper
pip install requests
pip install flask
pip install python-dotenv

# Test installations
echo "🧪 Testing installations..."

# Test Python
python3 --version
echo "✅ Python working"

# Test FFmpeg
ffmpeg -version | head -1
echo "✅ FFmpeg working"

# Test Whisper
python3 -c "import whisper; print('Available models:', whisper.available_models())"
echo "✅ Whisper working"

# Download Whisper models for offline use
echo "📥 Downloading Whisper models..."
python3 -c "import whisper; whisper.load_model('tiny'); print('Tiny model downloaded')"
python3 -c "import whisper; whisper.load_model('base'); print('Base model downloaded')"
python3 -c "import whisper; whisper.load_model('small'); print('Small model downloaded')"

# Create test audio file and test transcription
echo "🎤 Testing Whisper transcription..."
# Create a simple test (you'll need to provide a test audio file)
echo "Note: Place a test audio file (test.wav) in ~/atlas_worker/ to test transcription"

# Set up directories
mkdir -p ~/atlas_worker/queue/tasks
mkdir -p ~/atlas_worker/queue/results
mkdir -p ~/atlas_worker/logs

echo ""
echo "🎉 Mac Mini software installation complete!"
echo ""
echo "✅ Installed:"
echo "  - Python 3.11+ with virtual environment"
echo "  - OpenAI Whisper (tiny, base, small models)"
echo "  - FFmpeg for audio processing"  
echo "  - Required Python packages"
echo ""
echo "📁 Atlas worker directory: ~/atlas_worker/"
echo "🔧 Virtual environment: ~/atlas_worker/venv/"
echo ""
echo "🧪 Verify installation:"
echo "  cd ~/atlas_worker && source venv/bin/activate"
echo "  python3 -c \"import whisper; print('Whisper ready!')\""