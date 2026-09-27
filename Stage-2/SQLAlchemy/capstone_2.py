# 🎫 Ticket: Build Blog REST API
# Assigned to: Shivansh Stack: FastAPI + SQLAlchemy 2.0 + Pydantic v2 + SQLite File: Stage-2/SQLAlchemy/blog_api.py Due: End of day
from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from pydantic import BaseModel, ConfigDict
import os
from fastapi import FastAPI, Depends, HTTPException
import functools
import time
# Requirements
# Two entities:
app = FastAPI()

# Author — has id, name, email (unique)
class Base(DeclarativeBase):
    pass
class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(40), unique = True)
    posts: Mapped[list["Post"]] = relationship(back_populates = "author", cascade= "all, delete-orphan")
# Post — has id, title, content, author_id (foreign key)
class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(60))
    content: Mapped[str] = mapped_column(String(5000))
    author_id: Mapped[int] = mapped_column(ForeignKey(Author.id))
# An author can have many posts.
    author: Mapped[Author] = relationship(back_populates = "posts")

# Four service functions:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/capstone.db", echo = False)
Base.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session
class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    model_config = ConfigDict(from_attributes=True)

class AuthorCreate(BaseModel):
    name: str
    email: str

class AuthorResponse(BaseModel):
    id: int
    name: str
    email: str
    posts: list[PostResponse] = []
    model_config = ConfigDict(from_attributes=True)

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result= func(*args, **kwargs)
        end = time.perf_counter()-start
        print(f"[LATENCY] {func.__name__} completed in {end*1000:.2f}ms")
        return result
    return wrapper

# create_author — save a new author, return it
@timer
def create_author(db: Session, author: AuthorCreate) -> Author:
    new_author = Author(name= author.name, email = author.email)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

# get_author — find by id, raise error if not found
@timer
def get_author(db: Session, author_id: int) -> Author:
    result = db.get(Author, author_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return result

# create_post — validate author exists, save post, return it
@timer
def create_post(db: Session, post: PostCreate) -> Post:
    result = db.get(Author, post.author_id)
    if not result:
        raise HTTPException(status_code=404, detail="Author not found")
    new_post = Post(title = post.title, content = post.content, author_id = post.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# get_author_posts — return all posts for an author
@timer
def get_author_posts(db: Session, author_id: int) -> list[Post]:
    result = get_author(db, author_id)
    return result.posts

# Four endpoints:

# POST /authors → create author
@app.post("/authors",status_code = 201, response_model = AuthorResponse)
def create_author_endpoint(author: AuthorCreate, db:Session = Depends(get_db)):
    return create_author(db, author)

# GET /authors/{id} → get author with their posts
@app.get("/authors/{author_id}", status_code = 200, response_model = AuthorResponse)
def get_author_endpoint(author_id: int, db: Session = Depends(get_db)):
    return get_author(db, author_id)

# POST /posts → create a post
@app.post("/posts", status_code = 201, response_model = PostResponse)
def create_post_endpoint(post: PostCreate, db:Session = Depends(get_db)):
    return create_post(db,post)

# GET /posts/{author_id} → get all posts by author
@app.get("/posts/{author_id}", status_code = 200, response_model = list[PostResponse])
def get_posts_endpoint( author_id: int, db: Session = Depends(get_db)):
    return get_author_posts(db, author_id)

# Rules
# Use custom exceptions for not-found cases
# Use @timer decorator on all service functions
# Use Depends(get_db) for session injection
# Endpoints only call services — no logic inside endpoints