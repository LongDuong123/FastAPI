from fastapi import FastAPI
import uvicorn

from user.controller import controller

app = FastAPI()

app.include_router(controller.router)

if __name__ == "__main__":  
    uvicorn.run(app, host="localhost", port=8080)