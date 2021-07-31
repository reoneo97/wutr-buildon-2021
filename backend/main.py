from typing import Optional
from fastapi import FastAPI
from api.api import router as api_router
from loguru import logger
from api.routes.authentication import get_current_user, get_fake_user, get_current_username
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "https://localhost:80",
    "http://localhost:80",
    "http://buildonapp-env.eba-jy7d9spr.ap-southeast-1.elasticbeanstalk.com",
    "https://buildonapp-env.eba-jy7d9spr.ap-southeast-1.elasticbeanstalk.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
@app.get("/")
async def root():
    logger.info("accesssed root")
    return {"message": "Hello World"}

def test_user():
    return "test_user"

app.dependency_overrides[get_current_user] = get_fake_user
app.dependency_overrides[get_current_username] = test_user