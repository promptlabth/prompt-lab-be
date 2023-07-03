from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import datetime
class Sponsors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    ads_image: str
    ads_start_date: datetime
    ads_end_date: datetime
    sponsor_type: Optional[int] = Field(default=None, foreign_key="sponsortypes.id")
    
