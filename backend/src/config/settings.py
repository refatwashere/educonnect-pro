import os
from typing import List

class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-super-secret-key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    CORS_ORIGINS: List[str] = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
    DATABASE_URL: str = os.getenv("DATABASE_URL", os.getenv("DATABASE_URL_SUPABASE", "sqlite:///./educonnect.db"))

settings = Settings()