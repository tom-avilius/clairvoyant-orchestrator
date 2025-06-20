from fastapi import APIRouter
# to validate requests
from pydantic import BaseModel
# to make requests
import httpx

# instantiate router
router = APIRouter()

# the endpoint to make requests
# NOTE: This is for development only.
NLI_URL = "http://localhost:8000/analyze"  # or your deployed NLI endpoint


# the pydantic model
class NewsInput(BaseModel):
    news: str


# handle /analyze enpoint
@router.post("/analyze")
async def analyze_news(payload: NewsInput):
    """
    params
    payload: NewsInput => news: str
    The query or claim the user wishes to validate.
    """
    # set timeout
    # OPTIMIZE: The timeout may be too high..
    timeout = httpx.Timeout(20.0, connect=5.0)
    # make the request
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(NLI_URL, json={"news": payload.news})
        return response.json()  # send this back to Vue frontend
