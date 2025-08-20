#!/bin/bash

# Atlas Production Automated Testing Script
# This script runs automated tests for the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Automated Testing..."

# Configuration
TESTING_LOG="/home/ubuntu/dev/atlas/logs/automated_testing.log"
TESTING_REPORT_DIR="/home/ubuntu/dev/atlas/reports/testing"
TESTING_CONFIG="/home/ubuntu/dev/atlas/config/testing.json"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $TESTING_LOG)"
mkdir -p "$TESTING_REPORT_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $TESTING_LOG
    echo "$1"
}

# Function to initialize testing configuration
initialize_testing_config() {
    log_message "Initializing testing configuration"
    
    # Create default testing configuration if it doesn't exist
    if [ ! -f "$TESTING_CONFIG" ]; then
        cat > "$TESTING_CONFIG" << EOF
{
    "testing": {
        "automated": {
            "enabled": true,
            "frequency_hours": 24,
            "test_types": [
                "unit",
                "integration",
                "system",
                "performance",
                "security"
            ],
            "coverage_target_percent": 80
        },
        "continuous": {
            "enabled": true,
            "on_commit": true,
            "on_merge": true,
            "on_deploy": true
        },
        "reporting": {
            "enabled": true,
            "format": "junit",
            "recipients": ["admin@khamel.com"]
        },
        "notifications": {
            "email": {
                "enabled": true,
                "smtp_server": "smtp.gmail.com",
                "port": 587,
                "sender": "atlas.tests@gmail.com",
                "password": "your_app_password"
            },
            "slack": {
                "enabled": false,
                "webhook_url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
            }
        }
    },
    "test_suites": {
        "unit": {
            "name": "Unit Tests",
            "description": "Individual component testing",
            "directory": "/home/ubuntu/dev/atlas/tests/unit",
            "runner": "pytest",
            "arguments": "-v --tb=short"
        },
        "integration": {
            "name": "Integration Tests",
            "description": "Component interaction testing",
            "directory": "/home/ubuntu/dev/atlas/tests/integration",
            "runner": "pytest",
            "arguments": "-v --tb=short"
        },
        "system": {
            "name": "System Tests",
            "description": "End-to-end system testing",
            "directory": "/home/ubuntu/dev/atlas/tests/system",
            "runner": "pytest",
            "arguments": "-v --tb=short"
        },
        "performance": {
            "name": "Performance Tests",
            "description": "System performance and load testing",
            "directory": "/home/ubuntu/dev/atlas/tests/performance",
            "runner": "locust",
            "arguments": "--headless --users 10 --spawn-rate 1 --run-time 5m"
        },
        "security": {
            "name": "Security Tests",
            "description": "Security vulnerability scanning",
            "directory": "/home/ubuntu/dev/atlas/tests/security",
            "runner": "bandit",
            "arguments": "-r /home/ubuntu/dev/atlas -f json"
        }
    },
    "test_coverage": {
        "target_percent": 80,
        "minimum_acceptable_percent": 60,
        "report_format": "html",
        "exclusions": [
            "tests/*",
            "docs/*",
            "config/*",
            "logs/*",
            "backups/*"
        ]
    }
}
EOF
        echo "✅ Created default testing configuration"
        log_message "Default testing configuration created"
    else
        echo "✅ Testing configuration already exists"
    fi
}

# Function to run unit tests
run_unit_tests() {
    log_message "Running unit tests"
    
    echo ""
    echo "Running Unit Tests..."
    echo "=================="
    
    local unit_test_report="$TESTING_REPORT_DIR/unit_tests_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create unit test report header
    echo "Atlas Production Unit Tests" > "$unit_test_report"
    echo "Generated: $(date)" >> "$unit_test_report"
    echo "=========================" >> "$unit_test_report"
    echo "" >> "$unit_test_report"
    
    # Get unit test configuration
    local unit_test_dir=$(jq -r '.test_suites.unit.directory' "$TESTING_CONFIG")
    local unit_test_runner=$(jq -r '.test_suites.unit.runner' "$TESTING_CONFIG")
    local unit_test_args=$(jq -r '.test_suites.unit.arguments' "$TESTING_CONFIG")
    
    echo "Unit Test Configuration:" >> "$unit_test_report"
    echo "---------------------" >> "$unit_test_report"
    echo "Test Directory: $unit_test_dir" >> "$unit_test_report"
    echo "Test Runner: $unit_test_runner" >> "$unit_test_report"
    echo "Arguments: $unit_test_args" >> "$unit_test_report"
    echo "" >> "$unit_test_report"
    
    # Check if test directory exists
    if [ ! -d "$unit_test_dir" ]; then
        echo "❌ Unit test directory not found: $unit_test_dir" >> "$unit_test_report"
        log_message "Unit test directory not found: $unit_test_dir"
        return 1
    fi
    
    # Change to test directory
    cd "$unit_test_dir"
    
    # Run unit tests
    echo "Running Unit Tests..." >> "$unit_test_report"
    echo "------------------" >> "$unit_test_report"
    
    # Activate virtual environment
    source /home/ubuntu/dev/atlas/atlas_venv/bin/activate
    
    # Run tests and capture output
    local test_output=""
    local test_exit_code=0
    
    if $unit_test_runner $unit_test_args > /tmp/unit_test_output.txt 2>&1; then
        test_output=$(cat /tmp/unit_test_output.txt)
        echo "$test_output" >> "$unit_test_report"
        echo "✅ Unit tests completed successfully" >> "$unit_test_report"
    else
        test_output=$(cat /tmp/unit_test_output.txt)
        echo "$test_output" >> "$unit_test_report"
        echo "❌ Unit tests failed" >> "$unit_test_report"
        test_exit_code=1
    fi
    
    # Clean up temporary file
    rm -f /tmp/unit_test_output.txt
    
    # Parse test results
    echo "" >> "$unit_test_report"
    echo "Test Results Summary:" >> "$unit_test_report"
    echo "------------------" >> "$unit_test_report"
    
    local total_tests=$(echo "$test_output" | grep -E "(PASSED|FAILED)" | wc -l)
    local passed_tests=$(echo "$test_output" | grep -c "PASSED")
    local failed_tests=$(echo "$test_output" | grep -c "FAILED")
    local skipped_tests=$(echo "$test_output" | grep -c "SKIPPED")
    
    echo "Total Tests: $total_tests" >> "$unit_test_report"
    echo "Passed Tests: $passed_tests" >> "$unit_test_report"
    echo "Failed Tests: $failed_tests" >> "$unit_test_report"
    echo "Skipped Tests: $skipped_tests" >> "$unit_test_report"
    
    if [ $total_tests -gt 0 ]; then
        local pass_rate=$(echo "scale=2; $passed_tests * 100 / $total_tests" | bc)
        echo "Pass Rate: ${pass_rate}%" >> "$unit_test_report"
    else
        local pass_rate=0
        echo "Pass Rate: 0%" >> "$unit_test_report"
    fi
    echo "" >> "$unit_test_report"
    
    # Coverage analysis
    echo "Coverage Analysis:" >> "$unit_test_report"
    echo "----------------" >> "$unit_test_report"
    
    # Run coverage analysis
    if command -v coverage &> /dev/null; then
        if coverage run -m pytest $unit_test_args > /dev/null 2>&1; then
            local coverage_report=$(coverage report 2>/dev/null || echo "Coverage report unavailable")
            echo "$coverage_report" >> "$unit_test_report"
            
            # Extract coverage percentage
            local coverage_percent=$(echo "$coverage_report" | grep "TOTAL" | awk '{print $4}' | sed 's/%//')
            if [ ! -z "$coverage_percent" ]; then
                echo "Coverage Percentage: ${coverage_percent}%" >> "$unit_test_report"
                
                # Compare with target
                local coverage_target=$(jq -r '.test_coverage.target_percent' "$TESTING_CONFIG")
                if [ $coverage_percent -ge $coverage_target ]; then
                    echo "✅ Coverage meets target (${coverage_percent}% >= ${coverage_target}%)" >> "$unit_test_report"
                else
                    echo "❌ Coverage does not meet target (${coverage_percent}% < ${coverage_target}%)" >> "$unit_test_report"
                fi
            else
                echo "Coverage Percentage: Unknown" >> "$unit_test_report"
            fi
        else
            echo "❌ Coverage analysis failed" >> "$unit_test_report"
        fi
    else
        echo "❌ Coverage tool not installed" >> "$unit_test_report"
    fi
    echo "" >> "$unit_test_report"
    
    # Test recommendations
    echo "Test Recommendations:" >> "$unit_test_report"
    echo "------------------" >> "$unit_test_report"
    
    if [ $test_exit_code -eq 0 ]; then
        echo "✅ Unit tests passed" >> "$unit_test_report"
        echo "✅ Continue current testing practices" >> "$unit_test_report"
        echo "✅ Review test coverage periodically" >> "$unit_test_report"
    else
        echo "❌ Unit tests failed" >> "$unit_test_report"
        echo "❌ Review failed test cases" >> "$unit_test_report"
        echo "❌ Fix test failures immediately" >> "$unit_test_report"
        echo "❌ Improve test coverage" >> "$unit_test_report"
    fi
    
    if [ $skipped_tests -gt 0 ]; then
        echo "⚠️ Skipped tests detected" >> "$unit_test_report"
        echo "✅ Review reasons for skipped tests" >> "$unit_test_report"
        echo "✅ Address dependencies causing skips" >> "$unit_test_report"
    fi
    echo "" >> "$unit_test_report"
    
    echo "✅ Unit tests completed"
    echo "📋 Unit test report saved to: $unit_test_report"
    log_message "Unit tests completed: $unit_test_report"
    
    # Display summary
    echo ""
    echo "Unit Test Summary:"
    echo "  Total Tests: $total_tests"
    echo "  Passed Tests: $passed_tests"
    echo "  Failed Tests: $failed_tests"
    echo "  Skipped Tests: $skipped_tests"
    echo "  Pass Rate: ${pass_rate}%"
    if [ ! -z "$coverage_percent" ]; then
        echo "  Coverage: ${coverage_percent}%"
        local coverage_target=$(jq -r '.test_coverage.target_percent' "$TESTING_CONFIG")
        if [ $coverage_percent -ge $coverage_target ]; then
            echo "  Coverage Status: ✅ MEETS TARGET"
        else
            echo "  Coverage Status: ❌ BELOW TARGET"
        fi
    else
        echo "  Coverage: Unknown"
    fi
    if [ $test_exit_code -eq 0 ]; then
        echo "  Test Status: ✅ PASSED"
    else
        echo "  Test Status: ❌ FAILED"
    fi
    echo "  Report: $unit_test_report"
    
    return $test_exit_code
}

# Function to run integration tests
run_integration_tests() {
    log_message "Running integration tests"
    
    echo ""
    echo "Running Integration Tests..."
    echo "========================="
    
    local integration_test_report="$TESTING_REPORT_DIR/integration_tests_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create integration test report header
    echo "Atlas Production Integration Tests" > "$integration_test_report"
    echo "Generated: $(date)" >> "$integration_test_report"
    echo "================================" >> "$integration_test_report"
    echo "" >> "$integration_test_report"
    
    # Get integration test configuration
    local integration_test_dir=$(jq -r '.test_suites.integration.directory' "$TESTING_CONFIG")
    local integration_test_runner=$(jq -r '.test_suites.integration.runner' "$TESTING_CONFIG")
    local integration_test_args=$(jq -r '.test_suites.integration.arguments' "$TESTING_CONFIG")
    
    echo "Integration Test Configuration:" >> "$integration_test_report"
    echo "-----------------------------" >> "$integration_test_report"
    echo "Test Directory: $integration_test_dir" >> "$integration_test_report"
    echo "Test Runner: $integration_test_runner" >> "$integration_test_report"
    echo "Arguments: $integration_test_args" >> "$integration_test_report"
    echo "" >> "$integration_test_report"
    
    # Check if test directory exists
    if [ ! -d "$integration_test_dir" ]; then
        echo "❌ Integration test directory not found: $integration_test_dir" >> "$integration_test_report"
        log_message "Integration test directory not found: $integration_test_dir"
        return 1
    fi
    
    # Change to test directory
    cd "$integration_test_dir"
    
    # Run integration tests
    echo "Running Integration Tests..." >> "$integration_test_report"
    echo "-------------------------" >> "$integration_test_report"
    
    # Activate virtual environment
    source /home/ubuntu/dev/atlas/atlas_venv/bin/activate
    
    # Run tests and capture output
    local test_output=""
    local test_exit_code=0
    
    if $integration_test_runner $integration_test_args > /tmp/integration_test_output.txt 2>&1; then
        test_output=$(cat /tmp/integration_test_output.txt)
        echo "$test_output" >> "$integration_test_report"
        echo "✅ Integration tests completed successfully" >> "$integration_test_report"
    else
        test_output=$(cat /tmp/integration_test_output.txt)
        echo "$test_output" >> "$integration_test_report"
        echo "❌ Integration tests failed" >> "$integration_test_report"
        test_exit_code=1
    fi
    
    # Clean up temporary file
    rm -f /tmp/integration_test_output.txt
    
    # Parse test results
    echo "" >> "$integration_test_report"
    echo "Test Results Summary:" >> "$integration_test_report"
    echo "------------------" >> "$integration_test_report"
    
    local total_tests=$(echo "$test_output" | grep -E "(PASSED|FAILED)" | wc -l)
    local passed_tests=$(echo "$test_output" | grep -c "PASSED")
    local failed_tests=$(echo "$test_output" | grep -c "FAILED")
    local skipped_tests=$(echo "$test_output" | grep -c "SKIPPED")
    
    echo "Total Tests: $total_tests" >> "$integration_test_report"
    echo "Passed Tests: $passed_tests" >> "$integration_test_report"
    echo "Failed Tests: $failed_tests" >> "$integration_test_report"
    echo "Skipped Tests: $skipped_tests" >> "$integration_test_report"
    
    if [ $total_tests -gt 0 ]; then
        local pass_rate=$(echo "scale=2; $passed_tests * 100 / $total_tests" | bc)
        echo "Pass Rate: ${pass_rate}%" >> "$integration_test_report"
    else
        local pass_rate=0
        echo "Pass Rate: 0%" >> "$integration_test_report"
    fi
    echo "" >> "$integration_test_report"
    
    # Integration test recommendations
    echo "Test Recommendations:" >> "$integration_test_report"
    echo "------------------" >> "$integration_test_report"
    
    if [ $test_exit_code -eq 0 ]; then
        echo "✅ Integration tests passed" >> "$integration_test_report"
        echo "✅ Continue current testing practices" >> "$integration_test_report"
        echo "✅ Review integration test coverage periodically" >> "$integration_test_report"
    else
        echo "❌ Integration tests failed" >> "$integration_test_report"
        echo "❌ Review failed integration test cases" >> "$integration_test_report"
        echo "❌ Fix integration test failures immediately" >> "$integration_test_report"
        echo "❌ Improve integration test coverage" >> "$integration_test_report"
    fi
    
    if [ $skipped_tests -gt 0 ]; then
        echo "⚠️ Skipped integration tests detected" >> "$integration_test_report"
        echo "✅ Review reasons for skipped integration tests" >> "$integration_test_report"
        echo "✅ Address dependencies causing integration test skips" >> "$integration_test_report"
    fi
    echo "" >> "$integration_test_report"
    
    echo "✅ Integration tests completed"
    echo "📋 Integration test report saved to: $integration_test_report"
    log_message "Integration tests completed: $integration_test_report"
    
    # Display summary
    echo ""
    echo "Integration Test Summary:"
    echo "  Total Tests: $total_tests"
    echo "  Passed Tests: $passed_tests"
    echo "  Failed Tests: $failed_tests"
    echo "  Skipped Tests: $skipped_tests"
    echo "  Pass Rate: ${pass_rate}%"
    if [ $test_exit_code -eq 0 ]; then
        echo "  Test Status: ✅ PASSED"
    else
        echo "  Test Status: ❌ FAILED"
    fi
    echo "  Report: $integration_test_report"
    
    return $test_exit_code
}

# Function to run system tests
run_system_tests() {
    log_message "Running system tests"
    
    echo ""
    echo "Running System Tests..."
    echo "===================="
    
    local system_test_report="$TESTING_REPORT_DIR/system_tests_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create system test report header
    echo "Atlas Production System Tests" > "$system_test_report"
    echo "Generated: $(date)" >> "$system_test_report"
    echo "===========================" >> "$system_test_report"
    echo "" >> "$system_test_report"
    
    # Get system test configuration
    local system_test_dir=$(jq -r '.test_suites.system.directory' "$TESTING_CONFIG")
    local system_test_runner=$(jq -r '.test_suites.system.runner' "$TESTING_CONFIG")
    local system_test_args=$(jq -r '.test_suites.system.arguments' "$TESTING_CONFIG")
    
    echo "System Test Configuration:" >> "$system_test_report"
    echo "------------------------" >> "$system_test_report"
    echo "Test Directory: $system_test_dir" >> "$system_test_report"
    echo "Test Runner: $system_test_runner" >> "$system_test_report"
    echo "Arguments: $system_test_args" >> "$system_test_report"
    echo "" >> "$system_test_report"
    
    # Check if test directory exists
    if [ ! -d "$system_test_dir" ]; then
        echo "❌ System test directory not found: $system_test_dir" >> "$system_test_report"
        log_message "System test directory not found: $system_test_dir"
        return 1
    fi
    
    # Change to test directory
    cd "$system_test_dir"
    
    # Run system tests
    echo "Running System Tests..." >> "$system_test_report"
    echo "--------------------" >> "$system_test_report"
    
    # Activate virtual environment
    source /home/ubuntu/dev/atlas/atlas_venv/bin/activate
    
    # Run tests and capture output
    local test_output=""
    local test_exit_code=0
    
    if $system_test_runner $system_test_args > /tmp/system_test_output.txt 2>&1; then
        test_output=$(cat /tmp/system_test_output.txt)
        echo "$test_output" >> "$system_test_report"
        echo "✅ System tests completed successfully" >> "$system_test_report"
    else
        test_output=$(cat /tmp/system_test_output.txt)
        echo "$test_output" >> "$system_test_report"
        echo "❌ System tests failed" >> "$system_test_report"
        test_exit_code=1
    fi
    
    # Clean up temporary file
    rm -f /tmp/system_test_output.txt
    
    # Parse test results
    echo "" >> "$system_test_report"
    echo "Test Results Summary:" >> "$system_test_report"
    echo "------------------" >> "$system_test_report"
    
    local total_tests=$(echo "$test_output" | grep -E "(PASSED|FAILED)" | wc -l)
    local passed_tests=$(echo "$test_output" | grep -c "PASSED")
    local failed_tests=$(echo "$test_output" | grep -c "FAILED")
    local skipped_tests=$(echo "$test_output" | grep -c "SKIPPED")
    
    echo "Total Tests: $total_tests" >> "$system_test_report"
    echo "Passed Tests: $passed_tests" >> "$system_test_report"
    echo "Failed Tests: $failed_tests" >> "$system_test_report"
    echo "Skipped Tests: $skipped_tests" >> "$system_test_report"
    
    if [ $total_tests -gt 0 ]; then
        local pass_rate=$(echo "scale=2; $passed_tests * 100 / $total_tests" | bc)
        echo "Pass Rate: ${pass_rate}%" >> "$system_test_report"
    else
        local pass_rate=0
        echo "Pass Rate: 0%" >> "$system_test_report"
    fi
    echo "" >> "$system_test_report"
    
    # System test recommendations
    echo "Test Recommendations:" >> "$system_test_report"
    echo "------------------" >> "$system_test_report"
    
    if [ $test_exit_code -eq 0 ]; then
        echo "✅ System tests passed" >> "$system_test_report"
        echo "✅ Continue current testing practices" >> "$system_test_report"
        echo "✅ Review system test coverage periodically" >> "$system_test_report"
    else
        echo "❌ System tests failed" >> "$system_test_report"
        echo "❌ Review failed system test cases" >> "$system_test_report"
        echo "❌ Fix system test failures immediately" >> "$system_test_report"
        echo "❌ Improve system test coverage" >> "$system_test_report"
    fi
    
    if [ $skipped_tests -gt 0 ]; then
        echo "⚠️ Skipped system tests detected" >> "$system_test_report"
        echo "✅ Review reasons for skipped system tests" >> "$system_test_report"
        echo "✅ Address dependencies causing system test skips" >> "$system_test_report"
    fi
    echo "" >> "$system_test_report"
    
    echo "✅ System tests completed"
    echo "📋 System test report saved to: $system_test_report"
    log_message "System tests completed: $system_test_report"
    
    # Display summary
    echo ""
    echo "System Test Summary:"
    echo "  Total Tests: $total_tests"
    echo "  Passed Tests: $passed_tests"
    echo "  Failed Tests: $failed_tests"
    echo "  Skipped Tests: $skipped_tests"
    echo "  Pass Rate: ${pass_rate}%"
    if [ $test_exit_code -eq 0 ]; then
        echo "  Test Status: ✅ PASSED"
    else
        echo "  Test Status: ❌ FAILED"
    fi
    echo "  Report: $system_test_report"
    
    return $test_exit_code
}

# Function to run performance tests
run_performance_tests() {
    log_message "Running performance tests"
    
    echo ""
    echo "Running Performance Tests..."
    echo "========================="
    
    local performance_test_report="$TESTING_REPORT_DIR/performance_tests_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create performance test report header
    echo "Atlas Production Performance Tests" > "$performance_test_report"
    echo "Generated: $(date)" >> "$performance_test_report"
    echo "================================" >> "$performance_test_report"
    echo "" >> "$performance_test_report"
    
    # Get performance test configuration
    local performance_test_dir=$(jq -r '.test_suites.performance.directory' "$TESTING_CONFIG")
    local performance_test_runner=$(jq -r '.test_suites.performance.runner' "$TESTING_CONFIG")
    local performance_test_args=$(jq -r '.test_suites.performance.arguments' "$TESTING_CONFIG")
    
    echo "Performance Test Configuration:" >> "$performance_test_report"
    echo "-----------------------------" >> "$performance_test_report"
    echo "Test Directory: $performance_test_dir" >> "$performance_test_report"
    echo "Test Runner: $performance_test_runner" >> "$performance_test_report"
    echo "Arguments: $performance_test_args" >> "$performance_test_report"
    echo "" >> "$performance_test_report"
    
    # Check if performance testing tool is installed
    if ! command -v $performance_test_runner &> /dev/null; then
        echo "❌ Performance testing tool not installed: $performance_test_runner" >> "$performance_test_report"
        log_message "Performance testing tool not installed: $performance_test_runner"
        return 1
    fi
    
    # Check if test directory exists
    if [ ! -d "$performance_test_dir" ]; then
        echo "❌ Performance test directory not found: $performance_test_dir" >> "$performance_test_report"
        log_message "Performance test directory not found: $performance_test_dir"
        return 1
    fi
    
    # Change to test directory
    cd "$performance_test_dir"
    
    # Run performance tests
    echo "Running Performance Tests..." >> "$performance_test_report"
    echo "-------------------------" >> "$performance_test_report"
    
    # Activate virtual environment
    source /home/ubuntu/dev/atlas/atlas_venv/bin/activate
    
    # Run tests and capture output
    local test_output=""
    local test_exit_code=0
    
    if $performance_test_runner $performance_test_args > /tmp/performance_test_output.txt 2>&1; then
        test_output=$(cat /tmp/performance_test_output.txt)
        echo "$test_output" >> "$performance_test_report"
        echo "✅ Performance tests completed successfully" >> "$performance_test_report"
    else
        test_output=$(cat /tmp/performance_test_output.txt)
        echo "$test_output" >> "$performance_test_report"
        echo "❌ Performance tests failed" >> "$performance_test_report"
        test_exit_code=1
    fi
    
    # Clean up temporary file
    rm -f /tmp/performance_test_output.txt
    
    # Parse test results
    echo "" >> "$performance_test_report"
    echo "Performance Test Results Summary:" >> "$performance_test_report"
    echo "-------------------------------" >> "$performance_test_report"
    
    # Extract performance metrics
    local response_times=$(echo "$test_output" | grep -E "(Response time|Latency)" | head -5)
    local throughput=$(echo "$test_output" | grep -E "(Throughput|Requests per second)" | head -3)
    local errors=$(echo "$test_output" | grep -E "(Error|Failure)" | head -3)
    
    if [ ! -z "$response_times" ]; then
        echo "Response Times:" >> "$performance_test_report"
        echo "$response_times" >> "$performance_test_report"
    else
        echo "Response Times: Not measured" >> "$performance_test_report"
    fi
    
    if [ ! -z "$throughput" ]; then
        echo "Throughput:" >> "$performance_test_report"
        echo "$throughput" >> "$performance_test_report"
    else
        echo "Throughput: Not measured" >> "$performance_test_report"
    fi
    
    if [ ! -z "$errors" ]; then
        echo "Errors:" >> "$performance_test_report"
        echo "$errors" >> "$performance_test_report"
    else
        echo "Errors: None detected" >> "$performance_test_report"
    fi
    echo "" >> "$performance_test_report"
    
    # Performance test recommendations
    echo "Performance Test Recommendations:" >> "$performance_test_report"
    echo "-------------------------------" >> "$performance_test_report"
    
    if [ $test_exit_code -eq 0 ]; then
        echo "✅ Performance tests completed successfully" >> "$performance_test_report"
        echo "✅ Continue current performance testing practices" >> "$performance_test_report"
        echo "✅ Review performance metrics periodically" >> "$performance_test_report"
    else
        echo "❌ Performance tests failed" >> "$performance_test_report"
        echo "❌ Review failed performance test cases" >> "$performance_test_report"
        echo "❌ Fix performance test failures immediately" >> "$performance_test_report"
        echo "❌ Improve performance test coverage" >> "$performance_test_report"
    fi
    
    echo "" >> "$performance_test_report"
    
    echo "✅ Performance tests completed"
    echo "📋 Performance test report saved to: $performance_test_report"
    log_message "Performance tests completed: $performance_test_report"
    
    # Display summary
    echo ""
    echo "Performance Test Summary:"
    echo "  Test Runner: $performance_test_runner"
    echo "  Arguments: $performance_test_args"
    echo "  Response Times:"
    if [ ! -z "$response_times" ]; then
        echo "$response_times" | head -3 | while read -r line; do
            echo "    $line"
        done
    else
        echo "    Not measured"
    fi
    echo "  Throughput:"
    if [ ! -z "$throughput" ]; then
        echo "$throughput" | head -2 | while read -r line; do
            echo "    $line"
        done
    else
        echo "    Not measured"
    fi
    echo "  Errors:"
    if [ ! -z "$errors" ]; then
        echo "$errors" | head -2 | while read -r line; do
            echo "    $line"
        done
    else
        echo "    None detected"
    fi
    if [ $test_exit_code -eq 0 ]; then
        echo "  Test Status: ✅ PASSED"
    else
        echo "  Test Status: ❌ FAILED"
    fi
    echo "  Report: $performance_test_report"
    
    return $test_exit_code
}

# Function to run security tests
run_security_tests() {
    log_message "Running security tests"
    
    echo ""
    echo "Running Security Tests..."
    echo "======================"
    
    local security_test_report="$TESTING_REPORT_DIR/security_tests_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create security test report header
    echo "Atlas Production Security Tests" > "$security_test_report"
    echo "Generated: $(date)" >> "$security_test_report"
    echo "=============================" >> "$security_test_report"
    echo "" >> "$security_test_report"
    
    # Get security test configuration
    local security_test_dir=$(jq -r '.test_suites.security.directory' "$TESTING_CONFIG")
    local security_test_runner=$(jq -r '.test_suites.security.runner' "$TESTING_CONFIG")
    local security_test_args=$(jq -r '.test_suites.security.arguments' "$TESTING_CONFIG")
    
    echo "Security Test Configuration:" >> "$security_test_report"
    echo "--------------------------" >> "$security_test_report"
    echo "Test Directory: $security_test_dir" >> "$security_test_report"
    echo "Test Runner: $security_test_runner" >> "$security_test_report"
    echo "Arguments: $security_test_args" >> "$security_test_report"
    echo "" >> "$security_test_report"
    
    # Check if security testing tool is installed
    if ! command -v $security_test_runner &> /dev/null; then
        echo "❌ Security testing tool not installed: $security_test_runner" >> "$security_test_report"
        log_message "Security testing tool not installed: $security_test_runner"
        return 1
    fi
    
    # Change to Atlas directory
    cd /home/ubuntu/dev/atlas
    
    # Run security tests
    echo "Running Security Tests..." >> "$security_test_report"
    echo "----------------------" >> "$security_test_report"
    
    # Activate virtual environment
    source /home/ubuntu/dev/atlas/atlas_venv/bin/activate
    
    # Run tests and capture output
    local test_output=""
    local test_exit_code=0
    
    if $security_test_runner $security_test_args > /tmp/security_test_output.txt 2>&1; then
        test_output=$(cat /tmp/security_test_output.txt)
        echo "$test_output" >> "$security_test_report"
        echo "✅ Security tests completed successfully" >> "$security_test_report"
    else
        test_output=$(cat /tmp/security_test_output.txt)
        echo "$test_output" >> "$security_test_report"
        echo "❌ Security tests failed" >> "$security_test_report"
        test_exit_code=1
    fi
    
    # Clean up temporary file
    rm -f /tmp/security_test_output.txt
    
    # Parse test results
    echo "" >> "$security_test_report"
    echo "Security Test Results Summary:" >> "$security_test_report"
    echo "----------------------------" >> "$security_test_report"
    
    # Extract security findings
    local high_severity=$(echo "$test_output" | grep -c "HIGH")
    local medium_severity=$(echo "$test_output" | grep -c "MEDIUM")
    local low_severity=$(echo "$test_output" | grep -c "LOW")
    
    echo "Security Findings:" >> "$security_test_report"
    echo "  High Severity: $high_severity" >> "$security_test_report"
    echo "  Medium Severity: $medium_severity" >> "$security_test_report"
    echo "  Low Severity: $low_severity" >> "$security_test_report"
    echo "" >> "$security_test_report"
    
    # Extract vulnerabilities
    local vulnerabilities=$(echo "$test_output" | grep -E "(VULNERABILITY|VULN)" | head -5)
    if [ ! -z "$vulnerabilities" ]; then
        echo "Vulnerabilities Found:" >> "$security_test_report"
        echo "$vulnerabilities" >> "$security_test_report"
    else
        echo "Vulnerabilities Found: None detected" >> "$security_test_report"
    fi
    echo "" >> "$security_test_report"
    
    # Security test recommendations
    echo "Security Test Recommendations:" >> "$security_test_report"
    echo "----------------------------" >> "$security_test_report"
    
    if [ $test_exit_code -eq 0 ]; then
        echo "✅ Security tests completed successfully" >> "$security_test_report"
        echo "✅ Continue current security testing practices" >> "$security_test_report"
        echo "✅ Review security findings periodically" >> "$security_test_report"
    else
        echo "❌ Security tests failed" >> "$security_test_report"
        echo "❌ Review failed security test cases" >> "$security_test_report"
        echo "❌ Fix security test failures immediately" >> "$security_test_report"
        echo "❌ Improve security test coverage" >> "$security_test_report"
    fi
    
    if [ $high_severity -gt 0 ] || [ $medium_severity -gt 0 ]; then
        echo "❌ Security vulnerabilities detected" >> "$security_test_report"
        echo "❌ Address high and medium severity issues immediately" >> "$security_test_report"
        echo "✅ Schedule regular security scans" >> "$security_test_report"
    else
        echo "✅ No high or medium severity security issues detected" >> "$security_test_report"
        echo "✅ Continue regular security monitoring" >> "$security_test_report"
    fi
    echo "" >> "$security_test_report"
    
    echo "✅ Security tests completed"
    echo "📋 Security test report saved to: $security_test_report"
    log_message "Security tests completed: $security_test_report"
    
    # Display summary
    echo ""
    echo "Security Test Summary:"
    echo "  Test Runner: $security_test_runner"
    echo "  Arguments: $security_test_args"
    echo "  High Severity Issues: $high_severity"
    echo "  Medium Severity Issues: $medium_severity"
    echo "  Low Severity Issues: $low_severity"
    echo "  Vulnerabilities:"
    if [ ! -z "$vulnerabilities" ]; then
        echo "$vulnerabilities" | head -3 | while read -r line; do
            echo "    $line"
        done
    else
        echo "    None detected"
    fi
    if [ $test_exit_code -eq 0 ]; then
        echo "  Test Status: ✅ PASSED"
    else
        echo "  Test Status: ❌ FAILED"
    fi
    if [ $high_severity -gt 0 ] || [ $medium_severity -gt 0 ]; then
        echo "  Security Status: ❌ VULNERABILITIES DETECTED"
    else
        echo "  Security Status: ✅ NO CRITICAL VULNERABILITIES"
    fi
    echo "  Report: $security_test_report"
    
    return $test_exit_code
}

# Function to generate test summary report
generate_test_summary() {
    log_message "Generating test summary report"
    
    echo ""
    echo "Generating Test Summary Report..."
    echo "=============================="
    
    local summary_report="$TESTING_REPORT_DIR/test_summary_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create test summary report header
    echo "Atlas Production Test Summary Report" > "$summary_report"
    echo "Generated: $(date)" >> "$summary_report"
    echo "=================================" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add system information
    echo "System Information:" >> "$summary_report"
    echo "------------------" >> "$summary_report"
    echo "Hostname: $(hostname)" >> "$summary_report"
    echo "OS: $(lsb_release -d | cut -f2)" >> "$summary_report"
    echo "Kernel: $(uname -r)" >> "$summary_report"
    echo "Uptime: $(uptime -p)" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add test configuration
    echo "Test Configuration:" >> "$summary_report"
    echo "-----------------" >> "$summary_report"
    
    local automated_enabled=$(jq -r '.testing.automated.enabled' "$TESTING_CONFIG")
    local continuous_enabled=$(jq -r '.testing.continuous.enabled' "$TESTING_CONFIG")
    local coverage_target=$(jq -r '.test_coverage.target_percent' "$TESTING_CONFIG")
    local test_types=$(jq -r '.testing.automated.test_types[]' "$TESTING_CONFIG")
    
    echo "Automated Testing: $automated_enabled" >> "$summary_report"
    echo "Continuous Testing: $continuous_enabled" >> "$summary_report"
    echo "Coverage Target: ${coverage_target}%" >> "$summary_report"
    echo "Test Types:" >> "$summary_report"
    while IFS= read -r test_type; do
        echo "  - $test_type" >> "$summary_report"
    done <<< "$test_types"
    echo "" >> "$summary_report"
    
    # Add test results summary
    echo "Test Results Summary:" >> "$summary_report"
    echo "------------------" >> "$summary_report"
    
    # Find recent test reports
    local recent_unit_test=$(ls -t "$TESTING_REPORT_DIR"/unit_tests_*.txt 2>/dev/null | head -1)
    local recent_integration_test=$(ls -t "$TESTING_REPORT_DIR"/integration_tests_*.txt 2>/dev/null | head -1)
    local recent_system_test=$(ls -t "$TESTING_REPORT_DIR"/system_tests_*.txt 2>/dev/null | head -1)
    local recent_performance_test=$(ls -t "$TESTING_REPORT_DIR"/performance_tests_*.txt 2>/dev/null | head -1)
    local recent_security_test=$(ls -t "$TESTING_REPORT_DIR"/security_tests_*.txt 2>/dev/null | head -1)
    
    # Parse unit test results
    echo "Unit Tests:" >> "$summary_report"
    echo "----------" >> "$summary_report"
    if [ ! -z "$recent_unit_test" ] && [ -f "$recent_unit_test" ]; then
        local unit_total=$(grep "Total Tests:" "$recent_unit_test" | awk '{print $3}' || echo "0")
        local unit_passed=$(grep "Passed Tests:" "$recent_unit_test" | awk '{print $3}' || echo "0")
        local unit_failed=$(grep "Failed Tests:" "$recent_unit_test" | awk '{print $3}' || echo "0")
        local unit_skipped=$(grep "Skipped Tests:" "$recent_unit_test" | awk '{print $3}' || echo "0")
        local unit_coverage=$(grep "Coverage Percentage:" "$recent_unit_test" | awk '{print $3}' | sed 's/%//' || echo "0")
        local unit_status=$(grep "Test Status:" "$recent_unit_test" | awk '{print $3}' || echo "UNKNOWN")
        
        echo "  Total Tests: $unit_total" >> "$summary_report"
        echo "  Passed Tests: $unit_passed" >> "$summary_report"
        echo "  Failed Tests: $unit_failed" >> "$summary_report"
        echo "  Skipped Tests: $unit_skipped" >> "$summary_report"
        echo "  Coverage: ${unit_coverage}%" >> "$summary_report"
        echo "  Status: $unit_status" >> "$summary_report"
    else
        echo "  No recent unit test report found" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Parse integration test results
    echo "Integration Tests:" >> "$summary_report"
    echo "----------------" >> "$summary_report"
    if [ ! -z "$recent_integration_test" ] && [ -f "$recent_integration_test" ]; then
        local integration_total=$(grep "Total Tests:" "$recent_integration_test" | awk '{print $3}' || echo "0")
        local integration_passed=$(grep "Passed Tests:" "$recent_integration_test" | awk '{print $3}' || echo "0")
        local integration_failed=$(grep "Failed Tests:" "$recent_integration_test" | awk '{print $3}' || echo "0")
        local integration_skipped=$(grep "Skipped Tests:" "$recent_integration_test" | awk '{print $3}' || echo "0")
        local integration_status=$(grep "Test Status:" "$recent_integration_test" | awk '{print $3}' || echo "UNKNOWN")
        
        echo "  Total Tests: $integration_total" >> "$summary_report"
        echo "  Passed Tests: $integration_passed" >> "$summary_report"
        echo "  Failed Tests: $integration_failed" >> "$summary_report"
        echo "  Skipped Tests: $integration_skipped" >> "$summary_report"
        echo "  Status: $integration_status" >> "$summary_report"
    else
        echo "  No recent integration test report found" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Parse system test results
    echo "System Tests:" >> "$summary_report"
    echo "------------" >> "$summary_report"
    if [ ! -z "$recent_system_test" ] && [ -f "$recent_system_test" ]; then
        local system_total=$(grep "Total Tests:" "$recent_system_test" | awk '{print $3}' || echo "0")
        local system_passed=$(grep "Passed Tests:" "$recent_system_test" | awk '{print $3}' || echo "0")
        local system_failed=$(grep "Failed Tests:" "$recent_system_test" | awk '{print $3}' || echo "0")
        local system_skipped=$(grep "Skipped Tests:" "$recent_system_test" | awk '{print $3}' || echo "0")
        local system_status=$(grep "Test Status:" "$recent_system_test" | awk '{print $3}' || echo "UNKNOWN")
        
        echo "  Total Tests: $system_total" >> "$summary_report"
        echo "  Passed Tests: $system_passed" >> "$summary_report"
        echo "  Failed Tests: $system_failed" >> "$summary_report"
        echo "  Skipped Tests: $system_skipped" >> "$summary_report"
        echo "  Status: $system_status" >> "$summary_report"
    else
        echo "  No recent system test report found" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Parse performance test results
    echo "Performance Tests:" >> "$summary_report"
    echo "----------------" >> "$summary_report"
    if [ ! -z "$recent_performance_test" ] && [ -f "$recent_performance_test" ]; then
        local performance_status=$(grep "Test Status:" "$recent_performance_test" | awk '{print $3}' || echo "UNKNOWN")
        echo "  Status: $performance_status" >> "$summary_report"
        
        # Extract performance metrics
        local response_times=$(grep "Response Times:" "$recent_performance_test" | wc -l)
        local throughput=$(grep "Throughput:" "$recent_performance_test" | wc -l)
        local errors=$(grep "Errors:" "$recent_performance_test" | wc -l)
        
        if [ $response_times -gt 0 ]; then
            echo "  Response Times: Measured" >> "$summary_report"
        else
            echo "  Response Times: Not measured" >> "$summary_report"
        fi
        
        if [ $throughput -gt 0 ]; then
            echo "  Throughput: Measured" >> "$summary_report"
        else
            echo "  Throughput: Not measured" >> "$summary_report"
        fi
        
        if [ $errors -gt 0 ]; then
            echo "  Errors: Detected" >> "$summary_report"
        else
            echo "  Errors: None detected" >> "$summary_report"
        fi
    else
        echo "  No recent performance test report found" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Parse security test results
    echo "Security Tests:" >> "$summary_report"
    echo "-------------" >> "$summary_report"
    if [ ! -z "$recent_security_test" ] && [ -f "$recent_security_test" ]; then
        local security_status=$(grep "Test Status:" "$recent_security_test" | awk '{print $3}' || echo "UNKNOWN")
        local security_vulnerabilities=$(grep "Security Status:" "$recent_security_test" | awk '{print $3}' | grep -c "VULNERABILITIES DETECTED" || echo "0")
        echo "  Status: $security_status" >> "$summary_report"
        
        if [ $security_vulnerabilities -gt 0 ]; then
            echo "  Security Status: ❌ VULNERABILITIES DETECTED" >> "$summary_report"
            local high_severity=$(grep "High Severity:" "$recent_security_test" | awk '{print $3}' || echo "0")
            local medium_severity=$(grep "Medium Severity:" "$recent_security_test" | awk '{print $3}' || echo "0")
            echo "  High Severity Issues: $high_severity" >> "$summary_report"
            echo "  Medium Severity Issues: $medium_severity" >> "$summary_report"
        else
            echo "  Security Status: ✅ NO CRITICAL VULNERABILITIES" >> "$summary_report"
        fi
    else
        echo "  No recent security test report found" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Add overall test status
    echo "Overall Test Status:" >> "$summary_report"
    echo "------------------" >> "$summary_report"
    
    # Determine overall status
    local overall_status="UNKNOWN"
    local failed_tests=0
    
    # Count failed tests
    if [ ! -z "$recent_unit_test" ] && [ -f "$recent_unit_test" ]; then
        local unit_status=$(grep "Test Status:" "$recent_unit_test" | awk '{print $3}' || echo "UNKNOWN")
        if [ "$unit_status" = "❌" ] || [ "$unit_status" = "FAILED" ]; then
            failed_tests=$((failed_tests + 1))
        fi
    fi
    
    if [ ! -z "$recent_integration_test" ] && [ -f "$recent_integration_test" ]; then
        local integration_status=$(grep "Test Status:" "$recent_integration_test" | awk '{print $3}' || echo "UNKNOWN")
        if [ "$integration_status" = "❌" ] || [ "$integration_status" = "FAILED" ]; then
            failed_tests=$((failed_tests + 1))
        fi
    fi
    
    if [ ! -z "$recent_system_test" ] && [ -f "$recent_system_test" ]; then
        local system_status=$(grep "Test Status:" "$recent_system_test" | awk '{print $3}' || echo "UNKNOWN")
        if [ "$system_status" = "❌" ] || [ "$system_status" = "FAILED" ]; then
            failed_tests=$((failed_tests + 1))
        fi
    fi
    
    if [ ! -z "$recent_performance_test" ] && [ -f "$recent_performance_test" ]; then
        local performance_status=$(grep "Test Status:" "$recent_performance_test" | awk '{print $3}' || echo "UNKNOWN")
        if [ "$performance_status" = "❌" ] || [ "$performance_status" = "FAILED" ]; then
            failed_tests=$((failed_tests + 1))
        fi
    fi
    
    if [ ! -z "$recent_security_test" ] && [ -f "$recent_security_test" ]; then
        local security_status=$(grep "Security Status:" "$recent_security_test" | awk '{print $3}' | grep -c "VULNERABILITIES DETECTED" || echo "0")
        if [ $security_status -gt 0 ]; then
            failed_tests=$((failed_tests + 1))
        fi
    fi
    
    if [ $failed_tests -eq 0 ]; then
        overall_status="✅ ALL TESTS PASSED"
    elif [ $failed_tests -lt 3 ]; then
        overall_status="⚠️ SOME TESTS FAILED"
    else
        overall_status="❌ MULTIPLE TESTS FAILED"
    fi
    
    echo "Overall Status: $overall_status" >> "$summary_report"
    echo "Failed Test Suites: $failed_tests" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add recommendations
    echo "Recommendations:" >> "$summary_report"
    echo "-------------" >> "$summary_report"
    
    if [ "$overall_status" = "✅ ALL TESTS PASSED" ]; then
        echo "✅ Continue current testing practices" >> "$summary_report"
        echo "✅ Schedule regular automated tests" >> "$summary_report"
        echo "✅ Monitor test results for trends" >> "$summary_report"
    elif [ "$overall_status" = "⚠️ SOME TESTS FAILED" ]; then
        echo "⚠️ Review failed test suites" >> "$summary_report"
        echo "✅ Address identified issues promptly" >> "$summary_report"
        echo "✅ Schedule additional testing after fixes" >> "$summary_report"
    else
        echo "❌ Address all failed test suites immediately" >> "$summary_report"
        echo "✅ Implement comprehensive testing improvements" >> "$summary_report"
        echo "✅ Schedule emergency testing review" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Add next steps
    echo "Next Steps:" >> "$summary_report"
    echo "----------" >> "$summary_report"
    echo "1. Review detailed test reports in $TESTING_REPORT_DIR/" >> "$summary_report"
    echo "2. Address any failed test cases" >> "$summary_report"
    echo "3. Improve test coverage to meet ${coverage_target}% target" >> "$summary_report"
    echo "4. Schedule next automated test run" >> "$summary_report"
    echo "5. Update test configuration as needed" >> "$summary_report"
    echo "" >> "$summary_report"
    
    echo "✅ Test summary report generated"
    echo "📋 Test summary report saved to: $summary_report"
    log_message "Test summary report generated: $summary_report"
    
    # Display summary
    echo ""
    echo "Test Summary Report:"
    echo "  System: $(hostname) ($(lsb_release -d | cut -f2))"
    echo "  Kernel: $(uname -r)"
    echo "  Uptime: $(uptime -p)"
    echo "  Automated Testing: $automated_enabled"
    echo "  Continuous Testing: $continuous_enabled"
    echo "  Coverage Target: ${coverage_target}%"
    echo "  Test Types: $(echo "$test_types" | tr '\n' ', ' | sed 's/, $//')"
    echo "  Overall Status: $overall_status"
    echo "  Failed Suites: $failed_tests"
    echo "  Report: $summary_report"
}

# Function to clean old test reports
clean_old_test_reports() {
    log_message "Cleaning old test reports"
    
    echo ""
    echo "Cleaning Old Test Reports..."
    echo "=========================="
    
    # Remove test reports older than 90 days
    find "$TESTING_REPORT_DIR" -name "unit_tests_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$TESTING_REPORT_DIR" -name "integration_tests_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$TESTING_REPORT_DIR" -name "system_tests_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$TESTING_REPORT_DIR" -name "performance_tests_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$TESTING_REPORT_DIR" -name "security_tests_*.txt" -mtime +90 -delete 2>/dev/null || true
    find "$TESTING_REPORT_DIR" -name "test_summary_*.txt" -mtime +90 -delete 2>/dev/null || true
    
    echo "✅ Old test reports cleaned"
    log_message "Old test reports cleaned"
}

# Main function
main() {
    log_message "=== Starting Atlas Automated Testing ==="
    
    # Initialize configuration
    initialize_testing_config
    
    # Start time
    local start_time=$(date)
    log_message "Automated testing started at: $start_time"
    
    # Handle different testing operations
    case $1 in
        "unit")
            run_unit_tests
            ;;
        "integration")
            run_integration_tests
            ;;
        "system")
            run_system_tests
            ;;
        "performance")
            run_performance_tests
            ;;
        "security")
            run_security_tests
            ;;
        "summary")
            generate_test_summary
            ;;
        "clean")
            clean_old_test_reports
            ;;
        *)
            # Run comprehensive automated testing
            run_unit_tests
            run_integration_tests
            run_system_tests
            run_performance_tests
            run_security_tests
            generate_test_summary
            clean_old_test_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Automated testing completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Automated Testing Completed ==="
    
    echo ""
    echo "✅ Automated testing completed!"
    echo "⏱️ Duration: ${duration} seconds"
    echo "📊 Reports saved to: $TESTING_REPORT_DIR"
    echo "📝 Log file: $TESTING_LOG"
}

# Run main function
main "$@"