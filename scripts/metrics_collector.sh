#!/bin/bash

# Atlas Production Metrics Collector
# This script collects and aggregates metrics from the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Metrics Collection..."

# Configuration
METRICS_DIR="/home/ubuntu/dev/atlas/metrics"
METRICS_LOG="/home/ubuntu/dev/atlas/logs/metrics_collection.log"
PROMETHEUS_ENDPOINT="http://localhost:9090"

# Create metrics directory if it doesn't exist
mkdir -p "$METRICS_DIR"
mkdir -p "$(dirname $METRICS_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $METRICS_LOG
    echo "$1"
}

# Function to collect system metrics
collect_system_metrics() {
    log_message "Collecting system metrics"
    
    echo "Collecting System Metrics..."
    echo "=========================="
    
    local metrics_file="$METRICS_DIR/system_metrics_$(date +%Y%m%d_%H%M%S).json"
    
    # Collect CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    
    # Collect memory usage
    local memory_total=$(free -b | grep Mem | awk '{print $2}')
    local memory_used=$(free -b | grep Mem | awk '{print $3}')
    local memory_usage=$(echo "scale=2; $memory_used * 100 / $memory_total" | bc)
    
    # Collect disk usage
    local disk_total=$(df / | tail -1 | awk '{print $2}')
    local disk_used=$(df / | tail -1 | awk '{print $3}')
    local disk_usage=$(echo "scale=2; $disk_used * 100 / $disk_total" | bc)
    
    # Collect system load
    local load_avg=$(uptime | awk -F'load average:' '{print $2}' | xargs)
    
    # Create JSON metrics file
    cat > "$metrics_file" << EOF
{
    "timestamp": "$(date -Iseconds)",
    "system": {
        "cpu_usage_percent": $cpu_usage,
        "memory": {
            "total_bytes": $memory_total,
            "used_bytes": $memory_used,
            "usage_percent": $memory_usage
        },
        "disk": {
            "total_kb": $disk_total,
            "used_kb": $disk_used,
            "usage_percent": $disk_usage
        },
        "load_average": "$load_avg"
    }
}
EOF
    
    echo "CPU Usage: ${cpu_usage}%"
    echo "Memory Usage: ${memory_usage}%"
    echo "Disk Usage: ${disk_usage}%"
    echo "Load Average: $load_avg"
    echo "Metrics saved to: $metrics_file"
    
    log_message "System metrics collected: $metrics_file"
}

# Function to collect application metrics
collect_application_metrics() {
    log_message "Collecting application metrics"
    
    echo ""
    echo "Collecting Application Metrics..."
    echo "==============================="
    
    local metrics_file="$METRICS_DIR/application_metrics_$(date +%Y%m%d_%H%M%S).json"
    
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
    
    # Collect database metrics
    local db_responsive="false"
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        db_responsive="true"
        
        # Count database records (simplified)
        local db_article_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM articles;" 2>/dev/null || echo "0")
        local db_podcast_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM podcasts;" 2>/dev/null || echo "0")
        local db_youtube_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM youtube_videos;" 2>/dev/null || echo "0")
    fi
    
    # Create JSON metrics file
    cat > "$metrics_file" << EOF
{
    "timestamp": "$(date -Iseconds)",
    "application": {
        "processes_count": $app_processes,
        "memory_usage_kb": $app_memory,
        "responsive": $app_responsive
    },
    "database": {
        "responsive": $db_responsive,
        "articles_count": $db_article_count,
        "podcasts_count": $db_podcast_count,
        "youtube_videos_count": $db_youtube_count
    }
}
EOF
    
    echo "Application Processes: $app_processes"
    echo "Application Memory Usage: ${app_memory}KB"
    echo "Application Responsive: $app_responsive"
    echo "Database Responsive: $db_responsive"
    if [ "$db_responsive" = "true" ]; then
        echo "Articles in Database: $db_article_count"
        echo "Podcasts in Database: $db_podcast_count"
        echo "YouTube Videos in Database: $db_youtube_count"
    fi
    echo "Metrics saved to: $metrics_file"
    
    log_message "Application metrics collected: $metrics_file"
}

# Function to collect service metrics
collect_service_metrics() {
    log_message "Collecting service metrics"
    
    echo ""
    echo "Collecting Service Metrics..."
    echo "==========================="
    
    local metrics_file="$METRICS_DIR/service_metrics_$(date +%Y%m%d_%H%M%S).json"
    
    # Define services to check
    local services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    # Create JSON structure
    echo "{" > "$metrics_file"
    echo "    \"timestamp\": \"$(date -Iseconds)\"," >> "$metrics_file"
    echo "    \"services\": {" >> "$metrics_file"
    
    local first_service=true
    for service_info in "${services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        # Check if service is active
        local service_active="false"
        local service_uptime="0"
        
        if systemctl is-active --quiet $service_name; then
            service_active="true"
            # Get service uptime (simplified)
            service_uptime=$(($(date +%s) - $(date -d "$service_uptime" +%s)))
        fi
        
        # Add to JSON
        if [ "$first_service" = "true" ]; then
            first_service=false
        else
            echo "        ," >> "$metrics_file"
        fi
        
        cat >> "$metrics_file" << EOF
        "$service_name": {
            "description": "$service_desc",
            "active": $service_active,
            "uptime_seconds": $service_uptime
        }
EOF
    done
    
    echo "    }" >> "$metrics_file"
    echo "}" >> "$metrics_file"
    
    # Display service status
    for service_info in "${services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc: Running"
        else
            echo "❌ $service_desc: Not Running"
        fi
    done
    
    echo "Metrics saved to: $metrics_file"
    
    log_message "Service metrics collected: $metrics_file"
}

# Function to collect Prometheus metrics
collect_prometheus_metrics() {
    log_message "Collecting Prometheus metrics"
    
    echo ""
    echo "Collecting Prometheus Metrics..."
    echo "=============================="
    
    # Check if Prometheus is accessible
    if curl -f -s $PROMETHEUS_ENDPOINT/status > /dev/null 2>&1; then
        echo "✅ Prometheus is accessible"
        
        # Collect some key metrics
        local metrics_file="$METRICS_DIR/prometheus_metrics_$(date +%Y%m%d_%H%M%S).txt"
        
        # Get metric names
        curl -s "$PROMETHEUS_ENDPOINT/api/v1/label/__name__/values" | jq -r '.data[]' | head -20 > "$metrics_file"
        
        echo "Sample metrics collected:"
        head -10 "$metrics_file"
        echo "Metrics saved to: $metrics_file"
    else
        echo "❌ Prometheus is not accessible"
    fi
    
    log_message "Prometheus metrics collection attempted"
}

# Function to generate metrics summary
generate_metrics_summary() {
    log_message "Generating metrics summary"
    
    echo ""
    echo "Generating Metrics Summary..."
    echo "==========================="
    
    local summary_file="$METRICS_DIR/metrics_summary_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create summary header
    echo "Atlas Production Metrics Summary" > "$summary_file"
    echo "Generated: $(date)" >> "$summary_file"
    echo "================================" >> "$summary_file"
    echo "" >> "$summary_file"
    
    # Add system metrics summary
    echo "System Metrics:" >> "$summary_file"
    echo "--------------" >> "$summary_file"
    local latest_system_metrics=$(ls -t $METRICS_DIR/system_metrics_*.json 2>/dev/null | head -1)
    if [ ! -z "$latest_system_metrics" ]; then
        jq '.' "$latest_system_metrics" >> "$summary_file"
    else
        echo "No system metrics available" >> "$summary_file"
    fi
    echo "" >> "$summary_file"
    
    # Add application metrics summary
    echo "Application Metrics:" >> "$summary_file"
    echo "------------------" >> "$summary_file"
    local latest_app_metrics=$(ls -t $METRICS_DIR/application_metrics_*.json 2>/dev/null | head -1)
    if [ ! -z "$latest_app_metrics" ]; then
        jq '.' "$latest_app_metrics" >> "$summary_file"
    else
        echo "No application metrics available" >> "$summary_file"
    fi
    echo "" >> "$summary_file"
    
    # Add service metrics summary
    echo "Service Metrics:" >> "$summary_file"
    echo "---------------" >> "$summary_file"
    local latest_service_metrics=$(ls -t $METRICS_DIR/service_metrics_*.json 2>/dev/null | head -1)
    if [ ! -z "$latest_service_metrics" ]; then
        jq '.' "$latest_service_metrics" >> "$summary_file"
    else
        echo "No service metrics available" >> "$summary_file"
    fi
    
    echo "Summary report saved to: $summary_file"
    echo ""
    echo "Latest metrics summary:"
    head -20 "$summary_file"
    
    log_message "Metrics summary generated: $summary_file"
}

# Function to clean old metrics files
clean_old_metrics() {
    log_message "Cleaning old metrics files"
    
    echo ""
    echo "Cleaning Old Metrics Files..."
    echo "==========================="
    
    # Remove metrics files older than 30 days
    find "$METRICS_DIR" -name "*.json" -mtime +30 -delete 2>/dev/null || true
    find "$METRICS_DIR" -name "*.txt" -mtime +30 -delete 2>/dev/null || true
    
    echo "Old metrics files cleaned"
    log_message "Old metrics files cleaned"
}

# Main metrics collection function
main() {
    log_message "=== Starting Atlas Metrics Collection ==="
    
    # Start time
    local start_time=$(date)
    log_message "Metrics collection started at: $start_time"
    
    # Handle different collection types
    case $1 in
        "system")
            collect_system_metrics
            ;;
        "application")
            collect_application_metrics
            ;;
        "service")
            collect_service_metrics
            ;;
        "prometheus")
            collect_prometheus_metrics
            ;;
        "summary")
            generate_metrics_summary
            ;;
        "clean")
            clean_old_metrics
            ;;
        *)
            # Run all collections
            collect_system_metrics
            collect_application_metrics
            collect_service_metrics
            collect_prometheus_metrics
            generate_metrics_summary
            clean_old_metrics
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Metrics collection completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Metrics Collection Completed ==="
    
    echo ""
    echo "✅ Metrics collection complete!"
    echo "📁 Metrics saved to: $METRICS_DIR"
}

# Run main function
main "$@"