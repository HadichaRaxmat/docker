FROM python:3.9-slim

WORKDIR /app
COPY app.py /app/

RUN pip install fastapi uvicorn

EXPOSE 8000 8100
CMD ["python", "app.py"]
