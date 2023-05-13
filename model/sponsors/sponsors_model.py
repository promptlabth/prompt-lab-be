from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import date
class Sponsors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    ads_image: str
    ads_start_date: date
    ads_end_date: date
    sponsor_type: Optional[int] = Field(default=None, foreign_key="sponsortypes.id")
