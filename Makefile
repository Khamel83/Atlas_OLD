# Atlas Operations Makefile
# Provides single-command operations for Atlas transcript processing

.PHONY: status logs restart smoke install test-watchdog test-restart-policy test-resource-limits help

# Default target
help:
	@echo "Atlas Operations Commands:"
	@echo "  make status              - Show system status"
	@echo "  make logs                - Show recent logs"
	@echo "  make restart             - Restart all services"
	@echo "  make smoke               - Run smoke test"
	@echo "  make install             - Install systemd services"
	@echo "  make test-watchdog       - Test SystemD watchdog functionality"
	@echo "  make test-restart-policy - Test auto-restart on process kill"
	@echo "  make test-resource-limits- Show resource limits and usage"
	@echo "  make help                - Show this help"

# Show system status
status:
	@echo "🎯 Atlas System Status"
	@echo "======================"
	@echo "📍 Database Path: $$(bash scripts/db_path.sh)"
	@python3 scripts/db_introspect.py
	@echo ""
	@echo "📊 Processing Statistics:"
	@python3 atlas_status.py
	@echo ""
	@echo "🔧 Service Status:"
	@systemctl --no-pager status atlas.service atlas-watchdog.timer 2>/dev/null || echo "Services not installed"

# Show recent logs
logs:
	@echo "📋 Recent Atlas Logs"
	@echo "===================="
	@echo "🔧 Atlas Service:"
	@tail -20 logs/atlas_service.log 2>/dev/null || echo "No atlas service log"
	@echo ""
	@echo "📝 Watchdog:"
	@journalctl -u atlas-watchdog --no-pager -n 10 2>/dev/null || echo "No watchdog logs"
	@echo ""
	@echo "🔍 Discovery:"
	@journalctl -u atlas-discovery --no-pager -n 10 2>/dev/null || echo "No discovery logs"

# Restart all services
restart:
	@echo "🔄 Restarting Atlas Services"
	@echo "============================="
	@sudo systemctl restart atlas.service 2>/dev/null || echo "⚠️ atlas.service not found"
	@sudo systemctl restart atlas-watchdog.timer 2>/dev/null || echo "⚠️ atlas-watchdog.timer not found"
	@sudo systemctl restart atlas-discovery.timer 2>/dev/null || echo "⚠️ atlas-discovery.timer not found"
	@echo "✅ Restart commands completed"

# Run smoke test
smoke:
	@echo "🧪 Atlas Smoke Test"
	@echo "==================="
	@echo "📊 Database health:"
	@python3 scripts/db_introspect.py
	@echo ""
	@echo "🎯 Processing test:"
	@python3 scripts/fixed_transcript_worker.py --limit 1
	@echo ""
	@echo "📈 Updated status:"
	@python3 atlas_status.py

# Install systemd services
install:
	@echo "⚙️ Installing Atlas systemd services"
	@echo "===================================="
	@sudo cp systemd/*.service systemd/*.timer /etc/systemd/system/
	@sudo systemctl daemon-reload
	@echo "✅ Services copied and daemon reloaded"
	@echo ""
	@echo "🚀 Enable services with:"
	@echo "  sudo systemctl enable --now atlas-watchdog.timer"
	@echo "  sudo systemctl enable --now atlas-discovery.timer"
	@echo "  sudo systemctl enable --now atlas-transcribe@1"

# Development helpers
dev-status:
	@python3 atlas_status.py --detailed

dev-logs:
	@tail -f logs/atlas_service.log

dev-test-worker:
	@python3 scripts/fixed_transcript_worker.py --limit 2

dev-test-watchdog:
	@python3 maintenance/enhanced_progress_watchdog.py

dev-test-notify:
	@python3 scripts/notify.py --test

# SystemD Watchdog Testing
test-watchdog:
	@echo "🔍 Testing SystemD Watchdog"
	@echo "============================"
	@sudo systemctl status atlas.service
	@echo ""
	@echo "📋 Recent watchdog logs:"
	@journalctl -u atlas.service -f --since "5 minutes ago" | grep -i watchdog | head -5
	@echo ""
	@echo "🔧 Service resource limits:"
	@systemctl show atlas.service | grep -E "(Memory|CPU|Limit)"

test-restart-policy:
	@echo "🚨 Testing Auto-Restart Policy"
	@echo "=============================="
	@echo "Killing Atlas service manager process..."
	@sudo kill -9 $$(pgrep -f atlas_service_manager) || echo "Process not found"
	@echo "Waiting 35 seconds for auto-restart..."
	@sleep 35
	@echo "Checking service status:"
	@systemctl is-active atlas.service

test-resource-limits:
	@echo "📊 Testing Resource Limits"
	@echo "=========================="
	@systemctl show atlas.service | grep -E "(Memory|CPU|Limit)" | sort
	@echo ""
	@echo "Current usage:"
	@ps aux | grep atlas_service_manager | grep -v grep || echo "Service not running"