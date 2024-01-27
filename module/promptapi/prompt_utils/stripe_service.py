import stripe
from stripe import Subscription
import os

def GetSubscriptionByCusId(cusId):
    stripe.api_key = os.getenv("STRIPE_KEY")
    subscription = stripe.Subscription.list(customer=cusId, status="active")
    return subscription.data[0]

class StripeService:
    
    def __init__(self) -> None:
        stripe.api_key = os.getenv("STRIPE_KEY")
    
    def getSubscriptionByCusId(cusId: str) -> Subscription:
        subscription = stripe.Subscription.list(
            customer=cusId, 
            status="active",
        )
        return subscription.data[0]