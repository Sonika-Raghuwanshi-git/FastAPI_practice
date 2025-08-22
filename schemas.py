from pydantic import BaseModel
from typing import List, Optional

# ---------- Blog -----------
class BlogBase(BaseModel):
    title: str
    body: str
    published: bool = True

class BlogCreate(BlogBase):
    pass

class BlogOut(BlogBase):
    id: int
    class Config:
        from_attributes = True


# ---------- User -----------
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    blogs: List[BlogOut] = []
    class Config:
        from_attributes = True
