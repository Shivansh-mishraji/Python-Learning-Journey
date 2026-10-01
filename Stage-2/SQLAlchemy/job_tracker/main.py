# main.py — entry point
# from fastapi import FastAPI
# import the two routers
# import models so tables get created on startup
import os
import sys

# Ensure job_tracker directory is in sys.path so submodules resolve correctly from any working directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from routers import applications, users
from models import User, Application

# app = FastAPI()
app = FastAPI()
# app.include_router(users.router)
app.include_router(users.router)
# app.include_router(applications.router)
app.include_router(applications.router)
# run with: uvicorn job_tracker.main:app --reload
