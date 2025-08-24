FROM python:3.11-slim
WORKDIR /app
RUN pip install fastapi uvicorn httpx
COPY relay.py .
ENV PORT=8080
CMD ["uvicorn", "relay:app", "--host", "0.0.0.0", "--port", "8080"]
