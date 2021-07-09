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
        logger.info("Listing table already present")

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
        logger.info("User Table created")
    except ClientError as e:
        logger.info("User table already present")
    # views_table = db.create_table(
    #     TableName='views',
    #     KeySchema=[
    #         {
    #             'AttributeName': 'username',
    #             'KeyType': 'HASH'
    #         },
    #         {
    #             'AttributeName': 'listing_id',
    #             'KeyType': 'HASH'
    #         }
    #     ],
    #     AttributeDefinitions=[
    #         {
    #             'AttributeName': 'username',
    #             'AttributeType': 'S'
    #         },
    #         {
    #             'AttributeName': 'listing_id',
    #             'AttributeType': 'S'
    #         },
    #     ],
    #     ProvisionedThroughput={
    #         'ReadCapacityUnits': 5,
    #         'WriteCapacityUnits': 5
    #     }
    # )
    # logger.info("Views Table created")
    return
def create_table_from_model(table_name,model):
    pass

if __name__ == "__main__":
    create_tables()