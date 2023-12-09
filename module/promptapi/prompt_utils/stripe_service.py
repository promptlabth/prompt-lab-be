import stripe
import os

def GetSubscriptionByCusId(cusId):
    stripe.api_key = os.getenv("STRIPE_KEY")
    subscription = stripe.Subscription.list(customer=cusId)
    return subscription.data[0]