FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY docker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY docker/ .

CMD ["python", "app.py"]
