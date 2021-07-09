from typing import Optional, Set, List
from pydantic import BaseModel
from decimal import Decimal


class ListingKey(BaseModel):
    id: str


class ListingImage(BaseModel):
    filename: str


class Listing(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    images: List[ListingImage]
    user: str
    tags: List[str] = list()

class ListingCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    images: List[ListingImage]
    tags: List[str] = list()

class ListingDb(Listing):
    id: str
