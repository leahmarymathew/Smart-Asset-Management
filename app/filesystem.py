import os
import stat
import time

BASE_PATH = "data/assets"

def create_asset_dir(asset_id):
    path = os.path.join(BASE_PATH, asset_id)
    os.makedirs(path, exist_ok=True)
    os.makedirs(os.path.join(path, "files"), exist_ok=True)
    return path

def get_fs_metadata(path):
    s = os.stat(path)
    return {
        "size_bytes": s.st_size,
        "permissions": stat.filemode(s.st_mode),
        "last_modified": time.ctime(s.st_mtime),
        "created": time.ctime(s.st_ctime)
    }
