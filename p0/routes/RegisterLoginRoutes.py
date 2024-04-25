from fastapi import APIRouter, HTTPException
from services.RegisterLoginService import create_user ,if_email_exists ,user_exist ,login_user
from model.DataModels import UserModel
from model.UserDto import UserDetailsDto

user_router = APIRouter()

@user_router.post("/register")
def register_user(user : UserModel):
    if if_email_exists(user.email):
        create_user(user)
        return {" user created successfully "}
    return {"user with email id already exists "}

@user_router.post("/login")
def login(user : UserDetailsDto):
    if user_exist(user):
        return login_user(user)
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


