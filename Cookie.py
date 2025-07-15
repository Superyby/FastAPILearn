# from fastapi import Cookie
# from fastapi import FastAPI
# from pydantic import *
# from fastapi.responses import JSONResponse

# app = FastAPI()


# @app.get("/cookie/get")
# async def get_cookie(username: str | None = Cookie(None)):
#     print("cookie_name:", username)
#     return "success"

# @app.get("/cookie/set")
# async def set_cookie():
#     response = JSONResponse(content={"msg": "set cookie"})
#     response.set_cookie('token', '12345678')
#     return response

from fastapi import FastAPI, Cookie
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/cookie/get")
async def get_cookie(username: str | None = Cookie(None)):
    print("cookie_name:", username)
    return "success"

@app.get("/cookie/set")
async def set_cookie():
    response = JSONResponse(content={"msg": "set cookie"})
    response.set_cookie('token', '12345678')  # 修正方法名
    return response