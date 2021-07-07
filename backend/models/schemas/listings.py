from typing import Optional, Set
from pydantic import BaseModel


class Listing(BaseModel):
    name: str
    description: str
    price: float
    for_sale: bool
    tags: Set[str] = set()
    
class ListingInit(BaseModel):
    name: str
    