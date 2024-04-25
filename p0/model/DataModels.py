from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    name : str
    email : EmailStr
    password : str
    userType : str

class JobModel(BaseModel):
    compName: str
    jobExperience: str
    jobRole: str
    techStack: str
    location: str
    salary: int
    dateOfApplication: datetime
    userId :int