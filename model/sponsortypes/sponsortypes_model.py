from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

class Sponsortypes( SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str