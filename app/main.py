from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# to handle the result (NLI pipelining) endpoint
from api import result
# to handle the sources (trustworthy) enpoint
from api import sources

# instance of fast api
app = FastAPI()

# to allow the frontend to talk
# NOTE: This is used for development only.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# inlcude the /analyze route
app.include_router(result.router)
# include the /sources route
app.include_router(sources.router)
