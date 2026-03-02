FROM python:3.9-slim
WORKDIR /app
RUN pip install requests flask
COPY app.py .
CMD ["python", "app.py"]


