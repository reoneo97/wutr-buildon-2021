import boto3 
from ..dynamodb import __create_item, __get_item, generate_id
from loguru import logger
from botocore.exceptions import ClientError

TABLE_NAME = "views"
def add_view(username:str , listing_id:str,TABLE_NAME = TABLE_NAME):
    pass

def get_user_item_matrix(TABLE_NAME = TABLE_NAME):
    pass
