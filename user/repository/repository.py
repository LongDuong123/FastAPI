import hashlib
from ...libs.mysql.mysql import MySql
from ...libs.password.password import Hasher
from model import model

class UserRepository:
    def __init__(self, username: str, password: str, host: str, port: int, database: str):
        self.db = MySql(username, password, host, port, database)

    def create_user(self, user: model.UserRegister):
        hash_password = Hasher.get_password_hash(user.password)

        add_user = model_py.User(
            username = user.username,
            email = user.email,
            password = hash_password
        )

        self.db.session.add(add_user)
        return add_user
        

    def get_user():
        print("Get User")

    def update_profile():
        print("Update Profile")

