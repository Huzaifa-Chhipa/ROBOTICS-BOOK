FROM python:3.11-slim

WORKDIR /app

COPY Backend/ ./Backend/

RUN pip install --no-cache-dir -r Backend/requirements.txt

CMD ["sh", "-c", "uvicorn Backend.src.main:app --host 0.0.0.0 --port $PORT"]