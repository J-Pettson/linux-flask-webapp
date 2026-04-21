#!/bin/bash
cd /home/pettson/server-lab || exit 1
source /home/pettson/server-lab/venv/bin/activate
exec python /home/pettson/server-lab/app.py
