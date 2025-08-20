#!/bin/bash

# Atlas Production Risk Management Script
# This script manages risks for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Risk Management..."

# Configuration
RISK_LOG="/home/ubuntu/dev/atlas/logs/risk_management.log"
RISK_REPORT_DIR="/home/ubuntu/dev/atlas/reports/risk"
RISK_CONFIG="/home/ubuntu/dev/atlas/config/risk.json"
RISK_ASSESSMENTS_DIR="/home/ubuntu/dev/atlas/risk/assessments"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $RISK_LOG)"
mkdir -p "$RISK_REPORT_DIR"
mkdir -p "$RISK_ASSESSMENTS_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $RISK_LOG
    echo "$1"
}

# Function to initialize risk configuration
initialize_risk_config() {
    log_message "Initializing risk configuration"
    
    # Create default risk configuration if it doesn't exist
    if [ ! -f "$RISK_CONFIG" ]; then
        cat > "$RISK_CONFIG" << EOF
{
    "risk_management": {
        "assessment_frequency": "monthly",
        "risk_tolerance": "medium",
        "escalation_threshold": "high",
        "review_process": "quarterly"
    },
    "risk_categories": {
        "technical_risks": {
            "name": "Technical Risks",
            "weight": 40,
            "subcategories": [
                "system_failure",
                "data_loss",
                "performance_degradation",
                "security_breach"
            ]
        },
        "operational_risks": {
            "name": "Operational Risks",
            "weight": 30,
            "subcategories": [
                "process_failure",
                "human_error",
                "resource_shortage",
                "compliance_violation"
            ]
        },
        "business_risks": {
            "name": "Business Risks",
            "weight": 20,
            "subcategories": [
                "revenue_loss",
                "reputation_damage",
                "competitive_disadvantage",
                "regulatory_penalty"
            ]
        },
        "external_risks": {
            "name": "External Risks",
            "weight": 10,
            "subcategories": [
                "vendor_failure",
                "market_changes",
                "natural_disasters",
                "cyber_attacks"
            ]
        }
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
    },
    "reporting": {
        "frequency": "weekly",
        "recipients": ["admin@khamel.com", "risk@khamel.com"],
        "format": "pdf"
    }
}
EOF
        echo "✅ Created default risk configuration"
        log_message "Default risk configuration created"
    else
        echo "✅ Risk configuration already exists"
    fi
}

# Function to assess technical risks
assess_technical_risks() {
    log_message "Assessing technical risks"
    
    echo "Assessing Technical Risks..."
    echo "=========================="
    
    local risk_assessment_report="$RISK_REPORT_DIR/technical_risks_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create risk assessment report header
    echo "Atlas Production Technical Risk Assessment" > "$risk_assessment_report"
    echo "Generated: $(date)" >> "$risk_assessment_report"
    echo "=========================================" >> "$risk_assessment_report"
    echo "" >> "$risk_assessment_report"
    
    # Get technical risk weight
    local tech_risk_weight=$(jq -r '.risk_categories.technical_risks.weight' "$RISK_CONFIG")
    
    echo "Technical Risk Weight: ${tech_risk_weight}%" >> "$risk_assessment_report"
    echo "" >> "$risk_assessment_report"
    
    # Initialize risk scores
    local system_failure_risk=0
    local data_loss_risk=0
    local performance_degradation_risk=0
    local security_breach_risk=0
    
    # Assess system failure risk
    echo "System Failure Risk Assessment:" >> "$risk_assessment_report"
    echo "------------------------------" >> "$risk_assessment_report"
    
    # Check system uptime
    local system_uptime_days=$(uptime -p | awk '{print $2}' | sed 's/day.*//')
    if [ -z "$system_uptime_days" ]; then
        system_uptime_days=0
    fi
    
    if [ $system_uptime_days -gt 30 ]; then
        echo "✅ System has been stable for $system_uptime_days days" >> "$risk_assessment_report"
        system_failure_risk=10  # Low risk
    elif [ $system_uptime_days -gt 7 ]; then
        echo "⚠️ System has been stable for $system_uptime_days days" >> "$risk_assessment_report"
        system_failure_risk=30  # Medium risk
    else
        echo "❌ System has been stable for only $system_uptime_days days" >> "$risk_assessment_report"
        system_failure_risk=70  # High risk
    fi
    
    # Check critical services status
    local critical_services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    local services_down=0
    for service_info in "${critical_services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc is running" >> "$risk_assessment_report"
        else
            echo "❌ $service_desc is not running" >> "$risk_assessment_report"
            services_down=$((services_down + 1))
        fi
    done
    
    if [ $services_down -gt 0 ]; then
        system_failure_risk=$((system_failure_risk + 20))
        echo "❌ $services_down critical services are down" >> "$risk_assessment_report"
    fi
    echo "" >> "$risk_assessment_report"
    
    # Assess data loss risk
    echo "Data Loss Risk Assessment:" >> "$risk_assessment_report"
    echo "-------------------------" >> "$risk_assessment_report"
    
    # Check backup status
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        local backup_count=$(find "$backup_dir" -name "*.sql*" | wc -l)
        if [ $backup_count -gt 0 ]; then
            echo "✅ Backups are being created ($backup_count backup files)" >> "$risk_assessment_report"
            
            # Check backup age
            local latest_backup=$(find "$backup_dir" -name "*.sql*" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
            if [ ! -z "$latest_backup" ]; then
                local backup_age_seconds=$(( $(date +%s) - $(stat -c %Y "$latest_backup") ))
                local backup_age_hours=$(( backup_age_seconds / 3600 ))
                
                if [ $backup_age_hours -lt 24 ]; then
                    echo "✅ Latest backup is current (${backup_age_hours} hours old)" >> "$risk_assessment_report"
                    data_loss_risk=10  # Low risk
                elif [ $backup_age_hours -lt 48 ]; then
                    echo "⚠️ Latest backup is somewhat outdated (${backup_age_hours} hours old)" >> "$risk_assessment_report"
                    data_loss_risk=40  # Medium risk
                else
                    echo "❌ Latest backup is outdated (${backup_age_hours} hours old)" >> "$risk_assessment_report"
                    data_loss_risk=80  # High risk
                fi
            else
                echo "❌ No recent backups found" >> "$risk_assessment_report"
                data_loss_risk=90  # Very high risk
            fi
        else
            echo "❌ No backup files found" >> "$risk_assessment_report"
            data_loss_risk=100  # Critical risk
        fi
    else
        echo "❌ Backup directory not found" >> "$risk_assessment_report"
        data_loss_risk=100  # Critical risk
    fi
    echo "" >> "$risk_assessment_report"
    
    # Assess performance degradation risk
    echo "Performance Degradation Risk Assessment:" >> "$risk_assessment_report"
    echo "---------------------------------------" >> "$risk_assessment_report"
    
    # Check system resources
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local memory_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "Current Resource Usage:" >> "$risk_assessment_report"
    echo "  CPU: ${cpu_usage}%" >> "$risk_assessment_report"
    echo "  Memory: ${memory_usage}%" >> "$risk_assessment_report"
    echo "  Disk: ${disk_usage}%" >> "$risk_assessment_report"
    
    # Assess performance risk based on resource usage
    if [ $cpu_usage -lt 70 ] && [ $memory_usage -lt 70 ] && [ $disk_usage -lt 80 ]; then
        echo "✅ Resource usage is within normal limits" >> "$risk_assessment_report"
        performance_degradation_risk=20  # Low risk
    elif [ $cpu_usage -lt 85 ] && [ $memory_usage -lt 85 ] && [ $disk_usage -lt 90 ]; then
        echo "⚠️ Resource usage is elevated but manageable" >> "$risk_assessment_report"
        performance_degradation_risk=50  # Medium risk
    else
        echo "❌ Resource usage is high and may impact performance" >> "$risk_assessment_report"
        performance_degradation_risk=80  # High risk
    fi
    echo "" >> "$risk_assessment_report"
    
    # Assess security breach risk
    echo "Security Breach Risk Assessment:" >> "$risk_assessment_report"
    echo "------------------------------" >> "$risk_assessment_report"
    
    # Check security configurations
    local security_issues=0
    
    # Check if firewall is active
    if sudo ufw status | grep -q "Status: active"; then
        echo "✅ Firewall is active" >> "$risk_assessment_report"
    else
        echo "❌ Firewall is not active" >> "$risk_assessment_report"
        security_issues=$((security_issues + 1))
    fi
    
    # Check SSH configuration
    if grep -q "^PasswordAuthentication no" /etc/ssh/sshd_config; then
        echo "✅ SSH password authentication is disabled" >> "$risk_assessment_report"
    else
        echo "❌ SSH password authentication is enabled" >> "$risk_assessment_report"
        security_issues=$((security_issues + 1))
    fi
    
    # Check web authentication
    if [ -f "/etc/nginx/.htpasswd" ]; then
        echo "✅ Web authentication is configured" >> "$risk_assessment_report"
    else
        echo "❌ Web authentication is not configured" >> "$risk_assessment_report"
        security_issues=$((security_issues + 1))
    fi
    
    # Calculate security risk score
    if [ $security_issues -eq 0 ]; then
        echo "✅ No critical security issues found" >> "$risk_assessment_report"
        security_breach_risk=20  # Low risk
    elif [ $security_issues -eq 1 ]; then
        echo "⚠️ One security issue found" >> "$risk_assessment_report"
        security_breach_risk=50  # Medium risk
    else
        echo "❌ Multiple security issues found ($security_issues)" >> "$risk_assessment_report"
        security_breach_risk=80  # High risk
    fi
    echo "" >> "$risk_assessment_report"
    
    # Calculate weighted technical risk score
    echo "Technical Risk Scores:" >> "$risk_assessment_report"
    echo "---------------------" >> "$risk_assessment_report"
    echo "System Failure Risk: ${system_failure_risk}/100" >> "$risk_assessment_report"
    echo "Data Loss Risk: ${data_loss_risk}/100" >> "$risk_assessment_report"
    echo "Performance Degradation Risk: ${performance_degradation_risk}/100" >> "$risk_assessment_report"
    echo "Security Breach Risk: ${security_breach_risk}/100" >> "$risk_assessment_report"
    echo "" >> "$risk_assessment_report"
    
    # Calculate overall technical risk
    local overall_tech_risk=$(echo "scale=2; ($system_failure_risk + $data_loss_risk + $performance_degradation_risk + $security_breach_risk) / 4" | bc)
    
    echo "Overall Technical Risk Score: ${overall_tech_risk}/100" >> "$risk_assessment_report"
    echo "" >> "$risk_assessment_report"
    
    # Risk classification
    echo "Risk Classification:" >> "$risk_assessment_report"
    echo "-------------------" >> "$risk_assessment_report"
    
    if (( $(echo "$overall_tech_risk < 30" | bc -l) )); then
        echo "✅ LOW RISK: Technical infrastructure is stable and secure" >> "$risk_assessment_report"
        local risk_level="LOW"
    elif (( $(echo "$overall_tech_risk < 60" | bc -l) )); then
        echo "⚠️ MEDIUM RISK: Some technical issues require attention" >> "$risk_assessment_report"
        local risk_level="MEDIUM"
    elif (( $(echo "$overall_tech_risk < 80" | bc -l) )); then
        echo "❌ HIGH RISK: Significant technical issues require immediate attention" >> "$risk_assessment_report"
        local risk_level="HIGH"
    else
        echo "💥 CRITICAL RISK: Severe technical issues threaten system stability" >> "$risk_assessment_report"
        local risk_level="CRITICAL"
    fi
    echo "" >> "$risk_assessment_report"
    
    # Recommendations
    echo "Recommendations:" >> "$risk_assessment_report"
    echo "--------------" >> "$risk_assessment_report"
    
    case $risk_level in
        "LOW")
            echo "✅ Continue current technical maintenance practices" >> "$risk_assessment_report"
            echo "✅ Schedule regular system health checks" >> "$risk_assessment_report"
            echo "✅ Monitor for emerging technical risks" >> "$risk_assessment_report"
            ;;
        "MEDIUM")
            echo "⚠️ Address identified technical issues promptly" >> "$risk_assessment_report"
            if [ $system_failure_risk -gt 30 ]; then
                echo "   - Investigate system stability issues" >> "$risk_assessment_report"
            fi
            if [ $data_loss_risk -gt 30 ]; then
                echo "   - Review and improve backup procedures" >> "$risk_assessment_report"
            fi
            if [ $performance_degradation_risk -gt 30 ]; then
                echo "   - Optimize system resource usage" >> "$risk_assessment_report"
            fi
            if [ $security_breach_risk -gt 30 ]; then
                echo "   - Address security configuration issues" >> "$risk_assessment_report"
            fi
            echo "✅ Implement preventive measures" >> "$risk_assessment_report"
            ;;
        "HIGH")
            echo "❌ Address critical technical issues immediately" >> "$risk_assessment_report"
            echo "✅ Develop and implement risk mitigation plan" >> "$risk_assessment_report"
            echo "✅ Increase monitoring frequency" >> "$risk_assessment_report"
            if [ $system_failure_risk -gt 50 ]; then
                echo "   - Stabilize critical system services" >> "$risk_assessment_report"
            fi
            if [ $data_loss_risk -gt 50 ]; then
                echo "   - Implement robust backup and recovery" >> "$risk_assessment_report"
            fi
            if [ $performance_degradation_risk -gt 50 ]; then
                echo "   - Optimize system performance immediately" >> "$risk_assessment_report"
            fi
            if [ $security_breach_risk -gt 50 ]; then
                echo "   - Strengthen security configurations" >> "$risk_assessment_report"
            fi
            ;;
        "CRITICAL")
            echo "💥 EMERGENCY: Implement crisis response procedures" >> "$risk_assessment_report"
            echo "✅ Activate emergency response team" >> "$risk_assessment_report"
            echo "✅ Implement immediate risk mitigation measures" >> "$risk_assessment_report"
            echo "✅ Escalate to senior management" >> "$risk_assessment_report"
            if [ $system_failure_risk -gt 70 ]; then
                echo "   - Stabilize system immediately" >> "$risk_assessment_report"
            fi
            if [ $data_loss_risk -gt 70 ]; then
                echo "   - Recover from backups if necessary" >> "$risk_assessment_report"
            fi
            if [ $performance_degradation_risk -gt 70 ]; then
                echo "   - Reduce system load to prevent crash" >> "$risk_assessment_report"
            fi
            if [ $security_breach_risk -gt 70 ]; then
                echo "   - Isolate compromised systems" >> "$risk_assessment_report"
            fi
            ;;
    esac
    echo "" >> "$risk_assessment_report"
    
    # Store risk assessment
    local assessment_file="$RISK_ASSESSMENTS_DIR/technical_$(date +%Y%m%d_%H%M%S).json"
    cat > "$assessment_file" << EOF
{
    "assessment_id": "TECH_$(date +%Y%m%d_%H%M%S)",
    "timestamp": "$(date -Iseconds)",
    "category": "technical",
    "scores": {
        "system_failure": $system_failure_risk,
        "data_loss": $data_loss_risk,
        "performance_degradation": $performance_degradation_risk,
        "security_breach": $security_breach_risk,
        "overall": $overall_tech_risk
    },
    "risk_level": "$risk_level",
    "findings": {
        "system_stability": "$system_uptime_days days uptime",
        "services_down": $services_down,
        "backup_status": "$backup_count backups available",
        "resource_usage": "CPU: ${cpu_usage}%, Memory: ${memory_usage}%, Disk: ${disk_usage}%",
        "security_issues": $security_issues
    },
    "recommendations": [
        "Review system stability",
        "Check backup procedures",
        "Optimize resource usage",
        "Address security issues"
    ]
}
EOF
    
    echo "✅ Technical risk assessment completed"
    echo "📋 Risk assessment report saved to: $risk_assessment_report"
    echo "💾 Risk assessment data saved to: $assessment_file"
    log_message "Technical risk assessment completed: $risk_assessment_report"
    
    # Display summary
    echo ""
    echo "Technical Risk Assessment Summary:"
    echo "  System Failure Risk: ${system_failure_risk}/100"
    echo "  Data Loss Risk: ${data_loss_risk}/100"
    echo "  Performance Degradation Risk: ${performance_degradation_risk}/100"
    echo "  Security Breach Risk: ${security_breach_risk}/100"
    echo "  Overall Technical Risk: ${overall_tech_risk}/100"
    echo "  Risk Level: $risk_level"
    echo "  Report: $risk_assessment_report"
    echo "  Data: $assessment_file"
}

# Function to assess operational risks
assess_operational_risks() {
    log_message "Assessing operational risks"
    
    echo ""
    echo "Assessing Operational Risks..."
    echo "============================="
    
    local operational_risk_report="$RISK_REPORT_DIR/operational_risks_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create operational risk report header
    echo "Atlas Production Operational Risk Assessment" > "$operational_risk_report"
    echo "Generated: $(date)" >> "$operational_risk_report"
    echo "===========================================" >> "$operational_risk_report"
    echo "" >> "$operational_risk_report"
    
    # Get operational risk weight
    local operational_risk_weight=$(jq -r '.risk_categories.operational_risks.weight' "$RISK_CONFIG")
    
    echo "Operational Risk Weight: ${operational_risk_weight}%" >> "$operational_risk_report"
    echo "" >> "$operational_risk_report"
    
    # Initialize operational risk scores
    local process_failure_risk=0
    local human_error_risk=0
    local resource_shortage_risk=0
    local compliance_violation_risk=0
    
    # Assess process failure risk
    echo "Process Failure Risk Assessment:" >> "$operational_risk_report"
    echo "-------------------------------" >> "$operational_risk_report"
    
    # Check if standard operating procedures exist
    local sop_dir="/home/ubuntu/dev/atlas/docs/sop"
    if [ -d "$sop_dir" ]; then
        local sop_count=$(find "$sop_dir" -name "*.md" | wc -l)
        if [ $sop_count -gt 0 ]; then
            echo "✅ Standard operating procedures documented ($sop_count SOPs)" >> "$operational_risk_report"
            process_failure_risk=20  # Low risk
        else
            echo "❌ No standard operating procedures found" >> "$operational_risk_report"
            process_failure_risk=80  # High risk
        fi
    else
        echo "❌ SOP directory not found" >> "$operational_risk_report"
        process_failure_risk=90  # High risk
    fi
    
    # Check change management procedures
    local change_mgmt_script="/home/ubuntu/dev/atlas/scripts/change_management.sh"
    if [ -f "$change_mgmt_script" ]; then
        echo "✅ Change management procedures implemented" >> "$operational_risk_report"
        process_failure_risk=$((process_failure_risk - 10))
    else
        echo "❌ Change management procedures not implemented" >> "$operational_risk_report"
        process_failure_risk=$((process_failure_risk + 20))
    fi
    echo "" >> "$operational_risk_report"
    
    # Assess human error risk
    echo "Human Error Risk Assessment:" >> "$operational_risk_report"
    echo "---------------------------" >> "$operational_risk_report"
    
    # Check if training documentation exists
    local training_docs="/home/ubuntu/dev/atlas/docs/training"
    if [ -d "$training_docs" ]; then
        local training_count=$(find "$training_docs" -name "*.md" | wc -l)
        if [ $training_count -gt 0 ]; then
            echo "✅ Training documentation available ($training_count documents)" >> "$operational_risk_report"
            human_error_risk=30  # Medium-low risk
        else
            echo "❌ Training documentation incomplete" >> "$operational_risk_report"
            human_error_risk=60  # Medium risk
        fi
    else
        echo "❌ Training documentation not found" >> "$operational_risk_report"
        human_error_risk=80  # High risk
    fi
    
    # Check if access controls are properly implemented
    local authorized_users=$(cut -d: -f1 /etc/passwd | wc -l)
    local system_users=$(grep -c "nologin\|false" /etc/passwd)
    local actual_users=$((authorized_users - system_users))
    
    if [ $actual_users -le 5 ]; then
        echo "✅ Limited number of authorized users ($actual_users users)" >> "$operational_risk_report"
        human_error_risk=$((human_error_risk + 10))  # Lower risk with fewer users
    else
        echo "⚠️ Large number of authorized users ($actual_users users)" >> "$operational_risk_report"
        human_error_risk=$((human_error_risk + 30))  # Higher risk with more users
    fi
    echo "" >> "$operational_risk_report"
    
    # Assess resource shortage risk
    echo "Resource Shortage Risk Assessment:" >> "$operational_risk_report"
    echo "---------------------------------" >> "$operational_risk_report"
    
    # Check system resources
    local cpu_count=$(nproc)
    local memory_gb=$(free -g | grep Mem | awk '{print $2}')
    local disk_total_gb=$(df -BG / | tail -1 | awk '{print $2}' | sed 's/G//')
    
    echo "System Resources:" >> "$operational_risk_report"
    echo "  CPU Cores: $cpu_count" >> "$operational_risk_report"
    echo "  Memory: ${memory_gb}GB" >> "$operational_risk_report"
    echo "  Disk Space: ${disk_total_gb}GB" >> "$operational_risk_report"
    
    # Assess if resources are adequate
    if [ $cpu_count -ge 2 ] && [ $memory_gb -ge 4 ] && [ $disk_total_gb -ge 50 ]; then
        echo "✅ System resources appear adequate" >> "$operational_risk_report"
        resource_shortage_risk=20  # Low risk
    elif [ $cpu_count -ge 1 ] && [ $memory_gb -ge 2 ] && [ $disk_total_gb -ge 20 ]; then
        echo "⚠️ System resources are marginal" >> "$operational_risk_report"
        resource_shortage_risk=50  # Medium risk
    else
        echo "❌ System resources are inadequate" >> "$operational_risk_report"
        resource_shortage_risk=80  # High risk
    fi
    
    # Check if auto-scaling is configured
    local scaling_script="/home/ubuntu/dev/atlas/scripts/production_scaling.sh"
    if [ -f "$scaling_script" ]; then
        echo "✅ Auto-scaling capabilities are available" >> "$operational_risk_report"
        resource_shortage_risk=$((resource_shortage_risk - 15))
    else
        echo "❌ Auto-scaling capabilities not configured" >> "$operational_risk_report"
        resource_shortage_risk=$((resource_shortage_risk + 15))
    fi
    echo "" >> "$operational_risk_report"
    
    # Assess compliance violation risk
    echo "Compliance Violation Risk Assessment:" >> "$operational_risk_report"
    echo "------------------------------------" >> "$operational_risk_report"
    
    # Check if compliance monitoring is in place
    local compliance_script="/home/ubuntu/dev/atlas/scripts/compliance_checker.sh"
    if [ -f "$compliance_script" ]; then
        echo "✅ Compliance monitoring is implemented" >> "$operational_risk_report"
        compliance_violation_risk=30  # Medium-low risk
    else
        echo "❌ Compliance monitoring not implemented" >> "$operational_risk_report"
        compliance_violation_risk=70  # High risk
    fi
    
    # Check recent compliance reports
    local compliance_reports=$(find "$RISK_REPORT_DIR" -name "compliance_*.txt" -mtime -30 2>/dev/null | wc -l)
    if [ $compliance_reports -gt 0 ]; then
        echo "✅ Recent compliance reports available ($compliance_reports reports)" >> "$operational_risk_report"
        compliance_violation_risk=$((compliance_violation_risk - 20))
    else
        echo "❌ No recent compliance reports found" >> "$operational_risk_report"
        compliance_violation_risk=$((compliance_violation_risk + 10))
    fi
    echo "" >> "$operational_risk_report"
    
    # Calculate weighted operational risk score
    echo "Operational Risk Scores:" >> "$operational_risk_report"
    echo "-----------------------" >> "$operational_risk_report"
    echo "Process Failure Risk: ${process_failure_risk}/100" >> "$operational_risk_report"
    echo "Human Error Risk: ${human_error_risk}/100" >> "$operational_risk_report"
    echo "Resource Shortage Risk: ${resource_shortage_risk}/100" >> "$operational_risk_report"
    echo "Compliance Violation Risk: ${compliance_violation_risk}/100" >> "$operational_risk_report"
    echo "" >> "$operational_risk_report"
    
    # Calculate overall operational risk
    local overall_operational_risk=$(echo "scale=2; ($process_failure_risk + $human_error_risk + $resource_shortage_risk + $compliance_violation_risk) / 4" | bc)
    
    echo "Overall Operational Risk Score: ${overall_operational_risk}/100" >> "$operational_risk_report"
    echo "" >> "$operational_risk_report"
    
    # Risk classification
    echo "Risk Classification:" >> "$operational_risk_report"
    echo "-------------------" >> "$operational_risk_report"
    
    if (( $(echo "$overall_operational_risk < 30" | bc -l) )); then
        echo "✅ LOW RISK: Operational processes are well-managed" >> "$operational_risk_report"
        local risk_level="LOW"
    elif (( $(echo "$overall_operational_risk < 60" | bc -l) )); then
        echo "⚠️ MEDIUM RISK: Some operational issues require attention" >> "$risk_assessment_report"
        local risk_level="MEDIUM"
    elif (( $(echo "$overall_operational_risk < 80" | bc -l) )); then
        echo "❌ HIGH RISK: Significant operational issues require immediate attention" >> "$operational_risk_report"
        local risk_level="HIGH"
    else
        echo "💥 CRITICAL RISK: Severe operational issues threaten business continuity" >> "$operational_risk_report"
        local risk_level="CRITICAL"
    fi
    echo "" >> "$operational_risk_report"
    
    # Recommendations
    echo "Recommendations:" >> "$operational_risk_report"
    echo "--------------" >> "$operational_risk_report"
    
    case $risk_level in
        "LOW")
            echo "✅ Continue current operational practices" >> "$operational_risk_report"
            echo "✅ Schedule regular operational reviews" >> "$operational_risk_report"
            echo "✅ Monitor for operational efficiency improvements" >> "$operational_risk_report"
            ;;
        "MEDIUM")
            echo "⚠️ Address identified operational issues" >> "$operational_risk_report"
            if [ $process_failure_risk -gt 30 ]; then
                echo "   - Improve standard operating procedures" >> "$operational_risk_report"
            fi
            if [ $human_error_risk -gt 30 ]; then
                echo "   - Enhance training programs" >> "$operational_risk_report"
            fi
            if [ $resource_shortage_risk -gt 30 ]; then
                echo "   - Review resource allocation" >> "$operational_risk_report"
            fi
            if [ $compliance_violation_risk -gt 30 ]; then
                echo "   - Strengthen compliance monitoring" >> "$operational_risk_report"
            fi
            echo "✅ Implement preventive operational measures" >> "$operational_risk_report"
            ;;
        "HIGH")
            echo "❌ Address critical operational issues immediately" >> "$operational_risk_report"
            echo "✅ Develop and implement operational risk mitigation plan" >> "$operational_risk_report"
            echo "✅ Increase operational monitoring frequency" >> "$operational_risk_report"
            if [ $process_failure_risk -gt 50 ]; then
                echo "   - Stabilize operational processes" >> "$operational_risk_report"
            fi
            if [ $human_error_risk -gt 50 ]; then
                echo "   - Implement additional training" >> "$operational_risk_report"
            fi
            if [ $resource_shortage_risk -gt 50 ]; then
                echo "   - Address resource limitations" >> "$operational_risk_report"
            fi
            if [ $compliance_violation_risk -gt 50 ]; then
                echo "   - Strengthen compliance procedures" >> "$operational_risk_report"
            fi
            ;;
        "CRITICAL")
            echo "💥 EMERGENCY: Implement operational crisis response procedures" >> "$operational_risk_report"
            echo "✅ Activate operational emergency response team" >> "$operational_risk_report"
            echo "✅ Implement immediate operational risk mitigation measures" >> "$operational_risk_report"
            echo "✅ Escalate to senior management" >> "$operational_risk_report"
            if [ $process_failure_risk -gt 70 ]; then
                echo "   - Stabilize critical operational processes" >> "$operational_risk_report"
            fi
            if [ $human_error_risk -gt 70 ]; then
                echo "   - Implement emergency operational procedures" >> "$operational_risk_report"
            fi
            if [ $resource_shortage_risk -gt 70 ]; then
                echo "   - Secure additional operational resources" >> "$operational_risk_report"
            fi
            if [ $compliance_violation_risk -gt 70 ]; then
                echo "   - Address compliance violations immediately" >> "$operational_risk_report"
            fi
            ;;
    esac
    echo "" >> "$operational_risk_report"
    
    # Store operational risk assessment
    local op_assessment_file="$RISK_ASSESSMENTS_DIR/operational_$(date +%Y%m%d_%H%M%S).json"
    cat > "$op_assessment_file" << EOF
{
    "assessment_id": "OP_$(date +%Y%m%d_%H%M%S)",
    "timestamp": "$(date -Iseconds)",
    "category": "operational",
    "scores": {
        "process_failure": $process_failure_risk,
        "human_error": $human_error_risk,
        "resource_shortage": $resource_shortage_risk,
        "compliance_violation": $compliance_violation_risk,
        "overall": $overall_operational_risk
    },
    "risk_level": "$risk_level",
    "findings": {
        "sop_count": $sop_count,
        "training_docs": $training_count,
        "authorized_users": $actual_users,
        "system_resources": "CPU: $cpu_count, Memory: ${memory_gb}GB, Disk: ${disk_total_gb}GB",
        "compliance_reports": $compliance_reports
    },
    "recommendations": [
        "Review operational procedures",
        "Enhance training programs",
        "Address resource limitations",
        "Strengthen compliance monitoring"
    ]
}
EOF
    
    echo "✅ Operational risk assessment completed"
    echo "📋 Risk assessment report saved to: $operational_risk_report"
    echo "💾 Risk assessment data saved to: $op_assessment_file"
    log_message "Operational risk assessment completed: $operational_risk_report"
    
    # Display summary
    echo ""
    echo "Operational Risk Assessment Summary:"
    echo "  Process Failure Risk: ${process_failure_risk}/100"
    echo "  Human Error Risk: ${human_error_risk}/100"
    echo "  Resource Shortage Risk: ${resource_shortage_risk}/100"
    echo "  Compliance Violation Risk: ${compliance_violation_risk}/100"
    echo "  Overall Operational Risk: ${overall_operational_risk}/100"
    echo "  Risk Level: $risk_level"
    echo "  Report: $operational_risk_report"
    echo "  Data: $op_assessment_file"
}

# Function to assess business risks
assess_business_risks() {
    log_message "Assessing business risks"
    
    echo ""
    echo "Assessing Business Risks..."
    echo "=========================="
    
    local business_risk_report="$RISK_REPORT_DIR/business_risks_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create business risk report header
    echo "Atlas Production Business Risk Assessment" > "$business_risk_report"
    echo "Generated: $(date)" >> "$business_risk_report"
    echo "========================================" >> "$business_risk_report"
    echo "" >> "$business_risk_report"
    
    # Get business risk weight
    local business_risk_weight=$(jq -r '.risk_categories.business_risks.weight' "$RISK_CONFIG")
    
    echo "Business Risk Weight: ${business_risk_weight}%" >> "$business_risk_report"
    echo "" >> "$business_risk_report"
    
    # Initialize business risk scores
    local revenue_loss_risk=0
    local reputation_damage_risk=0
    local competitive_disadvantage_risk=0
    local regulatory_penalty_risk=0
    
    # Assess revenue loss risk
    echo "Revenue Loss Risk Assessment:" >> "$business_risk_report"
    echo "----------------------------" >> "$business_risk_report"
    
    # Check service availability
    local service_uptime=$(uptime | awk -F'load average:' '{print $2}' | xargs | awk '{print $1}' | cut -d',' -f1)
    if (( $(echo "$service_uptime < 1.0" | bc -l) )); then
        echo "✅ Service uptime is excellent (load: $service_uptime)" >> "$business_risk_report"
        revenue_loss_risk=10  # Low risk
    elif (( $(echo "$service_uptime < 2.0" | bc -l) )); then
        echo "⚠️ Service uptime is good (load: $service_uptime)" >> "$business_risk_report"
        revenue_loss_risk=30  # Medium-low risk
    else
        echo "❌ Service uptime needs improvement (load: $service_uptime)" >> "$business_risk_report"
        revenue_loss_risk=70  # High risk
    fi
    
    # Check if business continuity plan exists
    local bc_plan="/home/ubuntu/dev/atlas/scripts/business_continuity.sh"
    if [ -f "$bc_plan" ]; then
        echo "✅ Business continuity plan is implemented" >> "$business_risk_report"
        revenue_loss_risk=$((revenue_loss_risk - 15))
    else
        echo "❌ Business continuity plan not implemented" >> "$business_risk_report"
        revenue_loss_risk=$((revenue_loss_risk + 20))
    fi
    echo "" >> "$business_risk_report"
    
    # Assess reputation damage risk
    echo "Reputation Damage Risk Assessment:" >> "$business_risk_report"
    echo "---------------------------------" >> "$business_risk_report"
    
    # Check if security breach response plan exists
    local incident_response="/home/ubuntu/dev/atlas/scripts/incident_response.sh"
    if [ -f "$incident_response" ]; then
        echo "✅ Incident response procedures are implemented" >> "$business_risk_report"
        reputation_damage_risk=20  # Low risk
    else
        echo "❌ Incident response procedures not implemented" >> "$business_risk_report"
        reputation_damage_risk=60  # High risk
    fi
    
    # Check if monitoring and alerting are in place
    if systemctl is-active --quiet atlas-prometheus && systemctl is-active --quiet atlas-grafana; then
        echo "✅ Monitoring and alerting systems are active" >> "$business_risk_report"
        reputation_damage_risk=$((reputation_damage_risk - 10))
    else
        echo "❌ Monitoring and alerting systems are not active" >> "$business_risk_report"
        reputation_damage_risk=$((reputation_damage_risk + 20))
    fi
    echo "" >> "$business_risk_report"
    
    # Assess competitive disadvantage risk
    echo "Competitive Disadvantage Risk Assessment:" >> "$business_risk_report"
    echo "---------------------------------------" >> "$business_risk_report"
    
    # Check system performance compared to industry standards
    local current_cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local current_memory=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    local current_disk=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "Current Performance Metrics:" >> "$business_risk_report"
    echo "  CPU Usage: ${current_cpu}%" >> "$business_risk_report"
    echo "  Memory Usage: ${current_memory}%" >> "$business_risk_report"
    echo "  Disk Usage: ${current_disk}%" >> "$business_risk_report"
    
    # Assess competitive position based on performance
    if [ $current_cpu -lt 50 ] && [ $current_memory -lt 60 ] && [ $current_disk -lt 70 ]; then
        echo "✅ System performance is competitive" >> "$business_risk_report"
        competitive_disadvantage_risk=20  # Low risk
    elif [ $current_cpu -lt 70 ] && [ $current_memory -lt 80 ] && [ $current_disk -lt 85 ]; then
        echo "⚠️ System performance is acceptable but could be improved" >> "$business_risk_report"
        competitive_disadvantage_risk=50  # Medium risk
    else
        echo "❌ System performance may put us at a competitive disadvantage" >> "$business_risk_report"
        competitive_disadvantage_risk=80  # High risk
    fi
    
    # Check if performance optimization is ongoing
    local perf_tuning_script="/home/ubuntu/dev/atlas/scripts/performance_tuning.sh"
    if [ -f "$perf_tuning_script" ]; then
        echo "✅ Performance tuning procedures are implemented" >> "$business_risk_report"
        competitive_disadvantage_risk=$((competitive_disadvantage_risk - 15))
    else
        echo "❌ Performance tuning procedures not implemented" >> "$business_risk_report"
        competitive_disadvantage_risk=$((competitive_disadvantage_risk + 15))
    fi
    echo "" >> "$business_risk_report"
    
    # Assess regulatory penalty risk
    echo "Regulatory Penalty Risk Assessment:" >> "$business_risk_report"
    echo "----------------------------------" >> "$business_risk_report"
    
    # Check if compliance monitoring is in place
    local compliance_script="/home/ubuntu/dev/atlas/scripts/compliance_checker.sh"
    if [ -f "$compliance_script" ]; then
        echo "✅ Regulatory compliance monitoring is implemented" >> "$business_risk_report"
        regulatory_penalty_risk=30  # Medium-low risk
    else
        echo "❌ Regulatory compliance monitoring not implemented" >> "$business_risk_report"
        regulatory_penalty_risk=70  # High risk
    fi
    
    # Check recent compliance reports
    local compliance_reports=$(find "$RISK_REPORT_DIR" -name "compliance_*.txt" -mtime -30 2>/dev/null | wc -l)
    if [ $compliance_reports -gt 0 ]; then
        echo "✅ Recent compliance reports available ($compliance_reports reports)" >> "$business_risk_report"
        regulatory_penalty_risk=$((regulatory_penalty_risk - 20))
    else
        echo "❌ No recent compliance reports found" >> "$business_risk_report"
        regulatory_penalty_risk=$((regulatory_penalty_risk + 10))
    fi
    echo "" >> "$business_risk_report"
    
    # Calculate weighted business risk score
    echo "Business Risk Scores:" >> "$business_risk_report"
    echo "--------------------" >> "$business_risk_report"
    echo "Revenue Loss Risk: ${revenue_loss_risk}/100" >> "$business_risk_report"
    echo "Reputation Damage Risk: ${reputation_damage_risk}/100" >> "$business_risk_report"
    echo "Competitive Disadvantage Risk: ${competitive_disadvantage_risk}/100" >> "$business_risk_report"
    echo "Regulatory Penalty Risk: ${regulatory_penalty_risk}/100" >> "$business_risk_report"
    echo "" >> "$business_risk_report"
    
    # Calculate overall business risk
    local overall_business_risk=$(echo "scale=2; ($revenue_loss_risk + $reputation_damage_risk + $competitive_disadvantage_risk + $regulatory_penalty_risk) / 4" | bc)
    
    echo "Overall Business Risk Score: ${overall_business_risk}/100" >> "$business_risk_report"
    echo "" >> "$business_risk_report"
    
    # Risk classification
    echo "Risk Classification:" >> "$business_risk_report"
    echo "-------------------" >> "$business_risk_report"
    
    if (( $(echo "$overall_business_risk < 30" | bc -l) )); then
        echo "✅ LOW RISK: Business operations are stable and compliant" >> "$business_risk_report"
        local risk_level="LOW"
    elif (( $(echo "$overall_business_risk < 60" | bc -l) )); then
        echo "⚠️ MEDIUM RISK: Some business risks require attention" >> "$business_risk_report"
        local risk_level="MEDIUM"
    elif (( $(echo "$overall_business_risk < 80" | bc -l) )); then
        echo "❌ HIGH RISK: Significant business risks require immediate attention" >> "$business_risk_report"
        local risk_level="HIGH"
    else
        echo "💥 CRITICAL RISK: Severe business risks threaten organizational viability" >> "$business_risk_report"
        local risk_level="CRITICAL"
    fi
    echo "" >> "$business_risk_report"
    
    # Recommendations
    echo "Recommendations:" >> "$business_risk_report"
    echo "--------------" >> "$business_risk_report"
    
    case $risk_level in
        "LOW")
            echo "✅ Continue current business risk management practices" >> "$business_risk_report"
            echo "✅ Schedule regular business risk assessments" >> "$business_risk_report"
            echo "✅ Monitor for emerging business risks" >> "$business_risk_report"
            ;;
        "MEDIUM")
            echo "⚠️ Address identified business risks" >> "$business_risk_report"
            if [ $revenue_loss_risk -gt 30 ]; then
                echo "   - Improve service availability and uptime" >> "$business_risk_report"
            fi
            if [ $reputation_damage_risk -gt 30 ]; then
                echo "   - Strengthen incident response capabilities" >> "$business_risk_report"
            fi
            if [ $competitive_disadvantage_risk -gt 30 ]; then
                echo "   - Optimize system performance" >> "$business_risk_report"
            fi
            if [ $regulatory_penalty_risk -gt 30 ]; then
                echo "   - Enhance compliance monitoring" >> "$business_risk_report"
            fi
            echo "✅ Implement preventive business measures" >> "$business_risk_report"
            ;;
        "HIGH")
            echo "❌ Address critical business risks immediately" >> "$business_risk_report"
            echo "✅ Develop and implement business risk mitigation plan" >> "$business_risk_report"
            echo "✅ Increase business risk monitoring frequency" >> "$business_risk_report"
            if [ $revenue_loss_risk -gt 50 ]; then
                echo "   - Stabilize business operations" >> "$business_risk_report"
            fi
            if [ $reputation_damage_risk -gt 50 ]; then
                echo "   - Implement comprehensive incident response" >> "$business_risk_report"
            fi
            if [ $competitive_disadvantage_risk -gt 50 ]; then
                echo "   - Accelerate performance optimization" >> "$business_risk_report"
            fi
            if [ $regulatory_penalty_risk -gt 50 ]; then
                echo "   - Strengthen regulatory compliance" >> "$business_risk_report"
            fi
            ;;
        "CRITICAL")
            echo "💥 EMERGENCY: Implement business crisis response procedures" >> "$business_risk_report"
            echo "✅ Activate business emergency response team" >> "$business_risk_report"
            echo "✅ Implement immediate business risk mitigation measures" >> "$business_risk_report"
            echo "✅ Escalate to senior management" >> "$business_risk_report"
            if [ $revenue_loss_risk -gt 70 ]; then
                echo "   - Stabilize critical business operations" >> "$business_risk_report"
            fi
            if [ $reputation_damage_risk -gt 70 ]; then
                echo "   - Implement emergency crisis management" >> "$business_risk_report"
            fi
            if [ $competitive_disadvantage_risk -gt 70 ]; then
                echo "   - Address competitive positioning immediately" >> "$business_risk_report"
            fi
            if [ $regulatory_penalty_risk -gt 70 ]; then
                echo "   - Address regulatory compliance violations" >> "$business_risk_report"
            fi
            ;;
    esac
    echo "" >> "$business_risk_report"
    
    # Store business risk assessment
    local business_assessment_file="$RISK_ASSESSMENTS_DIR/business_$(date +%Y%m%d_%H%M%S).json"
    cat > "$business_assessment_file" << EOF
{
    "assessment_id": "BUS_$(date +%Y%m%d_%H%M%S)",
    "timestamp": "$(date -Iseconds)",
    "category": "business",
    "scores": {
        "revenue_loss": $revenue_loss_risk,
        "reputation_damage": $reputation_damage_risk,
        "competitive_disadvantage": $competitive_disadvantage_risk,
        "regulatory_penalty": $regulatory_penalty_risk,
        "overall": $overall_business_risk
    },
    "risk_level": "$risk_level",
    "findings": {
        "system_performance": "CPU: ${current_cpu}%, Memory: ${current_memory}%, Disk: ${current_disk}%",
        "service_uptime": "Load: $service_uptime",
        "compliance_reports": $compliance_reports,
        "performance_metrics": "Competitive: $competitive_disadvantage_risk, Reputation: $reputation_damage_risk"
    },
    "recommendations": [
        "Improve service availability",
        "Strengthen incident response",
        "Optimize system performance",
        "Enhance regulatory compliance"
    ]
}
EOF
    
    echo "✅ Business risk assessment completed"
    echo "📋 Risk assessment report saved to: $business_risk_report"
    echo "💾 Risk assessment data saved to: $business_assessment_file"
    log_message "Business risk assessment completed: $business_risk_report"
    
    # Display summary
    echo ""
    echo "Business Risk Assessment Summary:"
    echo "  Revenue Loss Risk: ${revenue_loss_risk}/100"
    echo "  Reputation Damage Risk: ${reputation_damage_risk}/100"
    echo "  Competitive Disadvantage Risk: ${competitive_disadvantage_risk}/100"
    echo "  Regulatory Penalty Risk: ${regulatory_penalty_risk}/100"
    echo "  Overall Business Risk: ${overall_business_risk}/100"
    echo "  Risk Level: $risk_level"
    echo "  Report: $business_risk_report"
    echo "  Data: $business_assessment_file"
}

# Function to assess external risks
assess_external_risks() {
    log_message "Assessing external risks"
    
    echo ""
    echo "Assessing External Risks..."
    echo "=========================="
    
    local external_risk_report="$RISK_REPORT_DIR/external_risks_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create external risk report header
    echo "Atlas Production External Risk Assessment" > "$external_risk_report"
    echo "Generated: $(date)" >> "$external_risk_report"
    echo "========================================" >> "$external_risk_report"
    echo "" >> "$external_risk_report"
    
    # Get external risk weight
    local external_risk_weight=$(jq -r '.risk_categories.external_risks.weight' "$RISK_CONFIG")
    
    echo "External Risk Weight: ${external_risk_weight}%" >> "$external_risk_report"
    echo "" >> "$external_risk_report"
    
    # Initialize external risk scores
    local vendor_failure_risk=0
    local market_changes_risk=0
    local natural_disasters_risk=0
    local cyber_attacks_risk=0
    
    # Assess vendor failure risk
    echo "Vendor Failure Risk Assessment:" >> "$external_risk_report"
    echo "------------------------------" >> "$external_risk_report"
    
    # Check if vendor management processes exist
    local vendor_docs="/home/ubuntu/dev/atlas/docs/vendor"
    if [ -d "$vendor_docs" ]; then
        local vendor_count=$(find "$vendor_docs" -name "*.md" | wc -l)
        if [ $vendor_count -gt 0 ]; then
            echo "✅ Vendor management documentation exists ($vendor_count vendors)" >> "$external_risk_report"
            vendor_failure_risk=30  # Medium-low risk
        else
            echo "❌ Vendor management documentation is incomplete" >> "$external_risk_report"
            vendor_failure_risk=60  # Medium risk
        fi
    else
        echo "❌ Vendor management documentation not found" >> "$external_risk_report"
        vendor_failure_risk=80  # High risk
    fi
    
    # Check if vendor redundancy exists
    local vendor_redundancy_script="/home/ubuntu/dev/atlas/scripts/vendor_redundancy.sh"
    if [ -f "$vendor_redundancy_script" ]; then
        echo "✅ Vendor redundancy procedures are implemented" >> "$external_risk_report"
        vendor_failure_risk=$((vendor_failure_risk - 20))
    else
        echo "❌ Vendor redundancy procedures not implemented" >> "$external_risk_report"
        vendor_failure_risk=$((vendor_failure_risk + 20))
    fi
    echo "" >> "$external_risk_report"
    
    # Assess market changes risk
    echo "Market Changes Risk Assessment:" >> "$external_risk_report"
    echo "------------------------------" >> "$external_risk_report"
    
    # Check if market monitoring processes exist
    local market_monitoring_script="/home/ubuntu/dev/atlas/scripts/market_monitoring.sh"
    if [ -f "$market_monitoring_script" ]; then
        echo "✅ Market monitoring processes are implemented" >> "$external_risk_report"
        market_changes_risk=40  # Medium risk
    else
        echo "❌ Market monitoring processes not implemented" >> "$external_risk_report"
        market_changes_risk=70  # High risk
    fi
    
    # Check if competitive analysis is performed
    local competitive_analysis_script="/home/ubuntu/dev/atlas/scripts/competitive_analysis.sh"
    if [ -f "$competitive_analysis_script" ]; then
        echo "✅ Competitive analysis is performed regularly" >> "$external_risk_report"
        market_changes_risk=$((market_changes_risk - 15))
    else
        echo "❌ Competitive analysis is not performed regularly" >> "$external_risk_report"
        market_changes_risk=$((market_changes_risk + 15))
    fi
    echo "" >> "$external_risk_report"
    
    # Assess natural disasters risk
    echo "Natural Disasters Risk Assessment:" >> "$external_risk_report"
    echo "--------------------------------" >> "$external_risk_report"
    
    # Check if disaster recovery plan exists
    local dr_plan="/home/ubuntu/dev/atlas/scripts/disaster_recovery.sh"
    if [ -f "$dr_plan" ]; then
        echo "✅ Disaster recovery plan is implemented" >> "$external_risk_report"
        natural_disasters_risk=30  # Medium-low risk
    else
        echo "❌ Disaster recovery plan not implemented" >> "$external_risk_report"
        natural_disasters_risk=80  # High risk
    fi
    
    # Check if backups are geographically distributed
    local geo_backup_check=$(find "/home/ubuntu/dev/atlas/backups" -name "*.sql*" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
    if [ ! -z "$geo_backup_check" ]; then
        echo "✅ Backup systems are in place" >> "$external_risk_report"
        natural_disasters_risk=$((natural_disasters_risk - 10))
    else
        echo "❌ Backup systems may be insufficient" >> "$external_risk_report"
        natural_disasters_risk=$((natural_disasters_risk + 10))
    fi
    echo "" >> "$external_risk_report"
    
    # Assess cyber attacks risk
    echo "Cyber Attacks Risk Assessment:" >> "$external_risk_report"
    echo "-----------------------------" >> "$external_risk_report"
    
    # Check if security monitoring is in place
    if systemctl is-active --quiet atlas-prometheus && systemctl is-active --quiet atlas-grafana; then
        echo "✅ Security monitoring systems are active" >> "$external_risk_report"
        cyber_attacks_risk=40  # Medium risk
    else
        echo "❌ Security monitoring systems are not active" >> "$external_risk_report"
        cyber_attacks_risk=80  # High risk
    fi
    
    # Check if intrusion detection is implemented
    local ids_script="/home/ubuntu/dev/atlas/scripts/intrusion_detection.sh"
    if [ -f "$ids_script" ]; then
        echo "✅ Intrusion detection systems are implemented" >> "$external_risk_report"
        cyber_attacks_risk=$((cyber_attacks_risk - 20))
    else
        echo "❌ Intrusion detection systems not implemented" >> "$external_risk_report"
        cyber_attacks_risk=$((cyber_attacks_risk + 20))
    fi
    
    # Check if regular security assessments are performed
    local security_assessment_script="/home/ubuntu/dev/atlas/scripts/security_scanner.sh"
    if [ -f "$security_assessment_script" ]; then
        echo "✅ Regular security assessments are performed" >> "$external_risk_report"
        cyber_attacks_risk=$((cyber_attacks_risk - 15))
    else
        echo "❌ Regular security assessments are not performed" >> "$external_risk_report"
        cyber_attacks_risk=$((cyber_attacks_risk + 15))
    fi
    echo "" >> "$external_risk_report"
    
    # Calculate weighted external risk score
    echo "External Risk Scores:" >> "$external_risk_report"
    echo "--------------------" >> "$external_risk_report"
    echo "Vendor Failure Risk: ${vendor_failure_risk}/100" >> "$external_risk_report"
    echo "Market Changes Risk: ${market_changes_risk}/100" >> "$external_risk_report"
    echo "Natural Disasters Risk: ${natural_disasters_risk}/100" >> "$external_risk_report"
    echo "Cyber Attacks Risk: ${cyber_attacks_risk}/100" >> "$external_risk_report"
    echo "" >> "$external_risk_report"
    
    # Calculate overall external risk
    local overall_external_risk=$(echo "scale=2; ($vendor_failure_risk + $market_changes_risk + $natural_disasters_risk + $cyber_attacks_risk) / 4" | bc)
    
    echo "Overall External Risk Score: ${overall_external_risk}/100" >> "$external_risk_report"
    echo "" >> "$external_risk_report"
    
    # Risk classification
    echo "Risk Classification:" >> "$external_risk_report"
    echo "-------------------" >> "$external_risk_report"
    
    if (( $(echo "$overall_external_risk < 30" | bc -l) )); then
        echo "✅ LOW RISK: External risks are well-managed" >> "$external_risk_report"
        local risk_level="LOW"
    elif (( $(echo "$overall_external_risk < 60" | bc -l) )); then
        echo "⚠️ MEDIUM RISK: Some external risks require attention" >> "$external_risk_report"
        local risk_level="MEDIUM"
    elif (( $(echo "$overall_external_risk < 80" | bc -l) )); then
        echo "❌ HIGH RISK: Significant external risks require immediate attention" >> "$external_risk_report"
        local risk_level="HIGH"
    else
        echo "💥 CRITICAL RISK: Severe external risks threaten business continuity" >> "$external_risk_report"
        local risk_level="CRITICAL"
    fi
    echo "" >> "$external_risk_report"
    
    # Recommendations
    echo "Recommendations:" >> "$external_risk_report"
    echo "--------------" >> "$external_risk_report"
    
    case $risk_level in
        "LOW")
            echo "✅ Continue current external risk management practices" >> "$external_risk_report"
            echo "✅ Schedule regular external risk assessments" >> "$external_risk_report"
            echo "✅ Monitor for emerging external risks" >> "$external_risk_report"
            ;;
        "MEDIUM")
            echo "⚠️ Address identified external risks" >> "$external_risk_report"
            if [ $vendor_failure_risk -gt 30 ]; then
                echo "   - Strengthen vendor management processes" >> "$external_risk_report"
            fi
            if [ $market_changes_risk -gt 30 ]; then
                echo "   - Implement market monitoring" >> "$external_risk_report"
            fi
            if [ $natural_disasters_risk -gt 30 ]; then
                echo "   - Review disaster recovery plans" >> "$external_risk_report"
            fi
            if [ $cyber_attacks_risk -gt 30 ]; then
                echo "   - Enhance cybersecurity measures" >> "$external_risk_report"
            fi
            echo "✅ Implement preventive external risk measures" >> "$external_risk_report"
            ;;
        "HIGH")
            echo "❌ Address critical external risks immediately" >> "$external_risk_report"
            echo "✅ Develop and implement external risk mitigation plan" >> "$external_risk_report"
            echo "✅ Increase external risk monitoring frequency" >> "$external_risk_report"
            if [ $vendor_failure_risk -gt 50 ]; then
                echo "   - Strengthen vendor relationships" >> "$external_risk_report"
            fi
            if [ $market_changes_risk -gt 50 ]; then
                echo "   - Accelerate market monitoring" >> "$external_risk_report"
            fi
            if [ $natural_disasters_risk -gt 50 ]; then
                echo "   - Enhance disaster preparedness" >> "$external_risk_report"
            fi
            if [ $cyber_attacks_risk -gt 50 ]; then
                echo "   - Strengthen cybersecurity posture" >> "$external_risk_report"
            fi
            ;;
        "CRITICAL")
            echo "💥 EMERGENCY: Implement external risk crisis response procedures" >> "$external_risk_report"
            echo "✅ Activate external risk emergency response team" >> "$external_risk_report"
            echo "✅ Implement immediate external risk mitigation measures" >> "$external_risk_report"
            echo "✅ Escalate to senior management" >> "$external_risk_report"
            if [ $vendor_failure_risk -gt 70 ]; then
                echo "   - Secure alternative vendor arrangements" >> "$external_risk_report"
            fi
            if [ $market_changes_risk -gt 70 ]; then
                echo "   - Implement emergency market response" >> "$external_risk_report"
            fi
            if [ $natural_disasters_risk -gt 70 ]; then
                echo "   - Activate disaster recovery procedures" >> "$external_risk_report"
            fi
            if [ $cyber_attacks_risk -gt 70 ]; then
                echo "   - Implement cybersecurity emergency response" >> "$external_risk_report"
            fi
            ;;
    esac
    echo "" >> "$external_risk_report"
    
    # Store external risk assessment
    local external_assessment_file="$RISK_ASSESSMENTS_DIR/external_$(date +%Y%m%d_%H%M%S).json"
    cat > "$external_assessment_file" << EOF
{
    "assessment_id": "EXT_$(date +%Y%m%d_%H%M%S)",
    "timestamp": "$(date -Iseconds)",
    "category": "external",
    "scores": {
        "vendor_failure": $vendor_failure_risk,
        "market_changes": $market_changes_risk,
        "natural_disasters": $natural_disasters_risk,
        "cyber_attacks": $cyber_attacks_risk,
        "overall": $overall_external_risk
    },
    "risk_level": "$risk_level",
    "findings": {
        "vendors_managed": $(if [ -d "$vendor_docs" ]; then find "$vendor_docs" -name "*.md" | wc -l; else echo "0"; fi),
        "security_monitoring": $(if systemctl is-active --quiet atlas-prometheus && systemctl is-active --quiet atlas-grafana; then echo "true"; else echo "false"; fi),
        "disaster_recovery": $(if [ -f "$dr_plan" ]; then echo "true"; else echo "false"; fi),
        "market_monitoring": $(if [ -f "$market_monitoring_script" ]; then echo "true"; else echo "false"; fi)
    },
    "recommendations": [
        "Strengthen vendor management",
        "Implement market monitoring",
        "Review disaster recovery plans",
        "Enhance cybersecurity measures"
    ]
}
EOF
    
    echo "✅ External risk assessment completed"
    echo "📋 Risk assessment report saved to: $external_risk_report"
    echo "💾 Risk assessment data saved to: $external_assessment_file"
    log_message "External risk assessment completed: $external_risk_report"
    
    # Display summary
    echo ""
    echo "External Risk Assessment Summary:"
    echo "  Vendor Failure Risk: ${vendor_failure_risk}/100"
    echo "  Market Changes Risk: ${market_changes_risk}/100"
    echo "  Natural Disasters Risk: ${natural_disasters_risk}/100"
    echo "  Cyber Attacks Risk: ${cyber_attacks_risk}/100"
    echo "  Overall External Risk: ${overall_external_risk}/100"
    echo "  Risk Level: $risk_level"
    echo "  Report: $external_risk_report"
    echo "  Data: $external_assessment_file"
}

# Function to generate risk matrix
generate_risk_matrix() {
    log_message "Generating risk matrix"
    
    echo ""
    echo "Generating Risk Matrix..."
    echo "========================="
    
    local risk_matrix_report="$RISK_REPORT_DIR/risk_matrix_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create risk matrix report header
    echo "Atlas Production Risk Matrix" > "$risk_matrix_report"
    echo "Generated: $(date)" >> "$risk_matrix_report"
    echo "============================" >> "$risk_matrix_report"
    echo "" >> "$risk_matrix_report"
    
    # Get risk categories and weights
    echo "Risk Categories:" >> "$risk_matrix_report"
    echo "---------------" >> "$risk_matrix_report"
    
    local risk_categories=$(jq -r '.risk_categories | keys[]' "$RISK_CONFIG")
    while IFS= read -r category_key; do
        local category_name=$(jq -r ".risk_categories.$category_key.name" "$RISK_CONFIG")
        local category_weight=$(jq -r ".risk_categories.$category_key.weight" "$RISK_CONFIG")
        echo "$category_name (${category_weight}%)" >> "$risk_matrix_report"
    done <<< "$risk_categories"
    echo "" >> "$risk_matrix_report"
    
    # Get recent risk assessments
    echo "Recent Risk Assessments:" >> "$risk_matrix_report"
    echo "-----------------------" >> "$risk_matrix_report"
    
    # Find latest assessments
    local latest_assessments=$(ls -t "$RISK_ASSESSMENTS_DIR"/*.json 2>/dev/null | head -10)
    if [ -z "$latest_assessments" ]; then
        echo "❌ No recent risk assessments found" >> "$risk_matrix_report"
        echo "✅ Risk matrix report generated: $risk_matrix_report"
        log_message "Risk matrix report generated: $risk_matrix_report"
        return 0
    fi
    
    # Process each assessment
    local total_risk_score=0
    local total_weight=0
    local assessment_count=0
    
    while IFS= read -r assessment_file; do
        if [ -f "$assessment_file" ]; then
            local assessment_category=$(jq -r '.category' "$assessment_file")
            local assessment_score=$(jq -r '.scores.overall' "$assessment_file")
            local assessment_level=$(jq -r '.risk_level' "$assessment_file")
            
            # Get category weight
            local category_weight=$(jq -r ".risk_categories.${assessment_category}.weight" "$RISK_CONFIG")
            
            echo "Assessment: $assessment_category" >> "$risk_matrix_report"
            echo "  Overall Score: ${assessment_score}/100" >> "$risk_matrix_report"
            echo "  Risk Level: $assessment_level" >> "$risk_matrix_report"
            echo "  Category Weight: ${category_weight}%" >> "$risk_matrix_report"
            echo "" >> "$risk_matrix_report"
            
            # Calculate weighted score
            local weighted_score=$(echo "scale=2; $assessment_score * $category_weight / 100" | bc)
            total_risk_score=$(echo "scale=2; $total_risk_score + $weighted_score" | bc)
            total_weight=$((total_weight + category_weight))
            assessment_count=$((assessment_count + 1))
        fi
    done <<< "$latest_assessments"
    
    # Calculate overall risk score
    echo "Risk Matrix Summary:" >> "$risk_matrix_report"
    echo "-------------------" >> "$risk_matrix_report"
    echo "Assessments Processed: $assessment_count" >> "$risk_matrix_report"
    echo "Total Weight: ${total_weight}%" >> "$risk_matrix_report"
    echo "Weighted Risk Score: ${total_risk_score}/100" >> "$risk_matrix_report"
    echo "" >> "$risk_matrix_report"
    
    # Risk classification
    echo "Overall Risk Classification:" >> "$risk_matrix_report"
    echo "--------------------------" >> "$risk_matrix_report"
    
    if (( $(echo "$total_risk_score < 30" | bc -l) )); then
        echo "✅ LOW RISK: Organization risk exposure is acceptable" >> "$risk_matrix_report"
        local overall_risk_level="LOW"
    elif (( $(echo "$total_risk_score < 60" | bc -l) )); then
        echo "⚠️ MEDIUM RISK: Organization has moderate risk exposure" >> "$risk_matrix_report"
        local overall_risk_level="MEDIUM"
    elif (( $(echo "$total_risk_score < 80" | bc -l) )); then
        echo "❌ HIGH RISK: Organization has significant risk exposure" >> "$risk_matrix_report"
        local overall_risk_level="HIGH"
    else
        echo "💥 CRITICAL RISK: Organization faces severe risk exposure" >> "$risk_matrix_report"
        local overall_risk_level="CRITICAL"
    fi
    echo "" >> "$risk_matrix_report"
    
    # Risk tolerance check
    echo "Risk Tolerance Check:" >> "$risk_matrix_report"
    echo "--------------------" >> "$risk_matrix_report"
    
    local risk_tolerance=$(jq -r '.risk_management.risk_tolerance' "$RISK_CONFIG")
    echo "Organization Risk Tolerance: $risk_tolerance" >> "$risk_matrix_report"
    echo "Current Risk Exposure: $overall_risk_level" >> "$risk_matrix_report"
    
    case $risk_tolerance in
        "low")
            if [ "$overall_risk_level" = "LOW" ]; then
                echo "✅ Risk exposure is within tolerance" >> "$risk_matrix_report"
            else
                echo "❌ Risk exposure exceeds tolerance" >> "$risk_matrix_report"
            fi
            ;;
        "medium")
            if [ "$overall_risk_level" = "LOW" ] || [ "$overall_risk_level" = "MEDIUM" ]; then
                echo "✅ Risk exposure is within tolerance" >> "$risk_matrix_report"
            else
                echo "❌ Risk exposure exceeds tolerance" >> "$risk_matrix_report"
            fi
            ;;
        "high")
            if [ "$overall_risk_level" = "CRITICAL" ]; then
                echo "❌ Risk exposure exceeds tolerance" >> "$risk_matrix_report"
            else
                echo "✅ Risk exposure is within tolerance" >> "$risk_matrix_report"
            fi
            ;;
    esac
    echo "" >> "$risk_matrix_report"
    
    # Risk mitigation priorities
    echo "Risk Mitigation Priorities:" >> "$risk_matrix_report"
    echo "--------------------------" >> "$risk_matrix_report"
    
    # Identify highest risk assessments
    local highest_risk_score=0
    local highest_risk_category=""
    
    while IFS= read -r assessment_file; do
        if [ -f "$assessment_file" ]; then
            local assessment_category=$(jq -r '.category' "$assessment_file")
            local assessment_score=$(jq -r '.scores.overall' "$assessment_file")
            
            if (( $(echo "$assessment_score > $highest_risk_score" | bc -l) )); then
                highest_risk_score=$assessment_score
                highest_risk_category=$assessment_category
            fi
        fi
    done <<< "$latest_assessments"
    
    if [ ! -z "$highest_risk_category" ]; then
        echo "Highest Risk Category: $highest_risk_category (${highest_risk_score}/100)" >> "$risk_matrix_report"
        echo "   Priority: Address $highest_risk_category risks first" >> "$risk_matrix_report"
    fi
    echo "" >> "$risk_matrix_report"
    
    # Recommendations
    echo "Risk Management Recommendations:" >> "$risk_matrix_report"
    echo "------------------------------" >> "$risk_matrix_report"
    
    case $overall_risk_level in
        "LOW")
            echo "✅ Continue current risk management practices" >> "$risk_matrix_report"
            echo "✅ Schedule regular risk assessments" >> "$risk_matrix_report"
            echo "✅ Monitor for emerging risks" >> "$risk_matrix_report"
            ;;
        "MEDIUM")
            echo "⚠️ Implement risk mitigation measures" >> "$risk_matrix_report"
            echo "✅ Develop detailed risk mitigation plans" >> "$risk_matrix_report"
            echo "✅ Increase risk monitoring frequency" >> "$risk_matrix_report"
            echo "✅ Review risk tolerance levels" >> "$risk_matrix_report"
            ;;
        "HIGH")
            echo "❌ Address critical risk exposures immediately" >> "$risk_matrix_report"
            echo "✅ Develop and implement comprehensive risk mitigation plans" >> "$risk_matrix_report"
            echo "✅ Activate risk management escalation procedures" >> "$risk_matrix_report"
            echo "✅ Engage senior management for risk oversight" >> "$risk_matrix_report"
            ;;
        "CRITICAL")
            echo "💥 EMERGENCY: Implement crisis risk management procedures" >> "$risk_matrix_report"
            echo "✅ Activate enterprise risk management protocols" >> "$risk_matrix_report"
            echo "✅ Engage board-level risk oversight" >> "$risk_matrix_report"
            echo "✅ Implement immediate risk reduction measures" >> "$risk_matrix_report"
            echo "✅ Establish risk management war room" >> "$risk_matrix_report"
            ;;
    esac
    echo "" >> "$risk_matrix_report"
    
    # Risk monitoring
    echo "Risk Monitoring Schedule:" >> "$risk_matrix_report"
    echo "------------------------" >> "$risk_matrix_report"
    
    local assessment_frequency=$(jq -r '.risk_management.assessment_frequency' "$RISK_CONFIG")
    echo "Risk Assessment Frequency: $assessment_frequency" >> "$risk_matrix_report"
    
    local review_process=$(jq -r '.risk_management.review_process' "$RISK_CONFIG")
    echo "Risk Review Process: $review_process" >> "$risk_matrix_report"
    
    local escalation_threshold=$(jq -r '.risk_management.escalation_threshold' "$RISK_CONFIG")
    echo "Risk Escalation Threshold: $escalation_threshold" >> "$risk_matrix_report"
    echo "" >> "$risk_matrix_report"
    
    echo "✅ Risk matrix generated"
    echo "📋 Risk matrix report saved to: $risk_matrix_report"
    log_message "Risk matrix generated: $risk_matrix_report"
    
    # Display summary
    echo ""
    echo "Risk Matrix Summary:"
    echo "  Overall Risk Score: ${total_risk_score}/100"
    echo "  Risk Tolerance: $risk_tolerance"
    echo "  Risk Exposure: $overall_risk_level"
    if (( $(echo "$total_risk_score < 30" | bc -l) )); then
        echo "  Status: ✅ ACCEPTABLE"
    elif (( $(echo "$total_risk_score < 60" | bc -l) )); then
        echo "  Status: ⚠️ MODERATE"
    elif (( $(echo "$total_risk_score < 80" | bc -l) )); then
        echo "  Status: ❌ HIGH"
    else
        echo "  Status: 💥 CRITICAL"
    fi
    echo "  Report: $risk_matrix_report"
}

# Function to create risk mitigation plan
create_mitigation_plan() {
    log_message "Creating risk mitigation plan"
    
    echo ""
    echo "Creating Risk Mitigation Plan..."
    echo "=============================="
    
    local mitigation_plan_report="$RISK_REPORT_DIR/mitigation_plan_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create mitigation plan report header
    echo "Atlas Production Risk Mitigation Plan" > "$mitigation_plan_report"
    echo "Generated: $(date)" >> "$mitigation_plan_report"
    echo "=====================================" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    # Get mitigation strategies
    echo "Mitigation Strategies:" >> "$mitigation_plan_report"
    echo "--------------------" >> "$mitigation_plan_report"
    
    local mitigation_strategies=$(jq -r '.mitigation_strategies | keys[]' "$RISK_CONFIG")
    while IFS= read -r strategy_key; do
        local strategy_name=$(jq -r ".mitigation_strategies.$strategy_key.name" "$RISK_CONFIG")
        local strategy_priority=$(jq -r ".mitigation_strategies.$strategy_key.priority" "$RISK_CONFIG")
        local strategy_budget=$(jq -r ".mitigation_strategies.$strategy_key.budget_allocation" "$RISK_CONFIG")
        
        echo "$strategy_name:" >> "$mitigation_plan_report"
        echo "  Priority: $strategy_priority" >> "$mitigation_plan_report"
        echo "  Budget Allocation: ${strategy_budget}%" >> "$mitigation_plan_report"
        echo "" >> "$mitigation_plan_report"
    done <<< "$mitigation_strategies"
    echo "" >> "$mitigation_plan_report"
    
    # Get recent risk assessments to identify mitigation needs
    echo "Risk Mitigation Priorities:" >> "$mitigation_plan_report"
    echo "--------------------------" >> "$mitigation_plan_report"
    
    local risk_assessments=$(ls -t "$RISK_ASSESSMENTS_DIR"/*.json 2>/dev/null | head -5)
    if [ -z "$risk_assessments" ]; then
        echo "❌ No recent risk assessments found" >> "$mitigation_plan_report"
        echo "✅ Mitigation plan report generated: $mitigation_plan_report"
        log_message "Mitigation plan generated: $mitigation_plan_report"
        return 0
    fi
    
    # Process each assessment to identify mitigation opportunities
    local mitigation_opportunities=0
    
    while IFS= read -r assessment_file; do
        if [ -f "$assessment_file" ]; then
            local assessment_category=$(jq -r '.category' "$assessment_file")
            local assessment_score=$(jq -r '.scores.overall' "$assessment_file")
            local risk_level=$(jq -r '.risk_level' "$assessment_file")
            local recommendations=$(jq -r '.recommendations[]' "$assessment_file")
            
            echo "Category: $assessment_category" >> "$mitigation_plan_report"
            echo "  Risk Level: $risk_level (${assessment_score}/100)" >> "$mitigation_plan_report"
            echo "  Recommended Mitigations:" >> "$mitigation_plan_report"
            
            local rec_count=1
            while IFS= read -r recommendation; do
                echo "    $rec_count. $recommendation" >> "$mitigation_plan_report"
                rec_count=$((rec_count + 1))
                mitigation_opportunities=$((mitigation_opportunities + 1))
            done <<< "$recommendations"
            echo "" >> "$mitigation_plan_report"
        fi
    done <<< "$risk_assessments"
    
    echo "Total Mitigation Opportunities Identified: $mitigation_opportunities" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    # Prioritize mitigation actions
    echo "Prioritized Mitigation Actions:" >> "$mitigation_plan_report"
    echo "------------------------------" >> "$mitigation_plan_report"
    
    # Sort assessments by risk score (highest first)
    local sorted_assessments=$(find "$RISK_ASSESSMENTS_DIR" -name "*.json" -exec jq -r '.scores.overall + " " + .category + " " + .risk_level' {} \; | sort -rn | head -5)
    
    local action_priority=1
    while IFS= read -r sorted_item; do
        local risk_score=$(echo $sorted_item | awk '{print $1}')
        local category=$(echo $sorted_item | awk '{print $2}')
        local risk_level=$(echo $sorted_item | awk '{print $3}')
        
        echo "$action_priority. $category Risk ($risk_level)" >> "$mitigation_plan_report"
        echo "   Risk Score: ${risk_score}/100" >> "$mitigation_plan_report"
        echo "   Action: Address immediately" >> "$mitigation_plan_report"
        echo "" >> "$mitigation_plan_report"
        action_priority=$((action_priority + 1))
    done <<< "$sorted_assessments"
    echo "" >> "$mitigation_plan_report"
    
    # Resource allocation
    echo "Resource Allocation:" >> "$mitigation_plan_report"
    echo "------------------" >> "$mitigation_plan_report"
    
    # Get budget allocations
    while IFS= read -r strategy_key; do
        local strategy_name=$(jq -r ".mitigation_strategies.$strategy_key.name" "$RISK_CONFIG")
        local strategy_budget=$(jq -r ".mitigation_strategies.$strategy_key.budget_allocation" "$RISK_CONFIG")
        
        echo "$strategy_name: ${strategy_budget}%" >> "$mitigation_plan_report"
    done <<< "$mitigation_strategies"
    echo "" >> "$mitigation_plan_report"
    
    # Timeline for mitigation
    echo "Mitigation Timeline:" >> "$mitigation_plan_report"
    echo "------------------" >> "$mitigation_plan_report"
    
    echo "Immediate Actions (0-30 days):" >> "$mitigation_plan_report"
    echo "  - Address critical risk exposures" >> "$mitigation_plan_report"
    echo "  - Implement high-priority mitigations" >> "$mitigation_plan_report"
    echo "  - Engage stakeholders for resource allocation" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    echo "Short-term Actions (30-90 days):" >> "$mitigation_plan_report"
    echo "  - Implement medium-priority mitigations" >> "$mitigation_plan_report"
    echo "  - Develop detailed implementation plans" >> "$mitigation_plan_report"
    echo "  - Monitor mitigation effectiveness" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    echo "Long-term Actions (90+ days):" >> "$mitigation_plan_report"
    echo "  - Implement strategic risk mitigations" >> "$mitigation_plan_report"
    echo "  - Review and update risk management framework" >> "$mitigation_plan_report"
    echo "  - Conduct comprehensive risk reassessment" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    # Success metrics
    echo "Success Metrics:" >> "$mitigation_plan_report"
    echo "---------------" >> "$mitigation_plan_report"
    
    echo "Risk Reduction Targets:" >> "$mitigation_plan_report"
    echo "  - Reduce overall risk score by 25%" >> "$mitigation_plan_report"
    echo "  - Address all critical risk exposures" >> "$mitigation_plan_report"
    echo "  - Achieve acceptable risk tolerance levels" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    echo "Monitoring and Reporting:" >> "$mitigation_plan_report"
    echo "  - Weekly risk score reviews" >> "$mitigation_plan_report"
    echo "  - Monthly mitigation progress reports" >> "$mitigation_plan_report"
    echo "  - Quarterly comprehensive risk assessments" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    # Implementation responsibilities
    echo "Implementation Responsibilities:" >> "$mitigation_plan_report"
    echo "------------------------------" >> "$mitigation_plan_report"
    
    echo "Risk Management Team:" >> "$mitigation_plan_report"
    echo "  - Monitor risk scores and trends" >> "$mitigation_plan_report"
    echo "  - Coordinate mitigation activities" >> "$mitigation_plan_report"
    echo "  - Report on mitigation progress" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    echo "Technical Team:" >> "$mitigation_plan_report"
    echo "  - Implement technical mitigations" >> "$mitigation_plan_report"
    echo "  - Monitor system performance and security" >> "$mitigation_plan_report"
    echo "  - Address technical vulnerabilities" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    echo "Operational Team:" >> "$mitigation_plan_report"
    echo "  - Implement process improvements" >> "$mitigation_plan_report"
    echo "  - Address operational risks" >> "$mitigation_plan_report"
    echo "  - Ensure compliance with procedures" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    echo "Executive Management:" >> "$mitigation_plan_report"
    echo "  - Approve risk mitigation budgets" >> "$mitigation_plan_report"
    echo "  - Provide strategic direction" >> "$mitigation_plan_report"
    echo "  - Review risk management effectiveness" >> "$mitigation_plan_report"
    echo "" >> "$mitigation_plan_report"
    
    echo "✅ Risk mitigation plan generated"
    echo "📋 Mitigation plan report saved to: $mitigation_plan_report"
    log_message "Risk mitigation plan generated: $mitigation_plan_report"
    
    # Display summary
    echo ""
    echo "Risk Mitigation Plan Summary:"
    echo "  Mitigation Opportunities: $mitigation_opportunities"
    echo "  Risk Categories Assessed: $(echo "$risk_assessments" | wc -l)"
    echo "  Strategic Areas: Prevention, Detection, Response"
    echo "  Report: $mitigation_plan_report"
}

# Function to generate risk dashboard
generate_risk_dashboard() {
    log_message "Generating risk dashboard"
    
    echo ""
    echo "Generating Risk Dashboard..."
    echo "=========================="
    
    local risk_dashboard_report="$RISK_REPORT_DIR/risk_dashboard_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create risk dashboard report header
    echo "Atlas Production Risk Dashboard" > "$risk_dashboard_report"
    echo "Generated: $(date)" >> "$risk_dashboard_report"
    echo "===============================" >> "$risk_dashboard_report"
    echo "" >> "$risk_dashboard_report"
    
    # Dashboard header
    echo "RISK DASHBOARD" >> "$risk_dashboard_report"
    echo "=============" >> "$risk_dashboard_report"
    echo "" >> "$risk_dashboard_report"
    
    # Overall risk status
    echo "Overall Risk Status:" >> "$risk_dashboard_report"
    echo "-------------------" >> "$risk_dashboard_report"
    
    # Get latest risk matrix to determine overall risk
    local latest_risk_matrix=$(ls -t "$RISK_REPORT_DIR"/risk_matrix_*.txt 2>/dev/null | head -1)
    if [ ! -z "$latest_risk_matrix" ] && [ -f "$latest_risk_matrix" ]; then
        local overall_risk_score=$(grep "Weighted Risk Score:" "$latest_risk_matrix" | awk '{print $4}' | sed 's|/100||')
        local overall_risk_level=$(grep "Risk Exposure:" "$latest_risk_matrix" | awk '{print $4}')
        
        echo "Overall Risk Score: ${overall_risk_score}/100" >> "$risk_dashboard_report"
        echo "Risk Exposure Level: $overall_risk_level" >> "$risk_dashboard_report"
        
        case $overall_risk_level in
            "LOW")
                echo "Status: ✅ ACCEPTABLE" >> "$risk_dashboard_report"
                ;;
            "MEDIUM")
                echo "Status: ⚠️ MODERATE" >> "$risk_dashboard_report"
                ;;
            "HIGH")
                echo "Status: ❌ HIGH" >> "$risk_dashboard_report"
                ;;
            "CRITICAL")
                echo "Status: 💥 CRITICAL" >> "$risk_dashboard_report"
                ;;
            *)
                echo "Status: UNKNOWN" >> "$risk_dashboard_report"
                ;;
        esac
    else
        echo "Overall Risk Score: UNAVAILABLE" >> "$risk_dashboard_report"
        echo "Risk Exposure Level: UNKNOWN" >> "$risk_dashboard_report"
        echo "Status: ❓ UNKNOWN" >> "$risk_dashboard_report"
    fi
    echo "" >> "$risk_dashboard_report"
    
    # Risk categories
    echo "Risk Categories:" >> "$risk_dashboard_report"
    echo "----------------" >> "$risk_dashboard_report"
    
    # Get latest assessments for each category
    local categories=("technical" "operational" "business" "external")
    for category in "${categories[@]}"; do
        local latest_assessment=$(ls -t "$RISK_ASSESSMENTS_DIR"/${category}_*.json 2>/dev/null | head -1)
        if [ ! -z "$latest_assessment" ] && [ -f "$latest_assessment" ]; then
            local category_score=$(jq -r '.scores.overall' "$latest_assessment")
            local category_level=$(jq -r '.risk_level' "$latest_assessment")
            
            echo "$category Risk:" >> "$risk_dashboard_report"
            echo "  Score: ${category_score}/100" >> "$risk_dashboard_report"
            echo "  Level: $category_level" >> "$risk_dashboard_report"
            
            case $category_level in
                "LOW")
                    echo "  Status: ✅ LOW" >> "$risk_dashboard_report"
                    ;;
                "MEDIUM")
                    echo "  Status: ⚠️ MEDIUM" >> "$risk_dashboard_report"
                    ;;
                "HIGH")
                    echo "  Status: ❌ HIGH" >> "$risk_dashboard_report"
                    ;;
                "CRITICAL")
                    echo "  Status: 💥 CRITICAL" >> "$risk_dashboard_report"
                    ;;
                *)
                    echo "  Status: ❓ UNKNOWN" >> "$risk_dashboard_report"
                    ;;
            esac
        else
            echo "$category Risk:" >> "$risk_dashboard_report"
            echo "  Score: N/A" >> "$risk_dashboard_report"
            echo "  Level: UNKNOWN" >> "$risk_dashboard_report"
            echo "  Status: ❓ UNKNOWN" >> "$risk_dashboard_report"
        fi
        echo "" >> "$risk_dashboard_report"
    done
    
    # Recent risk events
    echo "Recent Risk Events:" >> "$risk_dashboard_report"
    echo "------------------" >> "$risk_dashboard_report"
    
    # Check recent alerts and incidents
    local alert_log="/home/ubuntu/dev/atlas/logs/alerts.log"
    if [ -f "$alert_log" ]; then
        local recent_alerts=$(tail -10 "$alert_log" 2>/dev/null | grep -c "ALERT\|CRITICAL\|WARNING" || echo "0")
        echo "Recent Alerts: $recent_alerts" >> "$risk_dashboard_report"
    else
        echo "Recent Alerts: 0" >> "$risk_dashboard_report"
    fi
    
    local incident_log="/home/ubuntu/dev/atlas/logs/incidents.log"
    if [ -f "$incident_log" ]; then
        local recent_incidents=$(tail -10 "$incident_log" 2>/dev/null | grep -c "INCIDENT\|CRITICAL" || echo "0")
        echo "Recent Incidents: $recent_incidents" >> "$risk_dashboard_report"
    else
        echo "Recent Incidents: 0" >> "$risk_dashboard_report"
    fi
    
    local security_log="/home/ubuntu/dev/atlas/logs/security.log"
    if [ -f "$security_log" ]; then
        local recent_security_events=$(tail -10 "$security_log" 2>/dev/null | grep -c "SECURITY\|ATTACK\|BREACH" || echo "0")
        echo "Recent Security Events: $recent_security_events" >> "$risk_dashboard_report"
    else
        echo "Recent Security Events: 0" >> "$risk_dashboard_report"
    fi
    echo "" >> "$risk_dashboard_report"
    
    # Risk mitigation status
    echo "Risk Mitigation Status:" >> "$risk_dashboard_report"
    echo "----------------------" >> "$risk_dashboard_report"
    
    # Check if mitigation plan exists
    local mitigation_plan=$(ls -t "$RISK_REPORT_DIR"/mitigation_plan_*.txt 2>/dev/null | head -1)
    if [ ! -z "$mitigation_plan" ] && [ -f "$mitigation_plan" ]; then
        echo "Mitigation Plan: ✅ IMPLEMENTED" >> "$risk_dashboard_report"
        
        # Check recent mitigation activities
        local mitigation_activities=$(grep -c "MITIGATION\|ACTION\|IMPLEMENTED" "$mitigation_plan" 2>/dev/null || echo "0")
        echo "Mitigation Activities: $mitigation_activities" >> "$risk_dashboard_report"
    else
        echo "Mitigation Plan: ❌ NOT IMPLEMENTED" >> "$risk_dashboard_report"
        echo "Mitigation Activities: 0" >> "$risk_dashboard_report"
    fi
    echo "" >> "$risk_dashboard_report"
    
    # System health indicators
    echo "System Health Indicators:" >> "$risk_dashboard_report"
    echo "-----------------------" >> "$risk_dashboard_report"
    
    # Check system uptime
    local system_uptime=$(uptime -p)
    echo "System Uptime: $system_uptime" >> "$risk_dashboard_report"
    
    # Check resource usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local memory_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "CPU Usage: ${cpu_usage}%" >> "$risk_dashboard_report"
    echo "Memory Usage: ${memory_usage}%" >> "$risk_dashboard_report"
    echo "Disk Usage: ${disk_usage}%" >> "$risk_dashboard_report"
    
    # Resource health status
    if [ $cpu_usage -lt 70 ] && [ $memory_usage -lt 70 ] && [ $disk_usage -lt 80 ]; then
        echo "Resource Health: ✅ HEALTHY" >> "$risk_dashboard_report"
    elif [ $cpu_usage -lt 85 ] && [ $memory_usage -lt 85 ] && [ $disk_usage -lt 90 ]; then
        echo "Resource Health: ⚠️ CAUTION" >> "$risk_dashboard_report"
    else
        echo "Resource Health: ❌ WARNING" >> "$risk_dashboard_report"
    fi
    echo "" >> "$risk_dashboard_report"
    
    # Service status indicators
    echo "Service Status:" >> "$risk_dashboard_report"
    echo "--------------" >> "$risk_dashboard_report"
    
    # Check critical services
    local critical_services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    local services_running=0
    local total_services=${#critical_services[@]}
    
    for service_info in "${critical_services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "$service_desc: ✅ RUNNING" >> "$risk_dashboard_report"
            services_running=$((services_running + 1))
        else
            echo "$service_desc: ❌ STOPPED" >> "$risk_dashboard_report"
        fi
    done
    
    echo "Services Running: $services_running/$total_services" >> "$risk_dashboard_report"
    
    if [ $services_running -eq $total_services ]; then
        echo "Service Health: ✅ EXCELLENT" >> "$risk_dashboard_report"
    elif [ $services_running -ge $((total_services * 3 / 4)) ]; then
        echo "Service Health: ⚠️ GOOD" >> "$risk_dashboard_report"
    else
        echo "Service Health: ❌ POOR" >> "$risk_dashboard_report"
    fi
    echo "" >> "$risk_dashboard_report"
    
    # Risk exposure summary
    echo "Risk Exposure Summary:" >> "$risk_dashboard_report"
    echo "--------------------" >> "$risk_dashboard_report"
    
    if [ ! -z "$latest_risk_matrix" ] && [ -f "$latest_risk_matrix" ]; then
        local risk_exposure=$(grep "Risk Exposure:" "$latest_risk_matrix" | awk '{print $4}')
        echo "Risk Exposure: $risk_exposure" >> "$risk_dashboard_report"
        
        case $risk_exposure in
            "LOW")
                echo "Action Required: ✅ MONITOR" >> "$risk_dashboard_report"
                ;;
            "MEDIUM")
                echo "Action Required: ⚠️ REVIEW" >> "$risk_dashboard_report"
                ;;
            "HIGH")
                echo "Action Required: ❌ ADDRESS" >> "$risk_dashboard_report"
                ;;
            "CRITICAL")
                echo "Action Required: 💥 IMMEDIATE" >> "$risk_dashboard_report"
                ;;
            *)
                echo "Action Required: ❓ REVIEW" >> "$risk_dashboard_report"
                ;;
        esac
    else
        echo "Risk Exposure: UNKNOWN" >> "$risk_dashboard_report"
        echo "Action Required: ❓ REVIEW" >> "$risk_dashboard_report"
    fi
    echo "" >> "$risk_dashboard_report"
    
    # Recommendations
    echo "Dashboard Recommendations:" >> "$risk_dashboard_report"
    echo "------------------------" >> "$risk_dashboard_report"
    
    echo "1. Review this dashboard weekly" >> "$risk_dashboard_report"
    echo "2. Monitor risk trends and changes" >> "$risk_dashboard_report"
    echo "3. Address high-risk categories immediately" >> "$risk_dashboard_report"
    echo "4. Update mitigation plans quarterly" >> "$risk_dashboard_report"
    echo "5. Report significant changes to management" >> "$risk_dashboard_report"
    echo "" >> "$risk_dashboard_report"
    
    echo "✅ Risk dashboard generated"
    echo "📋 Dashboard report saved to: $risk_dashboard_report"
    log_message "Risk dashboard generated: $risk_dashboard_report"
    
    # Display summary
    echo ""
    echo "Risk Dashboard Summary:"
    echo "  Overall Risk Score: $(if [ ! -z "$overall_risk_score" ]; then echo "${overall_risk_score}/100"; else echo "N/A"; fi)"
    echo "  Risk Exposure: $(if [ ! -z "$overall_risk_level" ]; then echo "$overall_risk_level"; else echo "UNKNOWN"; fi)"
    echo "  Critical Services: $services_running/$total_services running"
    echo "  System Health: $(if [ $cpu_usage -lt 70 ] && [ $memory_usage -lt 70 ] && [ $disk_usage -lt 80 ]; then echo "HEALTHY"; elif [ $cpu_usage -lt 85 ] && [ $memory_usage -lt 85 ] && [ $disk_usage -lt 90 ]; then echo "CAUTION"; else echo "WARNING"; fi)"
    if [ ! -z "$latest_risk_matrix" ] && [ -f "$latest_risk_matrix" ]; then
        local risk_exposure=$(grep "Risk Exposure:" "$latest_risk_matrix" | awk '{print $4}')
        echo "  Risk Exposure Level: $risk_exposure"
    fi
    echo "  Report: $risk_dashboard_report"
}

# Function to clean old risk reports
clean_old_reports() {
    log_message "Cleaning old risk reports"
    
    echo ""
    echo "Cleaning Old Risk Reports..."
    echo "=========================="
    
    # Remove risk reports older than 90 days
    find "$RISK_REPORT_DIR" -name "technical_risks_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$RISK_REPORT_DIR" -name "operational_risks_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$RISK_REPORT_DIR" -name "business_risks_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$RISK_REPORT_DIR" -name "external_risks_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$RISK_REPORT_DIR" -name "risk_matrix_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$RISK_REPORT_DIR" -name "mitigation_plan_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$RISK_REPORT_DIR" -name "risk_dashboard_*.txt" -mtime +90 -delete 2>/dev/null || true
    
    # Remove risk assessment data older than 365 days
    find "$RISK_ASSESSMENTS_DIR" -name "*.json" -mtime +365 -delete 2>/dev/null || true
    
    echo "✅ Old risk reports cleaned"
    log_message "Old risk reports cleaned"
}

# Main risk management function
main() {
    log_message "=== Starting Atlas Risk Management ==="
    
    # Initialize configuration
    initialize_risk_config
    
    # Start time
    local start_time=$(date)
    log_message "Risk management started at: $start_time"
    
    # Handle different risk management operations
    case $1 in
        "technical")
            assess_technical_risks
            ;;
        "operational")
            assess_operational_risks
            ;;
        "business")
            assess_business_risks
            ;;
        "external")
            assess_external_risks
            ;;
        "matrix")
            generate_risk_matrix
            ;;
        "mitigation")
            create_mitigation_plan
            ;;
        "dashboard")
            generate_risk_dashboard
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive risk management
            assess_technical_risks
            assess_operational_risks
            assess_business_risks
            assess_external_risks
            generate_risk_matrix
            create_mitigation_plan
            generate_risk_dashboard
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Risk management completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Risk Management Completed ==="
    
    echo ""
    echo "✅ Risk management operations completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $RISK_REPORT_DIR"
    echo "💾 Assessments saved to: $RISK_ASSESSMENTS_DIR"
    echo "📝 Log file: $RISK_LOG"
}

# Run main function
main "$@"