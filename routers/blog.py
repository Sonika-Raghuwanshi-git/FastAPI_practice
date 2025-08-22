from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
# from  import models, schemas, database
from models import Blog
from schemas import BlogOut, BlogCreate
from typing import List
from database import get_db

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.post("/", response_model= BlogOut)
def create(request: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(title=request.title, body=request.body, published=request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/", response_model=List[BlogOut])
def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@router.get("/{id}", response_model=BlogOut)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog

