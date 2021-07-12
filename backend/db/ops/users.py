import boto3 
from ..dynamodb import __create_item, __get_item
from models.users import User, UserKey
from loguru import logger

TABLE_NAME = "users"
def get_user(key: UserKey)->User:

    return __get_item(key.dict(), table_name=TABLE_NAME)