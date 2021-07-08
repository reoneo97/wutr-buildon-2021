from fastapi import File, UploadFile, APIRouter, Depends,HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import StreamingResponse,FileResponse,Response
from models.listings import Listing, ListingInit, ListingImage

from db.image import upload_image_s3, download_image_s3
from PIL import Image
from io import BytesIO
from loguru import logger

from api.dependencies.authentication import get_user_id
router = APIRouter()

@router.post("/create/1",response_model=ListingInit)
def create_listing(listing: ListingInit):
    results = {"listing":listing}
    
    return results
    

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