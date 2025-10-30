from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import models
from app.db.database import *
from app.schemas import schemas

router = APIRouter()


@router.post("/", response_model=schemas.BlogResponse)
async def create_blog(request: schemas.BlogCreate, db: AsyncSession = Depends(get_db)):
    new_blog = models.Blog(title=request.title, content=request.content)
    db.add(new_blog)
    await db.commit()
    await db.refresh(new_blog)
    return new_blog

@router.get("/", response_model=list[schemas.BlogResponse])
async def get_blog(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Blog))
    blogs = result.scalars().all()
    # blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blogs
