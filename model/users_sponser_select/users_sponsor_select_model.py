from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Session, SQLModel, Relationship
from datetime import datetime

if TYPE_CHECKING:
    from model.users.users_model import Users
    from model.sponsors.sponsors_model import Sponsors

class Usersponsorselects(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date_time: datetime

    sponsor_id: Optional[int] = Field(default=None, foreign_key="sponsors.id")
    sponsor: Optional[Sponsors] = Relationship(back_populates="usersponsorselects")
    
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    user: Optional[Users] = Relationship(back_populates="usersponsorselects")