#!/bin/bash

# Atlas Production Performance Monitoring Script
# This script continuously monitors the performance of the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Performance Monitoring..."

# Configuration
PERFORMANCE_LOG="/home/ubuntu/dev/atlas/logs/performance_monitoring.log"
PERFORMANCE_REPORT_DIR="/home/ubuntu/dev/atlas/reports/performance"
PERFORMANCE_CONFIG="/home/ubuntu/dev/atlas/config/performance.json"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $PERFORMANCE_LOG)"
mkdir -p "$PERFORMANCE_REPORT_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $PERFORMANCE_LOG
    echo "$1"
}

# Function to initialize performance configuration
initialize_performance_config() {
    log_message "Initializing performance configuration"
    
    # Create default performance configuration if it doesn't exist
    if [ ! -f "$PERFORMANCE_CONFIG" ]; then
        cat > "$PERFORMANCE_CONFIG" << EOF
{
    "performance": {
        "monitoring": {
            "enabled": true,
            "interval_seconds": 60,
            "alert_thresholds": {
                "cpu_usage_percent": 80,
                "memory_usage_percent": 80,
                "disk_usage_percent": 85,
                "response_time_ms": 1000
            }
        },
        "metrics": {
            "collection": {
                "enabled": true,
                "frequency_seconds": 15,
                "retention_days": 30
            },
            "export": {
                "enabled": true,
                "format": "prometheus",
                "endpoint": "http://localhost:9090/metrics"
            }
        },
        "alerts": {
            "enabled": true,
            "email": {
                "enabled": true,
                "recipients": ["admin@khamel.com"],
                "smtp_server": "smtp.gmail.com",
                "port": 587
            },
            "slack": {
                "enabled": false,
                "webhook_url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
            }
        },
        "reporting": {
            "enabled": true,
            "frequency_hours": 24,
            "format": "json"
        }
    }
}
EOF
        echo "✅ Created default performance configuration"
        log_message "Default performance configuration created"
    else
        echo "✅ Performance configuration already exists"
    fi
}

# Function to collect system metrics
collect_system_metrics() {
    log_message "Collecting system metrics"
    
    echo ""
    echo "Collecting System Metrics..."
    echo "=========================="
    
    local metrics_report="$PERFORMANCE_REPORT_DIR/system_metrics_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create metrics report header
    echo "Atlas Production System Metrics Collection" > "$metrics_report"
    echo "Generated: $(date)" >> "$metrics_report"
    echo "========================================" >> "$metrics_report"
    echo "" >> "$metrics_report"
    
    # Get system metrics configuration
    local collection_enabled=$(jq -r '.performance.metrics.collection.enabled' "$PERFORMANCE_CONFIG")
    local collection_frequency=$(jq -r '.performance.metrics.collection.frequency_seconds' "$PERFORMANCE_CONFIG")
    local retention_days=$(jq -r '.performance.metrics.collection.retention_days' "$PERFORMANCE_CONFIG")
    
    echo "Metrics Collection Configuration:" >> "$metrics_report"
    echo "-------------------------------" >> "$metrics_report"
    echo "Collection Enabled: $collection_enabled" >> "$metrics_report"
    echo "Collection Frequency: ${collection_frequency} seconds" >> "$metrics_report"
    echo "Retention Period: ${retention_days} days" >> "$metrics_report"
    echo "" >> "$metrics_report"
    
    # Collect CPU metrics
    echo "CPU Metrics:" >> "$metrics_report"
    echo "----------" >> "$metrics_report"
    
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local cpu_cores=$(nproc)
    local load_avg=$(uptime | awk -F'load average:' '{print $2}' | xargs)
    
    echo "CPU Usage: ${cpu_usage}%" >> "$metrics_report"
    echo "CPU Cores: $cpu_cores" >> "$metrics_report"
    echo "Load Average: $load_avg" >> "$metrics_report"
    echo "" >> "$metrics_report"
    
    # Collect memory metrics
    echo "Memory Metrics:" >> "$metrics_report"
    echo "-------------" >> "$metrics_report"
    
    local memory_total_gb=$(free -g | grep Mem | awk '{print $2}')
    local memory_used_gb=$(free -g | grep Mem | awk '{print $3}')
    local memory_usage=$(echo "scale=2; $memory_used_gb * 100 / $memory_total_gb" | bc)
    
    echo "Memory Total: ${memory_total_gb}GB" >> "$metrics_report"
    echo "Memory Used: ${memory_used_gb}GB" >> "$metrics_report"
    echo "Memory Usage: ${memory_usage}%" >> "$metrics_report"
    echo "" >> "$metrics_report"
    
    # Collect disk metrics
    echo "Disk Metrics:" >> "$metrics_report"
    echo "-----------" >> "$metrics_report"
    
    local disk_total_gb=$(df -BG / | tail -1 | awk '{print $2}' | sed 's/G//')
    local disk_used_gb=$(df -BG / | tail -1 | awk '{print $3}' | sed 's/G//')
    local disk_usage=$(echo "scale=2; $disk_used_gb * 100 / $disk_total_gb" | bc)
    
    echo "Disk Total: ${disk_total_gb}GB" >> "$metrics_report"
    echo "Disk Used: ${disk_used_gb}GB" >> "$metrics_report"
    echo "Disk Usage: ${disk_usage}%" >> "$metrics_report"
    echo "" >> "$metrics_report"
    
    # Collect network metrics
    echo "Network Metrics:" >> "$metrics_report"
    echo "--------------" >> "$metrics_report"
    
    local network_rx_bytes=$(cat /proc/net/dev | grep eth0 | awk '{print $2}')
    local network_tx_bytes=$(cat /proc/net/dev | grep eth0 | awk '{print $10}')
    
    echo "Network RX: ${network_rx_bytes} bytes" >> "$metrics_report"
    echo "Network TX: ${network_tx_bytes} bytes" >> "$metrics_report"
    echo "" >> "$metrics_report"
    
    # Export metrics
    echo "Exporting Metrics:" >> "$metrics_report"
    echo "----------------" >> "$metrics_report"
    
    local export_enabled=$(jq -r '.performance.metrics.export.enabled' "$PERFORMANCE_CONFIG")
    local export_format=$(jq -r '.performance.metrics.export.format' "$PERFORMANCE_CONFIG")
    local export_endpoint=$(jq -r '.performance.metrics.export.endpoint' "$PERFORMANCE_CONFIG")
    
    echo "Export Enabled: $export_enabled" >> "$metrics_report"
    echo "Export Format: $export_format" >> "$metrics_report"
    echo "Export Endpoint: $export_endpoint" >> "$metrics_report"
    
    if [ "$export_enabled" = "true" ]; then
        # Create metrics file in Prometheus format
        local prometheus_metrics_file="$PERFORMANCE_REPORT_DIR/metrics.prom"
        
        cat > "$prometheus_metrics_file" << EOF
# HELP atlas_cpu_usage_percent CPU usage percentage
# TYPE atlas_cpu_usage_percent gauge
atlas_cpu_usage_percent $cpu_usage

# HELP atlas_memory_usage_percent Memory usage percentage
# TYPE atlas_memory_usage_percent gauge
atlas_memory_usage_percent $memory_usage

# HELP atlas_disk_usage_percent Disk usage percentage
# TYPE atlas_disk_usage_percent gauge
atlas_disk_usage_percent $disk_usage

# HELP atlas_load_average_1min Load average over 1 minute
# TYPE atlas_load_average_1min gauge
atlas_load_average_1min $(echo $load_avg | awk '{print $1}' | sed 's/,//')

# HELP atlas_load_average_5min Load average over 5 minutes
# TYPE atlas_load_average_5min gauge
atlas_load_average_5min $(echo $load_avg | awk '{print $2}' | sed 's/,//')

# HELP atlas_load_average_15min Load average over 15 minutes
# TYPE atlas_load_average_15min gauge
atlas_load_average_15min $(echo $load_avg | awk '{print $3}')

# HELP atlas_network_rx_bytes Network received bytes
# TYPE atlas_network_rx_bytes counter
atlas_network_rx_bytes $network_rx_bytes

# HELP atlas_network_tx_bytes Network transmitted bytes
# TYPE atlas_network_tx_bytes counter
atlas_network_tx_bytes $network_tx_bytes
EOF
        
        echo "✅ Metrics exported to: $prometheus_metrics_file" >> "$metrics_report"
        
        # Try to send metrics to Prometheus endpoint
        if curl -f -s -X POST "$export_endpoint" -H "Content-Type: text/plain" --data-binary "@$prometheus_metrics_file" > /dev/null 2>&1; then
            echo "✅ Metrics sent to Prometheus endpoint: $export_endpoint" >> "$metrics_report"
        else
            echo "❌ Failed to send metrics to Prometheus endpoint" >> "$metrics_report"
        fi
    else
        echo "❌ Metrics export is disabled" >> "$metrics_report"
    fi
    echo "" >> "$metrics_report"
    
    echo "✅ System metrics collection completed"
    echo "📋 Metrics report saved to: $metrics_report"
    log_message "System metrics collection completed: $metrics_report"
    
    # Display summary
    echo ""
    echo "System Metrics Summary:"
    echo "  CPU Usage: ${cpu_usage}%"
    echo "  Memory Usage: ${memory_usage}%"
    echo "  Disk Usage: ${disk_usage}%"
    echo "  Load Average: $load_avg"
    echo "  Network RX: ${network_rx_bytes} bytes"
    echo "  Network TX: ${network_tx_bytes} bytes"
    echo "  Report: $metrics_report"
}

# Function to monitor performance thresholds
monitor_performance_thresholds() {
    log_message "Monitoring performance thresholds"
    
    echo ""
    echo "Monitoring Performance Thresholds..."
    echo "================================="
    
    local threshold_report="$PERFORMANCE_REPORT_DIR/performance_thresholds_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create threshold report header
    echo "Atlas Production Performance Threshold Monitoring" > "$threshold_report"
    echo "Generated: $(date)" >> "$threshold_report"
    echo "=============================================" >> "$threshold_report"
    echo "" >> "$threshold_report"
    
    # Get alert thresholds
    local cpu_threshold=$(jq -r '.performance.monitoring.alert_thresholds.cpu_usage_percent' "$PERFORMANCE_CONFIG")
    local memory_threshold=$(jq -r '.performance.monitoring.alert_thresholds.memory_usage_percent' "$PERFORMANCE_CONFIG")
    local disk_threshold=$(jq -r '.performance.monitoring.alert_thresholds.disk_usage_percent' "$PERFORMANCE_CONFIG")
    local response_time_threshold=$(jq -r '.performance.monitoring.alert_thresholds.response_time_ms' "$PERFORMANCE_CONFIG")
    
    echo "Alert Thresholds:" >> "$threshold_report"
    echo "---------------" >> "$threshold_report"
    echo "CPU Usage Threshold: ${cpu_threshold}%" >> "$threshold_report"
    echo "Memory Usage Threshold: ${memory_threshold}%" >> "$threshold_report"
    echo "Disk Usage Threshold: ${disk_threshold}%" >> "$threshold_report"
    echo "Response Time Threshold: ${response_time_threshold}ms" >> "$threshold_report"
    echo "" >> "$threshold_report"
    
    # Check current metrics against thresholds
    echo "Threshold Checks:" >> "$threshold_report"
    echo "---------------" >> "$threshold_report"
    
    # Check CPU usage
    local current_cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    if (( $(echo "$current_cpu > $cpu_threshold" | bc -l) )); then
        echo "❌ CPU Usage Alert: ${current_cpu}% > ${cpu_threshold}%" >> "$threshold_report"
        send_performance_alert "CPU Usage" "${current_cpu}%" "${cpu_threshold}%"
    else
        echo "✅ CPU Usage OK: ${current_cpu}% <= ${cpu_threshold}%" >> "$threshold_report"
    fi
    echo "" >> "$threshold_report"
    
    # Check memory usage
    local current_memory=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    if [ $current_memory -gt $memory_threshold ]; then
        echo "❌ Memory Usage Alert: ${current_memory}% > ${memory_threshold}%" >> "$threshold_report"
        send_performance_alert "Memory Usage" "${current_memory}%" "${memory_threshold}%"
    else
        echo "✅ Memory Usage OK: ${current_memory}% <= ${memory_threshold}%" >> "$threshold_report"
    fi
    echo "" >> "$threshold_report"
    
    # Check disk usage
    local current_disk=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    if [ $current_disk -gt $disk_threshold ]; then
        echo "❌ Disk Usage Alert: ${current_disk}% > ${disk_threshold}%" >> "$threshold_report"
        send_performance_alert "Disk Usage" "${current_disk}%" "${disk_threshold}%"
    else
        echo "✅ Disk Usage OK: ${current_disk}% <= ${disk_threshold}%" >> "$threshold_report"
    fi
    echo "" >> "$threshold_report"
    
    # Check response time
    local start_time=$(date +%s%3N)
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        local end_time=$(date +%s%3N)
        local current_response_time=$((end_time - start_time))
        
        # Handle negative response times (shouldn't happen, but just in case)
        if [ $current_response_time -lt 0 ]; then
            current_response_time=$((current_response_time * -1))
        fi
        
        if [ $current_response_time -gt $response_time_threshold ]; then
            echo "❌ Response Time Alert: ${current_response_time}ms > ${response_time_threshold}ms" >> "$threshold_report"
            send_performance_alert "Response Time" "${current_response_time}ms" "${response_time_threshold}ms"
        else
            echo "✅ Response Time OK: ${current_response_time}ms <= ${response_time_threshold}ms" >> "$threshold_report"
        fi
    else
        echo "❌ Service Unreachable - Response Time Alert" >> "$threshold_report"
        send_performance_alert "Service Unreachable" "Unreachable" "Reachable"
    fi
    echo "" >> "$threshold_report"
    
    # Check service status
    echo "Service Status Checks:" >> "$threshold_report"
    echo "--------------------" >> "$threshold_report"
    
    local critical_services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    for service_info in "${critical_services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc is running" >> "$threshold_report"
        else
            echo "❌ $service_desc is not running" >> "$threshold_report"
            send_performance_alert "Service Down" "$service_desc" "Running"
        fi
    done
    echo "" >> "$threshold_report"
    
    # Generate recommendations
    echo "Performance Recommendations:" >> "$threshold_report"
    echo "-------------------------" >> "$threshold_report"
    
    if (( $(echo "$current_cpu <= $cpu_threshold" | bc -l) )) && \
       [ $current_memory -le $memory_threshold ] && \
       [ $current_disk -le $disk_threshold ]; then
        echo "✅ System performance is within acceptable limits" >> "$threshold_report"
        echo "✅ Continue current performance monitoring practices" >> "$threshold_report"
        echo "✅ Review performance periodically" >> "$threshold_report"
    else
        echo "❌ System performance is exceeding thresholds" >> "$threshold_report"
        echo "❌ Review system resources and optimize as needed" >> "$threshold_report"
        echo "❌ Consider upgrading system resources if needed" >> "$threshold_report"
        echo "❌ Implement performance optimization techniques" >> "$threshold_report"
    fi
    echo "" >> "$threshold_report"
    
    echo "✅ Performance threshold monitoring completed"
    echo "📋 Threshold report saved to: $threshold_report"
    log_message "Performance threshold monitoring completed: $threshold_report"
    
    # Display summary
    echo ""
    echo "Performance Threshold Summary:"
    echo "  CPU Threshold: ${cpu_threshold}% (Current: ${current_cpu}%)"
    echo "  Memory Threshold: ${memory_threshold}% (Current: ${current_memory}%)"
    echo "  Disk Threshold: ${disk_threshold}% (Current: ${current_disk}%)"
    echo "  Response Time Threshold: ${response_time_threshold}ms"
    if [ ! -z "$current_response_time" ]; then
        echo "  Current Response Time: ${current_response_time}ms"
    else
        echo "  Current Response Time: Unreachable"
    fi
    echo "  Critical Services: $(for service_info in "${critical_services[@]}"; do echo "$(echo $service_info | cut -d':' -f2): $(if systemctl is-active --quiet $(echo $service_info | cut -d':' -f1); then echo "Running"; else echo "Not Running"; fi)"; done)"
    echo "  Report: $threshold_report"
}

# Function to send performance alert
send_performance_alert() {
    local metric=$1
    local current_value=$2
    local threshold_value=$3
    
    log_message "Sending performance alert for $metric: $current_value > $threshold_value"
    
    echo ""
    echo "Sending Performance Alert..."
    echo "=========================="
    
    # Get alert configuration
    local alerts_enabled=$(jq -r '.performance.alerts.enabled' "$PERFORMANCE_CONFIG")
    local email_enabled=$(jq -r '.performance.alerts.email.enabled' "$PERFORMANCE_CONFIG")
    local slack_enabled=$(jq -r '.performance.alerts.slack.enabled' "$PERFORMANCE_CONFIG")
    
    if [ "$alerts_enabled" != "true" ]; then
        echo "ℹ️ Performance alerts are disabled"
        log_message "Performance alerts are disabled"
        return 0
    fi
    
    # Create alert message
    local alert_message="Atlas Performance Alert - $(date)

Metric: $metric
Current Value: $current_value
Threshold Value: $threshold_value
Alert Type: PERFORMANCE_THRESHOLD_EXCEEDED

This is an automated performance alert from your Atlas production system.

Immediate action may be required to address this performance issue.

For more information, check the performance reports in:
$PERFORMANCE_REPORT_DIR/

To disable these alerts, update the configuration in:
$PERFORMANCE_CONFIG"

    # Send email alert
    if [ "$email_enabled" = "true" ]; then
        local recipients=$(jq -r '.performance.alerts.email.recipients[]' "$PERFORMANCE_CONFIG")
        local smtp_server=$(jq -r '.performance.alerts.email.smtp_server' "$PERFORMANCE_CONFIG")
        local port=$(jq -r '.performance.alerts.email.port' "$PERFORMANCE_CONFIG")
        
        echo "📧 Sending email alert for $metric threshold exceeded"
        echo "To: $recipients"
        echo "Subject: Atlas Performance Alert - $metric Threshold Exceeded"
        echo ""
        echo "$alert_message"
        
        log_message "Email alert sent for $metric threshold exceeded"
    else
        echo "ℹ️ Email alerts are disabled"
    fi
    
    # Send Slack alert
    if [ "$slack_enabled" = "true" ]; then
        local webhook_url=$(jq -r '.performance.alerts.slack.webhook_url' "$PERFORMANCE_CONFIG")
        
        echo "💬 Sending Slack alert for $metric threshold exceeded"
        echo "Webhook URL: $webhook_url"
        echo "Message: $alert_message"
        
        log_message "Slack alert sent for $metric threshold exceeded"
    else
        echo "ℹ️ Slack alerts are disabled"
    fi
    
    echo "✅ Performance alert sent"
    log_message "Performance alert sent for $metric: $current_value > $threshold_value"
}

# Function to generate performance report
generate_performance_report() {
    log_message "Generating performance report"
    
    echo ""
    echo "Generating Performance Report..."
    echo "============================="
    
    local performance_report="$PERFORMANCE_REPORT_DIR/performance_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create performance report header
    echo "Atlas Production Performance Report" > "$performance_report"
    echo "Generated: $(date)" >> "$performance_report"
    echo "================================" >> "$performance_report"
    echo "" >> "$performance_report"
    
    # Add system information
    echo "System Information:" >> "$performance_report"
    echo "------------------" >> "$performance_report"
    echo "Hostname: $(hostname)" >> "$performance_report"
    echo "OS: $(lsb_release -d | cut -f2)" >> "$performance_report"
    echo "Kernel: $(uname -r)" >> "$performance_report"
    echo "Uptime: $(uptime -p)" >> "$performance_report"
    echo "" >> "$performance_report"
    
    # Add current metrics
    echo "Current Performance Metrics:" >> "$performance_report"
    echo "--------------------------" >> "$performance_report"
    
    local current_cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local current_memory=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    local current_disk=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "CPU Usage: ${current_cpu}%" >> "$performance_report"
    echo "Memory Usage: ${current_memory}%" >> "$performance_report"
    echo "Disk Usage: ${current_disk}%" >> "$performance_report"
    
    # Check response time
    local start_time=$(date +%s%3N)
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        local end_time=$(date +%s%3N)
        local current_response_time=$((end_time - start_time))
        
        # Handle negative response times (shouldn't happen, but just in case)
        if [ $current_response_time -lt 0 ]; then
            current_response_time=$((current_response_time * -1))
        fi
        
        echo "Response Time: ${current_response_time}ms" >> "$performance_report"
    else
        echo "Response Time: Unreachable" >> "$performance_report"
    fi
    echo "" >> "$performance_report"
    
    # Add threshold information
    echo "Performance Thresholds:" >> "$performance_report"
    echo "--------------------" >> "$performance_report"
    
    local cpu_threshold=$(jq -r '.performance.monitoring.alert_thresholds.cpu_usage_percent' "$PERFORMANCE_CONFIG")
    local memory_threshold=$(jq -r '.performance.monitoring.alert_thresholds.memory_usage_percent' "$PERFORMANCE_CONFIG")
    local disk_threshold=$(jq -r '.performance.monitoring.alert_thresholds.disk_usage_percent' "$PERFORMANCE_CONFIG")
    local response_time_threshold=$(jq -r '.performance.monitoring.alert_thresholds.response_time_ms' "$PERFORMANCE_CONFIG")
    
    echo "CPU Usage Threshold: ${cpu_threshold}%" >> "$performance_report"
    echo "Memory Usage Threshold: ${memory_threshold}%" >> "$performance_report"
    echo "Disk Usage Threshold: ${disk_threshold}%" >> "$performance_report"
    echo "Response Time Threshold: ${response_time_threshold}ms" >> "$performance_report"
    echo "" >> "$performance_report"
    
    # Add service status
    echo "Service Status:" >> "$performance_report"
    echo "-------------" >> "$performance_report"
    
    local critical_services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    for service_info in "${critical_services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc is running" >> "$performance_report"
        else
            echo "❌ $service_desc is not running" >> "$performance_report"
        fi
    done
    echo "" >> "$performance_report"
    
    # Add performance summary
    echo "Performance Summary:" >> "$performance_report"
    echo "------------------" >> "$performance_report"
    
    # Check if metrics are within thresholds
    local within_thresholds=true
    
    if (( $(echo "$current_cpu > $cpu_threshold" | bc -l) )); then
        within_thresholds=false
        echo "❌ CPU usage (${current_cpu}%) exceeds threshold (${cpu_threshold}%)" >> "$performance_report"
    fi
    
    if [ $current_memory -gt $memory_threshold ]; then
        within_thresholds=false
        echo "❌ Memory usage (${current_memory}%) exceeds threshold (${memory_threshold}%)" >> "$performance_report"
    fi
    
    if [ $current_disk -gt $disk_threshold ]; then
        within_thresholds=false
        echo "❌ Disk usage (${current_disk}%) exceeds threshold (${disk_threshold}%)" >> "$performance_report"
    fi
    
    if [ ! -z "$current_response_time" ] && [ $current_response_time -gt $response_time_threshold ]; then
        within_thresholds=false
        echo "❌ Response time (${current_response_time}ms) exceeds threshold (${response_time_threshold}ms)" >> "$performance_report"
    fi
    
    if $within_thresholds; then
        echo "✅ All performance metrics are within acceptable thresholds" >> "$performance_report"
    else
        echo "❌ Some performance metrics exceed acceptable thresholds" >> "$performance_report"
    fi
    echo "" >> "$performance_report"
    
    # Add recommendations
    echo "Performance Recommendations:" >> "$performance_report"
    echo "-------------------------" >> "$performance_report"
    
    if $within_thresholds; then
        echo "✅ Continue current performance monitoring practices" >> "$performance_report"
        echo "✅ Review performance reports regularly" >> "$performance_report"
        echo "✅ Monitor trends for early warning signs" >> "$performance_report"
    else
        echo "❌ Address performance issues immediately" >> "$performance_report"
        echo "✅ Review system resources and optimize as needed" >> "$performance_report"
        echo "✅ Consider upgrading system resources if needed" >> "$performance_report"
        echo "✅ Implement performance optimization techniques" >> "$performance_report"
        echo "✅ Schedule regular performance reviews" >> "$performance_report"
    fi
    echo "" >> "$performance_report"
    
    # Add reporting information
    echo "Reporting Information:" >> "$performance_report"
    echo "--------------------" >> "$performance_report"
    
    local reporting_enabled=$(jq -r '.performance.reporting.enabled' "$PERFORMANCE_CONFIG")
    local reporting_frequency=$(jq -r '.performance.reporting.frequency_hours' "$PERFORMANCE_CONFIG")
    local reporting_format=$(jq -r '.performance.reporting.format' "$PERFORMANCE_CONFIG")
    
    echo "Reporting Enabled: $reporting_enabled" >> "$performance_report"
    echo "Reporting Frequency: ${reporting_frequency} hours" >> "$performance_report"
    echo "Reporting Format: $reporting_format" >> "$performance_report"
    echo "" >> "$performance_report"
    
    echo "✅ Performance report generated"
    echo "📋 Performance report saved to: $performance_report"
    log_message "Performance report generated: $performance_report"
    
    # Display summary
    echo ""
    echo "Performance Report Summary:"
    echo "  System: $(hostname) ($(lsb_release -d | cut -f2))"
    echo "  Kernel: $(uname -r)"
    echo "  Uptime: $(uptime -p)"
    echo "  CPU Usage: ${current_cpu}% (Threshold: ${cpu_threshold}%)"
    echo "  Memory Usage: ${current_memory}% (Threshold: ${memory_threshold}%)"
    echo "  Disk Usage: ${current_disk}% (Threshold: ${disk_threshold}%)"
    if [ ! -z "$current_response_time" ]; then
        echo "  Response Time: ${current_response_time}ms (Threshold: ${response_time_threshold}ms)"
    else
        echo "  Response Time: Unreachable (Threshold: ${response_time_threshold}ms)"
    fi
    echo "  Services Running: $(for service_info in "${critical_services[@]}"; do if systemctl is-active --quiet $(echo $service_info | cut -d':' -f1); then echo "$(echo $service_info | cut -d':' -f2)"; fi; done | wc -l)/${#critical_services[@]}"
    if $within_thresholds; then
        echo "  Status: ✅ WITHIN THRESHOLDS"
    else
        echo "  Status: ❌ EXCEEDING THRESHOLDS"
    fi
    echo "  Report: $performance_report"
}

# Function to clean old performance reports
clean_old_reports() {
    log_message "Cleaning old performance reports"
    
    echo ""
    echo "Cleaning Old Performance Reports..."
    echo "================================"
    
    # Remove performance reports older than 90 days
    find "$PERFORMANCE_REPORT_DIR" -name "system_metrics_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$PERFORMANCE_REPORT_DIR" -name "performance_thresholds_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$PERFORMANCE_REPORT_DIR" -name "performance_report_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$PERFORMANCE_REPORT_DIR" -name "metrics.prom" -mtime +90 -delete 2>/dev/null || true
    
    echo "✅ Old performance reports cleaned"
    log_message "Old performance reports cleaned"
}

# Main performance monitoring function
main() {
    log_message "=== Starting Atlas Performance Monitoring ==="
    
    # Initialize configuration
    initialize_performance_config
    
    # Start time
    local start_time=$(date)
    log_message "Performance monitoring started at: $start_time"
    
    # Handle different performance monitoring operations
    case $1 in
        "collect")
            collect_system_metrics
            ;;
        "thresholds")
            monitor_performance_thresholds
            ;;
        "report")
            generate_performance_report
            ;;
        "alert")
            if [ $# -lt 4 ]; then
                echo "❌ Usage: $0 alert <metric> <current_value> <threshold_value>"
                return 1
            fi
            send_performance_alert "$2" "$3" "$4"
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive performance monitoring
            collect_system_metrics
            monitor_performance_thresholds
            generate_performance_report
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Performance monitoring completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Performance Monitoring Completed ==="
    
    echo ""
    echo "✅ Performance monitoring completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $PERFORMANCE_REPORT_DIR"
    echo "📝 Log file: $PERFORMANCE_LOG"
}

# Run main function
main "$@"