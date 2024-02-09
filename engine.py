from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker
from sqlalchemy.orm import Session
from config import DBSettings

Base: DeclarativeBase = declarative_base()
settings = DBSettings()
engine = create_engine(settings.URL)
session = sessionmaker(engine, expire_on_commit=False)


def get_db() -> Session:
    db = session()
    try:
        yield db
    finally:
        db.close()
