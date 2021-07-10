import boto3
from ..dynamodb import __get_item, __update_item, __batch_get_item
from loguru import logger

TABLE_NAME = "users_feed"


def remove_listing_from_feed(username: str, listing_id: str):
    user_key = {"username": username}
    item = __get_item(user_key, TABLE_NAME)
    logger.info(item)
    try:
        idx = item["feed"].index(listing_id)
    except ValueError:
        logger.error(f"Listing {listing_id} not found in feed")
        return
    exp = f"REMOVE feed[{idx}]"
    
    __update_item(user_key, TABLE_NAME,exp)
    logger.info("Item removed from feed ")

def get_user_feed(username:str):
    user_key = {"username": username}
    item = __get_item(user_key, TABLE_NAME)
    ids = item["feed"]
    keys = [{"id":idx} for idx in ids]
    logger.info(keys[0])
    #listings = [__get_item(key,"listings") for key in keys]
    db_response = __batch_get_item(keys,"listings")
    return db_response["Responses"]["listings"]
