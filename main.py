# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
import models, database
from routers import blog


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create DB tables asynchronously using the async engine before the app starts
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield


app = FastAPI(title="FastAPI Blog", lifespan=lifespan)


app.include_router(blog.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Blog!"}
