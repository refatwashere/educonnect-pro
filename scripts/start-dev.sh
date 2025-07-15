#!/bin/bash

echo "Starting EduConnect Pro Development Environment..."
echo

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
if ! command_exists python3; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

if ! command_exists pnpm; then
    echo "Error: pnpm is not installed"
    exit 1
fi

# Start backend
echo "Starting Backend..."
cd ../backend
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload &
BACKEND_PID=$!

# Start frontend
echo "Starting Frontend..."
cd ../frontend
pnpm install
pnpm dev &
FRONTEND_PID=$!

echo
echo "Development servers started:"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo "API Docs: http://localhost:8000/docs"
echo
echo "Press Ctrl+C to stop all servers"

# Wait for interrupt
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait