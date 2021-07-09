from typing import Optional, Set, List, Union
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

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
    created_timestamp: str

class ListingCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    images: List[ListingImage]
    tags: List[str] = list()

class ListingDb(Listing):
    id: str
    created_timestamp: str # Override for putting into DB
