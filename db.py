from aioredis import Redis
import aioredis


async def get_redis_session() -> Redis:
    return await aioredis.create_redis_pool("redis://localhost")
