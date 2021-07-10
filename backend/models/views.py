from pydantic import BaseModel

class UserView(BaseModel):
    timestamp: int
    user: str
    listing_id: str
    engagement: int