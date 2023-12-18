import stripe
from stripe import Subscription
import os

from datetime import datetime

from schemas.pydantic.stripeServiceSchema import StartEndPlan

class StripeService:
    
    def __init__(self) -> None:
        stripe.api_key = os.getenv("STRIPE_KEY")
    
    def getSubscriptionByCusId(self, cusId: str) -> Subscription:
        subscription = stripe.Subscription.list(
            customer=cusId, 
            status="active",
        )
        return subscription.data[0]
    
    def get_start_end_date(self, stripe_id: str) -> StartEndPlan:
        subscription = self.getSubscriptionByCusId(stripe_id)
        return StartEndPlan(
            start_date=datetime.fromtimestamp(subscription["current_period_start"]),
            end_date=datetime.fromtimestamp(subscription["current_period_end"])
        )