from sqlalchemy.orm import Session
from .config.database import engine, SessionLocal, Base
from .models.database import User
from .services.auth import get_password_hash
import uuid

def create_tables():
    Base.metadata.create_all(bind=engine)

def create_default_user():
    db = SessionLocal()
    try:
        # Check if default user exists
        existing_user = db.query(User).filter(User.username == "teacher@school.edu").first()
        if not existing_user:
            default_user = User(
                id=str(uuid.uuid4()),
                username="teacher@school.edu",
                hashed_password=get_password_hash("password"),
                role="teacher"
            )
            db.add(default_user)
            db.commit()
            print("Default user created: teacher@school.edu / password")
    finally:
        db.close()

def init_database():
    create_tables()
    create_default_user()

if __name__ == "__main__":
    init_database()