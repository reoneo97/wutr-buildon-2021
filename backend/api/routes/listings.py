from fastapi import File, UploadFile, APIRouter, Depends,HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import StreamingResponse,FileResponse,Response
from models.listings import *

from db.s3 import upload_image_s3, download_image_s3
from db.ops import listings as listing_db
from PIL import Image
from io import BytesIO
from loguru import logger
from .utils import get_current_timestamp
from api.dependencies.authentication import get_user_id
router = APIRouter()

# TODO: Add more async await commands to make the application faster

@router.post("/create",response_model=Listing)
def post_listing(
    listing: ListingCreate, username: str = Depends(get_user_id)
    )-> Listing:
    """
    Creates a listing object given certain parameters. 
    The input will only take in the necessary attributes of the object and add
    in the other required parameters such as username, timestamp and listing id
    """
    listing = Listing(
        user=username, created_timestamp = get_current_timestamp(),
        **listing.dict())
    db_entry = listing_db.create_listing(listing)
    logger.info(f"Post Request done for {db_entry.id}")
    return db_entry

#TODO: Should this end point return the images as well?
@router.get("/{listing_id}",response_model=Listing)
def get_listing(listing_id:str):
    key = ListingKey(id = listing_id)
    listing = listing_db.get_listing(key)
    
    #TODO: Update View Table - Store history of user views 
    if not listing:
        raise HTTPException(423,detail="Listing cannot be found")
    logger.info(f"Get Request for {listing_id}")

    return listing
    
@router.put("/{listing_id}",response_model=Listing)
def update_listing(listing_id:str):
    return {424:"Not Implemented"}

@router.get("/search")
async def search_listing(search_key: str):
    return {424:"Not Implemented"}

# TODO: Provide better information about the error 
@router.post("/img/upload_img", response_model=ListingImage)
async def upload_image(
    username: str = Depends(get_user_id),
    file: UploadFile = File(...),
    ) -> ListingImage:
    if file.content_type.split("/")[0] != "image":
        raise HTTPException(422,detail="Input image must either be .png or .jpg")
        return
    logger.info(username)
    filename = upload_image_s3(username, file)
    response = {"filename":filename}
    return response

@router.get("/img/{img_id}",)
async def download_image(
    img_id:str, 
    username:str = Depends(get_user_id),
    ):

    img_name = f"{username}/{img_id}"
    img = download_image_s3(img_name)
    if not img:
        raise HTTPException(423,detail="Image cannot be found")
    return StreamingResponse(img,media_type="image/png")

