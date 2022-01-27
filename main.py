from configs.connection import database
from fastapi import FastAPI, Depends, Request
from functools import lru_cache
from configs import appinfo
import time
from fastapi_pagination import add_pagination

app = FastAPI()

@lru_cache()
def app_setting():
    return appinfo.Setting()

@app.get("/root", tags=["Home"])
async def home():
    return {
        "Info" : "Welcome in Home Economy"
    }


@app.get("/check/{item}", tags=["Home"])
async def home(item: str):
    return {
        "Check Item" : item
    }

@app.get("/app/info", tags=["App"])
async def app_info():
    return {
        "app_name"      : "Home Economy App",
        "app_version"   : "1.0",
        "app_framework" : "FastAPI",
        "app_date"      : "2021-01-01 20:48:10",
        "Owner"         : "Pacis Jules ISHIMWE"
    }

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)

    return response

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


from auth import controller as authController
from users import controller as userController
from saving import controller as savingController

app.include_router(authController.router, tags=["Auth"])
app.include_router(userController.router, tags=["Users"])
app.include_router(savingController.router, tags=["Saving"])

add_pagination(app)
