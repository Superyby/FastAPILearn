from fastapi import Header, FastAPI

app = FastAPI()


@app.get("/header")
async def read_header(user_agent: str | None = Header(None),host: str | None = Header(None)):
    print('User-Agent:', user_agent)
    print('Host:',host)
    return {"message": "header"}