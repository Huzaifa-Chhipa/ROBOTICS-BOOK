FROM tensorflow/tensorflow:1.15.5-py3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend

ENV PYTHONPATH=/app

CMD ["sh", "-c", "uvicorn backend.src.main:app --host 0.0.0.0 --port $PORT"]