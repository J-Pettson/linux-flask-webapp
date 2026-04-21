#!/bin/bash

backup_dir=~/server-lab/backup
timestamp=$(date +%F_%H-%M-%S)

cp -r ~/server-lab/web "$backup_dir/web_backup_$timestamp"
echo "Backup created: web_backup_$timestamp"

# Keep only the 5 newest backups
ls -dt $backup_dir/web_backup_* 2>/dev/null| tail -n +6 | xargs -r rm -r

echo "Old backups cleaned" 
