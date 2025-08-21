from fastapi import FastAPI
from typing import Optional
from .schema.schema import Blog

app = FastAPI()



@app.get("/")
def home():
    return {"message": "Hello From FastAPI"}

# @app.get("/blog")
# def get_blogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
#     return {"data": f"{limit} blogs from DB, published={published}, sort={sort}"}

# @app.get("/blog/unpublished")
# def unpublished():
#     return {"data": "All unpublished blogs"}

@app.get("/blog/{id}")
def show_blog(id: int):
    return {"data": f"Blog with id{id}"}

# @app.get("/blog/{id}/comments")
# def comments(id: int, limit: int = 10):
#     return {"data": f"{limit} comments for blog {id}"}

@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog created with title {request.title}"}
    