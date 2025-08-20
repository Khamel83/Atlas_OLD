#!/bin/bash

# Atlas Production Performance Monitoring Script
# This script continuously monitors performance metrics of the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Performance Monitoring..."

# Configuration
PERF_MONITOR_LOG="/home/ubuntu/dev/atlas/logs/performance_monitor.log"
PERF_METRICS_DIR="/home/ubuntu/dev/atlas/metrics/performance"
PERF_ALERT_THRESHOLD=80  # Percentage threshold for alerts

# Create logs and metrics directories if they don't exist
mkdir -p "$(dirname $PERF_MONITOR_LOG)"
mkdir -p "$PERF_METRICS_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $PERF_MONITOR_LOG
    echo "$1"
}

# Function to collect CPU metrics
collect_cpu_metrics() {
    local cpu_metrics_file="$PERF_METRICS_DIR/cpu_metrics_$(date +%Y%m%d).json"
    
    # Collect CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    
    # Collect CPU load averages
    local load_avg_1min=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | sed 's/,//')
    local load_avg_5min=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $2}' | sed 's/,//')
    local load_avg_15min=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $3}')
    
    # Create JSON metrics file (append to existing file)
    local timestamp=$(date -Iseconds)
    cat >> "$cpu_metrics_file" << EOF
{
    "timestamp": "$timestamp",
    "cpu_usage_percent": $cpu_usage,
    "load_average_1min": $load_avg_1min,
    "load_average_5min": $load_avg_5min,
    "load_average_15min": $load_avg_15min
},
EOF
    
    # Check for high CPU usage
    if (( $(echo "$cpu_usage > $PERF_ALERT_THRESHOLD" | bc -l) )); then
        log_message "ALERT: High CPU usage detected - ${cpu_usage}%"
        echo "⚠️ HIGH CPU USAGE: ${cpu_usage}%"
    fi
    
    log_message "CPU metrics collected: $cpu_usage%"
}

# Function to collect memory metrics
collect_memory_metrics() {
    local memory_metrics_file="$PERF_METRICS_DIR/memory_metrics_$(date +%Y%m%d).json"
    
    # Collect memory usage
    local memory_total=$(free -b | grep Mem | awk '{print $2}')
    local memory_used=$(free -b | grep Mem | awk '{print $3}')
    local memory_usage=$(echo "scale=2; $memory_used * 100 / $memory_total" | bc)
    
    # Get top memory consuming processes
    local top_memory_processes=$(ps aux --sort=-%mem | head -6 | tail -5 | awk '{print $2":"$4":"$11}')
    
    # Create JSON metrics file (append to existing file)
    local timestamp=$(date -Iseconds)
    cat >> "$memory_metrics_file" << EOF
{
    "timestamp": "$timestamp",
    "memory_total_bytes": $memory_total,
    "memory_used_bytes": $memory_used,
    "memory_usage_percent": $memory_usage,
    "top_processes": [
EOF
    
    # Add top processes to JSON
    local first_process=true
    while IFS= read -r line; do
        local pid=$(echo $line | cut -d':' -f1)
        local mem_pct=$(echo $line | cut -d':' -f2)
        local process=$(echo $line | cut -d':' -f3)
        
        if [ "$first_process" = "true" ]; then
            first_process=false
        else
            echo "        ," >> "$memory_metrics_file"
        fi
        
        cat >> "$memory_metrics_file" << EOF
        {
            "pid": "$pid",
            "memory_percent": $mem_pct,
            "process": "$process"
        }
EOF
    done <<< "$top_memory_processes"
    
    cat >> "$memory_metrics_file" << EOF
    ]
},
EOF
    
    # Check for high memory usage
    if (( $(echo "$memory_usage > $PERF_ALERT_THRESHOLD" | bc -l) )); then
        log_message "ALERT: High memory usage detected - ${memory_usage}%"
        echo "⚠️ HIGH MEMORY USAGE: ${memory_usage}%"
    fi
    
    log_message "Memory metrics collected: $memory_usage%"
}

# Function to collect disk metrics
collect_disk_metrics() {
    local disk_metrics_file="$PERF_METRICS_DIR/disk_metrics_$(date +%Y%m%d).json"
    
    # Collect disk usage
    local disk_total=$(df / | tail -1 | awk '{print $2}')
    local disk_used=$(df / | tail -1 | awk '{print $3}')
    local disk_usage=$(echo "scale=2; $disk_used * 100 / $disk_total" | bc)
    
    # Create JSON metrics file (append to existing file)
    local timestamp=$(date -Iseconds)
    cat >> "$disk_metrics_file" << EOF
{
    "timestamp": "$timestamp",
    "disk_total_kb": $disk_total,
    "disk_used_kb": $disk_used,
    "disk_usage_percent": $disk_usage
},
EOF
    
    # Check for high disk usage
    if (( $(echo "$disk_usage > $PERF_ALERT_THRESHOLD" | bc -l) )); then
        log_message "ALERT: High disk usage detected - ${disk_usage}%"
        echo "⚠️ HIGH DISK USAGE: ${disk_usage}%"
    fi
    
    log_message "Disk metrics collected: $disk_usage%"
}

# Function to collect network metrics
collect_network_metrics() {
    local network_metrics_file="$PERF_METRICS_DIR/network_metrics_$(date +%Y%m%d).json"
    
    # Collect network statistics
    local rx_bytes=$(cat /proc/net/dev | grep eth0 | awk '{print $2}')
    local tx_bytes=$(cat /proc/net/dev | grep eth0 | awk '{print $10}')
    
    # Create JSON metrics file (append to existing file)
    local timestamp=$(date -Iseconds)
    cat >> "$network_metrics_file" << EOF
{
    "timestamp": "$timestamp",
    "rx_bytes": $rx_bytes,
    "tx_bytes": $tx_bytes
},
EOF
    
    log_message "Network metrics collected"
}

# Function to collect application metrics
collect_application_metrics() {
    local app_metrics_file="$PERF_METRICS_DIR/application_metrics_$(date +%Y%m%d).json"
    
    # Collect application process information
    local app_processes=$(pgrep -f "atlas" | wc -l)
    local app_memory=$(ps -o pid,vsz,rss,comm -p $(pgrep -f "atlas" | head -1) 2>/dev/null | tail -1 | awk '{print $3}' 2>/dev/null || echo "0")
    
    # Check if application is responding
    local app_responsive="false"
    if curl -f -s http://localhost:5000/health > /dev/null 2>&1; then
        app_responsive="true"
    elif curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        app_responsive="true"
    fi
    
    # Measure response time
    local response_time="null"
    if [ "$app_responsive" = "true" ]; then
        local start_time=$(date +%s%3N)
        curl -f -s http://localhost:5000/ > /dev/null 2>&1
        local end_time=$(date +%s%3N)
        response_time=$((end_time - start_time))
    fi
    
    # Create JSON metrics file (append to existing file)
    local timestamp=$(date -Iseconds)
    cat >> "$app_metrics_file" << EOF
{
    "timestamp": "$timestamp",
    "processes_count": $app_processes,
    "memory_usage_kb": $app_memory,
    "responsive": $app_responsive,
    "response_time_ms": $response_time
},
EOF
    
    log_message "Application metrics collected"
}

# Function to generate performance report
generate_performance_report() {
    log_message "Generating performance report"
    
    local report_file="$PERF_METRICS_DIR/performance_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create report header
    echo "Atlas Production Performance Report" > "$report_file"
    echo "Generated: $(date)" >> "$report_file"
    echo "==================================" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add current system metrics
    echo "Current System Metrics:" >> "$report_file"
    echo "----------------------" >> "$report_file"
    echo "CPU Usage: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)%" >> "$report_file"
    echo "Memory Usage: $(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')%" >> "$report_file"
    echo "Disk Usage: $(df / | tail -1 | awk '{print $5}' | sed 's/%//')%" >> "$report_file"
    echo "Load Average: $(uptime | awk -F'load average:' '{print $2}')" >> "$report_file"
    echo "" >> "$report_file"
    
    # Add top processes
    echo "Top CPU Consuming Processes:" >> "$report_file"
    echo "---------------------------" >> "$report_file"
    ps aux --sort=-%cpu | head -6 | tail -5 >> "$report_file"
    echo "" >> "$report_file"
    
    echo "Top Memory Consuming Processes:" >> "$report_file"
    echo "------------------------------" >> "$report_file"
    ps aux --sort=-%mem | head -6 | tail -5 >> "$report_file"
    echo "" >> "$report_file"
    
    # Add application status
    echo "Application Status:" >> "$report_file"
    echo "------------------" >> "$report_file"
    if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        echo "✅ Application is responsive" >> "$report_file"
    else
        echo "❌ Application is not responsive" >> "$report_file"
    fi
    echo "" >> "$report_file"
    
    echo "✅ Performance report generated: $report_file"
    log_message "Performance report generated: $report_file"
    
    # Display summary
    echo ""
    echo "Performance Summary:"
    echo "  CPU Usage: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)%"
    echo "  Memory Usage: $(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')%"
    echo "  Disk Usage: $(df / | tail -1 | awk '{print $5}' | sed 's/%//')%"
    echo "Report saved to: $report_file"
}

# Function to check for performance alerts
check_performance_alerts() {
    log_message "Checking for performance alerts"
    
    # Check CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    if (( $(echo "$cpu_usage > $PERF_ALERT_THRESHOLD" | bc -l) )); then
        log_message "ALERT: High CPU usage - ${cpu_usage}%"
        echo "🚨 HIGH CPU USAGE ALERT: ${cpu_usage}%"
    fi
    
    # Check memory usage
    local memory_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    if [ $memory_usage -gt $PERF_ALERT_THRESHOLD ]; then
        log_message "ALERT: High memory usage - ${memory_usage}%"
        echo "🚨 HIGH MEMORY USAGE ALERT: ${memory_usage}%"
    fi
    
    # Check disk usage
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    if [ $disk_usage -gt $PERF_ALERT_THRESHOLD ]; then
        log_message "ALERT: High disk usage - ${disk_usage}%"
        echo "🚨 HIGH DISK USAGE ALERT: ${disk_usage}%"
    fi
    
    # Check application responsiveness
    if ! curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
        log_message "ALERT: Application not responsive"
        echo "🚨 APPLICATION NOT RESPONDING"
    fi
}

# Function to run continuous monitoring
run_continuous_monitoring() {
    log_message "Starting continuous performance monitoring"
    
    echo "Starting Continuous Performance Monitoring..."
    echo "=========================================="
    echo "Press Ctrl+C to stop monitoring"
    echo ""
    
    # Run monitoring loop
    while true; do
        echo "=== Performance Check - $(date) ==="
        
        # Collect all metrics
        collect_cpu_metrics
        collect_memory_metrics
        collect_disk_metrics
        collect_network_metrics
        collect_application_metrics
        
        # Check for alerts
        check_performance_alerts
        
        # Wait before next check
        sleep 60
    done
}

# Function to clean old performance metrics
clean_old_metrics() {
    log_message "Cleaning old performance metrics"
    
    echo "Cleaning Old Performance Metrics..."
    echo "================================="
    
    # Remove metrics files older than 7 days
    find "$PERF_METRICS_DIR" -name "*metrics_*.json" -mtime +7 -delete 2>/dev/null || true
    find "$PERF_METRICS_DIR" -name "performance_report_*.txt" -mtime +7 -delete 2>/dev/null || true
    
    echo "✅ Old performance metrics cleaned"
    log_message "Old performance metrics cleaned"
}

# Main performance monitoring function
main() {
    log_message "=== Starting Atlas Performance Monitoring ==="
    
    # Start time
    local start_time=$(date)
    log_message "Performance monitoring started at: $start_time"
    
    # Handle different monitoring operations
    case $1 in
        "cpu")
            collect_cpu_metrics
            ;;
        "memory")
            collect_memory_metrics
            ;;
        "disk")
            collect_disk_metrics
            ;;
        "network")
            collect_network_metrics
            ;;
        "application")
            collect_application_metrics
            ;;
        "report")
            generate_performance_report
            ;;
        "alerts")
            check_performance_alerts
            ;;
        "continuous")
            run_continuous_monitoring
            ;;
        "clean")
            clean_old_metrics
            ;;
        *)
            # Run a single collection cycle
            echo "Collecting Performance Metrics..."
            echo "=============================="
            
            collect_cpu_metrics
            collect_memory_metrics
            collect_disk_metrics
            collect_network_metrics
            collect_application_metrics
            check_performance_alerts
            generate_performance_report
            clean_old_metrics
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Performance monitoring completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Performance Monitoring Completed ==="
    
    echo ""
    echo "✅ Performance monitoring cycle complete!"
    echo "📊 Metrics saved to: $PERF_METRICS_DIR"
}

# Run main function
main "$@"