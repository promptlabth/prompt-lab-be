from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from model.promptMessages import prompt_messages_model
from model.users_sponser_select import users_sponsor_select_model
from model.featureusings import feature_usings_model
class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firebase_id : Optional[str] = Field(default=None, unique=True)
    name: Optional[str] = None
    email: str
    profilepic: str
    promptmessages: List["prompt_messages_model.Promptmessages"] = Relationship(back_populates="user")
    featureusings: List["feature_usings_model.Featureusings"] = Relationship(back_populates="user")
    usersponsorselects: List["users_sponsor_select_model.Usersponsorselects"] = Relationship(back_populates="user")

