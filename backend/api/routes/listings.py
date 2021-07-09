from fastapi import File, UploadFile, APIRouter, Depends,HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import StreamingResponse,FileResponse,Response
from models.listings import *

from db.s3 import upload_image_s3, download_image_s3
from db.dynamodb import create_listing
from db.dynamodb import get_listing as get_listing_db
from PIL import Image
from io import BytesIO
from loguru import logger

from api.dependencies.authentication import get_user_id
router = APIRouter()

@router.post("/create/",response_model=ListingDb)
def post_listing(
    listing: ListingCreate, username: str = Depends(get_user_id)
    ):
    listing = Listing(user=username,**listing.dict())
    db_entry = create_listing(listing)
    logger.info(f"Post Request done for {db_entry.id}")
    return db_entry

@router.get("/{listing_id}",response_model=Listing)
def get_listing(listing_id:str):
    key = ListingKey(id = listing_id)
    listing = get_listing_db(key)
    logger.info(f"Get Request for {listing_id}")
    return listing
    

# TODO: Provide better information about the error 
@router.post("/img/upload_img/", response_model=ListingImage)
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

@router.get("/img/{img_id}")
async def download_image(
    img_id:str, 
    username:str = Depends(get_user_id),
    ):

    img_name = f"{username}/{img_id}"
    img = download_image_s3(img_name)

    return StreamingResponse(img,media_type="image/png")