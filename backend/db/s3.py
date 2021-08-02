import boto3
from botocore.exceptions import ClientError
import uuid
from loguru import logger
from PIL import Image
import io


# TODO: Store unsecure bucket links somewhere else
PHOTO_BUCKET = "wutr-images2"
REGION_NAME = "ap-southeast-1"
# TODO: Provide better exception handling


def upload_image_s3(image):
    filename = __generate_image_filename()
    file_ext = image.content_type.split("/")[1]
    filename = f'{filename}.{file_ext}'
    r = __upload_image(image, filename, PHOTO_BUCKET)
    if not r:
        return False
    return filename

def download_image_s3(filename) -> Image.Image or False:
    image = __download_image(filename,PHOTO_BUCKET)
    return image
def __generate_image_filename():
    return uuid.uuid1().hex

def __upload_image(image, file_name: str, bucket: str, object_name=None,):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3',region_name=REGION_NAME)

    try:
        response = s3_client.upload_fileobj(
            image.file, bucket, file_name,
            ExtraArgs={'ContentType': image.content_type}
        )
    except ClientError as e:
        logger.error(e)
        return None
    logger.info(f"Uploaded {file_name} successfully to S3")
    return True

def __download_image(file_name:str, bucket_name:str):

    # Upload the file
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    logger.info(f'key is {file_name}')
    try:
        image = bucket.Object(file_name)
        img_data = image.get().get('Body').read()
        return io.BytesIO(img_data)
    except ClientError as e:
        return None        
