@echo off
echo 🎓 EduConnect Pro - Quick Setup
echo ===============================

echo.
echo 📦 Setting up Backend...
cd backend
python -m venv .venv
call .venv\Scripts\activate
pip install --no-cache-dir -r requirements.txt
cd ..

echo.
echo 🌐 Setting up Frontend (using npm)...
cd frontend
npm install --no-optional
cd ..

echo.
echo ✅ Quick Setup Complete!
echo.
echo 🚀 To start development:
echo   Backend:  cd backend ^&^& python start.py
echo   Frontend: cd frontend ^&^& npm run dev
echo.
echo 🔗 URLs:
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:8000
echo.
echo 🔑 Mock Login: teacher@school.edu / password
pause