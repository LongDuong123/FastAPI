import uvicorn
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from dotenv import load_dotenv

from user.api.controller import UserController
from user.repository.user import UserRepository
from user.service.user import UserService
from user.api.router import Routers
from libs.mysql.mysql import MySql
from libs.mysql.mysql import Base
from user.model.schema import User

load_dotenv()

database = MySql(os.getenv('MYSQL_USER'), os.getenv('MYSQL_PASSWORD'), os.getenv('MYSQL_HOST'), int(os.getenv('MYSQL_PORT')), os.getenv('MYSQL_DATABASE'))
repository = UserRepository(database)
service = UserService(repository)
controller = UserController(service)

Base.metadata.create_all(database.get_engine())

app = FastAPI()
app.include_router(Routers(controller))