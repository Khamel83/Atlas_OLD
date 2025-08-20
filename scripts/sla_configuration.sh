#!/bin/bash

# Atlas Production Service Level Agreement (SLA) Configuration Script
# This script configures and manages SLA settings for the Atlas production environment

set -e  # Exit on any error

echo "Configuring Atlas Production SLA Settings..."

# Configuration
SLA_CONFIG="/home/ubuntu/dev/atlas/config/sla.json"
SLA_LOG="/home/ubuntu/dev/atlas/logs/sla_config.log"

# Create logs directory if it doesn't exist
mkdir -p "$(dirname $SLA_LOG)"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $SLA_LOG
    echo "$1"
}

# Function to initialize SLA configuration
initialize_sla_config() {
    log_message "Initializing SLA configuration"
    
    # Create default SLA configuration if it doesn't exist
    if [ ! -f "$SLA_CONFIG" ]; then
        cat > "$SLA_CONFIG" << EOF
{
    "sla": {
        "availability_target": 99.9,
        "response_time_target_ms": 1000,
        "uptime_target_hours": 8760,
        "maintenance_window_hours": 12,
        "incident_response_time_minutes": 30,
        "recovery_time_objective_hours": 4
    },
    "services": {
        "web_interface": {
            "name": "Web Interface",
            "endpoint": "http://localhost/",
            "importance": "high",
            "availability_target": 99.9,
            "response_time_target_ms": 1000
        },
        "api": {
            "name": "API Service",
            "endpoint": "http://localhost:5000/",
            "importance": "high",
            "availability_target": 99.9,
            "response_time_target_ms": 1500
        },
        "database": {
            "name": "Database Service",
            "endpoint": "postgresql://localhost/atlas",
            "importance": "critical",
            "availability_target": 99.95,
            "response_time_target_ms": 500
        },
        "monitoring": {
            "name": "Monitoring Service",
            "endpoint": "http://localhost:9090/",
            "importance": "medium",
            "availability_target": 99.5,
            "response_time_target_ms": 2000
        },
        "dashboard": {
            "name": "Dashboard Service",
            "endpoint": "http://localhost:3000/",
            "importance": "medium",
            "availability_target": 99.5,
            "response_time_target_ms": 2000
        }
    },
    "reporting": {
        "frequency": "daily",
        "recipients": ["admin@khamel.com"],
        "format": "text",
        "notifications_enabled": true
    },
    "mitigation_strategies": {
        "prevention": {
            "name": "Prevention",
            "priority": "high",
            "budget_allocation": 50
        },
        "detection": {
            "name": "Detection",
            "priority": "medium",
            "budget_allocation": 30
        },
        "response": {
            "name": "Response",
            "priority": "high",
            "budget_allocation": 20
        }
    }
}
EOF
        echo "✅ Created default SLA configuration"
        log_message "Default SLA configuration created"
    else
        echo "✅ SLA configuration already exists"
    fi
}

# Function to configure availability targets
configure_availability_targets() {
    log_message "Configuring availability targets"
    
    echo "Configuring Availability Targets..."
    echo "================================="
    
    local availability_config_report="$SLA_REPORT_DIR/availability_config_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create availability configuration report header
    echo "Atlas Production Availability Configuration" > "$availability_config_report"
    echo "Generated: $(date)" >> "$availability_config_report"
    echo "========================================" >> "$availability_config_report"
    echo "" >> "$availability_config_report"
    
    # Get current availability targets
    local current_availability_target=$(jq -r '.sla.availability_target' "$SLA_CONFIG")
    local current_uptime_target_hours=$(jq -r '.sla.uptime_target_hours' "$SLA_CONFIG")
    local current_maintenance_window_hours=$(jq -r '.sla.maintenance_window_hours' "$SLA_CONFIG")
    
    echo "Current Availability Targets:" >> "$availability_config_report"
    echo "--------------------------" >> "$availability_config_report"
    echo "Overall Availability Target: ${current_availability_target}%" >> "$availability_config_report"
    echo "Uptime Target: ${current_uptime_target_hours} hours/year" >> "$availability_config_report"
    echo "Maintenance Window: ${current_maintenance_window_hours} hours/year" >> "$availability_config_report"
    echo "" >> "$availability_config_report"
    
    # Configure service-specific availability targets
    echo "Service-Specific Availability Targets:" >> "$availability_config_report"
    echo "------------------------------------" >> "$availability_config_report"
    
    local services=$(jq -r '.services | keys[]' "$SLA_CONFIG")
    while IFS= read -r service_key; do
        local service_name=$(jq -r ".services.$service_key.name" "$SLA_CONFIG")
        local service_availability_target=$(jq -r ".services.$service_key.availability_target" "$SLA_CONFIG")
        local service_importance=$(jq -r ".services.$service_key.importance" "$SLA_CONFIG")
        
        echo "$service_name:" >> "$availability_config_report"
        echo "  Availability Target: ${service_availability_target}%" >> "$availability_config_report"
        echo "  Importance: $service_importance" >> "$availability_config_report"
        echo "" >> "$availability_config_report"
    done
    
    # Validate availability targets
    echo "Availability Target Validation:" >> "$availability_config_report"
    echo "-----------------------------" >> "$availability_config_report"
    
    local validation_passed=true
    
    # Check if overall availability target is reasonable
    if (( $(echo "$current_availability_target >= 99.0" | bc -l) )) && (( $(echo "$current_availability_target <= 100.0" | bc -l) )); then
        echo "✅ Overall availability target is valid: ${current_availability_target}%" >> "$availability_config_report"
    else
        echo "❌ Overall availability target is invalid: ${current_availability_target}%" >> "$availability_config_report"
        validation_passed=false
    fi
    
    # Check if service-specific targets are reasonable
    while IFS= read -r service_key; do
        local service_name=$(jq -r ".services.$service_key.name" "$SLA_CONFIG")
        local service_availability_target=$(jq -r ".services.$service_key.availability_target" "$SLA_CONFIG")
        
        if (( $(echo "$service_availability_target >= 99.0" | bc -l) )) && (( $(echo "$service_availability_target <= 100.0" | bc -l) )); then
            echo "✅ $service_name availability target is valid: ${service_availability_target}%" >> "$availability_config_report"
        else
            echo "❌ $service_name availability target is invalid: ${service_availability_target}%" >> "$availability_config_report"
            validation_passed=false
        fi
    done <<< "$services"
    
    echo "" >> "$availability_config_report"
    
    # Update configuration if needed
    if ! $validation_passed; then
        echo "❌ Some availability targets are invalid. Updating to defaults..." >> "$availability_config_report"
        
        # Update overall availability target
        if (( $(echo "$current_availability_target < 99.0" | bc -l) )) || (( $(echo "$current_availability_target > 100.0" | bc -l) )); then
            jq '.sla.availability_target = 99.9' "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
            echo "✅ Updated overall availability target to 99.9%" >> "$availability_config_report"
        fi
        
        # Update service-specific targets
        while IFS= read -r service_key; do
            local service_availability_target=$(jq -r ".services.$service_key.availability_target" "$SLA_CONFIG")
            
            if (( $(echo "$service_availability_target < 99.0" | bc -l) )) || (( $(echo "$service_availability_target > 100.0" | bc -l) )); then
                local default_target=99.9
                
                # Set higher target for critical services
                local service_importance=$(jq -r ".services.$service_key.importance" "$SLA_CONFIG")
                if [ "$service_importance" = "critical" ]; then
                    default_target=99.95
                elif [ "$service_importance" = "high" ]; then
                    default_target=99.9
                elif [ "$service_importance" = "medium" ]; then
                    default_target=99.5
                else
                    default_target=99.0
                fi
                
                jq ".services.$service_key.availability_target = $default_target" "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
                echo "✅ Updated $service_key availability target to ${default_target}%" >> "$availability_config_report"
            fi
        done <<< "$services"
    else
        echo "✅ All availability targets are valid" >> "$availability_config_report"
    fi
    
    echo "" >> "$availability_config_report"
    
    echo "✅ Availability targets configured"
    echo "📋 Availability configuration report saved to: $availability_config_report"
    log_message "Availability targets configured: $availability_config_report"
    
    # Display summary
    echo ""
    echo "Availability Configuration Summary:"
    echo "  Overall Target: ${current_availability_target}%"
    echo "  Uptime Target: ${current_uptime_target_hours} hours/year"
    echo "  Maintenance Window: ${current_maintenance_window_hours} hours/year"
    echo "  Services Configured: $(echo "$services" | wc -l)"
    echo "  Validation: $(if $validation_passed; then echo "✅ PASSED"; else echo "❌ FAILED"; fi)"
    echo "  Report: $availability_config_report"
}

# Function to configure response time targets
configure_response_time_targets() {
    log_message "Configuring response time targets"
    
    echo ""
    echo "Configuring Response Time Targets..."
    echo "=================================="
    
    local response_time_config_report="$SLA_REPORT_DIR/response_time_config_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create response time configuration report header
    echo "Atlas Production Response Time Configuration" > "$response_time_config_report"
    echo "Generated: $(date)" >> "$response_time_config_report"
    echo "=========================================" >> "$response_time_config_report"
    echo "" >> "$response_time_config_report"
    
    # Get current response time targets
    local current_response_time_target_ms=$(jq -r '.sla.response_time_target_ms' "$SLA_CONFIG")
    
    echo "Current Response Time Targets:" >> "$response_time_config_report"
    echo "----------------------------" >> "$response_time_config_report"
    echo "Overall Response Time Target: ${current_response_time_target_ms} ms" >> "$response_time_config_report"
    echo "" >> "$response_time_config_report"
    
    # Configure service-specific response time targets
    echo "Service-Specific Response Time Targets:" >> "$response_time_config_report"
    echo "-------------------------------------" >> "$response_time_config_report"
    
    local services=$(jq -r '.services | keys[]' "$SLA_CONFIG")
    while IFS= read -r service_key; do
        local service_name=$(jq -r ".services.$service_key.name" "$SLA_CONFIG")
        local service_response_time_target_ms=$(jq -r ".services.$service_key.response_time_target_ms" "$SLA_CONFIG")
        local service_importance=$(jq -r ".services.$service_key.importance" "$SLA_CONFIG")
        
        echo "$service_name:" >> "$response_time_config_report"
        echo "  Response Time Target: ${service_response_time_target_ms} ms" >> "$response_time_config_report"
        echo "  Importance: $service_importance" >> "$response_time_config_report"
        echo "" >> "$response_time_config_report"
    done
    
    # Validate response time targets
    echo "Response Time Target Validation:" >> "$response_time_config_report"
    echo "------------------------------" >> "$response_time_config_report"
    
    local validation_passed=true
    
    # Check if overall response time target is reasonable
    if [ $current_response_time_target_ms -ge 100 ] && [ $current_response_time_target_ms -le 10000 ]; then
        echo "✅ Overall response time target is valid: ${current_response_time_target_ms} ms" >> "$response_time_config_report"
    else
        echo "❌ Overall response time target is invalid: ${current_response_time_target_ms} ms" >> "$response_time_config_report"
        validation_passed=false
    fi
    
    # Check if service-specific targets are reasonable
    while IFS= read -r service_key; do
        local service_name=$(jq -r ".services.$service_key.name" "$SLA_CONFIG")
        local service_response_time_target_ms=$(jq -r ".services.$service_key.response_time_target_ms" "$SLA_CONFIG")
        
        if [ $service_response_time_target_ms -ge 100 ] && [ $service_response_time_target_ms -le 10000 ]; then
            echo "✅ $service_name response time target is valid: ${service_response_time_target_ms} ms" >> "$response_time_config_report"
        else
            echo "❌ $service_name response time target is invalid: ${service_response_time_target_ms} ms" >> "$response_time_config_report"
            validation_passed=false
        fi
    done <<< "$services"
    
    echo "" >> "$response_time_config_report"
    
    # Update configuration if needed
    if ! $validation_passed; then
        echo "❌ Some response time targets are invalid. Updating to defaults..." >> "$response_time_config_report"
        
        # Update overall response time target
        if [ $current_response_time_target_ms -lt 100 ] || [ $current_response_time_target_ms -gt 10000 ]; then
            jq '.sla.response_time_target_ms = 1000' "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
            echo "✅ Updated overall response time target to 1000 ms" >> "$response_time_config_report"
        fi
        
        # Update service-specific targets
        while IFS= read -r service_key; do
            local service_response_time_target_ms=$(jq -r ".services.$service_key.response_time_target_ms" "$SLA_CONFIG")
            
            if [ $service_response_time_target_ms -lt 100 ] || [ $service_response_time_target_ms -gt 10000 ]; then
                local default_target=1000
                
                # Set different targets based on service importance
                local service_importance=$(jq -r ".services.$service_key.importance" "$SLA_CONFIG")
                if [ "$service_importance" = "critical" ]; then
                    default_target=500
                elif [ "$service_importance" = "high" ]; then
                    default_target=1000
                elif [ "$service_importance" = "medium" ]; then
                    default_target=1500
                else
                    default_target=2000
                fi
                
                jq ".services.$service_key.response_time_target_ms = $default_target" "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
                echo "✅ Updated $service_key response time target to ${default_target} ms" >> "$response_time_config_report"
            fi
        done <<< "$services"
    else
        echo "✅ All response time targets are valid" >> "$response_time_config_report"
    fi
    
    echo "" >> "$response_time_config_report"
    
    echo "✅ Response time targets configured"
    echo "📋 Response time configuration report saved to: $response_time_config_report"
    log_message "Response time targets configured: $response_time_config_report"
    
    # Display summary
    echo ""
    echo "Response Time Configuration Summary:"
    echo "  Overall Target: ${current_response_time_target_ms} ms"
    echo "  Services Configured: $(echo "$services" | wc -l)"
    echo "  Validation: $(if $validation_passed; then echo "✅ PASSED"; else echo "❌ FAILED"; fi)"
    echo "  Report: $response_time_config_report"
}

# Function to configure incident response targets
configure_incident_response_targets() {
    log_message "Configuring incident response targets"
    
    echo ""
    echo "Configuring Incident Response Targets..."
    echo "======================================"
    
    local incident_response_config_report="$SLA_REPORT_DIR/incident_response_config_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create incident response configuration report header
    echo "Atlas Production Incident Response Configuration" > "$incident_response_config_report"
    echo "Generated: $(date)" >> "$incident_response_config_report"
    echo "=============================================" >> "$incident_response_config_report"
    echo "" >> "$incident_response_config_report"
    
    # Get current incident response targets
    local current_incident_response_time_minutes=$(jq -r '.sla.incident_response_time_minutes' "$SLA_CONFIG")
    local current_recovery_time_objective_hours=$(jq -r '.sla.recovery_time_objective_hours' "$SLA_CONFIG")
    
    echo "Current Incident Response Targets:" >> "$incident_response_config_report"
    echo "--------------------------------" >> "$incident_response_config_report"
    echo "Incident Response Time: ${current_incident_response_time_minutes} minutes" >> "$incident_response_config_report"
    echo "Recovery Time Objective: ${current_recovery_time_objective_hours} hours" >> "$incident_response_config_report"
    echo "" >> "$incident_response_config_report"
    
    # Configure incident response procedures
    echo "Incident Response Procedures:" >> "$incident_response_config_report"
    echo "---------------------------" >> "$incident_response_config_report"
    
    # Check if incident response procedures exist
    local ir_procedures=(
        "/home/ubuntu/dev/atlas/scripts/incident_response.sh:Incident Response Script"
        "/home/ubuntu/dev/atlas/docs/incident_response.md:Incident Response Documentation"
        "/home/ubuntu/dev/atlas/scripts/emergency_tools.py:Emergency Tools"
    )
    
    local procedures_found=0
    
    for procedure_info in "${ir_procedures[@]}"; do
        local procedure_path=$(echo $procedure_info | cut -d':' -f1)
        local procedure_desc=$(echo $procedure_info | cut -d':' -f2)
        
        if [ -f "$procedure_path" ]; then
            echo "✅ $procedure_desc exists" >> "$incident_response_config_report"
            procedures_found=$((procedures_found + 1))
        else
            echo "❌ $procedure_desc not found" >> "$incident_response_config_report"
        fi
    done
    
    echo "Incident Response Procedures Found: $procedures_found/${#ir_procedures[@]}" >> "$incident_response_config_report"
    echo "" >> "$incident_response_config_report"
    
    # Validate incident response targets
    echo "Incident Response Target Validation:" >> "$incident_response_config_report"
    echo "----------------------------------" >> "$incident_response_config_report"
    
    local validation_passed=true
    
    # Check if incident response time target is reasonable
    if [ $current_incident_response_time_minutes -ge 1 ] && [ $current_incident_response_time_minutes -le 120 ]; then
        echo "✅ Incident response time target is valid: ${current_incident_response_time_minutes} minutes" >> "$incident_response_config_report"
    else
        echo "❌ Incident response time target is invalid: ${current_incident_response_time_minutes} minutes" >> "$incident_response_config_report"
        validation_passed=false
    fi
    
    # Check if recovery time objective is reasonable
    if [ $current_recovery_time_objective_hours -ge 1 ] && [ $current_recovery_time_objective_hours -le 24 ]; then
        echo "✅ Recovery time objective is valid: ${current_recovery_time_objective_hours} hours" >> "$incident_response_config_report"
    else
        echo "❌ Recovery time objective is invalid: ${current_recovery_time_objective_hours} hours" >> "$incident_response_config_report"
        validation_passed=false
    fi
    
    echo "" >> "$incident_response_config_report"
    
    # Update configuration if needed
    if ! $validation_passed; then
        echo "❌ Some incident response targets are invalid. Updating to defaults..." >> "$incident_response_config_report"
        
        # Update incident response time target
        if [ $current_incident_response_time_minutes -lt 1 ] || [ $current_incident_response_time_minutes -gt 120 ]; then
            jq '.sla.incident_response_time_minutes = 30' "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
            echo "✅ Updated incident response time target to 30 minutes" >> "$incident_response_config_report"
        fi
        
        # Update recovery time objective
        if [ $current_recovery_time_objective_hours -lt 1 ] || [ $current_recovery_time_objective_hours -gt 24 ]; then
            jq '.sla.recovery_time_objective_hours = 4' "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
            echo "✅ Updated recovery time objective to 4 hours" >> "$incident_response_config_report"
        fi
    else
        echo "✅ All incident response targets are valid" >> "$incident_response_config_report"
    fi
    
    echo "" >> "$incident_response_config_report"
    
    # Configure escalation procedures
    echo "Escalation Procedures:" >> "$incident_response_config_report"
    echo "--------------------" >> "$incident_response_config_report"
    
    # Check if escalation procedures exist
    local escalation_procedures=(
        "/home/ubuntu/dev/atlas/scripts/escalation_procedure.sh:Escalation Script"
        "/home/ubuntu/dev/atlas/docs/escalation_procedure.md:Escalation Documentation"
    )
    
    local escalation_found=0
    
    for procedure_info in "${escalation_procedures[@]}"; do
        local procedure_path=$(echo $procedure_info | cut -d':' -f1)
        local procedure_desc=$(echo $procedure_info | cut -d':' -f2)
        
        if [ -f "$procedure_path" ]; then
            echo "✅ $procedure_desc exists" >> "$incident_response_config_report"
            escalation_found=$((escalation_found + 1))
        else
            echo "❌ $procedure_desc not found" >> "$incident_response_config_report"
        fi
    done
    
    echo "Escalation Procedures Found: $escalation_found/${#escalation_procedures[@]}" >> "$incident_response_config_report"
    echo "" >> "$incident_response_config_report"
    
    echo "✅ Incident response targets configured"
    echo "📋 Incident response configuration report saved to: $incident_response_config_report"
    log_message "Incident response targets configured: $incident_response_config_report"
    
    # Display summary
    echo ""
    echo "Incident Response Configuration Summary:"
    echo "  Response Time Target: ${current_incident_response_time_minutes} minutes"
    echo "  Recovery Time Objective: ${current_recovery_time_objective_hours} hours"
    echo "  Procedures Found: $procedures_found/${#ir_procedures[@]}"
    echo "  Escalation Procedures Found: $escalation_found/${#escalation_procedures[@]}"
    echo "  Validation: $(if $validation_passed; then echo "✅ PASSED"; else echo "❌ FAILED"; fi)"
    echo "  Report: $incident_response_config_report"
}

# Function to configure reporting settings
configure_reporting_settings() {
    log_message "Configuring reporting settings"
    
    echo ""
    echo "Configuring Reporting Settings..."
    echo "==============================="
    
    local reporting_config_report="$SLA_REPORT_DIR/reporting_config_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create reporting configuration report header
    echo "Atlas Production Reporting Configuration" > "$reporting_config_report"
    echo "Generated: $(date)" >> "$reporting_config_report"
    echo "======================================" >> "$reporting_config_report"
    echo "" >> "$reporting_config_report"
    
    # Get current reporting settings
    local current_reporting_frequency=$(jq -r '.reporting.frequency' "$SLA_CONFIG")
    local current_reporting_format=$(jq -r '.reporting.format' "$SLA_CONFIG")
    local current_notifications_enabled=$(jq -r '.reporting.notifications_enabled' "$SLA_CONFIG")
    
    echo "Current Reporting Settings:" >> "$reporting_config_report"
    echo "--------------------------" >> "$reporting_config_report"
    echo "Reporting Frequency: $current_reporting_frequency" >> "$reporting_config_report"
    echo "Reporting Format: $current_reporting_format" >> "$reporting_config_report"
    echo "Notifications Enabled: $current_notifications_enabled" >> "$reporting_config_report"
    echo "" >> "$reporting_config_report"
    
    # Configure recipients
    echo "Reporting Recipients:" >> "$reporting_config_report"
    echo "-------------------" >> "$reporting_config_report"
    
    local recipients=$(jq -r '.reporting.recipients[]' "$SLA_CONFIG")
    local recipient_count=0
    
    while IFS= read -r recipient; do
        echo "Recipient $((recipient_count + 1)): $recipient" >> "$reporting_config_report"
        recipient_count=$((recipient_count + 1))
    done <<< "$recipients"
    
    echo "Total Recipients: $recipient_count" >> "$reporting_config_report"
    echo "" >> "$reporting_config_report"
    
    # Validate reporting settings
    echo "Reporting Settings Validation:" >> "$reporting_config_report"
    echo "---------------------------" >> "$reporting_config_report"
    
    local validation_passed=true
    
    # Check if reporting frequency is valid
    local valid_frequencies=("hourly" "daily" "weekly" "monthly")
    local frequency_valid=false
    
    for freq in "${valid_frequencies[@]}"; do
        if [ "$current_reporting_frequency" = "$freq" ]; then
            frequency_valid=true
            break
        fi
    done
    
    if $frequency_valid; then
        echo "✅ Reporting frequency is valid: $current_reporting_frequency" >> "$reporting_config_report"
    else
        echo "❌ Reporting frequency is invalid: $current_reporting_frequency" >> "$reporting_config_report"
        validation_passed=false
    fi
    
    # Check if reporting format is valid
    local valid_formats=("text" "json" "csv" "pdf")
    local format_valid=false
    
    for fmt in "${valid_formats[@]}"; do
        if [ "$current_reporting_format" = "$fmt" ]; then
            format_valid=true
            break
        fi
    done
    
    if $format_valid; then
        echo "✅ Reporting format is valid: $current_reporting_format" >> "$reporting_config_report"
    else
        echo "❌ Reporting format is invalid: $current_reporting_format" >> "$reporting_config_report"
        validation_passed=false
    fi
    
    # Check if recipients are valid
    if [ $recipient_count -gt 0 ]; then
        echo "✅ Reporting recipients are configured: $recipient_count recipients" >> "$reporting_config_report"
    else
        echo "❌ No reporting recipients configured" >> "$reporting_config_report"
        validation_passed=false
    fi
    
    echo "" >> "$reporting_config_report"
    
    # Update configuration if needed
    if ! $validation_passed; then
        echo "❌ Some reporting settings are invalid. Updating to defaults..." >> "$reporting_config_report"
        
        # Update reporting frequency
        if ! $frequency_valid; then
            jq '.reporting.frequency = "daily"' "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
            echo "✅ Updated reporting frequency to daily" >> "$reporting_config_report"
        fi
        
        # Update reporting format
        if ! $format_valid; then
            jq '.reporting.format = "text"' "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
            echo "✅ Updated reporting format to text" >> "$reporting_config_report"
        fi
        
        # Add default recipient if none exist
        if [ $recipient_count -eq 0 ]; then
            jq '.reporting.recipients = ["admin@khamel.com"]' "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
            echo "✅ Added default recipient: admin@khamel.com" >> "$reporting_config_report"
        fi
    else
        echo "✅ All reporting settings are valid" >> "$reporting_config_report"
    fi
    
    echo "" >> "$reporting_config_report"
    
    # Configure reporting schedules
    echo "Reporting Schedules:" >> "$reporting_config_report"
    echo "------------------" >> "$reporting_config_report"
    
    # Check if cron jobs are configured
    local cron_jobs=(
        "daily:/home/ubuntu/dev/atlas/scripts/sla_monitoring.sh:Daily SLA Monitoring"
        "weekly:/home/ubuntu/dev/atlas/scripts/production_readiness_report.py:Weekly Production Readiness Report"
        "monthly:/home/ubuntu/dev/atlas/scripts/production_status_check.sh:Monthly Production Status Check"
    )
    
    local cron_jobs_found=0
    
    for job_info in "${cron_jobs[@]}"; do
        local schedule=$(echo $job_info | cut -d':' -f1)
        local script_path=$(echo $job_info | cut -d':' -f2)
        local job_desc=$(echo $job_info | cut -d':' -f3)
        
        if crontab -l 2>/dev/null | grep -q "$(basename $script_path)"; then
            echo "✅ $job_desc cron job is configured for $schedule execution" >> "$reporting_config_report"
            cron_jobs_found=$((cron_jobs_found + 1))
        else
            echo "❌ $job_desc cron job is not configured" >> "$reporting_config_report"
        fi
    done
    
    echo "Reporting Cron Jobs Found: $cron_jobs_found/${#cron_jobs[@]}" >> "$reporting_config_report"
    echo "" >> "$reporting_config_report"
    
    echo "✅ Reporting settings configured"
    echo "📋 Reporting configuration report saved to: $reporting_config_report"
    log_message "Reporting settings configured: $reporting_config_report"
    
    # Display summary
    echo ""
    echo "Reporting Configuration Summary:"
    echo "  Frequency: $current_reporting_frequency"
    echo "  Format: $current_reporting_format"
    echo "  Notifications: $current_notifications_enabled"
    echo "  Recipients: $recipient_count"
    echo "  Cron Jobs: $cron_jobs_found/${#cron_jobs[@]}"
    echo "  Validation: $(if $validation_passed; then echo "✅ PASSED"; else echo "❌ FAILED"; fi)"
    echo "  Report: $reporting_config_report"
}

# Function to configure mitigation strategies
configure_mitigation_strategies() {
    log_message "Configuring mitigation strategies"
    
    echo ""
    echo "Configuring Mitigation Strategies..."
    echo "=================================="
    
    local mitigation_config_report="$SLA_REPORT_DIR/mitigation_config_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create mitigation configuration report header
    echo "Atlas Production Mitigation Strategies Configuration" > "$mitigation_config_report"
    echo "Generated: $(date)" >> "$mitigation_config_report"
    echo "==================================================" >> "$mitigation_config_report"
    echo "" >> "$mitigation_config_report"
    
    # Get current mitigation strategies
    echo "Current Mitigation Strategies:" >> "$mitigation_config_report"
    echo "----------------------------" >> "$mitigation_config_report"
    
    local strategies=$(jq -r '.mitigation_strategies | keys[]' "$SLA_CONFIG")
    while IFS= read -r strategy_key; do
        local strategy_name=$(jq -r ".mitigation_strategies.$strategy_key.name" "$SLA_CONFIG")
        local strategy_priority=$(jq -r ".mitigation_strategies.$strategy_key.priority" "$SLA_CONFIG")
        local strategy_budget=$(jq -r ".mitigation_strategies.$strategy_key.budget_allocation" "$SLA_CONFIG")
        
        echo "$strategy_name:" >> "$mitigation_config_report"
        echo "  Priority: $strategy_priority" >> "$mitigation_config_report"
        echo "  Budget Allocation: ${strategy_budget}%" >> "$mitigation_config_report"
        echo "" >> "$mitigation_config_report"
    done
    
    # Validate mitigation strategies
    echo "Mitigation Strategy Validation:" >> "$mitigation_config_report"
    echo "-----------------------------" >> "$mitigation_config_report"
    
    local validation_passed=true
    local total_budget=0
    
    while IFS= read -r strategy_key; do
        local strategy_priority=$(jq -r ".mitigation_strategies.$strategy_key.priority" "$SLA_CONFIG")
        local strategy_budget=$(jq -r ".mitigation_strategies.$strategy_key.budget_allocation" "$SLA_CONFIG")
        
        # Validate priority
        local valid_priorities=("low" "medium" "high" "critical")
        local priority_valid=false
        
        for priority in "${valid_priorities[@]}"; do
            if [ "$strategy_priority" = "$priority" ]; then
                priority_valid=true
                break
            fi
        done
        
        if $priority_valid; then
            echo "✅ $strategy_key priority is valid: $strategy_priority" >> "$mitigation_config_report"
        else
            echo "❌ $strategy_key priority is invalid: $strategy_priority" >> "$mitigation_config_report"
            validation_passed=false
        fi
        
        # Validate budget allocation
        if [ $strategy_budget -ge 0 ] && [ $strategy_budget -le 100 ]; then
            echo "✅ $strategy_key budget allocation is valid: ${strategy_budget}%" >> "$mitigation_config_report"
            total_budget=$((total_budget + strategy_budget))
        else
            echo "❌ $strategy_key budget allocation is invalid: ${strategy_budget}%" >> "$mitigation_config_report"
            validation_passed=false
        fi
    done <<< "$strategies"
    
    echo "Total Budget Allocation: ${total_budget}%" >> "$mitigation_config_report"
    echo "" >> "$mitigation_config_report"
    
    # Check if total budget allocation is 100%
    if [ $total_budget -eq 100 ]; then
        echo "✅ Total budget allocation is correct: ${total_budget}%" >> "$mitigation_config_report"
    else
        echo "❌ Total budget allocation is incorrect: ${total_budget}% (should be 100%)" >> "$mitigation_config_report"
        validation_passed=false
    fi
    echo "" >> "$mitigation_config_report"
    
    # Update configuration if needed
    if ! $validation_passed; then
        echo "❌ Some mitigation strategies are invalid. Updating to defaults..." >> "$mitigation_config_report"
        
        # Reset to default mitigation strategies
        jq '.mitigation_strategies = {
            "prevention": {
                "name": "Prevention",
                "priority": "high",
                "budget_allocation": 50
            },
            "detection": {
                "name": "Detection",
                "priority": "medium",
                "budget_allocation": 30
            },
            "response": {
                "name": "Response",
                "priority": "high",
                "budget_allocation": 20
            }
        }' "$SLA_CONFIG" > "$SLA_CONFIG.tmp" && mv "$SLA_CONFIG.tmp" "$SLA_CONFIG"
        
        echo "✅ Updated mitigation strategies to defaults" >> "$mitigation_config_report"
        echo "  Prevention: 50%" >> "$mitigation_config_report"
        echo "  Detection: 30%" >> "$mitigation_config_report"
        echo "  Response: 20%" >> "$mitigation_config_report"
        echo "  Total: 100%" >> "$mitigation_config_report"
    else
        echo "✅ All mitigation strategies are valid" >> "$mitigation_config_report"
    fi
    
    echo "" >> "$mitigation_config_report"
    
    # Configure mitigation implementation
    echo "Mitigation Implementation:" >> "$mitigation_config_report"
    echo "------------------------" >> "$mitigation_config_report"
    
    # Check if mitigation scripts exist
    local mitigation_scripts=(
        "/home/ubuntu/dev/atlas/scripts/prevention_mitigation.py:Prevention Mitigation Script"
        "/home/ubuntu/dev/atlas/scripts/detection_mitigation.py:Detection Mitigation Script"
        "/home/ubuntu/dev/atlas/scripts/response_mitigation.py:Response Mitigation Script"
    )
    
    local scripts_found=0
    
    for script_info in "${mitigation_scripts[@]}"; do
        local script_path=$(echo $script_info | cut -d':' -f1)
        local script_desc=$(echo $script_info | cut -d':' -f2)
        
        if [ -f "$script_path" ]; then
            echo "✅ $script_desc exists" >> "$mitigation_config_report"
            scripts_found=$((scripts_found + 1))
        else
            echo "❌ $script_desc not found" >> "$mitigation_config_report"
        fi
    done
    
    echo "Mitigation Scripts Found: $scripts_found/${#mitigation_scripts[@]}" >> "$mitigation_config_report"
    echo "" >> "$mitigation_config_report"
    
    echo "✅ Mitigation strategies configured"
    echo "📋 Mitigation configuration report saved to: $mitigation_config_report"
    log_message "Mitigation strategies configured: $mitigation_config_report"
    
    # Display summary
    echo ""
    echo "Mitigation Strategy Configuration Summary:"
    echo "  Strategies Configured: $(echo "$strategies" | wc -l)"
    echo "  Budget Allocation: ${total_budget}%"
    echo "  Scripts Found: $scripts_found/${#mitigation_scripts[@]}"
    echo "  Validation: $(if $validation_passed; then echo "✅ PASSED"; else echo "❌ FAILED"; fi)"
    echo "  Report: $mitigation_config_report"
}

# Function to clean old SLA configuration reports
clean_old_config_reports() {
    log_message "Cleaning old SLA configuration reports"
    
    echo ""
    echo "Cleaning Old SLA Configuration Reports..."
    echo "======================================="
    
    # Remove SLA configuration reports older than 90 days
    find "$SLA_REPORT_DIR" -name "availability_config_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$SLA_REPORT_DIR" -name "response_time_config_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$SLA_REPORT_DIR" -name "incident_response_config_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$SLA_REPORT_DIR" -name "reporting_config_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$SLA_REPORT_DIR" -name "mitigation_config_*.txt" -mtime +90 -delete 2>/dev/null || true
    
    echo "✅ Old SLA configuration reports cleaned"
    log_message "Old SLA configuration reports cleaned"
}

# Main SLA configuration function
main() {
    log_message "=== Starting Atlas SLA Configuration ==="
    
    # Initialize configuration
    initialize_sla_config
    
    # Start time
    local start_time=$(date)
    log_message "SLA configuration started at: $start_time"
    
    # Handle different SLA configuration operations
    case $1 in
        "availability")
            configure_availability_targets
            ;;
        "response")
            configure_response_time_targets
            ;;
        "incidents")
            configure_incident_response_targets
            ;;
        "reporting")
            configure_reporting_settings
            ;;
        "mitigation")
            configure_mitigation_strategies
            ;;
        "clean")
            clean_old_config_reports
            ;;
        *)
            # Run comprehensive SLA configuration
            configure_availability_targets
            configure_response_time_targets
            configure_incident_response_targets
            configure_reporting_settings
            configure_mitigation_strategies
            clean_old_config_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "SLA configuration completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== SLA Configuration Completed ==="
    
    echo ""
    echo "✅ SLA configuration completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $SLA_REPORT_DIR"
    echo "📝 Configuration file: $SLA_CONFIG"
    echo "📝 Log file: $SLA_LOG"
}

# Run main function
main "$@"