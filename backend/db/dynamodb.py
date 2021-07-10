import boto3
from loguru import logger
import uuid
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

# TODO Put this as decorator?
# Perform generic functions 

def __get_table(table_name):

    db = boto3.resource('dynamodb',region_name="us-east-1")
    return db.Table(table_name)

def __create_item(item, table_name):
    table = __get_table(table_name)
    table.put_item(
        Item=item
    )
    logger.info(f'Item placed in {table_name} successfully')


def __get_item(item_key, table_name):
    table = __get_table(table_name)
    response = table.get_item(
        Key=item_key
    )
    if "Item" not in response.keys():
        return None
    return response["Item"]

def __table_query(key,value,table_name):
    pass

def __table_scan(attr,value,table_name):
    table = __get_table(table_name)
    logger.debug([attr,value,table_name])
    response = table.scan(
        FilterExpression=Attr(attr).eq(value)
    )
    return response["Items"]

def generate_id():
    return uuid.uuid1().hex
