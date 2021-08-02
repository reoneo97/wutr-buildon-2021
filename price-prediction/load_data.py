import boto3
import pandas as pd
from loguru import logger
from decimal import Decimal
TABLE_NAME = "price-info"
REGION_NAME="ap-southeast-1"

def __get_table(table_name):

    db = boto3.resource('dynamodb', region_name=REGION_NAME)
    return db.Table(table_name)


def load_data(filename):
    df = pd.read_csv(filename)
    df = df.loc[:,["id","name","price"]]

    df["price"] = df["price"].apply(lambda x:round(Decimal(x),2))
    df_data=df.to_dict(orient="records")
    logger.debug(df_data)
    table = __get_table(TABLE_NAME)

    with table.batch_writer() as writer:
        for item in df_data:
            writer.put_item(Item=item)
    logger.info("Data loaded")
load_data("data/electronics_products.csv")