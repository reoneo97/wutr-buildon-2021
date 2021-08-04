import boto3 
from ..dynamodb import __create_item, __get_item
from loguru import logger
from botocore.exceptions import ClientError

from models.listings import ListingImageBbox



def get_image_bbox(key)->ListingImageBbox:
    
    item =  __get_item(key, table_name="images")
    logger.debug(f"Item Info: {item}")
    if not item:
        return None
    else:
        return item

def get_image_info(key):
    item =  __get_item(key, table_name="image_info")
    logger.debug(f"Item Info: {item}")
    if not item:
        return None
    else:
        return item