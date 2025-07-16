from fastapi import FastAPI
from router import user
from fastapi.requests import Request
from model import AsyncSessionFactory, Base
from middleware import db
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

app.include_router(user.router)

# 添加中间件
app.add_middleware(BaseHTTPMiddleware, dispatch=db.create_session_middleware) 