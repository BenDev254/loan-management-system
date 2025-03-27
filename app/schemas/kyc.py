
from pydantic import BaseModel
from typing import List, Optional

class KYCBase(BaseModel):
    customer_number: str
    name: str
    dob: str

class KYCResponse(KYCBase):
    id: int

    class Config:
        from_attributes = True
        