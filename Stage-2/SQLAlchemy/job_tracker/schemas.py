# schemas.py — pydantic schemas
# import BaseModel, ConfigDict from pydantic
from pydantic import BaseModel, ConfigDict

#
# UserCreate      → name, email
class UserCreate(BaseModel): 
    name: str
    email: str
# UserResponse    → id, name, email, applications=[]  + from_attributes=True
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    applications: list["ApplicationResponse"] = []

    model_config= ConfigDict(from_attributes = True)

# ApplicationCreate → company, role, status, job_description, user_id
class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str 
    job_description: str
    user_id: int

# ApplicationResponse → id, company, role, status, job_description, user_id  + from_attributes=True
class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str
    job_description: str
    user_id: int

    model_config = ConfigDict(from_attributes = True)

# StatusUpdate    → status (only this one field, used for PATCH endpoint)
class StatusUpdate(BaseModel):
    status: str