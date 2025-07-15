import pytest

def test_login_success(client):
    response = client.post(
        "/api/v3/auth/token",
        data={"username": "teacher@school.edu", "password": "password"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(client):
    response = client.post(
        "/api/v3/auth/token",
        data={"username": "wrong", "password": "wrong"}
    )
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]

def test_login_missing_credentials(client):
    response = client.post("/api/v3/auth/token", data={})
    assert response.status_code == 422

def test_get_current_user(client, auth_headers):
    response = client.get("/api/v3/users/me", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "teacher@school.edu"
    assert data["role"] == "teacher"

def test_get_current_user_unauthorized(client):
    response = client.get("/api/v3/users/me")
    assert response.status_code == 401