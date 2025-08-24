### [1.1] Diagnose Document Content Extraction Failure
**Phase:** 1
**Status:** todo
**Depends On:** []

**Context**
- The `audit_atlas_reality.py` script revealed that 18,575 documents have no content. This task is to diagnose the root cause of this failure.

**Steps**
1. Read the code for the document processing pipeline, located in `run.py` and any related modules.
2. Identify the specific function responsible for content extraction from documents.
3. Add detailed logging to this function to trace its execution and identify the point of failure.
4. Run the document processing pipeline on a single, sample document that is known to be failing.
5. Analyze the logs to determine the exact cause of the failure.

**Success Criteria**
- The root cause of the document content extraction failure is identified and documented.

**Failure/Triage**
- If the root cause of the failure cannot be identified after 4 hours of investigation: capture logs at `logs/document_extraction_diagnosis.log`, create follow-up task `FIX-1.1-document-extraction-diagnosis` with root cause and next steps.

**Artifacts**
- A new log file: `logs/document_extraction_diagnosis.log`

**Notes**
- This is the highest priority task.

### [1.2] Fix Document Content Extraction
**Phase:** 1
**Status:** blocked
**Depends On:** [1.1]

**Context**
- Now that the root cause of the document content extraction failure is known, this task is to fix it.

**Steps**
1. Based on the findings from Task 1.1, develop a fix for the content extraction logic.
2. Write a unit test to verify that the fix works as expected.
3. Run the unit test and ensure that it passes.

**Success Criteria**
- The unit test for the fix passes.

**Failure/Triage**
- If the unit test does not pass after 3 attempts: capture logs, create follow-up task `FIX-1.2-document-extraction-fix` with root cause and next steps.

**Artifacts**
- A new unit test file.

**Notes**
- The fix should be simple and well-documented.

### [1.3] Re-process Failed Documents
**Phase:** 1
**Status:** blocked
**Depends On:** [1.2]

**Context**
- Now that the document content extraction logic is fixed, this task is to re-process the 18,575 documents that previously failed.

**Steps**
1. Create a script to identify and re-process the 18,575 failed documents.
2. Run the script in a screen session to ensure it continues to run in the background.
3. Monitor the script's progress and ensure that it is running without errors.

**Success Criteria**
- The script successfully re-processes all 18,575 failed documents, and the `check_all_content.py` script shows that at least 90% of them now have content.

**Failure/Triage**
- If the script fails to re-process the documents, or the success rate is less than 90%: capture logs, create follow-up task `FIX-1.3-reprocess-failed-documents` with root cause and next steps.

**Artifacts**
- A new script: `scripts/reprocess_failed_documents.py`

**Notes**
- This task may take a long time to run.

### [1.4] Analyze Article Fetching Failures
**Phase:** 1
**Status:** todo
**Depends On:** []

**Context**
- The article success rate is only 50%. This task is to analyze the `retry_log` to identify the most common reasons for failure.

**Steps**
1. Read the `retry_log` file.
2. Write a script to parse the log file and identify the most common error messages and failure patterns.
3. Categorize the failures (e.g., paywalls, Cloudflare, 404s, etc.).

**Success Criteria**
- A report is generated that details the most common reasons for article fetching failures.

**Failure/Triage**
- If the script fails to parse the log file, or the report is not generated: create follow-up task `FIX-1.4-analyze-article-failures` with root cause and next steps.

**Artifacts**
- A new report file: `reports/article_fetching_failures.md`

**Notes**
- The report should be clear and easy to understand.

### [1.5] Enhance Article Fetching Pipeline
**Phase:** 1
**Status:** blocked
**Depends On:** [1.4]

**Context**
- Now that the most common reasons for article fetching failures are known, this task is to enhance the pipeline to address them.

**Steps**
1. Based on the findings from Task 1.4, implement new strategies for handling paywalls and other common issues.
2. Integrate a proxy rotation service to avoid being blocked.
3. Add a more sophisticated user-agent rotation mechanism.
4. Test the enhanced pipeline on a sample of 100 failed articles.

**Success Criteria**
- The success rate on the sample of 100 failed articles is at least 85%.

**Failure/Triage**
- If the success criteria is not met after 3 attempts: capture logs, create follow-up task `FIX-1.5-enhance-article-pipeline` with root cause and next steps.

**Artifacts**
- Updated code in the article fetching pipeline.

**Notes**
- This is a critical task for improving the reliability of the system.

### [1.6] Implement Instapaper Processing
**Phase:** 1
**Status:** blocked
**Depends On:** [1.5]

**Context**
- The Instapaper processing pipeline is currently missing.

**Steps**
1. Design and implement a pipeline to process Instapaper exports.
2. The pipeline should be able to parse the Instapaper CSV format, extract the article URLs, and process them using the enhanced article fetching pipeline.
3. Test the pipeline on a sample Instapaper export.

**Success Criteria**
- All articles from the sample Instapaper export are successfully processed and stored in the database.

**Failure/Triage**
- If the success criteria is not met after 2 attempts: capture logs, create follow-up task `FIX-1.6-implement-instapaper-processing` with root cause and next steps.

**Artifacts**
- A new script: `scripts/process_instapaper.py`

**Notes**
- The user will provide a sample Instapaper export file.

### [1.7] Create End-to-End Core Functionality Test Suite
**Phase:** 1
**Status:** blocked
**Depends On:** [1.3, 1.5, 1.6]

**Context**
- A comprehensive end-to-end test suite is needed to validate the core functionality.

**Steps**
1. Create a test suite that covers the entire lifecycle of an article, podcast, document, and Instapaper item, from ingestion to storage and retrieval.
2. The test suite should be automated and run as part of the CI/CD pipeline.

**Success Criteria**
- The test suite passes without any errors.

**Failure/Triage**
- If the test suite does not pass after 3 attempts: capture logs, create follow-up task `FIX-1.7-create-e2e-test-suite` with root cause and next steps.

**Artifacts**
- A new test suite file: `tests/test_e2e.py`

**Notes**
- This test suite will be a critical part of the project's quality gates.

## Phase 2: Comprehensive Testing & Hardening

(High-level tasks to be detailed later)

## Phase 3: Documentation, Refactoring & Usability

(High-level tasks to be detailed later)

## Phase 4: Final Review & Production Readiness

(High-level tasks to be detailed later)
