#!/bin/bash

# Atlas Production Data Integrity Checker
# This script verifies the integrity and consistency of data in the Atlas production environment

set -e  # Exit on any error

echo "Starting Atlas Production Data Integrity Check..."

# Configuration
INTEGRITY_LOG="/home/ubuntu/dev/atlas/logs/data_integrity.log"
INTEGRITY_REPORT_DIR="/home/ubuntu/dev/atlas/data/integrity_reports"
DATABASE_NAME="atlas"
DATABASE_USER="atlas_user"

# Create logs and reports directories if they don't exist
mkdir -p "$(dirname $INTEGRITY_LOG)"
mkdir -p "$INTEGRITY_REPORT_DIR"

# Function to log messages
log_message() {
    echo "$(date): $1" >> $INTEGRITY_LOG
    echo "$1"
}

# Function to check database connectivity
check_database_connectivity() {
    log_message "Checking database connectivity"
    
    echo "Checking Database Connectivity..."
    echo "=============================="
    
    # Check if PostgreSQL is running
    if ! systemctl is-active --quiet postgresql; then
        echo "❌ PostgreSQL is not running"
        log_message "PostgreSQL is not running"
        return 1
    fi
    
    # Check database connectivity
    if sudo -u postgres pg_isready -U $DATABASE_USER -d $DATABASE_NAME > /dev/null 2>&1; then
        echo "✅ Database is accessible"
        log_message "Database is accessible"
        return 0
    else
        echo "❌ Cannot connect to database"
        log_message "Cannot connect to database"
        return 1
    fi
}

# Function to check database schema integrity
check_database_schema() {
    log_message "Checking database schema integrity"
    
    echo ""
    echo "Checking Database Schema Integrity..."
    echo "=================================="
    
    local schema_report="$INTEGRITY_REPORT_DIR/schema_check_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create schema report header
    echo "Atlas Database Schema Integrity Check" > "$schema_report"
    echo "Generated: $(date)" >> "$schema_report"
    echo "===================================" >> "$schema_report"
    echo "" >> "$schema_report"
    
    # Check if required tables exist
    local required_tables=("articles" "podcasts" "youtube_videos" "metadata")
    local missing_tables=()
    
    for table in "${required_tables[@]}"; do
        if sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '$table');" 2>/dev/null | grep -q "t"; then
            echo "✅ Table '$table' exists" >> "$schema_report"
        else
            echo "❌ Table '$table' is missing" >> "$schema_report"
            missing_tables+=("$table")
        fi
    done
    
    echo "" >> "$schema_report"
    
    # Check table row counts
    echo "Table Row Counts:" >> "$schema_report"
    echo "----------------" >> "$schema_report"
    for table in "${required_tables[@]}"; do
        if sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '$table');" 2>/dev/null | grep -q "t"; then
            local row_count=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM $table;" 2>/dev/null || echo "0")
            echo "$table: $row_count rows" >> "$schema_report"
        fi
    done
    
    # Report results
    if [ ${#missing_tables[@]} -eq 0 ]; then
        echo "✅ All required tables exist"
    else
        echo "❌ Missing tables: ${missing_tables[*]}"
        log_message "MISSING TABLES: ${missing_tables[*]}"
    fi
    
    echo "📋 Schema check report saved to: $schema_report"
    log_message "Schema check completed: $schema_report"
}

# Function to verify data consistency
verify_data_consistency() {
    log_message "Verifying data consistency"
    
    echo ""
    echo "Verifying Data Consistency..."
    echo "=========================="
    
    local consistency_report="$INTEGRITY_REPORT_DIR/consistency_check_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create consistency report header
    echo "Atlas Data Consistency Check" > "$consistency_report"
    echo "Generated: $(date)" >> "$consistency_report"
    echo "===========================" >> "$consistency_report"
    echo "" >> "$consistency_report"
    
    # Check for orphaned records
    echo "Checking for Orphaned Records:" >> "$consistency_report"
    echo "----------------------------" >> "$consistency_report"
    
    # Check for articles with missing metadata
    local orphaned_articles=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM articles WHERE id NOT IN (SELECT article_id FROM metadata WHERE article_id IS NOT NULL);" 2>/dev/null || echo "0")
    echo "Articles with missing metadata: $orphaned_articles" >> "$consistency_report"
    
    # Check for podcasts with missing metadata
    local orphaned_podcasts=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM podcasts WHERE id NOT IN (SELECT podcast_id FROM metadata WHERE podcast_id IS NOT NULL);" 2>/dev/null || echo "0")
    echo "Podcasts with missing metadata: $orphaned_podcasts" >> "$consistency_report"
    
    # Check for YouTube videos with missing metadata
    local orphaned_youtube=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM youtube_videos WHERE id NOT IN (SELECT youtube_id FROM metadata WHERE youtube_id IS NOT NULL);" 2>/dev/null || echo "0")
    echo "YouTube videos with missing metadata: $orphaned_youtube" >> "$consistency_report"
    
    echo "" >> "$consistency_report"
    
    # Check for duplicate URLs
    echo "Checking for Duplicate URLs:" >> "$consistency_report"
    echo "--------------------------" >> "$consistency_report"
    
    # Check for duplicate article URLs
    local duplicate_articles=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM (SELECT url FROM articles GROUP BY url HAVING COUNT(*) > 1) AS duplicates;" 2>/dev/null || echo "0")
    echo "Duplicate article URLs: $duplicate_articles" >> "$consistency_report"
    
    # Check for duplicate podcast URLs
    local duplicate_podcasts=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM (SELECT url FROM podcasts GROUP BY url HAVING COUNT(*) > 1) AS duplicates;" 2>/dev/null || echo "0")
    echo "Duplicate podcast URLs: $duplicate_podcasts" >> "$consistency_report"
    
    # Check for duplicate YouTube URLs
    local duplicate_youtube=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM (SELECT url FROM youtube_videos GROUP BY url HAVING COUNT(*) > 1) AS duplicates;" 2>/dev/null || echo "0")
    echo "Duplicate YouTube URLs: $duplicate_youtube" >> "$consistency_report"
    
    # Report results
    local orphaned_total=$((orphaned_articles + orphaned_podcasts + orphaned_youtube))
    local duplicates_total=$((duplicate_articles + duplicate_podcasts + duplicate_youtube))
    
    if [ $orphaned_total -eq 0 ]; then
        echo "✅ No orphaned records found"
    else
        echo "⚠️ Orphaned records found: $orphaned_total"
        log_message "ORPHANED RECORDS FOUND: $orphaned_total"
    fi
    
    if [ $duplicates_total -eq 0 ]; then
        echo "✅ No duplicate URLs found"
    else
        echo "⚠️ Duplicate URLs found: $duplicates_total"
        log_message "DUPLICATE URLS FOUND: $duplicates_total"
    fi
    
    echo "📋 Consistency check report saved to: $consistency_report"
    log_message "Consistency check completed: $consistency_report"
}

# Function to validate content files
validate_content_files() {
    log_message "Validating content files"
    
    echo ""
    echo "Validating Content Files..."
    echo "========================"
    
    local file_validation_report="$INTEGRITY_REPORT_DIR/file_validation_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create validation report header
    echo "Atlas Content File Validation" > "$file_validation_report"
    echo "Generated: $(date)" >> "$file_validation_report"
    echo "============================" >> "$file_validation_report"
    echo "" >> "$file_validation_report"
    
    # Check content directories
    local content_dirs=(
        "/home/ubuntu/dev/atlas/outputs/articles"
        "/home/ubuntu/dev/atlas/outputs/podcasts"
        "/home/ubuntu/dev/atlas/outputs/youtube"
    )
    
    local missing_dirs=()
    local dir_stats=()
    
    for dir in "${content_dirs[@]}"; do
        if [ -d "$dir" ]; then
            echo "✅ Directory exists: $dir" >> "$file_validation_report"
            
            # Count files in directory
            local file_count=$(find "$dir" -type f 2>/dev/null | wc -l)
            local dir_size=$(du -sh "$dir" 2>/dev/null | cut -f1)
            echo "  Files: $file_count, Size: $dir_size" >> "$file_validation_report"
            dir_stats+=("$dir:$file_count:$dir_size")
        else
            echo "❌ Directory missing: $dir" >> "$file_validation_report"
            missing_dirs+=("$dir")
        fi
    done
    
    echo "" >> "$file_validation_report"
    
    # Check for broken symlinks
    echo "Checking for Broken Symlinks:" >> "$file_validation_report"
    echo "----------------------------" >> "$file_validation_report"
    
    local broken_links=0
    for dir in "${content_dirs[@]}"; do
        if [ -d "$dir" ]; then
            local dir_broken=$(find "$dir" -type l -exec test ! -e {} \; -print 2>/dev/null | wc -l)
            if [ $dir_broken -gt 0 ]; then
                echo "  Broken symlinks in $dir: $dir_broken" >> "$file_validation_report"
                broken_links=$((broken_links + dir_broken))
            fi
        fi
    done
    
    if [ $broken_links -eq 0 ]; then
        echo "  No broken symlinks found" >> "$file_validation_report"
    fi
    
    # Report results
    if [ ${#missing_dirs[@]} -eq 0 ]; then
        echo "✅ All content directories exist"
    else
        echo "❌ Missing directories: ${missing_dirs[*]}"
        log_message "MISSING DIRECTORIES: ${missing_dirs[*]}"
    fi
    
    if [ $broken_links -eq 0 ]; then
        echo "✅ No broken symlinks found"
    else
        echo "⚠️ Broken symlinks found: $broken_links"
        log_message "BROKEN SYMLINKS FOUND: $broken_links"
    fi
    
    echo "📋 File validation report saved to: $file_validation_report"
    log_message "File validation completed: $file_validation_report"
}

# Function to check database constraints
check_database_constraints() {
    log_message "Checking database constraints"
    
    echo ""
    echo "Checking Database Constraints..."
    echo "============================="
    
    local constraint_report="$INTEGRITY_REPORT_DIR/constraint_check_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create constraint report header
    echo "Atlas Database Constraint Check" > "$constraint_report"
    echo "Generated: $(date)" >> "$constraint_report"
    echo "=============================" >> "$constraint_report"
    echo "" >> "$constraint_report"
    
    # Check for NOT NULL constraint violations
    echo "Checking NOT NULL Constraints:" >> "$constraint_report"
    echo "----------------------------" >> "$constraint_report"
    
    # Check articles table
    local articles_null_title=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM articles WHERE title IS NULL;" 2>/dev/null || echo "0")
    local articles_null_url=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM articles WHERE url IS NULL;" 2>/dev/null || echo "0")
    echo "Articles with NULL title: $articles_null_title" >> "$constraint_report"
    echo "Articles with NULL url: $articles_null_url" >> "$constraint_report"
    
    # Check podcasts table
    local podcasts_null_title=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM podcasts WHERE title IS NULL;" 2>/dev/null || echo "0")
    local podcasts_null_url=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM podcasts WHERE url IS NULL;" 2>/dev/null || echo "0")
    echo "Podcasts with NULL title: $podcasts_null_title" >> "$constraint_report"
    echo "Podcasts with NULL url: $podcasts_null_url" >> "$constraint_report"
    
    # Check YouTube videos table
    local youtube_null_title=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM youtube_videos WHERE title IS NULL;" 2>/dev/null || echo "0")
    local youtube_null_url=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM youtube_videos WHERE url IS NULL;" 2>/dev/null || echo "0")
    echo "YouTube videos with NULL title: $youtube_null_title" >> "$constraint_report"
    echo "YouTube videos with NULL url: $youtube_null_url" >> "$constraint_report"
    
    echo "" >> "$constraint_report"
    
    # Check for unique constraint violations
    echo "Checking Unique Constraints:" >> "$constraint_report"
    echo "--------------------------" >> "$constraint_report"
    
    # Check unique URLs in articles
    local articles_duplicate_urls=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM (SELECT url FROM articles WHERE url IS NOT NULL GROUP BY url HAVING COUNT(*) > 1) AS duplicates;" 2>/dev/null || echo "0")
    echo "Articles with duplicate URLs: $articles_duplicate_urls" >> "$constraint_report"
    
    # Check unique URLs in podcasts
    local podcasts_duplicate_urls=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM (SELECT url FROM podcasts WHERE url IS NOT NULL GROUP BY url HAVING COUNT(*) > 1) AS duplicates;" 2>/dev/null || echo "0")
    echo "Podcasts with duplicate URLs: $podcasts_duplicate_urls" >> "$constraint_report"
    
    # Check unique URLs in YouTube videos
    local youtube_duplicate_urls=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM (SELECT url FROM youtube_videos WHERE url IS NOT NULL GROUP BY url HAVING COUNT(*) > 1) AS duplicates;" 2>/dev/null || echo "0")
    echo "YouTube videos with duplicate URLs: $youtube_duplicate_urls" >> "$constraint_report"
    
    # Report results
    local null_total=$((articles_null_title + articles_null_url + podcasts_null_title + podcasts_null_url + youtube_null_title + youtube_null_url))
    local duplicate_total=$((articles_duplicate_urls + podcasts_duplicate_urls + youtube_duplicate_urls))
    
    if [ $null_total -eq 0 ]; then
        echo "✅ No NULL constraint violations found"
    else
        echo "⚠️ NULL constraint violations found: $null_total"
        log_message "NULL CONSTRAINT VIOLATIONS: $null_total"
    fi
    
    if [ $duplicate_total -eq 0 ]; then
        echo "✅ No unique constraint violations found"
    else
        echo "⚠️ Unique constraint violations found: $duplicate_total"
        log_message "UNIQUE CONSTRAINT VIOLATIONS: $duplicate_total"
    fi
    
    echo "📋 Constraint check report saved to: $constraint_report"
    log_message "Constraint check completed: $constraint_report"
}

# Function to generate data integrity summary
generate_integrity_summary() {
    log_message "Generating data integrity summary"
    
    echo ""
    echo "Generating Data Integrity Summary..."
    echo "================================="
    
    local summary_report="$INTEGRITY_REPORT_DIR/integrity_summary_$(date +%Y%m%d_%H%M%S).txt"
    
    # Create summary report header
    echo "Atlas Production Data Integrity Summary" > "$summary_report"
    echo "Generated: $(date)" >> "$summary_report"
    echo "=====================================" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add database information
    echo "Database Information:" >> "$summary_report"
    echo "-------------------" >> "$summary_report"
    echo "Database Name: $DATABASE_NAME" >> "$summary_report"
    echo "Database User: $DATABASE_USER" >> "$summary_report"
    if sudo -u postgres pg_isready -U $DATABASE_USER -d $DATABASE_NAME > /dev/null 2>&1; then
        echo "Status: ✅ Connected" >> "$summary_report"
    else
        echo "Status: ❌ Disconnected" >> "$summary_report"
    fi
    echo "" >> "$summary_report"
    
    # Add table statistics
    echo "Table Statistics:" >> "$summary_report"
    echo "---------------" >> "$summary_report"
    for table in "articles" "podcasts" "youtube_videos"; do
        if sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '$table');" 2>/dev/null | grep -q "t"; then
            local row_count=$(sudo -u postgres psql -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM $table;" 2>/dev/null || echo "0")
            echo "$table: $row_count rows" >> "$summary_report"
        else
            echo "$table: Table not found" >> "$summary_report"
        fi
    done
    echo "" >> "$summary_report"
    
    # Add integrity check results
    echo "Integrity Check Results:" >> "$summary_report"
    echo "----------------------" >> "$summary_report"
    
    # Count recent issues from reports
    local schema_issues=$(ls -t $INTEGRITY_REPORT_DIR/schema_check_*.txt 2>/dev/null | head -1 | xargs grep -c "❌" 2>/dev/null || echo "0")
    local consistency_issues=$(ls -t $INTEGRITY_REPORT_DIR/consistency_check_*.txt 2>/dev/null | head -1 | xargs grep -c "⚠️\|❌" 2>/dev/null || echo "0")
    local file_issues=$(ls -t $INTEGRITY_REPORT_DIR/file_validation_*.txt 2>/dev/null | head -1 | xargs grep -c "❌" 2>/dev/null || echo "0")
    local constraint_issues=$(ls -t $INTEGRITY_REPORT_DIR/constraint_check_*.txt 2>/dev/null | head -1 | xargs grep -c "⚠️\|❌" 2>/dev/null || echo "0")
    
    echo "Schema Issues: $schema_issues" >> "$summary_report"
    echo "Consistency Issues: $consistency_issues" >> "$summary_report"
    echo "File Validation Issues: $file_issues" >> "$summary_report"
    echo "Constraint Violations: $constraint_issues" >> "$summary_report"
    echo "" >> "$summary_report"
    
    # Add recommendations
    echo "Recommendations:" >> "$summary_report"
    echo "--------------" >> "$summary_report"
    if [ $((schema_issues + consistency_issues + file_issues + constraint_issues)) -gt 0 ]; then
        echo "• Review and fix identified data integrity issues" >> "$summary_report"
        echo "• Run data integrity checks regularly" >> "$summary_report"
        echo "• Implement automated data validation" >> "$summary_report"
    else
        echo "• ✅ All data integrity checks passed" >> "$summary_report"
        echo "• Continue regular monitoring" >> "$summary_report"
    fi
    
    echo "📋 Integrity summary report saved to: $summary_report"
    log_message "Integrity summary generated: $summary_report"
    
    # Display summary
    echo ""
    echo "Data Integrity Summary:"
    echo "  Schema Issues: $schema_issues"
    echo "  Consistency Issues: $consistency_issues"
    echo "  File Validation Issues: $file_issues"
    echo "  Constraint Violations: $constraint_issues"
    echo "Report saved to: $summary_report"
}

# Function to clean old integrity reports
clean_old_reports() {
    log_message "Cleaning old integrity reports"
    
    echo ""
    echo "Cleaning Old Integrity Reports..."
    echo "=============================="
    
    # Remove integrity reports older than 30 days
    find "$INTEGRITY_REPORT_DIR" -name "schema_check_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$INTEGRITY_REPORT_DIR" -name "consistency_check_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$INTEGRITY_REPORT_DIR" -name "file_validation_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$INTEGRITY_REPORT_DIR" -name "constraint_check_*.txt" -mtime +30 -delete 2>/dev/null || true
    find "$INTEGRITY_REPORT_DIR" -name "integrity_summary_*.txt" -mtime +30 -delete 2>/dev/null || true
    
    echo "✅ Old integrity reports cleaned"
    log_message "Old integrity reports cleaned"
}

# Main data integrity function
main() {
    log_message "=== Starting Atlas Data Integrity Check ==="
    
    # Check database connectivity first
    if ! check_database_connectivity; then
        echo "❌ Cannot proceed with data integrity check due to database connectivity issues"
        exit 1
    fi
    
    # Start time
    local start_time=$(date)
    log_message "Data integrity check started at: $start_time"
    
    # Handle different integrity operations
    case $1 in
        "schema")
            check_database_schema
            ;;
        "consistency")
            verify_data_consistency
            ;;
        "files")
            validate_content_files
            ;;
        "constraints")
            check_database_constraints
            ;;
        "summary")
            generate_integrity_summary
            ;;
        "clean")
            clean_old_reports
            ;;
        *)
            # Run comprehensive data integrity check
            check_database_schema
            verify_data_consistency
            validate_content_files
            check_database_constraints
            generate_integrity_summary
            clean_old_reports
            ;;
    esac
    
    # End time
    local end_time=$(date)
    local duration=$(echo $(date -d "$end_time" +%s) - $(date -d "$start_time" +%s) | bc)
    log_message "Data integrity check completed at: $end_time (Duration: ${duration}s)"
    
    log_message "=== Data Integrity Check Completed ==="
    
    echo ""
    echo "✅ Data integrity check complete!"
    echo "📋 Reports saved to: $INTEGRITY_REPORT_DIR"
    echo "📝 Log file: $INTEGRITY_LOG"
}

# Run main function
main "$@"