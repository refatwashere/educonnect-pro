import pytest

def test_get_classes_unauthorized(client):
    response = client.get("/api/v3/classes")
    assert response.status_code == 401

def test_get_classes_empty(client, auth_headers):
    response = client.get("/api/v3/classes", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == []

def test_create_class_success(client, auth_headers):
    class_data = {
        "name": "Physics 101",
        "description": "Introduction to Physics",
        "subject": "Physics",
        "grade_level": "Grade 10"
    }
    response = client.post("/api/v3/classes", json=class_data, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Physics 101"
    assert data["description"] == "Introduction to Physics"
    assert data["subject"] == "Physics"
    assert data["grade_level"] == "Grade 10"
    assert data["students_count"] == 0
    assert "id" in data
    assert "created_at" in data

def test_create_class_unauthorized(client):
    class_data = {"name": "Test Class"}
    response = client.post("/api/v3/classes", json=class_data)
    assert response.status_code == 401

def test_get_class_by_id(client, auth_headers):
    # Create class first
    class_data = {"name": "Math 101", "description": "Basic Math"}
    create_response = client.post("/api/v3/classes", json=class_data, headers=auth_headers)
    class_id = create_response.json()["id"]
    
    # Get class by ID
    response = client.get(f"/api/v3/classes/{class_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Math 101"
    assert data["id"] == class_id

def test_get_class_not_found(client, auth_headers):
    response = client.get("/api/v3/classes/nonexistent", headers=auth_headers)
    assert response.status_code == 404

def test_update_class(client, auth_headers):
    # Create class first
    class_data = {"name": "Chemistry 101"}
    create_response = client.post("/api/v3/classes", json=class_data, headers=auth_headers)
    class_id = create_response.json()["id"]
    
    # Update class
    update_data = {"name": "Advanced Chemistry", "description": "Advanced Chemistry Course"}
    response = client.put(f"/api/v3/classes/{class_id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Advanced Chemistry"
    assert data["description"] == "Advanced Chemistry Course"

def test_delete_class(client, auth_headers):
    # Create class first
    class_data = {"name": "Biology 101"}
    create_response = client.post("/api/v3/classes", json=class_data, headers=auth_headers)
    class_id = create_response.json()["id"]
    
    # Delete class
    response = client.delete(f"/api/v3/classes/{class_id}", headers=auth_headers)
    assert response.status_code == 204
    
    # Verify class is deleted
    get_response = client.get(f"/api/v3/classes/{class_id}", headers=auth_headers)
    assert get_response.status_code == 404