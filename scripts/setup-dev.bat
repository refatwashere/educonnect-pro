@echo off
echo 🎓 EduConnect Pro - Development Setup
echo =====================================

echo.
echo 📦 Setting up Backend...
cd backend
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
cd ..

echo.
echo 🌐 Setting up Frontend...
cd frontend
call pnpm install
cd ..

echo.
echo ✅ Setup Complete!
echo.
echo 🚀 To start development:
echo   Backend:  cd backend && python start.py
echo   Frontend: cd frontend && pnpm run dev
echo.
echo 🔗 URLs:
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:8000
echo   API Docs: http://localhost:8000/docs
echo.
echo 🔑 Mock Login: teacher@school.edu / password
pause