# Multi-stage Dockerfile for Matomo MCP Server
# Optimized for Glama hosting platform

# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml README.md LICENSE ./
COPY matomo_mcp ./matomo_mcp

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY matomo_mcp ./matomo_mcp

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MCP_TRANSPORT=stdio

# Health check (if Glama supports it)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import matomo_mcp; print('OK')" || exit 1

# Run the MCP server
ENTRYPOINT ["python", "-m", "matomo_mcp"]
