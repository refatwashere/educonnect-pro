# Getting Started with EduConnect Pro

This guide will help you set up EduConnect Pro for development.

## Prerequisites

- **Node.js** 18+ and **pnpm**
- **Python** 3.8+
- **Git**

## Quick Setup

### 1. Clone and Setup

```bash
git clone <repository-url>
cd educonnect-pro
```

### 2. Automated Setup

```bash
# Windows
scripts\start-dev.bat

# Linux/Mac
chmod +x scripts/start-dev.sh
scripts/start-dev.sh
```

### 3. Manual Setup (Alternative)

**Backend:**
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

**Frontend:**
```bash
cd frontend
pnpm install
pnpm dev
```

## Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Default Credentials

- **Username**: teacher@school.edu
- **Password**: password

## Project Structure

```
educonnect-pro/
├── backend/src/
│   ├── models/          # Data models
│   ├── routes/          # API endpoints
│   ├── services/        # Business logic
│   ├── config/          # Settings
│   └── main.py          # FastAPI app
├── frontend/src/
│   ├── app/             # Next.js pages
│   └── shared/          # Shared types
├── shared/              # Project-wide types
├── scripts/             # Development scripts
└── docs/                # Documentation
```

## Verification Steps

1. **Backend Health Check**: Visit http://localhost:8000
2. **API Documentation**: Visit http://localhost:8000/docs
3. **Frontend**: Visit http://localhost:3000
4. **Login Test**: Use default credentials to access /classes

## Next Steps

1. Read the [API Guide](./api-guide.md) to understand the backend
2. Check the [Frontend Guide](./frontend-guide.md) for UI development
3. See [Contributing](./contributing.md) to start contributing

## Common Issues

- **Port conflicts**: Change ports in start scripts if needed
- **Python version**: Ensure Python 3.8+ is installed
- **Node.js version**: Ensure Node.js 18+ is installed
- **Dependencies**: Run `pip install -r requirements.txt` and `pnpm install`

For more issues, see [Troubleshooting](./troubleshooting.md).