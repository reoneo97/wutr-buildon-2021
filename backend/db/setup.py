import boto3
from botocore.exceptions import ClientError
from models.listings import ListingDb
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
    views_table = db.create_table(
        TableName='views',
        KeySchema=[
            {
                'AttributeName': 'view_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'username',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'view_id',
                'AttributeType': 'S'
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
    return

def create_table_from_model(table_name,model):
    pass

if __name__ == "__main__":
    create_tables()