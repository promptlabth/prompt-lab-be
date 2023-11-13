from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from model.users.users_model import Users

class Coins(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: int
    
    # Relationship
    user_id : Optional[int] = Field(default=None, foreign_key="users.id")
    # 1 coin have 1 user
    user: Optional["Users"] = Relationship(back_populates="coins")