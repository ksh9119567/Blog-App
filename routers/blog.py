# routers/blog.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import models, schemas, database
from sqlalchemy.future import select

router = APIRouter(prefix="/blog", tags=["Blogs"])

# Dependency
async def get_db():
    db = database.AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()

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
