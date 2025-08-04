# Dockerfile pour FastAPI + React intégré
FROM node:18 AS frontend-builder
WORKDIR /app/frontend
COPY frontend ./frontend
RUN cd frontend && npm install && npm run build

FROM python:3.11-slim
WORKDIR /app
COPY --from=frontend-builder /app/frontend/build ./app/frontend/build
COPY ./app ./app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]