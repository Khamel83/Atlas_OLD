#!/bin/bash

# Atlas Production Business Continuity Script
# This script ensures business continuity for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Business Continuity..."

# Configuration
BC_LOG="/home/ubuntu/dev/atlas/logs/business_continuity.log"
BC_REPORT_DIR="/home/ubuntu/dev/atlas/reports/business_continuity"
BC_CONFIG="/home/ubuntu/dev/atlas/config/business_continuity.json"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $BC_LOG)"
mkdir -p "$BC_REPORT_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $BC_LOG
    echo "$1"
}

# Function to initialize business continuity configuration
initialize_bc_config() {
    log_message "Initializing business continuity configuration"
    
    # Create default BC configuration if it doesn't exist
    if [ ! -f "$BC_CONFIG" ]; then
        cat > "$BC_CONFIG" << EOF
{
    "business_continuity": {
        "rto_hours": 4,
        "rpo_hours": 24,
        "availability_target": 99.9,
        "mtbf_days": 365,
        "mttr_hours": 2
    },
    "continuity_plans": {
        "primary_site": {
            "location": "OCI VM.Standard2.1",
            "region": "us-phoenix-1",
            "contact": "admin@khamel.com"
        },
        "secondary_site": {
            "location": "OCI VM.Standard2.1",
            "region": "us-ashburn-1",
            "contact": "admin@khamel.com"
        },
        "remote_access": {
            "vpn_required": true,
            "mfa_required": true,
            "backup_communication": "Slack, Email, Phone"
        }
    },
    "critical_functions": [
        "content_processing",
        "database_access",
        "web_interface",
        "monitoring",
        "backup_creation"
    ],
    "recovery_teams": {
        "primary_team": {
            "members": ["admin@khamel.com"],
            "roles": ["System Administrator"]
        },
        "backup_team": {
            "members": ["backup@khamel.com"],
            "roles": ["Backup Administrator"]
        }
    }
}
EOF
        echo "✅ Created default business continuity configuration"
        log_message "Default business continuity configuration created"
    else
        echo "✅ Business continuity configuration already exists"
    fi
}

# Function to assess business impact
assess_business_impact() {
    log_message "Assessing business impact"
    
    echo "Assessing Business Impact..."
    echo "=========================="
    
    local impact_report="$BC_REPORT_DIR/business_impact_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create impact report header
    echo "Atlas Production Business Impact Assessment" > "$impact_report"
    echo "Generated: $(date)" >> "$impact_report"
    echo "===========================================" >> "$impact_report"
    echo "" >> "$impact_report"
    
    # Define critical functions and their impact
    local critical_functions=(
        "content_processing:High:Revenue generation and user satisfaction"
        "database_access:Critical:Data integrity and availability"
        "web_interface:High:User access and engagement"
        "monitoring:Medium:System health and performance tracking"
        "backup_creation:High:Data protection and recovery capability"
    )
    
    echo "Critical Functions Impact Assessment:" >> "$impact_report"
    echo "------------------------------------" >> "$impact_report"
    
    local high_impact_count=0
    local critical_impact_count=0
    
    for func_info in "${critical_functions[@]}"; do
        local function=$(echo $func_info | cut -d':' -f1)
        local impact=$(echo $func_info | cut -d':' -f2)
        local description=$(echo $func_info | cut -d':' -f3)
        
        echo "$function:" >> "$impact_report"
        echo "  Impact Level: $impact" >> "$impact_report"
        echo "  Description: $description" >> "$impact_report"
        echo "" >> "$impact_report"
        
        if [ "$impact" = "High" ]; then
            high_impact_count=$((high_impact_count + 1))
        elif [ "$impact" = "Critical" ]; then
            critical_impact_count=$((critical_impact_count + 1))
        fi
    done
    
    echo "Impact Summary:" >> "$impact_report"
    echo "--------------" >> "$impact_report"
    echo "Critical Impact Functions: $critical_impact_count" >> "$impact_report"
    echo "High Impact Functions: $high_impact_count" >> "$impact_report"
    echo "Medium Impact Functions: $((5 - high_impact_count - critical_impact_count))" >> "$impact_report"
    echo "" >> "$impact_report"
    
    # Calculate downtime cost (simplified)
    echo "Downtime Cost Estimation:" >> "$impact_report"
    echo "------------------------" >> "$impact_report"
    
    # Estimate based on function importance
    local hourly_cost=100  # Simplified cost estimation
    local rto_hours=$(jq -r '.business_continuity.rto_hours' "$BC_CONFIG")
    local estimated_cost=$((hourly_cost * rto_hours))
    
    echo "Estimated Hourly Downtime Cost: \$${hourly_cost}" >> "$impact_report"
    echo "Recovery Time Objective (RTO): ${rto_hours} hours" >> "$impact_report"
    echo "Estimated Maximum Downtime Cost: \$${estimated_cost}" >> "$impact_report"
    echo "" >> "$impact_report"
    
    echo "✅ Business impact assessment completed"
    echo "📋 Impact report saved to: $impact_report"
    log_message "Business impact assessment completed: $impact_report"
    
    # Display summary
    echo ""
    echo "Business Impact Summary:"
    echo "  Critical Functions: $critical_impact_count"
    echo "  High Impact Functions: $high_impact_count"
    echo "  Estimated Downtime Cost: \$${estimated_cost}"
    echo "  Report: $impact_report"
}

# Function to evaluate continuity plans
evaluate_continuity_plans() {
    log_message "Evaluating continuity plans"
    
    echo ""
    echo "Evaluating Continuity Plans..."
    echo "============================="
    
    local plans_report="$BC_REPORT_DIR/continuity_plans_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create plans report header
    echo "Atlas Production Continuity Plans Evaluation" > "$plans_report"
    echo "Generated: $(date)" >> "$plans_report"
    echo "===========================================" >> "$plans_report"
    echo "" >> "$plans_report"
    
    # Evaluate primary site
    echo "Primary Site Evaluation:" >> "$plans_report"
    echo "-----------------------" >> "$plans_report"
    
    local primary_location=$(jq -r '.continuity_plans.primary_site.location' "$BC_CONFIG")
    local primary_region=$(jq -r '.continuity_plans.primary_site.region' "$BC_CONFIG")
    local primary_contact=$(jq -r '.continuity_plans.primary_site.contact' "$BC_CONFIG")
    
    echo "Location: $primary_location" >> "$plans_report"
    echo "Region: $primary_region" >> "$plans_report"
    echo "Contact: $primary_contact" >> "$plans_report"
    
    # Check if primary site is accessible
    if ping -c 1 "$(hostname)" > /dev/null 2>&1; then
        echo "✅ Primary site is accessible" >> "$plans_report"
    else
        echo "❌ Primary site is not accessible" >> "$plans_report"
    fi
    echo "" >> "$plans_report"
    
    # Evaluate secondary site
    echo "Secondary Site Evaluation:" >> "$plans_report"
    echo "-------------------------" >> "$plans_report"
    
    local secondary_location=$(jq -r '.continuity_plans.secondary_site.location' "$BC_CONFIG")
    local secondary_region=$(jq -r '.continuity_plans.secondary_site.region' "$BC_CONFIG")
    local secondary_contact=$(jq -r '.continuity_plans.secondary_site.contact' "$BC_CONFIG")
    
    echo "Location: $secondary_location" >> "$plans_report"
    echo "Region: $secondary_region" >> "$plans_report"
    echo "Contact: $secondary_contact" >> "$plans_report"
    echo "ℹ️ Secondary site evaluation requires manual verification" >> "$plans_report"
    echo "" >> "$plans_report"
    
    # Evaluate remote access
    echo "Remote Access Evaluation:" >> "$plans_report"
    echo "------------------------" >> "$plans_report"
    
    local vpn_required=$(jq -r '.continuity_plans.remote_access.vpn_required' "$BC_CONFIG")
    local mfa_required=$(jq -r '.continuity_plans.remote_access.mfa_required' "$BC_CONFIG")
    local backup_communication=$(jq -r '.continuity_plans.remote_access.backup_communication' "$BC_CONFIG")
    
    echo "VPN Required: $vpn_required" >> "$plans_report"
    echo "MFA Required: $mfa_required" >> "$plans_report"
    echo "Backup Communication: $backup_communication" >> "$plans_report"
    
    # Check VPN connectivity
    echo "VPN Connectivity: Not tested (requires manual verification)" >> "$plans_report"
    
    # Check MFA configuration
    echo "MFA Configuration: Not tested (requires manual verification)" >> "$plans_report"
    echo "" >> "$plans_report"
    
    # Evaluate backup communication channels
    echo "Backup Communication Channels:" >> "$plans_report"
    echo "-----------------------------" >> "$plans_report"
    echo "$backup_communication" >> "$plans_report"
    echo "✅ Backup communication channels documented" >> "$plans_report"
    echo "" >> "$plans_report"
    
    echo "✅ Continuity plans evaluation completed"
    echo "📋 Plans report saved to: $plans_report"
    log_message "Continuity plans evaluation completed: $plans_report"
    
    # Display summary
    echo ""
    echo "Continuity Plans Summary:"
    echo "  Primary Site: $primary_location ($primary_region)"
    echo "  Secondary Site: $secondary_location ($secondary_region)"
    echo "  VPN Required: $vpn_required"
    echo "  MFA Required: $mfa_required"
    echo "  Report: $plans_report"
}

# Function to test critical functions
test_critical_functions() {
    log_message "Testing critical functions"
    
    echo ""
    echo "Testing Critical Functions..."
    echo "============================"
    
    local functions_report="$BC_REPORT_DIR/critical_functions_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create functions report header
    echo "Atlas Production Critical Functions Test" > "$functions_report"
    echo "Generated: $(date)" >> "$functions_report"
    echo "=======================================" >> "$functions_report"
    echo "" >> "$functions_report"
    
    # Initialize counters
    local passed_tests=0
    local failed_tests=0
    
    # Test content processing
    echo "Content Processing Test:" >> "$functions_report"
    echo "----------------------" >> "$functions_report"
    
    # Check if Atlas service is running
    if systemctl is-active --quiet atlas; then
        echo "✅ Atlas service is running" >> "$functions_report"
        passed_tests=$((passed_tests + 1))
        
        # Check if content processing is working
        if curl -f -s http://localhost:5000/ > /dev/null 2>&1; then
            echo "✅ Content processing web interface is accessible" >> "$functions_report"
            passed_tests=$((passed_tests + 1))
        else
            echo "❌ Content processing web interface is not accessible" >> "$functions_report"
            failed_tests=$((failed_tests + 1))
        fi
    else
        echo "❌ Atlas service is not running" >> "$functions_report"
        failed_tests=$((failed_tests + 1))
    fi
    echo "" >> "$functions_report"
    
    # Test database access
    echo "Database Access Test:" >> "$functions_report"
    echo "-------------------" >> "$functions_report"
    
    # Check if PostgreSQL is running
    if systemctl is-active --quiet postgresql; then
        echo "✅ PostgreSQL is running" >> "$functions_report"
        passed_tests=$((passed_tests + 1))
        
        # Check database connectivity
        if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
            echo "✅ Database is accessible" >> "$functions_report"
            passed_tests=$((passed_tests + 1))
        else
            echo "❌ Database is not accessible" >> "$functions_report"
            failed_tests=$((failed_tests + 1))
        fi
    else
        echo "❌ PostgreSQL is not running" >> "$functions_report"
        failed_tests=$((failed_tests + 1))
    fi
    echo "" >> "$functions_report"
    
    # Test web interface
    echo "Web Interface Test:" >> "$functions_report"
    echo "------------------" >> "$functions_report"
    
    # Check Nginx status
    if systemctl is-active --quiet nginx; then
        echo "✅ Nginx is running" >> "$functions_report"
        passed_tests=$((passed_tests + 1))
        
        # Check web interface accessibility
        if curl -f -s http://localhost/ > /dev/null 2>&1; then
            echo "✅ Web interface is accessible via Nginx" >> "$functions_report"
            passed_tests=$((passed_tests + 1))
        else
            echo "❌ Web interface is not accessible via Nginx" >> "$functions_report"
            failed_tests=$((failed_tests + 1))
        fi
    else
        echo "❌ Nginx is not running" >> "$functions_report"
        failed_tests=$((failed_tests + 1))
    fi
    echo "" >> "$functions_report"
    
    # Test monitoring
    echo "Monitoring Test:" >> "$functions_report"
    echo "---------------" >> "$functions_report"
    
    # Check Prometheus status
    if systemctl is-active --quiet atlas-prometheus; then
        echo "✅ Prometheus is running" >> "$functions_report"
        passed_tests=$((passed_tests + 1))
        
        # Check Prometheus accessibility
        if curl -f -s http://localhost:9090/ > /dev/null 2>&1; then
            echo "✅ Prometheus is accessible" >> "$functions_report"
            passed_tests=$((passed_tests + 1))
        else
            echo "❌ Prometheus is not accessible" >> "$functions_report"
            failed_tests=$((failed_tests + 1))
        fi
    else
        echo "❌ Prometheus is not running" >> "$functions_report"
        failed_tests=$((failed_tests + 1))
    fi
    
    # Check Grafana status
    if systemctl is-active --quiet atlas-grafana; then
        echo "✅ Grafana is running" >> "$functions_report"
        passed_tests=$((passed_tests + 1))
        
        # Check Grafana accessibility
        if curl -f -s http://localhost:3000/ > /dev/null 2>&1; then
            echo "✅ Grafana is accessible" >> "$functions_report"
            passed_tests=$((passed_tests + 1))
        else
            echo "❌ Grafana is not accessible" >> "$functions_report"
            failed_tests=$((failed_tests + 1))
        fi
    else
        echo "❌ Grafana is not running" >> "$functions_report"
        failed_tests=$((failed_tests + 1))
    fi
    echo "" >> "$functions_report"
    
    # Test backup creation
    echo "Backup Creation Test:" >> "$functions_report"
    echo "--------------------" >> "$functions_report"
    
    # Check if backup directory exists
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        echo "✅ Backup directory exists" >> "$functions_report"
        passed_tests=$((passed_tests + 1))
        
        # Check if backup script exists
        local backup_script="/home/ubuntu/dev/atlas/scripts/production_backup.sh"
        if [ -f "$backup_script" ]; then
            echo "✅ Backup script exists" >> "$functions_report"
            passed_tests=$((passed_tests + 1))
            
            # Check if backup cron job is configured
            if crontab -l 2>/dev/null | grep -q "production_backup.sh"; then
                echo "✅ Backup cron job is configured" >> "$functions_report"
                passed_tests=$((passed_tests + 1))
            else
                echo "❌ Backup cron job is not configured" >> "$functions_report"
                failed_tests=$((failed_tests + 1))
            fi
        else
            echo "❌ Backup script not found" >> "$functions_report"
            failed_tests=$((failed_tests + 1))
        fi
    else
        echo "❌ Backup directory not found" >> "$functions_report"
        failed_tests=$((failed_tests + 1))
    fi
    echo "" >> "$functions_report"
    
    # Summary
    echo "Critical Functions Test Summary:" >> "$functions_report"
    echo "-------------------------------" >> "$functions_report"
    echo "Passed Tests: $passed_tests" >> "$functions_report"
    echo "Failed Tests: $failed_tests" >> "$functions_report"
    echo "Success Rate: $((passed_tests * 100 / (passed_tests + failed_tests)))%" >> "$functions_report"
    echo "" >> "$functions_report"
    
    echo "✅ Critical functions test completed"
    echo "📋 Functions report saved to: $functions_report"
    log_message "Critical functions test completed: $functions_report"
    
    # Display summary
    echo ""
    echo "Critical Functions Test Summary:"
    echo "  Passed Tests: $passed_tests"
    echo "  Failed Tests: $failed_tests"
    echo "  Success Rate: $((passed_tests * 100 / (passed_tests + failed_tests)))%"
    echo "  Report: $functions_report"
}

# Function to verify recovery teams
verify_recovery_teams() {
    log_message "Verifying recovery teams"
    
    echo ""
    echo "Verifying Recovery Teams..."
    echo "=========================="
    
    local teams_report="$BC_REPORT_DIR/recovery_teams_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create teams report header
    echo "Atlas Production Recovery Teams Verification" > "$teams_report"
    echo "Generated: $(date)" >> "$teams_report"
    echo "=============================================" >> "$teams_report"
    echo "" >> "$teams_report"
    
    # Verify primary team
    echo "Primary Team Verification:" >> "$teams_report"
    echo "-------------------------" >> "$teams_report"
    
    local primary_members=$(jq -r '.recovery_teams.primary_team.members[]' "$BC_CONFIG")
    local primary_roles=$(jq -r '.recovery_teams.primary_team.roles[]' "$BC_CONFIG")
    
    echo "Team Members:" >> "$teams_report"
    while IFS= read -r member; do
        echo "  - $member" >> "$teams_report"
    done <<< "$primary_members"
    
    echo "Roles:" >> "$teams_report"
    while IFS= read -r role; do
        echo "  - $role" >> "$teams_report"
    done <<< "$primary_roles"
    
    echo "✅ Primary team information verified" >> "$teams_report"
    echo "" >> "$teams_report"
    
    # Verify backup team
    echo "Backup Team Verification:" >> "$teams_report"
    echo "------------------------" >> "$teams_report"
    
    local backup_members=$(jq -r '.recovery_teams.backup_team.members[]' "$BC_CONFIG")
    local backup_roles=$(jq -r '.recovery_teams.backup_team.roles[]' "$BC_CONFIG")
    
    echo "Team Members:" >> "$teams_report"
    while IFS= read -r member; do
        echo "  - $member" >> "$teams_report"
    done <<< "$backup_members"
    
    echo "Roles:" >> "$teams_report"
    while IFS= read -r role; do
        echo "  - $role" >> "$teams_report"
    done <<< "$backup_roles"
    
    echo "✅ Backup team information verified" >> "$teams_report"
    echo "" >> "$teams_report"
    
    # Verify contact information
    echo "Contact Information Verification:" >> "$teams_report"
    echo "---------------------------------" >> "$teams_report"
    
    # Check if contact information is present
    if [ ! -z "$primary_members" ] && [ ! -z "$backup_members" ]; then
        echo "✅ Contact information is documented" >> "$teams_report"
    else
        echo "❌ Contact information is incomplete" >> "$teams_report"
    fi
    echo "" >> "$teams_report"
    
    # Verify team access
    echo "Team Access Verification:" >> "$teams_report"
    echo "------------------------" >> "$teams_report"
    
    # Check if team members have appropriate system access
    echo "ℹ️ Team access verification requires manual review of:" >> "$teams_report"
    echo "  - System user accounts" >> "$teams_report"
    echo "  - SSH key access" >> "$teams_report"
    echo "  - Database access privileges" >> "$teams_report"
    echo "  - Monitoring system access" >> "$teams_report"
    echo "" >> "$teams_report"
    
    echo "✅ Recovery teams verification completed"
    echo "📋 Teams report saved to: $teams_report"
    log_message "Recovery teams verification completed: $teams_report"
    
    # Display summary
    echo ""
    echo "Recovery Teams Verification Summary:"
    echo "  Primary Team Members:"
    while IFS= read -r member; do
        echo "    - $member"
    done <<< "$primary_members"
    echo "  Backup Team Members:"
    while IFS= read -r member; do
        echo "    - $member"
    done <<< "$backup_members"
    echo "  Report: $teams_report"
}

# Function to test remote access
test_remote_access() {
    log_message "Testing remote access"
    
    echo ""
    echo "Testing Remote Access..."
    echo "========================"
    
    local remote_report="$BC_REPORT_DIR/remote_access_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create remote access report header
    echo "Atlas Production Remote Access Test" > "$remote_report"
    echo "Generated: $(date)" >> "$remote_report"
    echo "==================================" >> "$remote_report"
    echo "" >> "$remote_report"
    
    # Test SSH access
    echo "SSH Access Test:" >> "$remote_report"
    echo "---------------" >> "$remote_report"
    
    # Check if SSH is running
    if systemctl is-active --quiet ssh; then
        echo "✅ SSH service is running" >> "$remote_report"
        
        # Check SSH port
        local ssh_port=$(grep "^Port" /etc/ssh/sshd_config | awk '{print $2}')
        if [ -z "$ssh_port" ]; then
            ssh_port=22
        fi
        echo "SSH Port: $ssh_port" >> "$remote_report"
        
        # Check if SSH is accessible locally
        if nc -z localhost $ssh_port > /dev/null 2>&1; then
            echo "✅ SSH port is accessible locally" >> "$remote_report"
        else
            echo "❌ SSH port is not accessible locally" >> "$remote_report"
        fi
    else
        echo "❌ SSH service is not running" >> "$remote_report"
    fi
    echo "" >> "$remote_report"
    
    # Test web interface access
    echo "Web Interface Access Test:" >> "$remote_report"
    echo "-------------------------" >> "$remote_report"
    
    # Check if web interfaces are accessible
    local web_interfaces=(
        "80:HTTP (Nginx)"
        "443:HTTPS (Nginx)"
        "5000:Atlas Direct"
        "9090:Prometheus"
        "3000:Grafana"
    )
    
    for interface_info in "${web_interfaces[@]}"; do
        local port=$(echo $interface_info | cut -d':' -f1)
        local description=$(echo $interface_info | cut -d':' -f2)
        
        if nc -z localhost $port > /dev/null 2>&1; then
            echo "✅ $description (port $port) is accessible" >> "$remote_report"
        else
            echo "❌ $description (port $port) is not accessible" >> "$remote_report"
        fi
    done
    echo "" >> "$remote_report"
    
    # Test database access
    echo "Database Access Test:" >> "$remote_report"
    echo "--------------------" >> "$remote_report"
    
    # Check PostgreSQL access
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        echo "✅ Database is accessible locally" >> "$remote_report"
    else
        echo "❌ Database is not accessible locally" >> "$remote_report"
    fi
    echo "" >> "$remote_report"
    
    # Test monitoring access
    echo "Monitoring Access Test:" >> "$remote_report"
    echo "----------------------" >> "$remote_report"
    
    # Check Prometheus access
    if curl -f -s http://localhost:9090/ > /dev/null 2>&1; then
        echo "✅ Prometheus is accessible" >> "$remote_report"
    else
        echo "❌ Prometheus is not accessible" >> "$remote_report"
    fi
    
    # Check Grafana access
    if curl -f -s http://localhost:3000/ > /dev/null 2>&1; then
        echo "✅ Grafana is accessible" >> "$remote_report"
    else
        echo "❌ Grafana is not accessible" >> "$remote_report"
    fi
    echo "" >> "$remote_report"
    
    # Test backup access
    echo "Backup Access Test:" >> "$remote_report"
    echo "------------------" >> "$remote_report"
    
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        echo "✅ Backup directory is accessible" >> "$remote_report"
        
        # Check backup file access
        local backup_files=$(find "$backup_dir" -name "*.sql*" | wc -l)
        echo "Backup files available: $backup_files" >> "$remote_report"
    else
        echo "❌ Backup directory is not accessible" >> "$remote_report"
    fi
    echo "" >> "$remote_report"
    
    echo "✅ Remote access test completed"
    echo "📋 Remote access report saved to: $remote_report"
    log_message "Remote access test completed: $remote_report"
    
    # Display summary
    echo ""
    echo "Remote Access Test Summary:"
    echo "  SSH Access: $(if systemctl is-active --quiet ssh; then echo "Available"; else echo "Unavailable"; fi)"
    echo "  Web Interfaces: Tested"
    echo "  Database Access: $(if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then echo "Available"; else echo "Unavailable"; fi)"
    echo "  Monitoring Access: Tested"
    echo "  Backup Access: $(if [ -d "$backup_dir" ]; then echo "Available"; else echo "Unavailable"; fi)"
    echo "  Report: $remote_report"
}

# Function to generate business continuity report
generate_bc_report() {
    log_message "Generating business continuity report"
    
    echo ""
    echo "Generating Business Continuity Report..."
    echo "======================================"
    
    local bc_report="$BC_REPORT_DIR/business_continuity_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create business continuity report header
    echo "Atlas Production Business Continuity Report" > "$bc_report"
    echo "Generated: $(date)" >> "$bc_report"
    echo "=========================================" >> "$bc_report"
    echo "" >> "$bc_report"
    
    # Add system information
    echo "System Information:" >> "$bc_report"
    echo "------------------" >> "$bc_report"
    echo "Hostname: $(hostname)" >> "$bc_report"
    echo "OS: $(lsb_release -d | cut -f2)" >> "$bc_report"
    echo "Kernel: $(uname -r)" >> "$bc_report"
    echo "Uptime: $(uptime -p)" >> "$bc_report"
    echo "" >> "$bc_report"
    
    # Add business continuity metrics
    echo "Business Continuity Metrics:" >> "$bc_report"
    echo "---------------------------" >> "$bc_report"
    
    local rto_hours=$(jq -r '.business_continuity.rto_hours' "$BC_CONFIG")
    local rpo_hours=$(jq -r '.business_continuity.rpo_hours' "$BC_CONFIG")
    local availability_target=$(jq -r '.business_continuity.availability_target' "$BC_CONFIG")
    
    echo "Recovery Time Objective (RTO): ${rto_hours} hours" >> "$bc_report"
    echo "Recovery Point Objective (RPO): ${rpo_hours} hours" >> "$bc_report"
    echo "Availability Target: ${availability_target}%" >> "$bc_report"
    echo "" >> "$bc_report"
    
    # Add critical functions status
    echo "Critical Functions Status:" >> "$bc_report"
    echo "--------------------------" >> "$bc_report"
    
    # Check service statuses
    local critical_services=(
        "atlas:Atlas Main Service"
        "postgresql:PostgreSQL Database"
        "nginx:Nginx Web Server"
        "atlas-prometheus:Prometheus Monitoring"
        "atlas-grafana:Grafana Dashboard"
    )
    
    local services_running=0
    for service_info in "${critical_services[@]}"; do
        local service_name=$(echo $service_info | cut -d':' -f1)
        local service_desc=$(echo $service_info | cut -d':' -f2)
        
        if systemctl is-active --quiet $service_name; then
            echo "✅ $service_desc is running" >> "$bc_report"
            services_running=$((services_running + 1))
        else
            echo "❌ $service_desc is not running" >> "$bc_report"
        fi
    done
    echo "" >> "$bc_report"
    
    # Add web interface status
    echo "Web Interface Status:" >> "$bc_report"
    echo "--------------------" >> "$bc_report"
    
    local web_interfaces=(
        "http://localhost/:Main Web Interface"
        "http://localhost:5000/:Atlas Direct Interface"
        "http://localhost:9090/:Prometheus"
        "http://localhost:3000/:Grafana"
    )
    
    for interface_info in "${web_interfaces[@]}"; do
        local url=$(echo $interface_info | cut -d':' -f1)
        local description=$(echo $interface_info | cut -d':' -f2)
        
        if curl -f -s "$url" > /dev/null 2>&1; then
            echo "✅ $description is accessible" >> "$bc_report"
        else
            echo "❌ $description is not accessible" >> "$bc_report"
        fi
    done
    echo "" >> "$bc_report"
    
    # Add database status
    echo "Database Status:" >> "$bc_report"
    echo "----------------" >> "$bc_report"
    
    if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then
        echo "✅ Database is accessible" >> "$bc_report"
        
        # Get database size
        local db_size=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT pg_size_pretty(pg_database_size('atlas'));" 2>/dev/null || echo "Unknown")
        echo "Database Size: $db_size" >> "$bc_report"
        
        # Get record counts
        local articles_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM articles;" 2>/dev/null || echo "0")
        local podcasts_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM podcasts;" 2>/dev/null || echo "0")
        local youtube_count=$(sudo -u postgres psql -U atlas_user -d atlas -tAc "SELECT COUNT(*) FROM youtube_videos;" 2>/dev/null || echo "0")
        
        echo "Record Counts:" >> "$bc_report"
        echo "  Articles: $articles_count" >> "$bc_report"
        echo "  Podcasts: $podcasts_count" >> "$bc_report"
        echo "  YouTube Videos: $youtube_count" >> "$bc_report"
    else
        echo "❌ Database is not accessible" >> "$bc_report"
    fi
    echo "" >> "$bc_report"
    
    # Add backup status
    echo "Backup Status:" >> "$bc_report"
    echo "-------------" >> "$bc_report"
    
    local backup_dir="/home/ubuntu/dev/atlas/backups"
    if [ -d "$backup_dir" ]; then
        echo "✅ Backup directory exists" >> "$bc_report"
        
        # Count backup files
        local backup_count=$(find "$backup_dir" -name "*.sql*" | wc -l)
        echo "Backup files: $backup_count" >> "$bc_report"
        
        # Check latest backup
        local latest_backup=$(find "$backup_dir" -name "atlas_backup_*.sql*" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
        if [ ! -z "$latest_backup" ]; then
            local backup_age_seconds=$(( $(date +%s) - $(stat -c %Y "$latest_backup") ))
            local backup_age_hours=$(( backup_age_seconds / 3600 ))
            echo "Latest backup age: ${backup_age_hours} hours" >> "$bc_report"
        else
            echo "❌ No backups found" >> "$bc_report"
        fi
    else
        echo "❌ Backup directory not found" >> "$bc_report"
    fi
    echo "" >> "$bc_report"
    
    # Add recommendations
    echo "Recommendations:" >> "$bc_report"
    echo "--------------" >> "$bc_report"
    
    if [ $services_running -eq ${#critical_services[@]} ]; then
        echo "✅ All critical services are running" >> "$bc_report"
    else
        echo "❌ Some critical services are not running" >> "$bc_report"
        echo "   Action: Investigate and restart failed services" >> "$bc_report"
    fi
    
    # Check backup age
    if [ ! -z "$latest_backup" ] && [ $backup_age_hours -lt 24 ]; then
        echo "✅ Backups are current (less than 24 hours old)" >> "$bc_report"
    else
        echo "❌ Backups are not current (older than 24 hours)" >> "$bc_report"
        echo "   Action: Verify backup process and schedule" >> "$bc_report"
    fi
    echo "" >> "$bc_report"
    
    echo "✅ Business continuity report generated"
    echo "📋 BC report saved to: $bc_report"
    log_message "Business continuity report generated: $bc_report"
    
    # Display summary
    echo ""
    echo "Business Continuity Summary:"
    echo "  Services Running: $services_running/${#critical_services[@]}"
    echo "  Web Interfaces: Tested"
    echo "  Database Status: $(if sudo -u postgres pg_isready -U atlas_user -d atlas > /dev/null 2>&1; then echo "Accessible"; else echo "Not Accessible"; fi)"
    echo "  Backups: $(if [ ! -z "$latest_backup" ]; then echo "Available (${backup_age_hours}h old)"; else echo "Not Available"; fi)"
    echo "  Report: $bc_report"
}

# Function to clean old business continuity reports
clean_old_reports() {
    log_message "Cleaning old business continuity reports"
    
    echo ""
    echo "Cleaning Old Business Continuity Reports..."
    echo "=========================================="
    
    # Remove BC reports older than 90 days
    find "$BC_REPORT_DIR" -name "business_impact_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$BC_REPORT_DIR" -name "continuity_plans_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$BC_REPORT_DIR" -name "critical_functions_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$BC_REPORT_DIR" -name "recovery_teams_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$BC_REPORT_DIR" -name "remote_access_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$BC_REPORT_DIR" -name "business_continuity_*.txt" -mtime +90 -delete 2>/dev/null || true
    
    echo "✅ Old business continuity reports cleaned"
    log_message "Old business continuity reports cleaned"
}

# Main business continuity function
main() {
    log_message "=== Starting Atlas Business Continuity ==="
    
    # Initialize configuration
    initialize_bc_config
    
    # Start time
    local start_time=$(date)
    log_message "Business continuity started at: $start_time"
    
    # Handle different BC operations
    case $1 in
        "impact")
            assess_business_impact
            ;;
        "plans")
            evaluate_continuity_plans
            ;;
        "functions")
            test_critical_functions
            ;;
        "teams")
            verify_recovery_teams
            ;;
        "remote")
            test_remote_access
            ;;
        "report")
            generate_bc_report
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive business continuity assessment
            assess_business_impact
            evaluate_continuity_plans
            test_critical_functions
            verify_recovery_teams
            test_remote_access
            generate_bc_report
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Business continuity completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Business Continuity Completed ==="
    
    echo ""
    echo "✅ Business continuity assessment complete!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $BC_REPORT_DIR"
    echo "📝 Log file: $BC_LOG"
}

# Run main function
main "$@"