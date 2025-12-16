FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend

EXPOSE 7860

CMD ["sh", "-c", "uvicorn backend.src.main:app --host 0.0.0.0 --port ${PORT:-7860}"]
