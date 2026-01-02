from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to Smart Asset Management API", "endpoints": {"/health": "Health check"}})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "Smart Asset Management"})

if __name__ == "__main__":
    app.run(debug=True)
