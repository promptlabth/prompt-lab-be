from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from model.users.users_model import Users
    from model.tones.tone_model import Tones
    from model.features.features_model import Features
    from model.promptRows.prompt_row_model import Promptrows


class Promptmessages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date_time: datetime
    input_message:str
    result_message: str

    # Relationship
    user_id : Optional[int] = Field(default=None, foreign_key="users.id")
    # 1 promptmessage have 1 user
    user: Optional["Users"] = Relationship(back_populates="promptmessages")

    tone_id : Optional[int] = Field(default=None, foreign_key="tones.id")
    # 1 promptmessage have 1 tone
    tone: Optional["Tones"] = Relationship(back_populates="promptmessages")


    feature_id : Optional[int] = Field(default=None, foreign_key="features.id")
    # 1 promptmessage have 1 feature
    feature: Optional["Features"] = Relationship(back_populates="promptmessages")
 
    # 1 promptmessage have many promptrows
    promptrows: List["Promptrows"] = Relationship(back_populates="prev_prompt")

