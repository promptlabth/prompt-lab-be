from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship, Column, String

if TYPE_CHECKING:
    from app.model.users.users_model import Users

class UserMessageBalance(SQLModel, table=True):
    __tablename__ = "user_balance_messages"

    firebase_id: str = Field(primary_key=True, foreign_key="users.firebase_id")
    user: Optional["Users"] = Relationship(back_populates="user_balance_messages")
    
    balance_message: int = Field(nullable=False, sa_column=Column("balance_message"))
    