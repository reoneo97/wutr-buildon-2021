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