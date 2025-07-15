# API Documentation

EduConnect Pro backend API built with FastAPI.

## Base URL

- Development: `http://localhost:8000`
- API Prefix: `/api/v3`

## Authentication

The API uses JWT Bearer token authentication.

### Login

```http
POST /api/v3/auth/token
Content-Type: application/x-www-form-urlencoded

username=teacher@school.edu&password=password
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer"
}
```

### Using Token

Include in headers:
```http
Authorization: Bearer <access_token>
```

## Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v3/auth/token` | Login and get access token |
| GET | `/api/v3/users/me` | Get current user info |

### Classes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v3/classes` | List all classes |
| POST | `/api/v3/classes` | Create new class |
| GET | `/api/v3/classes/{id}` | Get class by ID |
| PUT | `/api/v3/classes/{id}` | Update class |
| DELETE | `/api/v3/classes/{id}` | Delete class |

## Data Models

### Class

```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "subject": "string",
  "grade_level": "string",
  "students_count": 0,
  "created_by": "string",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

### User

```json
{
  "id": "string",
  "username": "string",
  "role": "string"
}
```

## Examples

### Create Class

```bash
curl -X POST "http://localhost:8000/api/v3/classes" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Physics 101",
    "description": "Introduction to Physics",
    "subject": "Physics",
    "grade_level": "9"
  }'
```

### Get All Classes

```bash
curl -X GET "http://localhost:8000/api/v3/classes" \
  -H "Authorization: Bearer <token>"
```

## Interactive Documentation

Visit http://localhost:8000/docs for Swagger UI documentation with interactive testing.