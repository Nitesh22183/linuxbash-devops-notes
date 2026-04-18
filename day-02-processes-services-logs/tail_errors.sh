#!/bin/bash
tail -f /var/log/nginx/error.log | grep "crti"
