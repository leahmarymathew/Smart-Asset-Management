import jwt
from flask import request, jsonify
from .database import get_db
from .config import SECRET_KEY

def login():
    data = request.json
    db = get_db()
    c = db.cursor()
    c.execute("SELECT role FROM users WHERE username=? AND password=?", (data["username"], data["password"]))
    row = c.fetchone()
    db.close()

    if not row:
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({"user": data["username"], "role": row[0]}, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})
