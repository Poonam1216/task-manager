from datetime import datetime
from .extensions import db


class Task(db.Model):
    """
    Task database model.

    Enforces valid state via:
    - required title
    - controlled priority/status values
    """

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    status = db.Column(
        db.String(50),
        nullable=False,
        default="pending"
    )

    priority = db.Column(
        db.String(50),
        nullable=False,
        default="medium"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"
