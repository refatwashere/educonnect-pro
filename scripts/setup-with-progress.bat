@echo off
setlocal enabledelayedexpansion

echo 🎓 EduConnect Pro - Setup with Progress
echo =======================================

:: Progress bar function
set "bar=████████████████████████████████████████"
set "spaces=                                        "

echo.
echo [1/4] 📦 Setting up Python Virtual Environment...
cd backend
python -m venv .venv
call .venv\Scripts\activate

echo.
echo [2/4] 📦 Installing Python Dependencies...
echo Progress: [          ] 0%%
pip install --progress-bar pretty --verbose fastapi==0.68.0
echo Progress: [██        ] 20%%
pip install --progress-bar pretty --verbose uvicorn==0.15.0
echo Progress: [████      ] 40%%
pip install --progress-bar pretty --verbose pydantic==1.10.12
echo Progress: [██████    ] 60%%
pip install --progress-bar pretty --verbose python-jose[cryptography]==3.3.0
echo Progress: [████████  ] 80%%
pip install --progress-bar pretty --verbose passlib[bcrypt]==1.7.4
echo Progress: [██████████] 100%%
cd ..

echo.
echo [3/4] 🌐 Installing Node.js Dependencies...
cd frontend
echo Progress: [          ] 0%% - Installing core packages...
npm install --progress=true --loglevel=info next@^14.0.0 react@^18.2.0 react-dom@^18.2.0
echo Progress: [███       ] 30%% - Installing UI libraries...
npm install --progress=true --loglevel=info tailwindcss@^3.3.0 autoprefixer@^10.4.0 postcss@^8.4.0
echo Progress: [██████    ] 60%% - Installing dev dependencies...
npm install --progress=true --loglevel=info --save-dev typescript@^5.2.0 @types/react@^18.2.0 @types/react-dom@^18.2.0
echo Progress: [█████████ ] 90%% - Installing remaining packages...
npm install --progress=true --loglevel=info eslint@^8.51.0 eslint-config-next@^14.0.0
echo Progress: [██████████] 100%%
cd ..

echo.
echo [4/4] ✅ Setup Complete!
echo.
echo 🚀 To start development:
echo   Backend:  cd backend ^&^& python start.py
echo   Frontend: cd frontend ^&^& npm run dev
echo.
echo 🔗 URLs:
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:8000
echo   API Docs: http://localhost:8000/docs
echo.
echo 🔑 Mock Login: teacher@school.edu / password
pause