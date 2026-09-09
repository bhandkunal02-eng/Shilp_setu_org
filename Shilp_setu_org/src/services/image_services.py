
from dotenv import load_dotenv
from imagekitio import ImageKit
import os
load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL"),
)

def upload_image(file, file_name):
    result = imagekit.files.upload(file=file, file_name=file_name, folder="/media")
    return {"url": result.url, "file_name": result.name, "file_id": result.file_id}