# Route 53 Notes

## What is Route 53?
Route 53 is AWS DNS service used to manage domains, hosted zones, and traffic routing.

## Public vs Private hosted zone
- Public hosted zone: internet-facing DNS
- Private hosted zone: internal DNS inside VPC

## A record
Maps a domain to an IP address.

## CNAME
Maps one domain name to another domain name.

## Alias record
AWS-specific record that can point to resources like ALB and CloudFront.

## TTL
TTL means time to live and controls how long DNS responses are cached.


# DNS Flow Example

User enters: api.example.com
-> Route 53 checks DNS record
-> Record points to EC2 public IP or ALB
-> Request reaches Nginx on port 80
-> Nginx reverse proxies to FastAPI app on port 8000
