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
        try:
            subscription_data = subscription.data[0]
        except:
            subscription_data = None
        return subscription_data
    
    def get_start_end_date(self, stripe_id: str) -> StartEndPlan:
        subscription = self.getSubscriptionByCusId(stripe_id)
        if subscription is None:
            return StartEndPlan(
                start_date=None,
                end_date=None
            )
        return StartEndPlan(
            start_date=datetime.fromtimestamp(subscription["current_period_start"]),
            end_date=datetime.fromtimestamp(subscription["current_period_end"])
        )