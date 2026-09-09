from sqlalchemy import Column,Integer,String,Boolean,DateTime,BOOLEAN,Float
from src.DB.db import Base


class OrderModel(Base):
    __tablename__="Order_table"
    order_id=Column(Integer,primary_key=True)
    product_id=Column(Integer)
    product_name=Column(String)
    product_price=Column(Float)
    customer_info=Column(String)
    marketplace=Column(String)
    order_status=Column(String)
    order_date=Column(DateTime)