from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import TransactionDataSchema
from models import TransactionData

router = APIRouter()

@router.get("/transactions/{customer_id}", response_model=list[TransactionDataSchema])
def get_transactions(customer_id: str, db: Session = Depends(get_db)):
    transactions = db.query(TransactionData).filter(TransactionData.customer_id == customer_id).all()
    return transactions
