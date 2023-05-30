from sqlmodel import Field, SQLModel
from typing import Optional

class Languages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    language_name: str