from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from models.users import User, User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded",
        email="john@example.com",
        full_name="John Doe"
    )
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

# TODO: Change this to perform actual user validation
def get_fake_user() -> User:
    return User(
        username="jinbeblob",
        email="rasdsa@gmail.com",
        full_name="reo",
    )
async def get_user_id() -> str:
    user = get_fake_user()
    return user.username