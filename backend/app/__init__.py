from flask import Flask
from flask_cors import CORS  # ✅ add this import

from .routes import register_routes

def create_app() -> Flask:
    app = Flask(__name__)

    CORS(app)  # ✅ allow frontend (React) requests

    register_routes(app)
    return app
