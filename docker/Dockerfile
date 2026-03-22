FROM python:3.9-slim

WORKDIR /app

RUN pip install requests flask 
RUN apt-get update && apt-get install -y curl


COPY app/ .
CMD ["python", "/app/app.py"]
