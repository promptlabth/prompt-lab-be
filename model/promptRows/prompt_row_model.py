from sqlmodel import Field, SQLModel
from typing import Optional

class Promptrows(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    row_number: int
    
    prev_prompt_id : Optional[int] = Field(default=None, foreign_key="promptmessages.id")