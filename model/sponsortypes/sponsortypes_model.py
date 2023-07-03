from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
if TYPE_CHECKING:
    from model.sponsors.sponsors_model import Sponsors

class Sponsortypes( SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    sponsors: List["Sponsors"] = Relationship(back_populates="sponsor_type")
