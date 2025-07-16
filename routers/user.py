from fastapi import FastAPI,Path,Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str =Path(max_length=10,description="名字")):
    """
    Args:
        name (str, optional): _description_. Defaults to Path(max_length=10,description="名字").
    Returns:
        _type_: _description_
    """
    return {"message": f"Hello {name}"}


@app.get("/books")
async def book_list(page: int=Query(default=1,description="页码"),size: int=Query(default=10,description="每页数量")):
    return {"page": page,"size": size}
    # return {"page": page,"size": size}