import boto3
import pandas as pd
from loguru import logger
from decimal import Decimal

from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import torch

TABLE_NAME = "price-info"
REGION_NAME="ap-southeast-1"

model = SentenceTransformer('stsb-mpnet-base-v2', cache_folder="/tmp/")

def __get_table(table_name):

    db = boto3.resource('dynamodb', region_name=REGION_NAME)
    return db.Table(table_name)


def load_s3(filename, bucket="price-prediction-tensors"):
    s3 = boto3.client('s3')
    s3.upload_file(filename, bucket, filename)


def load_data_to_db(filename):
    df = pd.read_csv(filename)
    df = df.loc[:,["id","name","price"]]
    df.to_csv("search_embed.csv", index=False)
    load_s3("search_embed.csv")

    df["price"] = df["price"].apply(lambda x:round(Decimal(x),2))
    
    # save to csv file in s3 bucket
    search_names = df["name"].tolist()
    search_embed = model.encode(search_names, convert_to_tensor=True)
    arr = search_embed.cpu().numpy()
    byte_list = [vec.tobytes() for vec in arr]
    df["encoded"] = byte_list
    # save to dynamodb
    df_data = df.to_dict(orient="records")
    table = __get_table("price-info")

    with table.batch_writer() as writer:
        for item in df_data:
            writer.put_item(Item=item)
    logger.info("Data loaded")
    return arr


def truncateTable(tableName):
    table = __get_table(tableName)
    
    # Get table keys
    tableKeyNames = [key.get("AttributeName") for key in table.key_schema]

    # Only retrieve the keys for each item in the table (minimize data transfer)
    ProjectionExpression = ", ".join(tableKeyNames)
    
    response = table.scan(ProjectionExpression=ProjectionExpression)
    data = response.get('Items')
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(
            ProjectionExpression=ProjectionExpression, 
            ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    with table.batch_writer() as batch:
        for each in data:
            batch.delete_item(
                Key={key: each[key] for key in tableKeyNames}
            )
