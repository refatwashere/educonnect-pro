# Testing Guide

## 🧪 Test Setup

### Prerequisites
```bash
cd backend
pip install pytest pytest-asyncio httpx
```

### Test Structure
```
backend/
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_classes.py
│   └── conftest.py
```

## 🔧 Basic Test Setup

### Create Test Configuration
```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.config.database import get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)
```

### Authentication Tests
```python
# tests/test_auth.py
def test_login_success(client):
    response = client.post(
        "/api/v3/auth/token",
        data={"username": "teacher@school.edu", "password": "password"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_credentials(client):
    response = client.post(
        "/api/v3/auth/token",
        data={"username": "wrong", "password": "wrong"}
    )
    assert response.status_code == 401
```

### Classes Tests
```python
# tests/test_classes.py
def test_get_classes_unauthorized(client):
    response = client.get("/api/v3/classes")
    assert response.status_code == 401

def test_create_class_success(client):
    # Login first
    login_response = client.post(
        "/api/v3/auth/token",
        data={"username": "teacher@school.edu", "password": "password"}
    )
    token = login_response.json()["access_token"]
    
    # Create class
    response = client.post(
        "/api/v3/classes",
        json={"name": "Test Class", "description": "Test Description"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Class"
```

## 🚀 Running Tests

### Run All Tests
```bash
cd backend
pytest
```

### Run Specific Tests
```bash
pytest tests/test_auth.py
pytest tests/test_classes.py -v
```

### Run with Coverage
```bash
pip install pytest-cov
pytest --cov=src tests/
```

## 🔍 Manual Testing

### API Testing with curl
```bash
# Login
curl -X POST "http://localhost:8000/api/v3/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=teacher@school.edu&password=password"

# Get classes (replace TOKEN)
curl -X GET "http://localhost:8000/api/v3/classes" \
  -H "Authorization: Bearer TOKEN"

# Create class
curl -X POST "http://localhost:8000/api/v3/classes" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Physics 101", "description": "Introduction to Physics"}'
```

### Frontend Testing
```bash
cd frontend
npm test  # If tests are added
```

## 📊 Test Coverage Goals

- **Authentication**: Login, logout, token validation
- **Classes**: CRUD operations, authorization
- **Database**: Connection, migrations, data integrity
- **API**: Response formats, error handling
- **Integration**: End-to-end user flows

## 🎯 Next Testing Steps

1. **Add Unit Tests**: Test individual functions
2. **Integration Tests**: Test API endpoints
3. **E2E Tests**: Test complete user workflows
4. **Performance Tests**: Load testing for scalability
5. **Security Tests**: Authentication and authorization