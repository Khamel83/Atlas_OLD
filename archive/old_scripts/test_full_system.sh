#!/bin/bash
# Atlas Integration Test Suite
# Comprehensive testing for fresh clone validation

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0

test_result() {
    local test_name="$1"
    local result="$2"
    local expected="$3"
    
    if [ "$result" = "$expected" ]; then
        echo -e "${GREEN}✅ PASS${NC}: $test_name"
        ((PASSED++))
    else
        echo -e "${RED}❌ FAIL${NC}: $test_name (expected: $expected, got: $result)"
        ((FAILED++))
    fi
}

echo -e "${BLUE}🧪 Atlas Integration Test Suite${NC}"
echo "======================================="

# Test 1: Database initialization
echo -e "${BLUE}📊 Testing database initialization...${NC}"
python3 -c "
from helpers.simple_database import SimpleDatabase
import os
try:
    db = SimpleDatabase()
    print('database_init_success')
except Exception as e:
    print(f'database_init_failed: {e}')
" > /tmp/test_db.out 2>&1

DB_RESULT=$(head -1 /tmp/test_db.out)
test_result "Database initialization" "$DB_RESULT" "database_init_success"

# Test 2: Database tables exist
echo -e "${BLUE}🗃️ Testing database schema...${NC}"
if [ -f "atlas.db" ]; then
    TABLES=$(sqlite3 atlas.db ".tables" 2>/dev/null | wc -w)
    if [ "$TABLES" -ge 4 ]; then
        test_result "Database schema" "tables_exist" "tables_exist"
    else
        test_result "Database schema" "missing_tables" "tables_exist"
    fi
else
    test_result "Database schema" "no_database" "tables_exist"
fi

# Test 3: Python dependencies
echo -e "${BLUE}📦 Testing Python dependencies...${NC}"
python3 -c "
try:
    import fastapi, sqlite3, requests
    print('dependencies_ok')
except ImportError as e:
    print('dependencies_missing')
" > /tmp/test_deps.out 2>&1

DEPS_RESULT=$(head -1 /tmp/test_deps.out)
test_result "Python dependencies" "$DEPS_RESULT" "dependencies_ok"

# Test 4: Service startup
echo -e "${BLUE}🚀 Testing service startup...${NC}"
if [ -f "scripts/atlas_service.sh" ]; then
    # Stop any existing services
    ./scripts/atlas_service.sh stop >/dev/null 2>&1 || true
    sleep 2
    
    # Start service
    ./scripts/atlas_service.sh start >/dev/null 2>&1
    sleep 5
    
    # Check if service is running
    if ./scripts/atlas_service.sh status | grep -q "running"; then
        test_result "Service startup" "service_running" "service_running"
    else
        test_result "Service startup" "service_failed" "service_running"
    fi
else
    test_result "Service startup" "no_service_script" "service_running"
fi

# Test 5: API connectivity
echo -e "${BLUE}🌐 Testing API connectivity...${NC}"
if command -v curl >/dev/null 2>&1; then
    # Wait for API to be ready
    sleep 10
    
    if curl -s -f http://localhost:8000/health >/dev/null 2>&1; then
        test_result "API connectivity" "api_responding" "api_responding"
    else
        test_result "API connectivity" "api_failed" "api_responding"
    fi
else
    echo -e "${YELLOW}⚠️ curl not found, skipping API test${NC}"
fi

# Test 6: Cognitive API endpoints
echo -e "${BLUE}🧠 Testing cognitive endpoints...${NC}"
if command -v curl >/dev/null 2>&1; then
    COGNITIVE_TESTS=0
    COGNITIVE_PASSED=0
    
    # Test surface endpoint
    if curl -s http://localhost:8000/api/v1/cognitive/surface | grep -q '\['; then
        ((COGNITIVE_PASSED++))
    fi
    ((COGNITIVE_TESTS++))
    
    # Test temporal endpoint  
    if curl -s http://localhost:8000/api/v1/cognitive/temporal | grep -q '\['; then
        ((COGNITIVE_PASSED++))
    fi
    ((COGNITIVE_TESTS++))
    
    # Test patterns endpoint
    if curl -s http://localhost:8000/api/v1/cognitive/patterns | grep -q '\['; then
        ((COGNITIVE_PASSED++))
    fi
    ((COGNITIVE_TESTS++))
    
    if [ "$COGNITIVE_PASSED" -ge 2 ]; then
        test_result "Cognitive API endpoints" "cognitive_working" "cognitive_working"
    else
        test_result "Cognitive API endpoints" "cognitive_failed" "cognitive_working"
    fi
else
    echo -e "${YELLOW}⚠️ curl not found, skipping cognitive API test${NC}"
fi

# Test 7: Worker API
echo -e "${BLUE}👷 Testing worker API...${NC}"
if command -v curl >/dev/null 2>&1; then
    if curl -s http://localhost:8000/api/v1/worker/status | grep -q 'workers'; then
        test_result "Worker API" "worker_api_ok" "worker_api_ok"
    else
        test_result "Worker API" "worker_api_failed" "worker_api_ok"
    fi
fi

# Test 8: File structure
echo -e "${BLUE}📁 Testing file structure...${NC}"
REQUIRED_DIRS=("helpers" "api" "logs" "inputs" "output")
DIRS_OK=0

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        ((DIRS_OK++))
    fi
done

if [ "$DIRS_OK" -eq ${#REQUIRED_DIRS[@]} ]; then
    test_result "File structure" "directories_ok" "directories_ok"
else
    test_result "File structure" "missing_directories" "directories_ok"
fi

# Test 9: Process management
echo -e "${BLUE}⚙️ Testing process management...${NC}"
ATLAS_PROCESSES=$(ps aux | grep atlas | grep -v grep | wc -l)

if [ "$ATLAS_PROCESSES" -ge 1 ] && [ "$ATLAS_PROCESSES" -le 3 ]; then
    test_result "Process management" "processes_ok" "processes_ok"
else
    test_result "Process management" "process_leak" "processes_ok"
fi

# Final results
echo ""
echo -e "${BLUE}📊 Test Results Summary${NC}"
echo "======================================="
echo -e "✅ Passed: ${GREEN}$PASSED${NC}"
echo -e "❌ Failed: ${RED}$FAILED${NC}"
echo -e "Total: $((PASSED + FAILED))"

if [ "$FAILED" -eq 0 ]; then
    echo ""
    echo -e "${GREEN}🎉 ALL TESTS PASSED! Atlas is ready for use.${NC}"
    exit 0
else
    echo ""
    echo -e "${RED}⚠️ Some tests failed. Check the output above for details.${NC}"
    echo -e "${YELLOW}💡 This may be expected on fresh systems missing optional dependencies.${NC}"
    exit 1
fi