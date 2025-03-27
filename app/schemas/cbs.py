
from pydantic import BaseModel
from typing import List, Optional

class KYCRequest(BaseModel):
    customer_number: str

class KYCResponse(BaseModel):
    customer_number: str
    name: str
    dob: str
    id_number: Optional[str] = None

class TransactionRequest(BaseModel):
    customer_number: str

class TransactionDetail(BaseModel):
    transaction_id: str
    amount: float
    date: str
    type: str  # Credit/Debit

class TransactionResponse(BaseModel):
    customer_number: str
    transactions: List[TransactionDetail]
