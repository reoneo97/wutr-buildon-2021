import boto3
from ..dynamodb import __create_item, __get_item, generate_id
from loguru import logger
from botocore.exceptions import ClientError
from models.views import UserView
from utils import get_unix_timestamp
TABLE_NAME = "views" #FIXME: Maybe change to user_history?


def add_view(username: str, listing_id: str, TABLE_NAME=TABLE_NAME):
    # TODO Might not want to keep engagment

    view_item = {
        "username":username,"listing_id":listing_id,
        "engagement":1, "timestamp":get_unix_timestamp()}

    __create_item(view_item,TABLE_NAME)
    logger.info(f'View created user:{username}, listing: {listing_id}')
    
def get_user_item_matrix(TABLE_NAME=TABLE_NAME):
    pass
