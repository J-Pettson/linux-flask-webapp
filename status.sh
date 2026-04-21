#!/bin/bash

echo "Checking server status..."


if pgrep -f "http.server" > /dev/null
then
    echo "Server is RUNNING"
else
    echo "Server is STOPPED"
fi
