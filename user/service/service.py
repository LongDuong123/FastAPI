from user.repository.repository import UserRepository
from user.model.model import *
from user.model.model_db import User

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        
    def login(self, user: UserLoginRequest):
        self.repo.get_user()
        return

    def register(self, user: UserRegisterRequest) -> User:
        profile = self.repo.create_user(user.username, user.password, user.email)
        return profile


    # def profile(self):
    #     print("...service...profile...")
    #     user = self.repo.update_profile()
    #     return
