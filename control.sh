#!/bin/bash

echo "1) Start server"
echo "2) Stop server"
echo "3) Status"
echo "4) View logs"
echo "5) Backup site"
echo "6) Restart server"

read -p "Choose: " choice

case $choice in
    1) ./start_server.sh ;;
    2) ./stop_server.sh ;;
    3) ./status.sh ;;
    4) ./view_logs.sh ;;
    5) ./backup_site.sh ;;
    6) ./restart_server.sh ;;
    *) echo "Invalid option" ;;
 esac
