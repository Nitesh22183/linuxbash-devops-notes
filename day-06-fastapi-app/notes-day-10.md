# Day 10 Notes - Nginx and Route 53

## What is Nginx?
Nginx is a web server and reverse proxy.

## What is a reverse proxy?
A reverse proxy receives user requests and forwards them to a backend application.

## Why use Nginx in front of FastAPI?
- expose standard port 80
- hide internal app port 8000
- support production-style routing
- prepare for future HTTPS


## Reverse proxy troubleshooting
If Nginx fails:
- check nginx service status
- check nginx config syntax
- check backend app reachability on port 8000
- check nginx logs
- check security group rule for port 80
