from pydantic import BaseModel

class UserProfile(BaseModel):
    username: str
    email: str
    phone: str

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
