from sqlmodel import Field, SQLModel, Relationship
from typing import Optional,List
from model.tones import tone_model
class Languages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    language_name: Optional[str] = Field(default=None, unique=True)
    tones: List["tone_model.Tones"] = Relationship(back_populates="language")