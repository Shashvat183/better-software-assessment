import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as c:
        yield c


def test_add_edit_delete_comment(client):
    # Add
    res = client.post("/api/tasks/1/comments", json={"text": "hello"})
    assert res.status_code == 201
    created = res.get_json()
    assert created["text"] == "hello"
    cid = created["id"]

    # Edit
    res = client.put(f"/api/tasks/1/comments/{cid}", json={"text": "updated"})
    assert res.status_code == 200
    updated = res.get_json()
    assert updated["text"] == "updated"

    # Delete
    res = client.delete(f"/api/tasks/1/comments/{cid}")
    assert res.status_code == 204


def test_404_on_wrong_task_or_comment(client):
    # Edit non-existent
    res = client.put("/api/tasks/99/comments/999", json={"text": "x"})
    assert res.status_code == 404

    # Delete non-existent
    res = client.delete("/api/tasks/99/comments/999")
    assert res.status_code == 404
