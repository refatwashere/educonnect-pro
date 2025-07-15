#!/usr/bin/env python3
"""
EduConnect Pro Backend Startup Script
Run this to start the FastAPI development server
"""

import uvicorn
import os
import sys

if __name__ == "__main__":
    # Add the src directory to Python path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
    
    print("🚀 Starting EduConnect Pro Backend API...")
    print("📍 API will be available at: http://localhost:8000")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔑 Mock Login: teacher@school.edu / password")
    print("-" * 50)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["src"]
    )