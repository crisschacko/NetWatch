from flask import Flask, jsonify, render_template
from monitor import get_system_stats

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


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
