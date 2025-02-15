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

class UserRegisterResponse(BaseModel):
    token: str
    profile: UserProfile

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserLoginResponse(BaseModel):
    token: str
