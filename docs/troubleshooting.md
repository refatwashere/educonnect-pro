# Troubleshooting Guide

Common issues and solutions for EduConnect Pro development.

## Backend Issues

### Python Virtual Environment

**Problem**: `python` command not found
**Solution**:
```bash
# Windows
py -m venv .venv
# Linux/Mac
python3 -m venv .venv
```

**Problem**: Virtual environment not activating
**Solution**:
```bash
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### Dependencies

**Problem**: `pip install` fails
**Solution**:
```bash
# Upgrade pip first
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Problem**: `bcrypt` installation fails on Windows
**Solution**:
```bash
# Install Visual C++ Build Tools or use pre-compiled wheel
pip install --only-binary=all bcrypt
```

### FastAPI Server

**Problem**: Port 8000 already in use
**Solution**:
```bash
# Use different port
uvicorn src.main:app --reload --port 8001
```

**Problem**: CORS errors from frontend
**Solution**: Add CORS middleware to `main.py`:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Frontend Issues

### Node.js and pnpm

**Problem**: `pnpm` command not found
**Solution**:
```bash
npm install -g pnpm
```

**Problem**: Node.js version incompatible
**Solution**:
```bash
# Check version
node --version
# Should be 18+ for Next.js 14
```

### Next.js Development

**Problem**: Port 3000 already in use
**Solution**:
```bash
# Use different port
pnpm dev -- --port 3001
```

**Problem**: TypeScript errors
**Solution**:
```bash
# Check TypeScript configuration
npx tsc --noEmit
```

**Problem**: Tailwind styles not working
**Solution**: Verify `tailwind.config.ts`:
```typescript
module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  // ...
}
```

## Authentication Issues

**Problem**: JWT token expired
**Solution**: Implement token refresh or re-login

**Problem**: 401 Unauthorized errors
**Solution**: Check token format:
```javascript
// Correct format
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

## Database Issues

**Problem**: Mock database resets on server restart
**Solution**: This is expected behavior in development. For persistence, implement proper database connection.

## Build Issues

### Backend Build

**Problem**: Import errors in production
**Solution**: Use absolute imports and check PYTHONPATH

### Frontend Build

**Problem**: Build fails with TypeScript errors
**Solution**:
```bash
# Fix TypeScript errors first
pnpm lint
pnpm build
```

**Problem**: Static export issues
**Solution**: Check `next.config.js` configuration

## Performance Issues

**Problem**: Slow API responses
**Solution**:
1. Add database indexing
2. Implement caching
3. Use pagination for large datasets

**Problem**: Large bundle size
**Solution**:
1. Use dynamic imports
2. Optimize images
3. Remove unused dependencies

## Development Environment

**Problem**: Hot reload not working
**Solution**:
```bash
# Backend
uvicorn src.main:app --reload

# Frontend
pnpm dev
```

**Problem**: Environment variables not loading
**Solution**: Create `.env.local` in frontend root:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Getting Help

1. Check this troubleshooting guide
2. Search GitHub issues
3. Check the [API documentation](./api-guide.md)
4. Create a new issue with:
   - Error message
   - Steps to reproduce
   - Environment details
   - Expected vs actual behavior