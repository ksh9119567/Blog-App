from fastapi import APIRouter

from app.api.v1 import (
    blog,
    user,
)

# Root Router
api_router = APIRouter(prefix="/api")

# Include Individual Routers
api_router.include_router(blog.router, prefix="/blogs", tags=["Blogs"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
