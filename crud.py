from models import Banner, Question, Location, Users, Product
from sqlalchemy.orm import Session, joinedload
from upload_depends import upload_image
from sqlalchemy import asc, desc
from sqlalchemy import func, or_

def create_banner(db: Session, file):
    uploaded_name = upload_image('banners', file)
    new_add = Banner(
        img = uploaded_name
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_banner(page, limit, db: Session):
    result = db.query(Banner)\
        .order_by(desc(Banner.create_at))\
            .offset((page - 1) * limit)\
                .limit(limit)\
                    .all()
    return result


def create_qa(req, model, db: Session):
    new_add = model(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_questions(db: Session):
    result = db.query(Question).options(joinedload(Question.answer)).all()
    return result



def signUp(req, db: Session):
    user = db.query(Users).filter(
        or_(
            Users.username == req.username,
            Users.email == req.email
        )
    ).first()
    if user:
        return False
    new_add = Users(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True 


def signIn(req, db: Session):
    user = db.query(Users).filter(
        and_(
            or_(
                Users.username == req.email,
                Users.email == req.email
            ),
            Users.password == req.password 
        )
    ).first()
    if user:
        return True


def read_users(db: Session):
    result = db.query(
        Users.username,
        Users.email
    ).all()
    return result



def search_product(q, db: Session):
    result = db.query(Product)\
        .filter(
            or_(
                func.lower(Product.name).like(f'%{q}%'),
            
            )
        ).all()
    return result



def create_location(req, model, db: Session):
    new_add = model(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_location(db: Session):
    result = db.query(Location).all()
    return result


