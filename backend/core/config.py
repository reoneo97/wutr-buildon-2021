from pydantic import BaseModel

class ApplicationConfig(BaseModel):
    image_bucket_name: str
    model_bucket_name: str