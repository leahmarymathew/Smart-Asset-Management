import jwt
from flask import request, jsonify
from functools import wraps
from .config import SECRET_KEY

def require_role(allowed):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return jsonify({"error": "Token missing"}), 403

            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            except:
                return jsonify({"error": "Invalid token"}), 403

            if payload["role"] not in allowed:
                return jsonify({"error": "Access denied"}), 403

            return f(*args, **kwargs)
        return wrapper
    return decorator
