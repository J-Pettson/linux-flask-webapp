from flask import Flask, request, redirect
import os
import logging
import sys

app = Flask(__name__)

def dark_page(title, content):
    return f"""
    <html>
    <head>
         <title>{title}</title>
         <style>
          body {{
               background-color: #111;
               color: #00ff88;
               font-family: monospace;
               padding: 30px;
          }}
          h1 {{
               margin-bottom: 20px;
          }}
          pre {{
              background: #1a1a1a;
              color: #cfcfcf;
              padding: 20px;
              border: 1px solid #00ff88;
              border-radius: 8px;
              white-space: pre-warp;
          }}
          a:hover {{
               background-color: #00ff88;
               color: #111;
          }}
        </style>
        </head>
        <body>
            <a href="/"> Back</a>
            <h1>{title}</h1>
            <pre>{content}</pre>
       </body>
       </html>
       """

@app.before_request
def lowercase_redirect():
    if request.path != request.path.lower():
         logging.info(f"Redirect:{request.path} -> {request.path.lower()}")
         return redirect(request.path.lower())

@app.before_request
def log_request_info():
    logging.info(f"{request.remote_addr} - {request.method} {request.path}")

@app.after_request
def log_response_info(response):
    logging.info(f"{request.remote_addr} - {request.method} {request.path} - {response.status}")
    return response

logging.basicConfig(
    filename="/home/pettson/server-lab/logs/server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Jesper's Flask Server</title>
        <style>
             body {
                 background-color: #111;
                 color: #00ff88;
                 font-family: monospace;
                 text-align: center;
                 padding-top: 80px;
             }
             h1 {
                 font-size: 48px;
                 margin-bottom: 10px;
             }

             p {
                color: #cfcfcf;
                margin-bottom: 30px;
             }

             .links {
                display: flex;
                flex-direction: column;
                gap: 12px;
                align-items: center;
             }
             a {
                display: inline-block;
                width: 220px;
                padding: 12px;
                text-decoration: none;
                color: white;
                border: 1px solid #00ff88;
                border-radius: 8px;
                transition: 0.2s;
             }

             a:hover {
                 background-color: 00ff88;
                 color: #111;
             }

             .small {
                 margin-top: 40px;
                 color: #888;
                 font-size: 14px;
             }
.links li {
    margin: 10px 0;
}
          </style>
         </head>
         <body>
               <h1> Jesper's Flask Server</h1>
               <p>System dashboard and monitoring lab</p>

               <ul class="links">
                   <li><a href="/hello">/hello</a></li>
                   <li><a href="/status">/status</a></li>
                   <li><a href="/metrics">/metrics</a></li>
                   <li><a href="/logs">/logs</a></li>
                   <li><a href="/health">/health</a></li>
                   <li><a href="/who">/who</a></li>
              </ul>

              <div class="small">
                  Flask &middot; Python &middot; Logging &middot; Monitoring &middot; Systemd
             </div>
           </body>
          </html>
    """

@app.route("/hello")
def hello():
    return dark_page("Hello", f"Uptime:\n{os.popen('uptime').read()}")

@app.route("/status")
def status():

    uptime = os.popen("uptime").read()
    disk = os.popen("df -h /").read()
    memory = os.popen("free -h").read()
    cpu = os.popen("top -bn1 | grep 'Cpu'").read()


    return dark_page("Server Status",  f"""=== SERVER STATUS ===

--- UPTIME ---
{uptime}

--- DISK ---
{disk}

--- MEMORY ---
{memory}

--- CPU ---
{cpu}
""")

@app.route("/who")
def who():
    users = os.popen("who").read()

    if not users.strip():
         users = "No logged in users found"

    return dark_page("Logged In Users", users)


@app.route("/logs")
def logs():
    try:
        path = "/home/pettson/server-lab/logs/server.log"

        if not os.path.exists(path):
            return dark_page("Logs", "Log file does not exist")

        with open(path, "r") as f:
            lines = f.readlines()

        last_lines = lines[-50:] # show last 50 lines only

        if not last_lines:
              return dark_page("Logs", "No logs found")

        return dark_page("Logs",  "".join(last_lines))

    except Exception as e:
        return dark_page("Logs", f"ERROR: {str(e)}")

@app.route("/health")
def health():
    content = f"""status: ok
service: server-lab
time: {os.popen("date").read().strip()}"""
    return dark_page("Health", content)

@app.route("/metrics")
def metrics():
    try:
        disk = os.popen("df -h /").read()
        memory = os.popen("free -h").read()
        cpu = os.popen("top -bn1 | grep 'cpu'").read()

        content = f"""--- DISK ---
{disk}

--- MEMORY ---
{memory}

--- CPU ---
{cpu}"""
        return dark_page("Metrics", content)

    except Exception as e:
        return dark_page("Metrics", f"ERROR:{str(e)}")

@app.errorhandler(404)
def not_found(error):
    logging.warning(f"404 Not Found:{request.path}")
    return """
    <html>
    <head>
        <title>404 - Page Not Found</title>
        <style>
            body {
                background: #111;
                color: #00ff88;
                font-family: monospace;
                text-align: center;
                padding-top: 11px;
            }
            a {
               color: #ffffff;
               text-decoration: none;
               border: 1px solid #00ff88;:
               padding: 10px 16px;
               border-radius: 6px;
             }
             a:hover {
                 background: #ooff88;
                 color: #111;
             }
          </style>
       </head>
       <body>
          <h1>404 - Page Not Found</h1>
          <p><a href="/">Go back home</a></p>
      </body>
      </html>
      """, 404
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
