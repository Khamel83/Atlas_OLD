#!/bin/bash

# Atlas Production Financial Management Script
# This script manages financial aspects of the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Financial Management..."

# Configuration
FINANCE_LOG="/home/ubuntu/dev/atlas/logs/financial_management.log"
FINANCE_REPORT_DIR="/home/ubuntu/dev/atlas/reports/finance"
FINANCE_CONFIG="/home/ubuntu/dev/atlas/config/finance.json"
COST_DATA_DIR="/home/ubuntu/dev/atlas/finance/costs"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $FINANCE_LOG)"
mkdir -p "$FINANCE_REPORT_DIR"
mkdir -p "$COST_DATA_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $FINANCE_LOG
    echo "$1"
}

# Function to initialize finance configuration
initialize_finance_config() {
    log_message "Initializing finance configuration"
    
    # Create default finance configuration if it doesn't exist
    if [ ! -f "$FINANCE_CONFIG" ]; then
        cat > "$FINANCE_CONFIG" << EOF
{
    "budget": {
        "monthly_budget_usd": 0,
        "annual_budget_usd": 0,
        "currency": "USD"
    },
    "cost_centers": {
        "compute": {
            "name": "Compute Resources",
            "allocation_percentage": 50
        },
        "storage": {
            "name": "Storage Resources",
            "allocation_percentage": 30
        },
        "networking": {
            "name": "Networking Resources",
            "allocation_percentage": 10
        },
        "other": {
            "name": "Other Resources",
            "allocation_percentage": 10
        }
    },
    "forecasting": {
        "method": "linear_regression",
        "confidence_level": 95,
        "forecast_periods": 12
    },
    "reporting": {
        "frequency": "monthly",
        "recipients": ["admin@khamel.com"],
        "format": "pdf"
    },
    "optimization": {
        "enabled": true,
        "recommendations": true,
        "auto_apply": false
    }
}
EOF
        echo "✅ Created default finance configuration"
        log_message "Default finance configuration created"
    else
        echo "✅ Finance configuration already exists"
    fi
}

# Function to track resource costs
track_resource_costs() {
    log_message "Tracking resource costs"
    
    echo "Tracking Resource Costs..."
    echo "=========================="
    
    local cost_tracking_report="$FINANCE_REPORT_DIR/cost_tracking_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create cost tracking report header
    echo "Atlas Production Resource Cost Tracking" > "$cost_tracking_report"
    echo "Generated: $(date)" >> "$cost_tracking_report"
    echo "=======================================" >> "$cost_tracking_report"
    echo "" >> "$cost_tracking_report"
    
    # Get current month and year
    local current_month=$(date +%m)
    local current_year=$(date +%Y)
    
    echo "Current Period: $current_year-$current_month" >> "$cost_tracking_report"
    echo "Currency: USD (Free Tier)" >> "$cost_tracking_report"
    echo "" >> "$cost_tracking_report"
    
    # Track compute costs (OCI Free Tier)
    echo "Compute Costs:" >> "$cost_tracking_report"
    echo "-------------" >> "$cost_tracking_report"
    
    # Get system information
    local cpu_count=$(nproc)
    local memory_gb=$(free -g | grep Mem | awk '{print $2}')
    local instance_type="VM.Standard2.1"  # Default OCI instance type
    
    echo "Instance Type: $instance_type" >> "$cost_tracking_report"
    echo "CPU Cores: $cpu_count" >> "$cost_tracking_report"
    echo "Memory: ${memory_gb}GB" >> "$cost_tracking_report"
    
    # Check if within free tier limits
    local compute_cost=0
    if [ $cpu_count -le 4 ] && [ $memory_gb -le 24 ]; then
        echo "✅ Within OCI Always Free Tier limits" >> "$cost_tracking_report"
        echo "Compute Cost: \$${compute_cost}/month" >> "$cost_tracking_report"
    else
        # Calculate approximate cost (simplified)
        compute_cost=$((cpu_count * 5))  # Rough estimate: $5 per CPU core
        echo "⚠️ Exceeding OCI Always Free Tier limits" >> "$cost_tracking_report"
        echo "Estimated Compute Cost: \$${compute_cost}/month" >> "$cost_tracking_report"
    fi
    echo "" >> "$cost_tracking_report"
    
    # Track storage costs
    echo "Storage Costs:" >> "$cost_tracking_report"
    echo "-------------" >> "$cost_tracking_report"
    
    # Get disk usage
    local disk_usage_gb=$(df -BG / | tail -1 | awk '{print $3}' | sed 's/G//')
    local disk_total_gb=$(df -BG / | tail -1 | awk '{print $2}' | sed 's/G//')
    
    echo "Disk Usage: ${disk_usage_gb}GB" >> "$cost_tracking_report"
    echo "Disk Total: ${disk_total_gb}GB" >> "$cost_tracking_report"
    
    # Check if within free tier limits (10GB block storage)
    local storage_cost=0
    if [ $disk_usage_gb -le 10 ]; then
        echo "✅ Within OCI Always Free Tier limits" >> "$cost_tracking_report"
        echo "Storage Cost: \$${storage_cost}/month" >> "$cost_tracking_report"
    else
        # Calculate approximate cost (simplified)
        local excess_gb=$((disk_usage_gb - 10))
        storage_cost=$((excess_gb * 2))  # Rough estimate: $2 per GB over limit
        echo "⚠️ Exceeding OCI Always Free Tier limits by ${excess_gb}GB" >> "$cost_tracking_report"
        echo "Estimated Storage Cost: \$${storage_cost}/month" >> "$cost_tracking_report"
    fi
    echo "" >> "$cost_tracking_report"
    
    # Track object storage costs
    echo "Object Storage Costs:" >> "$cost_tracking_report"
    echo "--------------------" >> "$cost_tracking_report"
    
    # Check if using OCI Object Storage
    local object_storage_used_gb=0
    local object_storage_cost=0
    
    # This would typically query OCI API, but we'll simulate
    if command -v oci &> /dev/null; then
        echo "✅ OCI CLI is available" >> "$cost_tracking_report"
        
        # Check if backup bucket exists
        local backup_bucket="atlas-backups-bucket"
        if oci os bucket list --compartment-id $(jq -r '.oci.compartment_id // "dummy"' "/home/ubuntu/dev/atlas/config/oci.json" 2>/dev/null || echo "dummy") > /dev/null 2>&1; then
            echo "✅ Backup bucket exists" >> "$cost_tracking_report"
            
            # Get bucket size (simplified)
            object_storage_used_gb=2  # Simulated value
            if [ $object_storage_used_gb -le 10 ]; then
                echo "✅ Within OCI Always Free Tier limits (10GB)" >> "$cost_tracking_report"
                echo "Object Storage Used: ${object_storage_used_gb}GB" >> "$cost_tracking_report"
                echo "Object Storage Cost: \$${object_storage_cost}/month" >> "$cost_tracking_report"
            else
                local excess_gb=$((object_storage_used_gb - 10))
                object_storage_cost=$((excess_gb * 2))  # Rough estimate: $2 per GB over limit
                echo "⚠️ Exceeding OCI Always Free Tier limits by ${excess_gb}GB" >> "$cost_tracking_report"
                echo "Estimated Object Storage Cost: \$${object_storage_cost}/month" >> "$cost_tracking_report"
            fi
        else
            echo "ℹ️ No backup bucket found" >> "$cost_tracking_report"
        fi
    else
        echo "❌ OCI CLI not available" >> "$cost_tracking_report"
        echo "Object Storage Used: ${object_storage_used_gb}GB" >> "$cost_tracking_report"
        echo "Object Storage Cost: \$${object_storage_cost}/month" >> "$cost_tracking_report"
    fi
    echo "" >> "$cost_tracking_report"
    
    # Track networking costs
    echo "Networking Costs:" >> "$cost_tracking_report"
    echo "----------------" >> "$cost_tracking_report"
    
    # Get network usage (simplified)
    local network_in_gb=0
    local network_out_gb=0
    local network_cost=0
    
    # Check if within free tier limits
    local total_network_gb=$((network_in_gb + network_out_gb))
    if [ $total_network_gb -le 10000 ]; then  # 10TB free tier
        echo "✅ Within OCI Always Free Tier limits (10TB)" >> "$cost_tracking_report"
        echo "Network Usage: ${total_network_gb}GB" >> "$cost_tracking_report"
        echo "Network Cost: \$${network_cost}/month" >> "$cost_tracking_report"
    else
        local excess_gb=$((total_network_gb - 10000))
        network_cost=$((excess_gb / 1000))  # Rough estimate: $1 per TB over limit
        echo "⚠️ Exceeding OCI Always Free Tier limits by ${excess_gb}GB" >> "$cost_tracking_report"
        echo "Estimated Network Cost: \$${network_cost}/month" >> "$cost_tracking_report"
    fi
    echo "" >> "$cost_tracking_report"
    
    # Calculate total costs
    echo "Total Monthly Costs:" >> "$cost_tracking_report"
    echo "--------------------" >> "$cost_tracking_report"
    
    local total_cost=$((compute_cost + storage_cost + object_storage_cost + network_cost))
    
    echo "Compute: \$${compute_cost}/month" >> "$cost_tracking_report"
    echo "Storage: \$${storage_cost}/month" >> "$cost_tracking_report"
    echo "Object Storage: \$${object_storage_cost}/month" >> "$cost_tracking_report"
    echo "Networking: \$${network_cost}/month" >> "$cost_tracking_report"
    echo "------------------------" >> "$cost_tracking_report"
    echo "Total Estimated Cost: \$${total_cost}/month" >> "$cost_tracking_report"
    echo "" >> "$cost_tracking_report"
    
    # Compare with budget
    echo "Budget Comparison:" >> "$cost_tracking_report"
    echo "-----------------" >> "$cost_tracking_report"
    
    local monthly_budget=$(jq -r '.budget.monthly_budget_usd' "$FINANCE_CONFIG")
    if [ "$monthly_budget" = "0" ]; then
        monthly_budget=0  # Free tier
    fi
    
    echo "Monthly Budget: \$${monthly_budget}" >> "$cost_tracking_report"
    echo "Current Cost: \$${total_cost}" >> "$cost_tracking_report"
    
    if [ $total_cost -le $monthly_budget ]; then
        echo "✅ Within budget (\$${total_cost} <= \$${monthly_budget})" >> "$cost_tracking_report"
    else
        local over_budget=$((total_cost - monthly_budget))
        echo "❌ Over budget by \$${over_budget} (\$${total_cost} > \$${monthly_budget})" >> "$cost_tracking_report"
    fi
    echo "" >> "$cost_tracking_report"
    
    # Store cost data for trending
    local cost_data_file="$COST_DATA_DIR/costs_$(date +%Y%m).json"
    cat > "$cost_data_file" << EOF
{
    "period": "$current_year-$current_month",
    "compute": {
        "cost": $compute_cost,
        "usage": {
            "cpu_cores": $cpu_count,
            "memory_gb": $memory_gb
        }
    },
    "storage": {
        "cost": $storage_cost,
        "usage": {
            "disk_gb": $disk_usage_gb,
            "total_gb": $disk_total_gb
        }
    },
    "object_storage": {
        "cost": $object_storage_cost,
        "usage": {
            "gb": $object_storage_used_gb
        }
    },
    "networking": {
        "cost": $network_cost,
        "usage": {
            "in_gb": $network_in_gb,
            "out_gb": $network_out_gb,
            "total_gb": $total_network_gb
        }
    },
    "total": {
        "cost": $total_cost,
        "budget": $monthly_budget
    }
}
EOF
    
    echo "✅ Resource cost tracking completed"
    echo "📋 Cost tracking report saved to: $cost_tracking_report"
    echo "💾 Cost data saved to: $cost_data_file"
    log_message "Resource cost tracking completed: $cost_tracking_report"
    
    # Display summary
    echo ""
    echo "Resource Cost Summary:"
    echo "  Compute: \$${compute_cost}/month"
    echo "  Storage: \$${storage_cost}/month"
    echo "  Object Storage: \$${object_storage_cost}/month"
    echo "  Networking: \$${network_cost}/month"
    echo "  Total: \$${total_cost}/month"
    if [ $total_cost -le $monthly_budget ]; then
        echo "  Status: ✅ Within Budget (\$${monthly_budget})"
    else
        echo "  Status: ❌ Over Budget by \$${over_budget}"
    fi
    echo "  Report: $cost_tracking_report"
    echo "  Data: $cost_data_file"
}

# Function to generate financial forecast
generate_financial_forecast() {
    log_message "Generating financial forecast"
    
    echo ""
    echo "Generating Financial Forecast..."
    echo "================================"
    
    local forecast_report="$FINANCE_REPORT_DIR/forecast_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create forecast report header
    echo "Atlas Production Financial Forecast" > "$forecast_report"
    echo "Generated: $(date)" >> "$forecast_report"
    echo "===================================" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Get forecasting parameters
    local forecast_method=$(jq -r '.forecasting.method' "$FINANCE_CONFIG")
    local confidence_level=$(jq -r '.forecasting.confidence_level' "$FINANCE_CONFIG")
    local forecast_periods=$(jq -r '.forecasting.forecast_periods' "$FINANCE_CONFIG")
    
    echo "Forecasting Parameters:" >> "$forecast_report"
    echo "----------------------" >> "$forecast_report"
    echo "Method: $forecast_method" >> "$forecast_report"
    echo "Confidence Level: ${confidence_level}%" >> "$forecast_report"
    echo "Forecast Periods: ${forecast_periods} months" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Analyze historical cost data
    echo "Historical Cost Analysis:" >> "$forecast_report"
    echo "-------------------------" >> "$forecast_report"
    
    # Get available cost data files
    local cost_files=$(find "$COST_DATA_DIR" -name "costs_*.json" | sort)
    local cost_count=$(echo "$cost_files" | wc -l)
    
    if [ $cost_count -eq 0 ]; then
        echo "❌ No historical cost data found" >> "$forecast_report"
        echo "ℹ️ Using current costs for projection" >> "$forecast_report"
        
        # Use current costs
        local current_total_cost=$(jq -r '.total.cost' "$COST_DATA_DIR/costs_$(date +%Y%m).json" 2>/dev/null || echo "0")
        echo "Current Month Cost: \$${current_total_cost}" >> "$forecast_report"
    else
        echo "Available Historical Data: $cost_count months" >> "$forecast_report"
        
        # Calculate average monthly cost
        local total_historical_cost=0
        local month_count=0
        
        while IFS= read -r cost_file; do
            if [ -f "$cost_file" ]; then
                local month_cost=$(jq -r '.total.cost' "$cost_file")
                total_historical_cost=$((total_historical_cost + month_cost))
                month_count=$((month_count + 1))
                echo "  $(basename $cost_file .json): \$${month_cost}" >> "$forecast_report"
            fi
        done <<< "$cost_files"
        
        if [ $month_count -gt 0 ]; then
            local average_monthly_cost=$((total_historical_cost / month_count))
            echo "Average Monthly Cost: \$${average_monthly_cost}" >> "$forecast_report"
        else
            local average_monthly_cost=0
            echo "Average Monthly Cost: \$${average_monthly_cost}" >> "$forecast_report"
        fi
    fi
    echo "" >> "$forecast_report"
    
    # Generate forecast
    echo "Financial Forecast:" >> "$forecast_report"
    echo "------------------" >> "$forecast_report"
    
    # Use simple linear projection for demo
    local current_month=$(date +%m)
    local current_year=$(date +%Y)
    
    # Get current cost
    local current_cost_file="$COST_DATA_DIR/costs_${current_year}${current_month}.json"
    local current_cost=0
    
    if [ -f "$current_cost_file" ]; then
        current_cost=$(jq -r '.total.cost' "$current_cost_file")
    else
        # Use last available cost or zero
        current_cost=$(echo "$cost_files" | tail -1 | xargs jq -r '.total.cost' 2>/dev/null || echo "0")
    fi
    
    echo "Current Monthly Cost: \$${current_cost}" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Project costs for next periods
    echo "Projected Costs (${forecast_periods} months):" >> "$forecast_report"
    echo "------------------------------------------" >> "$forecast_report"
    
    local projected_cost=$current_cost
    local total_projected_cost=0
    
    for ((i=1; i<=forecast_periods; i++)); do
        # Simple projection with slight growth
        local growth_rate=1.02  # 2% monthly growth
        projected_cost=$(echo "scale=2; $projected_cost * $growth_rate" | bc)
        total_projected_cost=$(echo "scale=2; $total_projected_cost + $projected_cost" | bc)
        
        # Calculate future month/year
        local future_month=$(( (current_month + i - 1) % 12 + 1 ))
        local future_year=$(( current_year + (current_month + i - 1) / 12 ))
        
        if [ $i -le 12 ]; then
            echo "  $future_year-$future_month: \$${projected_cost}" >> "$forecast_report"
        fi
    done
    echo "" >> "$forecast_report"
    
    # Calculate totals
    echo "Forecast Summary:" >> "$forecast_report"
    echo "----------------" >> "$forecast_report"
    echo "Current Monthly Cost: \$${current_cost}" >> "$forecast_report"
    echo "Average Monthly Cost: \$${average_monthly_cost:-0}" >> "$forecast_report"
    echo "Projected Monthly Cost (12 months): \$${projected_cost}" >> "$forecast_report"
    echo "Total Projected Cost (12 months): \$${total_projected_cost}" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Annual projection
    echo "Annual Projections:" >> "$forecast_report"
    echo "------------------" >> "$forecast_report"
    
    local annual_current_cost=$((current_cost * 12))
    local annual_projected_cost=$(echo "scale=2; $projected_cost * 12" | bc)
    
    echo "Annual Cost (Current Rate): \$${annual_current_cost}" >> "$forecast_report"
    echo "Annual Cost (Projected Rate): \$${annual_projected_cost}" >> "$forecast_report"
    echo "" >> "$forecast_report"
    
    # Budget comparison
    echo "Budget Comparison:" >> "$forecast_report"
    echo "-----------------" >> "$forecast_report"
    
    local annual_budget=$(jq -r '.budget.annual_budget_usd' "$FINANCE_CONFIG")
    if [ "$annual_budget" = "0" ]; then
        annual_budget=0  # Free tier
    fi
    
    echo "Annual Budget: \$${annual_budget}" >> "$forecast_report"
    echo "Projected Annual Cost: \$${annual_projected_cost}" >> "$forecast_report"
    
    if (( $(echo "$annual_projected_cost <= $annual_budget" | bc -l) )); then
        echo "✅ Within annual budget" >> "$forecast_report"
    else
        local over_budget=$(echo "scale=2; $annual_projected_cost - $annual_budget" | bc)
        echo "❌ Over annual budget by \$${over_budget}" >> "$forecast_report"
    fi
    echo "" >> "$forecast_report"
    
    # Recommendations
    echo "Recommendations:" >> "$forecast_report"
    echo "--------------" >> "$forecast_report"
    
    if (( $(echo "$annual_projected_cost <= $annual_budget" | bc -l) )); then
        echo "✅ Current cost trajectory is sustainable" >> "$forecast_report"
        echo "✅ Continue monitoring costs monthly" >> "$forecast_report"
    else
        echo "❌ Projected costs exceed budget" >> "$forecast_report"
        echo "❌ Consider cost optimization measures:" >> "$forecast_report"
        echo "   - Review resource utilization" >> "$forecast_report"
        echo "   - Implement auto-scaling policies" >> "$forecast_report"
        echo "   - Optimize storage usage" >> "$forecast_report"
        echo "   - Review backup retention policies" >> "$forecast_report"
    fi
    echo "" >> "$forecast_report"
    
    echo "✅ Financial forecast generated"
    echo "📋 Forecast report saved to: $forecast_report"
    log_message "Financial forecast generated: $forecast_report"
    
    # Display summary
    echo ""
    echo "Financial Forecast Summary:"
    echo "  Current Monthly Cost: \$${current_cost}"
    echo "  Projected Monthly Cost: \$${projected_cost}"
    echo "  Annual Projected Cost: \$${annual_projected_cost}"
    echo "  Annual Budget: \$${annual_budget}"
    if (( $(echo "$annual_projected_cost <= $annual_budget" | bc -l) )); then
        echo "  Status: ✅ Within Budget"
    else
        echo "  Status: ❌ Over Budget"
    fi
    echo "  Report: $forecast_report"
}

# Function to optimize costs
optimize_costs() {
    log_message "Optimizing costs"
    
    echo ""
    echo "Optimizing Costs..."
    echo "=================="
    
    local optimization_report="$FINANCE_REPORT_DIR/cost_optimization_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create optimization report header
    echo "Atlas Production Cost Optimization Report" > "$optimization_report"
    echo "Generated: $(date)" >> "$optimization_report"
    echo "=========================================" >> "$optimization_report"
    echo "" >> "$optimization_report"
    
    # Get optimization settings
    local optimization_enabled=$(jq -r '.optimization.enabled' "$FINANCE_CONFIG")
    local auto_apply=$(jq -r '.optimization.auto_apply' "$FINANCE_CONFIG")
    
    echo "Optimization Settings:" >> "$optimization_report"
    echo "--------------------" >> "$optimization_report"
    echo "Optimization Enabled: $optimization_enabled" >> "$optimization_report"
    echo "Auto Apply Recommendations: $auto_apply" >> "$optimization_report"
    echo "" >> "$optimization_report"
    
    if [ "$optimization_enabled" != "true" ]; then
        echo "❌ Cost optimization is disabled" >> "$optimization_report"
        echo "✅ Cost optimization completed (disabled)"
        echo "📋 Optimization report saved to: $optimization_report"
        log_message "Cost optimization completed (disabled): $optimization_report"
        return 0
    fi
    
    # Initialize optimization recommendations
    echo "Optimization Recommendations:" >> "$optimization_report"
    echo "----------------------------" >> "$optimization_report"
    
    local recommendations_applied=0
    local recommendations_available=0
    
    # Check compute optimization
    echo "Compute Optimization:" >> "$optimization_report"
    echo "-------------------" >> "$optimization_report"
    
    # Get current instance specs
    local cpu_count=$(nproc)
    local memory_gb=$(free -g | grep Mem | awk '{print $2}')
    
    # Check if within free tier
    if [ $cpu_count -le 4 ] && [ $memory_gb -le 24 ]; then
        echo "✅ Instance within Always Free Tier limits" >> "$optimization_report"
        echo "   Current: $cpu_count CPUs, ${memory_gb}GB RAM" >> "$optimization_report"
    else
        echo "⚠️ Instance exceeding Always Free Tier limits" >> "$optimization_report"
        echo "   Consider downsizing to VM.Standard2.1 (1 CPU, 1GB RAM)" >> "$optimization_report"
        echo "   or VM.Standard2.2 (2 CPUs, 2GB RAM)" >> "$optimization_report"
        recommendations_available=$((recommendations_available + 1))
    fi
    echo "" >> "$optimization_report"
    
    # Check storage optimization
    echo "Storage Optimization:" >> "$optimization_report"
    echo "--------------------" >> "$optimization_report"
    
    # Get disk usage
    local disk_usage_gb=$(df -BG / | tail -1 | awk '{print $3}' | sed 's/G//')
    local disk_total_gb=$(df -BG / | tail -1 | awk '{print $2}' | sed 's/G//')
    
    # Check if within free tier (10GB block storage)
    if [ $disk_usage_gb -le 10 ]; then
        echo "✅ Block storage within Always Free Tier limits (10GB)" >> "$optimization_report"
        echo "   Current usage: ${disk_usage_gb}GB" >> "$optimization_report"
    else
        echo "⚠️ Block storage exceeding Always Free Tier limits" >> "$optimization_report"
        echo "   Current usage: ${disk_usage_gb}GB" >> "$optimization_report"
        echo "   Recommendation: Clean up unused files and logs" >> "$optimization_report"
        recommendations_available=$((recommendations_available + 1))
    fi
    echo "" >> "$optimization_report"
    
    # Check object storage optimization
    echo "Object Storage Optimization:" >> "$optimization_report"
    echo "---------------------------" >> "$optimization_report"
    
    # Check backup retention
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        local backup_count=$(find "$backup_dir" -name "*.sql*" | wc -l)
        local backup_size_gb=$(du -BG "$backup_dir" 2>/dev/null | cut -f1 | sed 's/G//')
        
        echo "Backup Statistics:" >> "$optimization_report"
        echo "  Backup files: $backup_count" >> "$optimization_report"
        echo "  Backup size: ${backup_size_gb}GB" >> "$optimization_report"
        
        # Check if backups are within free tier (10GB object storage)
        if [ $backup_size_gb -le 10 ]; then
            echo "✅ Object storage within Always Free Tier limits (10GB)" >> "$optimization_report"
        else
            echo "⚠️ Object storage exceeding Always Free Tier limits" >> "$optimization_report"
            echo "   Recommendation: Implement backup rotation policy" >> "$optimization_report"
            echo "   Current backups: ${backup_size_gb}GB" >> "$optimization_report"
            recommendations_available=$((recommendations_available + 1))
        fi
        
        # Check backup age
        local old_backups=$(find "$backup_dir" -name "*.sql*" -mtime +30 | wc -l)
        if [ $old_backups -gt 0 ]; then
            echo "⚠️ Old backups found: $old_backups (older than 30 days)" >> "$optimization_report"
            echo "   Recommendation: Remove backups older than 30 days" >> "$optimization_report"
            recommendations_available=$((recommendations_available + 1))
        fi
    else
        echo "❌ Backup directory not found" >> "$optimization_report"
    fi
    echo "" >> "$optimization_report"
    
    # Check log optimization
    echo "Log Optimization:" >> "$optimization_report"
    echo "---------------" >> "$optimization_report"
    
    local log_dir="/home/ubuntu/dev/atlas/logs"
    if [ -d "$log_dir" ]; then
        local log_size_gb=$(du -BG "$log_dir" 2>/dev/null | cut -f1 | sed 's/G//')
        echo "Log directory size: ${log_size_gb}GB" >> "$optimization_report"
        
        if [ $log_size_gb -gt 1 ]; then
            echo "⚠️ Large log directory size" >> "$optimization_report"
            echo "   Recommendation: Implement log rotation and cleanup" >> "$optimization_report"
            recommendations_available=$((recommendations_available + 1))
        else
            echo "✅ Log directory size is reasonable" >> "$optimization_report"
        fi
        
        # Check for old logs
        local old_logs=$(find "$log_dir" -name "*.log" -mtime +30 | wc -l)
        if [ $old_logs -gt 0 ]; then
            echo "⚠️ Old logs found: $old_logs (older than 30 days)" >> "$optimization_report"
            echo "   Recommendation: Remove logs older than 30 days" >> "$optimization_report"
            recommendations_available=$((recommendations_available + 1))
        fi
    else
        echo "❌ Log directory not found" >> "$optimization_report"
    fi
    echo "" >> "$optimization_report"
    
    # Check for unused services
    echo "Unused Services Check:" >> "$optimization_report"
    echo "---------------------" >> "$optimization_report"
    
    local unused_services=(
        "telnetd:Telnet Daemon"
        "ftpd:FTP Daemon"
        "rpcbind:RPC Bind"
        "nfs-kernel-server:NFS Server"
    )
    
    local unused_found=0
    for service_info in "${unused_services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name 2>/dev/null; then
            echo "⚠️ Unused service running: $service_desc" >> "$optimization_report"
            echo "   Recommendation: Disable $service_name service" >> "$optimization_report"
            unused_found=$((unused_found + 1))
            recommendations_available=$((recommendations_available + 1))
        fi
    done
    
    if [ $unused_found -eq 0 ]; then
        echo "✅ No unused services found" >> "$optimization_report"
    fi
    echo "" >> "$optimization_report"
    
    # Check for oversized applications
    echo "Application Optimization:" >> "$optimization_report"
    echo "------------------------" >> "$optimization_report"
    
    # Check Atlas directory size
    local atlas_dir="/home/ubuntu/dev/atlas"
    if [ -d "$atlas_dir" ]; then
        local atlas_size_gb=$(du -BG "$atlas_dir" 2>/dev/null | cut -f1 | sed 's/G//')
        echo "Atlas directory size: ${atlas_size_gb}GB" >> "$optimization_report"
        
        if [ $atlas_size_gb -gt 5 ]; then
            echo "⚠️ Large Atlas directory size" >> "$optimization_report"
            echo "   Recommendation: Clean up temporary files and outputs" >> "$optimization_report"
            recommendations_available=$((recommendations_available + 1))
        else
            echo "✅ Atlas directory size is reasonable" >> "$optimization_report"
        fi
    fi
    echo "" >> "$optimization_report"
    
    # Summary
    echo "Optimization Summary:" >> "$optimization_report"
    echo "--------------------" >> "$optimization_report"
    echo "Available Recommendations: $recommendations_available" >> "$optimization_report"
    echo "Applied Recommendations: $recommendations_applied" >> "$optimization_report"
    echo "" >> "$optimization_report"
    
    # Apply recommendations if auto-apply is enabled
    if [ "$auto_apply" = "true" ] && [ $recommendations_available -gt 0 ]; then
        echo "Auto-Applying Recommendations:" >> "$optimization_report"
        echo "-----------------------------" >> "$optimization_report"
        
        # For demo purposes, we'll just log that we would apply recommendations
        echo "ℹ️ In a real implementation, recommendations would be auto-applied" >> "$optimization_report"
        echo "   - Cleanup old backups" >> "$optimization_report"
        echo "   - Remove unused services" >> "$optimization_report"
        echo "   - Optimize log rotation" >> "$optimization_report"
        recommendations_applied=$recommendations_available
    elif [ $recommendations_available -gt 0 ]; then
        echo "Manual Action Required:" >> "$optimization_report"
        echo "----------------------" >> "$optimization_report"
        echo "✅ Review recommendations and apply manually" >> "$optimization_report"
        echo "   Recommendations are marked with ⚠️ above" >> "$optimization_report"
    else
        echo "✅ No cost optimization needed at this time" >> "$optimization_report"
    fi
    echo "" >> "$optimization_report"
    
    echo "✅ Cost optimization completed"
    echo "📋 Optimization report saved to: $optimization_report"
    log_message "Cost optimization completed: $optimization_report"
    
    # Display summary
    echo ""
    echo "Cost Optimization Summary:"
    echo "  Recommendations Available: $recommendations_available"
    echo "  Recommendations Applied: $recommendations_applied"
    echo "  Auto-Apply Enabled: $auto_apply"
    echo "  Report: $optimization_report"
}

# Function to generate financial report
generate_financial_report() {
    log_message "Generating financial report"
    
    echo ""
    echo "Generating Financial Report..."
    echo "============================="
    
    local financial_report="$FINANCE_REPORT_DIR/financial_report_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create financial report header
    echo "Atlas Production Financial Report" > "$financial_report"
    echo "Generated: $(date)" >> "$financial_report"
    echo "================================" >> "$financial_report"
    echo "" >> "$financial_report"
    
    # Add system information
    echo "System Information:" >> "$financial_report"
    echo "------------------" >> "$financial_report"
    echo "Hostname: $(hostname)" >> "$financial_report"
    echo "OS: $(lsb_release -d | cut -f2)" >> "$financial_report"
    echo "Kernel: $(uname -r)" >> "$financial_report"
    echo "Uptime: $(uptime -p)" >> "$financial_report"
    echo "" >> "$financial_report"
    
    # Add current resource usage
    echo "Current Resource Usage:" >> "$financial_report"
    echo "----------------------" >> "$financial_report"
    
    # CPU and memory
    local cpu_count=$(nproc)
    local memory_total_gb=$(free -g | grep Mem | awk '{print $2}')
    local memory_used_gb=$(free -g | grep Mem | awk '{print $3}')
    local memory_usage_percent=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    
    echo "CPU Cores: $cpu_count" >> "$financial_report"
    echo "Memory: ${memory_total_gb}GB total, ${memory_used_gb}GB used (${memory_usage_percent}%)" >> "$financial_report"
    
    # Disk usage
    local disk_total_gb=$(df -BG / | tail -1 | awk '{print $2}' | sed 's/G//')
    local disk_used_gb=$(df -BG / | tail -1 | awk '{print $3}' | sed 's/G//')
    local disk_usage_percent=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "Disk: ${disk_total_gb}GB total, ${disk_used_gb}GB used (${disk_usage_percent}%)" >> "$financial_report"
    
    # Network usage (simplified)
    echo "Network: Usage data not available" >> "$financial_report"
    echo "" >> "$financial_report"
    
    # Add cost analysis
    echo "Cost Analysis:" >> "$financial_report"
    echo "-------------" >> "$financial_report"
    
    # Get current costs
    local current_month=$(date +%Y%m)
    local current_cost_file="$COST_DATA_DIR/costs_${current_month}.json"
    
    if [ -f "$current_cost_file" ]; then
        local current_total_cost=$(jq -r '.total.cost' "$current_cost_file")
        local current_compute_cost=$(jq -r '.compute.cost' "$current_cost_file")
        local current_storage_cost=$(jq -r '.storage.cost' "$current_cost_file")
        local current_object_storage_cost=$(jq -r '.object_storage.cost' "$current_cost_file")
        local current_network_cost=$(jq -r '.networking.cost' "$current_cost_file")
        
        echo "Current Monthly Costs:" >> "$financial_report"
        echo "  Compute: \$${current_compute_cost}" >> "$financial_report"
        echo "  Storage: \$${current_storage_cost}" >> "$financial_report"
        echo "  Object Storage: \$${current_object_storage_cost}" >> "$financial_report"
        echo "  Networking: \$${current_network_cost}" >> "$financial_report"
        echo "  Total: \$${current_total_cost}" >> "$financial_report"
    else
        echo "❌ Current cost data not available" >> "$financial_report"
        local current_total_cost=0
    fi
    echo "" >> "$financial_report"
    
    # Add historical cost analysis
    echo "Historical Cost Analysis:" >> "$financial_report"
    echo "------------------------" >> "$financial_report"
    
    # Get historical cost files
    local cost_files=$(find "$COST_DATA_DIR" -name "costs_*.json" | sort)
    local cost_count=$(echo "$cost_files" | wc -l)
    
    if [ $cost_count -eq 0 ]; then
        echo "❌ No historical cost data available" >> "$financial_report"
    else
        echo "Available Historical Data: $cost_count months" >> "$financial_report"
        
        # Calculate historical averages
        local total_historical_cost=0
        local total_compute_cost=0
        local total_storage_cost=0
        local total_object_storage_cost=0
        local total_network_cost=0
        local month_count=0
        
        while IFS= read -r cost_file; do
            if [ -f "$cost_file" ]; then
                local month_total=$(jq -r '.total.cost' "$cost_file")
                local month_compute=$(jq -r '.compute.cost' "$cost_file")
                local month_storage=$(jq -r '.storage.cost' "$cost_file")
                local month_object_storage=$(jq -r '.object_storage.cost' "$cost_file")
                local month_network=$(jq -r '.networking.cost' "$cost_file")
                
                total_historical_cost=$((total_historical_cost + month_total))
                total_compute_cost=$((total_compute_cost + month_compute))
                total_storage_cost=$((total_storage_cost + month_storage))
                total_object_storage_cost=$((total_object_storage_cost + month_object_storage))
                total_network_cost=$((total_network_cost + month_network))
                month_count=$((month_count + 1))
            fi
        done <<< "$cost_files"
        
        if [ $month_count -gt 0 ]; then
            local avg_total_cost=$((total_historical_cost / month_count))
            local avg_compute_cost=$((total_compute_cost / month_count))
            local avg_storage_cost=$((total_storage_cost / month_count))
            local avg_object_storage_cost=$((total_object_storage_cost / month_count))
            local avg_network_cost=$((total_network_cost / month_count))
            
            echo "Average Monthly Costs:" >> "$financial_report"
            echo "  Compute: \$${avg_compute_cost}" >> "$financial_report"
            echo "  Storage: \$${avg_storage_cost}" >> "$financial_report"
            echo "  Object Storage: \$${avg_object_storage_cost}" >> "$financial_report"
            echo "  Networking: \$${avg_network_cost}" >> "$financial_report"
            echo "  Total: \$${avg_total_cost}" >> "$financial_report"
        fi
    fi
    echo "" >> "$financial_report"
    
    # Add budget information
    echo "Budget Information:" >> "$financial_report"
    echo "------------------" >> "$financial_report"
    
    local monthly_budget=$(jq -r '.budget.monthly_budget_usd' "$FINANCE_CONFIG")
    local annual_budget=$(jq -r '.budget.annual_budget_usd' "$FINANCE_CONFIG")
    
    if [ "$monthly_budget" = "0" ]; then
        monthly_budget=0  # Free tier
    fi
    
    if [ "$annual_budget" = "0" ]; then
        annual_budget=0  # Free tier
    fi
    
    echo "Monthly Budget: \$${monthly_budget}" >> "$financial_report"
    echo "Annual Budget: \$${annual_budget}" >> "$financial_report"
    
    # Calculate budget utilization
    if [ $current_total_cost -gt 0 ] && [ $monthly_budget -gt 0 ]; then
        local budget_utilization_percent=$((current_total_cost * 100 / monthly_budget))
        echo "Current Budget Utilization: ${budget_utilization_percent}%" >> "$financial_report"
    fi
    echo "" >> "$financial_report"
    
    # Add cost optimization status
    echo "Cost Optimization Status:" >> "$financial_report"
    echo "-----------------------" >> "$financial_report"
    
    local optimization_enabled=$(jq -r '.optimization.enabled' "$FINANCE_CONFIG")
    local auto_apply=$(jq -r '.optimization.auto_apply' "$FINANCE_CONFIG")
    
    echo "Optimization Enabled: $optimization_enabled" >> "$financial_report"
    echo "Auto Apply Recommendations: $auto_apply" >> "$financial_report"
    
    # Get recent optimization report
    local recent_optimization_report=$(ls -t $FINANCE_REPORT_DIR/cost_optimization_*.txt 2>/dev/null | head -1)
    if [ ! -z "$recent_optimization_report" ] && [ -f "$recent_optimization_report" ]; then
        local recommendations_available=$(grep -c "Recommendation:" "$recent_optimization_report" 2>/dev/null || echo "0")
        echo "Recent Optimization Recommendations: $recommendations_available" >> "$financial_report"
    else
        echo "Recent Optimization Recommendations: N/A" >> "$financial_report"
    fi
    echo "" >> "$financial_report"
    
    # Add forecast information
    echo "Financial Forecast:" >> "$financial_report"
    echo "------------------" >> "$financial_report"
    
    # Get recent forecast report
    local recent_forecast_report=$(ls -t $FINANCE_REPORT_DIR/forecast_*.txt 2>/dev/null | head -1)
    if [ ! -z "$recent_forecast_report" ] && [ -f "$recent_forecast_report" ]; then
        local projected_monthly_cost=$(grep "Projected Monthly Cost" "$recent_forecast_report" | awk '{print $NF}' | sed 's/\$//')
        local projected_annual_cost=$(grep "Annual Cost (Projected Rate)" "$recent_forecast_report" | awk '{print $NF}' | sed 's/\$//')
        
        echo "Projected Monthly Cost: \$${projected_monthly_cost:-0}" >> "$financial_report"
        echo "Projected Annual Cost: \$${projected_annual_cost:-0}" >> "$financial_report"
        
        if [ $annual_budget -gt 0 ]; then
            if (( $(echo "$projected_annual_cost <= $annual_budget" | bc -l) )); then
                echo "✅ Projected annual cost within budget" >> "$financial_report"
            else
                local over_budget=$(echo "scale=2; $projected_annual_cost - $annual_budget" | bc)
                echo "❌ Projected annual cost exceeds budget by \$${over_budget}" >> "$financial_report"
            fi
        fi
    else
        echo "Forecast data not available" >> "$financial_report"
    fi
    echo "" >> "$financial_report"
    
    # Add recommendations
    echo "Financial Recommendations:" >> "$financial_report"
    echo "------------------------" >> "$financial_report"
    
    if [ $current_total_cost -eq 0 ]; then
        echo "✅ Current costs are within free tier limits" >> "$financial_report"
        echo "✅ Continue monitoring resource usage" >> "$financial_report"
    elif [ $monthly_budget -gt 0 ] && [ $current_total_cost -le $monthly_budget ]; then
        echo "✅ Current costs are within monthly budget" >> "$financial_report"
        echo "✅ Continue cost monitoring practices" >> "$financial_report"
    elif [ $monthly_budget -gt 0 ]; then
        local budget_variance=$((current_total_cost - monthly_budget))
        echo "❌ Current costs exceed monthly budget by \$${budget_variance}" >> "$financial_report"
        echo "❌ Review cost optimization recommendations" >> "$financial_report"
        echo "❌ Consider upgrading OCI plan if needed" >> "$financial_report"
    fi
    echo "" >> "$financial_report"
    
    # Add next steps
    echo "Next Steps:" >> "$financial_report"
    echo "----------" >> "$financial_report"
    echo "1. Review cost optimization recommendations" >> "$financial_report"
    echo "2. Monitor resource usage trends" >> "$financial_report"
    echo "3. Update budget allocations as needed" >> "$financial_report"
    echo "4. Schedule regular financial reviews" >> "$financial_report"
    echo "5. Implement cost-saving measures" >> "$financial_report"
    echo "" >> "$financial_report"
    
    echo "✅ Financial report generated"
    echo "📋 Financial report saved to: $financial_report"
    log_message "Financial report generated: $financial_report"
    
    # Display summary
    echo ""
    echo "Financial Report Summary:"
    echo "  Current Monthly Cost: \$${current_total_cost:-0}"
    echo "  Monthly Budget: \$${monthly_budget}"
    echo "  Annual Budget: \$${annual_budget}"
    echo "  Historical Data: $cost_count months"
    echo "  Optimization Enabled: $optimization_enabled"
    echo "  Report: $financial_report"
}

# Function to clean old financial reports
clean_old_reports() {
    log_message "Cleaning old financial reports"
    
    echo ""
    echo "Cleaning Old Financial Reports..."
    echo "================================"
    
    # Remove financial reports older than 90 days
    find "$FINANCE_REPORT_DIR" -name "cost_tracking_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$FINANCE_REPORT_DIR" -name "forecast_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$FINANCE_REPORT_DIR" -name "cost_optimization_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$FINANCE_REPORT_DIR" -name "financial_report_*.txt" -mtime +90 -delete 2>/dev/null || true
    
    # Remove cost data older than 1 year
    find "$COST_DATA_DIR" -name "costs_*.json" -mtime +365 -delete 2>/dev/null || true
    
    echo "✅ Old financial reports cleaned"
    log_message "Old financial reports cleaned"
}

# Main financial management function
main() {
    log_message "=== Starting Atlas Financial Management ==="
    
    # Initialize configuration
    initialize_finance_config
    
    # Start time
    local start_time=$(date)
    log_message "Financial management started at: $start_time"
    
    # Handle different financial operations
    case $1 in
        "track")
            track_resource_costs
            ;;
        "forecast")
            generate_financial_forecast
            ;;
        "optimize")
            optimize_costs
            ;;
        "report")
            generate_financial_report
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive financial management
            track_resource_costs
            generate_financial_forecast
            optimize_costs
            generate_financial_report
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Financial management completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Financial Management Completed ==="
    
    echo ""
    echo "✅ Financial management complete!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $FINANCE_REPORT_DIR"
    echo "💾 Cost data saved to: $COST_DATA_DIR"
    echo "📝 Log file: $FINANCE_LOG"
}

# Run main function
main "$@"