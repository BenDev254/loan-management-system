from sqlalchemy.orm import Session
from app.schemas.subscriptions import SubscriptionRequest, SubscriptionResponse
from models import Loan
from models import Subscription
from schemas.loans import LoanCreate
from fastapi import HTTPException


def create_loan(db: Session, loan_data: LoanCreate):
    try:
        loan = Loan(**loan_data.dict())
        db.add(loan)
        db.commit()
        db.refresh(loan)
        return loan
    except Exception as e:
        db.rollback() #Rollback on failure
        raise HTTPException(status_code=500, detail="Loan creation failed")
    
    
def create_subscription(db: Session, subscription_data: SubscriptionRequest):
    """
    Creates a new customer subscription for loan services.
    """
    new_subscription = Subscription(
        customer_number=subscription_data.customer_number,
        name=subscription_data.name,
        email=subscription_data.email
    )
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)

    return SubscriptionResponse(
        customer_number=new_subscription.customer_number,
        message="Subscription successful"
    )


def get_loan_status(db: Session, loan_id: int):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    return loan