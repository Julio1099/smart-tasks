from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        orm_mode = True

class BoardCreate(BaseModel):
    name: str
    is_public: Optional[bool] = False

class BoardOut(BaseModel):
    id: int
    name: str
    is_public: bool
    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = 'todo'

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    class Config:
        orm_mode = True 