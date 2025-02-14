from fastapi import APIRouter

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

    # @router.post("/profile")
    # def profile():
        
    #     return

    # @router.post("/logout")
    # def logout():
    #     print("...controller....logout...")
    #     return

    return Router

