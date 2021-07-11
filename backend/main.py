from typing import Optional

from fastapi import FastAPI
from api.api import router as api_router
app = FastAPI(root_path="/api/")
from loguru import logger

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app.include_router(api_router)
@app.get("/")
async def root():
    logger.info("accesssed root")
    return {"message": "Hello World"}