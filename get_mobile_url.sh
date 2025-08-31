#!/bin/bash

# Get Mobile Installation URL for Atlas iOS Shortcuts
# This script shows the URL to use for installing shortcuts on your iPhone

echo "🚀 Atlas Mobile Shortcut Installer"
echo "=================================="
echo

# Try to get the IP address
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    IP=$(ipconfig getifaddr en0 2>/dev/null)
    if [ -z "$IP" ]; then
        IP=$(ipconfig getifaddr en1 2>/dev/null)
    fi
else
    # Linux/other Unix
    IP=$(ip route get 1 2>/dev/null | head -1 | awk '{print $7}')
    if [ -z "$IP" ]; then
        IP=$(hostname -I 2>/dev/null | awk '{print $1}')
    fi
fi

# Fallback method using ifconfig if available
if [ -z "$IP" ] && command -v ifconfig >/dev/null 2>&1; then
    IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -n1)
fi

if [ -z "$IP" ]; then
    echo "❌ Could not determine your IP address automatically."
    echo
    echo "To find your IP manually:"
    echo "  1. System Preferences → Network"
    echo "  2. Select your active connection (Wi-Fi/Ethernet)"
    echo "  3. Look for 'IP Address'"
    echo
    echo "Then visit: http://YOUR_IP:8000/shortcuts"
else
    INSTALL_URL="http://${IP}:8000/shortcuts"
    echo "📱 Open this URL on your iPhone to install shortcuts:"
    echo
    echo "    $INSTALL_URL"
    echo
    echo "🔗 Or use this QR code:"
    echo
    # Create a simple QR code using qrencode if available
    if command -v qrencode >/dev/null 2>&1; then
        qrencode -t ANSI "$INSTALL_URL"
    else
        echo "   (Install qrencode for QR code: brew install qrencode)"
    fi
    echo
    echo "📋 Instructions:"
    echo "  1. Open the URL above on your iPhone"
    echo "  2. Tap each shortcut to download"
    echo "  3. Follow iOS prompts: 'Get Shortcut' → 'Add Shortcut'"
    echo "  4. Test with: 'Hey Siri, save to Atlas'"
fi

echo
echo "✅ Alternative: Run './install_shortcuts.sh' on this Mac"
echo