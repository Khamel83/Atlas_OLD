#!/usr/bin/env python3
"""
Dashboard Server - Web interface for Atlas analytics
Provides a simple web server for viewing analytics and insights.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DashboardServer:
    """
    Simple dashboard server for Atlas analytics.
    
    Provides web interface for:
    - Analytics overview
    - Content insights
    - Consumption patterns
    - Trend analysis
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize DashboardServer with configuration."""
        self.config = config or {}
        self.host = self.config.get('dashboard_host', 'localhost')
        self.port = self.config.get('dashboard_port', 8080)
        self.static_dir = Path(self.config.get('static_dir', 'dashboard/static'))
        self.templates_dir = Path(self.config.get('templates_dir', 'dashboard/templates'))
        
        # Ensure directories exist
        self.static_dir.mkdir(parents=True, exist_ok=True)
        self.templates_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize analytics engine
        from helpers.analytics_engine import AnalyticsEngine
        self.analytics = AnalyticsEngine(config)
        
        self._create_default_templates()
    
    def _create_default_templates(self):
        """Create default HTML templates."""
        # Main dashboard template
        dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atlas Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { text-align: center; margin-bottom: 30px; }
        .card { background: white; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .metric { display: inline-block; margin: 10px 20px; text-align: center; }
        .metric-value { font-size: 2em; font-weight: bold; color: #2196F3; }
        .metric-label { color: #666; }
        .chart-placeholder { height: 200px; background: #f0f0f0; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #666; }
        .content-list { list-style: none; padding: 0; }
        .content-item { padding: 10px; border-bottom: 1px solid #eee; }
        .content-title { font-weight: bold; }
        .content-meta { color: #666; font-size: 0.9em; }
        .refresh-btn { background: #2196F3; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
        .refresh-btn:hover { background: #1976D2; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Atlas Personal Analytics Dashboard</h1>
            <p>Content consumption insights and analytics</p>
            <button class="refresh-btn" onclick="window.location.reload()">Refresh Data</button>
        </div>
        
        <div class="card">
            <h2>Overview (Last 30 Days)</h2>
            <div id="overview-metrics">
                <div class="metric">
                    <div class="metric-value" id="total-content">-</div>
                    <div class="metric-label">Total Content</div>
                </div>
                <div class="metric">
                    <div class="metric-value" id="total-words">-</div>
                    <div class="metric-label">Total Words</div>
                </div>
                <div class="metric">
                    <div class="metric-value" id="reading-hours">-</div>
                    <div class="metric-label">Reading Hours</div>
                </div>
                <div class="metric">
                    <div class="metric-value" id="total-events">-</div>
                    <div class="metric-label">Interactions</div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>Content Distribution</h2>
            <div class="chart-placeholder">Content type distribution chart would appear here</div>
            <div id="distribution-details"></div>
        </div>
        
        <div class="card">
            <h2>Top Content</h2>
            <h3>Most Engaged</h3>
            <ul class="content-list" id="most-engaged"></ul>
            
            <h3>Longest Content</h3>
            <ul class="content-list" id="longest-content"></ul>
        </div>
        
        <div class="card">
            <h2>Recommendations</h2>
            <ul id="recommendations"></ul>
        </div>
        
        <div class="card">
            <h2>System Information</h2>
            <p><strong>Generated:</strong> <span id="generated-time">-</span></p>
            <p><strong>Period:</strong> Last 30 days</p>
            <p><strong>Status:</strong> <span id="system-status">Active</span></p>
        </div>
    </div>
    
    <script>
        // Load analytics data
        fetch('/api/insights')
            .then(response => response.json())
            .then(data => {
                updateDashboard(data);
            })
            .catch(error => {
                console.error('Error loading analytics:', error);
                document.getElementById('system-status').textContent = 'Error loading data';
            });
        
        function updateDashboard(insights) {
            const overview = insights.overview || {};
            
            // Update overview metrics
            document.getElementById('total-content').textContent = overview.total_content || 0;
            document.getElementById('total-words').textContent = (overview.total_words || 0).toLocaleString();
            document.getElementById('reading-hours').textContent = overview.estimated_reading_hours || 0;
            document.getElementById('total-events').textContent = overview.total_events || 0;
            
            // Update content distribution
            const distribution = insights.content_distribution?.distribution || [];
            const distributionDiv = document.getElementById('distribution-details');
            distributionDiv.innerHTML = distribution.map(item => 
                `<p><strong>${item.type}:</strong> ${item.count} items (${item.percentage}%)</p>`
            ).join('');
            
            // Update top content
            const mostEngaged = insights.top_content?.most_engaged || [];
            const mostEngagedList = document.getElementById('most-engaged');
            mostEngagedList.innerHTML = mostEngaged.map(item =>
                `<li class="content-item">
                    <div class="content-title">${item.title}</div>
                    <div class="content-meta">${item.type} • ${item.events} interactions</div>
                </li>`
            ).join('');
            
            const longestContent = insights.top_content?.longest_content || [];
            const longestList = document.getElementById('longest-content');
            longestList.innerHTML = longestContent.map(item =>
                `<li class="content-item">
                    <div class="content-title">${item.title}</div>
                    <div class="content-meta">${item.type} • ${item.words.toLocaleString()} words</div>
                </li>`
            ).join('');
            
            // Update recommendations
            const recommendations = insights.recommendations || [];
            const recommendationsList = document.getElementById('recommendations');
            recommendationsList.innerHTML = recommendations.map(rec =>
                `<li>${rec}</li>`
            ).join('');
            
            // Update generated time
            document.getElementById('generated-time').textContent = 
                new Date(insights.generated_at).toLocaleString();
        }
    </script>
</body>
</html>"""
        
        dashboard_file = self.templates_dir / 'dashboard.html'
        with open(dashboard_file, 'w') as f:
            f.write(dashboard_html)
        
        logger.info("Created default dashboard template")
    
    def get_insights_json(self, days: int = 30) -> str:
        """Get insights as JSON for API endpoints."""
        try:
            insights = self.analytics.generate_insights(days)
            return json.dumps(insights, indent=2)
        except Exception as e:
            logger.error(f"Error getting insights JSON: {str(e)}")
            return json.dumps({"error": str(e)})
    
    def get_dashboard_html(self) -> str:
        """Get dashboard HTML content."""
        try:
            dashboard_file = self.templates_dir / 'dashboard.html'
            if dashboard_file.exists():
                with open(dashboard_file, 'r') as f:
                    return f.read()
            else:
                return "<html><body><h1>Dashboard template not found</h1></body></html>"
        except Exception as e:
            logger.error(f"Error getting dashboard HTML: {str(e)}")
            return f"<html><body><h1>Error: {str(e)}</h1></body></html>"
    
    def start_server(self, threaded: bool = True):
        """Start the dashboard web server."""
        try:
            # Simple HTTP server implementation
            import http.server
            import socketserver
            from urllib.parse import urlparse, parse_qs
            
            class DashboardHandler(http.server.BaseHTTPRequestHandler):
                def do_GET(self):
                    parsed_path = urlparse(self.path)
                    
                    if parsed_path.path == '/':
                        # Serve dashboard
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        dashboard_html = self.server.dashboard.get_dashboard_html()
                        self.wfile.write(dashboard_html.encode())
                        
                    elif parsed_path.path == '/api/insights':
                        # Serve insights JSON
                        query_params = parse_qs(parsed_path.query)
                        days = int(query_params.get('days', [30])[0])
                        
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.end_headers()
                        insights_json = self.server.dashboard.get_insights_json(days)
                        self.wfile.write(insights_json.encode())
                        
                    elif parsed_path.path.startswith('/static/'):
                        # Serve static files
                        file_path = self.server.dashboard.static_dir / parsed_path.path[8:]
                        if file_path.exists():
                            self.send_response(200)
                            if file_path.suffix == '.css':
                                self.send_header('Content-type', 'text/css')
                            elif file_path.suffix == '.js':
                                self.send_header('Content-type', 'application/javascript')
                            else:
                                self.send_header('Content-type', 'application/octet-stream')
                            self.end_headers()
                            with open(file_path, 'rb') as f:
                                self.wfile.write(f.read())
                        else:
                            self.send_error(404)
                    else:
                        self.send_error(404)
                
                def log_message(self, format, *args):
                    # Suppress default HTTP logging
                    pass
            
            # Create server
            with socketserver.TCPServer((self.host, self.port), DashboardHandler) as httpd:
                httpd.dashboard = self
                
                logger.info(f"Dashboard server starting on http://{self.host}:{self.port}")
                print(f"Atlas Dashboard available at: http://{self.host}:{self.port}")
                print("Press Ctrl+C to stop the server")
                
                if threaded:
                    import threading
                    server_thread = threading.Thread(target=httpd.serve_forever)
                    server_thread.daemon = True
                    server_thread.start()
                    return httpd
                else:
                    httpd.serve_forever()
                    
        except Exception as e:
            logger.error(f"Error starting dashboard server: {str(e)}")
            raise
    
    def stop_server(self, server):
        """Stop the dashboard server."""
        try:
            if server:
                server.shutdown()
                logger.info("Dashboard server stopped")
        except Exception as e:
            logger.error(f"Error stopping server: {str(e)}")
    
    def generate_static_dashboard(self, output_file: str = "dashboard_export.html"):
        """Generate static HTML dashboard."""
        try:
            insights = self.analytics.generate_insights(30)
            
            # Get template and inject data
            template = self.get_dashboard_html()
            
            # Replace the fetch call with embedded data
            insights_js = f"const insights = {json.dumps(insights)}; updateDashboard(insights);"
            template = template.replace(
                "fetch('/api/insights')\n            .then(response => response.json())\n            .then(data => {\n                updateDashboard(data);\n            })\n            .catch(error => {\n                console.error('Error loading analytics:', error);\n                document.getElementById('system-status').textContent = 'Error loading data';\n            });",
                insights_js
            )
            
            # Write to file
            output_path = Path(output_file)
            with open(output_path, 'w') as f:
                f.write(template)
            
            logger.info(f"Static dashboard generated: {output_path}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"Error generating static dashboard: {str(e)}")
            return None


def start_dashboard_server(config: Dict[str, Any] = None, port: int = 8080):
    """Convenience function to start dashboard server."""
    config = config or {}
    config['dashboard_port'] = port
    
    dashboard = DashboardServer(config)
    return dashboard.start_server(threaded=True)


def generate_dashboard_export(config: Dict[str, Any] = None, output_file: str = "atlas_dashboard.html"):
    """Convenience function to generate static dashboard."""
    dashboard = DashboardServer(config)
    return dashboard.generate_static_dashboard(output_file)