from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()

DB_URL="mysql+asyncmy://root:root@127.0.0.1:3306/fastapi_sqlalchemy?charset=utf8mb4"

engine = create_async_engine(DB_URL, echo=True,
                             pool_pre_ping=True,
                             pool_recycle=3600,
                             pool_size=20,
                             max_overflow=10)



AsyncSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False,autoflush=True)

Base = declarative_base()


# 导入其他模型的Python文件
from model import user
from model import article