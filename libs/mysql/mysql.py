from sqlalchemy import create_engine

class MySql:
    def __init__(self, username: str, password: str, host: str, port: int, database: str):
        self.database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(self.database_url)
        self.session = sessionmaker(bind=self.engine)
        self.base = declarative_base()

    def get_session():
        return self.session

    def get_engine():
        return self.engine
