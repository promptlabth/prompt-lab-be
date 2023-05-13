from sqlmodel import Field, SQLModel
from typing import Optional

class Promptrows(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    prev_prompt : Optional[int] = Field(default=None, foreign_key="promptmessages.id")
    row_number: int