from sqlalchemy import *
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime




class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Banner(Base):
    __tablename__ = 'banner'
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    
    
class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    text = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    answer = relationship('Answer', back_populates='question')
    

class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    question = relationship('Question', back_populates='answer')
    


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, index=True)
    name_tm = Column(String)
    name_ru = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name_tm = Column(String)
    name_ru = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    product = relationship('Product', back_populates='category')



class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    name_tm = Column(String)
    name_ru = Column(String)
    description_tm = Column(String)
    description_ru = Column(String)
    price = Column(Float)
    code = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    category    = relationship('Category', back_populates='product')
   
