FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Use lowercase folder name
COPY backend ./backend

# Set Python path so modules are found
ENV PYTHONPATH=/app

# Start FastAPI app
CMD ["sh", "-c", "uvicorn backend.src.main:app --host 0.0.0.0 --port $PORT"]