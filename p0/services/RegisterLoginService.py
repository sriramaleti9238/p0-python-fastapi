from pydantic import EmailStr

from model.DataModels import UserModel
from model.UserDto import UserDetailsDto
from model.schema import User
from database.db import Session
from model.UserAuth import encode_user

def if_email_exists(email : EmailStr):
    db=Session()
    user =db.query(User).filter(User.email == email).first()
    db.close()

    if user:
        return False
    return True

def create_user(user : UserModel):
    db = Session()
    new_user = User(name=user.name, email=user.email, password=user.password, userType=user.userType)
    db.add(new_user)
    db.commit()
    db.close()
    return new_user

def login_user(user : UserDetailsDto):
    db = Session()
    user_exist = db.query(User).filter(
        User.email == user.userEmail,
        User.password == user.password,
        User.userType == user.typeOfEmp
    ).first()
    db.close()
    return encode_user(user_exist.name , user_exist.userType)

def user_exist(user : UserDetailsDto):
    db = Session()
    user = db.query(User).filter(
        User.email == user.userEmail,
        User.password == user.password,
        User.userType == user.typeOfEmp
    ).first()
    db.close()
    if user:
        return True
    return False


