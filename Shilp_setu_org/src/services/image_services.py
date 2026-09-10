import os

from dotenv import load_dotenv
from imagekitio import ImageKit

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY")
)


def upload_image(file, file_name):
    result = imagekit.files.upload(
        file=file,
        file_name=file_name,
        folder="/media"
    )

    return {
        "url": result.url,
        "file_name": result.name,
        "file_id": result.file_id,
    }