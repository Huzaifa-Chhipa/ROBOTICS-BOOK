FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Backend ./Backend

# 🔥 THIS LINE FIXES EVERYTHING
ENV PYTHONPATH=/app

CMD ["sh", "-c", "uvicorn Backend.src.main:app --host 0.0.0.0 --port $PORT"]