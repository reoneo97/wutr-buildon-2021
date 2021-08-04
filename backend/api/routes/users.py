from fastapi import APIRouter, Depends, HTTPException
from models.users import User
from models.listings import ListingFeed, ShortListing, ListingFeedShort
router = APIRouter()
from loguru import logger
from .authentication import get_current_user

from db.ops import users_feed as users_feed_db
from db.ops import listings as listing_db


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/feed",response_model = ListingFeedShort)
async def get_user_feed(
    current_user: User = Depends(get_current_user),limit:int =20, 
    ):
    """Get the User Feed. Reads in a List of Ids stored on DynamoDb and then
    displays the information
    """
    username = current_user.username
    listings = users_feed_db.get_user_feed(username)
    logger.debug(listings)
    if not listings:
        raise HTTPException(423,"Listing Feed for User Not Found (Check RecSys?)")
    return {"listings":listings[:limit],"count":len(listings[:limit])}

@router.get("/my_listings",response_model=ListingFeedShort)
async def get_user_listings(
    current_user: User = Depends(get_current_user), limit:int =20):
    """
    Gets all postings from the user and returns maximum of 20 of them 
    """
    my_username = current_user.username
    my_listings = listing_db.get_user_listings(my_username)
    return {"listings":my_listings[:limit],"count":len(my_listings)}

