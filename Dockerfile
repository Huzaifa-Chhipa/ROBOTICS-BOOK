# Use TensorFlow 1.15 preinstalled image
FROM tensorflow/tensorflow:1.15.5-py3

WORKDIR /app

# Install system dependencies for Python packages
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

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy requirements (without openai for now)
COPY requirements.txt .

# Optional: Comment out or remove openai line in requirements.txt
RUN sed -i '/openai/d' requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend ./backend

# Set Python path for imports
ENV PYTHONPATH=/app

# Start FastAPI app
CMD ["sh", "-c", "uvicorn backend.src.main:app --host 0.0.0.0 --port $PORT"]