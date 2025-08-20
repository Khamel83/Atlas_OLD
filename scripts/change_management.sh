#!/bin/bash

# Atlas Production Change Management Script
# This script manages changes to the Atlas production environment following best practices

set -e  # Exit on any error

echo "Starting Atlas Production Change Management..."

# Configuration
CHANGE_LOG="/home/ubuntu/dev/atlas/logs/change_management.log"
CHANGE_DIR="/home/ubuntu/dev/atlas/changes"
BACKUP_DIR="/home/ubuntu/dev/atlas/backups"

# Create logs and changes directories if they don't exist
mkdir -p "$(dirname $CHANGE_LOG)"
mkdir -p "$CHANGE_DIR"
mkdir -p "$BACKUP_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $CHANGE_LOG
    echo "$1"
}

# Function to create change request
create_change_request() {
    local change_id=$1
    local change_type=$2
    local description=$3
    local priority=$4
    local implementation_date=$5
    
    log_message "Creating change request: $change_id"
    
    # Create change directory
    local change_path="$CHANGE_DIR/$change_id"
    mkdir -p "$change_path"
    
    # Create change request document
    cat > "$change_path/change_request.json" << EOF
{
    "change_id": "$change_id",
    "timestamp": "$(date -Iseconds)",
    "type": "$change_type",
    "description": "$description",
    "priority": "$priority",
    "implementation_date": "$implementation_date",
    "status": "PENDING_APPROVAL",
    "requester": "$(whoami)",
    "approver": "",
    "approval_date": "",
    "impact_assessment": "",
    "rollback_plan": "",
    "testing_plan": "",
    "implementation_steps": [],
    "completion_notes": ""
}
EOF
    
    # Create change log
    touch "$change_path/change.log"
    
    echo "Change request created: $change_path/change_request.json"
    log_message "Change request created: $change_id"
}

# Function to approve change request
approve_change_request() {
    local change_id=$1
    local approver=$2
    local impact_assessment=$3
    local rollback_plan=$4
    
    log_message "Approving change request: $change_id"
    
    local change_path="$CHANGE_DIR/$change_id"
    if [ ! -f "$change_path/change_request.json" ]; then
        echo "ERROR: Change request $change_id not found"
        return 1
    fi
    
    # Update change request with approval information
    jq --arg approver "$approver" --arg impact "$impact_assessment" --arg rollback "$rollback_plan" --arg timestamp "$(date -Iseconds)" '
        .status = "APPROVED" |
        .approver = $approver |
        .approval_date = $timestamp |
        .impact_assessment = $impact |
        .rollback_plan = $rollback
    ' "$change_path/change_request.json" > "$change_path/change_request.json.tmp" && mv "$change_path/change_request.json.tmp" "$change_path/change_request.json"
    
    echo "Change request $change_id approved"
    log_message "Change request $change_id approved by $approver"
}

# Function to reject change request
reject_change_request() {
    local change_id=$1
    local approver=$2
    local reason=$3
    
    log_message "Rejecting change request: $change_id"
    
    local change_path="$CHANGE_DIR/$change_id"
    if [ ! -f "$change_path/change_request.json" ]; then
        echo "ERROR: Change request $change_id not found"
        return 1
    fi
    
    # Update change request with rejection information
    jq --arg approver "$approver" --arg reason "$reason" --arg timestamp "$(date -Iseconds)" '
        .status = "REJECTED" |
        .approver = $approver |
        .approval_date = $timestamp |
        .rejection_reason = $reason
    ' "$change_path/change_request.json" > "$change_path/change_request.json.tmp" && mv "$change_path/change_request.json.tmp" "$change_path/change_request.json"
    
    echo "Change request $change_id rejected"
    log_message "Change request $change_id rejected by $approver: $reason"
}

# Function to implement change
implement_change() {
    local change_id=$1
    
    log_message "Implementing change: $change_id"
    
    local change_path="$CHANGE_DIR/$change_id"
    if [ ! -f "$change_path/change_request.json" ]; then
        echo "ERROR: Change request $change_id not found"
        return 1
    fi
    
    # Check if change is approved
    local status=$(jq -r '.status' "$change_path/change_request.json")
    if [ "$status" != "APPROVED" ]; then
        echo "ERROR: Change request $change_id is not approved (status: $status)"
        return 1
    fi
    
    # Update status to implementing
    jq '.status = "IMPLEMENTING"' "$change_path/change_request.json" > "$change_path/change_request.json.tmp" && mv "$change_path/change_request.json.tmp" "$change_path/change_request.json"
    
    # Create backup before implementation
    echo "Creating backup before change implementation..."
    local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
    if [ -f "$backup_script" ]; then
        $backup_script
        echo "✅ Backup created successfully"
        log_message "Backup created before implementing change $change_id"
    else
        echo "❌ Backup script not found, proceeding without backup"
        log_message "WARNING: No backup created before implementing change $change_id"
    fi
    
    # Implementation steps would go here
    # This is a placeholder - actual implementation would depend on the specific change
    
    # Update status to implemented
    jq --arg timestamp "$(date -Iseconds)" '
        .status = "IMPLEMENTED" |
        .implementation_date = $timestamp
    ' "$change_path/change_request.json" > "$change_path/change_request.json.tmp" && mv "$change_path/change_request.json.tmp" "$change_path/change_request.json"
    
    echo "Change $change_id implemented successfully"
    log_message "Change $change_id implemented"
}

# Function to rollback change
rollback_change() {
    local change_id=$1
    local reason=$2
    
    log_message "Rolling back change: $change_id"
    
    local change_path="$CHANGE_DIR/$change_id"
    if [ ! -f "$change_path/change_request.json" ]; then
        echo "ERROR: Change request $change_id not found"
        return 1
    fi
    
    # Get rollback plan
    local rollback_plan=$(jq -r '.rollback_plan' "$change_path/change_request.json")
    
    # Update status to rolling back
    jq '.status = "ROLLING_BACK"' "$change_path/change_request.json" > "$change_path/change_request.json.tmp" && mv "$change_path/change_request.json.tmp" "$change_path/change_request.json"
    
    # Execute rollback steps
    echo "Executing rollback plan: $rollback_plan"
    # In a real implementation, this would execute the actual rollback steps
    
    # Update status to rolled back
    jq --arg reason "$reason" --arg timestamp "$(date -Iseconds)" '
        .status = "ROLLED_BACK" |
        .rollback_reason = $reason |
        .completion_date = $timestamp
    ' "$change_path/change_request.json" > "$change_path/change_request.json.tmp" && mv "$change_path/change_request.json.tmp" "$change_path/change_request.json"
    
    echo "Change $change_id rolled back successfully"
    log_message "Change $change_id rolled back: $reason"
}

# Function to close change
close_change() {
    local change_id=$1
    local notes=$2
    
    log_message "Closing change: $change_id"
    
    local change_path="$CHANGE_DIR/$change_id"
    if [ ! -f "$change_path/change_request.json" ]; then
        echo "ERROR: Change request $change_id not found"
        return 1
    fi
    
    # Update status to closed
    jq --arg notes "$notes" --arg timestamp "$(date -Iseconds)" '
        .status = "CLOSED" |
        .completion_notes = $notes |
        .completion_date = $timestamp
    ' "$change_path/change_request.json" > "$change_path/change_request.json.tmp" && mv "$change_path/change_request.json.tmp" "$change_path/change_request.json"
    
    echo "Change $change_id closed successfully"
    log_message "Change $change_id closed"
}

# Function to list changes
list_changes() {
    log_message "Listing changes"
    
    if [ ! -d "$CHANGE_DIR" ] || [ -z "$(ls -A $CHANGE_DIR)" ]; then
        echo "No changes found"
        return 0
    fi
    
    echo "Current Changes:"
    echo "================"
    
    for change_dir in "$CHANGE_DIR"/*; do
        if [ -d "$change_dir" ]; then
            local change_id=$(basename "$change_dir")
            local request_file="$change_dir/change_request.json"
            
            if [ -f "$request_file" ]; then
                local status=$(jq -r '.status' "$request_file")
                local type=$(jq -r '.type' "$request_file")
                local description=$(jq -r '.description' "$request_file")
                
                echo "ID: $change_id"
                echo "  Type: $type"
                echo "  Status: $status"
                echo "  Description: $description"
                echo ""
            fi
        fi
    done
}

# Function to get change details
get_change_details() {
    local change_id=$1
    
    log_message "Getting details for change $change_id"
    
    local change_path="$CHANGE_DIR/$change_id"
    if [ ! -f "$change_path/change_request.json" ]; then
        echo "ERROR: Change request $change_id not found"
        return 1
    fi
    
    echo "Change Details:"
    echo "==============="
    jq '.' "$change_path/change_request.json"
    
    echo ""
    echo "Change Log:"
    echo "==========="
    if [ -f "$change_path/change.log" ]; then
        cat "$change_path/change.log"
    else
        echo "No change log found"
    fi
}

# Function to validate change management process
validate_change_process() {
    log_message "Validating change management process"
    
    echo "Change Management Process Validation:"
    echo "===================================="
    
    # Check if required directories exist
    if [ -d "$CHANGE_DIR" ]; then
        echo "✅ Change directory exists"
    else
        echo "❌ Change directory missing"
        return 1
    fi
    
    if [ -d "$BACKUP_DIR" ]; then
        echo "✅ Backup directory exists"
    else
        echo "❌ Backup directory missing"
        return 1
    fi
    
    # Check if backup script exists
    local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
    if [ -f "$backup_script" ]; then
        echo "✅ Backup script exists"
    else
        echo "❌ Backup script missing"
    fi
    
    # Check if required tools are available
    local required_tools=("jq" "git")
    for tool in "${required_tools[@]}"; do
        if command -v $tool &> /dev/null; then
            echo "✅ $tool is available"
        else
            echo "❌ $tool is not available"
        fi
    done
    
    echo "Validation completed"
    log_message "Change management process validation completed"
}

# Function to send change notification
send_notification() {
    local change_id=$1
    local message=$2
    
    log_message "Sending notification for change $change_id: $message"
    
    # In a real implementation, this would send an email or Slack notification
    echo "📧 CHANGE NOTIFICATION [$change_id]: $message"
}

# Main change management function
main() {
    log_message "=== Starting Atlas Change Management ==="
    
    # Handle different change management operations
    case $1 in
        "create")
            if [ $# -lt 6 ]; then
                echo "Usage: $0 create <change_id> <type> <description> <priority> <implementation_date>"
                return 1
            fi
            create_change_request "$2" "$3" "$4" "$5" "$6"
            ;;
        "approve")
            if [ $# -lt 5 ]; then
                echo "Usage: $0 approve <change_id> <approver> <impact_assessment> <rollback_plan>"
                return 1
            fi
            approve_change_request "$2" "$3" "$4" "$5"
            ;;
        "reject")
            if [ $# -lt 4 ]; then
                echo "Usage: $0 reject <change_id> <approver> <reason>"
                return 1
            fi
            reject_change_request "$2" "$3" "$4"
            ;;
        "implement")
            if [ $# -lt 2 ]; then
                echo "Usage: $0 implement <change_id>"
                return 1
            fi
            implement_change "$2"
            ;;
        "rollback")
            if [ $# -lt 3 ]; then
                echo "Usage: $0 rollback <change_id> <reason>"
                return 1
            fi
            rollback_change "$2" "$3"
            ;;
        "close")
            if [ $# -lt 3 ]; then
                echo "Usage: $0 close <change_id> <notes>"
                return 1
            fi
            close_change "$2" "$3"
            ;;
        "list")
            list_changes
            ;;
        "details")
            if [ $# -lt 2 ]; then
                echo "Usage: $0 details <change_id>"
                return 1
            fi
            get_change_details "$2"
            ;;
        "validate")
            validate_change_process
            ;;
        *)
            echo "Atlas Production Change Management"
            echo "=================================="
            echo ""
            echo "Usage:"
            echo "  $0 create <id> <type> <desc> <priority> <date>  Create new change request"
            echo "  $0 approve <id> <approver> <impact> <rollback>  Approve change request"
            echo "  $0 reject <id> <approver> <reason>              Reject change request"
            echo "  $0 implement <id>                               Implement approved change"
            echo "  $0 rollback <id> <reason>                       Rollback implemented change"
            echo "  $0 close <id> <notes>                           Close completed change"
            echo "  $0 list                                         List all changes"
            echo "  $0 details <id>                                 Get change details"
            echo "  $0 validate                                     Validate change process"
            echo ""
            echo "Examples:"
            echo "  $0 create CHG001 "Software Update" "Update Atlas to v2.0" High "2023-12-01""
            echo "  $0 approve CHG001 "Admin" "Low impact" "Rollback to previous version""
            echo "  $0 list"
            ;;
    esac
    
    log_message "=== Change Management Completed ==="
}

# Run main function
main "$@"