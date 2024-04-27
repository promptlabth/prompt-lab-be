from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from datetime import date

if TYPE_CHECKING:
    from app.model.promptMessages.prompt_messages_model import Promptmessages
    from app.model.inputPrompts.input_prompt_model import InputPrompts
class Features(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    date_of_create: date
    url: str


    # 1 feature have many promptmessage
    promptmessages: List["Promptmessages"] = Relationship(back_populates="feature")

    # 1 feature have many input_prompt
    input_prompts: List["InputPrompts"] = Relationship(back_populates="feature")