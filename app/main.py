from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api import result
from api import sources

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(result.router)
app.include_router(sources.router)
