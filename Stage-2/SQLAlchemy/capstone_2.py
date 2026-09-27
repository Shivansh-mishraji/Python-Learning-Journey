# Blog REST API
# using FastAPI + SQLAlchemy 2.0 + Pydantic v2 + SQLite

import os
import time
import functools

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from pydantic import BaseModel, ConfigDict
from fastapi import FastAPI, Depends, HTTPException


app = FastAPI()


# db setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/capstone.db", echo=False)


class Base(DeclarativeBase):
    pass


# models
class Author(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(40), unique=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="author", cascade="all, delete-orphan")


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(60))
    content: Mapped[str] = mapped_column(String(5000))
    author_id: Mapped[int] = mapped_column(ForeignKey(Author.id))
    author: Mapped[Author] = relationship(back_populates="posts")


Base.metadata.create_all(engine)


# pydantic schemas
class AuthorCreate(BaseModel):
    name: str
    email: str


class AuthorResponse(BaseModel):
    id: int
    name: str
    email: str
    posts: list["PostResponse"] = []

    model_config = ConfigDict(from_attributes=True)


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


# db dependency
def get_db():
    with Session(engine) as session:
        yield session


# timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"[LATENCY] {func.__name__} completed in {end * 1000:.2f}ms")
        return result
    return wrapper


# services
@timer
def create_author(db: Session, author: AuthorCreate) -> Author:
    new_author = Author(name=author.name, email=author.email)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


@timer
def get_author(db: Session, author_id: int) -> Author:
    result = db.get(Author, author_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return result


@timer
def create_post(db: Session, post: PostCreate) -> Post:
    if not db.get(Author, post.author_id):
        raise HTTPException(status_code=404, detail="Author not found")
    new_post = Post(title=post.title, content=post.content, author_id=post.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@timer
def get_author_posts(db: Session, author_id: int) -> list[Post]:
    author = get_author(db, author_id)
    return author.posts


# endpoints
@app.post("/authors", status_code=201, response_model=AuthorResponse)
def create_author_endpoint(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)


@app.get("/authors/{author_id}", status_code=200, response_model=AuthorResponse)
def get_author_endpoint(author_id: int, db: Session = Depends(get_db)):
    return get_author(db, author_id)


@app.post("/posts", status_code=201, response_model=PostResponse)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)


@app.get("/posts/{author_id}", status_code=200, response_model=list[PostResponse])
def get_posts_endpoint(author_id: int, db: Session = Depends(get_db)):
    return get_author_posts(db, author_id)