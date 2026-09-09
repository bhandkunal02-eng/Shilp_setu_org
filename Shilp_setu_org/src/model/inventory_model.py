from sqlalchemy import Column,Integer,String,Boolean,DateTime,BOOLEAN, Uuid
from src.DB.db import Base
from uuid import uuid4

class InventoryModel(Base):
    __tablename__="inventory_table"

    inventory_id=Uuid(as_uuid=True, primary_key=True, default=Uuid.uuid4)
    product_id=Column(Integer)
    Quantity=Column(Integer)
    
