from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from model.users.users_model import Users
    from model.plans.plans_model import Plans

class Subscriptions_Payments(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    subscription_id : str
    start_datetime: datetime
    end_datetime: datetime
    subscription_status: str
    datetime: datetime

    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    # 1 payment subscription have 1 user
    user: Optional["Users"] = Relationship(back_populates="subscriptions_payments")

    plan_id: Optional[int] = Field(default=None, foreign_key="plans.id")
    # 1 subscription payment have 1 plan
    plan: Optional["Plans"] = Relationship(back_populates="subscriptions_payments")
    