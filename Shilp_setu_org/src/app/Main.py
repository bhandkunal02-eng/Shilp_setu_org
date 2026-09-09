from fastapi import FastAPI, File, UploadFile

import task
from src.media.service import upload_image

from src.user.router import user_routes
from src.task.router import task_routes
from src.media.media_route import  media_route

app = FastAPI(
    title="Shilp Setu API",
    version="1.0.0",
)

app.include_router(media_route)
app.include_router(user_routes)
app.include_router(task_routes)