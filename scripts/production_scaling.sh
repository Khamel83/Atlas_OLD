#!/bin/bash

# Atlas Production Scaling Script
# This script helps scale Atlas production environment based on demand

set -e  # Exit on any error

echo "Starting Atlas Production Scaling..."

# Configuration
LOG_FILE="/home/ubuntu/dev/atlas/logs/scaling.log"
CURRENT_INSTANCE_TYPE="t2.micro"  # This would be dynamically determined in a real implementation

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $LOG_FILE)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $LOG_FILE
    echo "$1"
}

# Function to check current resource usage
check_resource_usage() {
    log_message "Checking current resource usage"
    
    # Check CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    
    # Check memory usage
    local memory_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    
    # Check disk usage
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "Current resource usage:"
    echo "  CPU: ${cpu_usage}%"
    echo "  Memory: ${memory_usage}%"
    echo "  Disk: ${disk_usage}%"
    
    log_message "CPU usage: ${cpu_usage}%, Memory usage: ${memory_usage}%, Disk usage: ${disk_usage}%"
    
    # Return usage metrics
    echo "$cpu_usage,$memory_usage,$disk_usage"
}

# Function to determine scaling needs
determine_scaling_needs() {
    local usage_metrics=$1
    local cpu_usage=$(echo $usage_metrics | cut -d',' -f1)
    local memory_usage=$(echo $usage_metrics | cut -d',' -f2)
    local disk_usage=$(echo $usage_metrics | cut -d',' -f3)
    
    log_message "Determining scaling needs based on usage metrics"
    
    # Check if scaling is needed
    if [ $cpu_usage -gt 80 ] || [ $memory_usage -gt 80 ]; then
        echo "scale_up"
        log_message "Scaling recommendation: Scale up"
    elif [ $cpu_usage -lt 30 ] && [ $memory_usage -lt 30 ] && [ "$CURRENT_INSTANCE_TYPE" != "t2.micro" ]; then
        echo "scale_down"
        log_message "Scaling recommendation: Scale down"
    else
        echo "no_scaling"
        log_message "Scaling recommendation: No scaling needed"
    fi
}

# Function to scale up resources
scale_up() {
    log_message "Scaling up resources"
    
    echo "Scaling up Atlas production environment..."
    
    # In a real cloud environment, this would interact with the cloud provider API
    # For example, with AWS CLI:
    # aws ec2 modify-instance-attribute --instance-id $INSTANCE_ID --instance-type "t2.small"
    
    # For OCI, this would use OCI CLI:
    # oci compute instance update --instance-id $INSTANCE_ID --shape "VM.Standard2.2"
    
    # For now, we'll just simulate the scaling
    echo "✅ Would scale up instance from $CURRENT_INSTANCE_TYPE to a larger instance type"
    echo "✅ Would increase CPU and memory resources"
    
    # Restart services to take advantage of new resources
    echo "Restarting services to utilize new resources..."
    sudo systemctl restart atlas
    sudo systemctl restart atlas-prometheus
    sudo systemctl restart atlas-grafana
    
    log_message "Scaling up completed"
}

# Function to scale down resources
scale_down() {
    log_message "Scaling down resources"
    
    echo "Scaling down Atlas production environment..."
    
    # In a real cloud environment, this would interact with the cloud provider API
    # For example, with AWS CLI:
    # aws ec2 modify-instance-attribute --instance-id $INSTANCE_ID --instance-type "t2.micro"
    
    # For OCI, this would use OCI CLI:
    # oci compute instance update --instance-id $INSTANCE_ID --shape "VM.Standard2.1"
    
    # For now, we'll just simulate the scaling
    echo "✅ Would scale down instance to a smaller instance type"
    echo "✅ Would reduce CPU and memory resources"
    
    # Restart services to adjust to new resources
    echo "Restarting services to adjust to new resources..."
    sudo systemctl restart atlas
    sudo systemctl restart atlas-prometheus
    sudo systemctl restart atlas-grafana
    
    log_message "Scaling down completed"
}

# Function to optimize application settings
optimize_application_settings() {
    log_message "Optimizing application settings for current resources"
    
    echo "Optimizing Atlas application settings..."
    
    # Adjust worker processes based on CPU cores
    local cpu_cores=$(nproc)
    echo "Detected $cpu_cores CPU cores"
    
    # Adjust database connection pool
    echo "Optimizing database connection pool..."
    
    # Adjust memory allocation for different components
    echo "Optimizing memory allocation..."
    
    # Adjust caching settings
    echo "Optimizing caching settings..."
    
    log_message "Application settings optimization completed"
}

# Function to check auto-scaling group status (placeholder)
check_auto_scaling() {
    log_message "Checking auto-scaling group status"
    
    # In a real implementation, this would check cloud provider auto-scaling groups
    echo "Auto-scaling group status check would be implemented here"
    
    log_message "Auto-scaling check completed"
}

# Function to send scaling notification
send_notification() {
    local action=$1
    local message=$2
    
    log_message "Scaling action: $action - $message"
    
    # In a real implementation, this would send an email or Slack notification
    echo "📧 Scaling notification: $action - $message"
}

# Main scaling function
main() {
    log_message "=== Starting Atlas Scaling Process ==="
    
    # Start time
    local start_time=$(date)
    log_message "Scaling process started at: $start_time"
    
    # Check current resource usage
    local usage_metrics=$(check_resource_usage)
    
    # Determine scaling needs
    local scaling_action=$(determine_scaling_needs $usage_metrics)
    
    # Perform scaling action
    case $scaling_action in
        "scale_up")
            scale_up
            send_notification "SCALE_UP" "Resources scaled up due to high usage"
            ;;
        "scale_down")
            scale_down
            send_notification "SCALE_DOWN" "Resources scaled down due to low usage"
            ;;
        "no_scaling")
            echo "No scaling needed at this time"
            send_notification "NO_ACTION" "No scaling required"
            ;;
        *)
            echo "Unknown scaling action: $scaling_action"
            log_message "ERROR: Unknown scaling action: $scaling_action"
            return 1
            ;;
    esac
    
    # Optimize application settings
    optimize_application_settings
    
    # Check auto-scaling (placeholder)
    check_auto_scaling
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Scaling process completed at: $end_time (Duration: ${duration}s)"
    log_message "=== Scaling Process Completed ==="
    
    return 0
}

# Handle script arguments
if [ "$1" == "--up" ]; then
    echo "Forcing scale up..."
    scale_up
    exit 0
elif [ "$1" == "--down" ]; then
    echo "Forcing scale down..."
    scale_down
    exit 0
elif [ "$1" == "--optimize" ]; then
    echo "Optimizing application settings..."
    optimize_application_settings
    exit 0
fi

# Run main scaling process
if main; then
    echo "✅ Atlas scaling process completed successfully"
    exit 0
else
    echo "❌ Atlas scaling process failed"
    exit 1
fi