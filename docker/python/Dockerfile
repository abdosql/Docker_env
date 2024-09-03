FROM python:3.9-slim

WORKDIR /app

RUN useradd -ms /bin/bash appuser
USER appuser

COPY python_worker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "src.tasks", "worker", "--loglevel=info"]