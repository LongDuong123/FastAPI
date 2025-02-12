from fastapi import FastAPI
import uvicorn

from controller import controller

app = FastAPI()

app.include_router(controller.router)

if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8080)