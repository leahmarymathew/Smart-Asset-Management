from flask import Flask
from .auth import login
from .rbac import require_role
from .assets import create_asset, list_assets, archive_asset

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login_route():
    return login()

@app.route("/assets", methods=["POST"])
@require_role(["admin", "manager"])
def create_asset_route():
    return create_asset()

@app.route("/assets", methods=["GET"])
@require_role(["admin", "manager", "viewer"])
def list_assets_route():
    return list_assets()

@app.route("/assets/<asset_id>/archive", methods=["POST"])
@require_role(["admin"])
def archive_asset_route(asset_id):
    return archive_asset(asset_id)

if __name__ == "__main__":
    app.run(debug=True)
