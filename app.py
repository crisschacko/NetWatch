from flask import Flask, jsonify, render_template

from monitor import get_system_stats, get_processes
from network import get_connections, get_network_stats

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/system")
def system_api():
    return jsonify(get_system_stats())


@app.get("/api/network")
def network_api():
    return jsonify({
        "stats": get_network_stats(),
        "connections": get_connections()
    })


@app.get("/api/processes")
def processes_api():
    return jsonify({
        "processes": get_processes()
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "online",
        "service": "NetWatch",
        "version": "1.0.0"
    })


if __name__ == "__main__":
    app.run(debug=True)
