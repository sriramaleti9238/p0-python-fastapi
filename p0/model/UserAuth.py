import jwt
from fastapi import HTTPException


def encode_user(username : str , typeofuser :str ):
    encoded_data = jwt.encode(payload={"name": username , "password": typeofuser },
                              key='secret',
                              algorithm="HS256")
    return encoded_data

def verify_token(token: str):
    try:
        payload = jwt.decode(token, key='secret', algorithms=["HS256"])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")