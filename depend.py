from fastapi import FastAPI, Depends
from typing import Dict

app = FastAPI()


async def list_common(page: int = 1, size: int = 10, q: str | None = None):
    query_params = []
    if q:
        query_params = q.split(" ")
    return {"page": page, "size": size, "query_params": query_params}

async def list_common_with_q(q: str | None = None):
    query_params = []
    if q:
        query_params = q.split(" ")
    return query_params
@app.get("/items")
async def get_items(common: Dict = Depends(list_common)):
    print('page', common['page'])
    print('size', common['size'])
    print('query_params', common['query_params'])
    return {"items": ['xx', 'yy']}


@app.get("/users")
async def get_items(query_params: Dict = Depends(list_common_with_q),page: int = 1, size: int = 10):
    print('page', page)
    print('size', size)
    print('query_params', query_params)
    return {"items": ['xx', 'yy']}