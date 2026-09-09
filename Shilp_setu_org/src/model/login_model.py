from sqlalchemy import Column,Integer,String,Boolean,DateTime,BOOLEAN
from src.DB.db import Base


class LoginModel(Base):
    __tablename__="login_table"
    email=Column(String)
    password=Column(String)
