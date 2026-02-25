from flask import Flask
from flask_cors import CORS

from .extensions import db, ma
from .config import Config
from .routes import task_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # enable CORS for all routes
    CORS(app)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(task_bp)

    with app.app_context():
        db.create_all()

    return app

@app.errorhandler(Exception)
def handle_error(e):
    return {"error": str(e)}, 500
