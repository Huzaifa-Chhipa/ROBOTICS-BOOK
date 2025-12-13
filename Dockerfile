FROM python:3.8-slim

WORKDIR /app

# System dependencies needed for TF1.15
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    wget \
    git \
    libfreetype6-dev \
    libhdf5-dev \
    libzmq3-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# Install TF1.15 + other dependencies
RUN pip install --no-cache-dir -r requirements.txt tensorflow==1.15

COPY backend ./backend

ENV PYTHONPATH=/app

CMD ["sh", "-c", "uvicorn backend.src.main:app --host 0.0.0.0 --port $PORT"]