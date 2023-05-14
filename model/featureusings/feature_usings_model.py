from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import date,time
class Featureusings(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    feature_id: Optional[int] = Field(default=None, foreign_key="features.id")
    dates: date
    timestart:time
    timestop:time
