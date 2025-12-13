FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
# Install TF1.15 + other dependencies
RUN pip install --no-cache-dir -r requirements.txt tensorflow==1.15

COPY backend ./backend

ENV PYTHONPATH=/app

CMD ["sh", "-c", "uvicorn backend.src.main:app --host 0.0.0.0 --port $PORT"]