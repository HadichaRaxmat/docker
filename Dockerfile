FROM python:3.9-slim
COPY app.py /app.py
EXPOSE 8000
CMD ["python", "app.py"]
