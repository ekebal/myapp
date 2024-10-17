from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"id": 1, "name": "John", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John"

def test_update_user():
    response = client.put("/users/1", json={"id": 1, "name": "Jane", "email": "jane@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Jane"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}
