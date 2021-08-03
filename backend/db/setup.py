import boto3
from botocore.exceptions import ClientError
from loguru import logger
import uuid


db = boto3.resource("dynamodb")

def create_tables():
    try:
        listing_table = db.create_table(
            TableName = 'listings',
            KeySchema=[
                {
                    "AttributeName":'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        logger.info("Listing Table created")
    except ClientError as e:
        logger.warning("Listing table already present")

    try:    
        user_table = db.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        logger.debug("User Table created")
    except ClientError as e:
        logger.warning("User table already present")
    try:    
        feed_table = db.create_table(
            TableName='users_feed',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        logger.debug("User Feed Table created")
    except ClientError as e:
        logger.warning("User feed table already present")
    try:
        views_table = db.create_table(
            TableName='views',
            KeySchema=[
                {
                    'AttributeName': 'timestamp',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'username',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'timestamp',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        logger.debug("Views Table created")
    except ClientError as e:
        logger.warning("Views table already present")
    try:
        images_table = db.create_table(
            TableName='image_bbox',
            KeySchema=[
                {
                    'AttributeName': 'filename',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'filename',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        logger.debug("Images Table created")
    except ClientError as e:
        logger.warning("Images table already present")
    try:
        images_table = db.create_table(
            TableName='image_info',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        logger.debug("Images Table created")
    except ClientError as e:
        logger.warning("Images table already present")
    return

def create_table_from_model(table_name,model):
    pass

if __name__ == "__main__":
    create_tables()