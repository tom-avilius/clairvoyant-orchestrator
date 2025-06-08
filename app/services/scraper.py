import httpx

async def get_articles(title: str) -> list:
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8001/scrape", json={"query": title})
        response.raise_for_status()
        return response.json()["articles"]

