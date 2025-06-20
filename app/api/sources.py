from fastapi import APIRouter
# to make requests
import httpx

# instantiate routes for modularity
router = APIRouter()

# the endpoint to make requests to.
# NOTE: This is for development only.
SOURCES_URL = "http://localhost:8000/sources"  # or your deployed NLI endpoint


# handle /sources endpoint
@router.get("/sources")
async def analyze_news(uuid: str):
    """
    params
    uuid: str
    The uuid sent to the user with the response of
    the analyze request.

    Sends the entailment news source and flags if it
    trustworthy.
    """
    # the timeout to wait for response
    timeout = httpx.Timeout(10.0, connect=5.0)
    # make the request
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.get(SOURCES_URL, params={"uuid": uuid})
        return response.json()  # return the response.
