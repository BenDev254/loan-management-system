from pydantic import BaseModel
from typing import Optional

class ScoreQueryRequest(BaseModel):
    customer_id: int  # This should now match User.id
    request_type: str  # e.g., "credit_score"

class ScoreQueryResponse(BaseModel):
    customer_id: int
    score: Optional[int]
    status: str  # "Success" or "Failed"