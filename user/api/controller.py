import os

from fastapi import HTTPException

from user.service.user import UserService
from libs.jwt.jwt import verify_token
from user.model.user import *

class UserController:
    def __init__(self, svc: UserService):
        self.svc = svc
    
    def login(self, user: UserLoginRequest) -> UserLoginResponse:
        accessToken = self.svc.login(user)
        if accessToken is None:
            raise HTTPException(status_code=400, detail="Invalid username or password")

        return UserLoginResponse(
            token= accessToken
        )

    def register(self, user: UserRegisterRequest) -> UserRegisterResponse:
        accessToken, data = self.svc.register(user)
        if accessToken is None:
            raise HTTPException(status_code=400, detail="Failed to create user")
            
        return UserRegisterResponse(
            token=accessToken,
            username=data.username,
            email=data.email,
            phone=data.phone
        )

    def profile(self, user: UserUpdateRequest, token: str) -> UserUpdateResponse:
        payload = verify_token(token, os.getenv('SECRET_KEY'), [os.getenv('SECURITY_ALGORITHM')])
        if not payload:
            raise HTTPException(status_code=401, detail="Missing Authorization header")

        id = payload.get('user_id')
        userProfile = self.svc.profile(id, user)
        if not userProfile:
            raise HTTPException(status_code=404, detail="Failed to update user profile")

        return UserUpdateResponse(
            username=userProfile.username,
            email=userProfile.email,
            phone=userProfile.phone
        )