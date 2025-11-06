from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

from app.models import models
from app.db.database import *
from app.schemas import schemas
from app.core.security import get_current_user, get_current_admin_user

router = APIRouter()


# POST API
@router.post("/", response_model=schemas.BlogResponse)
async def create_blog(request: schemas.BlogCreate, 
                      db: AsyncSession = Depends(get_db), 
                      current_user: models.User = Depends(get_current_user)):
    new_blog = models.Blog(title=request.title, content=request.content, user_id=current_user.id)
    db.add(new_blog)
    await db.commit()
    await db.refresh(new_blog)
    return new_blog


# GET API
@router.get("/", response_model=list[schemas.BlogResponse])
async def get_user_blog(db: AsyncSession = Depends(get_db),
                        current_user: models.User = Depends(get_current_user)):
    result = await db.execute(select(models.Blog).filter(models.Blog.user_id == current_user.id))
    blogs = result.scalars().all()
    if not blogs:
        raise HTTPException(status_code=404, detail="Blogs not found")
    return blogs


@router.get("/admin/all", response_model=list[schemas.BlogResponse])
async def get_all_blog(db: AsyncSession = Depends(get_db),
                       admin_user: models.User = Depends(get_current_admin_user)):
    result = await db.execute(select(models.Blog))
    blogs = result.scalars().all()
    if not blogs:
        raise HTTPException(status_code=404, detail="Blogs not found")
    return blogs


# POST API
@router.put("/{blog_id}", response_model=schemas.BlogResponse)
async def update_blog(blog_id: int,
                      request: schemas.BlogCreate,
                      db: AsyncSession = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)):
    if current_user.is_admin():
        result = await db.execute(select(models.Blog).filter(models.Blog.id == blog_id))
    else:
        result = await db.execute(select(models.Blog).filter(models.Blog.id == blog_id,
                                                             models.Blog.user_id == current_user.id))
        
    blog = result.scalars().first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found or not authorized")
    blog.title = request.title
    blog.content = request.content
    await db.commit()
    await db.refresh(blog)
    return blog


# DELETE API
@router.delete("/{blog_id}")
async def delete_blog(blog_id: int,
                      db: AsyncSession = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)):
    if current_user.is_admin():
        result = await db.execute(select(models.Blog).filter(models.Blog.id == blog_id))
    else:
        result = await db.execute(select(models.Blog).filter(
                models.Blog.id == blog_id,
                models.Blog.user_id == current_user.id)
    )
    blog = result.scalars().first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found or not authorized")
    await db.delete(blog)
    await db.commit()
    return "Blog deleted successfully"


@router.delete("/admin/all")
async def delete_all_blogs(db: AsyncSession = Depends(get_db),
                           admin_user: models.User = Depends(get_current_admin_user)):
    await db.execute(delete(models.Blog))
    await db.commit()
    return "Blogs deleted successfully"