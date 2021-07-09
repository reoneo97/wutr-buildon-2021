from typing import Optional
from pydantic import BaseModel

class UserKey(BaseModel):
    username: str
     
class User(UserKey):
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

