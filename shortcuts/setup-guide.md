# Atlas Apple Device Integration Setup Guide

## Overview

This guide helps you set up seamless content capture from your Apple devices (iPhone, iPad, Mac) to your Atlas knowledge system.

## Prerequisites

- Atlas server running and accessible from your device
- iOS 14+ or macOS 12+ 
- Atlas server URL (local IP or public URL)

## Setup Components

### 1. iOS Share Extension (AtlasCapture App)

**Installation:**
1. Build and install the AtlasCapture iOS app from `ios/AtlasCapture/`
2. Open the app and configure your Atlas server URL in Settings
3. Test the connection to ensure it's working

**Usage:**
- From any app (Safari, Notes, Messages, etc.), tap the Share button
- Select "Atlas Capture" from the share sheet
- Add optional notes and tap "Send to Atlas"
- Content will be processed automatically by Atlas

### 2. Shortcuts Integration

**Quick Setup:**
1. Open the Shortcuts app on your iPhone/iPad
2. Use the templates in `shortcuts/atlas-shortcuts.json`
3. Replace `YOUR_ATLAS_SERVER` with your actual server URL
4. Add shortcuts to Siri for voice activation

**Available Shortcuts:**

#### Basic Shortcuts
- **"Add to Atlas"** - Send clipboard content
- **"Voice to Atlas"** - Record and transcribe voice memo  
- **"URL to Atlas"** - Send current Safari URL
- **"Quick Note to Atlas"** - Capture text note

#### Advanced Shortcuts
- **"Reading List to Atlas"** - Bulk export Safari Reading List
- **"Atlas Health Check"** - Test server connectivity

### 3. Server Configuration

**Find Your Server URL:**

For local network:
```bash
# On your Atlas server, find the IP address
hostname -I
# Use: http://[IP_ADDRESS]:5000
# Example: http://192.168.1.100:5000
```

For cloud/VPS:
```bash
# Use your public domain or IP
# Example: https://atlas.yourdomain.com
```

**Test Server Accessibility:**
```bash
# From your iPhone, open Safari and visit:
http://YOUR_ATLAS_SERVER:5000/api/capture/health

# Should return: {"status": "healthy", ...}
```

## Detailed Setup Instructions

### iOS Share Extension Setup

1. **Configure Server URL**
   - Open AtlasCapture app
   - Tap "Settings" 
   - Enter your Atlas server URL
   - Tap "Test Connection" to verify

2. **Enable Share Extension**
   - Go to any app with shareable content
   - Tap Share button
   - Scroll right in the bottom row to "More"
   - Enable "Atlas Capture"
   - Reorder to preferred position

### Shortcuts App Setup

#### Creating "Add to Atlas" Shortcut

1. Open Shortcuts app → Tap "+" → Create Shortcut
2. Add these actions in order:

   **Action 1: Get Clipboard**
   - Search for "Get Clipboard"
   - Add the action

   **Action 2: Get Contents of URL**
   - Search for "Get Contents of URL"  
   - Set URL to: `http://YOUR_ATLAS_SERVER:5000/api/capture`
   - Set Method to: POST
   - Set Headers: `Content-Type: application/json`
   - Set Request Body to:
   ```json
   {
     "type": "text",
     "content": "[Clipboard]",
     "metadata": {
       "source": "siri_shortcut",
       "notes": "Captured via Siri"
     },
     "source_device": "iPhone"
   }
   ```

   **Action 3: Show Notification**
   - Search for "Show Notification"
   - Set Title: "Atlas Capture"
   - Set Body: "Content sent to Atlas"

3. **Configure Siri Phrase**
   - Tap shortcut settings
   - Tap "Add to Siri"
   - Record phrase: "Add to Atlas"

#### Creating "Voice to Atlas" Shortcut

1. Create new shortcut
2. Add these actions:

   **Action 1: Dictate Text**
   - Search for "Dictate Text"
   - Set Language if needed

   **Action 2: Get Contents of URL**
   - URL: `http://YOUR_ATLAS_SERVER:5000/api/capture`
   - Method: POST
   - Headers: `Content-Type: application/json`
   - Body:
   ```json
   {
     "type": "voice",
     "content": "[Dictated Text]",
     "metadata": {
       "source": "voice_shortcut",
       "notes": "Voice memo transcription"
     },
     "source_device": "iPhone"
   }
   ```

   **Action 3: Show Result**
   - Text: "Voice memo sent to Atlas"

3. Add to Siri with phrase: "Voice to Atlas"

### Advanced Configuration

#### Reading List Bulk Export

For bulk export of Safari Reading List:

1. **Get Reading List Items**
   - Add "Get My Shortcuts" action
   - Filter for Reading List items

2. **Repeat with Each Item**
   - For each URL, send to Atlas capture API
   - Add small delay between requests

#### Offline Queue Handling

The share extension automatically handles offline scenarios:
- Content saved locally when server unreachable
- Automatic retry when connection restored
- Status tracking in main app

## Usage Examples

### Voice Commands
- "Hey Siri, add to Atlas" - Captures clipboard
- "Hey Siri, voice to Atlas" - Records voice memo
- "Hey Siri, URL to Atlas" - Captures current Safari page

### Share Extension
- Reading an article → Share → Atlas Capture
- Interesting tweet → Share → Atlas Capture  
- Voice memo → Share → Atlas Capture

### Automation Ideas
- Morning routine: Export Reading List to Atlas
- Context-aware capture based on location
- Scheduled bulk processing of Notes app

## Troubleshooting

### Connection Issues

**"Connection failed" in app:**
- Verify Atlas server is running
- Check firewall settings on server
- Ensure devices are on same network (for local setup)
- Test URL in Safari browser first

**Shortcuts network errors:**
- Double-check server URL in shortcut
- Ensure JSON format is correct in request body
- Test with simple GET request to health endpoint first

### Share Extension Issues

**Extension not appearing:**
- Check iOS version (14+ required)
- Reinstall app if needed
- Reset share sheet in Settings → General → Reset

**Content not captured:**
- Check app permissions
- Verify supported content types
- Test with simple text first

### Permission Issues

**Microphone access for voice shortcuts:**
- Settings → Privacy & Security → Microphone → Shortcuts

**Safari access for Reading List:**
- Settings → Privacy & Security → Safari → Shortcuts

## Security Considerations

### Network Security
- Use HTTPS in production
- Consider VPN for remote access
- Firewall rules to restrict access

### Data Privacy
- Content processed locally on Atlas server
- No cloud services involved
- Review captured content regularly

## Advanced Features

### Custom Shortcuts
- Create shortcuts for specific content types
- Integrate with other automation apps
- Context-aware capture rules

### API Extensions
- Monitor capture queue status
- Batch operations
- Custom metadata fields

---

## Quick Reference

### Essential URLs
- Health check: `http://YOUR_SERVER:5000/api/capture/health`
- Capture API: `http://YOUR_SERVER:5000/api/capture`
- Status check: `http://YOUR_SERVER:5000/api/capture/status/{id}`

### Voice Commands
- "Hey Siri, add to Atlas"
- "Hey Siri, voice to Atlas"
- "Hey Siri, Atlas health check"

### Support
For issues or questions:
1. Check Atlas background service logs
2. Test API endpoints directly
3. Verify network connectivity
4. Review server configuration