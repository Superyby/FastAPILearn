from fastapi import APIRouter, Header, Depends
from fastapi.exceptions import HTTPException


async def login_required(token: str = Header()):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-token is invalid")


router = APIRouter('/item', tags=['item'], dependencies=[Depends(login_required)])

@router.get('/list')
async def read_items():
    return {"items": [{"name": "yyy"}]}