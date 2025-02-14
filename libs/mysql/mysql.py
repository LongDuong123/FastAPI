from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
class MySql:
    def __init__(self, username: str, password: str, host: str, port: int, database: str):
        self.database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(self.database_url)
        self.session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.session

    def get_engine(self):
        return self.engine

    def connect(self):
        try:
            connection = self.engine.connect()
            print("Đã kết nối tới cơ sở dữ liệu MySQL")
            return connection
        except Exception as e:
            print("Kết nối MySQL thất bại:", e)
            return None

