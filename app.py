from flask import Flask, jsonify, render_template

from monitor import get_system_stats, get_processes
from network import get_connections, get_network_stats


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/system")
def system_api():
    return jsonify(get_system_stats())


@app.route("/api/network")
def network_api():
    return jsonify({
        "stats": get_network_stats(),
        "connections": get_connections()
    })


@app.route("/api/processes")
def processes_api():
    return jsonify({
        "processes": get_processes()
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "service": "NetWatch",
        "version": "1.0.0"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
