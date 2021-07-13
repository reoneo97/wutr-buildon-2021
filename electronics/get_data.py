import boto3
from loguru import logger
import uuid
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

TABLE_NAME = "views"
def parse_items(items):
    for entry in items:
        entry["engagement"] = int(entry["engagement"])
        entry["timestamp"] = int(entry["timestamp"])
    return items

def get_data():

    db = boto3.resource('dynamodb', region_name="us-east-1")
    table = db.Table(TABLE_NAME) 
    response = table.scan()
    items = parse_items(response['Items'])
    
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(parse_items(response['Items']))
    return items


items = get_data()
logger.info(items)