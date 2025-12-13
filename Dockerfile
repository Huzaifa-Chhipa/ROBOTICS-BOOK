FROM python:3.11-slim

WORKDIR /app

# System dependencies for building packages
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    pkg-config \
    libfreetype6-dev \
    libhdf5-dev \
    libzmq3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy requirements
COPY requirements.txt .

# Install Python packages (latest TF2.x + openai + cohere)
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend ./backend

# Set PYTHONPATH
ENV PYTHONPATH=/app

# Start FastAPI app
CMD ["sh", "-c", "uvicorn backend.src.main:app --host 0.0.0.0 --port $PORT"]