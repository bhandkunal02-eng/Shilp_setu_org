from sqlalchemy import Column, Integer, String
from src.DB.db import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    file_id = Column(String, nullable=False)