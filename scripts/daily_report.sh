#!/bin/bash
# Atlas Daily Report Generator
# Generates and optionally sends daily activity reports

ATLAS_DIR="/home/ubuntu/dev/atlas"
REPORT_DIR="$ATLAS_DIR/reports/daily"
VENV_PATH="$ATLAS_DIR/atlas_venv"

# Ensure reports directory exists
mkdir -p "$REPORT_DIR"

# Activate virtual environment
source "$VENV_PATH/bin/activate"

# Generate today's report
cd "$ATLAS_DIR"
echo "🔄 Generating Atlas daily report..."
PYTHONPATH=. python helpers/daily_reporter.py

# Optional: Send notification (configure with your preferred method)
# Uncomment and configure one of these options:

# Option 1: Save to notification file for external pickup
# echo "$(date): $(tail -1 $REPORT_DIR/latest_notification.txt)" >> /tmp/atlas_notifications.log

# Option 2: System notification (if running on desktop)
# if command -v notify-send &> /dev/null; then
#     NOTIFICATION=$(python -c "
# from helpers.daily_reporter import AtlasDailyReporter
# r = AtlasDailyReporter()
# report = r.generate_daily_report()
# print(r.generate_push_notification(report))
# ")
#     notify-send "Atlas Daily Report" "$NOTIFICATION"
# fi

# Option 3: Email notification (requires sendmail/mail setup)
# if command -v mail &> /dev/null; then
#     SUBJECT="Atlas Daily Report - $(date +%Y-%m-%d)"
#     BODY=$(cat $REPORT_DIR/atlas_daily_$(date +%Y-%m-%d).json | python -m json.tool)
#     echo "$BODY" | mail -s "$SUBJECT" your-email@example.com
# fi

# Option 4: Slack webhook (requires curl and webhook URL)
# if [ ! -z "$SLACK_WEBHOOK_URL" ]; then
#     NOTIFICATION=$(python -c "
# from helpers.daily_reporter import AtlasDailyReporter
# r = AtlasDailyReporter()
# report = r.generate_daily_report()
# print(r.generate_push_notification(report))
# ")
#     curl -X POST -H 'Content-type: application/json' \
#          --data '{"text":"'"$NOTIFICATION"'"}' \
#          "$SLACK_WEBHOOK_URL"
# fi

echo "✅ Daily report generation complete"