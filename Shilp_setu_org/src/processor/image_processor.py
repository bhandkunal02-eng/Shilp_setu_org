from src.media.images import imagekit
from imagekitio.models.UploadFileRequestOption import UploadFileRequestOption
import  shutil
import os
import uuid
import tempfile


def upload_image(file, file_name: str):
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
    return imagekit.files.delete(file_id)
