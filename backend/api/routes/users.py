from fastapi import APIRouter, Depends
from models.users import User
router = APIRouter()
from api.dependencies.authentication import get_current_user

@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user