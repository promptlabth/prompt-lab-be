from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Session, SQLModel, create_engine, Relationship
from datetime import date

if TYPE_CHECKING:
    from model.featureusings.feature_usings_model import Featureusings
    from model.promptMessages.prompt_messages_model import Promptmessages
class Features(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    date_of_create: date
    url: str

    # 1 feature have many featureusings
    featureusings: List["Featureusings"] = Relationship(back_populates="feature")

    # 1 feature have many promptmessage
    promptmessages: List["Promptmessages"] = Relationship(back_populates="feature")