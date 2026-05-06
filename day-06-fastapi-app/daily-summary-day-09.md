# Day 09 Summary

## What I learned
- How to launch an EC2 instance
- How to connect using SSH
- How to install Docker on EC2
- How to pull an image from Docker Hub
- How to run my FastAPI app on EC2
- How security groups affect reachability

## What worked
- SSH connection
- Docker installation
- Container launch
- /health endpoint from public IP

## What broke
- Example: SSH key permission issue
- Example: app port blocked in security group

## How I fixed it
- Used chmod 400 on the key
- Added inbound rule for port 8000
