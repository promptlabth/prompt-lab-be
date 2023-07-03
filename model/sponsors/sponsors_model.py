from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Session, SQLModel, Relationship
from datetime import datetime
if TYPE_CHECKING:
    from model.sponsortypes.sponsortypes_model import Sponsortypes
class Sponsors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    ads_image: str
    ads_start_date: datetime
    ads_end_date: datetime
    sponsor_types_id: Optional[int] = Field(default=None, foreign_key="sponsor_types_id")
    sponsor_type: Optional["Sponsortypes"] = Relationship(back_populates="sponsor_types")

