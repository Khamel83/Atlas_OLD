from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import sys

# Add parent directory to Python path for module imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.routers import content, search, cognitive, auth, dashboard, transcription, worker, shortcuts

app = FastAPI(
    title="Atlas API",
    description="API for the Atlas cognitive amplification platform",
    version="1.0.0"
)

# Add CORS middleware with security restrictions
allowed_origins = [
    "http://localhost:3000",
    "http://localhost:8000", 
    "http://127.0.0.1:8000",
    "https://your-domain.com"  # Replace with actual production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(content.router, prefix="/api/v1/content", tags=["content"])
app.include_router(search.router, prefix="/api/v1/search", tags=["search"])
app.include_router(cognitive.router, prefix="/api/v1/cognitive", tags=["cognitive"])
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["dashboard"])
app.include_router(transcription.router, prefix="/api/v1/transcriptions", tags=["transcription"])
app.include_router(worker.router, prefix="/api/v1/worker", tags=["worker"])
app.include_router(shortcuts.router, prefix="/api/v1/shortcuts", tags=["shortcuts"])

@app.get("/api/v1/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/shortcuts")
async def shortcuts_redirect():
    """Redirect to shortcuts install page"""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/api/v1/shortcuts/install")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)