from typing import Optional, Set, List, Union
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class ListingKey(BaseModel):
    id: str

class ListingImageBox(BaseModel):
    cls: Optional[str] = None
    x: int
    y: int
    w: int
    h: int

class ListingInfo(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    tags: List[str] = list()  
    bbox: ListingImageBox  

class ImageName(BaseModel):
    id: str
    filename:str

class ListingImageBbox(BaseModel):
    filename: str
    bbox: List[ListingImageBox]
    bbox_len: int

class ListingImageInfoDb(BaseModel):
    id:str
    filename:str
    listings: List[ListingInfo]
    user: str
    created_timestamp: str

class ListingImage(BaseModel):
    id:str
    filename: str
    listings: List[ListingInfo]
    user: str

class ListingImageCreate(BaseModel):

    filename:str
    listings: List[ListingInfo]

class Listing(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    image: str
    user: str
    tags: List[str] = list()
    created_timestamp: str
    id:Optional[str] = None


class ListingDB(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    image: str
    user: str
    tags: List[str] = list()
    created_timestamp: str
    id:Optional[str] = None

class ListingFeed(BaseModel):
    """
    List of Listings and the count
    """
    listings: List[Listing]
    count: Optional[int]

class ListingIdFeed(BaseModel):
    images: List[str]
    count: Optional[int]

class ShortListing(BaseModel):
    id: str
    image: str

class ListingFeedShort(BaseModel):
    listings:List[ShortListing]
    count: Optional[int]
