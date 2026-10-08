from flask import Flask, jsonify, render_template
from monitor import get_system_stats, get_network_connections

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/system")
def system_stats():
    return jsonify(get_system_stats())


@app.route("/api/network")
def network_connections():
    return jsonify({
        "connections": get_network_connections()
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "project": "NetWatch"
    })


if __name__ == "__main__":
    app.run(debug=True)
