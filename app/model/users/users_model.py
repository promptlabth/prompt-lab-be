from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
if TYPE_CHECKING:
    from app.model.promptMessages.prompt_messages_model import Promptmessages
    from app.model.plans.plans_model import Plans
    from app.model.user_balance_messages.user_balance_messages_model import UserMessageBalance

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firebase_id : Optional[str] = Field(default=None, unique=True)
    name: Optional[str] = Field(nullable=True)
    email: Optional[str] = Field(nullable=True)
    profilepic: Optional[str] = Field(nullable=True)
    platform: Optional[str] = Field(nullable=True)
    access_token: Optional[str] = Field(nullable=True)

    stripe_id: Optional[str] = Field(nullable=True)

    plan_id: Optional[int] = Field(default=None, foreign_key="plans.id")
    # 1 User has 1 plan
    plan: Optional["Plans"] = Relationship(back_populates="users")

    # 1 User have many promptmessages
    promptmessages: List["Promptmessages"] = Relationship(back_populates="user")

    # 1 User have 1 UserMessageBalance
    balance_message: Optional["UserMessageBalance"] = Relationship(back_populates="user")

