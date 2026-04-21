from fastapi import FastAPI
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"message": "Hello from FastAPI"}

@app.get("/health")
def health():
    logger.info("Health endpoint called")
    return {"status": "ok"}

@app.get("/message")
def message():
    app_message = os.getenv("APP_MESSAGE", "Default message from FastAPI")
    logger.info("Message endpoint called")
    return {"message": app_message}
