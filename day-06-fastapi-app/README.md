# FastAPI DevOps Practice Project

## Project Overview
This is a Python FastAPI application used as the main project for my DevOps practice journey. I am using the same application across multiple stages such as local development, Docker containerization, Docker cache optimization, AWS EC2 deployment, and later CI/CD, Terraform, and Kubernetes.

## Application Endpoints
- `/` returns a welcome message
- `/health` returns app health status
- `/message` returns a message from an environment variable

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Docker
- AWS EC2
- Linux

## How to Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
