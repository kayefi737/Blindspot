from pydantic import BaseModel

class UserRequest(BaseModel):
  id: int
  name: str
  age: int
  height: str