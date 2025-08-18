# Multi-stage Docker build for Atlas Personal Knowledge System
# Optimized for production deployment with minimal attack surface

# Build stage
FROM python:3.11-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    pkg-config \
    libffi-dev \
    libssl-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create build user
RUN useradd --create-home --shell /bin/bash builder
USER builder
WORKDIR /home/builder

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim as production

# Install runtime dependencies only
RUN apt-get update && apt-get install -y \
    sqlite3 \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create application user
RUN useradd --create-home --shell /bin/bash --uid 1000 atlas
USER atlas
WORKDIR /home/atlas/app

# Copy Python packages from builder
COPY --from=builder /home/builder/.local /home/atlas/.local
ENV PATH="/home/atlas/.local/bin:$PATH"

# Copy application code
COPY --chown=atlas:atlas . .

# Create necessary directories
RUN mkdir -p \
    /home/atlas/app/data \
    /home/atlas/app/logs \
    /home/atlas/app/exports \
    /home/atlas/app/output \
    /home/atlas/app/inputs \
    /home/atlas/app/temp

# Set up configuration
RUN cp config/config.example.json config/config.json

# Expose ports
EXPOSE 5000 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:5000/api/capture/health || exit 1

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV ATLAS_CONFIG_PATH=/home/atlas/app/config/config.json
ENV ATLAS_DATA_DIR=/home/atlas/app/data

# Default command - can be overridden
CMD ["python", "scripts/atlas_background_service.py"] 