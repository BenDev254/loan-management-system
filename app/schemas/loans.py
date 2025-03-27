
from typing import Optional
from pydantic import BaseModel
from datetime import datetime 

class LoanBase(BaseModel):
    customer_number: str
    amount: float
    status: Optional[str] = "Pending"

class LoanCreate(LoanBase):
    pass

class LoanResponse(LoanBase):
    id: int

    class Config:
        from_attributes = True

