from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_cors import cross_origin
from .models import Task
from .extensions import db
from .schemas import task_schema, tasks_schema

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

task_bp = Blueprint("tasks", __name__)


@task_bp.route("/tasks", methods=["GET"])
@cross_origin()
def get_tasks():
    """Return all tasks"""

    tasks = Task.query.order_by(Task.created_at.desc()).all()
    logger.info("Fetched all tasks")

    return jsonify(tasks_schema.dump(tasks))


@task_bp.route("/tasks", methods=["POST"])
@cross_origin()
def create_task():
    """Create new task"""

    try:
        data = task_schema.load(request.json)
    except ValidationError as err:
        logger.warning(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400

    task = Task(**data)

    db.session.add(task)
    db.session.commit()

    logger.info(f"Task created with ID: {task.id}")

    return task_schema.jsonify(task), 201


@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
@cross_origin()
def update_task(task_id):

    task = Task.query.get_or_404(task_id)

    try:
        data = task_schema.load(request.json, partial=True)
    except ValidationError as err:
        logger.warning(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400

    for key, value in data.items():
        setattr(task, key, value)

    db.session.commit()

    logger.info(f"Task updated: {task.id}")

    return task_schema.jsonify(task)


@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
@cross_origin()
def delete_task(task_id):

    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    logger.info(f"Task deleted: {task_id}")

    return jsonify({"message": "deleted"})
