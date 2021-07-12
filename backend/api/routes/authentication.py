from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, APIRouter, status
from db.ops import users as users_db
from loguru import logger
from models.users import User,UserKey,UserAuth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()


#TODO: Better Security https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
def get_user(username:str) -> User:
    user_key = UserKey(username=username)
    user = users_db.get_user(user_key)
    if user: 
        user = User(**user)
        return user
    else: 
        return HTTPException(425, "No User found")

def fake_decode_token(token):
    logger.debug(token)
    user = get_user(token)
    return user


def get_fake_user() -> User:
    return User(
        username="jinbeblob",
        email="rasdsa@gmail.com",
        full_name="reo",
    )

#FAKE HASH
def password_hash(pwd):
    return pwd
    
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
async def get_user_id() -> str:
    user = get_fake_user()
    return user.username

#TODO: 
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_key = UserKey(username=form_data.username)
    user_info = users_db.get_user(user_key)
    if not user_info:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserAuth(**user_info)
    password = password_hash(form_data.password)
    if password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}
    