from fastapi import FastAPI
from fastapi.requests import Request
from model import AsyncSessionFactory, Base

async def create_session_middleware(request, call_next):
    # 请求到达视图函数之前执行的
    session = AsyncSessionFactory()
    request.state.session = session
    response = await call_next(request)
    # 响应浏览器之前执行的
    await session.close()

