import json
import pytest

from app import create_app
from app.extensions import db


@pytest.fixture
def client():

    app = create_app()

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_create_task(client):

    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "priority": "high"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Test Task"
    assert data["priority"] == "high"


def test_get_tasks(client):

    client.post(
        "/tasks",
        json={"title": "Task 1"}
    )

    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 1


def test_update_task(client):

    res = client.post(
        "/tasks",
        json={"title": "Old"}
    )

    task_id = res.get_json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"status": "completed"}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "completed"


def test_delete_task(client):

    res = client.post(
        "/tasks",
        json={"title": "Delete me"}
    )

    task_id = res.get_json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
