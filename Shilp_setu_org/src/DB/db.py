from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()


Base = declarative_base()
database_url = os.getenv("DB_CONNECTION")
if database_url and database_url.startswith("sqlite+aiosqlite://"):
    database_url = database_url.replace("sqlite+aiosqlite://", "sqlite://", 1)

if not database_url:
    raise RuntimeError("DB_CONNECTION is not configured")

engine = create_engine(url=database_url)
LocalSession = sessionmaker(bind=engine)


def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()
