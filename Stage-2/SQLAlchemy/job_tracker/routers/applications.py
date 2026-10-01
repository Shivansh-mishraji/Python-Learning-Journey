# routers/applications.py — application endpoints
# same imports as users.py
from models import Application
from schemas import ApplicationCreate, ApplicationResponse, StatusUpdate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import add_application, get_user_application, update_status, delete_application
from database import get_db
# router = APIRouter()
router = APIRouter()

# POST   /applications                    → add_application

@router.post("/applications", status_code = 201, response_model = ApplicationResponse)
def add_application_endpoint(data: ApplicationCreate, db: Session = Depends(get_db)):
    return add_application(db,data)

# GET    /applications/{user_id}          → get_user_applications

@router.get("/applications/{user_id}", status_code = 200, response_model = list[ApplicationResponse])
def get_user_application_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_user_application(db,user_id)

# PATCH  /applications/{app_id}/status   → update_status

@router.patch("/applications/{app_id}/status", status_code = 200, response_model = ApplicationResponse)
def update_status_endpoint( app_id: int, data: StatusUpdate, db:Session = Depends(get_db) ):
    return update_status(db,app_id,data.status)

# DELETE /applications/{app_id}          → delete_application

@router.delete("/applications/{app_id}", status_code = 204)
def delete_application_endpoint( app_id: int, db:Session = Depends(get_db) ):
    return delete_application(db,app_id)