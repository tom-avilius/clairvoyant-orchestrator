from fastapi import FastAPI

app = FastAPI()


@app.get("/result")
async def hello():
    return {
        "msg": "Hello there!"
    }
