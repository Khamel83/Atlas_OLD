#!/bin/bash

# Atlas Production Incident Response Script
# This script manages incident response for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Incident Response..."

# Configuration
INCIDENT_LOG="/home/ubuntu/dev/atlas/logs/incident_response.log"
INCIDENT_REPORT_DIR="/home/ubuntu/dev/atlas/incidents"
INCIDENT_CONFIG="/home/ubuntu/dev/atlas/config/incidents.json"

# Create logs and incidents directories if they don't exist
mkdir -p "$(dirname $INCIDENT_LOG)"
mkdir -p "$INCIDENT_REPORT_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $INCIDENT_LOG
    echo "$1"
}

# Function to initialize incident configuration
initialize_incident_config() {
    log_message "Initializing incident configuration"
    
    # Create default incident configuration if it doesn't exist
    if [ ! -f "$INCIDENT_CONFIG" ]; then
        cat > "$INCIDENT_CONFIG" << EOF
{
    "incident_response": {
        "response_time_minutes": 30,
        "escalation_time_minutes": 60,
        "notification_recipients": ["admin@khamel.com"],
        "incident_severity_levels": {
            "critical": {
                "name": "Critical",
                "response_time_minutes": 15,
                "escalation_time_minutes": 30,
                "notification_channels": ["email", "sms", "slack"]
            },
            "high": {
                "name": "High",
                "response_time_minutes": 30,
                "escalation_time_minutes": 60,
                "notification_channels": ["email", "slack"]
            },
            "medium": {
                "name": "Medium",
                "response_time_minutes": 60,
                "escalation_time_minutes": 120,
                "notification_channels": ["email"]
            },
            "low": {
                "name": "Low",
                "response_time_minutes": 120,
                "escalation_time_minutes": 240,
                "notification_channels": ["email"]
            }
        }
    },
    "incident_categories": {
        "system_outage": {
            "name": "System Outage",
            "description": "Complete or partial system outage affecting service availability"
        },
        "performance_degradation": {
            "name": "Performance Degradation",
            "description": "Degraded system performance affecting user experience"
        },
        "security_breach": {
            "name": "Security Breach",
            "description": "Unauthorized access or security vulnerability exploited"
        },
        "data_loss": {
            "name": "Data Loss",
            "description": "Loss or corruption of critical system data"
        },
        "service_disruption": {
            "name": "Service Disruption",
            "description": "Partial service disruption affecting specific functionality"
        }
    },
    "incident_response_teams": {
        "primary": {
            "name": "Primary Response Team",
            "members": ["admin@khamel.com"],
            "roles": ["System Administrator"]
        },
        "secondary": {
            "name": "Secondary Response Team",
            "members": ["backup@khamel.com"],
            "roles": ["Backup Administrator"]
        }
    },
    "communication_channels": {
        "email": {
            "enabled": true,
            "smtp_server": "smtp.gmail.com",
            "port": 587,
            "sender": "atlas.alerts@gmail.com",
            "password": "your_app_password"
        },
        "slack": {
            "enabled": false,
            "webhook_url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
        },
        "sms": {
            "enabled": false,
            "twilio_account_sid": "YOUR_TWILIO_ACCOUNT_SID",
            "twilio_auth_token": "YOUR_TWILIO_AUTH_TOKEN",
            "twilio_phone_number": "+1234567890"
        }
    }
}
EOF
        echo "✅ Created default incident configuration"
        log_message "Default incident configuration created"
    else
        echo "✅ Incident configuration already exists"
    fi
}

# Function to create incident report
create_incident_report() {
    log_message "Creating incident report"
    
    echo "Creating Incident Report..."
    echo "========================="
    
    # Get incident details
    local incident_id="INC-$(date +%Y%m%d)-$(printf "%04d" $((RANDOM % 10000)))"
    local incident_timestamp=$(date -Iseconds)
    local incident_severity=${1:-"medium"}
    local incident_category=${2:-"service_disruption"}
    local incident_description=${3:-"Unspecified incident"}
    
    # Create incident directory
    local incident_dir="$INCIDENT_REPORT_DIR/$incident_id"
    mkdir -p "$incident_dir"
    
    # Create incident report file
    local incident_report="$incident_dir/incident_report.json"
    
    # Create incident report content
    cat > "$incident_report" << EOF
{
    "incident_id": "$incident_id",
    "timestamp": "$incident_timestamp",
    "severity": "$incident_severity",
    "category": "$incident_category",
    "description": "$incident_description",
    "status": "open",
    "assigned_to": "unassigned",
    "reporter": "$(whoami)",
    "communication_log": [],
    "actions_taken": [],
    "resolution": "",
    "closed_timestamp": ""
}
EOF
    
    # Create incident log file
    local incident_log="$incident_dir/incident.log"
    echo "Incident $incident_id created at $incident_timestamp" > "$incident_log"
    echo "Severity: $incident_severity" >> "$incident_log"
    echo "Category: $incident_category" >> "$incident_log"
    echo "Description: $incident_description" >> "$incident_log"
    echo "" >> "$incident_log"
    
    echo "✅ Incident report created: $incident_id"
    echo "📁 Incident files saved to: $incident_dir"
    log_message "Incident report created: $incident_id"
    
    # Display incident summary
    echo ""
    echo "Incident Summary:"
    echo "  ID: $incident_id"
    echo "  Timestamp: $incident_timestamp"
    echo "  Severity: $incident_severity"
    echo "  Category: $incident_category"
    echo "  Description: $incident_description"
    echo "  Status: open"
    echo "  Assigned To: unassigned"
    echo "  Reporter: $(whoami)"
    echo "  Report: $incident_report"
    echo "  Log: $incident_log"
    
    # Send incident notification
    send_incident_notification "$incident_id" "$incident_severity" "$incident_category" "$incident_description"
    
    return 0
}

# Function to send incident notification
send_incident_notification() {
    local incident_id=$1
    local incident_severity=$2
    local incident_category=$3
    local incident_description=$4
    
    log_message "Sending incident notification for $incident_id"
    
    echo "Sending Incident Notification..."
    echo "=============================="
    
    # Get notification configuration
    local notification_channels=$(jq -r '.incident_response.incident_severity_levels.'$incident_severity'.notification_channels[]' "$INCIDENT_CONFIG")
    
    # Create notification content
    local notification_content="Atlas Production Incident Notification

Incident ID: $incident_id
Timestamp: $(date -Iseconds)
Severity: $incident_severity
Category: $incident_category
Description: $incident_description

This is an automated notification from your Atlas production system.

For more information, check the incident report in:
$INCIDENT_REPORT_DIR/$incident_id/

To update this incident, use the incident management commands:
  - Update status: atlas_incident.sh update $incident_id <status>
  - Assign to team member: atlas_incident.sh assign $incident_id <member>
  - Add action: atlas_incident.sh action $incident_id <description>
  - Close incident: atlas_incident.sh close $incident_id <resolution>

To disable these notifications, update the configuration in:
$INCIDENT_CONFIG"

    # Send notifications to all configured channels
    while IFS= read -r channel; do
        case $channel in
            "email")
                send_email_notification "$incident_id" "$incident_severity" "$incident_category" "$incident_description" "$notification_content"
                ;;
            "slack")
                send_slack_notification "$incident_id" "$incident_severity" "$incident_category" "$incident_description" "$notification_content"
                ;;
            "sms")
                send_sms_notification "$incident_id" "$incident_severity" "$incident_category" "$incident_description" "$notification_content"
                ;;
        esac
    done <<< "$notification_channels"
    
    echo "✅ Incident notifications sent"
    log_message "Incident notifications sent for $incident_id"
}

# Function to send email notification
send_email_notification() {
    local incident_id=$1
    local incident_severity=$2
    local incident_category=$3
    local incident_description=$4
    local notification_content=$5
    
    log_message "Sending email notification for $incident_id"
    
    echo "Sending Email Notification..."
    echo "==========================="
    
    # Check if email notifications are enabled
    local email_enabled=$(jq -r '.communication_channels.email.enabled' "$INCIDENT_CONFIG")
    if [ "$email_enabled" != "true" ]; then
        echo "ℹ️ Email notifications are disabled"
        log_message "Email notifications are disabled"
        return 0
    fi
    
    # Get email configuration
    local smtp_server=$(jq -r '.communication_channels.email.smtp_server' "$INCIDENT_CONFIG")
    local port=$(jq -r '.communication_channels.email.port' "$INCIDENT_CONFIG")
    local sender_email=$(jq -r '.communication_channels.email.sender' "$INCIDENT_CONFIG")
    local sender_password=$(jq -r '.communication_channels.email.password' "$INCIDENT_CONFIG")
    local recipients=$(jq -r '.incident_response.notification_recipients[]' "$INCIDENT_CONFIG")
    
    # Validate required configuration
    if [ -z "$sender_email" ] || [ -z "$sender_password" ]; then
        echo "❌ Missing email configuration"
        log_message "Missing email configuration"
        return 1
    fi
    
    # Create email subject
    local email_subject="Atlas Incident: $incident_id - $incident_severity - $incident_category"
    
    # In a real implementation, this would send an actual email
    # For now, we'll just log the notification
    echo "📧 EMAIL NOTIFICATION: $email_subject"
    echo "To: $recipients"
    echo "$notification_content"
    echo ""
    
    # Log to incident communication log
    local incident_report="$INCIDENT_REPORT_DIR/$incident_id/incident_report.json"
    if [ -f "$incident_report" ]; then
        local timestamp=$(date -Iseconds)
        jq --arg timestamp "$timestamp" --arg channel "email" --arg subject "$email_subject" --arg content "$notification_content" '
            .communication_log += [{
                "timestamp": $timestamp,
                "channel": $channel,
                "subject": $subject,
                "content": $content
            }]
        ' "$incident_report" > "$incident_report.tmp" && mv "$incident_report.tmp" "$incident_report"
    fi
    
    echo "✅ Email notification sent"
    log_message "Email notification sent for $incident_id"
}

# Function to send Slack notification
send_slack_notification() {
    local incident_id=$1
    local incident_severity=$2
    local incident_category=$3
    local incident_description=$4
    local notification_content=$5
    
    log_message "Sending Slack notification for $incident_id"
    
    echo "Sending Slack Notification..."
    echo "==========================="
    
    # Check if Slack notifications are enabled
    local slack_enabled=$(jq -r '.communication_channels.slack.enabled' "$INCIDENT_CONFIG")
    if [ "$slack_enabled" != "true" ]; then
        echo "ℹ️ Slack notifications are disabled"
        log_message "Slack notifications are disabled"
        return 0
    fi
    
    # Get Slack configuration
    local webhook_url=$(jq -r '.communication_channels.slack.webhook_url' "$INCIDENT_CONFIG")
    
    # Validate required configuration
    if [ -z "$webhook_url" ]; then
        echo "❌ Missing Slack webhook URL"
        log_message "Missing Slack webhook URL"
        return 1
    fi
    
    # Create Slack message payload
    local severity_color="good"
    case $incident_severity in
        "critical")
            severity_color="danger"
            ;;
        "high")
            severity_color="warning"
            ;;
        "medium")
            severity_color="#36a64f"
            ;;
        "low")
            severity_color="good"
            ;;
    esac
    
    local payload=$(jq -n --arg incident_id "$incident_id" --arg severity "$incident_severity" --arg category "$incident_category" --arg description "$incident_description" --arg color "$severity_color" '{
        "text": "Atlas Production Incident",
        "attachments": [
            {
                "color": $color,
                "fields": [
                    {
                        "title": "Incident ID",
                        "value": $incident_id,
                        "short": true
                    },
                    {
                        "title": "Severity",
                        "value": $severity,
                        "short": true
                    },
                    {
                        "title": "Category",
                        "value": $category,
                        "short": true
                    },
                    {
                        "title": "Description",
                        "value": $description,
                        "short": false
                    },
                    {
                        "title": "Timestamp",
                        "value": "'$(date -Iseconds)'",
                        "short": true
                    }
                ]
            }
        ]
    }')
    
    # In a real implementation, this would send an actual Slack message
    # For now, we'll just log the notification
    echo "💬 SLACK NOTIFICATION: Atlas Incident $incident_id"
    echo "Webhook URL: $webhook_url"
    echo "$payload"
    echo ""
    
    # Log to incident communication log
    local incident_report="$INCIDENT_REPORT_DIR/$incident_id/incident_report.json"
    if [ -f "$incident_report" ]; then
        local timestamp=$(date -Iseconds)
        jq --arg timestamp "$timestamp" --arg channel "slack" --arg subject "Atlas Incident $incident_id" --arg content "$payload" '
            .communication_log += [{
                "timestamp": $timestamp,
                "channel": $channel,
                "subject": $subject,
                "content": $content
            }]
        ' "$incident_report" > "$incident_report.tmp" && mv "$incident_report.tmp" "$incident_report"
    fi
    
    echo "✅ Slack notification sent"
    log_message "Slack notification sent for $incident_id"
}

# Function to send SMS notification
send_sms_notification() {
    local incident_id=$1
    local incident_severity=$2
    local incident_category=$3
    local incident_description=$4
    local notification_content=$5
    
    log_message "Sending SMS notification for $incident_id"
    
    echo "Sending SMS Notification..."
    echo "========================="
    
    # Check if SMS notifications are enabled
    local sms_enabled=$(jq -r '.communication_channels.sms.enabled' "$INCIDENT_CONFIG")
    if [ "$sms_enabled" != "true" ]; then
        echo "ℹ️ SMS notifications are disabled"
        log_message "SMS notifications are disabled"
        return 0
    fi
    
    # Get SMS configuration
    local twilio_account_sid=$(jq -r '.communication_channels.sms.twilio_account_sid' "$INCIDENT_CONFIG")
    local twilio_auth_token=$(jq -r '.communication_channels.sms.twilio_auth_token' "$INCIDENT_CONFIG")
    local twilio_phone_number=$(jq -r '.communication_channels.sms.twilio_phone_number' "$INCIDENT_CONFIG")
    local recipient_phone_numbers=$(jq -r '.incident_response.notification_recipients[]' "$INCIDENT_CONFIG")
    
    # Validate required configuration
    if [ -z "$twilio_account_sid" ] || [ -z "$twilio_auth_token" ] || [ -z "$twilio_phone_number" ]; then
        echo "❌ Missing SMS configuration"
        log_message "Missing SMS configuration"
        return 1
    fi
    
    # Create SMS message
    local sms_message="Atlas Incident: $incident_id - $incident_severity - $incident_category"
    
    # In a real implementation, this would send an actual SMS
    # For now, we'll just log the notification
    echo "📱 SMS NOTIFICATION: $sms_message"
    echo "To: $recipient_phone_numbers"
    echo "From: $twilio_phone_number"
    echo "Twilio Account SID: $twilio_account_sid"
    echo ""
    
    # Log to incident communication log
    local incident_report="$INCIDENT_REPORT_DIR/$incident_id/incident_report.json"
    if [ -f "$incident_report" ]; then
        local timestamp=$(date -Iseconds)
        jq --arg timestamp "$timestamp" --arg channel "sms" --arg subject "$sms_message" --arg content "Sent to $recipient_phone_numbers" '
            .communication_log += [{
                "timestamp": $timestamp,
                "channel": $channel,
                "subject": $subject,
                "content": $content
            }]
        ' "$incident_report" > "$incident_report.tmp" && mv "$incident_report.tmp" "$incident_report"
    fi
    
    echo "✅ SMS notification sent"
    log_message "SMS notification sent for $incident_id"
}

# Function to update incident status
update_incident_status() {
    local incident_id=$1
    local new_status=$2
    
    log_message "Updating incident $incident_id status to $new_status"
    
    echo "Updating Incident Status..."
    echo "========================="
    
    # Check if incident exists
    local incident_report="$INCIDENT_REPORT_DIR/$incident_id/incident_report.json"
    if [ ! -f "$incident_report" ]; then
        echo "❌ Incident $incident_id not found"
        log_message "Incident $incident_id not found"
        return 1
    fi
    
    # Update incident status
    local timestamp=$(date -Iseconds)
    jq --arg status "$new_status" --arg timestamp "$timestamp" '
        .status = $status |
        .actions_taken += [{
            "timestamp": $timestamp,
            "action": "status_update",
            "description": "Status updated to " + $status
        }]
    ' "$incident_report" > "$incident_report.tmp" && mv "$incident_report.tmp" "$incident_report"
    
    # Log to incident log
    local incident_log="$INCIDENT_REPORT_DIR/$incident_id/incident.log"
    echo "[$timestamp] Status updated to $new_status" >> "$incident_log"
    
    echo "✅ Incident $incident_id status updated to $new_status"
    log_message "Incident $incident_id status updated to $new_status"
    
    # Display updated incident summary
    echo ""
    echo "Updated Incident Summary:"
    echo "  ID: $incident_id"
    echo "  Status: $new_status"
    echo "  Timestamp: $timestamp"
    echo "  Report: $incident_report"
    echo "  Log: $incident_log"
}

# Function to assign incident to team member
assign_incident() {
    local incident_id=$1
    local assigned_member=$2
    
    log_message "Assigning incident $incident_id to $assigned_member"
    
    echo "Assigning Incident..."
    echo "==================="
    
    # Check if incident exists
    local incident_report="$INCIDENT_REPORT_DIR/$incident_id/incident_report.json"
    if [ ! -f "$incident_report" ]; then
        echo "❌ Incident $incident_id not found"
        log_message "Incident $incident_id not found"
        return 1
    fi
    
    # Assign incident to team member
    local timestamp=$(date -Iseconds)
    jq --arg member "$assigned_member" --arg timestamp "$timestamp" '
        .assigned_to = $member |
        .actions_taken += [{
            "timestamp": $timestamp,
            "action": "assignment",
            "description": "Assigned to " + $member
        }]
    ' "$incident_report" > "$incident_report.tmp" && mv "$incident_report.tmp" "$incident_report"
    
    # Log to incident log
    local incident_log="$INCIDENT_REPORT_DIR/$incident_id/incident.log"
    echo "[$timestamp] Assigned to $assigned_member" >> "$incident_log"
    
    echo "✅ Incident $incident_id assigned to $assigned_member"
    log_message "Incident $incident_id assigned to $assigned_member"
    
    # Display updated incident summary
    echo ""
    echo "Updated Incident Summary:"
    echo "  ID: $incident_id"
    echo "  Assigned To: $assigned_member"
    echo "  Timestamp: $timestamp"
    echo "  Report: $incident_report"
    echo "  Log: $incident_log"
}

# Function to add action to incident
add_incident_action() {
    local incident_id=$1
    local action_description=$2
    
    log_message "Adding action to incident $incident_id: $action_description"
    
    echo "Adding Incident Action..."
    echo "======================"
    
    # Check if incident exists
    local incident_report="$INCIDENT_REPORT_DIR/$incident_id/incident_report.json"
    if [ ! -f "$incident_report" ]; then
        echo "❌ Incident $incident_id not found"
        log_message "Incident $incident_id not found"
        return 1
    fi
    
    # Add action to incident
    local timestamp=$(date -Iseconds)
    jq --arg description "$action_description" --arg timestamp "$timestamp" '
        .actions_taken += [{
            "timestamp": $timestamp,
            "action": "manual_action",
            "description": $description
        }]
    ' "$incident_report" > "$incident_report.tmp" && mv "$incident_report.tmp" "$incident_report"
    
    # Log to incident log
    local incident_log="$INCIDENT_REPORT_DIR/$incident_id/incident.log"
    echo "[$timestamp] Manual action: $action_description" >> "$incident_log"
    
    echo "✅ Action added to incident $incident_id"
    log_message "Action added to incident $incident_id: $action_description"
    
    # Display updated incident summary
    echo ""
    echo "Updated Incident Summary:"
    echo "  ID: $incident_id"
    echo "  Action: $action_description"
    echo "  Timestamp: $timestamp"
    echo "  Report: $incident_report"
    echo "  Log: $incident_log"
}

# Function to close incident
close_incident() {
    local incident_id=$1
    local resolution=$2
    
    log_message "Closing incident $incident_id with resolution: $resolution"
    
    echo "Closing Incident..."
    echo "================"
    
    # Check if incident exists
    local incident_report="$INCIDENT_REPORT_DIR/$incident_id/incident_report.json"
    if [ ! -f "$incident_report" ]; then
        echo "❌ Incident $incident_id not found"
        log_message "Incident $incident_id not found"
        return 1
    fi
    
    # Close incident
    local timestamp=$(date -Iseconds)
    jq --arg resolution "$resolution" --arg timestamp "$timestamp" --arg closed_timestamp "$timestamp" '
        .status = "closed" |
        .resolution = $resolution |
        .closed_timestamp = $closed_timestamp |
        .actions_taken += [{
            "timestamp": $timestamp,
            "action": "closure",
            "description": "Incident closed with resolution: " + $resolution
        }]
    ' "$incident_report" > "$incident_report.tmp" && mv "$incident_report.tmp" "$incident_report"
    
    # Log to incident log
    local incident_log="$INCIDENT_REPORT_DIR/$incident_id/incident.log"
    echo "[$timestamp] Incident closed with resolution: $resolution" >> "$incident_log"
    
    echo "✅ Incident $incident_id closed"
    log_message "Incident $incident_id closed with resolution: $resolution"
    
    # Send closure notification
    local incident_severity=$(jq -r '.severity' "$incident_report")
    local incident_category=$(jq -r '.category' "$incident_report")
    local incident_description=$(jq -r '.description' "$incident_report")
    
    send_incident_closure_notification "$incident_id" "$incident_severity" "$incident_category" "$incident_description" "$resolution"
    
    # Display updated incident summary
    echo ""
    echo "Closed Incident Summary:"
    echo "  ID: $incident_id"
    echo "  Status: closed"
    echo "  Resolution: $resolution"
    echo "  Closed At: $timestamp"
    echo "  Report: $incident_report"
    echo "  Log: $incident_log"
}

# Function to send incident closure notification
send_incident_closure_notification() {
    local incident_id=$1
    local incident_severity=$2
    local incident_category=$3
    local incident_description=$4
    local resolution=$5
    
    log_message "Sending incident closure notification for $incident_id"
    
    echo "Sending Incident Closure Notification..."
    echo "======================================"
    
    # Get notification configuration
    local notification_channels=$(jq -r '.incident_response.incident_severity_levels.'$incident_severity'.notification_channels[]' "$INCIDENT_CONFIG")
    
    # Create closure notification content
    local closure_content="Atlas Production Incident Closure Notification

Incident ID: $incident_id
Timestamp: $(date -Iseconds)
Severity: $incident_severity
Category: $incident_category
Description: $incident_description
Resolution: $resolution

This is an automated notification from your Atlas production system.

The incident has been resolved with the following resolution:
$resolution

For more information, check the incident report in:
$INCIDENT_REPORT_DIR/$incident_id/

To disable these notifications, update the configuration in:
$INCIDENT_CONFIG"

    # Send closure notifications to all configured channels
    while IFS= read -r channel; do
        case $channel in
            "email")
                send_email_closure_notification "$incident_id" "$incident_severity" "$incident_category" "$incident_description" "$resolution" "$closure_content"
                ;;
            "slack")
                send_slack_closure_notification "$incident_id" "$incident_severity" "$incident_category" "$incident_description" "$resolution" "$closure_content"
                ;;
            "sms")
                send_sms_closure_notification "$incident_id" "$incident_severity" "$incident_category" "$incident_description" "$resolution" "$closure_content"
                ;;
        esac
    done <<< "$notification_channels"
    
    echo "✅ Incident closure notifications sent"
    log_message "Incident closure notifications sent for $incident_id"
}

# Function to send email closure notification
send_email_closure_notification() {
    local incident_id=$1
    local incident_severity=$2
    local incident_category=$3
    local incident_description=$4
    local resolution=$5
    local closure_content=$6
    
    log_message "Sending email closure notification for $incident_id"
    
    echo "Sending Email Closure Notification..."
    echo "=================================="
    
    # Check if email notifications are enabled
    local email_enabled=$(jq -r '.communication_channels.email.enabled' "$INCIDENT_CONFIG")
    if [ "$email_enabled" != "true" ]; then
        echo "ℹ️ Email notifications are disabled"
        log_message "Email notifications are disabled"
        return 0
    fi
    
    # Get email configuration
    local smtp_server=$(jq -r '.communication_channels.email.smtp_server' "$INCIDENT_CONFIG")
    local port=$(jq -r '.communication_channels.email.port' "$INCIDENT_CONFIG")
    local sender_email=$(jq -r '.communication_channels.email.sender' "$INCIDENT_CONFIG")
    local sender_password=$(jq -r '.communication_channels.email.password' "$INCIDENT_CONFIG")
    local recipients=$(jq -r '.incident_response.notification_recipients[]' "$INCIDENT_CONFIG")
    
    # Validate required configuration
    if [ -z "$sender_email" ] || [ -z "$sender_password" ]; then
        echo "❌ Missing email configuration"
        log_message "Missing email configuration"
        return 1
    fi
    
    # Create email subject
    local email_subject="Atlas Incident Resolved: $incident_id - $incident_severity - $incident_category"
    
    # In a real implementation, this would send an actual email
    # For now, we'll just log the notification
    echo "📧 EMAIL CLOSURE NOTIFICATION: $email_subject"
    echo "To: $recipients"
    echo "$closure_content"
    echo ""
    
    echo "✅ Email closure notification sent"
    log_message "Email closure notification sent for $incident_id"
}

# Function to send Slack closure notification
send_slack_closure_notification() {
    local incident_id=$1
    local incident_severity=$2
    local incident_category=$3
    local incident_description=$4
    local resolution=$5
    local closure_content=$6
    
    log_message "Sending Slack closure notification for $incident_id"
    
    echo "Sending Slack Closure Notification..."
    echo "=================================="
    
    # Check if Slack notifications are enabled
    local slack_enabled=$(jq -r '.communication_channels.slack.enabled' "$INCIDENT_CONFIG")
    if [ "$slack_enabled" != "true" ]; then
        echo "ℹ️ Slack notifications are disabled"
        log_message "Slack notifications are disabled"
        return 0
    fi
    
    # Get Slack configuration
    local webhook_url=$(jq -r '.communication_channels.slack.webhook_url' "$INCIDENT_CONFIG")
    
    # Validate required configuration
    if [ -z "$webhook_url" ]; then
        echo "❌ Missing Slack webhook URL"
        log_message "Missing Slack webhook URL"
        return 1
    fi
    
    # Create Slack message payload
    local severity_color="good"
    case $incident_severity in
        "critical")
            severity_color="good"
            ;;
        "high")
            severity_color="good"
            ;;
        "medium")
            severity_color="good"
            ;;
        "low")
            severity_color="good"
            ;;
    esac
    
    local payload=$(jq -n --arg incident_id "$incident_id" --arg severity "$incident_severity" --arg category "$incident_category" --arg description "$incident_description" --arg resolution "$resolution" --arg color "$severity_color" '{
        "text": "Atlas Production Incident Resolved",
        "attachments": [
            {
                "color": $color,
                "fields": [
                    {
                        "title": "Incident ID",
                        "value": $incident_id,
                        "short": true
                    },
                    {
                        "title": "Severity",
                        "value": $severity,
                        "short": true
                    },
                    {
                        "title": "Category",
                        "value": $category,
                        "short": true
                    },
                    {
                        "title": "Description",
                        "value": $description,
                        "short": false
                    },
                    {
                        "title": "Resolution",
                        "value": $resolution,
                        "short": false
                    },
                    {
                        "title": "Timestamp",
                        "value": "'$(date -Iseconds)'",
                        "short": true
                    }
                ]
            }
        ]
    }')
    
    # In a real implementation, this would send an actual Slack message
    # For now, we'll just log the notification
    echo "💬 SLACK CLOSURE NOTIFICATION: Atlas Incident $incident_id Resolved"
    echo "Webhook URL: $webhook_url"
    echo "$payload"
    echo ""
    
    echo "✅ Slack closure notification sent"
    log_message "Slack closure notification sent for $incident_id"
}

# Function to send SMS closure notification
send_sms_closure_notification() {
    local incident_id=$1
    local incident_severity=$2
    local incident_category=$3
    local incident_description=$4
    local resolution=$5
    local closure_content=$6
    
    log_message "Sending SMS closure notification for $incident_id"
    
    echo "Sending SMS Closure Notification..."
    echo "================================"
    
    # Check if SMS notifications are enabled
    local sms_enabled=$(jq -r '.communication_channels.sms.enabled' "$INCIDENT_CONFIG")
    if [ "$sms_enabled" != "true" ]; then
        echo "ℹ️ SMS notifications are disabled"
        log_message "SMS notifications are disabled"
        return 0
    fi
    
    # Get SMS configuration
    local twilio_account_sid=$(jq -r '.communication_channels.sms.twilio_account_sid' "$INCIDENT_CONFIG")
    local twilio_auth_token=$(jq -r '.communication_channels.sms.twilio_auth_token' "$INCIDENT_CONFIG")
    local twilio_phone_number=$(jq -r '.communication_channels.sms.twilio_phone_number' "$INCIDENT_CONFIG")
    local recipient_phone_numbers=$(jq -r '.incident_response.notification_recipients[]' "$INCIDENT_CONFIG")
    
    # Validate required configuration
    if [ -z "$twilio_account_sid" ] || [ -z "$twilio_auth_token" ] || [ -z "$twilio_phone_number" ]; then
        echo "❌ Missing SMS configuration"
        log_message "Missing SMS configuration"
        return 1
    fi
    
    # Create SMS message
    local sms_message="Atlas Incident Resolved: $incident_id - $incident_severity - $incident_category"
    
    # In a real implementation, this would send an actual SMS
    # For now, we'll just log the notification
    echo "📱 SMS CLOSURE NOTIFICATION: $sms_message"
    echo "To: $recipient_phone_numbers"
    echo "From: $twilio_phone_number"
    echo "Twilio Account SID: $twilio_account_sid"
    echo ""
    
    echo "✅ SMS closure notification sent"
    log_message "SMS closure notification sent for $incident_id"
}

# Function to list incidents
list_incidents() {
    log_message "Listing incidents"
    
    echo "Listing Incidents..."
    echo "=================="
    
    # Check if incidents directory exists
    if [ ! -d "$INCIDENT_REPORT_DIR" ] || [ -z "$(ls -A $INCIDENT_REPORT_DIR)" ]; then
        echo "❌ No incidents found"
        log_message "No incidents found"
        return 0
    fi
    
    echo "Recent Incidents:"
    echo "----------------"
    
    # List recent incidents
    for incident_dir in "$INCIDENT_REPORT_DIR"/*; do
        if [ -d "$incident_dir" ]; then
            local incident_id=$(basename "$incident_dir")
            local incident_report="$incident_dir/incident_report.json"
            
            if [ -f "$incident_report" ]; then
                local incident_timestamp=$(jq -r '.timestamp' "$incident_report")
                local incident_severity=$(jq -r '.severity' "$incident_report")
                local incident_category=$(jq -r '.category' "$incident_report")
                local incident_description=$(jq -r '.description' "$incident_report")
                local incident_status=$(jq -r '.status' "$incident_report")
                local incident_assigned=$(jq -r '.assigned_to' "$incident_report")
                
                echo "ID: $incident_id"
                echo "  Timestamp: $incident_timestamp"
                echo "  Severity: $incident_severity"
                echo "  Category: $incident_category"
                echo "  Description: $incident_description"
                echo "  Status: $incident_status"
                echo "  Assigned To: $incident_assigned"
                echo ""
            fi
        fi
    done
    
    echo "✅ Incidents listed"
    log_message "Incidents listed"
}

# Function to view incident details
view_incident() {
    local incident_id=$1
    
    log_message "Viewing incident $incident_id"
    
    echo "Viewing Incident Details..."
    echo "========================="
    
    # Check if incident exists
    local incident_report="$INCIDENT_REPORT_DIR/$incident_id/incident_report.json"
    if [ ! -f "$incident_report" ]; then
        echo "❌ Incident $incident_id not found"
        log_message "Incident $incident_id not found"
        return 1
    fi
    
    # Display incident details
    echo "Incident Details:"
    echo "================"
    echo "ID: $incident_id"
    echo "Timestamp: $(jq -r '.timestamp' "$incident_report")"
    echo "Severity: $(jq -r '.severity' "$incident_report")"
    echo "Category: $(jq -r '.category' "$incident_report")"
    echo "Description: $(jq -r '.description' "$incident_report")"
    echo "Status: $(jq -r '.status' "$incident_report")"
    echo "Assigned To: $(jq -r '.assigned_to' "$incident_report")"
    echo "Reporter: $(jq -r '.reporter' "$incident_report")"
    echo ""
    
    # Display communication log
    echo "Communication Log:"
    echo "----------------"
    local communication_count=$(jq -r '.communication_log | length' "$incident_report")
    if [ $communication_count -gt 0 ]; then
        for ((i=0; i<$communication_count; i++)); do
            local comm_timestamp=$(jq -r ".communication_log[$i].timestamp" "$incident_report")
            local comm_channel=$(jq -r ".communication_log[$i].channel" "$incident_report")
            local comm_subject=$(jq -r ".communication_log[$i].subject" "$incident_report")
            
            echo "[$comm_timestamp] $comm_channel: $comm_subject"
        done
    else
        echo "No communication log entries"
    fi
    echo ""
    
    # Display actions taken
    echo "Actions Taken:"
    echo "-------------"
    local actions_count=$(jq -r '.actions_taken | length' "$incident_report")
    if [ $actions_count -gt 0 ]; then
        for ((i=0; i<$actions_count; i++)); do
            local action_timestamp=$(jq -r ".actions_taken[$i].timestamp" "$incident_report")
            local action_type=$(jq -r ".actions_taken[$i].action" "$incident_report")
            local action_description=$(jq -r ".actions_taken[$i].description" "$incident_report")
            
            echo "[$action_timestamp] $action_type: $action_description"
        done
    else
        echo "No actions taken"
    fi
    echo ""
    
    # Display resolution
    local incident_status=$(jq -r '.status' "$incident_report")
    if [ "$incident_status" = "closed" ]; then
        echo "Resolution:"
        echo "----------"
        echo "Resolution: $(jq -r '.resolution' "$incident_report")"
        echo "Closed At: $(jq -r '.closed_timestamp' "$incident_report")"
        echo ""
    fi
    
    echo "✅ Incident details displayed"
    log_message "Incident details displayed for $incident_id"
}

# Function to clean old incident reports
clean_old_incidents() {
    log_message "Cleaning old incident reports"
    
    echo "Cleaning Old Incident Reports..."
    echo "=============================="
    
    # Remove incident reports older than 90 days
    find "$INCIDENT_REPORT_DIR" -name "INC-*" -mtime +90 -exec rm -rf {} \; 2>/dev/null || true
    
    echo "✅ Old incident reports cleaned"
    log_message "Old incident reports cleaned"
}

# Main incident response function
main() {
    log_message "=== Starting Atlas Incident Response ==="
    
    # Initialize configuration
    initialize_incident_config
    
    # Start time
    local start_time=$(date)
    log_message "Incident response started at: $start_time"
    
    # Handle different incident response operations
    case $1 in
        "create")
            if [ $# -lt 4 ]; then
                echo "❌ Usage: $0 create <severity> <category> <description>"
                echo "Available severities: critical, high, medium, low"
                echo "Available categories: system_outage, performance_degradation, security_breach, data_loss, service_disruption"
                return 1
            fi
            create_incident_report "$2" "$3" "$4"
            ;;
        "update")
            if [ $# -lt 3 ]; then
                echo "❌ Usage: $0 update <incident_id> <status>"
                return 1
            fi
            update_incident_status "$2" "$3"
            ;;
        "assign")
            if [ $# -lt 3 ]; then
                echo "❌ Usage: $0 assign <incident_id> <member>"
                return 1
            fi
            assign_incident "$2" "$3"
            ;;
        "action")
            if [ $# -lt 3 ]; then
                echo "❌ Usage: $0 action <incident_id> <description>"
                return 1
            fi
            add_incident_action "$2" "$3"
            ;;
        "close")
            if [ $# -lt 3 ]; then
                echo "❌ Usage: $0 close <incident_id> <resolution>"
                return 1
            fi
            close_incident "$2" "$3"
            ;;
        "list")
            list_incidents
            ;;
        "view")
            if [ $# -lt 2 ]; then
                echo "❌ Usage: $0 view <incident_id>"
                return 1
            fi
            view_incident "$2"
            ;;
        "notify")
            if [ $# -lt 5 ]; then
                echo "❌ Usage: $0 notify <incident_id> <severity> <category> <description>"
                return 1
            fi
            send_incident_notification "$2" "$3" "$4" "$5"
            ;;
        "clean")
            clean_old_incidents
            ;;
        *)
            # Display help
            echo "Atlas Production Incident Response System"
            echo "======================================"
            echo ""
            echo "Usage:"
            echo "  $0 create <severity> <category> <description>  Create new incident"
            echo "  $0 update <incident_id> <status>               Update incident status"
            echo "  $0 assign <incident_id> <member>               Assign incident to member"
            echo "  $0 action <incident_id> <description>          Add action to incident"
            echo "  $0 close <incident_id> <resolution>            Close incident"
            echo "  $0 list                                        List all incidents"
            echo "  $0 view <incident_id>                          View incident details"
            echo "  $0 notify <incident_id> <severity> <category> <description>"
            echo "                                                 Send incident notification"
            echo "  $0 clean                                       Clean old incident reports"
            echo ""
            echo "Examples:"
            echo "  $0 create critical system_outage \"Complete system outage\""
            echo "  $0 update INC-20231201-0001 investigating"
            echo "  $0 assign INC-20231201-0001 admin@khamel.com"
            echo "  $0 action INC-20231201-0001 \"Restarting services\""
            echo "  $0 close INC-20231201-0001 \"System restarted successfully\""
            echo "  $0 list"
            echo "  $0 view INC-20231201-0001"
            echo "  $0 notify INC-20231201-0001 critical system_outage \"Complete system outage\""
            echo "  $0 clean"
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Incident response completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Incident Response Completed ==="
    
    echo ""
    echo "✅ Incident response operations completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $INCIDENT_REPORT_DIR"
    echo "📝 Log file: $INCIDENT_LOG"
}

# Run main function
main "$@"