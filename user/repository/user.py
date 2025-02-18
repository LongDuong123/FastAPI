import hashlib

from sqlalchemy import or_

from libs.mysql.mysql import MySql
from libs.password.password import Hasher
from user.model.schema import User 

class UserRepository:
    def __init__(self, db: MySql):
        self.db = db
        self.session = self.db.get_session()

    def create_user(self, username: str, password: str, email: str):
        hash_password = Hasher.get_password_hash(password)

        add_user = User(
            username = username,
            email = email,
            hashed_password = str(hash_password),
        )

        self.session.add(add_user)
        self.session.commit()
        self.session.refresh(add_user)

        return add_user
        
    def get_user(self, username: str = None, email: str = None):
        user = self.session.query(User).filter(
            or_(User.username == username, User.email == email)
        ).first()

        return user

    def update_profile(self, id:str, username: str = None, password: str = None, phone: str = None):
        user = self.session.query(User).filter(User.id == id).first()
        
        if not user:
            return None

        if username:
            user.username = username
        if phone:
            user.phone = phone
        if password:
            user.hashed_password =  str(Hasher.get_password_hash(password))

        self.session.commit()
        self.session.refresh(user)
        return user
