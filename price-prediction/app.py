from sentence_transformers import SentenceTransformer, util
import random
import boto3
from loguru import logger
import pandas as pd
import torch

REGION_NAME = "ap-southeast-1"


def __get_table(table_name):

    db = boto3.resource('dynamodb', region_name=REGION_NAME)
    return db.Table(table_name)


def load_model():
    # To add model weights file after fine-tuning
    model = SentenceTransformer('stsb-mpnet-base-v2', cache_folder="/tmp/")
    return model


def price_predict(product_name):
    data = load_data()
    model = load_model()
    
    query_embed = model.encode(product_name, convert_to_tensor=True)
    search_names = data["name"].tolist()
    search_embed = model.encode(search_names, convert_to_tensor=True)
<<<<<<< Updated upstream

=======
    cos_scores = util.pytorch_cos_sim(query_embed, corpus_embed)[0]
    top_results = torch.topk(cos_scores, k=5)

    print("\n\n======================\n\n")
    print("Query:", query)
    print("\nTop 5 most similar sentences in corpus:")

    for score, idx in zip(top_results[0], top_results[1]):
        print(corpus[idx], "(Score: {:.4f})".format(score))
>>>>>>> Stashed changes
    results= util.semantic_search(query_embed,search_embed,top_k=5)
    idxs = [i["corpus_id"] for i in results[0]]
    
    return data.iloc[idxs][["name","price"]]

def load_data():
    table = __get_table("price-info")
    response = table.scan()
    items = response['Items']
    while 'LastEvaluatedKey' in response:
        logger.debug(f"Last Key: {response['LastEvaluatedKey']}")
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])
    items = pd.DataFrame.from_dict(items)
    return items


print(price_predict("samsung galaxy"))
