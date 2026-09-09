from sqlalchemy import Column, Float,Integer,String,Boolean,DateTime,BOOLEAN
from src.DB.db import Base


class ProductModel(Base):
    __tablename__="product_table"
    product_id=Column(Integer,primary_key=True)
    product_name=Column(String)
    product_name=Column(String)
    description=Column(String)
    description_url=Column(String)
    product_price=Column(Float)
    Category=Column(String)
    Quantity=Column(Integer)
    product_image=Column(String)
    listing_date=Column(DateTime)

