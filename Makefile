# Atlas Operations Makefile
# Provides single-command operations for Atlas transcript processing

.PHONY: status logs restart smoke install help

# Default target
help:
	@echo "Atlas Operations Commands:"
	@echo "  make status     - Show system status"
	@echo "  make logs       - Show recent logs"
	@echo "  make restart    - Restart all services"
	@echo "  make smoke      - Run smoke test"
	@echo "  make install    - Install systemd services"
	@echo "  make help       - Show this help"

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