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

        return UserLoginResponse(
            token= accessToken
        )

    def register(self, user: UserRegisterRequest) -> UserRegisterResponse:
        accessToken, data = self.svc.register(user)
        
        return UserRegisterResponse(
            token=accessToken,
            username=data.username,
            email=data.email,
            phone=data.phone
        )

    def profile(self, user: UserUpdateRequest, token: str) -> UserUpdateResponse:
        payload = verify_token(token, os.getenv('SECRET_KEY'), [os.getenv('SECURITY_ALGORITHM')])
        if payload is None:
            raise HTTPException(status_code=400, detail="Missing Authorization header")

        id = payload.get('user_id')
        user = self.svc.profile(id, user)
        return UserUpdateResponse(
            username=user.username,
            email=user.email,
            phone=user.phone
        )