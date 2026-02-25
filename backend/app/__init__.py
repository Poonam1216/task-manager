from flask import Flask
from flask_cors import CORS

from .extensions import db, ma
from .config import Config
from .routes import task_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # enable CORS globally
    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    ma.init_app(app)

    # register blueprint
    app.register_blueprint(task_bp)

    with app.app_context():
        db.create_all()

    return app
