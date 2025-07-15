from fastapi import FastAPI, Path, Query, Body,Cookie
from pydantic import *

app = FastAPI()


class Item(BaseModel):
    name: str = Field(default="ok", max_length=10)
    description: str | None = None
    price: float | None = 0
    # tax : float | None = None

    @field_validator("name")
    @classmethod
    def validator_name(cls, value: str):
        if ' ' in value:
            raise ValueError("不能有空格")
        return value


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(description="item信息")):
    # results = {"item_id": item_id,  **item.dict()}
    # if q: results.update({"q": q})
    # return results
    print("item_id", item_id)
    print(item.name, item.description)
    return {"msg": "update item success"}