from fastapi import APIRouter, Request, HTTPException, Security, Depends
from fastapi.security import APIKeyHeader

from user.api.controller import UserController
from user.model.user import *

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

def Routers(crtl: UserController):
    Router = APIRouter()
    
    @Router.post("/login")
    def login(user: UserLoginRequest) -> UserLoginResponse:
        return crtl.login(user)

    @Router.post("/register")
    def register(user: UserRegisterRequest) -> UserRegisterResponse:
        return crtl.register(user)

    @Router.post("/profile")
    def profile(user: UserUpdateRequest, token: str = Security(api_key_header)) -> UserUpdateResponse:
        if token is None:
            raise HTTPException(status_code=401, detail="Missing Authorization header")

        return crtl.profile(user, token)

    # @router.post("/logout")
    # def logout():
    #     print("...controller....logout...")
    #     return

    return Router

