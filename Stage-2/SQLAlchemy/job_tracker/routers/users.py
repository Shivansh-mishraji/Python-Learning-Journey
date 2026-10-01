# routers/users.py — user endpoints
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# import services and schemas
# from database import get_db

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import create_user, get_user
from schemas import UserCreate, UserResponse
from models import User
from database import get_db  
#
# router = APIRouter()   ← instead of app = FastAPI()
router = APIRouter()
#
# POST /users          → create_user

@router.post("/users", status_code = 201, response_model = UserResponse)
def create_user_endpoint(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db,data)

# GET  /users/{user_id} → get_user

@router.get("/users/{user_id}", status_code = 200, response_model = UserResponse)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_user(db,user_id)