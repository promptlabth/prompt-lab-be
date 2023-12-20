from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from model.promptMessages.prompt_messages_model import Promptmessages
    from model.inputPrompts.input_prompt_model import InputPrompts

class Models(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_name: str

    # 1 model have many prompt message
    promptmessages: List["Promptmessages"] = Relationship(back_populates="model")

    # 1 model have many input prompts
    inputPrompts: List["InputPrompts"] = Relationship(back_populates="model")