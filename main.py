from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app=FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int] =None #compelly optional

@ app.get("\ ")
def root():
    return{"message":"welcome to my api"}

@ app.get("\posts ")
def creat_post(post:Post):
    print(post.title)
    return{"data": "post"}  