from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import date
class Features(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    date_of_create: date
    url: str