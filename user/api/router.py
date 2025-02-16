from fastapi import APIRouter, Request, HTTPException

from user.api.controller import UserController
from user.model.user import *

def Routers(crtl: UserController):
    Router = APIRouter()
    
    @Router.post("/login")
    def login(user: UserLoginRequest) -> UserLoginResponse:
        return crtl.login(user)

    @Router.post("/register")
    def register(user: UserRegisterRequest) -> UserRegisterResponse:
        return crtl.register(user)

    @Router.post("/profile")
    def profile(user: UserUpdateRequest, request: Request) -> UserUpdateResponse:
        token = request.headers.get("Authorization")
        if token is None:
            raise HTTPException(status_code=400, detail="Missing Authorization header")
            
        return crtl.profile(user, str(token))

    # @router.post("/logout")
    # def logout():
    #     print("...controller....logout...")
    #     return

    return Router

