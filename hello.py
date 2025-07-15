from typing import *
from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def item(item_id: int,q: Optional[str] = None):
    return {"item_id": item_id,"q" : q}