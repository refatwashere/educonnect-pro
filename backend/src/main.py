from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .config.settings import settings
from .routes import auth, classes
from .models.user import UserInDB
from .services.user import get_current_user
from .database_init import init_database

app = FastAPI(
    title="EduConnect Pro Backend API",
    description="Unified API for educational institution management and timetable generation.",
    version="1.0.0"
)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_database()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v3")
app.include_router(classes.router, prefix="/api/v3")

@app.get("/")
async def read_root():
    return {"message": "Welcome to EduConnect Pro API v1!"}

@app.get("/api/v3/users/me")
async def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return {"username": current_user.username, "id": current_user.id, "role": current_user.role}