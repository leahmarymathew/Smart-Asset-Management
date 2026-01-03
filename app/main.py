
from flask import Flask, jsonify
from app.auth import login
from app.rbac import require_role

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to Smart Asset Management API", "endpoints": {"/health": "Health check"}})

@app.route("/login", methods=["POST"])
def login_route():
    return login()

@app.route("/admin", methods=["GET"])
@require_role(["admin"])
def admin_area():
    return jsonify({"msg": "Admin access granted"})

@app.route("/manager", methods=["GET"])
@require_role(["admin", "manager"])
def manager_area():
    return jsonify({"msg": "Manager access granted"})

@app.route("/viewer", methods=["GET"])
@require_role(["admin", "manager", "viewer"])
def viewer_area():
    return jsonify({"msg": "Viewer access granted"})

if __name__ == "__main__":
    app.run(debug=True)
