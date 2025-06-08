from fastapi import APIRouter, HTTPException
from app.models.schema import NewsQuery, AnalysisResult
from app.services import scraper, nlp, scoring

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResult)
async def analyze_news(query: NewsQuery):
    try:
        scraped_data = await scraper.get_articles(query.title)
        nlp_data = await nlp.analyze_text(scraped_data)
        score = await scoring.compute_score(nlp_data)
        
        return AnalysisResult(score=score, sources=scraped_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

