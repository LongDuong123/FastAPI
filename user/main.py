import uvicorn
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from dotenv import load_dotenv

from user.controller.controller import UserController
from user.repository.repository import UserRepository
from user.service.service import UserService
from user.controller.router import Routers
from libs.mysql.mysql import MySql

load_dotenv()

mysql = MySql(os.getenv('MYSQL_USER'), os.getenv('MYSQL_ROOT_PASSWORD'), os.getenv('MYSQL_HOST'), os.getenv('MYSQL_PORT'), os.getenv('MYSQL_DATABASE'))
repository = UserRepository(mysql)
service = UserService(repository)
controller = UserController(service)

app = FastAPI()
app.include_router(Routers(controller))

if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8080)