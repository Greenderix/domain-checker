from fastapi import APIRouter
from fastapi import HTTPException

from app.models import Visit
from database.database import insert_links, get_visited_domains

router = APIRouter()


@router.get("/visited_domains")
async def visited_domains(from_time: int, to_time: int):
    domains = get_visited_domains(from_time, to_time)
    return {"domains": domains, "status": "ok"}


@router.post("/visited_links")
async def visited_links(visit: Visit):
    insert_links(visit.links)
    return {"status": "ok"}
