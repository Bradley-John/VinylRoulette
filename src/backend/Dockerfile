FROM python:3.11-slim
WORKDIR /app
COPY src/backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
ENV PYTHONPATH=/app/src
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]