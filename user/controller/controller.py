from user.service.service import UserService

from user.model.model import *

class UserController:
    def __init__(self, svc: UserService):
        self.svc = svc
    
    def login(self, user: UserLoginRequest) -> UserLoginResponse:
        token = self.svc.login(UserLoginRequest)
        return UserLoginResponse()

    def register(self, user: UserRegisterRequest) -> UserRegisterResponse:
        data = self.svc.register(UserRegisterRequest)
        return UserRegisterResponse(
            profile= UserProfile(
                username= data.username,
                email= data.email,
                phone= data.phone,
            )
        )

    # def profile(self, user: UserRegisterResponse):
    #     user = self.svc.profile()
    #     return