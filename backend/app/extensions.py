from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# shared extensions initialized in app factory
db = SQLAlchemy()
ma = Marshmallow()
