# routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.hash import bcrypt_sha256

from app.models import models 
from app.schemas import schemas 
from app.db.database import *

router = APIRouter()


@router.post("/", response_model=schemas.UserResponse)
async def create_user(request: schemas.UserCreate, db: AsyncSession= Depends(get_db)):
    # hash password before storing
    hashed_pwd = bcrypt_sha256.hash(request.password[:72])
    new_user = models.User(username=request.username, email=request.email, password=hashed_pwd)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@router.get("/", response_model=schemas.UserResponse)
async def get_user(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    users = result.scalars().first() 
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users
