#!/bin/bash

PID_FILE=~/server-lab/server.pid

if [ -f "$PID_FILE"  ]; then
   PID=$(cat "$PID_FILE")

   if kill $PID 2>/dev/null; then
   rm "$PID_FILE"
   echo "server stopped (PID: $PID)"
   else
    echo "Failed to stop server (PID: $PID)"
   fi
  else
   echo "No PID file found"
fi
