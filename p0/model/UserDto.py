from pydantic import BaseModel


class UserDetailsDto(BaseModel):

    userEmail : str
    password : str
    typeOfEmp : str