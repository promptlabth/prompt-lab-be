from sqlmodel import Field, SQLModel
from typing import Optional

class Tones(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tone_name: str
    language_id: Optional[int] = Field(default=None, foreign_key="languages.id")