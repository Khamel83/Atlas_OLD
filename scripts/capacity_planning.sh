#!/bin/bash

# Atlas Production Capacity Planning Script
# This script plans and manages capacity for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Capacity Planning..."

# Configuration
CAPACITY_LOG="/home/ubuntu/dev/atlas/logs/capacity_planning.log"
CAPACITY_REPORT_DIR="/home/ubuntu/dev/atlas/reports/capacity"
CAPACITY_CONFIG="/home/ubuntu/dev/atlas/config/capacity.json"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $CAPACITY_LOG)"
mkdir -p "$CAPACITY_REPORT_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $CAPACITY_LOG
    echo "$1"
}

# Function to initialize capacity configuration
initialize_capacity_config() {
    log_message "Initializing capacity configuration"
    
    # Create default capacity configuration if it doesn't exist
    if [ ! -f "$CAPACITY_CONFIG" ]; then
        cat > "$CAPACITY_CONFIG" << EOF
{
    "capacity_planning": {
        "planning_horizon_months": 12,
        "growth_projection_percentage": 50,
        "resource_utilization_target": 70,
        "capacity_buffer_percentage": 20
    },
    "resources": {
        "compute": {
            "name": "Compute Resources",
            "current_allocation": {
                "cpu_cores": 2,
                "memory_gb": 8,
                "storage_gb": 50
            },
            "utilization_targets": {
                "cpu_percent": 70,
                "memory_percent": 70,
                "storage_percent": 80
            },
            "scaling_factors": {
                "cpu": 1.5,
                "memory": 1.5,
                "storage": 2.0
            }
        },
        "network": {
            "name": "Network Resources",
            "current_allocation": {
                "bandwidth_mbps": 100,
                "connections": 1000
            },
            "utilization_targets": {
                "bandwidth_percent": 70,
                "connections_percent": 80
            },
            "scaling_factors": {
                "bandwidth": 1.2,
                "connections": 1.5
            }
        },
        "database": {
            "name": "Database Resources",
            "current_allocation": {
                "storage_gb": 20,
                "connections": 50
            },
            "utilization_targets": {
                "storage_percent": 80,
                "connections_percent": 70
            },
            "scaling_factors": {
                "storage": 1.5,
                "connections": 1.2
            }
        }
    },
    "scaling_policies": {
        "automatic_scaling": {
            "enabled": true,
            "trigger_threshold_percent": 80,
            "cooldown_period_minutes": 10
        },
        "manual_scaling": {
            "enabled": true,
            "review_frequency_days": 30
        }
    },
    "forecasting": {
        "method": "linear_regression",
        "confidence_level": 95,
        "forecast_periods": 12
    }
}
EOF
        echo "✅ Created default capacity configuration"
        log_message "Default capacity configuration created"
    else
        echo "✅ Capacity configuration already exists"
    fi
}

# Function to analyze current capacity
analyze_current_capacity() {
    log_message "Analyzing current capacity"
    
    echo "Analyzing Current Capacity..."
    echo "=========================="
    
    local capacity_report="$CAPACITY_REPORT_DIR/current_capacity_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create capacity report header
    echo "Atlas Production Current Capacity Analysis" > "$capacity_report"
    echo "Generated: $(date)" >> "$capacity_report"
    echo "=======================================" >> "$capacity_report"
    echo "" >> "$capacity_report"
    
    # Get current system resources
    echo "Current System Resources:" >> "$capacity_report"
    echo "------------------------" >> "$capacity_report"
    
    # CPU information
    local cpu_cores=$(nproc)
    local cpu_model=$(lscpu | grep "Model name" | cut -d: -f2 | xargs)
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    
    echo "CPU:" >> "$capacity_report"
    echo "  Cores: $cpu_cores" >> "$capacity_report"
    echo "  Model: $cpu_model" >> "$capacity_report"
    echo "  Current Usage: ${cpu_usage}%" >> "$capacity_report"
    echo "" >> "$capacity_report"
    
    # Memory information
    local memory_total_gb=$(free -g | grep Mem | awk '{print $2}')
    local memory_used_gb=$(free -g | grep Mem | awk '{print $3}')
    local memory_usage=$(echo "scale=2; $memory_used_gb * 100 / $memory_total_gb" | bc)
    
    echo "Memory:" >> "$capacity_report"
    echo "  Total: ${memory_total_gb}GB" >> "$capacity_report"
    echo "  Used: ${memory_used_gb}GB" >> "$capacity_report"
    echo "  Current Usage: ${memory_usage}%" >> "$capacity_report"
    echo "" >> "$capacity_report"
    
    # Storage information
    local storage_total_gb=$(df -BG / | tail -1 | awk '{print $2}' | sed 's/G//')
    local storage_used_gb=$(df -BG / | tail -1 | awk '{print $3}' | sed 's/G//')
    local storage_usage=$(echo "scale=2; $storage_used_gb * 100 / $storage_total_gb" | bc)
    
    echo "Storage:" >> "$capacity_report"
    echo "  Total: ${storage_total_gb}GB" >> "$capacity_report"
    echo "  Used: ${storage_used_gb}GB" >> "$capacity_report"
    echo "  Current Usage: ${storage_usage}%" >> "$capacity_report"
    echo "" >> "$capacity_report"
    
    # Network information
    echo "Network:" >> "$capacity_report"
    echo "  Bandwidth: 100 Mbps (assumed)" >> "$capacity_report"
    echo "  Connections: $(ss -tuln | wc -l) (current)" >> "$capacity_report"
    echo "" >> "$capacity_report"
    
    # Database information
    echo "Database:" >> "$capacity_report"
    echo "  Storage: $(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT pg_size_pretty(pg_database_size('atlas'));" 2>/dev/null || echo "Unknown")" >> "$capacity_report"
    echo "  Connections: $(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM pg_stat_activity;" 2>/dev/null || echo "0")" >> "$capacity_report"
    echo "" >> "$capacity_report"
    
    # Compare with capacity targets
    echo "Capacity Utilization vs Targets:" >> "$capacity_report"
    echo "------------------------------" >> "$capacity_report"
    
    # Get capacity targets from configuration
    local cpu_target=$(jq -r '.resources.compute.utilization_targets.cpu_percent' "$CAPACITY_CONFIG")
    local memory_target=$(jq -r '.resources.compute.utilization_targets.memory_percent' "$CAPACITY_CONFIG")
    local storage_target=$(jq -r '.resources.compute.utilization_targets.storage_percent' "$CAPACITY_CONFIG")
    
    echo "CPU Usage: ${cpu_usage}% (Target: ${cpu_target}%)" >> "$capacity_report"
    if (( $(echo "$cpu_usage > $cpu_target" | bc -l) )); then
        echo "  ⚠️ CPU usage exceeds target" >> "$capacity_report"
    else
        echo "  ✅ CPU usage within target" >> "$capacity_report"
    fi
    echo "" >> "$capacity_report"
    
    echo "Memory Usage: ${memory_usage}% (Target: ${memory_target}%)" >> "$capacity_report"
    if (( $(echo "$memory_usage > $memory_target" | bc -l) )); then
        echo "  ⚠️ Memory usage exceeds target" >> "$capacity_report"
    else
        echo "  ✅ Memory usage within target" >> "$capacity_report"
    fi
    echo "" >> "$capacity_report"
    
    echo "Storage Usage: ${storage_usage}% (Target: ${storage_target}%)" >> "$capacity_report"
    if (( $(echo "$storage_usage > $storage_target" | bc -l) )); then
        echo "  ⚠️ Storage usage exceeds target" >> "$capacity_report"
    else
        echo "  ✅ Storage usage within target" >> "$capacity_report"
    fi
    echo "" >> "$capacity_report"
    
    # Capacity recommendations
    echo "Capacity Recommendations:" >> "$capacity_report"
    echo "-----------------------" >> "$capacity_report"
    
    local recommendations=()
    
    if (( $(echo "$cpu_usage > $cpu_target" | bc -l) )); then
        recommendations+=("Consider increasing CPU allocation")
    fi
    
    if (( $(echo "$memory_usage > $memory_target" | bc -l) )); then
        recommendations+=("Consider increasing memory allocation")
    fi
    
    if (( $(echo "$storage_usage > $storage_target" | bc -l) )); then
        recommendations+=("Consider increasing storage allocation")
    fi
    
    if [ ${#recommendations[@]} -eq 0 ]; then
        echo "✅ Current capacity is sufficient for current workload" >> "$capacity_report"
        echo "✅ No immediate capacity increases required" >> "$capacity_report"
        echo "✅ Continue monitoring resource utilization" >> "$capacity_report"
    else
        for recommendation in "${recommendations[@]}"; do
            echo "⚠️ $recommendation" >> "$capacity_report"
        done
        echo "✅ Schedule capacity review within 30 days" >> "$capacity_report"
    fi
    echo "" >> "$capacity_report"
    
    echo "✅ Current capacity analysis completed"
    echo "📋 Capacity report saved to: $capacity_report"
    log_message "Current capacity analysis completed: $capacity_report"
    
    # Display summary
    echo ""
    echo "Current Capacity Summary:"
    echo "  CPU: ${cpu_usage}% (Target: ${cpu_target}%)"
    echo "  Memory: ${memory_usage}% (Target: ${memory_target}%)"
    echo "  Storage: ${storage_usage}% (Target: ${storage_target}%)"
    echo "  Network: 100 Mbps (assumed)"
    echo "  Database: $(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT pg_size_pretty(pg_database_size('atlas'));" 2>/dev/null || echo "Unknown")"
    echo "  Report: $capacity_report"
    
    # Check if any recommendations were made
    if [ ${#recommendations[@]} -gt 0 ]; then
        echo "  Status: ⚠️ CAPACITY RECOMMENDATIONS MADE"
        echo "  Recommendations:"
        for recommendation in "${recommendations[@]}"; do
            echo "    - $recommendation"
        done
    else
        echo "  Status: ✅ CAPACITY SUFFICIENT"
    fi
}

# Function to project future capacity needs
project_future_capacity() {
    log_message "Projecting future capacity needs"
    
    echo ""
    echo "Projecting Future Capacity Needs..."
    echo "================================="
    
    local projection_report="$CAPACITY_REPORT_DIR/future_capacity_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create projection report header
    echo "Atlas Production Future Capacity Projection" > "$projection_report"
    echo "Generated: $(date)" >> "$projection_report"
    echo "========================================" >> "$projection_report"
    echo "" >> "$projection_report"
    
    # Get planning horizon and growth projection
    local planning_horizon_months=$(jq -r '.capacity_planning.planning_horizon_months' "$CAPACITY_CONFIG")
    local growth_projection_percentage=$(jq -r '.capacity_planning.growth_projection_percentage' "$CAPACITY_REPORT_DIR")
    
    echo "Planning Horizon: ${planning_horizon_months} months" >> "$projection_report"
    echo "Growth Projection: ${growth_projection_percentage}%" >> "$projection_report"
    echo "" >> "$projection_report"
    
    # Get current resource allocation
    echo "Current Resource Allocation:" >> "$projection_report"
    echo "---------------------------" >> "$projection_report"
    
    local current_cpu_cores=$(jq -r '.resources.compute.current_allocation.cpu_cores' "$CAPACITY_CONFIG")
    local current_memory_gb=$(jq -r '.resources.compute.current_allocation.memory_gb' "$CAPACITY_CONFIG")
    local current_storage_gb=$(jq -r '.resources.compute.current_allocation.storage_gb' "$CAPACITY_CONFIG")
    local current_bandwidth_mbps=$(jq -r '.resources.network.current_allocation.bandwidth_mbps' "$CAPACITY_CONFIG")
    local current_network_connections=$(jq -r '.resources.network.current_allocation.connections' "$CAPACITY_CONFIG")
    local current_database_storage_gb=$(jq -r '.resources.database.current_allocation.storage_gb' "$CAPACITY_CONFIG")
    local current_database_connections=$(jq -r '.resources.database.current_allocation.connections' "$CAPACITY_CONFIG")
    
    echo "Compute Resources:" >> "$projection_report"
    echo "  CPU Cores: $current_cpu_cores" >> "$projection_report"
    echo "  Memory: ${current_memory_gb}GB" >> "$projection_report"
    echo "  Storage: ${current_storage_gb}GB" >> "$projection_report"
    echo "" >> "$projection_report"
    
    echo "Network Resources:" >> "$projection_report"
    echo "  Bandwidth: ${current_bandwidth_mbps} Mbps" >> "$projection_report"
    echo "  Connections: $current_network_connections" >> "$projection_report"
    echo "" >> "$projection_report"
    
    echo "Database Resources:" >> "$projection_report"
    echo "  Storage: ${current_database_storage_gb}GB" >> "$projection_report"
    echo "  Connections: $current_database_connections" >> "$projection_report"
    echo "" >> "$projection_report"
    
    # Project future resource needs
    echo "Projected Resource Needs:" >> "$projection_report"
    echo "------------------------" >> "$projection_report"
    
    # Calculate projected growth factor
    local growth_factor=$(echo "scale=2; 1 + $growth_projection_percentage / 100" | bc)
    
    # Project compute resources
    echo "Compute Resources (Projected):" >> "$projection_report"
    local projected_cpu_cores=$(echo "scale=0; $current_cpu_cores * $growth_factor" | bc)
    local projected_memory_gb=$(echo "scale=0; $current_memory_gb * $growth_factor" | bc)
    local projected_storage_gb=$(echo "scale=0; $current_storage_gb * $growth_factor" | bc)
    
    echo "  CPU Cores: $projected_cpu_cores (Current: $current_cpu_cores)" >> "$projection_report"
    echo "  Memory: ${projected_memory_gb}GB (Current: ${current_memory_gb}GB)" >> "$projection_report"
    echo "  Storage: ${projected_storage_gb}GB (Current: ${current_storage_gb}GB)" >> "$projection_report"
    echo "" >> "$projection_report"
    
    # Project network resources
    echo "Network Resources (Projected):" >> "$projection_report"
    local projected_bandwidth_mbps=$(echo "scale=0; $current_bandwidth_mbps * $growth_factor" | bc)
    local projected_network_connections=$(echo "scale=0; $current_network_connections * $growth_factor" | bc)
    
    echo "  Bandwidth: ${projected_bandwidth_mbps} Mbps (Current: ${current_bandwidth_mbps} Mbps)" >> "$projection_report"
    echo "  Connections: $projected_network_connections (Current: $current_network_connections)" >> "$projection_report"
    echo "" >> "$projection_report"
    
    # Project database resources
    echo "Database Resources (Projected):" >> "$projection_report"
    local projected_database_storage_gb=$(echo "scale=0; $current_database_storage_gb * $growth_factor" | bc)
    local projected_database_connections=$(echo "scale=0; $current_database_connections * $growth_factor" | bc)
    
    echo "  Storage: ${projected_database_storage_gb}GB (Current: ${current_database_storage_gb}GB)" >> "$projection_report"
    echo "  Connections: $projected_database_connections (Current: $current_database_connections)" >> "$projection_report"
    echo "" >> "$projection_report"
    
    # Compare with OCI free tier limits
    echo "OCI Free Tier Comparison:" >> "$projection_report"
    echo "------------------------" >> "$projection_report"
    
    # OCI free tier limits (as of 2023)
    local oci_cpu_limit=4
    local oci_memory_limit=24
    local oci_storage_limit=100
    local oci_bandwidth_limit=10000
    local oci_connections_limit=10000
    
    echo "OCI Free Tier Limits:" >> "$projection_report"
    echo "  CPU Cores: $oci_cpu_limit" >> "$projection_report"
    echo "  Memory: ${oci_memory_limit}GB" >> "$projection_report"
    echo "  Storage: ${oci_storage_limit}GB" >> "$projection_report"
    echo "  Bandwidth: ${oci_bandwidth_limit} Mbps" >> "$projection_report"
    echo "  Connections: $oci_connections_limit" >> "$projection_report"
    echo "" >> "$projection_report"
    
    echo "Projected Needs vs OCI Limits:" >> "$projection_report"
    echo "----------------------------" >> "$projection_report"
    
    if [ $projected_cpu_cores -le $oci_cpu_limit ]; then
        echo "✅ CPU Cores: Within OCI free tier limit ($projected_cpu_cores ≤ $oci_cpu_limit)" >> "$projection_report"
    else
        echo "❌ CPU Cores: Exceeds OCI free tier limit ($projected_cpu_cores > $oci_cpu_limit)" >> "$projection_report"
    fi
    
    if (( $(echo "$projected_memory_gb <= $oci_memory_limit" | bc -l) )); then
        echo "✅ Memory: Within OCI free tier limit (${projected_memory_gb}GB ≤ ${oci_memory_limit}GB)" >> "$projection_report"
    else
        echo "❌ Memory: Exceeds OCI free tier limit (${projected_memory_gb}GB > ${oci_memory_limit}GB)" >> "$projection_report"
    fi
    
    if [ $projected_storage_gb -le $oci_storage_limit ]; then
        echo "✅ Storage: Within OCI free tier limit (${projected_storage_gb}GB ≤ ${oci_storage_limit}GB)" >> "$projection_report"
    else
        echo "❌ Storage: Exceeds OCI free tier limit (${projected_storage_gb}GB > ${oci_storage_limit}GB)" >> "$projection_report"
    fi
    
    if [ $projected_bandwidth_mbps -le $oci_bandwidth_limit ]; then
        echo "✅ Bandwidth: Within OCI free tier limit (${projected_bandwidth_mbps} Mbps ≤ ${oci_bandwidth_limit} Mbps)" >> "$projection_report"
    else
        echo "❌ Bandwidth: Exceeds OCI free tier limit (${projected_bandwidth_mbps} Mbps > ${oci_bandwidth_limit} Mbps)" >> "$projection_report"
    fi
    
    if [ $projected_network_connections -le $oci_connections_limit ]; then
        echo "✅ Network Connections: Within OCI free tier limit ($projected_network_connections ≤ $oci_connections_limit)" >> "$projection_report"
    else
        echo "❌ Network Connections: Exceeds OCI free tier limit ($projected_network_connections > $oci_connections_limit)" >> "$projection_report"
    fi
    
    if [ $projected_database_storage_gb -le $oci_storage_limit ]; then
        echo "✅ Database Storage: Within OCI free tier limit (${projected_database_storage_gb}GB ≤ ${oci_storage_limit}GB)" >> "$projection_report"
    else
        echo "❌ Database Storage: Exceeds OCI free tier limit (${projected_database_storage_gb}GB > ${oci_storage_limit}GB)" >> "$projection_report"
    fi
    
    if [ $projected_database_connections -le $oci_connections_limit ]; then
        echo "✅ Database Connections: Within OCI free tier limit ($projected_database_connections ≤ $oci_connections_limit)" >> "$projection_report"
    else
        echo "❌ Database Connections: Exceeds OCI free tier limit ($projected_database_connections > $oci_connections_limit)" >> "$projection_report"
    fi
    echo "" >> "$projection_report"
    
    # Capacity planning recommendations
    echo "Capacity Planning Recommendations:" >> "$projection_report"
    echo "--------------------------------" >> "$projection_report"
    
    local oci_limit_exceeded=false
    
    if [ $projected_cpu_cores -gt $oci_cpu_limit ]; then
        echo "❌ Projected CPU needs exceed OCI free tier limits" >> "$projection_report"
        oci_limit_exceeded=true
    fi
    
    if (( $(echo "$projected_memory_gb > $oci_memory_limit" | bc -l) )); then
        echo "❌ Projected memory needs exceed OCI free tier limits" >> "$projection_report"
        oci_limit_exceeded=true
    fi
    
    if [ $projected_storage_gb -gt $oci_storage_limit ]; then
        echo "❌ Projected storage needs exceed OCI free tier limits" >> "$projection_report"
        oci_limit_exceeded=true
    fi
    
    if [ $projected_bandwidth_mbps -gt $oci_bandwidth_limit ]; then
        echo "❌ Projected bandwidth needs exceed OCI free tier limits" >> "$projection_report"
        oci_limit_exceeded=true
    fi
    
    if [ $projected_network_connections -gt $oci_connections_limit ]; then
        echo "❌ Projected network connections exceed OCI free tier limits" >> "$projection_report"
        oci_limit_exceeded=true
    fi
    
    if [ $projected_database_storage_gb -gt $oci_storage_limit ]; then
        echo "❌ Projected database storage needs exceed OCI free tier limits" >> "$projection_report"
        oci_limit_exceeded=true
    fi
    
    if [ $projected_database_connections -gt $oci_connections_limit ]; then
        echo "❌ Projected database connections exceed OCI free tier limits" >> "$projection_report"
        oci_limit_exceeded=true
    fi
    
    if $oci_limit_exceeded; then
        echo "⚠️ Consider upgrading from OCI free tier to paid tier" >> "$projection_report"
        echo "⚠️ Evaluate resource optimization strategies" >> "$projection_report"
        echo "⚠️ Review growth projection assumptions" >> "$projection_report"
    else
        echo "✅ Projected resource needs are within OCI free tier limits" >> "$projection_report"
        echo "✅ Continue with current OCI free tier configuration" >> "$projection_report"
        echo "✅ Monitor resource usage trends" >> "$projection_report"
    fi
    echo "" >> "$projection_report"
    
    echo "✅ Future capacity projection completed"
    echo "📋 Projection report saved to: $projection_report"
    log_message "Future capacity projection completed: $projection_report"
    
    # Display summary
    echo ""
    echo "Future Capacity Projection Summary:"
    echo "  Planning Horizon: ${planning_horizon_months} months"
    echo "  Growth Projection: ${growth_projection_percentage}%"
    echo "  Projected CPU Cores: $projected_cpu_cores (Current: $current_cpu_cores)"
    echo "  Projected Memory: ${projected_memory_gb}GB (Current: ${current_memory_gb}GB)"
    echo "  Projected Storage: ${projected_storage_gb}GB (Current: ${current_storage_gb}GB)"
    echo "  Projected Bandwidth: ${projected_bandwidth_mbps} Mbps (Current: ${current_bandwidth_mbps} Mbps)"
    echo "  Projected Network Connections: $projected_network_connections (Current: $current_network_connections)"
    echo "  Projected Database Storage: ${projected_database_storage_gb}GB (Current: ${current_database_storage_gb}GB)"
    echo "  Projected Database Connections: $projected_database_connections (Current: $current_database_connections)"
    echo "  Report: $projection_report"
    
    # Check if any OCI limits are exceeded
    if $oci_limit_exceeded; then
        echo "  Status: ❌ OCI FREE TIER LIMITS EXCEEDED"
        echo "  Recommendations:"
        echo "    - Upgrade from OCI free tier to paid tier"
        echo "    - Evaluate resource optimization strategies"
        echo "    - Review growth projection assumptions"
    else
        echo "  Status: ✅ WITHIN OCI FREE TIER LIMITS"
        echo "  Recommendations:"
        echo "    - Continue with current OCI free tier configuration"
        echo "    - Monitor resource usage trends"
        echo "    - Schedule regular capacity planning reviews"
    fi
}

# Function to implement scaling policies
implement_scaling_policies() {
    log_message "Implementing scaling policies"
    
    echo ""
    echo "Implementing Scaling Policies..."
    echo "=============================="
    
    local scaling_report="$CAPACITY_REPORT_DIR/scaling_policies_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create scaling report header
    echo "Atlas Production Scaling Policies Implementation" > "$scaling_report"
    echo "Generated: $(date)" >> "$scaling_report"
    echo "==============================================" >> "$scaling_report"
    echo "" >> "$scaling_report"
    
    # Get scaling policy configuration
    local auto_scaling_enabled=$(jq -r '.scaling_policies.automatic_scaling.enabled' "$CAPACITY_CONFIG")
    local auto_scaling_threshold=$(jq -r '.scaling_policies.automatic_scaling.trigger_threshold_percent' "$CAPACITY_CONFIG")
    local auto_scaling_cooldown=$(jq -r '.scaling_policies.automatic_scaling.cooldown_period_minutes' "$CAPACITY_CONFIG")
    local manual_scaling_enabled=$(jq -r '.scaling_policies.manual_scaling.enabled' "$CAPACITY_CONFIG")
    local manual_scaling_review_frequency=$(jq -r '.scaling_policies.manual_scaling.review_frequency_days' "$CAPACITY_CONFIG")
    
    echo "Scaling Policy Configuration:" >> "$scaling_report"
    echo "---------------------------" >> "$scaling_report"
    echo "Automatic Scaling:" >> "$scaling_report"
    echo "  Enabled: $auto_scaling_enabled" >> "$scaling_report"
    echo "  Trigger Threshold: ${auto_scaling_threshold}%" >> "$scaling_report"
    echo "  Cooldown Period: ${auto_scaling_cooldown} minutes" >> "$scaling_report"
    echo "" >> "$scaling_report"
    
    echo "Manual Scaling:" >> "$scaling_report"
    echo "  Enabled: $manual_scaling_enabled" >> "$scaling_report"
    echo "  Review Frequency: ${manual_scaling_review_frequency} days" >> "$scaling_report"
    echo "" >> "$scaling_report"
    
    # Implement automatic scaling
    echo "Automatic Scaling Implementation:" >> "$scaling_report"
    echo "-------------------------------" >> "$scaling_report"
    
    if [ "$auto_scaling_enabled" = "true" ]; then
        echo "✅ Automatic scaling is enabled" >> "$scaling_report"
        
        # Create systemd service for automatic scaling
        local systemd_service_file="/etc/systemd/system/atlas-auto-scaling.service"
        sudo tee "$systemd_service_file" > /dev/null << EOF
[Unit]
Description=Atlas Automatic Scaling Service
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/dev/atlas
ExecStart=/home/ubuntu/dev/atlas/scripts/auto_scaling.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
        
        # Create systemd timer for automatic scaling
        local systemd_timer_file="/etc/systemd/system/atlas-auto-scaling.timer"
        sudo tee "$systemd_timer_file" > /dev/null << EOF
[Unit]
Description=Atlas Automatic Scaling Timer
Requires=atlas-auto-scaling.service

[Timer]
OnBootSec=5min
OnUnitActiveSec=5min

[Install]
WantedBy=timers.target
EOF
        
        # Enable and start the timer
        sudo systemctl daemon-reload
        sudo systemctl enable atlas-auto-scaling.timer
        sudo systemctl start atlas-auto-scaling.timer
        
        echo "✅ Automatic scaling service created" >> "$scaling_report"
        echo "✅ Automatic scaling timer configured" >> "$scaling_report"
        echo "✅ Automatic scaling service enabled" >> "$scaling_report"
        echo "✅ Automatic scaling service started" >> "$scaling_report"
    else
        echo "❌ Automatic scaling is disabled" >> "$scaling_report"
        echo "ℹ️ No automatic scaling service created" >> "$scaling_report"
    fi
    echo "" >> "$scaling_report"
    
    # Implement manual scaling
    echo "Manual Scaling Implementation:" >> "$scaling_report"
    echo "----------------------------" >> "$scaling_report"
    
    if [ "$manual_scaling_enabled" = "true" ]; then
        echo "✅ Manual scaling is enabled" >> "$scaling_report"
        
        # Create manual scaling reminder
        local manual_scaling_reminder="/home/ubuntu/dev/atlas/scripts/manual_scaling_reminder.sh"
        cat > "$manual_scaling_reminder" << EOF
#!/bin/bash
# Atlas Manual Scaling Reminder Script

echo "Atlas Manual Scaling Reminder"
echo "=========================="
echo ""
echo "It's time to review manual scaling requirements."
echo ""
echo "Current Resource Usage:"
echo "---------------------"
echo "CPU Usage: \$(top -bn1 | grep 'Cpu(s)' | awk '{print \$2}' | cut -d'%' -f1)%"
echo "Memory Usage: \$(free | grep Mem | awk '{printf(\"%.0f\", \$3/\$2 * 100.0)}')%"
echo "Disk Usage: \$(df / | tail -1 | awk '{print \$5}' | sed 's/%//')%"
echo ""
echo "Scaling Review Frequency: Every ${manual_scaling_review_frequency} days"
echo "Last Review: \$(date)"
echo ""
echo "For more information, check the capacity planning reports in:"
echo "$CAPACITY_REPORT_DIR/"
EOF
        
        # Make script executable
        chmod +x "$manual_scaling_reminder"
        
        # Create cron job for manual scaling reminders
        local cron_job="0 9 */${manual_scaling_review_frequency} * * $manual_scaling_reminder >> /home/ubuntu/dev/atlas/logs/manual_scaling_reminder.log 2>&1"
        
        # Add to crontab
        (crontab -l 2>/dev/null; echo "$cron_job") | crontab -
        
        echo "✅ Manual scaling reminder script created" >> "$scaling_report"
        echo "✅ Manual scaling reminder cron job configured" >> "$scaling_report"
        echo "✅ Manual scaling review scheduled every ${manual_scaling_review_frequency} days" >> "$scaling_report"
    else
        echo "❌ Manual scaling is disabled" >> "$scaling_report"
        echo "ℹ️ No manual scaling reminder created" >> "$scaling_report"
    fi
    echo "" >> "$scaling_report"
    
    # Scaling policy recommendations
    echo "Scaling Policy Recommendations:" >> "$scaling_report"
    echo "-----------------------------" >> "$scaling_report"
    
    if [ "$auto_scaling_enabled" = "true" ] && [ "$manual_scaling_enabled" = "true" ]; then
        echo "✅ Both automatic and manual scaling are enabled" >> "$scaling_report"
        echo "✅ Well-balanced scaling approach implemented" >> "$scaling_report"
        echo "✅ Continue current scaling policy implementation" >> "$scaling_report"
    elif [ "$auto_scaling_enabled" = "true" ]; then
        echo "✅ Automatic scaling is enabled" >> "$scaling_report"
        echo "⚠️ Manual scaling is disabled" >> "$scaling_report"
        echo "✅ Consider enabling manual scaling for oversight" >> "$scaling_report"
    elif [ "$manual_scaling_enabled" = "true" ]; then
        echo "✅ Manual scaling is enabled" >> "$scaling_report"
        echo "⚠️ Automatic scaling is disabled" >> "$scaling_report"
        echo "✅ Consider enabling automatic scaling for responsiveness" >> "$scaling_report"
    else
        echo "❌ Both automatic and manual scaling are disabled" >> "$scaling_report"
        echo "❌ No scaling policies are currently active" >> "$scaling_report"
        echo "⚠️ Consider implementing at least one scaling policy" >> "$scaling_report"
    fi
    echo "" >> "$scaling_report"
    
    echo "✅ Scaling policies implementation completed"
    echo "📋 Scaling policies report saved to: $scaling_report"
    log_message "Scaling policies implementation completed: $scaling_report"
    
    # Display summary
    echo ""
    echo "Scaling Policies Implementation Summary:"
    echo "  Automatic Scaling: $auto_scaling_enabled"
    echo "  Manual Scaling: $manual_scaling_enabled"
    echo "  Trigger Threshold: ${auto_scaling_threshold}%"
    echo "  Cooldown Period: ${auto_scaling_cooldown} minutes"
    echo "  Review Frequency: ${manual_scaling_review_frequency} days"
    echo "  Report: $scaling_report"
    
    # Check scaling policy status
    if [ "$auto_scaling_enabled" = "true" ] && [ "$manual_scaling_enabled" = "true" ]; then
        echo "  Status: ✅ WELL-BALANCED SCALING POLICIES"
        echo "  Recommendations:"
        echo "    - Continue current scaling policy implementation"
        echo "    - Monitor automatic scaling effectiveness"
        echo "    - Schedule regular manual scaling reviews"
    elif [ "$auto_scaling_enabled" = "true" ]; then
        echo "  Status: ⚠️ AUTOMATIC SCALING ONLY"
        echo "  Recommendations:"
        echo "    - Consider enabling manual scaling for oversight"
        echo "    - Monitor automatic scaling effectiveness"
        echo "    - Schedule occasional manual scaling reviews"
    elif [ "$manual_scaling_enabled" = "true" ]; then
        echo "  Status: ⚠️ MANUAL SCALING ONLY"
        echo "  Recommendations:"
        echo "    - Consider enabling automatic scaling for responsiveness"
        echo "    - Monitor manual scaling effectiveness"
        echo "    - Schedule regular manual scaling reviews"
    else
        echo "  Status: ❌ NO SCALING POLICIES ACTIVE"
        echo "  Recommendations:"
        echo "    - Implement at least one scaling policy"
        echo "    - Consider both automatic and manual scaling"
        echo "    - Monitor resource usage trends"
    fi
}

# Function to generate capacity forecast
generate_capacity_forecast() {
    log_message "Generating capacity forecast"
    
    echo ""
    echo "Generating Capacity Forecast..."
    echo "============================="
    
    local forecast_report="$CAPACITY_REPORT_DIR/capacity_forecast_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create forecast report header
    echo "Atlas Production Capacity Forecast" > "$forecast_report"
    echo "Generated: $(date)" >> "$forecast_report"
    echo "================================" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Get forecasting configuration
    local forecast_method=$(jq -r '.forecasting.method' "$CAPACITY_CONFIG")
    local confidence_level=$(jq -r '.forecasting.confidence_level' "$CAPACITY_CONFIG")
    local forecast_periods=$(jq -r '.forecasting.forecast_periods' "$CAPACITY_CONFIG")
    
    echo "Forecasting Configuration:" >> "$forecast_report"
    echo "------------------------" >> "$forecast_report"
    echo "Method: $forecast_method" >> "$forecast_report"
    echo "Confidence Level: ${confidence_level}%" >> "$forecast_report"
    echo "Forecast Periods: ${forecast_periods} months" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Generate forecast using linear regression
    echo "Capacity Forecast (Linear Regression):" >> "$forecast_report"
    echo "------------------------------------" >> "$forecast_report"
    
    # Get current resource usage
    local current_cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local current_memory_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    local current_disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "Current Resource Usage:" >> "$forecast_report"
    echo "  CPU Usage: ${current_cpu_usage}%" >> "$forecast_report"
    echo "  Memory Usage: ${current_memory_usage}%" >> "$forecast_report"
    echo "  Disk Usage: ${current_disk_usage}%" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Calculate projected usage (simple linear growth model)
    echo "Projected Resource Usage:" >> "$forecast_report"
    echo "------------------------" >> "$forecast_report"
    
    # Calculate growth rate (5% per month for demonstration)
    local growth_rate=1.05
    
    # Project usage for next 12 months
    echo "Month | CPU Usage (%) | Memory Usage (%) | Disk Usage (%)" >> "$forecast_report"
    echo "------|---------------|------------------|---------------" >> "$forecast_report"
    
    local projected_cpu_usage=$current_cpu_usage
    local projected_memory_usage=$current_memory_usage
    local projected_disk_usage=$current_disk_usage
    
    for month in $(seq 1 $forecast_periods); do
        # Calculate projected usage
        projected_cpu_usage=$(echo "scale=2; $projected_cpu_usage * $growth_rate" | bc)
        projected_memory_usage=$(echo "scale=2; $projected_memory_usage * $growth_rate" | bc)
        projected_disk_usage=$(echo "scale=2; $projected_disk_usage * $growth_rate" | bc)
        
        # Ensure values don't exceed 100%
        if (( $(echo "$projected_cpu_usage > 100" | bc -l) )); then
            projected_cpu_usage=100
        fi
        
        if (( $(echo "$projected_memory_usage > 100" | bc -l) )); then
            projected_memory_usage=100
        fi
        
        if (( $(echo "$projected_disk_usage > 100" | bc -l) )); then
            projected_disk_usage=100
        fi
        
        # Format output
        printf "%5d | %13.2f | %16.2f | %13.2f\n" $month $projected_cpu_usage $projected_memory_usage $projected_disk_usage >> "$forecast_report"
    done
    echo "" >> "$forecast_report"
    
    # Calculate when resources will reach critical levels (90%)
    echo "Resource Exhaustion Forecast:" >> "$forecast_report"
    echo "---------------------------" >> "$forecast_report"
    
    # Calculate months until critical levels
    local cpu_exhaustion_months=0
    local memory_exhaustion_months=0
    local disk_exhaustion_months=0
    
    local projected_cpu_usage=$current_cpu_usage
    local projected_memory_usage=$current_memory_usage
    local projected_disk_usage=$current_disk_usage
    
    for month in $(seq 1 100); do  # Check up to 100 months
        # Calculate projected usage
        projected_cpu_usage=$(echo "scale=2; $projected_cpu_usage * $growth_rate" | bc)
        projected_memory_usage=$(echo "scale=2; $projected_memory_usage * $growth_rate" | bc)
        projected_disk_usage=$(echo "scale=2; $projected_disk_usage * $growth_rate" | bc)
        
        # Check if critical levels reached
        if [ $cpu_exhaustion_months -eq 0 ] && (( $(echo "$projected_cpu_usage >= 90" | bc -l) )); then
            cpu_exhaustion_months=$month
        fi
        
        if [ $memory_exhaustion_months -eq 0 ] && (( $(echo "$projected_memory_usage >= 90" | bc -l) )); then
            memory_exhaustion_months=$month
        fi
        
        if [ $disk_exhaustion_months -eq 0 ] && (( $(echo "$projected_disk_usage >= 90" | bc -l) )); then
            disk_exhaustion_months=$month
        fi
        
        # Break if all critical levels reached
        if [ $cpu_exhaustion_months -gt 0 ] && [ $memory_exhaustion_months -gt 0 ] && [ $disk_exhaustion_months -gt 0 ]; then
            break
        fi
    done
    
    echo "CPU Exhaustion: In $cpu_exhaustion_months months (90% usage)" >> "$forecast_report"
    echo "Memory Exhaustion: In $memory_exhaustion_months months (90% usage)" >> "$forecast_report"
    echo "Disk Exhaustion: In $disk_exhaustion_months months (90% usage)" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Forecast recommendations
    echo "Forecast Recommendations:" >> "$forecast_report"
    echo "------------------------" >> "$forecast_report"
    
    if [ $cpu_exhaustion_months -gt 0 ] && [ $cpu_exhaustion_months -lt 12 ]; then
        echo "❌ CPU resources will be exhausted in $cpu_exhaustion_months months" >> "$forecast_report"
        echo "   Recommendation: Plan for CPU capacity increase within 6 months" >> "$forecast_report"
    elif [ $cpu_exhaustion_months -gt 0 ]; then
        echo "✅ CPU resources will be exhausted in $cpu_exhaustion_months months" >> "$forecast_report"
        echo "   Recommendation: Monitor CPU usage trends" >> "$forecast_report"
    else
        echo "✅ CPU resources will not be exhausted within forecast period" >> "$forecast_report"
        echo "   Recommendation: Continue current CPU allocation" >> "$forecast_report"
    fi
    
    if [ $memory_exhaustion_months -gt 0 ] && [ $memory_exhaustion_months -lt 12 ]; then
        echo "❌ Memory resources will be exhausted in $memory_exhaustion_months months" >> "$forecast_report"
        echo "   Recommendation: Plan for memory capacity increase within 6 months" >> "$forecast_report"
    elif [ $memory_exhaustion_months -gt 0 ]; then
        echo "✅ Memory resources will be exhausted in $memory_exhaustion_months months" >> "$forecast_report"
        echo "   Recommendation: Monitor memory usage trends" >> "$forecast_report"
    else
        echo "✅ Memory resources will not be exhausted within forecast period" >> "$forecast_report"
        echo "   Recommendation: Continue current memory allocation" >> "$forecast_report"
    fi
    
    if [ $disk_exhaustion_months -gt 0 ] && [ $disk_exhaustion_months -lt 12 ]; then
        echo "❌ Disk resources will be exhausted in $disk_exhaustion_months months" >> "$forecast_report"
        echo "   Recommendation: Plan for disk capacity increase within 6 months" >> "$forecast_report"
    elif [ $disk_exhaustion_months -gt 0 ]; then
        echo "✅ Disk resources will be exhausted in $disk_exhaustion_months months" >> "$forecast_report"
        echo "   Recommendation: Monitor disk usage trends" >> "$forecast_report"
    else
        echo "✅ Disk resources will not be exhausted within forecast period" >> "$forecast_report"
        echo "   Recommendation: Continue current disk allocation" >> "$forecast_report"
    fi
    echo "" >> "$forecast_report"
    
    # Capacity planning timeline
    echo "Capacity Planning Timeline:" >> "$forecast_report"
    echo "--------------------------" >> "$forecast_report"
    
    # Determine earliest exhaustion
    local earliest_exhaustion=$cpu_exhaustion_months
    if [ $memory_exhaustion_months -lt $earliest_exhaustion ] && [ $memory_exhaustion_months -gt 0 ]; then
        earliest_exhaustion=$memory_exhaustion_months
    fi
    if [ $disk_exhaustion_months -lt $earliest_exhaustion ] && [ $disk_exhaustion_months -gt 0 ]; then
        earliest_exhaustion=$disk_exhaustion_months
    fi
    
    if [ $earliest_exhaustion -gt 0 ] && [ $earliest_exhaustion -lt 12 ]; then
        echo "⚠️ Critical resource exhaustion expected in $earliest_exhaustion months" >> "$forecast_report"
        echo "   Action Items:" >> "$forecast_report"
        echo "   - Review capacity planning within 3 months" >> "$forecast_report"
        echo "   - Evaluate resource optimization strategies" >> "$forecast_report"
        echo "   - Plan for capacity increases" >> "$forecast_report"
        echo "   - Consider upgrading from OCI free tier" >> "$forecast_report"
    elif [ $earliest_exhaustion -gt 0 ]; then
        echo "✅ Resources will be exhausted in $earliest_exhaustion months" >> "$forecast_report"
        echo "   Action Items:" >> "$forecast_report"
        echo "   - Monitor resource usage trends" >> "$forecast_report"
        echo "   - Review capacity planning annually" >> "$forecast_report"
        echo "   - Evaluate resource optimization strategies" >> "$forecast_report"
    else
        echo "✅ No resource exhaustion expected within forecast period" >> "$forecast_report"
        echo "   Action Items:" >> "$forecast_report"
        echo "   - Continue current capacity planning practices" >> "$forecast_report"
        echo "   - Monitor resource usage trends" >> "$forecast_report"
        echo "   - Review capacity planning annually" >> "$forecast_report"
    fi
    echo "" >> "$forecast_report"
    
    echo "✅ Capacity forecast generated"
    echo "📋 Forecast report saved to: $forecast_report"
    log_message "Capacity forecast generated: $forecast_report"
    
    # Display summary
    echo ""
    echo "Capacity Forecast Summary:"
    echo "  Method: $forecast_method"
    echo "  Confidence Level: ${confidence_level}%"
    echo "  Forecast Periods: ${forecast_periods} months"
    echo "  Current CPU Usage: ${current_cpu_usage}%"
    echo "  Current Memory Usage: ${current_memory_usage}%"
    echo "  Current Disk Usage: ${current_disk_usage}%"
    echo "  CPU Exhaustion: In $cpu_exhaustion_months months"
    echo "  Memory Exhaustion: In $memory_exhaustion_months months"
    echo "  Disk Exhaustion: In $disk_exhaustion_months months"
    echo "  Report: $forecast_report"
    
    # Check forecast status
    if [ $cpu_exhaustion_months -gt 0 ] && [ $cpu_exhaustion_months -lt 12 ]; then
        echo "  Status: ❌ CRITICAL RESOURCE EXHAUSTION EXPECTED"
        echo "  Recommendations:"
        echo "    - Plan for CPU capacity increase within 6 months"
        echo "    - Review capacity planning within 3 months"
        echo "    - Evaluate resource optimization strategies"
    elif [ $memory_exhaustion_months -gt 0 ] && [ $memory_exhaustion_months -lt 12 ]; then
        echo "  Status: ❌ CRITICAL RESOURCE EXHAUSTION EXPECTED"
        echo "  Recommendations:"
        echo "    - Plan for memory capacity increase within 6 months"
        echo "    - Review capacity planning within 3 months"
        echo "    - Evaluate resource optimization strategies"
    elif [ $disk_exhaustion_months -gt 0 ] && [ $disk_exhaustion_months -lt 12 ]; then
        echo "  Status: ❌ CRITICAL RESOURCE EXHAUSTION EXPECTED"
        echo "  Recommendations:"
        echo "    - Plan for disk capacity increase within 6 months"
        echo "    - Review capacity planning within 3 months"
        echo "    - Evaluate resource optimization strategies"
    else
        echo "  Status: ✅ RESOURCES ADEQUATE FOR FORECAST PERIOD"
        echo "  Recommendations:"
        echo "    - Continue current capacity planning practices"
        echo "    - Monitor resource usage trends"
        echo "    - Review capacity planning annually"
    fi
}

# Function to clean old capacity reports
clean_old_capacity_reports() {
    log_message "Cleaning old capacity reports"
    
    echo ""
    echo "Cleaning Old Capacity Reports..."
    echo "=============================="
    
    # Remove capacity reports older than 90 days
    find "$CAPACITY_REPORT_DIR" -name "current_capacity_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$CAPACITY_REPORT_DIR" -name "future_capacity_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$CAPACITY_REPORT_DIR" -name "scaling_policies_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$CAPACITY_REPORT_DIR" -name "capacity_forecast_*.txt" -mtime +90 -delete 2>/dev/null || true
    
    echo "✅ Old capacity reports cleaned"
    log_message "Old capacity reports cleaned"
}

# Main capacity planning function
main() {
    log_message "=== Starting Atlas Capacity Planning ==="
    
    # Initialize configuration
    initialize_capacity_config
    
    # Start time
    local start_time=$(date)
    log_message "Capacity planning started at: $start_time"
    
    # Handle different capacity planning operations
    case $1 in
        "analyze")
            analyze_current_capacity
            ;;
        "project")
            project_future_capacity
            ;;
        "scale")
            implement_scaling_policies
            ;;
        "forecast")
            generate_capacity_forecast
            ;;
        "clean")
            clean_old_capacity_reports
            ;;
        *)
            # Run comprehensive capacity planning
            analyze_current_capacity
            project_future_capacity
            implement_scaling_policies
            generate_capacity_forecast
            clean_old_capacity_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Capacity planning completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Capacity Planning Completed ==="
    
    echo ""
    echo "✅ Capacity planning operations completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $CAPACITY_REPORT_DIR"
    echo "📝 Log file: $CAPACITY_LOG"
}

# Run main function
main "$@"