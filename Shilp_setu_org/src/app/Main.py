from fastapi import FastAPI, File, UploadFile

import task
from src.media.service import upload_image

#from src.user.router import user_routes
#from src.task.router import task_routes
from src.Route.media_route import  media_route
from src.Routes.orders import orders_Route
from src.Routes.product import product_route
from src.Routes.profile import profile_route

app = FastAPI(
    title="Shilp Setu API",
    version="1.0.0",
)

app.include_router(media_route)
app.include_router(orders_Route)
app.include_router(product_route)
app.include_router(profile_route)
#app.include_router(user_routes)
#app.include_router(task_routes)