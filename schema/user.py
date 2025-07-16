from pydantic import BaseModel

class CreateUserReqSchema(BaseModel):
    fullname: str
    email: str
    password: str
    
    
class UserRespSchema(BaseModel):
    id: int
    fullname: str
    email: str
    
