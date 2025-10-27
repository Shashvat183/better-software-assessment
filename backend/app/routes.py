from flask import Blueprint, jsonify, request
from flask_cors import CORS

bp = Blueprint("api", __name__, url_prefix="/api")

TASKS = [
    {"id": 1, "name": "Setup project"},
    {"id": 2, "name": "Connect frontend and backend"},
    {"id": 3, "name": "Add comment feature"},
]

def register_routes(app):
    CORS(app)  # allow frontend to send requests
    app.register_blueprint(bp)

@bp.get("/tasks")
def get_tasks():
    return jsonify({"tasks": TASKS})

@bp.post("/tasks")
def add_task():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing task name"}), 400
    
    new_id = len(TASKS) + 1
    new_task = {"id": new_id, "name": data["name"]}
    TASKS.append(new_task)
    return jsonify(new_task), 201
