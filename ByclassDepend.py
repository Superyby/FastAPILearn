from fastapi import FastAPI, Depends
from typing import Dict

app = FastAPI()


class CommonQueryParmas:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

    def get_query_params(self):
        query_params = []
        if self.q:
            query_params = self.q.split(" ")
        return query_params


@app.get("/books")
async def get_books(params=Depends(CommonQueryParmas), skip=100):
    print(params.q)
    print(params.get_query_params())
    print('skip', skip)
    return {"msg", "ok"}
