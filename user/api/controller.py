from user.service.user import UserService

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
            token= accessToken,
            profile= UserProfile(
                username= data.username,
                email= data.email,
                phone= None,
            )
        )

    # def profile(self, user: UserRegisterResponse):
    #     user = self.svc.profile()
    #     return