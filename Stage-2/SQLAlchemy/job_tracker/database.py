# database.py — db setup
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
import os
# do these 3 things:
# 1. create BASE_DIR and engine (sqlite, same as before)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/job_tracker.db", echo = True)
# 2. create Base(DeclarativeBase)
class Base(DeclarativeBase):
    pass

# 3. write get_db() dependency generator
def get_db():
    with Session(engine) as session:
        yield session