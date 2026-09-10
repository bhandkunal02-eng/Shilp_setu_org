from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from src.DB.db import get_db
from src.controler.image_controler import save_image
from src.schema.schema_image import ImageResponse

router = APIRouter(prefix="/images")

@router.post("/upload")
async def upload(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
) -> ImageResponse:
    image = save_image(db, file.file, file.filename)
    return ImageResponse(id=image.id, name=image.name, url=image.url)