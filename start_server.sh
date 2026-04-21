
#!/bin/bash

# Kill any existing server
pkill -f "http.server" 2>/dev/null

cd ~/server-lab/web || exit 1

mkdir -p ../logs

python3 -m http.server 8000 --bind 0.0.0.0 > ../logs/server.log 2>&1 &

echo $! > ~/server-lab/server.pid
echo "Server started (PID: $!)"
