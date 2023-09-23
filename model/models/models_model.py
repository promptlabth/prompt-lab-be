from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from model.promptMessages.prompt_messages_model import Promptmessages

class Models(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_name: str

    promptmessages: List["Promptmessages"] = Relationship(back_populates="model")