from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Fake News Gateway API")
app.include_router(router)

