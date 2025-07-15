@echo off
echo Starting EduConnect Pro Development Environment...
echo.

echo Starting Backend...
start "Backend" cmd /k "cd ..\backend && .venv\Scripts\activate && uvicorn src.main:app --reload"

timeout /t 3 /nobreak > nul

echo Starting Frontend...
start "Frontend" cmd /k "cd ..\frontend && pnpm dev"

echo.
echo Development servers starting...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
pause