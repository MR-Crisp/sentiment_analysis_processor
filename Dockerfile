FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/

COPY backend/sentiment_svm_model.joblib ./backend/
COPY backend/tfidf_vectorizer.joblib ./backend/
EXPOSE 5000

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
WORKDIR /app/backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]