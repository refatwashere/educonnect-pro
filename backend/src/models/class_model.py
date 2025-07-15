from pydantic import BaseModel
from typing import Optional

class ClassBase(BaseModel):
    name: str
    description: Optional[str] = None
    subject: Optional[str] = None
    grade_level: Optional[str] = None

class ClassCreate(ClassBase):
    pass

class ClassUpdate(ClassBase):
    name: Optional[str] = None

class Class(ClassBase):
    id: str
    students_count: int = 0
    created_by: str
    created_at: str
    updated_at: str

    model_config = {"from_attributes": True}