from sqlalchemy import Column,Integer,String,Boolean,DateTime,BOOLEAN, Uuid
from src.DB.db import Base
from uuid import uuid4

class profileModel(Base):
    __tablename__="profile_table"
    User_id=Uuid(as_uuid=True, primary_key=True, default=Uuid.uuid4)
    email=Column(String)
    password=Column(String)
    first_name=Column(String)
    last_name=Column(String)
    phone_number=Column(String)
    address=Column(String)
    profile_image=Column(String)
    artist_details=Column(String)
    gender=Column(String)


