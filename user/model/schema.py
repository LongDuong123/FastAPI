from sqlalchemy import Column, Integer, String
from libs.mysql.mysql import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    hashed_password = Column(String(256))
    phone = Column(String(20), nullable=True)