from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Union, Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Union[float, None] = None


class UpdatePost(Post):
    title: Optional[str]
    content: Optional[str]
    published: Optional[bool]
    rating: Optional[float]


my_posts = [
    {"id": 1, "title": "My First Post",
        "content": "This is the content of my first post"},
    {"id": 2, "title": "Second Post",
     "content": "This is the content of my second post"},
]


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
    return {}


@app.get("/")
def index():
    return {"msg": "Welcome to my API"}


@app.get("/posts/", status_code=status.HTTP_200_OK)
def get_posts():
    return {"data": my_posts}


@app.get("/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"data": post}


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    new_post = {"id": len(my_posts)+1, **post.dict()}
    my_posts.append(new_post)

    return {"data": new_post}


@app.patch("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id: int, updated_post: UpdatePost):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    for key, value in updated_post.dict().items():
        if value != None:
            post[key] = value

    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    try:
        my_posts.remove(find_post(id))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"data": None}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Genx",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
