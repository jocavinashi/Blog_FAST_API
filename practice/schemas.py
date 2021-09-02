from typing import Text ,Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
    user_id:int


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str

    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser

    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str

    class Config():
        orm_mode=True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None