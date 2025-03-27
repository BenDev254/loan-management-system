from pydantic import BaseModel
from datetime import datetime
from typing import List



class TransactionBase(BaseModel):
    customer_number: str
    transaction_details: str

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        from_attributes = True


class TransactionRequest(BaseModel):
    customer_number: str
