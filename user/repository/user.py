import hashlib
from libs.mysql.mysql import MySql
from libs.password.password import Hasher
from model.schema import User 

class UserRepository:
    def __init__(self, db: MySql):
        self.db = db

    def create_user(self, username: str, password: str, email: str):
        hash_password = Hasher.get_password_hash(password)

        add_user = User(
            username = username,
            email = email,
            hashed_password = str(hash_password),
        )

        session = self.db.get_session()
        session.add(add_user)
        session.commit()
        session.refresh(add_user)

        return add_user
        
    def get_user(self , username: str):
        session = self.db.get_session()
        user = session.query(User).filter(User.username == username).first()
        return user

    # def update_profile():
    #     print("Update Profile")

