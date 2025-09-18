# Atlas Operations Guide

This guide covers operational aspects of running Atlas in production environments, including monitoring, deployment, and maintenance procedures.

## Table of Contents

- [System Architecture](#system-architecture)
- [Service Management](#service-management)
- [Monitoring and Observability](#monitoring-and-observability)
- [Deployment Procedures](#deployment-procedures)
- [Backup and Recovery](#backup-and-recovery)
- [Troubleshooting](#troubleshooting)
- [Operational Tools](#operational-tools)

## System Architecture

Atlas consists of several interconnected services that work together to provide reliable content ingestion and processing:

### Core Services

1. **atlas-api** (`api.py`)
   - FastAPI-based REST API
   - Content ingestion endpoints
   - Web interface serving
   - Health monitoring endpoints

2. **atlas-scheduler** (`scheduler.py`)
   - Periodic task scheduling
   - Content processing workflows
   - Background job management

3. **atlas-worker** (`worker.py`)
   - Background processing workers
   - Content analysis and extraction
   - External API integrations

4. **atlas-monitor** (`monitoring_dashboard_service.py`)
   - Real-time monitoring dashboard
   - Metrics collection and visualization
   - WebSocket-based live updates

### Supporting Services

5. **atlas-observability** (`standalone_observability.py`)
   - Dedicated observability service
   - Structured logging aggregation
   - System metrics collection
   - Alerting and notifications

### Data Flow

```
External Sources → Atlas API → Database → Workers → Processed Content
                    ↓
               Monitor ← Observability → Alerting
```

## Service Management

### Starting and Stopping Services

All services are managed by systemd and can be controlled using the provided operational tools:

```bash
# Using atlas_ops tool
python3 tools/atlas_ops.py start atlas-api
python3 tools/atlas_ops.py stop atlas-api
python3 tools/atlas_ops.py restart atlas-api
python3 tools/atlas_ops.py status atlas-api

# Using systemctl directly
sudo systemctl start atlas-api
sudo systemctl stop atlas-api
sudo systemctl restart atlas-api
sudo systemctl status atlas-api
```

### Service Dependencies

Services have specific dependencies that must be respected:

```
atlas-monitor (monitoring dashboard)
    ↓
atlas-observability (metrics/logging)
    ↓
atlas-api (main application)
    ↓
atlas-scheduler (task scheduling)
    ↓
atlas-worker (background processing)
```

### Health Checks

Each service provides health check endpoints:

- **API Service**: `http://localhost:7444/health`
- **Monitoring Dashboard**: `http://localhost:7445/health`
- **Observability Service**: `http://localhost:7446/health`

## Monitoring and Observability

### Real-time Monitoring

The monitoring dashboard provides real-time insights into system operations:

- **Access URL**: `http://localhost:7445`
- **WebSocket Updates**: Live metrics streaming
- **Health Status**: Service availability and performance
- **Resource Usage**: CPU, memory, disk, network metrics

### Metrics Collection

System metrics are collected and stored for analysis:

- **System Metrics**: CPU, memory, disk, network usage
- **Application Metrics**: Request rates, response times, error rates
- **Database Metrics**: Query performance, connection counts, lock contention
- **Business Metrics**: Content processed, success rates, backlog status

### Logging

Structured logging with JSON formatting for better analysis:

```bash
# View live logs
journalctl -u atlas-api -f

# View logs with filtering
journalctl -u atlas-api --since "1 hour ago" | grep ERROR

# Export logs for analysis
journalctl -u atlas-api --since "1 day ago" > atlas-api.log
```

### Alerting

The system monitors various conditions and can send alerts:

- **Service Availability**: Detects when services are down
- **Resource Usage**: Alerts on high CPU/memory/disk usage
- **Error Rates**: Monitors for increased error frequencies
- **Database Health**: Checks database connectivity and performance

Alert notifications can be sent via:
- Email (SMTP configuration required)
- Webhooks (for integration with external systems)
- Log entries (for monitoring system integration)

## Deployment Procedures

### Prerequisites

Before deployment, ensure:

1. **System Requirements**
   - Ubuntu 20.04+ or compatible Linux distribution
   - Python 3.9-3.12
   - Minimum 4GB RAM, 8GB recommended
   - 50GB disk space (expandable based on content volume)

2. **Dependencies**
   - System dependencies: `python3`, `python3-pip`, `sqlite3`
   - Python dependencies: Listed in `requirements.txt`
   - System services: `systemd`, `nginx` (optional for reverse proxy)

### Installation

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd atlas
   ```

2. **Install Dependencies**
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   cp config/development.env config/.env
   # Edit config/.env with your settings
   ```

4. **Setup Services**
   ```bash
   sudo cp systemd/* /etc/systemd/system/
   sudo systemctl daemon-reload
   ```

5. **Initialize Database**
   ```bash
   python3 core/database.py
   ```

### Deployment Strategies

#### Blue-Green Deployment

1. **Deploy New Version**
   ```bash
   python3 tools/deployment_manager.py deploy --version v2.0.0 --strategy blue-green
   ```

2. **Verify New Version**
   ```bash
   # Check health and performance
   curl http://localhost:7444/health
   ```

3. **Switch Traffic**
   ```bash
   python3 tools/deployment_manager.py switch-traffic --version v2.0.0
   ```

#### Rolling Deployment

```bash
python3 tools/deployment_manager.py deploy --version v2.0.0 --strategy rolling
```

### Configuration Management

Use the configuration CLI for managing settings:

```bash
# View current configuration
python3 tools/config_cli.py show

# Set configuration values
python3 tools/config_cli.py set API_PORT 8080

# Validate configuration
python3 tools/config_cli.py validate

# Export configuration
python3 tools/config_cli.py export --format yaml
```

## Backup and Recovery

### Database Backup

1. **Create Backup**
   ```bash
   python3 tools/atlas_ops.py backup
   ```

2. **Schedule Automatic Backups**
   ```bash
   # Edit systemd timer
   sudo systemctl edit atlas-backup.timer
   ```

### Configuration Backup

```bash
# Backup configuration files
tar -czf atlas-config-$(date +%Y%m%d).tar.gz config/

# Backup secrets (ensure proper security)
python3 tools/config_cli.py secret export --format env > atlas-secrets-$(date +%Y%m%d).env
```

### Recovery Procedures

1. **Database Recovery**
   ```bash
   python3 tools/atlas_ops.py restore --backup-file /path/to/backup.sql
   ```

2. **Configuration Recovery**
   ```bash
   # Restore configuration files
   tar -xzf atlas-config-YYYYMMDD.tar.gz

   # Restore secrets
   python3 tools/config_cli.py secret import --file atlas-secrets-YYYYMMDD.env
   ```

## Troubleshooting

### Common Issues

#### Service Won't Start

1. **Check Service Status**
   ```bash
   sudo systemctl status atlas-api
   ```

2. **View Logs**
   ```bash
   journalctl -u atlas-api -n 50
   ```

3. **Check Configuration**
   ```bash
   python3 tools/config_cli.py validate
   ```

#### High Resource Usage

1. **Monitor Resource Usage**
   ```bash
   htop
   df -h
   ```

2. **Check Database Performance**
   ```bash
   python3 tools/atlas_ops.py check-database
   ```

3. **Adjust Configuration**
   ```bash
   python3 tools/config_cli.py set MAX_CONCURRENT_ARTICLES 3
   ```

#### API Connectivity Issues

1. **Check Service Status**
   ```bash
   curl http://localhost:7444/health
   ```

2. **Verify Network Configuration**
   ```bash
   netstat -tlnp | grep 7444
   ```

3. **Check Firewall Rules**
   ```bash
   sudo ufw status
   ```

### Performance Tuning

#### Database Optimization

1. **Enable WAL Mode**
   ```bash
   python3 tools/atlas_ops.py optimize-database
   ```

2. **Vacuum Database**
   ```bash
   python3 tools/atlas_ops.py vacuum-database
   ```

#### Application Tuning

Adjust these configuration parameters based on your system resources:

```bash
# Number of concurrent articles to process
python3 tools/config_cli.py set MAX_CONCURRENT_ARTICLES 5

# Rate limiting settings
python3 tools/config_cli.py set RATE_LIMIT_REQUESTS_PER_MINUTE 60

# Cache settings
python3 tools/config_cli.py set CACHE_TTL 300
```

## Operational Tools

### Atlas Operations Tool

Comprehensive system management:

```bash
python3 tools/atlas_ops.py <command> [options]

Commands:
  health-check          Check system health status
  service-status       Get status of all services
  start <service>      Start a service
  stop <service>       Stop a service
  restart <service>    Restart a service
  backup               Create database backup
  restore <file>       Restore from backup
  logs <service>       View service logs
  metrics              Show system metrics
```

### Deployment Manager

Manage deployments and versions:

```bash
python3 tools/deployment_manager.py <command> [options]

Commands:
  deploy <version>      Deploy new version
  rollback <version>    Rollback to previous version
  list-versions        List available versions
  cleanup              Clean up old versions
  health-check         Check deployment health
```

### Monitoring Agent

Continuous monitoring and alerting:

```bash
python3 tools/monitoring_agent.py <command> [options]

Commands:
  start                Start monitoring daemon
  stop                 Stop monitoring daemon
  status               Check monitoring status
  metrics              Show current metrics
  alerts               Show active alerts
  test-alert           Test alert configuration
```

### Configuration CLI

Manage configuration and secrets:

```bash
python3 tools/config_cli.py <command> [options]

Commands:
  show [key]           Show configuration values
  set <key> <value>    Set configuration value
  delete <key>         Delete configuration value
  validate             Validate configuration
  export [format]      Export configuration
  secret <command>     Manage secrets
```

## Security Considerations

### Secret Management

1. **Use Environment Variables**
   ```bash
   python3 tools/config_cli.py secret set API_KEY your_api_key
   ```

2. **Rotate Secrets Regularly**
   ```bash
   python3 tools/config_cli.py secret rotate API_KEY
   ```

3. **Audit Secret Access**
   ```bash
   python3 tools/config_cli.py secret audit
   ```

### Network Security

1. **Firewall Configuration**
   ```bash
   sudo ufw allow 7444/tcp  # API port
   sudo ufw allow 7445/tcp  # Monitoring port
   ```

2. **SSL/TLS Configuration**
   - Use reverse proxy (nginx) for SSL termination
   - Configure certificates for secure access

3. **API Security**
   - Use API keys for authentication
   - Implement rate limiting
   - Monitor for suspicious activity

## Maintenance Schedule

### Daily Tasks

- Monitor system health and performance
- Check error logs and alert conditions
- Verify backup completion
- Review resource usage trends

### Weekly Tasks

- Update software packages
- Clean up temporary files
- Review security logs
- Test backup and recovery procedures

### Monthly Tasks

- Archive old logs
- Performance tuning and optimization
- Security audit
- Capacity planning

## Performance Monitoring

### Key Metrics to Monitor

1. **System Health**
   - CPU usage (alert if > 80% for 5 minutes)
   - Memory usage (alert if > 85% for 5 minutes)
   - Disk usage (alert if > 90%)
   - Network latency (alert if > 100ms)

2. **Application Performance**
   - API response time (alert if > 2 seconds)
   - Error rate (alert if > 5%)
   - Database query time (alert if > 1 second)
   - Background job processing time

3. **Business Metrics**
   - Content ingestion rate
   - Processing success rate
   - Backlog size and trend
   - User activity metrics

### Dashboard Configuration

The monitoring dashboard can be customized to display relevant metrics:

```bash
# Edit dashboard configuration
python3 tools/config_cli.py set DASHBOARD_LAYOUT custom

# Add custom metrics
python3 tools/config_cli.py set CUSTOM_METRICS "metric1,metric2,metric3"
```

## Emergency Procedures

### Service Failure

1. **Immediate Actions**
   - Check service status: `sudo systemctl status atlas-api`
   - Review logs: `journalctl -u atlas-api -n 100`
   - Restart service: `sudo systemctl restart atlas-api`

2. **Escalation**
   - If service doesn't restart, check system resources
   - If resources are exhausted, stop non-essential services
   - If problem persists, initiate rollback procedure

### Data Corruption

1. **Identify Corruption**
   - Check database integrity: `python3 tools/atlas_ops.py check-database`
   - Review error logs for corruption indicators

2. **Recovery**
   - Restore from most recent backup
   - Verify data integrity
   - Monitor for recurrence

### Security Incident

1. **Containment**
   - Stop affected services
   - Isolate from network if necessary
   - Preserve logs for analysis

2. **Recovery**
   - Patch vulnerabilities
   - Restore from clean backup
   - Reset compromised credentials
   - Monitor for suspicious activity

## Support and Resources

### Getting Help

- **Documentation**: See `docs/` directory for detailed guides
- **Community**: Check project repositories for issues and discussions
- **Logs**: Review service logs for diagnostic information
- **Monitoring**: Use the monitoring dashboard for real-time insights

### Reporting Issues

When reporting issues, include:

1. System information (OS version, Python version)
2. Atlas version and configuration
3. Relevant log entries
4. Steps to reproduce the issue
5. Expected vs. actual behavior

### Contributing

To contribute to Atlas:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

---

*This guide is part of the Atlas documentation. For additional information, see other files in the `docs/` directory.*