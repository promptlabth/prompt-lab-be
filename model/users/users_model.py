from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = None
    email: str
    profilepic: str