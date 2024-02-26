from fastapi import FastAPI
from routes.route import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello, NBKR!"}
