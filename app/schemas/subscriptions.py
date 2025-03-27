
import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class SubscriptionBase(BaseModel):
    customer_number: Optional[str]
    name: Optional[str]
    email: Optional[EmailStr]
    service_type: Optional[str]
    status: Optional[str] = "active"
    created_at: Optional[datetime.datetime] = None

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionRequest(BaseModel):  
    customer_number: str
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    service_type: str

class SubscriptionResponse(SubscriptionBase):
    id: int
    customer_number: str
    name: Optional[str]
    email: Optional[EmailStr]
    service_type: str
    status: str = "active"
    created_at: datetime

    class Config:
        from_attributes = True
