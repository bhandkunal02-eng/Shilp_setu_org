import os

from dotenv import load_dotenv
from imagekitio import ImageKit

load_dotenv()

private_key = os.getenv("IMAGEKIT_PRIVATE_KEY")
if not private_key:
    raise RuntimeError("IMAGEKIT_PRIVATE_KEY is not configured")

imagekit = ImageKit(private_key=private_key)


def upload_image(file: bytes, file_name: str) -> dict[str, str]:
    """Upload image bytes to ImageKit and return model-ready fields."""
    result = imagekit.files.upload(
        file=file,
        file_name=file_name,
        folder="/media",
    )

    return {
        "url": result.url,
        "file_name": result.name,
        "file_id": result.file_id,
    }


def delete_image(file_id: str):
    """Delete an image from ImageKit by its file ID."""
    return imagekit.files.delete(file_id)