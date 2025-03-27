
from pydantic import BaseModel
from typing import Optional



class AuthRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

