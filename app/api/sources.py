from fastapi import APIRouter
import httpx

router = APIRouter()

SOURCES_URL = "http://localhost:8000/sources"  # or your deployed NLI endpoint


@router.get("/sources")
async def analyze_news(uuid: str):
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.get(SOURCES_URL, params={"uuid": uuid})
        return response.json()
