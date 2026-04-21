#!/bin/bash
cd /home/pettson/server-lab/web  || exit 1
exec python3 -m http.server 8000 --bind 0.0.0.0
