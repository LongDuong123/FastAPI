from fastapi import APIRouter

from service import service
from model import model

class UserController:
    def __init__(self, svc: service.UserService):
        self.svc = svc
    
    def login(self, user: model.UserLogin):
        token = self.svc.login()
        return

    def register(self, user: model.UserRegister):
        user = self.svc.register()
        return

    def profile(self, user: model.UserProfile):
        user = self.svc.profile()
        return

##################################### 
router = APIRouter()

@router.post("/login")
def login(user: model.UserLogin):
    """
    Endpoint Login: input {}, output{}
    """
    UserController.login()
    return

@router.post("/register")
def register(user: model.UserRegister):
    """
    Endpoint Register: input {} , output {}
    """
    UserController.register
    return

@router.post("/profile")
def profile():
    """
    Endpoint profile: input {} , output {}
    """
    UserController.profile()
    return

# @router.post("/logout")
# def logout():
#     print("...controller....logout...")
#     return