from sqlalchemy.orm import Session
from models import Subscription
from schemas.subscriptions import SubscriptionRequest, SubscriptionResponse

def create_subscription(db: Session, request: SubscriptionRequest) -> SubscriptionResponse:
    subscription = Subscription(
        customer_number=request.customer_number,
        service_type=request.service_type
    )
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return SubscriptionResponse(
        id=subscription.id,
        customer_number=subscription.customer_number,
        name=subscription.name,
        email=subscription.email,
        service_type=subscription.service_type,
        status=subscription.status
    )

def get_subscription(db: Session, customer_number: str):
    return db.query(Subscription).filter(Subscription.customer_number == customer_number).first()

