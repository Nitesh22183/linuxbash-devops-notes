# Day 10 Summary

## What I learned
- What Nginx is
- What a reverse proxy is
- How to configure Nginx to forward traffic to a backend app
- How to test through port 80
- What Route 53 is
- Difference between A, CNAME, and Alias records
- What TTL means

## What worked
- Nginx installation
- Nginx reverse proxy to FastAPI app
- /health worked through port 80

## What broke
- Example: syntax mistake in nginx config
- Example: security group did not allow port 80

## How I fixed it
- used sudo nginx -t before reload
- added HTTP port 80 inbound rule
