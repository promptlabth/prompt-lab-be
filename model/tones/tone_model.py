from sqlmodel import Field, SQLModel, Relationship
from typing import Optional,List, TYPE_CHECKING
if TYPE_CHECKING:
    from model.promptMessages import prompt_messages_model

class Tones(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tone_name: str
    language_id: Optional[int] = Field(default=None, foreign_key="languages.id")
    language: Optional[language] = Relationship(back_populates="tones")
    promptmessages: List["prompt_messages_model.Promptmessages"] = Relationship(back_populates="tone")

