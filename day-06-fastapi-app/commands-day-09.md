# Day 09 Commands

## SSH
ssh -i ~/Downloads/your-key.pem ubuntu@YOUR_PUBLIC_IP

## Install Docker
sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker

## Pull image
sudo docker pull nex22183/fastapi-app:day8

## Run container
sudo docker run -d -p 8000:8000 --name fastapi-ec2 -e APP_MESSAGE="Hello from EC2" nex22183/fastapi-app:day8

## Check running containers
sudo docker ps

## Check logs
sudo docker logs fastapi-ec2
