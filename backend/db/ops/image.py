import boto3 
from ..dynamodb import __create_item, __get_item
from loguru import logger
from botocore.exceptions import ClientError

from models.listings import ListingImage, ListingImageInfo
TABLE_NAME = "images"


def get_listing(key)->ListingImageInfo:
    
    item =  __get_item(key, table_name=TABLE_NAME)
    logger.debug(f"Item Info: {item}")
    if not item:
        return None
    else:
        return item