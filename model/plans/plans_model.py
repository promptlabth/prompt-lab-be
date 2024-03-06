from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from model.users.users_model import Users

class Plans(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    planType: str
    maxMessages: int
    product_id: Optional[str] = Field()

    # 1 Plan have mamy Users
    users: List["Users"] = Relationship(back_populates="plan")
