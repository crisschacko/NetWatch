from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="NetWatch")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>NetWatch</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                text-align: center;
                padding: 80px;
            }

            h1 {
                font-size: 48px;
            }

            p {
                color: #cbd5e1;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>NetWatch</h1>
        <p>Network & System Monitoring Dashboard</p>
        <p>System is running successfully.</p>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {
        "status": "online",
        "project": "NetWatch"
    }
