# wutr-buildon-2021
Team WUTR Repo for BuildOn 2021

Backend: FastAPI
Frontend: Vue.js

Test: Scripts to populate dataset

## Database Schemas

Database is using DynamoDB which is a No-SQL Database and relies on storing key-value pairs. There are 4 main tables
## Listing Table

Contains all the listing information

``` python
class Listing(BaseModel):
    name: str
    description: str
    price: Decimal
    for_sale: bool
    images: List[ListingImage] : # File path from S3
    user: str
    tags: List[str] = list()
    created_timestamp: str
    id:Optional[str] = None
```

## User Database
Contains User information

## Views Database
For each user contains the listings that the user has interacted with
- This is used for the recommendation system

## User_Feed Database
- Contains a List of ListingIds for each user. 
- The API will only pull items from this database and then remove them if the user has already clicked on the listing
- Adding additional Ids to this database will be done by AWS Lambda Functions

# Machine Learning

### Price Prediction Model

SentenceBert which uses Siamese neural networks to evaluate whether items are similar or not
- For our case we chose to use a smaller version of BERT DistilBert because of our smaller training size.
  - Faster inference and because our price dataset is smaller
  - Allows room for scaling up the model when we get more data


@article{DBLP:journals/corr/abs-1908-10084,
  author    = {Nils Reimers and
               Iryna Gurevych},
  title     = {Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks},
  journal   = {CoRR},
  volume    = {abs/1908.10084},
  year      = {2019},
  url       = {http://arxiv.org/abs/1908.10084},
  archivePrefix = {arXiv},
  eprint    = {1908.10084},
  timestamp = {Thu, 26 Nov 2020 12:13:54 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1908-10084.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}