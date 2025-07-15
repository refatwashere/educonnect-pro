# Database Setup Guide

## 🗄️ Database Integration Overview

EduConnect Pro now supports both SQLite (development) and PostgreSQL (production via Supabase).

## 🚀 Quick Setup

### Local Development (SQLite)
```bash
cd backend
pip install -r requirements.txt
uvicorn src.main:app --reload
```
- Database auto-created as `educonnect.db`
- Default user: `teacher@school.edu` / `password`

### Production (Supabase PostgreSQL)

1. **Create Supabase Project**:
   - Visit https://supabase.com
   - Create new project
   - Note your connection details

2. **Get Connection String**:
   - Go to Settings → Database
   - Copy connection string

3. **Configure Environment**:
   ```bash
   # Create .env file from .env.example
   cp .env.example .env
   
   # Update DATABASE_URL in .env
   DATABASE_URL=postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres
   ```

## 🔧 Database Schema

### Tables Created Automatically:
- **users**: Authentication and user management
- **classes**: Class information and management

### Default Data:
- Default teacher account created on first run
- Username: `teacher@school.edu`
- Password: `password`

## 🧪 Testing Database

### Verify Setup:
1. Start backend: `uvicorn src.main:app --reload`
2. Visit: http://localhost:8000/docs
3. Test login endpoint with default credentials
4. Create a test class via API

### Manual Database Check:
```bash
# For SQLite
sqlite3 educonnect.db
.tables
SELECT * FROM users;
SELECT * FROM classes;
```

## 🔄 Database Operations

### Reset Database:
```bash
# Delete SQLite database
rm educonnect.db

# Restart server to recreate
uvicorn src.main:app --reload
```

### Backup Database:
```bash
# SQLite backup
cp educonnect.db educonnect_backup.db

# PostgreSQL backup (via Supabase dashboard)
```

## 🚨 Troubleshooting

**Issue**: Database connection errors
**Solution**: Check DATABASE_URL format and credentials

**Issue**: Tables not created
**Solution**: Restart server - tables auto-create on startup

**Issue**: Default user not created
**Solution**: Check logs for database write permissions