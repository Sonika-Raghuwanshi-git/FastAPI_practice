from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import User
from schemas import UserOut,UserCreate
from database import get_db
from hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/", response_model=UserOut)
def create_user(request:UserCreate, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)
    new_user = User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

