from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    pass

class Plans(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    planType: str
    maxMessages: int

    
    

