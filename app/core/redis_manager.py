# app/core/redis_manager.py
import redis.asyncio as redis
import os

# In production, load from .env
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

redis_client = redis.from_url(REDIS_URL, decode_responses=True)
