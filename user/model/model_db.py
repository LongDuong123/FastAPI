from sqlalchemy import Column, Integer, String
from ...libs.mysql.mysql import MySql

class User(MySql.base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    hashed_password = Column(String(256))
    phone = Column(String(20))