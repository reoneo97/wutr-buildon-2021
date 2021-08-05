import boto3 
from ..dynamodb import __create_item, __get_item, generate_id, __table_scan
from loguru import logger
from botocore.exceptions import ClientError
from models.listings import *

TABLE_NAME = "listings"
def create_listing(listing: ListingImage, table_name=TABLE_NAME):
    listing_db = ListingImageInfoDb(**listing.dict())
    try:
        __create_item(listing_db.dict(), table_name)
        return listing_db
    except ClientError as e:
        logger.exception("Unable to add to Client. Credentials Issue?")
        return False


def get_listing(key: ListingKey)->Listing:
    logger.info(key.dict())
    return __get_item(key.dict(), table_name=TABLE_NAME)



def get_user_listings(username):
    items = __table_scan("user",username,TABLE_NAME)
    logger.debug(items)
    return items
