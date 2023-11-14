from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class SubscriptionsPayments(SQLModel, table=True):
    __tablename__ = "subscriptions_payments"

    id: Optional[int] = Field(default=None, primary_key=True)
    transaction_stripe_id: Optional[str] = Field(default=None)
    datetime: datetime
    start_datetime: Optional[datetime] = Field(default=None)
    end_datetime: Optional[datetime] = Field(default=None)
    subscription_status: Optional[str] = Field(default=None)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    payment_method_id: Optional[str]
    plan_id: Optional[int] = Field(default=None, foreign_key="plans.id")

    # Additional fields for relationships can be added if needed
