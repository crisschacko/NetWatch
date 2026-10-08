from flask import Flask, jsonify
from monitor import get_system_stats

app = Flask(__name__)


@app.route("/")
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
                padding: 60px;
            }

            h1 {
                font-size: 48px;
            }

            .status {
                margin: 30px auto;
                padding: 20px;
                max-width: 500px;
                background: #1e293b;
                border-radius: 12px;
            }
        </style>
    </head>

    <body>
        <h1>NetWatch</h1>

        <div class="status">
            <h2>Network & System Monitoring</h2>
            <p>Dashboard is online.</p>
            <p>Visit <b>/api/system</b> to view system statistics.</p>
        </div>
    </body>
    </html>
    """


@app.route("/api/system")
def system_stats():
    return jsonify(get_system_stats())


@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "project": "NetWatch"
    })


if __name__ == "__main__":
    app.run(debug=True)
