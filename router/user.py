from fastapi import FastAPI, APIRouter, Depends
import sqlalchemy.exc
from schema.user import CreateUserReqSchema, UserRespSchema
from model import AsyncSessionFactory, Base
from model import User
from fastapi.exceptions import HTTPException
import sqlalchemy
from model import AsyncSession
from fastapi.requests import Request
from sqlalchemy import delete, select, or_,update
from schema.user import UserRespSchema
from typing import List


router = APIRouter(prefix="/user", tags=["user"])


@router.post('/add', response_model=UserRespSchema)
async def add_user(req: CreateUserReqSchema):
    # try:
    #     # 不用异步
    #     session = AsyncSessionFactory()

    #     user=User(email=req.email,fullname=req.fullname,password=req.password)
    #     session.add(user)
    #     await session.commit()
    #     await session.refresh(user)
    # except sqlalchemy.exc.IntergrityError as e:
    #     await session.rollback()
    #     raise HTTPException(status_code=500,detail=str(e))
    # # # 手动开启事务
    # # await session.begin()

    # # await session.commit()
    # # await session.rollback()

    # await session.close()
    # return user

    # 用上下文
    async with AsyncSessionFactory() as session:
        user = User(email=req.email, fullname=req.fullname,
                    password=req.password)
        session.add(user)
        return user


async def get_session():
    session = AsyncSessionFactory()
    try:
        yield session
    finally:
        await session.close()


@router.post("/add/depend", response_model=UserRespSchema)
async def add_user_depend(req: CreateUserReqSchema, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        user = User(email=req.email, username=req.fullname,
                    password=req.password)
        session.add(user)


@router.post("/add/middleware", response_model=UserRespSchema)
async def add_user_middleware(req: Request, user_data: UserRespSchema):
    session = req.state.session
    try:
        async with session.begin():
            user = User(email=user_data.email,
                        username=user_data.fullname, password=user_data.password)
            session.add(user)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/delete/{id}")
async def delete_user(id: int, request: Request):
    session = request.state.session
    try:
        async with session.begin():
            sql = delete(User).where(User.id == id)
            await session.execute(sql)
        return {"message": "删除成功"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/user/select/{id}", response_model=UserRespSchema)
async def get_user(id: int, request: Request):
    session = request.state.session
    async with session.begin():
        query = await session.execute(select(User).where(User.id == id))
        result = query.one()._asdict()
        return result


# 查询多个数据
@router.get("/user/select", response_model=List[UserRespSchema])
async def get_users(session: AsyncSession = Depends(get_session), q: str | None = None):
    async with session.begin():
        stmt = select(User.id,User.name,User.email).where(or_(User.name.like(f"%{q}%"), User.email.like(f"%{q}%")))
        query = await session.execute(stmt)
        result = [row._asdict() for row in query]
        return result


@router.post("/user/add", response_model=UserRespSchema)
async def add_user(user_body: CreateUserReqSchema,req: Request):
    async with req.state.session.begin():
        user = user.User(email=user_body.email, fullname=user_body.fullname, password=user_body.password)
        req.state.session.add(user)
    return user


# 查找修改再保存
@router.put("/user/{id}", response_model=UserRespSchema)
async def update_user(id: int, user_body: CreateUserReqSchema, req: Request):
    session = req.state.session
    async with req.state.session.begin():
        query = await session.execute(select(user.User).where(user.User.id == id))
        user = query.scalars().first()
        user.email = user_body.email
        user.fullname = user_body.fullname
        user.password = user_body.password
    return user

# 直接修改
@router.put('/user/update/{id}')
async def update_user(id: int, user_body: UserRespSchema, req: Request):
    session = req.state.session
    async with req.state.session.begin():
        await session.execute(update(User).where(User.id == id).values(user_body))
