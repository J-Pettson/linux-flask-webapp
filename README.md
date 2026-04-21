# Flask Monitoring Dashboard


A small linux home lab project built with Flask and Python.

This app acts as a lightweight internal dashboard for basic server monitoring. It includes a homepage with navigation, system status pages, log viewing, metrics, health checks, and runs as a systemd service on Ubuntu.

## Features

- Dark-themed homepage dashboard
-̈́ `/hello` route showing uptime
- `/status` route showing:
    -uptime
    -disk usage
    -memory usage
    -CPU usage
- `/metrics` route for system metrics
- `/logs` route showing the latest log lines
- `/who` route showing logged-in users
- `/health` route for service health
- Custom dark-themed pages
- Logging to file
- Runs as a `systemd` service

## Tech used
- Python
- Flask
- Ubuntu Linux
- systemd
- Bash/Linux commands:
  -`uptime`
  - `df-h`
  - `free -h`
  - `top`
  - `who`

## What I learned

This project helped me practice:

- Python basics
- Flask routing
- HTML and CSS basics
- Linux commands
- Reading and debugging error messages
- Log handling
- Running a Python app as a systemd service
- Restarting and troubleshooting services

## Example Routes

- `/`
- `/hello`
- `/status`
- `/metrics` 
- `/logs`
- `/health`
- `/who`

## Screenshots
### Homepage
![Web Interface](screenshots/Homepage.png)

### Hello Page
![Web Interface](screenshots/Hello.png)

### Status Page
![Web Interface](screenshots/Status.png)

### Metrics Page
![Web Interface](screenshots/Metrics.png)

### Logs Page
![Web Interface](screenshots/Logs.png)

### Health Page
![Web Interface](screenshots/Health.png)

### Who Page
![Web Interface](screenshots/Who.png)

## Running the App Manually

```bash
cd ~/server-lab
source venv/bin/activate
python app.py 

