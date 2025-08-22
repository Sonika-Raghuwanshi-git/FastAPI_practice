# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# # Pydantic Model
# class Blog(BaseModel):
#     title: str
#     body: str
#     published: bool = True


# # Routes
# @app.get("/")
# def home():
#     return {"message": "Hello FastAPI"}


# @app.get("/blog/{id}")
# def show_blog(id: int):
#     return {"data": f"Blog with id {id}"}


# @app.post("/blog")
# def create_blog(request: Blog):
#     return {"data": f"Blog created with title {request.title}"}


# @app.put("/blog/{id}")
# def update_blog(id: int, request: Blog):
#     return {
#         "data": f"Blog with id {id} updated to title '{request.title}' and published = {request.published}"
#     }

# @app.delete("/blog/{id}")
# def delete_blog(id: int):
#     return {"data": f"Blog with id {id} has been deleted"}


from fastapi import FastAPI
from database import engine, Base
from routers import blog, user, authentication

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
