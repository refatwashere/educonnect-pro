@echo off
echo 🎓 EduConnect Pro - PNPM with Progress
echo =====================================

echo.
echo [1/3] 📦 Setting up Backend...
cd backend
python -m venv .venv
call .venv\Scripts\activate
pip install --progress-bar pretty -r requirements.txt
cd ..

echo.
echo [2/3] 🌐 Installing Frontend with PNPM (verbose)...
cd frontend
:: PNPM with progress and detailed output
pnpm install --reporter=default --progress=true --loglevel=info
cd ..

echo.
echo [3/3] ✅ Setup Complete!
echo.
echo 🚀 Commands:
echo   Backend:  cd backend ^&^& python start.py  
echo   Frontend: cd frontend ^&^& pnpm dev
echo.
pause