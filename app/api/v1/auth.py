# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import models
from app.db import database
from app.core.redis_manager import redis_client
from app.core.security import (verify_password, create_access_token, 
    create_refresh_token, verify_and_refresh_token, get_current_user)

router = APIRouter()

@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.User).filter(models.User.email == request.username))
    user = result.scalars().first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    refresh_token = await create_refresh_token(data={"sub": user.email})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh")
async def refresh_token(refresh_token: str = Body(...)):
    return await verify_and_refresh_token(refresh_token)


@router.post("/logout")
async def logout(current_user: models.User = Depends(get_current_user)):
    await redis_client.delete(f"refresh_token:{current_user.email}")
    return {"message": "Logged out successfully"}
