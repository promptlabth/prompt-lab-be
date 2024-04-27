from sqlmodel import Field, SQLModel, Relationship
from typing import Optional,List, TYPE_CHECKING
if TYPE_CHECKING:
    from app.model.promptMessages.prompt_messages_model import Promptmessages
    from app.model.languages.languages_model import Languages

class Tones(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tone_name: str

    # Relation 
    # 1 Tone have 1 Language
    language_id: Optional[int] = Field(default=None, foreign_key="languages.id")
    language: Optional["Languages"] = Relationship(back_populates="tones")
    
    # 1 Tone have many PromptMessages
    promptmessages: List["Promptmessages"] = Relationship(back_populates="tone")
