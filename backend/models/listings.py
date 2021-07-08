from typing import Optional, Set
from pydantic import BaseModel


class ListingImage(BaseModel):
    filename: str

class Listing(BaseModel):
    name: str
    description: str
    price: float
    for_sale: bool
    tags: Set[str] = set()
    
class ListingInit(BaseModel):
    name: str
    image: ListingImage
    