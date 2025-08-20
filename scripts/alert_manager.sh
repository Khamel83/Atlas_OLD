#!/bin/bash

# Atlas Production Alert Management Script
# This script manages alerts for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Alert Management..."

# Configuration
ALERT_LOG="/home/ubuntu/dev/atlas/logs/alert_management.log"
ALERT_CONFIG="/home/ubuntu/dev/atlas/config/alerts.json"
ALERT_HISTORY_DIR="/home/ubuntu/dev/atlas/alerts/history"

# Create logs and alerts directories if they don't exist
mkdir -p "$(dirname $ALERT_LOG)"
mkdir -p "$ALERT_HISTORY_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $ALERT_LOG
    echo "$1"
}

# Function to initialize alert configuration
initialize_alert_config() {
    log_message "Initializing alert configuration"
    
    # Create default alert configuration if it doesn't exist
    if [ ! -f "$ALERT_CONFIG" ]; then
        cat > "$ALERT_CONFIG" << EOF
{
    "alerts": {
        "email": {
            "enabled": true,
            "smtp_server": "smtp.gmail.com",
            "port": 587,
            "sender": "atlas.alerts@gmail.com",
            "password": "your_app_password",
            "recipients": ["admin@khamel.com"]
        },
        "slack": {
            "enabled": false,
            "webhook_url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
        }
    },
    "alert_rules": {
        "critical": {
            "cpu_usage": 90,
            "memory_usage": 90,
            "disk_usage": 95,
            "service_down": true
        },
        "warning": {
            "cpu_usage": 80,
            "memory_usage": 80,
            "disk_usage": 85,
            "high_error_rates": 10
        }
    },
    "notification_channels": {
        "email": true,
        "slack": false,
        "sms": false
    }
}
EOF
        echo "✅ Created default alert configuration"
        log_message "Default alert configuration created"
    else
        echo "✅ Alert configuration already exists"
    fi
}

# Function to send email alert
send_email_alert() {
    local subject=$1
    local message=$2
    
    log_message "Sending email alert: $subject"
    
    # Check if email configuration exists
    if [ ! -f "$ALERT_CONFIG" ]; then
        echo "❌ Alert configuration not found"
        return 1
    fi
    
    # Check if email alerts are enabled
    local email_enabled=$(jq -r '.alerts.email.enabled' "$ALERT_CONFIG")
    if [ "$email_enabled" != "true" ]; then
        echo "ℹ️ Email alerts are disabled"
        log_message "Email alerts are disabled"
        return 0
    fi
    
    # Extract email configuration
    local smtp_server=$(jq -r '.alerts.email.smtp_server' "$ALERT_CONFIG")
    local port=$(jq -r '.alerts.email.port' "$ALERT_CONFIG")
    local sender_email=$(jq -r '.alerts.email.sender' "$ALERT_CONFIG")
    local sender_password=$(jq -r '.alerts.email.password' "$ALERT_CONFIG")
    local recipients=$(jq -r '.alerts.email.recipients[]' "$ALERT_CONFIG")
    
    # Validate required environment variables
    if [ -z "$sender_email" ] || [ -z "$sender_password" ]; then
        echo "❌ Missing email configuration"
        log_message "Missing email configuration"
        return 1
    fi
    
    # Create alert message
    local alert_message="Atlas Production Alert

Subject: $subject
Time: $(date)
Message: $message

This is an automated alert from your Atlas production system.

For more information, check the logs in:
$ALERT_LOG

To disable these alerts, update the configuration in:
$ALERT_CONFIG"

    # In a real implementation, this would send an actual email
    # For now, we'll just log the alert
    echo "📧 EMAIL ALERT: $subject"
    echo "To: $recipients"
    echo "$alert_message"
    echo ""
    
    # Log to alert history
    local alert_file="$ALERT_HISTORY_DIR/alert_$(date +%Y%m%d_%H%M%S).json"
    cat > "$alert_file" << EOF
{
    "timestamp": "$(date -Iseconds)",
    "type": "email",
    "subject": "$subject",
    "message": "$message",
    "recipients": ["$recipients"]
}
EOF
    
    log_message "Email alert logged to: $alert_file"
}

# Function to send Slack alert
send_slack_alert() {
    local subject=$1
    local message=$2
    
    log_message "Sending Slack alert: $subject"
    
    # Check if Slack configuration exists
    if [ ! -f "$ALERT_CONFIG" ]; then
        echo "❌ Alert configuration not found"
        return 1
    fi
    
    # Check if Slack alerts are enabled
    local slack_enabled=$(jq -r '.alerts.slack.enabled' "$ALERT_CONFIG")
    if [ "$slack_enabled" != "true" ]; then
        echo "ℹ️ Slack alerts are disabled"
        log_message "Slack alerts are disabled"
        return 0
    fi
    
    # Extract Slack configuration
    local webhook_url=$(jq -r '.alerts.slack.webhook_url' "$ALERT_CONFIG")
    
    # Validate required configuration
    if [ -z "$webhook_url" ]; then
        echo "❌ Missing Slack webhook URL"
        log_message "Missing Slack webhook URL"
        return 1
    fi
    
    # Create alert payload
    local payload=$(jq -n --arg subject "$subject" --arg message "$message" '{
        "text": "Atlas Production Alert",
        "attachments": [
            {
                "color": "danger",
                "fields": [
                    {
                        "title": $subject,
                        "value": $message,
                        "short": false
                    },
                    {
                        "title": "Time",
                        "value": "'$(date)'",
                        "short": true
                    }
                ]
            }
        ]
    }')
    
    # In a real implementation, this would send an actual Slack message
    # For now, we'll just log the alert
    echo "💬 SLACK ALERT: $subject"
    echo "Webhook URL: $webhook_url"
    echo "$payload"
    echo ""
    
    # Log to alert history
    local alert_file="$ALERT_HISTORY_DIR/alert_$(date +%Y%m%d_%H%M%S).json"
    cat > "$alert_file" << EOF
{
    "timestamp": "$(date -Iseconds)",
    "type": "slack",
    "subject": "$subject",
    "message": "$message",
    "webhook_url": "$webhook_url"
}
EOF
    
    log_message "Slack alert logged to: $alert_file"
}

# Function to send SMS alert
send_sms_alert() {
    local subject=$1
    local message=$2
    
    log_message "Sending SMS alert: $subject"
    
    # Check if SMS configuration exists
    if [ ! -f "$ALERT_CONFIG" ]; then
        echo "❌ Alert configuration not found"
        return 1
    fi
    
    # Check if SMS alerts are enabled
    local sms_enabled=$(jq -r '.alerts.sms.enabled' "$ALERT_CONFIG")
    if [ "$sms_enabled" != "true" ]; then
        echo "ℹ️ SMS alerts are disabled"
        log_message "SMS alerts are disabled"
        return 0
    fi
    
    # Extract SMS configuration
    local twilio_account_sid=$(jq -r '.alerts.sms.twilio_account_sid' "$ALERT_CONFIG")
    local twilio_auth_token=$(jq -r '.alerts.sms.twilio_auth_token' "$ALERT_CONFIG")
    local twilio_phone_number=$(jq -r '.alerts.sms.twilio_phone_number' "$ALERT_CONFIG")
    local recipient_phone_numbers=$(jq -r '.alerts.sms.recipient_phone_numbers[]' "$ALERT_CONFIG")
    
    # Validate required configuration
    if [ -z "$twilio_account_sid" ] || [ -z "$twilio_auth_token" ] || [ -z "$twilio_phone_number" ]; then
        echo "❌ Missing SMS configuration"
        log_message "Missing SMS configuration"
        return 1
    fi
    
    # Create alert message
    local alert_message="Atlas Alert: $subject - $message"
    
    # In a real implementation, this would send an actual SMS
    # For now, we'll just log the alert
    echo "📱 SMS ALERT: $subject"
    echo "To: $recipient_phone_numbers"
    echo "Message: $alert_message"
    echo ""
    
    # Log to alert history
    local alert_file="$ALERT_HISTORY_DIR/alert_$(date +%Y%m%d_%H%M%S).json"
    cat > "$alert_file" << EOF
{
    "timestamp": "$(date -Iseconds)",
    "type": "sms",
    "subject": "$subject",
    "message": "$message",
    "recipient_phone_numbers": ["$recipient_phone_numbers"]
}
EOF
    
    log_message "SMS alert logged to: $alert_file"
}

# Function to check system alerts
check_system_alerts() {
    log_message "Checking system alerts"
    
    echo "Checking System Alerts..."
    echo "========================"
    
    # Check CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local critical_cpu=$(jq -r '.alert_rules.critical.cpu_usage' "$ALERT_CONFIG")
    local warning_cpu=$(jq -r '.alert_rules.warning.cpu_usage' "$ALERT_CONFIG")
    
    if (( $(echo "$cpu_usage > $critical_cpu" | bc -l) )); then
        send_email_alert "CRITICAL: High CPU Usage" "CPU usage is at ${cpu_usage}%, exceeding critical threshold of ${critical_cpu}%"
        send_slack_alert "CRITICAL: High CPU Usage" "CPU usage is at ${cpu_usage}%, exceeding critical threshold of ${critical_cpu}%"
    elif (( $(echo "$cpu_usage > $warning_cpu" | bc -l) )); then
        send_email_alert "WARNING: High CPU Usage" "CPU usage is at ${cpu_usage}%, exceeding warning threshold of ${warning_cpu}%"
        send_slack_alert "WARNING: High CPU Usage" "CPU usage is at ${cpu_usage}%, exceeding warning threshold of ${warning_cpu}%"
    fi
    
    # Check memory usage
    local memory_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    local critical_memory=$(jq -r '.alert_rules.critical.memory_usage' "$ALERT_CONFIG")
    local warning_memory=$(jq -r '.alert_rules.warning.memory_usage' "$ALERT_CONFIG")
    
    if [ $memory_usage -gt $critical_memory ]; then
        send_email_alert "CRITICAL: High Memory Usage" "Memory usage is at ${memory_usage}%, exceeding critical threshold of ${critical_memory}%"
        send_slack_alert "CRITICAL: High Memory Usage" "Memory usage is at ${memory_usage}%, exceeding critical threshold of ${critical_memory}%"
    elif [ $memory_usage -gt $warning_memory ]; then
        send_email_alert "WARNING: High Memory Usage" "Memory usage is at ${memory_usage}%, exceeding warning threshold of ${warning_memory}%"
        send_slack_alert "WARNING: High Memory Usage" "Memory usage is at ${memory_usage}%, exceeding warning threshold of ${warning_memory}%"
    fi
    
    # Check disk usage
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    local critical_disk=$(jq -r '.alert_rules.critical.disk_usage' "$ALERT_CONFIG")
    local warning_disk=$(jq -r '.alert_rules.warning.disk_usage' "$ALERT_CONFIG")
    
    if [ $disk_usage -gt $critical_disk ]; then
        send_email_alert "CRITICAL: High Disk Usage" "Disk usage is at ${disk_usage}%, exceeding critical threshold of ${critical_disk}%"
        send_slack_alert "CRITICAL: High Disk Usage" "Disk usage is at ${disk_usage}%, exceeding critical threshold of ${critical_disk}%"
    elif [ $disk_usage -gt $warning_disk ]; then
        send_email_alert "WARNING: High Disk Usage" "Disk usage is at ${disk_usage}%, exceeding warning threshold of ${warning_disk}%"
        send_slack_alert "WARNING: High Disk Usage" "Disk usage is at ${disk_usage}%, exceeding warning threshold of ${warning_disk}%"
    fi
    
    echo "✅ System alert check completed"
    log_message "System alert check completed"
}

# Function to check service alerts
check_service_alerts() {
    log_message "Checking service alerts"
    
    echo ""
    echo "Checking Service Alerts..."
    echo "========================="
    
    # Define services to check
    local services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    local service_down_alert=$(jq -r '.alert_rules.critical.service_down' "$ALERT_CONFIG")
    
    for service_info in "${services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if [ "$service_down_alert" = "true" ]; then
            if ! systemctl is-active --quiet $service_name; then
                send_email_alert "CRITICAL: Service Down" "$service_desc ($service_name) is not running"
                send_slack_alert "CRITICAL: Service Down" "$service_desc ($service_name) is not running"
            fi
        fi
    done
    
    echo "✅ Service alert check completed"
    log_message "Service alert check completed"
}

# Function to check application alerts
check_application_alerts() {
    log_message "Checking application alerts"
    
    echo ""
    echo "Checking Application Alerts..."
    echo "============================="
    
    # Check if web interface is accessible
    if ! curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        send_email_alert "CRITICAL: Web Interface Unreachable" "Atlas web interface is not responding"
        send_slack_alert "CRITICAL: Web Interface Unreachable" "Atlas web interface is not responding"
    fi
    
    # Check database connectivity
    if ! sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        send_email_alert "CRITICAL: Database Connection Failed" "Cannot connect to Atlas database"
        send_slack_alert "CRITICAL: Database Connection Failed" "Cannot connect to Atlas database"
    fi
    
    echo "✅ Application alert check completed"
    log_message "Application alert check completed"
}

# Function to generate alert report
generate_alert_report() {
    log_message "Generating alert report"
    
    echo ""
    echo "Generating Alert Report..."
    echo "========================="
    
    local report_file="$ALERT_HISTORY_DIR/alert_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create report header
    echo "Atlas Production Alert Report" > "$report_file"
    echo "Generated: $(date)" >> "$report_file"
    echo "============================" >> "$report_file"
    echo "" >> "$report_file"
    
    # Count alerts by severity
    local critical_count=0
    local warning_count=0
    local info_count=0
    
    # Check recent alert files
    for alert_file in "$ALERT_HISTORY_DIR"/alert_*.json; do
        if [ -f "$alert_file" ]; then
            local subject=$(jq -r '.subject' "$alert_file")
            if [[ "$subject" == *"CRITICAL"* ]]; then
                critical_count=$((critical_count + 1))
            elif [[ "$subject" == *"WARNING"* ]]; then
                warning_count=$((warning_count + 1))
            else
                info_count=$((info_count + 1))
            fi
        fi
    done
    
    echo "Alert Summary:" >> "$report_file"
    echo "-------------" >> "$report_file"
    echo "Critical Alerts: $critical_count" >> "$report_file"
    echo "Warning Alerts: $warning_count" >> "$report_file"
    echo "Info Alerts: $info_count" >> "$report_file"
    echo "" >> "$report_file"
    
    # List recent alerts
    echo "Recent Alerts:" >> "$report_file"
    echo "-------------" >> "$report_file"
    for alert_file in "$ALERT_HISTORY_DIR"/alert_*.json; do
        if [ -f "$alert_file" ]; then
            local timestamp=$(jq -r '.timestamp' "$alert_file")
            local subject=$(jq -r '.subject' "$alert_file")
            echo "$timestamp - $subject" >> "$report_file"
        fi
    done
    
    echo "✅ Alert report generated: $report_file"
    log_message "Alert report generated: $report_file"
    
    # Display summary
    echo ""
    echo "Alert Summary:"
    echo "  Critical: $critical_count"
    echo "  Warning: $warning_count"
    echo "  Info: $info_count"
    echo "Report saved to: $report_file"
}

# Function to clean old alert files
clean_old_alerts() {
    log_message "Cleaning old alert files"
    
    echo ""
    echo "Cleaning Old Alert Files..."
    echo "=========================="
    
    # Remove alert files older than 30 days
    find "$ALERT_HISTORY_DIR" -name "alert_*.json" -mtime +30 -delete 2>/dev/null || true
    find "$ALERT_HISTORY_DIR" -name "alert_report_*.txt" -mtime +30 -delete 2>/dev/null || true
    
    echo "✅ Old alert files cleaned"
    log_message "Old alert files cleaned"
}

# Function to list alert history
list_alert_history() {
    log_message "Listing alert history"
    
    echo "Alert History:"
    echo "=============="
    
    if [ -z "$(ls -A $ALERT_HISTORY_DIR/alert_*.json 2>/dev/null)" ]; then
        echo "❌ No alerts found"
        return 0
    fi
    
    # List recent alerts
    for alert_file in "$ALERT_HISTORY_DIR"/alert_*.json; do
        if [ -f "$alert_file" ]; then
            local timestamp=$(jq -r '.timestamp' "$alert_file")
            local subject=$(jq -r '.subject' "$alert_file")
            echo "$timestamp - $subject"
        fi
    done
}

# Main alert management function
main() {
    log_message "=== Starting Atlas Alert Management ==="
    
    # Initialize configuration
    initialize_alert_config
    
    # Start time
    local start_time=$(date)
    log_message "Alert management started at: $start_time"
    
    # Handle different alert management operations
    case $1 in
        "check")
            # Run all alert checks
            check_system_alerts
            check_service_alerts
            check_application_alerts
            ;;
        "system")
            check_system_alerts
            ;;
        "service")
            check_service_alerts
            ;;
        "application")
            check_application_alerts
            ;;
        "report")
            generate_alert_report
            ;;
        "clean")
            clean_old_alerts
            ;;
        "history")
            list_alert_history
            ;;
        "email")
            if [ $# -lt 3 ]; then
                echo "❌ Usage: $0 email <subject> <message>"
                return 1
            fi
            send_email_alert "$2" "$3"
            ;;
        "slack")
            if [ $# -lt 3 ]; then
                echo "❌ Usage: $0 slack <subject> <message>"
                return 1
            fi
            send_slack_alert "$2" "$3"
            ;;
        "sms")
            if [ $# -lt 3 ]; then
                echo "❌ Usage: $0 sms <subject> <message>"
                return 1
            fi
            send_sms_alert "$2" "$3"
            ;;
        *)
            # Run all operations
            check_system_alerts
            check_service_alerts
            check_application_alerts
            generate_alert_report
            clean_old_alerts
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Alert management completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Alert Management Completed ==="
    
    echo ""
    echo "✅ Alert management complete!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📁 Alert history stored in: $ALERT_HISTORY_DIR"
    echo "📝 Log file: $ALERT_LOG"
}

# Run main function
main "$@"