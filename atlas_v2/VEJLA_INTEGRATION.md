# Vejla Integration Guide for Atlas v2

This guide shows how to configure Vejla (macOS link router) to automatically send podcast and article URLs to Atlas v2 for processing.

## Architecture Overview

```
Vejla → Local Webhook → Atlas v2 → Processing Pipeline
```

**Flow:**
1. You encounter a podcast/article URL
2. Vejla intercepts the URL based on rules
3. Vejla sends URL to Atlas v2 webhook (localhost:8000)
4. Atlas v2 processes content immediately
5. Content appears in your Atlas database

## Prerequisites

- **Vejla** installed on macOS
- **Atlas v2** running locally (localhost:8000)
- **macOS Shortcuts** app (for webhook automation)

## Setup Steps

### 1. Start Atlas v2

```bash
cd atlas_v2
docker-compose up -d

# Verify it's running
curl http://localhost:8000/health
```

### 2. Create Webhook Shortcut

Open **Shortcuts** app and create a new shortcut:

**Name:** "Send to Atlas v2"

**Actions:**
1. **Get Contents of URL**
   - URL: `[Shortcut Input]`
   - Method: GET

2. **Get Text from Input**
   - Text: `[Contents of URL]`

3. **Get Contents of URL** (webhook call)
   - URL: `http://localhost:8000/webhook/vejla`
   - Method: POST
   - Headers:
     - `Content-Type`: `application/json`
     - `Authorization`: `Bearer atlas-v2-webhook-secret`
   - Request Body (JSON):
     ```json
     {
       "type": "article",
       "url": "[Shortcut Input]",
       "source": "Web",
       "metadata": {
         "title": "Web Article",
         "date": "[Current Date]"
       }
     }
     ```

4. **Show Notification**
   - Text: "Sent to Atlas v2: [Shortcut Input]"

### 3. Configure Vejla Rules

Open **Vejla** preferences and add these rules:

#### Rule 1: Podcast URLs → Atlas
- **If URL contains:** `podcast`, `episode`, `rss`
- **Open with:** Shortcuts → "Send to Atlas v2"

#### Rule 2: Newsletter URLs → Atlas
- **If URL contains:** `newsletter`, `substack`, `stratechery`
- **Open with:** Shortcuts → "Send to Atlas v2"

#### Rule 3: YouTube URLs → Atlas
- **If URL contains:** `youtube.com`, `youtu.be`
- **Open with:** Shortcuts → "Send to Atlas v2"

#### Rule 4: Specific Domains → Atlas
- **If domain is:** `acquired.fm`, `conversationswithtyler.com`, `stratechery.com`
- **Open with:** Shortcuts → "Send to Atlas v2"

### 4. Advanced: Direct Webhook Integration

For more direct integration, create this AppleScript:

**File:** `~/Scripts/atlas_v2_webhook.scpt`

```applescript
on run {input, parameters}
    set theURL to item 1 of input

    set json_data to "{" & ¬
        "\"type\": \"article\"," & ¬
        "\"url\": \"" & theURL & "\"," & ¬
        "\"source\": \"Vejla\"," & ¬
        "\"metadata\": {" & ¬
            "\"title\": \"Vejla Capture\"," & ¬
            "\"date\": \"" & (current date as string) & "\"" & ¬
        "}" & ¬
    "}"

    do shell script "curl -X POST http://localhost:8000/webhook/vejla " & ¬
        "-H 'Content-Type: application/json' " & ¬
        "-H 'Authorization: Bearer atlas-v2-webhook-secret' " & ¬
        "-d '" & json_data & "'"

    return theURL
end run
```

Then configure Vejla to use this script directly.

## Testing the Integration

### 1. Test Webhook Directly

```bash
curl -X POST http://localhost:8000/webhook/vejla \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer atlas-v2-webhook-secret" \
  -d '{
    "type": "podcast",
    "url": "https://acquired.fm/episodes/berkshire-hathaway-2024",
    "source": "Acquired",
    "metadata": {
      "title": "Berkshire Hathaway 2024",
      "date": "2025-09-30"
    }
  }'
```

Expected response:
```json
{
  "status": "queued",
  "content_id": "acquired-podcast-2025-09-30-berkshire-hathaway-2024",
  "estimated_processing_time_minutes": 2
}
```

### 2. Test via Vejla

1. Copy a podcast URL: `https://acquired.fm/episodes/berkshire-hathaway-2024`
2. Paste in browser or click link
3. Vejla should intercept and send to Atlas v2
4. Check Atlas logs: `docker logs atlas-v2`
5. Verify in Atlas dashboard: `curl http://localhost:8000/stats`

## Webhook Payload Format

Atlas v2 expects this JSON structure:

```json
{
  "type": "podcast" | "newsletter" | "youtube" | "article",
  "url": "https://example.com/content",
  "source": "Source Name",
  "metadata": {
    "title": "Content Title",
    "date": "2025-09-30",
    "duration_minutes": 45,
    "episode_number": 123,
    "author": "Author Name",
    "description": "Content description"
  }
}
```

**Required fields:**
- `url`: The content URL to process
- `type`: Content type for processing pipeline

**Optional fields:**
- `source`: Source name (helps with extraction patterns)
- `metadata`: Additional context for better processing

## Content Type Detection

Atlas v2 auto-detects content type from URL patterns:

- **Podcast:** `podcast`, `episode`, `show` in URL
- **YouTube:** `youtube.com`, `youtu.be`
- **Newsletter:** `newsletter`, `substack`, `daily-update`
- **Article:** Default fallback

## Troubleshooting

### Webhook Not Working

1. **Check Atlas v2 status:**
   ```bash
   curl http://localhost:8000/health
   ```

2. **Check logs:**
   ```bash
   docker logs atlas-v2 --tail 50
   ```

3. **Verify webhook secret:**
   - Must match in Shortcuts and Atlas v2
   - Default: `atlas-v2-webhook-secret`

### Vejla Not Triggering

1. **Check Vejla rules:** Verify URL patterns match
2. **Test shortcut directly:** Run in Shortcuts app manually
3. **Check shortcut permissions:** Allow network access

### Content Not Processing

1. **Check queue status:**
   ```bash
   curl http://localhost:8000/stats
   ```

2. **Look for processing errors:**
   ```bash
   docker logs atlas-v2 | grep ERROR
   ```

3. **Verify content doesn't already exist:**
   ```bash
   sqlite3 atlas_v2/data/atlas_v2.db "SELECT * FROM content_metadata WHERE source_url LIKE '%your-url%'"
   ```

## Performance Optimization

### Batch Processing
- Atlas v2 processes webhooks immediately
- Backlog runs every 6 hours
- Webhook processing takes ~2 minutes per item

### Rate Limiting
- Built-in rate limiting per domain
- Configurable in `config/sources.csv`
- Default: 3 seconds between requests

### Resource Usage
- RAM: ~2-4GB typical usage
- CPU: <20% on OCI Always-Free ARM
- Storage: ~1MB per transcript

## Security Notes

1. **Webhook Secret:** Change default token:
   ```bash
   echo "WEBHOOK_SECRET_TOKEN=your-secure-token-here" > .env
   ```

2. **Local Only:** Current setup only accepts localhost
3. **No Auth Required:** For local Vejla integration
4. **Logs:** Webhook calls are logged for debugging

## Next Steps

Once Vejla integration works:

1. **Deploy to OCI:** Move Atlas v2 to cloud for remote access
2. **Add Auth:** Implement proper webhook authentication
3. **Custom Rules:** Fine-tune Vejla rules for your workflow
4. **Monitoring:** Set up alerts for failed processing

This creates a seamless content capture workflow where any URL you encounter gets automatically processed and added to your knowledge base!