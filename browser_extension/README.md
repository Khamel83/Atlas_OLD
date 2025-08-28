# Atlas Browser Extension

The Atlas Browser Extension allows you to capture web content directly to your Atlas system with a single click.

## Features

1. **Save Current Page** - Save the entire current page to Atlas
2. **Save Selection** - Save selected text to Atlas
3. **Save Article Content** - Save just the main article content (auto-detected)
4. **Context Menu Integration** - Access Atlas capture options from the right-click menu
5. **Customizable Server URL** - Configure your Atlas server address

## Installation (Chrome/Chromium)

1. Open Chrome/Chromium browser
2. Navigate to `chrome://extensions`
3. Enable "Developer mode" (toggle in the top right)
4. Click "Load unpacked"
5. Select the `browser_extension` directory
6. The extension should now be installed and visible in your toolbar

## Installation (Firefox)

1. Open Firefox browser
2. Navigate to `about:debugging`
3. Click "This Firefox"
4. Click "Load Temporary Add-on"
5. Select the `manifest.json` file in the `browser_extension` directory
6. The extension should now be installed

## Configuration

1. Click the Atlas icon in your browser toolbar
2. Click the extension icon again to open the popup
3. Click the settings icon (gear) to configure your Atlas server URL
4. Enter your Atlas server address (default: `http://localhost:8000`)
5. Click "Save Settings"

## Usage

### Toolbar Button

Click the Atlas icon in your browser toolbar to open the popup menu with these options:
- **Save Current Page** - Saves the entire current page
- **Save Selection** - Saves any selected text
- **Save Article Content** - Saves just the main article content

### Context Menu

Right-click on any page, selection, or link to access Atlas capture options:
- **Save Page to Atlas** - Saves the current page
- **Save Selection to Atlas** - Saves the selected text
- **Save Link to Atlas** - Saves the clicked link

## Requirements

- Atlas running and accessible from your browser
- Web browser (Chrome, Chromium, or Firefox)
- Network connectivity to your Atlas server

## Troubleshooting

### Extension not appearing
- Ensure Developer Mode is enabled in Chrome extensions page
- Try refreshing the extensions page
- Check that the extension is enabled

### Content not saving
- Verify that your Atlas server is running
- Check that the server URL is correctly configured in extension settings
- Ensure your Atlas API is accessible from your browser (no CORS issues)
- Check the Atlas logs for error messages

### Article content extraction not working
- Some websites may have complex layouts that prevent accurate content detection
- Try using "Save Selection" instead and manually select the content
- The extension uses simple heuristics to detect content - it may not work perfectly on all sites

## Support

For issues with the browser extension:
- Check the Atlas documentation: `/docs/user-guides/`
- Visit GitHub Discussions: https://github.com/your-username/atlas/discussions
- Join the community Discord: https://discord.gg/atlas

For bug reports:
- File an issue on GitHub: https://github.com/your-username/atlas/issues
- Include screenshots and error messages when possible
- Describe steps to reproduce the issue