from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class Promptmessages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id : Optional[int] = Field(default=None, foreign_key="users.id")
    tone_id : Optional[int] = Field(default=None, foreign_key="tones.id")
    date_time: datetime
    feature_id : Optional[int] = Field(default=None, foreign_key="features.id")
    input_message:str
    result_message: str