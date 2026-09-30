# services.py — business logic
# import Session from sqlalchemy.orm
from sqlalchemy.orm import Session
# import models and schemas (from models import User, Application etc.)
from models import User, Application
from schemas import UserCreate, UserResponse, ApplicationCreate, ApplicationResponse, StatusUpdate
from fastapi import HTTPException
# put the @timer decorator here too
import functools
import time
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"[LATENCY] {func.__name__} completed in {end*1000:.2f}ms")
        return result
    return wrapper
# write these 6 service functions:
# create_user(db, data) -> User
@timer
def create_user(db: Session, data: UserCreate) -> User:
    new_user = User(name = data.name , email = data.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get_user(db, user_id) -> User          ← raise 404 if not found
@timer
def get_user(db: Session, user_id: int) -> User:
    result = db.get(User, user_id)
    if not result: 
        raise HTTPException(status_code= 404, detail = "User not found")
    return result

# add_application(db, data) -> Application  ← raise 404 if user not found
@timer
def add_application(db: Session, data: ApplicationCreate) -> Application:
    get_user(db,data.user_id)
#                                            ← raise 400 if status is invalid
    if data.status not in ["applied", "interview", "offer", "rejected"]:
        raise HTTPException(status_code = 400, detail = "Invalid Status.")
    new_application = Application(company = data.company, role= data.role, status = data.status, job_description = data.job_description, user_id = data.user_id)
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application

# get_user_applications(db, user_id) -> list[Application]
@timer
def get_user_application(db: Session, user_id: int) -> list[Application]:
    result = get_user(db, user_id)
    return result.applications

# update_status(db, app_id, new_status) -> Application  ← raise 400 if invalid status
@timer
def update_status(db:Session, app_id: int, new_status:str ) -> Application:
    result = db.get(Application, app_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Application not found")
    if new_status not in ["applied", "interview", "offer", "rejected"]:
        raise HTTPException(status_code=400, detail="Invalid Status.")
    result.status = new_status
    db.commit()
    db.refresh(result)
    return result

# delete_application(db, app_id) -> None   ← raise 404 if not found
@timer
def delete_application(db: Session, app_id: int) -> None:
    result = db.get(Application,app_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(result)
    db.commit()
#
# valid statuses: "applied", "interview", "offer", "rejected"
