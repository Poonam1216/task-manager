from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from .models import Task
from .extensions import db
from .schemas import task_schema, tasks_schema


task_bp = Blueprint("tasks", __name__)


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    """Return all tasks"""

    tasks = Task.query.order_by(Task.created_at.desc()).all()

    return jsonify(tasks_schema.dump(tasks))


@task_bp.route("/tasks", methods=["POST"])
def create_task():
    """Create new task"""

    try:
        data = task_schema.load(request.json)

    except ValidationError as err:
        return jsonify(err.messages), 400

    task = Task(**data)

    db.session.add(task)
    db.session.commit()

    return task_schema.jsonify(task), 201


@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    task = Task.query.get_or_404(task_id)

    try:
        data = task_schema.load(request.json, partial=True)

    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in data.items():
        setattr(task, key, value)

    db.session.commit()

    return task_schema.jsonify(task)


@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "deleted"})
