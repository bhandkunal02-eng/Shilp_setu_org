from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()


Base = declarative_base()
engine = create_engine(url=os.getenv("DB_CONNECTION"))
LocalSession = sessionmaker(bind=engine)


def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()
