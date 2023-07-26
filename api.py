from fastapi import APIRouter
from schemas import LoadOut
from main import get_redis_session

router = APIRouter()


@router.get("/load")
async def get_load():
    return LoadOut(

    )


@router.get("/records")
async def get_records():
    redis = await get_redis_session()

    all_records = await redis.hget("requests")
    records = {key.decode(): value.decode() for key, value in all_records.items()}

    return records


@router.post("/clear")
async def clear_load_records(
        time_range: str = None
):
    redis = await get_redis_session()

    if time_range:
        pass
    else:
        await redis.delete("requests")

    return {}

