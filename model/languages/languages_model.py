from sqlmodel import Field, SQLModel
from typing import Optional

class Languages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    language_name: Optional[str] = Field(default=None, unique=True)