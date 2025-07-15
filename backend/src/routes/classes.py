from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from ..models.class_model import Class, ClassCreate, ClassUpdate
from ..models.user import UserInDB
from ..services.user import get_current_user
from ..config.database import get_db
from ..services.database import create_class, get_classes, get_class_by_id, update_class, delete_class

router = APIRouter(prefix="/classes", tags=["classes"])

@router.get("/", response_model=List[Class])
async def get_all_classes(current_user: UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    db_classes = get_classes(db)
    return [Class(
        id=cls.id,
        name=cls.name,
        description=cls.description,
        subject=cls.subject,
        grade_level=cls.grade_level,
        students_count=cls.students_count,
        created_by=cls.created_by,
        created_at=cls.created_at.isoformat(),
        updated_at=cls.updated_at.isoformat()
    ) for cls in db_classes]

@router.post("/", response_model=Class, status_code=201)
async def create_new_class(class_data: ClassCreate, current_user: UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    db_class = create_class(db, class_data, current_user.id)
    return Class(
        id=db_class.id,
        name=db_class.name,
        description=db_class.description,
        subject=db_class.subject,
        grade_level=db_class.grade_level,
        students_count=db_class.students_count,
        created_by=db_class.created_by,
        created_at=db_class.created_at.isoformat(),
        updated_at=db_class.updated_at.isoformat()
    )

@router.get("/{class_id}", response_model=Class)
async def get_class(class_id: str, current_user: UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    db_class = get_class_by_id(db, class_id)
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    return Class(
        id=db_class.id,
        name=db_class.name,
        description=db_class.description,
        subject=db_class.subject,
        grade_level=db_class.grade_level,
        students_count=db_class.students_count,
        created_by=db_class.created_by,
        created_at=db_class.created_at.isoformat(),
        updated_at=db_class.updated_at.isoformat()
    )

@router.put("/{class_id}", response_model=Class)
async def update_existing_class(class_id: str, class_update: ClassUpdate, current_user: UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    db_class = update_class(db, class_id, class_update)
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    return Class(
        id=db_class.id,
        name=db_class.name,
        description=db_class.description,
        subject=db_class.subject,
        grade_level=db_class.grade_level,
        students_count=db_class.students_count,
        created_by=db_class.created_by,
        created_at=db_class.created_at.isoformat(),
        updated_at=db_class.updated_at.isoformat()
    )

@router.delete("/{class_id}", status_code=204)
async def delete_existing_class(class_id: str, current_user: UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    success = delete_class(db, class_id)
    if not success:
        raise HTTPException(status_code=404, detail="Class not found")