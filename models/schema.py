from pydantic import BaseModel
    


class questionSchema(BaseModel):
    username: str
    email: str
    text: str
    
    
class answerSchema(BaseModel):
    text: str
    question_id: int


class loginSchema(BaseModel):
    email: str
    password: str

    
class registerSchema(loginSchema):
    username: str
    retype_password: str


class Locationschema(BaseModel):
    name_tm: str
    name_ru: str


class categoryschema(BaseModel):
    name_tm: str
    name_ru: str

class productSchema(categoryschema):
    description_tm: str
    description_ru: str
    price: float 
    code: str 
    discount: float
    subcategory_id: int

