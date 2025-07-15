@echo off
echo 🎓 EduConnect Pro - Manual Start
echo ================================

echo.
echo Starting Backend...
start cmd /k "cd backend && .venv\Scripts\activate && python start.py"

echo.
echo Starting Frontend...
start cmd /k "cd frontend && npm run dev"

echo.
echo ✅ Both services starting in separate windows
echo.
echo 🔗 URLs:
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:8000
echo.
pause