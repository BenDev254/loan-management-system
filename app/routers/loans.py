from schemas.subscriptions import SubscriptionRequest, SubscriptionResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import LoanRequest, LoanResponse
from crud.loans import create_loan, create_subscription, get_loan_status

router = APIRouter()

@router.post("/loan/request", response_model=LoanResponse)
def request_loan(loan_request: LoanRequest, db: Session = Depends(get_db)):
    loan = create_loan(db, loan_request)
    if not loan:
        raise HTTPException(status_code=400, detail="Existing pending loan found")

    return LoanResponse(customer_id=loan.customer_id, amount=loan.amount, status=loan.status)

@router.get("/loan/status/{customer_id}", response_model=LoanResponse)
def loan_status(customer_id: str, db: Session = Depends(get_db)):
    loan = get_loan_status(db, customer_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    return LoanResponse(customer_id=loan.customer_id, amount=loan.amount, status=loan.status)


@router.post("/loans", response_model=LoanResponse)
def apply_for_loan(loan_request: LoanRequest, db: Session = Depends(get_db)):
    try:
        loan = create_loan(db, loan_request)
        return loan
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.post("/subscribe", response_model=SubscriptionResponse)
def subscribe_customer(subscription_data: SubscriptionRequest, db: Session = Depends(get_db)):
    """
    Registers a new customer for loan services.
    """
    customer = create_subscription(db, subscription_data)
    if not customer:
        raise HTTPException(status_code=400, detail="Subscription failed")
    return customer