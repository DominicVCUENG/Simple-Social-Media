from fastapi import FastAPI
from database import get_post, insert_post
from models import Posts, Post
from sqlite3 import Connection, Row

app = FastAPI()
connection = Connection('social.db')
connection.row_factory = Row

@app.get("/posts")
async def posts() -> Posts:
    return get_post(connection)

@app.post("/posts")
async def add_post(post : Post) -> Post:
    insert_post(connection, post)
    return post