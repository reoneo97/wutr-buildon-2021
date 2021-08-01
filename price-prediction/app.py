from sentence_transformers import SentenceTransformer, util
import random
import boto3
from loguru import logger
import pandas as pd
import numpy as np
import torch

REGION_NAME = "ap-southeast-1"


def __get_table(table_name):

    db = boto3.resource('dynamodb', region_name=REGION_NAME)
    return db.Table(table_name)


def load_model():
    # To add model weights file after fine-tuning
    model = SentenceTransformer('stsb-mpnet-base-v2', cache_folder="/tmp/")
    return model


def load_from_s3(filename, bucket="price-prediction-tensors"):
    s3 = boto3.resource('s3')
    # bucket = s3.Bucket(bucket)
    s3.meta.client.download_file(bucket, filename, "/tmp/" + filename)


def price_predict(product_name):
    # data = load_data()
    model = load_model()
    
    query_embed = model.encode(product_name, convert_to_tensor=True)
    # get txt and csv from s3 bucket

    df = load_data()
    tensor_tensor_reshaped = torch.stack(df["encoded"].tolist())
    logger.info(tensor_tensor_reshaped.shape)
    results= util.semantic_search(query_embed, tensor_tensor_reshaped, top_k=5)
    idxs = [i["corpus_id"] for i in results[0]]
    scores = [j["score"] for j in results[0]]

    product_list = df.iloc[idxs][["name", "price"]]
    product_list["score"] = scores

    # return weighted average of price
    score_sum = product_list["score"].sum()
    weighted_sum = 0
    for index, row in product_list.iterrows():
        weighted_sum += row['price'] * row['score'] / score_sum
        weighted_sum_returned = round(weighted_sum, 2)
    return weighted_sum_returned

def load_data():
    table = __get_table("price-info")
    response = table.scan()
    items = response['Items']
    while 'LastEvaluatedKey' in response:
        logger.debug(f"Last Key: {response['LastEvaluatedKey']}")
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])
    items = pd.DataFrame.from_dict(items)
    items["price"] = items["price"].apply(lambda x: float(x))
    items["encoded"] = items["encoded"].apply(
        lambda x: torch.from_numpy(np.frombuffer(bytes(x),dtype="float32"))
    )
    return items

def lambda_handler(event, context):
    input_text = event["product_name"]
    # try: 
    output_price = price_predict(input_text)
    response = {
        "statusCode": 200,
        "body": output_price
    }
    # except Exception as e:
    #     response = {
    #         "statusCode": 404,
    #         "body": 50 # e.message
    #     }

    return response
