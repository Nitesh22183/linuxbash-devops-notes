# Day 7 Commands

## Build image
docker build -t fastapi-app-day7 .

## List images
docker images

## Run container
docker run -d -p 8000:8000 --name fastapi-container fastapi-app-day7

## Check running containers
docker ps

## See logs
docker logs fastapi-container

## Enter container
docker exec -it fastapi-container /bin/bash

## Stop container
docker stop fastapi-container

## Remove container
docker rm fastapi-container

## Run with environment variable
docker run -d -p 8000:8000 --name fastapi-container -e APP_MESSAGE="Hello from Docker" fastapi-app-day7
