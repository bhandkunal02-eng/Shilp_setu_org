from pydantic import BaseModel


class ImageResponse(BaseModel):
    id: int
    name: str
    url: str
