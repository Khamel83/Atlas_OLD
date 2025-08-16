#!/bin/bash
# Atlas Background Service Starter
# Use this to start/stop/restart the unified background service

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ATLAS_DIR="$(dirname "$SCRIPT_DIR")"
SERVICE_SCRIPT="$SCRIPT_DIR/atlas_background_service.py"
PID_FILE="$ATLAS_DIR/logs/atlas_service.pid"
LOG_FILE="$ATLAS_DIR/logs/atlas_background_service.log"

case "$1" in
    start)
        if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
            echo "Atlas service already running (PID: $(cat $PID_FILE))"
        else
            echo "Starting Atlas background service..."
            mkdir -p "$ATLAS_DIR/logs"
            nohup python3 "$SERVICE_SCRIPT" > "$LOG_FILE" 2>&1 &
            echo $! > "$PID_FILE"
            echo "Atlas service started (PID: $!)"
            echo "Monitor with: tail -f $LOG_FILE"
        fi
        ;;
    stop)
        if [ -f "$PID_FILE" ]; then
            PID=$(cat "$PID_FILE")
            if kill -0 "$PID" 2>/dev/null; then
                echo "Stopping Atlas service (PID: $PID)..."
                kill "$PID"
                rm -f "$PID_FILE"
                echo "Atlas service stopped"
            else
                echo "Atlas service not running"
                rm -f "$PID_FILE"
            fi
        else
            echo "Atlas service not running (no PID file)"
        fi
        ;;
    restart)
        $0 stop
        sleep 2
        $0 start
        ;;
    status)
        if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
            echo "Atlas service running (PID: $(cat $PID_FILE))"
            echo "Log: tail -f $LOG_FILE"
        else
            echo "Atlas service not running"
        fi
        ;;
    logs)
        tail -f "$LOG_FILE"
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status|logs}"
        echo ""
        echo "Commands:"
        echo "  start   - Start Atlas background service"
        echo "  stop    - Stop Atlas background service" 
        echo "  restart - Restart Atlas background service"
        echo "  status  - Check service status"
        echo "  logs    - Follow service logs"
        exit 1
        ;;
esac