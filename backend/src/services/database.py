from sqlalchemy.orm import Session
from ..models.database import User as DBUser, Class as DBClass
from ..models.user import UserCreate, UserInDB
from ..models.class_model import ClassCreate, ClassUpdate
from ..services.auth import get_password_hash
import uuid

def create_user(db: Session, user: UserCreate) -> DBUser:
    db_user = DBUser(
        id=str(uuid.uuid4()),
        username=user.username,
        hashed_password=get_password_hash(user.password),
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str) -> DBUser:
    return db.query(DBUser).filter(DBUser.username == username).first()

def create_class(db: Session, class_data: ClassCreate, user_id: str) -> DBClass:
    db_class = DBClass(
        id=str(uuid.uuid4()),
        name=class_data.name,
        description=class_data.description,
        subject=class_data.subject,
        grade_level=class_data.grade_level,
        created_by=user_id
    )
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_classes(db: Session):
    return db.query(DBClass).all()

def get_class_by_id(db: Session, class_id: str):
    return db.query(DBClass).filter(DBClass.id == class_id).first()

def update_class(db: Session, class_id: str, class_update: ClassUpdate):
    db_class = db.query(DBClass).filter(DBClass.id == class_id).first()
    if db_class:
        update_data = class_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_class, key, value)
        db.commit()
        db.refresh(db_class)
    return db_class

def delete_class(db: Session, class_id: str):
    db_class = db.query(DBClass).filter(DBClass.id == class_id).first()
    if db_class:
        db.delete(db_class)
        db.commit()
        return True
    return False