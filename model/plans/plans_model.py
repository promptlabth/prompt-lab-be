from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from model.subscriptions_payments.subscriptions_payments_model import Subscriptions_Payments

class Plans(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    planType: str
    maxMessages: int
    product_id: str

    # 1 Plan have many subscriptions payments
    subscriptions_payments: List["Subscriptions_Payments"] = Relationship(back_populates="plan")