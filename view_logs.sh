#!/bin/bash

LOG_FILE=~/server-lab/logs/server.log
if  [ -f "$LOG_FILE"  ]; then
    tail -f "$LOG_FILE"
else
 echo "Log file not found"
fi
