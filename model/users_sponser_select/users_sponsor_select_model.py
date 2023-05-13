from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import date
class Usersponsorselects(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sponsor_id: Optional[int] = Field(default=None, foreign_key="sponsors.id")
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    date_time: date