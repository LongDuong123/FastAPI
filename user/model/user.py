from pydantic import BaseModel
from typing import Optional

class UserProfile(BaseModel):
    username: str
    email: str
    phone: Optional[str] = None

class UserRegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class UserRegisterResponse(UserProfile):
    token: str

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserLoginResponse(BaseModel):
    token: str

class UserUpdateRequest(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None

class UserUpdateResponse(UserProfile):
    pass