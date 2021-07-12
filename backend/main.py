from typing import Optional

from fastapi import FastAPI
from api.api import router as api_router
app = FastAPI()
from loguru import logger
from api.routes.authentication import get_current_user, get_fake_user


app.include_router(api_router)
@app.get("/")
async def root():
    logger.info("accesssed root")
    return {"message": "Hello World"}

app.dependency_overrides[get_current_user] = get_fake_user