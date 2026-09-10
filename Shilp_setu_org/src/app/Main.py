from fastapi import FastAPI

from src.DB.db import Base, engine
from src.Routes.auth import auth_route
from src.Routes.orders import orders_Route
from src.Routes.product import product_route
from src.Routes.profile import profile_route
from src.Routes.media_route import router
from src.model.image_model import Image


app = FastAPI(
    title="Shilp Setu API",
    version="1.0.0",
)

app.include_router(router)
app.include_router(auth_route)
app.include_router(orders_Route)
app.include_router(product_route)
app.include_router(profile_route)

Base.metadata.create_all(bind=engine)