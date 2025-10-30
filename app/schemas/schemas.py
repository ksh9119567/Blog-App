from pydantic import BaseModel, EmailStr
from typing import List, Optional
       
        
class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class BlogResponse(BlogBase):
    id: int
    user_id: Optional[int]
    
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    blogs: List[BlogResponse] = []

    class Config:
        orm_mode = True
 