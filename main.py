from fastapi import FastAPI, Request
import aioredis
from datetime import datetime

from db import get_redis_session
from api import router


app = FastAPI()


app.include_router(router)


# register middleware for requests saving in Redis
@app.middleware("http")
async def save_request(
        request: Request,
        call_next
):
    redis = await get_redis_session()

    now = datetime.now().strftime("%m:%d:%H:%M:%S")
    method = request.method
    data = await request.body()

    await redis.hset("requests", now, f"{method} {data.decode()}")

    return await call_next(request)
