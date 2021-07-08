from fastapi import APIRouter
from .routes import listings, users

router = APIRouter()

router.include_router(listings.router, prefix="/listings")
router.include_router(users.router, prefix="/users")