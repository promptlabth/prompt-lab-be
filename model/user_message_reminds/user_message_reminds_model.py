from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship, Column, String

if TYPE_CHECKING:
    from model.users.users_model import Users

class UserMessageReminds(SQLModel, table=True):
    __tablename__ = "user_message_reminds"

    firebase_id: str = Field(primary_key=True, foreign_key="users.firebase_id")
    user: Optional["Users"] = Relationship(back_populates="user_message_reminds")
    
    message_reminded: int = Field(nullable=False, sa_column=Column("message_reminded"))
    