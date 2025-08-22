"""
Unified API Server for Atlas
This server runs both the new FastAPI-based APIs and existing Flask-based APIs.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
import os
import sys

# Add parent directory to Python path for module imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import Flask applications
from api import analytics_api, search_api, capture

# Import FastAPI application
from api.main import app as fastapi_app

# Import new FastAPI-based APIs
from api.auth_api import auth_router
from api.content_api import content_router
from api.cognitive_api import cognitive_router

# Create Flask apps
analytics_flask_app = analytics_api.create_flask_app()
search_flask_app = search_api.create_flask_app()
capture_flask_app = capture.create_flask_app()

# Mount Flask apps to FastAPI using WSGI middleware
fastapi_app.mount("/api/analytics", WSGIMiddleware(analytics_flask_app))
fastapi_app.mount("/api/search", WSGIMiddleware(search_flask_app))
fastapi_app.mount("/api/capture", WSGIMiddleware(capture_flask_app))

# Include all API routers
fastapi_app.include_router(auth_router)
fastapi_app.include_router(content_router)
fastapi_app.include_router(cognitive_router)

if __name__ == "__main__":  
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)