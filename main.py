from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from db import Base, engine, get_db
from routers import authentication_router
from models import Banner
from routers import *


app = FastAPI(title='ART-BAZAAR')
app.mount('/uploads', StaticFiles(directory='uploads'), name='uploads')

Base.metadata.create_all(engine)
app.include_router(banner_router)
app.include_router(qa_router)
app.include_router(authentication_router)