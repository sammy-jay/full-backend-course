# Full Python Backend Course

All sections to be covered in the course are listed below

- [x] Virtual Environment setup
- [x] Project initialization
- [x] CRUD endpoints completion

## Project initialization

```bash
$ python -m venv env
$ source env/bin/activate

$ pip install fastapi[all]
```

## First API

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return { "message": "Hello World" }
```

Run the Web Server

```bash
$ uvicorn main:app --reload
```

### Path Operation

Each Path operation has a `path, method, and function`
Common Path methods are `get, post, put, delete`

### Request Body

```python
from fastapi.params import Body

def create_post(post: dict = Body(...)):
```

Using Pydantic

```python
from pydantic import BaseModel
```

Create a class for your Data Model and inherit from the BaseModel class.

```python
class Post(BaseModel):
    title: str
    content: str

def create_post(post: Post):
```
