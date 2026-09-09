from fastapi import APIRouter, File, UploadFile


media_route = APIRouter()


@media_route.get("/")
def root():
    return {"message": "Shilp Setu API is running"}

@media_route.post("/test_upload")
async def test_image_upload(file: UploadFile = File(...)):
    result = upload_image(
        file=file.file,
        file_name=file.filename,
    )