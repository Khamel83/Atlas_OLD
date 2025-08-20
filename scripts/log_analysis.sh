#!/bin/bash

# Atlas Production Log Analysis Script
# This script analyzes logs from the Atlas production environment to identify issues and trends

set -e  # Exit on any error

echo "Starting Atlas Production Log Analysis..."

# Configuration
LOG_ANALYSIS_DIR="/home/ubuntu/dev/atlas/logs/analysis"
LOG_FILES=(
    "/home/ubuntu/dev/atlas/logs/atlas_background.log"
    "/home/ubuntu/dev/atlas/logs/production.log"
    "/var/log/nginx/access.log"
    "/var/log/nginx/error.log"
    "/var/log/postgresql/postgresql-*.log"
    "/var/log/syslog"
)

# Create analysis directory if it doesn't exist
mkdir -p "$LOG_ANALYSIS_DIR"

# Function to analyze error patterns
analyze_error_patterns() {
    echo "Analyzing Error Patterns..."
    echo "=========================="
    
    local error_report="$LOG_ANALYSIS_DIR/error_analysis_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create error report header
    echo "Atlas Production Error Analysis Report" > "$error_report"
    echo "Generated: $(date)" >> "$error_report"
    echo "=====================================" >> "$error_report"
    echo "" >> "$error_report"
    
    # Analyze each log file for errors
    for log_file in "${LOG_FILES[@]}"; do
        # Handle wildcards
        if [[ "$log_file" == *"*"* ]]; then
            for expanded_file in $log_file; do
                if [ -f "$expanded_file" ]; then
                    analyze_single_log "$expanded_file" "$error_report"
                fi
            done
        elif [ -f "$log_file" ]; then
            analyze_single_log "$log_file" "$error_report"
        fi
    done
    
    # Show summary
    echo "Error analysis complete. Report saved to: $error_report"
    echo "Top 10 error patterns:"
    tail -n +$(($(grep -n "Top Error Patterns" "$error_report" | cut -d: -f1) + 1)) "$error_report" | head -10
}

# Function to analyze a single log file
analyze_single_log() {
    local log_file=$1
    local report_file=$2
    
    echo "Analyzing $log_file..."
    
    # Add section header to report
    echo "Log File: $log_file" >> "$report_file"
    echo "-------------------" >> "$report_file"
    
    # Count different types of errors
    local error_count=$(grep -i "error|exception|fail|critical" "$log_file" 2>/dev/null | wc -l)
    echo "Total errors: $error_count" >> "$report_file"
    
    # Show top error patterns
    echo "Top Error Patterns:" >> "$report_file"
    grep -i "error|exception|fail|critical" "$log_file" 2>/dev/null | \
        sed 's/.*\(ERROR|Error|error|EXCEPTION|Exception|exception|FAIL|Fail|fail|CRITICAL|Critical|critical\).*/\1/' | \
        sort | uniq -c | sort -nr | head -10 >> "$report_file"
    
    echo "" >> "$report_file"
}

# Function to analyze performance patterns
analyze_performance_patterns() {
    echo "Analyzing Performance Patterns..."
    echo "================================"
    
    local perf_report="$LOG_ANALYSIS_DIR/performance_analysis_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create performance report header
    echo "Atlas Production Performance Analysis Report" > "$perf_report"
    echo "Generated: $(date)" >> "$perf_report"
    echo "===========================================" >> "$perf_report"
    echo "" >> "$perf_report"
    
    # Analyze response times from Nginx access log
    if [ -f "/var/log/nginx/access.log" ]; then
        echo "Nginx Response Time Analysis:" >> "$perf_report"
        echo "----------------------------" >> "$perf_report"
        
        # Extract response times (assuming log format includes response time)
        local response_times=$(awk '{print $NF}' /var/log/nginx/access.log | grep -E '^[0-9]+\.?[0-9]*$' | head -1000)
        if [ ! -z "$response_times" ]; then
            # Calculate average response time
            local avg_response=$(echo "$response_times" | awk '{sum+=$1} END {print sum/NR}')
            echo "Average response time: ${avg_response}s" >> "$perf_report"
            
            # Calculate 95th percentile
            local p95_response=$(echo "$response_times" | sort -n | awk 'NR==int(0.95*NF+0.5)')
            echo "95th percentile response time: ${p95_response}s" >> "$perf_report"
        else
            echo "No response time data found in access log" >> "$perf_report"
        fi
        echo "" >> "$perf_report"
    fi
    
    # Show performance summary
    echo "Performance analysis complete. Report saved to: $perf_report"
}

# Function to analyze security patterns
analyze_security_patterns() {
    echo "Analyzing Security Patterns..."
    echo "============================="
    
    local security_report="$LOG_ANALYSIS_DIR/security_analysis_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create security report header
    echo "Atlas Production Security Analysis Report" > "$security_report"
    echo "Generated: $(date)" >> "$security_report"
    echo "========================================" >> "$security_report"
    echo "" >> "$security_report"
    
    # Analyze failed login attempts
    if [ -f "/var/log/auth.log" ]; then
        echo "Failed Login Attempts:" >> "$security_report"
        echo "---------------------" >> "$security_report"
        grep "Failed password|Invalid user|Connection closed by authenticating user" /var/log/auth.log | \
            tail -20 >> "$security_report"
        echo "" >> "$security_report"
        
        # Count failed attempts
        local failed_count=$(grep "Failed password|Invalid user" /var/log/auth.log | wc -l)
        echo "Total failed login attempts: $failed_count" >> "$security_report"
        echo "" >> "$security_report"
    fi
    
    # Analyze suspicious Nginx requests
    if [ -f "/var/log/nginx/access.log" ]; then
        echo "Suspicious Web Requests:" >> "$security_report"
        echo "-----------------------" >> "$security_report"
        grep -E "(wp-login|admin|shell|phpmyadmin|cgi-bin)" /var/log/nginx/access.log | \
            tail -20 >> "$security_report"
        echo "" >> "$security_report"
    fi
    
    # Show security summary
    echo "Security analysis complete. Report saved to: $security_report"
}

# Function to generate summary report
generate_summary_report() {
    echo "Generating Summary Report..."
    echo "==========================="
    
    local summary_report="$LOG_ANALYSIS_DIR/summary_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create summary report header
    echo "Atlas Production Log Analysis Summary Report" > "$summary_report"
    echo "Generated: $(date)" >> "$summary_report"
    echo "===========================================" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add timestamp of last log entries
    echo "Recent Log Activity:" >> "$summary_report"
    echo "-------------------" >> "$summary_report"
    for log_file in "${LOG_FILES[@]}"; do
        if [[ "$log_file" == *"*"* ]]; then
            for expanded_file in $log_file; do
                if [ -f "$expanded_file" ]; then
                    echo "$(basename $expanded_file): $(tail -1 $expanded_file 2>/dev/null | cut -d' ' -f1-3)" >> "$summary_report"
                fi
            done
        elif [ -f "$log_file" ]; then
            echo "$(basename $log_file): $(tail -1 $log_file 2>/dev/null | cut -d' ' -f1-3)" >> "$summary_report"
        fi
    done
    echo "" >> "$summary_report"
    
    # Show summary
    echo "Summary report complete. Report saved to: $summary_report"
    cat "$summary_report"
}

# Function to rotate and archive old logs
rotate_logs() {
    echo "Rotating Logs..."
    echo "==============="
    
    # This would typically be handled by logrotate, but we can do some basic cleanup
    local log_dir="/home/ubuntu/dev/atlas/logs"
    
    if [ -d "$log_dir" ]; then
        # Find and compress old log files
        find "$log_dir" -name "*.log" -mtime +7 -exec gzip {} \; 2>/dev/null || true
        echo "Compressed log files older than 7 days"
        
        # Remove very old compressed logs
        find "$log_dir" -name "*.log.gz" -mtime +30 -delete 2>/dev/null || true
        echo "Removed compressed log files older than 30 days"
    fi
}

# Main log analysis function
main() {
    echo "Starting Atlas Production Log Analysis..."
    echo "========================================"
    
    # Handle different analysis types
    case $1 in
        "errors")
            analyze_error_patterns
            ;;
        "performance")
            analyze_performance_patterns
            ;;
        "security")
            analyze_security_patterns
            ;;
        "rotate")
            rotate_logs
            ;;
        "summary")
            generate_summary_report
            ;;
        *)
            # Run all analyses
            analyze_error_patterns
            echo ""
            analyze_performance_patterns
            echo ""
            analyze_security_patterns
            echo ""
            generate_summary_report
            echo ""
            rotate_logs
            ;;
    esac
    
    echo ""
    echo "✅ Log analysis complete!"
    echo "📁 Analysis reports saved to: $LOG_ANALYSIS_DIR"
}

# Run main function
main "$@"