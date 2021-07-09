import boto3
from loguru import logger
import uuid
from models.listings import Listing, ListingImage, ListingKey, ListingDb

# TODO Put this as decorator?


def get_table(table_name):
    db = boto3.resource('dynamodb')
    return db.Table(table_name)


def create_listing(listing: Listing, table_name="listings"):
    idx = generate_id()
    listing_db = ListingDb(id=idx, **listing.dict())
    __create_item(listing_db.dict(), table_name)
    return listing_db


def get_listing(key: ListingKey):
    return __get_item(key.dict(), table_name="listings")


def __create_item(item, table_name):
    table = get_table(table_name)
    table.put_item(
        Item=item
    )
    logger.info(f'Item placed in {table_name} successfully')


def __get_item(item_key, table_name):
    table = get_table(table_name)
    response = table.get_item(
        Key=item_key
    )
    return response["Item"]


def generate_id():
    return uuid.uuid1().hex
