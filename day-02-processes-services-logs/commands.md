ps
ps -ef
ps aux
top
htop
pgrep nginx-finds PID by name
pidof nginx-gives PID of process
kill<PID>
kill-9<PID><process name>

systemctl status nginx
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl enable nginx
systemctl disable nginx
curl http://localhost-check the status


journalctl
journalctl -u nginx
journalctl -u nginx -n 20
journalctl -xe
tail /var/log/syslog
tail -f /var/log/syslog
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

grep, find, log filtering

grep nginx /var/log/syslog
grep -i error /var/log/nginx/error.log
grep -r "server" /etc/nginx/
find /var/log -name "*.log"
ls -lh /var/log/nginx/
 
