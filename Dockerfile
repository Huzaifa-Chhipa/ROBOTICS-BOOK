FROM tensorflow/tensorflow:1.15.5-py3

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libhdf5-dev \
    libzmq3-dev \
    pkg-config \
    git \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip first
RUN python3 -m pip install --upgrade pip

# Copy requirements & install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend ./backend

# PYTHONPATH for module imports
ENV PYTHONPATH=/app

# Start FastAPI app
CMD ["sh", "-c", "uvicorn backend.src.main:app --host 0.0.0.0 --port $PORT"]