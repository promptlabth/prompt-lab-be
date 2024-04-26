from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
if TYPE_CHECKING:
    from model.promptMessages.prompt_messages_model import Promptmessages
    from model.users_sponser_select.users_sponsor_select_model import Usersponsorselects
    from model.featureusings.feature_usings_model import Featureusings
    from model.coins.coins_model import Coins
    from model.plans.plans_model import Plans
    from model.user_message_reminds.user_message_reminds_model import UserMessageReminds

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firebase_id : Optional[str] = Field(default=None, unique=True)
    name: Optional[str] = Field(nullable=True)
    email: Optional[str] = Field(nullable=True)
    profilepic: Optional[str] = Field(nullable=True)
    platform: Optional[str] = Field(nullable=True)
    access_token: Optional[str] = Field(nullable=True)

    stripe_id: Optional[str] = Field(nullable=True)

    plan_id: Optional[int] = Field(default=None, foreign_key="plans.id")
    # 1 User has 1 plan
    plan: Optional["Plans"] = Relationship(back_populates="users")

    # 1 User has one coin
    coins: Optional["Coins"] = Relationship(back_populates="user")

    # 1 User have many promptmessages
    promptmessages: List["Promptmessages"] = Relationship(back_populates="user")
    # 1 USER have many feature usings
    featureusings: List["Featureusings"] = Relationship(back_populates="user")
    # 1 User have many UserSponsorselects
    usersponsorselects: List["Usersponsorselects"] = Relationship(back_populates="user")
    
    # 1 User have 1 UserMessageReminds
    user_message_reminds: Optional["UserMessageReminds"] = Relationship(back_populates="user")

