from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_TYPE = 'postgresql'
USERNAME = 'postgres'
PASSWORD = '183139'
HOST = '127.0.0.1'
PORT = '5432'
DB = 'anticafe'

SQLALCHEMY_DATABASE_URL = f"{ DB_TYPE }://{ USERNAME }:{ PASSWORD }@{ HOST }:{ PORT }/{ DB }"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./demo.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
