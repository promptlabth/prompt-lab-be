from typing import Optional, List
from sqlmodel import Field, Session, SQLModel, Relationship
from datetime import datetime
class Usersponsorselects(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sponsor_id: Optional[int] = Field(default=None, foreign_key="sponsors.id")
    date_time: datetime
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    users: Optional[users] = Relationship(back_populates="usersponsorselects")