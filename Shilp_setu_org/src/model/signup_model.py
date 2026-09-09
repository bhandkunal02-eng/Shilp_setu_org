from sqlalchemy import Column,Integer,String,Boolean,DateTime,BOOLEAN, Uuid
from src.DB.db import Base
from uuid import uuid4

class signupModel(Base):
    __tablename__="signup_table"
    User_id=Uuid(as_uuid=True, primary_key=True, default=Uuid.uuid4)
    email=Column(String)
    password=Column(String)
    confirm_password=Column(String)
    first_name=Column(String)
    last_name=Column(String)
    phone_number=Column(String)
    password_hash=Column(String)


