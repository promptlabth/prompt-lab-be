from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from model.sponsors import sponsors_model
class Sponsortypes( SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    sponsors: List["sponsors_model.Sponsors"] = Relationship(back_populates="sponsor")
