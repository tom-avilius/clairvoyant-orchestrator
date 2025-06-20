from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter()

NLI_URL = "http://localhost:8000/analyze"  # or your deployed NLI endpoint


class NewsInput(BaseModel):
    news: str


@router.post("/analyze")
async def analyze_news(payload: NewsInput):
    timeout = httpx.Timeout(20.0, connect=5.0)  # Increase timeout to 20s
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(NLI_URL, json={"news": payload.news})
        return response.json()  # send this back to Vue frontend
