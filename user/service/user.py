import os

from user.repository.user import UserRepository
from user.model.user import *
from user.model.schema import User
from libs.password.password import Hasher
from libs.jwt.jwt import generate_token, verify_token
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        
    def login(self, user: UserLoginRequest):
        profile = self.repo.get_user(user.username)
        if user is None:
            print("User not found")
            return

        if Hasher.verify_password(user.password, profile.hashed_password) == False:
            print("Password not match")
            return

        token = generate_token(
            profile.id, 
            os.getenv('SECRET_KEY'), 
            os.getenv('SECURITY_ALGORITHM'), 
            int(os.getenv('EXPIRE_MINUTES')))

        return token


    def register(self, user: UserRegisterRequest):
        profile = self.repo.create_user(user.username, user.password, user.email)
        if not profile:
            print("email exited ")
            return

        token = generate_token(
            profile.id, 
            os.getenv('SECRET_KEY'), 
            os.getenv('SECURITY_ALGORITHM'), 
            int(os.getenv('EXPIRE_MINUTES')))
            
        return token, profile

    def profile(self, id: str, user: UserUpdateRequest):
        user = self.repo.update_profile(id, user.username, user.password, user.phone)
        return user
