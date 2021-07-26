from typing import Optional, Set, List, Union
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class ListingKey(BaseModel):
    id: str

class ListingImageBox(BaseModel):
    cls: str
    x: int
    y: int
    w: int
    h: int

class ListingImage(BaseModel):
    filename: str

class ListingImageInfo(ListingImage):
    boxes: List[ListingImageBox]


class Listing(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    images: List[ListingImage]
    user: str
    tags: List[str] = list()
    created_timestamp: str
    id:Optional[str] = None

class ListingCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    images: List[ListingImage]
    tags: List[str] = list()

class ListingFeed(BaseModel):
    """
    List of Listings and the count
    """
    listings: List[Listing]
    count: Optional[int]

class ListingIdFeed(BaseModel):
    ids: List[ListingKey]
    count: Optional[int]

