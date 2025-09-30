# Atlas Ingestion Testing Framework

Comprehensive testing framework for validating all Atlas ingestion capabilities, transcription quality, search effectiveness, and system performance.

## Quick Start

### 1. Run Complete Testing Suite
```bash
python testing/unified_testing_dashboard.py
```
This provides a menu-driven interface for all testing options.

### 2. Test Your Podcast Data
```bash
python testing/podcast_transcription_test.py
```
Uses your existing `inputs/podcasts.opml` to test transcription models.

### 3. Validate Search Quality
```bash
python testing/search_quality_analyzer.py
```
Determines how transcription accuracy affects search results.

## Testing Modules

### 🎯 Unified Dashboard (`unified_testing_dashboard.py`)
**Central command center for all testing**
- Orchestrates all test modules
- Provides comprehensive reporting
- Tracks testing history and trends
- Menu-driven interface for easy use

**Test Modes:**
- **Full Suite**: Complete comprehensive testing
- **Quick Test**: Fast subset for rapid feedback
- **Transcription Focus**: Transcription-specific validation
- **Status Check**: Current system status
- **Trends**: Historical performance analysis

### 🎤 Enhanced Transcription (`../helpers/enhanced_transcription.py`)
**Multi-provider transcription testing**
- **Local Whisper**: tiny, small, medium, large, turbo models
- **API Services**: OpenAI, OpenRouter, AssemblyAI, Deepgram
- **Performance Comparison**: Speed vs accuracy analysis
- **Quality Metrics**: Word error rate, similarity scoring

### 📊 Ingestion Prototype (`ingestion_prototype.py`)
**Core ingestion pipeline testing**
- All transcription models with performance metrics
- Fidelity comparison against ground truth
- Search quality with different accuracies
- Resource usage and optimization analysis

### 🌐 Comprehensive Ingestion (`comprehensive_ingestion_tests.py`)
**All ingestion methods validation**
- **API Testing**: Instapaper, YouTube, RSS feeds
- **Local Files**: Documents, audio, video
- **Batch Processing**: OPML, URL lists, directories
- **Error Handling**: Network timeouts, corrupted files, missing credentials

### 📻 Podcast Transcription (`podcast_transcription_test.py`)
**Real-world podcast testing**
- Uses your existing OPML data
- Tests multiple episodes per feed
- Compares transcription models on actual content
- Provides speed vs accuracy recommendations

### 🔍 Search Quality Analyzer (`search_quality_analyzer.py`)
**Search effectiveness validation**
- Tests queries across transcription quality levels
- Determines minimum acceptable accuracy
- Provides search optimization recommendations
- Simulates transcription errors for analysis

### ⚡ Performance Benchmarker (`performance_benchmarker.py`)
**System performance analysis**
- CPU, memory, disk usage monitoring
- Concurrent operation testing
- Scalability analysis
- Bottleneck identification and optimization

### 🎯 Ground Truth Setup (`ground_truth_setup.py`)
**Test data preparation**
- Downloads samples with known transcripts
- Creates synthetic test content
- Validates test data quality
- Provides baseline for accuracy testing

## Test Results

### Output Locations
- **Dashboard Results**: `testing/dashboard/results/`
- **Individual Test Logs**: `testing/*/logs/`
- **Session History**: `testing/dashboard/test_history.json`
- **Performance Data**: `testing/performance/`

### Report Format
Each test produces comprehensive JSON reports with:
- **Performance Metrics**: Speed, accuracy, resource usage
- **Comparison Data**: Model vs model analysis
- **Recommendations**: Optimization suggestions
- **Error Analysis**: Failure patterns and handling
- **Trend Data**: Historical performance tracking

## Configuration

### Required Dependencies
```bash
pip install psutil  # For system monitoring
```

### Optional API Keys
Add to environment or config for enhanced testing:
```bash
export OPENROUTER_API_KEY="your_key_here"
export OPENAI_API_KEY="your_key_here"
export ASSEMBLYAI_API_KEY="your_key_here"
export DEEPGRAM_API_KEY="your_key_here"
```

### Test Configuration
Configure in your main config file:
```json
{
  "run_transcription": true,
  "transcription_model": "small",
  "test_data_directory": "test_data",
  "max_test_file_size_mb": 50
}
```

## Understanding Results

### Transcription Performance
- **Words per second**: Processing speed metric
- **Real-time factor**: Ratio of processing time to audio duration
- **Memory usage**: Peak memory consumption
- **Success rate**: Reliability across different content

### Search Quality Metrics
- **Success rate**: Percentage of queries returning relevant results
- **Relevance score**: Quality of top search results
- **Quality degradation**: Impact of transcription errors on search
- **Threshold analysis**: Minimum acceptable transcription quality

### Performance Benchmarks
- **Throughput**: Items/MB processed per second
- **Resource efficiency**: CPU/memory usage patterns
- **Scalability**: Performance under concurrent load
- **Optimization opportunities**: Specific improvement recommendations

## Common Use Cases

### 1. Pre-Production Validation
```bash
python testing/unified_testing_dashboard.py
# Select "1" for full test suite
```
Comprehensive validation before deploying to production.

### 2. Model Selection
```bash
python testing/podcast_transcription_test.py
```
Determine optimal transcription model for your content type.

### 3. Performance Optimization
```bash
python testing/performance_benchmarker.py
```
Identify system bottlenecks and optimization opportunities.

### 4. Search Quality Assessment
```bash
python testing/search_quality_analyzer.py
```
Validate search effectiveness and determine quality requirements.

### 5. Regular Health Checks
```bash
python testing/unified_testing_dashboard.py
# Select "2" for quick test
```
Fast validation for ongoing system health monitoring.

## Troubleshooting

### Common Issues

**No audio files found**
- Ensure test data exists in expected locations
- Run ground truth setup: `python testing/ground_truth_setup.py`

**Transcription failures**
- Check Whisper installation: `whisper --help`
- Verify audio file formats and accessibility
- Check system resources and permissions

**API errors**
- Validate API keys and network connectivity
- Check API rate limits and quotas
- Review error logs for specific failure details

**Performance issues**
- Monitor system resources during testing
- Reduce concurrent operations if needed
- Consider testing with smaller datasets first

### Debug Mode
Add `--debug` flag or set log level to DEBUG for detailed output:
```bash
python testing/unified_testing_dashboard.py --debug
```

### Log Analysis
Check detailed logs in:
- `testing/dashboard/dashboard.log`
- `testing/*/logs/` for module-specific logs
- System logs for resource and permission issues

## Integration

### With Existing Atlas System
- Uses existing configuration management
- Leverages current logging infrastructure
- Compatible with existing data structures
- Integrates with current error handling

### With CI/CD Pipelines
```bash
# Add to your CI pipeline
python testing/unified_testing_dashboard.py --mode=quick --output=json
```

### With Monitoring Systems
- JSON output format for easy parsing
- Historical data tracking for trend analysis
- Performance metrics for alerting
- Health check endpoints for monitoring

## Best Practices

1. **Start with Quick Test**: Get rapid feedback before comprehensive testing
2. **Use Your Real Data**: Test with actual OPML and content for realistic results
3. **Monitor Resources**: Watch system usage during intensive testing
4. **Regular Validation**: Set up periodic testing to catch regressions
5. **Document Results**: Save and compare test results over time
6. **Optimize Iteratively**: Use performance recommendations for continuous improvement

## Next Steps

1. Run initial comprehensive test suite
2. Review results and implement critical fixes
3. Configure optimal settings based on performance analysis
4. Set up regular monitoring for ongoing validation
5. Document your specific configuration and results

This framework provides everything needed to validate and optimize your Atlas ingestion pipeline for production use.