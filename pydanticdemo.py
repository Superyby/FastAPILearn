from datetime import date
from pydantic import *
from typing import Optional,Dict


class User(BaseModel):
    id: int
    name: str
    age: int
    data_joined: date | None
    tastes: Dict[str, PositiveInt]
    
if __name__ == "__main__":
    user = User(id=1, name="John Doe", age=42, data_joined=None,tastes={"apple": 5, "banana": 3})
    print(user.id)