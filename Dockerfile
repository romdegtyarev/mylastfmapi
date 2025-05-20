FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends vim && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]
