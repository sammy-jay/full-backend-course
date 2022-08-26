from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def index():
    return {"msg": "Welcome to my API"}


@app.get("/posts/")
def get_posts():
    return []


@app.post("/posts/")
def create_post(post: Post):
    print(post.title)
    return {}
