from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
if TYPE_CHECKING:
    from model.promptMessages.prompt_messages_model import Promptmessages
    from model.users_sponser_select.users_sponsor_select_model import Usersponsorselects
    from model.featureusings.feature_usings_model import Featureusings

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firebase_id : Optional[str] = Field(default=None, unique=True)
    name: Optional[str] = None
    email: str
    profilepic: str

    # 1 User have many promptmessages
    promptmessages: List["Promptmessages"] = Relationship(back_populates="user")
    # 1 USER have many feature usings
    featureusings: List["Featureusings"] = Relationship(back_populates="user")
    usersponsorselects: List["Usersponsorselects"] = Relationship(back_populates="user")


