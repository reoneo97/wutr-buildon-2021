from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    display_name: str
    
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None