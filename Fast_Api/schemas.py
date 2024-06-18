from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


class JwtModel(BaseModel):
    authjwt_secret_key: str = os.getenv('AUTHJWT_SECRET_KEY', 'default_secret_key')


class Registration(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    is_staff: bool

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "first_name": "bilo",
                "last_name": "Aliyev",
                "username": "Aliyev123",
                "email": "aliyev@gmail.com",
                "password": "****"

            }
        }


class Login(BaseModel):
    username: str
    password: str


class ProductM(BaseModel):
    id: int
    image: str
    name: str
    description: str
    price: str
    prices: int
    slug: str
    


class BlogM(BaseModel):
    id: int
    title: str
    owner: str
    slug: str


class ClientCommentM(BaseModel):
    msg: str
    full_name: str
