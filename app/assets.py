import os
import json
import uuid
from flask import request, jsonify
from .filesystem import create_asset_dir, get_fs_metadata
from .rbac import require_role

def create_asset():
    data = request.json
    asset_id = str(uuid.uuid4())

    path = create_asset_dir(asset_id)

    metadata = {
        "asset_id": asset_id,
        "name": data.get("name"),
        "type": data.get("type"),
        "owner": data.get("owner"),
        "status": "active"
    }

    fs_meta = get_fs_metadata(path)
    metadata.update(fs_meta)

    with open(os.path.join(path, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)

    return jsonify(metadata), 201

def list_assets():
    assets = []
    base = "data/assets"

    for asset_id in os.listdir(base):
        meta_path = os.path.join(base, asset_id, "metadata.json")
        if os.path.exists(meta_path):
            with open(meta_path) as f:
                assets.append(json.load(f))

    return jsonify(assets)

def archive_asset(asset_id):
    path = os.path.join("data/assets", asset_id, "metadata.json")
    if not os.path.exists(path):
        return jsonify({"error": "Asset not found"}), 404

    with open(path) as f:
        data = json.load(f)

    data["status"] = "archived"

    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    return jsonify({"msg": "Asset archived"})
