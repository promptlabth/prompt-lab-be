from typing import Optional, TYPE_CHECKING, List
from sqlmodel import Field, Session, SQLModel, Relationship
from datetime import datetime
if TYPE_CHECKING:
    from model.sponsortypes.sponsortypes_model import SponsorTypes
    from model.users_sponser_select.users_sponsor_select_model import Usersponsorselects
class Sponsors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    ads_image: str
    ads_start_date: datetime
    ads_end_date: datetime

    sponsor_types_id: Optional[int] = Field(default=None, foreign_key="sponsortypes.id")
    sponsor_type: Optional["SponsorTypes"] = Relationship(back_populates="sponsors")

    usersponsorselects: List["Usersponsorselects"] = Relationship(back_populates="sponsor")

